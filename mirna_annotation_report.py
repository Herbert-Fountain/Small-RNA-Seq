#!/usr/bin/env python3
"""
miRNA Biomarker Annotation Report
===================================
Reads miRNAs from biomarker_summary_tables.csv, then queries:
  - TargetScan Mouse 8.0 for predicted gene targets
  - NCBI Gene for top target gene function
  - NCBI PubMed for relevant publications with DOIs
Generates a Markdown report with biological context and citations.
"""

import pandas as pd
import numpy as np
import requests
import time
import os
import io
import zipfile
import sys

RESULTS_DIR = "results"
SUMMARY_CSV = os.path.join(RESULTS_DIR, "biomarker_summary_tables.csv")
OUTPUT_MD = os.path.join(RESULTS_DIR, "mirna_annotation_report.md")
NCBI_EMAIL = "herbert.fountain@cornell.edu"
NCBI_TOOL = "mirna_biomarker_annotation"
TARGETSCAN_URL = "https://www.targetscan.org/mmu_80/mmu_80_data_download/Summary_Counts.default_predictions.txt.zip"
TARGETSCAN_CACHE = "targetscan_summary_counts.txt"
NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def load_biomarkers(filepath):
    df = pd.read_csv(filepath)
    return df[['Group', 'Direction', 'miRNA', 'GeneID', 'log2FC', 'padj',
               'biomarker_score']].copy()


def download_targetscan():
    if os.path.exists(TARGETSCAN_CACHE):
        print(f"  Using cached TargetScan data: {TARGETSCAN_CACHE}")
        return pd.read_csv(TARGETSCAN_CACHE, sep='\t', low_memory=False)
    print("  Downloading TargetScan data...")
    resp = requests.get(TARGETSCAN_URL, timeout=120)
    resp.raise_for_status()
    with zipfile.ZipFile(io.BytesIO(resp.content)) as zf:
        txt_names = [n for n in zf.namelist() if n.endswith('.txt')]
        with zf.open(txt_names[0]) as f:
            data = f.read().decode('utf-8', errors='replace')
    with open(TARGETSCAN_CACHE, 'w') as f:
        f.write(data)
    return pd.read_csv(io.StringIO(data), sep='\t', low_memory=False)


def get_targetscan_targets(ts_df, mirna_id):
    if ts_df.empty:
        return 0, pd.DataFrame()
    mask = (ts_df['Species ID'] == 10090) & \
           (ts_df['Representative miRNA'].astype(str) == mirna_id)
    matches = ts_df[mask]
    if len(matches) == 0:
        seed_mask = ts_df['Representative miRNA'].astype(str).str.contains(
            mirna_id.replace('mmu-', ''), case=False, na=False)
        seed_matches = ts_df[seed_mask]
        if len(seed_matches) > 0:
            seed = seed_matches.iloc[0]['miRNA family']
            mask = (ts_df['miRNA family'] == seed) & (ts_df['Species ID'] == 10090)
            matches = ts_df[mask]
    if len(matches) == 0:
        return 0, pd.DataFrame()
    n_targets = matches['Gene Symbol'].nunique()
    score_col = 'Cumulative weighted context++ score'
    matches = matches.copy()
    matches[score_col] = pd.to_numeric(matches[score_col], errors='coerce')
    top = matches.nsmallest(10, score_col)
    display_cols = ['Gene Symbol', 'Total num conserved sites', score_col]
    display_cols = [c for c in display_cols if c in top.columns]
    return n_targets, top[display_cols]


def ncbi_request(endpoint, params, retries=3):
    params['tool'] = NCBI_TOOL
    params['email'] = NCBI_EMAIL
    url = f"{NCBI_BASE}/{endpoint}"
    for attempt in range(retries):
        try:
            resp = requests.get(url, params=params, timeout=30)
            resp.raise_for_status()
            time.sleep(0.35)
            return resp
        except requests.RequestException as e:
            if attempt < retries - 1:
                time.sleep(2)
            else:
                print(f"    WARNING: NCBI request failed: {e}")
                return None


def get_gene_summary(gene_symbol):
    resp = ncbi_request('esearch.fcgi', {
        'db': 'gene',
        'term': f'{gene_symbol}[Gene Name] AND Mus musculus[Organism]',
        'retmode': 'json', 'retmax': 1,
    })
    if not resp:
        return None
    ids = resp.json().get('esearchresult', {}).get('idlist', [])
    if not ids:
        return None
    resp = ncbi_request('esummary.fcgi', {
        'db': 'gene', 'id': ids[0], 'retmode': 'json',
    })
    if not resp:
        return None
    info = resp.json().get('result', {}).get(ids[0], {})
    return {
        'gene_id': ids[0],
        'symbol': info.get('name', gene_symbol),
        'full_name': info.get('description', ''),
        'summary': info.get('summary', 'No summary available.'),
    }


def search_pubmed(mirna_id, max_results=5):
    name = mirna_id.replace('mmu-', '')
    query = (f'("{name}"[Title/Abstract] OR "{mirna_id}"[Title/Abstract])'
             f' AND (function OR target OR role OR pathway)')
    resp = ncbi_request('esearch.fcgi', {
        'db': 'pubmed', 'term': query,
        'retmax': max_results, 'retmode': 'json', 'sort': 'relevance',
    })
    if not resp:
        return []
    ids = resp.json().get('esearchresult', {}).get('idlist', [])
    if not ids:
        resp = ncbi_request('esearch.fcgi', {
            'db': 'pubmed', 'term': f'"{name}"[Title/Abstract]',
            'retmax': max_results, 'retmode': 'json', 'sort': 'relevance',
        })
        if not resp:
            return []
        ids = resp.json().get('esearchresult', {}).get('idlist', [])
    if not ids:
        return []
    resp = ncbi_request('esummary.fcgi', {
        'db': 'pubmed', 'id': ','.join(ids), 'retmode': 'json',
    })
    if not resp:
        return []
    results = resp.json().get('result', {})
    articles = []
    for pmid in ids:
        art = results.get(pmid, {})
        if not art or 'error' in art:
            continue
        doi = ''
        for aid in art.get('articleids', []):
            if aid.get('idtype') == 'doi':
                doi = aid.get('value', '')
                break
        authors = art.get('authors', [])
        first = authors[0].get('name', 'Unknown') if authors else 'Unknown'
        author_str = f"{first} et al." if len(authors) > 1 else first
        articles.append({
            'pmid': pmid, 'title': art.get('title', 'No title'),
            'authors': author_str, 'journal': art.get('source', ''),
            'year': art.get('pubdate', '').split()[0] if art.get('pubdate') else '',
            'doi': doi,
        })
    return articles


def generate_report(mirnas_df, ts_df, output_path):
    unique_mirnas = mirnas_df['GeneID'].unique()
    print(f"\nAnnotating {len(unique_mirnas)} unique miRNAs...")
    lines = []
    lines.append("# miRNA Biomarker Annotation Report\n\n")
    lines.append("Automated annotation of biomarker miRNA candidates using "
                 "TargetScan Mouse 8.0, NCBI Gene, and PubMed.\n\n---\n\n")

    for i, gene_id in enumerate(unique_mirnas):
        mirna_name = gene_id.replace('mmu-', '')
        print(f"\n[{i+1}/{len(unique_mirnas)}] Processing {mirna_name}...")
        mirna_rows = mirnas_df[mirnas_df['GeneID'] == gene_id]

        lines.append(f"## {mirna_name}\n\n")
        lines.append("### Biomarker Context\n\n")
        lines.append("| Group | Direction | log2FC | FDR | Biomarker Score |\n")
        lines.append("|-------|-----------|--------|-----|----------------|\n")
        for _, row in mirna_rows.iterrows():
            lines.append(f"| {row['Group']} | {row['Direction']} | "
                         f"{row['log2FC']:+.2f} | {row['padj']:.2e} | "
                         f"{row['biomarker_score']:.1f} |\n")
        lines.append("\n")

        # TargetScan
        print("  Querying TargetScan...")
        n_targets, top_targets = get_targetscan_targets(ts_df, gene_id)
        lines.append("### Predicted Gene Targets (TargetScan Mouse 8.0)\n\n")
        if n_targets > 0:
            lines.append(f"**Total predicted target genes: {n_targets}**\n\n")
            if len(top_targets) > 0 and 'Gene Symbol' in top_targets.columns:
                top_gene = str(top_targets.iloc[0]['Gene Symbol'])
                lines.append("**Top 10 predicted targets (by weighted context++ score):**\n\n")
                lines.append("| " + " | ".join(top_targets.columns) + " |\n")
                lines.append("| " + " | ".join(['---'] * len(top_targets.columns)) + " |\n")
                for _, row in top_targets.iterrows():
                    vals = [str(row[c]) for c in top_targets.columns]
                    lines.append("| " + " | ".join(vals) + " |\n")
                lines.append("\n")

                print(f"  Looking up top target gene: {top_gene}...")
                gene_info = get_gene_summary(top_gene)
                if gene_info:
                    lines.append(f"**Top target gene: {gene_info['symbol']}** "
                                 f"({gene_info['full_name']})\n\n")
                    summary = gene_info['summary']
                    if len(summary) > 500:
                        summary = summary[:500] + '...'
                    lines.append(f"*Function:* {summary}\n\n")
                    lines.append(f"*NCBI Gene ID:* [{gene_info['gene_id']}]"
                                 f"(https://www.ncbi.nlm.nih.gov/gene/"
                                 f"{gene_info['gene_id']})\n\n")
        else:
            lines.append("No predicted targets found in TargetScan Mouse 8.0 "
                         "conserved predictions.\n\n")

        # PubMed
        print("  Searching PubMed...")
        articles = search_pubmed(gene_id, max_results=5)
        lines.append("### Literature\n\n")
        if articles:
            for j, art in enumerate(articles, 1):
                doi_link = ""
                if art['doi']:
                    doi_link = (f" DOI: [{art['doi']}]"
                                f"(https://doi.org/{art['doi']})")
                lines.append(
                    f"{j}. {art['authors']} ({art['year']}). "
                    f"*{art['title']}* {art['journal']}.{doi_link} "
                    f"PMID: [{art['pmid']}]"
                    f"(https://pubmed.ncbi.nlm.nih.gov/{art['pmid']}/)\n\n")
        else:
            lines.append("No relevant publications found in PubMed.\n\n")
        lines.append("---\n\n")

    lines.append("## Data Sources\n\n")
    lines.append("- **TargetScan Mouse 8.0**: Agarwal V, Bell GW, Nam JW, Bartel DP. "
                 "Predicting effective microRNA target sites in mammalian mRNAs. "
                 "*eLife*. 2015;4:e05005. DOI: [10.7554/eLife.05005]"
                 "(https://doi.org/10.7554/eLife.05005)\n\n")
    lines.append("- **miRBase**: Kozomara A, Birgaoanu M, Griffiths-Jones S. "
                 "miRBase: from microRNA sequences to function. "
                 "*Nucleic Acids Research*. 2019;47(D1):D155-D162. "
                 "DOI: [10.1093/nar/gky1141](https://doi.org/10.1093/nar/gky1141)\n\n")
    lines.append("- **NCBI PubMed/Gene**: National Center for Biotechnology Information. "
                 "https://www.ncbi.nlm.nih.gov/\n\n")

    report = ''.join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    return report


def main():
    print("=" * 60)
    print("miRNA Biomarker Annotation Report")
    print("=" * 60)

    print(f"\n[1/4] Loading biomarker summary from {SUMMARY_CSV}...")
    if not os.path.exists(SUMMARY_CSV):
        print(f"ERROR: {SUMMARY_CSV} not found.")
        sys.exit(1)
    mirnas_df = load_biomarkers(SUMMARY_CSV)
    print(f"  Found {len(mirnas_df)} entries, "
          f"{mirnas_df['GeneID'].nunique()} unique miRNAs")

    print(f"\n[2/4] Loading TargetScan Mouse 8.0 predictions...")
    try:
        ts_df = download_targetscan()
        print(f"  Loaded {len(ts_df)} target predictions")
    except Exception as e:
        print(f"  WARNING: Could not load TargetScan data: {e}")
        ts_df = pd.DataFrame()

    print(f"\n[3/4] Generating annotation report...")
    report = generate_report(mirnas_df, ts_df, OUTPUT_MD)

    print(f"\n[4/4] Report saved to {OUTPUT_MD}")
    print(f"  Report length: {len(report):,} characters")
    print("\n" + "=" * 60)
    print("ANNOTATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
