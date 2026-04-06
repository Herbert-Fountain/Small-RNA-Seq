#!/usr/bin/env python3
"""
miRNA Biomarker Annotation Report
===================================
Reads miRNAs from biomarker_summary_tables.csv, then:
  - TargetScan Mouse 8.0 for predicted gene targets (with seed family fallback)
  - NCBI Gene for top target gene function
  - NCBI PubMed for relevant publications with DOIs
  - miRBase mature.fa for mouse-human ortholog sequence comparison
Generates a Markdown report with biological context and citations.
"""

import pandas as pd
import numpy as np
import requests
import time
import os
import io
import zipfile
import re
import sys

RESULTS_DIR = "results"
SUMMARY_CSV = os.path.join(RESULTS_DIR, "biomarker_summary_tables.csv")
OUTPUT_MD = os.path.join(RESULTS_DIR, "mirna_annotation_report.md")
NCBI_EMAIL = "herbert.fountain@cornell.edu"
NCBI_TOOL = "mirna_biomarker_annotation"
TARGETSCAN_URL = "https://www.targetscan.org/mmu_80/mmu_80_data_download/Summary_Counts.default_predictions.txt.zip"
TARGETSCAN_CACHE = "targetscan_summary_counts.txt"
MIRBASE_FA = "mature.fa"
MIRBASE_URL = "https://www.mirbase.org/download/mature.fa"
NCBI_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


# ---------------------------------------------------------------------------
# miRBase sequence loading
# ---------------------------------------------------------------------------
def load_mirbase_sequences(filepath=MIRBASE_FA):
    """Parse miRBase mature.fa into a dict of {name: sequence}."""
    if not os.path.exists(filepath):
        print(f"  Downloading miRBase mature sequences...")
        resp = requests.get(MIRBASE_URL, timeout=60)
        resp.raise_for_status()
        with open(filepath, 'w') as f:
            f.write(resp.text)

    seqs = {}
    name = None
    seq_lines = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if name:
                    seqs[name] = ''.join(seq_lines).upper()
                parts = line[1:].split()
                name = parts[0]
                seq_lines = []
            else:
                seq_lines.append(line)
    if name:
        seqs[name] = ''.join(seq_lines).upper()
    return seqs


def find_human_ortholog(mmu_name, mirbase_seqs):
    """
    Find the human ortholog for a mouse miRNA and compare sequences.
    Returns dict with ortholog info or None.
    """
    # Get mouse sequence
    mmu_seq = mirbase_seqs.get(mmu_name)
    if not mmu_seq:
        return None

    # Derive expected human name: mmu-miR-xxx -> hsa-miR-xxx
    hsa_name = mmu_name.replace('mmu-', 'hsa-')
    hsa_seq = mirbase_seqs.get(hsa_name)

    # If exact name match fails, try variations
    if not hsa_seq:
        # Some miRNAs have species-specific numbering (e.g., mmu-miR-1a-3p -> hsa-miR-1-3p)
        # Try removing the letter suffix
        alt_name = re.sub(r'(miR-\d+)[a-z](-)', r'\1\2', hsa_name)
        if alt_name != hsa_name:
            hsa_seq = mirbase_seqs.get(alt_name)
            if hsa_seq:
                hsa_name = alt_name

    if not hsa_seq:
        # Try searching all human miRNAs for same base name
        base = re.sub(r'^mmu-', '', mmu_name)
        base = re.sub(r'[a-z](-[35]p)$', r'\1', base)  # miR-1a-3p -> miR-1-3p
        candidates = []
        for k, v in mirbase_seqs.items():
            if k.startswith('hsa-') and base.lower() in k.lower():
                candidates.append((k, v))
        if candidates:
            # Pick the closest name match
            hsa_name, hsa_seq = candidates[0]

    if not hsa_seq:
        return {'found': False, 'mmu_name': mmu_name, 'mmu_seq': mmu_seq}

    # Compare sequences
    identical = (mmu_seq == hsa_seq)
    if identical:
        return {
            'found': True, 'identical': True,
            'mmu_name': mmu_name, 'hsa_name': hsa_name,
            'mmu_seq': mmu_seq, 'hsa_seq': hsa_seq,
            'length': len(mmu_seq),
        }

    # Compute alignment details
    max_len = max(len(mmu_seq), len(hsa_seq))
    min_len = min(len(mmu_seq), len(hsa_seq))
    mismatches = []
    match_count = 0
    for pos in range(min_len):
        if mmu_seq[pos] == hsa_seq[pos]:
            match_count += 1
        else:
            mismatches.append({
                'position': pos + 1,
                'mouse': mmu_seq[pos],
                'human': hsa_seq[pos],
            })

    # Count length difference as additional mismatches
    length_diff = abs(len(mmu_seq) - len(hsa_seq))
    pct_identity = (match_count / max_len) * 100 if max_len > 0 else 0

    return {
        'found': True, 'identical': False,
        'mmu_name': mmu_name, 'hsa_name': hsa_name,
        'mmu_seq': mmu_seq, 'hsa_seq': hsa_seq,
        'mmu_len': len(mmu_seq), 'hsa_len': len(hsa_seq),
        'match_count': match_count, 'max_len': max_len,
        'pct_identity': pct_identity,
        'mismatches': mismatches,
        'length_diff': length_diff,
    }


# ---------------------------------------------------------------------------
# TargetScan
# ---------------------------------------------------------------------------
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
    """
    Get predicted targets. Returns (n_targets, top_targets_df, family_note).
    family_note explains if targets were found via a seed family member.
    """
    if ts_df.empty:
        return 0, pd.DataFrame(), None

    family_note = None

    # Try direct match for mouse
    mask = (ts_df['Species ID'] == 10090) & \
           (ts_df['Representative miRNA'].astype(str) == mirna_id)
    matches = ts_df[mask]

    if len(matches) == 0:
        # Find any entry with this miRNA name (any species) to get the seed family
        search_name = mirna_id.replace('mmu-', '')
        seed_mask = ts_df['Representative miRNA'].astype(str).str.contains(
            re.escape(search_name), case=False, na=False)
        seed_matches = ts_df[seed_mask]

        if len(seed_matches) == 0:
            # Try without -5p/-3p
            base_name = re.sub(r'-[35]p$', '', search_name)
            seed_mask = ts_df['Representative miRNA'].astype(str).str.contains(
                re.escape(base_name), case=False, na=False)
            seed_matches = ts_df[seed_mask]

        if len(seed_matches) > 0:
            seed = seed_matches.iloc[0]['miRNA family']
            # Find mouse entries with this seed
            mask = (ts_df['miRNA family'] == seed) & (ts_df['Species ID'] == 10090)
            matches = ts_df[mask]
            if len(matches) > 0:
                # Find which representative miRNA was used for mouse
                rep_mirna = matches.iloc[0]['Representative miRNA']
                family_note = (f"Note: {mirna_id.replace('mmu-', '')} shares seed family "
                               f"'{seed}' with {rep_mirna.replace('mmu-', '')}. "
                               f"These miRNAs have identical seed sequences and are "
                               f"predicted to regulate the same targets.")

    if len(matches) == 0:
        return 0, pd.DataFrame(), None

    n_targets = matches['Gene Symbol'].nunique()
    score_col = 'Cumulative weighted context++ score'
    matches = matches.copy()
    matches[score_col] = pd.to_numeric(matches[score_col], errors='coerce')
    top = matches.nsmallest(10, score_col)
    display_cols = ['Gene Symbol', 'Total num conserved sites', score_col]
    display_cols = [c for c in display_cols if c in top.columns]
    return n_targets, top[display_cols], family_note


# ---------------------------------------------------------------------------
# NCBI queries
# ---------------------------------------------------------------------------
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
        'summary': info.get('summary', ''),
    }


def fetch_abstracts(pmids):
    """Fetch full abstract text for a list of PMIDs."""
    if not pmids:
        return {}
    resp = ncbi_request('efetch.fcgi', {
        'db': 'pubmed',
        'id': ','.join(pmids),
        'rettype': 'abstract',
        'retmode': 'xml',
    })
    if not resp:
        return {}

    # Parse XML to extract abstracts
    abstracts = {}
    import xml.etree.ElementTree as ET
    try:
        root = ET.fromstring(resp.text)
        for article in root.findall('.//PubmedArticle'):
            pmid_el = article.find('.//PMID')
            if pmid_el is None:
                continue
            pmid = pmid_el.text

            abstract_el = article.find('.//Abstract')
            if abstract_el is not None:
                parts = []
                for text_el in abstract_el.findall('.//AbstractText'):
                    label = text_el.get('Label', '')
                    text = ''.join(text_el.itertext()).strip()
                    if label and text:
                        parts.append(f"{label}: {text}")
                    elif text:
                        parts.append(text)
                abstracts[pmid] = ' '.join(parts)
    except ET.ParseError:
        pass

    return abstracts


def generate_biological_summary(mirna_name, abstracts, articles):
    """
    Extract a biological function summary from PubMed abstracts.
    Pulls out key sentences mentioning the miRNA's function, targets,
    pathways, and disease associations.
    """
    if not abstracts:
        return None

    clean_name = mirna_name.replace('mmu-', '')
    # Patterns to match: miR name followed by functional language
    name_patterns = [
        re.escape(clean_name),
        re.escape(mirna_name),
        re.escape(clean_name.replace('-', '')),  # miR1495p
    ]
    name_re = '|'.join(name_patterns)

    # Keywords that indicate functional statements
    func_keywords = [
        'regulat', 'target', 'inhibit', 'promot', 'suppress',
        'pathway', 'signal', 'express', 'role', 'function',
        'associat', 'biomarker', 'involved', 'mediat', 'modulat',
        'oncogen', 'tumor', 'cancer', 'apoptosis', 'proliferat',
        'differentiat', 'inflammat', 'immune', 'cardiac', 'hepat',
        'renal', 'pulmonar', 'neural',
    ]

    relevant_sentences = []
    seen = set()

    for pmid, abstract in abstracts.items():
        # Split into sentences
        sentences = re.split(r'(?<=[.!?])\s+', abstract)
        for sent in sentences:
            # Must mention the miRNA
            if not re.search(name_re, sent, re.IGNORECASE):
                continue
            # Must contain a functional keyword
            if not any(kw in sent.lower() for kw in func_keywords):
                continue
            # Deduplicate similar sentences
            sent_clean = sent.strip()
            sent_key = sent_clean[:80].lower()
            if sent_key in seen:
                continue
            seen.add(sent_key)
            # Find which article this came from
            article_ref = None
            for art in articles:
                if art['pmid'] == pmid:
                    article_ref = art
                    break
            relevant_sentences.append((sent_clean, article_ref))

    if not relevant_sentences:
        return None

    # Build summary from the best sentences (max 5)
    summary_parts = []
    for sent, art_ref in relevant_sentences[:5]:
        # Truncate very long sentences
        if len(sent) > 300:
            sent = sent[:297] + '...'
        if art_ref and art_ref['doi']:
            citation = f"(PMID: {art_ref['pmid']})"
        elif art_ref:
            citation = f"(PMID: {art_ref['pmid']})"
        else:
            citation = ""
        summary_parts.append(f"{sent} {citation}")

    return ' '.join(summary_parts)


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


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------
def generate_report(mirnas_df, ts_df, mirbase_seqs, output_path):
    unique_mirnas = mirnas_df['GeneID'].unique()
    print(f"\nAnnotating {len(unique_mirnas)} unique miRNAs...")
    lines = []
    lines.append("# miRNA Biomarker Annotation Report\n\n")
    lines.append("Automated annotation of biomarker miRNA candidates using "
                 "TargetScan Mouse 8.0, NCBI Gene, PubMed, and miRBase "
                 "sequence data.\n\n---\n\n")

    for i, gene_id in enumerate(unique_mirnas):
        mirna_name = gene_id.replace('mmu-', '')
        print(f"\n[{i+1}/{len(unique_mirnas)}] Processing {mirna_name}...")
        mirna_rows = mirnas_df[mirnas_df['GeneID'] == gene_id]

        lines.append(f"## {mirna_name}\n\n")

        # Biomarker context
        lines.append("### Biomarker Context\n\n")
        lines.append("| Group | Direction | log2FC | FDR | Biomarker Score |\n")
        lines.append("|-------|-----------|--------|-----|----------------|\n")
        for _, row in mirna_rows.iterrows():
            lines.append(f"| {row['Group']} | {row['Direction']} | "
                         f"{row['log2FC']:+.2f} | {row['padj']:.2e} | "
                         f"{row['biomarker_score']:.1f} |\n")
        lines.append("\n")

        # Human ortholog comparison
        print("  Comparing with human ortholog...")
        ortho = find_human_ortholog(gene_id, mirbase_seqs)
        lines.append("### Human Ortholog (miRBase Sequence Comparison)\n\n")
        if ortho is None:
            lines.append(f"*{mirna_name} was not found in miRBase.*\n\n")
        elif not ortho['found']:
            lines.append(f"**No human ortholog found.**\n\n")
            lines.append(f"Mouse sequence: `{ortho['mmu_seq']}`\n\n")
        elif ortho['identical']:
            lines.append(f"**Human ortholog: {ortho['hsa_name']}** "
                         f"- **100% identical** ({ortho['length']} nt)\n\n")
            lines.append(f"Sequence: `{ortho['mmu_seq']}`\n\n")
            lines.append("The mature miRNA sequence is perfectly conserved "
                         "between mouse and human, suggesting direct translational "
                         "relevance of findings to human biology.\n\n")
        else:
            pct = ortho['pct_identity']
            lines.append(f"**Human ortholog: {ortho['hsa_name']}** "
                         f"- **{pct:.1f}% identity**\n\n")
            lines.append(f"| | Sequence | Length |\n")
            lines.append(f"|---|---|---|\n")
            lines.append(f"| Mouse ({ortho['mmu_name']}) | "
                         f"`{ortho['mmu_seq']}` | {ortho['mmu_len']} nt |\n")
            lines.append(f"| Human ({ortho['hsa_name']}) | "
                         f"`{ortho['hsa_seq']}` | {ortho['hsa_len']} nt |\n\n")

            # Show alignment
            mmu_s = ortho['mmu_seq']
            hsa_s = ortho['hsa_seq']
            match_line = ''
            for p in range(max(len(mmu_s), len(hsa_s))):
                if p < len(mmu_s) and p < len(hsa_s):
                    match_line += '|' if mmu_s[p] == hsa_s[p] else 'X'
                else:
                    match_line += '-'

            lines.append(f"```\n")
            lines.append(f"Mouse: {mmu_s}\n")
            lines.append(f"       {match_line}\n")
            lines.append(f"Human: {hsa_s}\n")
            lines.append(f"```\n")
            lines.append(f"(`|` = match, `X` = mismatch, `-` = length difference)\n\n")

            if ortho['mismatches']:
                lines.append("**Mismatches:**\n\n")
                for mm in ortho['mismatches']:
                    seed_note = " *(in seed region)*" if mm['position'] <= 8 else ""
                    lines.append(f"- Position {mm['position']}: "
                                 f"{mm['mouse']} (mouse) -> {mm['human']} (human)"
                                 f"{seed_note}\n")
                lines.append("\n")

            if ortho['length_diff'] > 0:
                lines.append(f"Length difference: {ortho['length_diff']} nt\n\n")

            # Note about seed region conservation
            seed_mismatches = [m for m in ortho['mismatches'] if m['position'] <= 8]
            if not seed_mismatches:
                lines.append("*Seed region (positions 2-8) is conserved between "
                             "species, indicating shared target gene regulation.*\n\n")
            else:
                lines.append(f"*WARNING: {len(seed_mismatches)} mismatch(es) in the "
                             f"seed region (positions 2-8), which may result in "
                             f"different target gene specificity between species.*\n\n")

        # TargetScan
        print("  Querying TargetScan...")
        n_targets, top_targets, family_note = get_targetscan_targets(ts_df, gene_id)
        lines.append("### Predicted Gene Targets (TargetScan Mouse 8.0)\n\n")
        if n_targets > 0:
            if family_note:
                lines.append(f"> {family_note}\n\n")
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
                if gene_info and gene_info['summary']:
                    lines.append(f"**Top target gene: {gene_info['symbol']}** "
                                 f"({gene_info['full_name']})\n\n")
                    summary = gene_info['summary']
                    if len(summary) > 500:
                        summary = summary[:500] + '...'
                    lines.append(f"*Function:* {summary}\n\n")
                    lines.append(f"*NCBI Gene ID:* [{gene_info['gene_id']}]"
                                 f"(https://www.ncbi.nlm.nih.gov/gene/"
                                 f"{gene_info['gene_id']})\n\n")
                elif gene_info:
                    lines.append(f"**Top target gene: {gene_info['symbol']}** "
                                 f"({gene_info['full_name']})\n\n")
                    lines.append(f"*NCBI Gene ID:* [{gene_info['gene_id']}]"
                                 f"(https://www.ncbi.nlm.nih.gov/gene/"
                                 f"{gene_info['gene_id']})\n\n")
        else:
            lines.append("No predicted targets found in TargetScan Mouse 8.0 "
                         "conserved predictions.\n\n")

        # PubMed
        print("  Searching PubMed...")
        articles = search_pubmed(gene_id, max_results=5)

        # Fetch abstracts and generate biological summary
        bio_summary = None
        if articles:
            pmids = [a['pmid'] for a in articles]
            print("  Fetching abstracts...")
            abstracts = fetch_abstracts(pmids)
            if abstracts:
                print("  Generating biological summary...")
                bio_summary = generate_biological_summary(gene_id, abstracts, articles)

        lines.append("### Biological Function Summary\n\n")
        if bio_summary:
            lines.append(f"{bio_summary}\n\n")
        else:
            lines.append(f"No functional summary could be generated from "
                         f"available literature.\n\n")

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

    # Data sources
    lines.append("## Data Sources\n\n")
    lines.append("- **TargetScan Mouse 8.0**: Agarwal V, Bell GW, Nam JW, Bartel DP. "
                 "Predicting effective microRNA target sites in mammalian mRNAs. "
                 "*eLife*. 2015;4:e05005. DOI: [10.7554/eLife.05005]"
                 "(https://doi.org/10.7554/eLife.05005)\n\n")
    lines.append("- **miRBase (Release 22.1)**: Kozomara A, Birgaoanu M, Griffiths-Jones S. "
                 "miRBase: from microRNA sequences to function. "
                 "*Nucleic Acids Research*. 2019;47(D1):D155-D162. "
                 "DOI: [10.1093/nar/gky1141](https://doi.org/10.1093/nar/gky1141)\n\n")
    lines.append("- **NCBI PubMed/Gene**: National Center for Biotechnology Information. "
                 "https://www.ncbi.nlm.nih.gov/\n\n")

    report = ''.join(lines)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(report)
    return report


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 60)
    print("miRNA Biomarker Annotation Report")
    print("=" * 60)

    print(f"\n[1/5] Loading biomarker summary from {SUMMARY_CSV}...")
    if not os.path.exists(SUMMARY_CSV):
        print(f"ERROR: {SUMMARY_CSV} not found.")
        sys.exit(1)
    mirnas_df = load_biomarkers(SUMMARY_CSV)
    print(f"  Found {len(mirnas_df)} entries, "
          f"{mirnas_df['GeneID'].nunique()} unique miRNAs")

    print(f"\n[2/5] Loading TargetScan Mouse 8.0 predictions...")
    try:
        ts_df = download_targetscan()
        print(f"  Loaded {len(ts_df)} target predictions")
    except Exception as e:
        print(f"  WARNING: Could not load TargetScan data: {e}")
        ts_df = pd.DataFrame()

    print(f"\n[3/5] Loading miRBase mature sequences...")
    try:
        mirbase_seqs = load_mirbase_sequences()
        n_mmu = sum(1 for k in mirbase_seqs if k.startswith('mmu-'))
        n_hsa = sum(1 for k in mirbase_seqs if k.startswith('hsa-'))
        print(f"  Loaded {len(mirbase_seqs)} sequences ({n_mmu} mouse, {n_hsa} human)")
    except Exception as e:
        print(f"  WARNING: Could not load miRBase data: {e}")
        mirbase_seqs = {}

    print(f"\n[4/5] Generating annotation report...")
    report = generate_report(mirnas_df, ts_df, mirbase_seqs, OUTPUT_MD)

    print(f"\n[5/5] Report saved to {OUTPUT_MD}")
    print(f"  Report length: {len(report):,} characters")
    print("\n" + "=" * 60)
    print("ANNOTATION COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    main()
