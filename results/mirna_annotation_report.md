# miRNA Biomarker Annotation Report

Automated annotation of biomarker miRNA candidates using TargetScan Mouse 8.0, NCBI Gene, PubMed, and miRBase sequence data.

---

## miR-149-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +4.92 | 1.20e-09 | 259.0 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-149-5p** - **100% identical** (23 nt)

Sequence: `UCUGGCUCCGUGUCUUCACUCCC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 433**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Syt2 | 1 | -1.129 |
| Tirap | 2 | -0.85 |
| Hnrnpa1 | 2 | -0.847 |
| Aif1 | 1 | -0.753 |
| Scfd1 | 1 | -0.71 |
| Ddah1 | 1 | -0.697 |
| Cep19 | 1 | -0.671 |
| Ddi2 | 1 | -0.643 |
| Serf2 | 1 | -0.626 |
| Olfm1 | 1 | -0.623 |

**Top target gene: Syt2** (synaptotagmin II)

*Function:* This gene encodes a member of the synaptotagmin protein family. Synaptotagmin proteins are involved in membrane trafficking and are characterized by an N-terminal transmembrane region as well as tandem calcium binding domains. The encoded protein is able to bind inositol polyphosphate and is thought to be involved in synaptic function and neurotransmitter release. [provided by RefSeq, Sep 2017]

*NCBI Gene ID:* [20980](https://www.ncbi.nlm.nih.gov/gene/20980)

### Biological Function Summary

We report that physiological doses of 17β-estradiol promote EV secretion specifically from ER+ BC cells via inhibition of miR-149-5p, hindering its regulatory activity on SP1, a transcription factor that regulates the EV biogenesis factor nSMase2. (PMID: 37252969) Additionally, miR-149-5p downregulation promotes hnRNPA1 expression, responsible for the loading of let-7's miRNAs into EVs. (PMID: 37252969) Notably, both oncogenic and tumor suppressive roles have been reported for miR-149-5p. (PMID: 35008841) In this review, we summarize the impact of miR-149-5p in the tumorigenesis and elaborate mechanisms of its involvement in this process in a variety of neoplastic conditions based on three lines of evidence, i.e., in vitro, in vivo and clinical settings. (PMID: 35008841) Aberrant expression of miR-149 was also associated with metabolic alterations in several organs, but the impact of hepatic miR-149-5p deregulation in MASLD remains poorly characterized. (PMID: 39263327)

### Literature

1. Drula R et al. (2023). *17β-estradiol promotes extracellular vesicle release and selective miRNA loading in ERα-positive breast cancer.* Proc Natl Acad Sci U S A. DOI: [10.1073/pnas.2122053120](https://doi.org/10.1073/pnas.2122053120) PMID: [37252969](https://pubmed.ncbi.nlm.nih.gov/37252969/)

2. Ghafouri-Fard S et al. (2021). *A Review on the Role of miR-149-5p in the Carcinogenesis.* Int J Mol Sci. DOI: [10.3390/ijms23010415](https://doi.org/10.3390/ijms23010415) PMID: [35008841](https://pubmed.ncbi.nlm.nih.gov/35008841/)

3. Correia de Sousa M et al. (2024). *Hepatic miR-149-5p upregulation fosters steatosis, inflammation and fibrosis development in mice and in human liver organoids.* JHEP Rep. DOI: [10.1016/j.jhepr.2024.101126](https://doi.org/10.1016/j.jhepr.2024.101126) PMID: [39263327](https://pubmed.ncbi.nlm.nih.gov/39263327/)

4. Shen Y et al. (2022). *Tumor-Suppressive and Oncogenic Roles of microRNA-149-5p in Human Cancers.* Int J Mol Sci. DOI: [10.3390/ijms231810823](https://doi.org/10.3390/ijms231810823) PMID: [36142734](https://pubmed.ncbi.nlm.nih.gov/36142734/)

5. Nathani A et al. (2025). *Targeting EGFR-TKI resistance in lung cancer: Role of miR-5193/miR-149-5p loaded NK-EVs and Carboplatin combination.* Int J Pharm. DOI: [10.1016/j.ijpharm.2025.125573](https://doi.org/10.1016/j.ijpharm.2025.125573) PMID: [40204039](https://pubmed.ncbi.nlm.nih.gov/40204039/)

---

## miR-1b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +5.00 | 2.21e-08 | 254.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-1-5p** - **27.3% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-1b-5p) | `UACAUACUUCUUUACAUUCCA` | 21 nt |
| Human (hsa-miR-1-5p) | `ACAUACUUCUUUAUAUGCCCAU` | 22 nt |

```
Mouse: UACAUACUUCUUUACAUUCCA
       XXXXXXX|XX||XXXXXX|||-
Human: ACAUACUUCUUUAUAUGCCCAU
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: U (mouse) -> A (human) *(in seed region)*
- Position 2: A (mouse) -> C (human) *(in seed region)*
- Position 3: C (mouse) -> A (human) *(in seed region)*
- Position 4: A (mouse) -> U (human) *(in seed region)*
- Position 5: U (mouse) -> A (human) *(in seed region)*
- Position 6: A (mouse) -> C (human) *(in seed region)*
- Position 7: C (mouse) -> U (human) *(in seed region)*
- Position 9: U (mouse) -> C (human)
- Position 10: C (mouse) -> U (human)
- Position 13: U (mouse) -> A (human)
- Position 14: A (mouse) -> U (human)
- Position 15: C (mouse) -> A (human)
- Position 16: A (mouse) -> U (human)
- Position 17: U (mouse) -> G (human)
- Position 18: U (mouse) -> C (human)

Length difference: 1 nt

*WARNING: 7 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-1b-5p shares seed family 'GGAAUGU' with miR-1a-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 731**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Serp1 | 3 | -1.018 |
| Fam150b | 1 | -0.958 |
| Coro1c | 2 | -0.868 |
| Sri | 1 | -0.745 |
| Tmsb4x | 1 | -0.74 |
| Gja1 | 2 | -0.713 |
| Pgrmc1 | 1 | -0.698 |
| Tpm4 | 1 | -0.698 |
| Bscl2 | 1 | -0.674 |
| Pirt | 1 | -0.664 |

**Top target gene: Serp1** (stress-associated endoplasmic reticulum protein 1)

*Function:* Acts upstream of or within several processes, including endoplasmic reticulum unfolded protein response; positive regulation of organ growth; and positive regulation of peptide hormone secretion. Predicted to be located in cytoplasmic microtubule. Predicted to be active in endoplasmic reticulum. Is expressed in several structures, including jaw and orbito-sphenoid. Orthologous to human SERP1 (stress associated endoplasmic reticulum protein 1). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [28146](https://www.ncbi.nlm.nih.gov/gene/28146)

### Biological Function Summary

Furthermore, the miRNAs mmu-miR-1b-5p and mmu-miR-10b-5p (a cancer-related miRNA) were significantly decreased (P < .05) in sera from the rats inoculated with Anisakis CE, compared with control rats inoculated with saline. (PMID: 30006808) The most significantly up-regulated miRNAs were miR-185-3p and miR-1b-5p and the most significantly down-regulated miRNAs were miR-129b-5p and miR-223-5p, of which the targeted genes were closely related to the PI3K-Akt signal pathway. (PMID: 36034465)

### Literature

1. Corcuera MT et al. (2018). *Exploring tumourigenic potential of the parasite Anisakis: a pilot study.* Parasitol Res. DOI: [10.1007/s00436-018-6008-2](https://doi.org/10.1007/s00436-018-6008-2) PMID: [30006808](https://pubmed.ncbi.nlm.nih.gov/30006808/)

2. Zhu W et al. (2022). *The analysis of Modified Qing' E Formula on the differential expression of exosomal miRNAs in the femoral head bone tissue of mice with steroid-induced ischemic necrosis of femoral head.* Front Endocrinol (Lausanne). DOI: [10.3389/fendo.2022.954778](https://doi.org/10.3389/fendo.2022.954778) PMID: [36034465](https://pubmed.ncbi.nlm.nih.gov/36034465/)

3. Wang C et al. (2021). *Identification and characterization of miRNA expression profiles across five tissues in giant panda.* Gene. DOI: [10.1016/j.gene.2020.145206](https://doi.org/10.1016/j.gene.2020.145206) PMID: [33059030](https://pubmed.ncbi.nlm.nih.gov/33059030/)

---

## miR-1a-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +7.68 | 9.23e-05 | 241.9 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-1-3p** - **100% identical** (22 nt)

Sequence: `UGGAAUGUAAAGAAGUAUGUAU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 551**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Serp1 | 3 | -1.018 |
| Fam150b | 1 | -0.958 |
| Sri | 1 | -0.745 |
| Gja1 | 2 | -0.713 |
| Pgrmc1 | 1 | -0.698 |
| Pirt | 1 | -0.664 |
| Cxcl11 | 1 | -0.66 |
| Ip6k2 | 1 | -0.657 |
| Srsf9 | 1 | -0.638 |
| Eif1ax | 1 | -0.618 |

**Top target gene: Serp1** (stress-associated endoplasmic reticulum protein 1)

*Function:* Acts upstream of or within several processes, including endoplasmic reticulum unfolded protein response; positive regulation of organ growth; and positive regulation of peptide hormone secretion. Predicted to be located in cytoplasmic microtubule. Predicted to be active in endoplasmic reticulum. Is expressed in several structures, including jaw and orbito-sphenoid. Orthologous to human SERP1 (stress associated endoplasmic reticulum protein 1). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [28146](https://www.ncbi.nlm.nih.gov/gene/28146)

### Biological Function Summary

Additionally, miR-1a-3p expression was altered in vitro and in vivo to assess its role in regulating adipogenic differentiation. (PMID: 39438865) More importantly, exosomes derived from GC-M1 macrophages exhibited a heightened capacity to regulate the adipogenic differentiation of BMSCs, which was mediated by miR-1a-3p. (PMID: 39438865) In vivo and in vitro, miR-1a-3p promoted the adipogenic differentiation of BMSCs by targeting Cebpz and played an important role in the onset and progression of GA-ONFH. (PMID: 39438865) Inhibiting miR-1a-3p expression, both in vitro and in vivo, significantly mitigates the preferential adipogenic differentiation of BMSCs, thus slowing the progression of GA-ONFH. (PMID: 39438865) PLD1, which is a downstream target of miR-1a-3p, was the crux in the regulation of lipid metabolism by TSPJ. (PMID: 40663939)

### Literature

1. Duan P et al. (2024). *Exosomal miR-1a-3p derived from glucocorticoid-stimulated M1 macrophages promotes the adipogenic differentiation of BMSCs in glucocorticoid-associated osteonecrosis of the femoral head by targeting Cebpz.* J Nanobiotechnology. DOI: [10.1186/s12951-024-02923-5](https://doi.org/10.1186/s12951-024-02923-5) PMID: [39438865](https://pubmed.ncbi.nlm.nih.gov/39438865/)

2. Yang N et al. (2025). *Total saponins from Panax japonicus inhibit phosphatidylcholine hydrolysis and relieve hepatic steatosis via the miR-1a-3p/PLD1 pathway.* Phytomedicine. DOI: [10.1016/j.phymed.2025.157050](https://doi.org/10.1016/j.phymed.2025.157050) PMID: [40663939](https://pubmed.ncbi.nlm.nih.gov/40663939/)

3. Chen T et al. (2024). *MiR-1a-3p Inhibits Apoptosis in Fluoride-exposed LS8 Cells by Targeting Map3k1.* Biol Trace Elem Res. DOI: [10.1007/s12011-023-03869-9](https://doi.org/10.1007/s12011-023-03869-9) PMID: [37782397](https://pubmed.ncbi.nlm.nih.gov/37782397/)

4. Angrisano T et al. (2023). *Cripto Is Targeted by miR-1a-3p in a Mouse Model of Heart Development.* Int J Mol Sci. DOI: [10.3390/ijms241512251](https://doi.org/10.3390/ijms241512251) PMID: [37569627](https://pubmed.ncbi.nlm.nih.gov/37569627/)

5. Li B et al. (2022). *A20 (TNFAIP3) alleviates viral myocarditis through ADAR1/miR-1a-3p-dependent regulation.* BMC Cardiovasc Disord. DOI: [10.1186/s12872-021-02438-z](https://doi.org/10.1186/s12872-021-02438-z) PMID: [35034631](https://pubmed.ncbi.nlm.nih.gov/35034631/)

---

## miR-504-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +5.39 | 2.25e-06 | 212.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-504-5p** - **100% identical** (22 nt)

Sequence: `AGACCCUGGUCUGCACUCUAUC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

The expression of the most 10 differential expressed miRNAs (miR-122-5p, miR-133a-3p, miR-504-5p, miR-187-3p, miR-133b, miR-200c-3p, miR-375, miR-200b-5p, miR-200b-3p, and miR203a) was confirmed by droplet digital PCR in an independent cohort. (PMID: 31773868) After 10 weeks of daunorubicin treatment, when a further rise in cTnT was accompanied by significant left ventricle systolic dysfunction, only miR-504-5p was significantly (p < 0.01) downregulated, whereas 10 miRNAs were significantly upregulated relative to the control group; at this time-point,... (PMID: 38235109) OBJECTIVE: We aimed to determine the accuracy of the predictive value of a selected panel of miRNAs (miR-504-5p and miR-429) obtained on endometrial samples, in detecting EC and EIN, and to explore their role along the neoplastic continuum. (PMID: 41585943) CONCLUSION: Our preliminary findings suggest that reduced expression of miR-504-5p and miR-429 characterizes the transition from EIN to EC, supporting their potential role as tumor suppressors in this setting. (PMID: 41585943) Through bioinformatics analysis, DSCR9, microRNA-504-5p (miR-504-5p), and G protein-coupled receptor 65 (GPR65) were identified as targets implicated in breast cancer development. (PMID: 37248366)

### Literature

1. Palmieri O et al. (2020). *microRNA-mRNA network model in patients with achalasia.* Neurogastroenterol Motil. DOI: [10.1111/nmo.13764](https://doi.org/10.1111/nmo.13764) PMID: [31773868](https://pubmed.ncbi.nlm.nih.gov/31773868/)

2. Adamcova M et al. (2023). *Cardiac miRNA expression during the development of chronic anthracycline-induced cardiomyopathy using an experimental rabbit model.* Front Pharmacol. DOI: [10.3389/fphar.2023.1298172](https://doi.org/10.3389/fphar.2023.1298172) PMID: [38235109](https://pubmed.ncbi.nlm.nih.gov/38235109/)

3. Manzi A et al. (2026). *Tissue expression of miR-504-5p and miR-429 as diagnostic biomarkers for endometrial cancer and endometrial intraepithelial neoplasia: a pilot study.* J Liq Biopsy. DOI: [10.1016/j.jlb.2025.100451](https://doi.org/10.1016/j.jlb.2025.100451) PMID: [41585943](https://pubmed.ncbi.nlm.nih.gov/41585943/)

4. Li M et al. (2023). *Downregulation of the long noncoding RNA DSCR9 (Down syndrome critical region 9) delays breast cancer progression by modulating microRNA-504-5p-dependent G protein-coupled receptor 65.* Hum Cell. DOI: [10.1007/s13577-023-00916-4](https://doi.org/10.1007/s13577-023-00916-4) PMID: [37248366](https://pubmed.ncbi.nlm.nih.gov/37248366/)

5. Gonçalves TF et al. (2019). *Network Profiling of Brain-Expressed X-Chromosomal MicroRNA Genes Implicates Shared Key MicroRNAs in Intellectual Disability.* J Mol Neurosci. DOI: [10.1007/s12031-018-1235-7](https://doi.org/10.1007/s12031-018-1235-7) PMID: [30604382](https://pubmed.ncbi.nlm.nih.gov/30604382/)

---

## miR-466q

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +3.56 | 1.36e-04 | 74.8 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `GUGCACACACACACAUACGU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

We show that miR-467f and miR-466q modulate the pro-inflammatory phenotype of activated N9 microglia cells and of primary microglia acutely isolated from late symptomatic SOD1G93A mice, a murine ALS model, by downregulating Tnf and Il1b expression. (PMID: 33462263) Further analysis of the mode of action of miR-467f and miR-466q indicated that they dampen the pro-inflammatory phenotype of microglia by modulating p38 MAPK signaling pathway via inhibition of expression of their target genes, Map3k8 and Mk2. (PMID: 33462263) Upregulated miRNAs in IECs from septic mice, particularly miR-149-5p, miR-466q, miR-495, and miR-511-3p, were seen to exhibit complex and global effects on gene regulation networks. (PMID: 36899862) Furthermore, Map3k5 was regulated by AK154638 and mir-466q simultaneously. (PMID: 36207684) Moreover, miR-466q and miR-467f mimics downregulate Mapk11, while miR-466m-5p and miR-466i-3p mimics promote the nuclear translocation of Nrf2. (PMID: 36497181)

### Literature

1. Giunti D et al. (2021). *Role of miRNAs shuttled by mesenchymal stem cell-derived small extracellular vesicles in modulating neuroinflammation.* Sci Rep. DOI: [10.1038/s41598-021-81039-4](https://doi.org/10.1038/s41598-021-81039-4) PMID: [33462263](https://pubmed.ncbi.nlm.nih.gov/33462263/)

2. Caidengbate S et al. (2023). *MicroRNA Profiles in Intestinal Epithelial Cells in a Mouse Model of Sepsis.* Cells. DOI: [10.3390/cells12050726](https://doi.org/10.3390/cells12050726) PMID: [36899862](https://pubmed.ncbi.nlm.nih.gov/36899862/)

3. Jiang S et al. (2022). *Comprehensive ceRNA network for MACF1 regulates osteoblast proliferation.* BMC Genomics. DOI: [10.1186/s12864-022-08910-0](https://doi.org/10.1186/s12864-022-08910-0) PMID: [36207684](https://pubmed.ncbi.nlm.nih.gov/36207684/)

4. Provenzano F et al. (2022). *Micro-RNAs Shuttled by Extracellular Vesicles Secreted from Mesenchymal Stem Cells Dampen Astrocyte Pathological Activation and Support Neuroprotection in In-Vitro Models of ALS.* Cells. DOI: [10.3390/cells11233923](https://doi.org/10.3390/cells11233923) PMID: [36497181](https://pubmed.ncbi.nlm.nih.gov/36497181/)

---

## miR-743b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +5.47 | 2.77e-03 | 74.2 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `GAAAGACAUCAUGCUGAAUAGA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

Here we found that miR-743b-3p was higher expressed in the liver tissues of ageing mice through the small RNA sequencing and bioinformatics analysis, and its target PPM1K was predicted and confirmed the target relationship of miR-743b-3p with PPM1K in the aged mouse liver tissues and the cultured... (PMID: 38565071) Moreover, using the transfected miR-743b-3p mimics/inhibitors into the senescent hepatocyte AML12. (PMID: 38565071) RESULTS: We found that miR-743b-3p inhibition reversed the hepatocyte senescence, and finally decreased the expression of genes involved in lipid synthesis(Chrebp, Fabp4, Acly and Pparγ) through increasing the target gene expression of PPM1K which regulated the expression of branched-chain amino ... (PMID: 38565071) CONCLUSIONS: These results identify that age-induced expression of miR-743b-3p inhibits its target PPM1K which induces BCAA metabolic disorder and regulates hepatocyte lipid accumulation during ageing. (PMID: 38565071) Bioinformatics analysis confirmed four differentially expressed microRNAs (miR-22-3p, miR-743b-3p, miR-201-5p and miR-144-5p) and their common target genes (Tmem69 and Cxcl10). (PMID: 28123428)

### Literature

1. Lu T et al. (2024). *miR-743b-3p promotes hepatic lipogenesis via branched-chain amino acids (BCAA) metabolism by targeting PPM1K in aged mice.* Arch Gerontol Geriatr. DOI: [10.1016/j.archger.2024.105424](https://doi.org/10.1016/j.archger.2024.105424) PMID: [38565071](https://pubmed.ncbi.nlm.nih.gov/38565071/)

2. Li JA et al. (2016). *Key genes expressed in different stages of spinal cord ischemia/reperfusion injury.* Neural Regen Res. DOI: [10.4103/1673-5374.194754](https://doi.org/10.4103/1673-5374.194754) PMID: [28123428](https://pubmed.ncbi.nlm.nih.gov/28123428/)

3. Chen F et al. (2021). *Identification of key microRNAs and the underlying molecular mechanism in spinal cord ischemia-reperfusion injury in rats.* PeerJ. DOI: [10.7717/peerj.11454](https://doi.org/10.7717/peerj.11454) PMID: [34123589](https://pubmed.ncbi.nlm.nih.gov/34123589/)

---

## miR-181a-2-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +2.61 | 2.21e-08 | 63.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-181a-2-3p** - **95.5% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-181a-2-3p) | `ACCACCGACCGUUGACUGUACC` | 22 nt |
| Human (hsa-miR-181a-2-3p) | `ACCACUGACCGUUGACUGUACC` | 22 nt |

```
Mouse: ACCACCGACCGUUGACUGUACC
       |||||X||||||||||||||||
Human: ACCACUGACCGUUGACUGUACC
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 6: C (mouse) -> U (human) *(in seed region)*

*WARNING: 1 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

Although abnormal microRNA expression has been implicated in MDS, the exact role of miR-181a-2-3p has not been entirely elucidated. (PMID: 36444993) METHODS: We evaluated miR-181a-2-3p expression in BM samples of 54 newly diagnosed MDS cases, 16 sAML patients and 32 healthy donors and then assessed its association with clinical characteristics and its potential value for MDS diagnosis and prognosis. (PMID: 36444993) Additionally, in MDS patients with secondary AML (sAML), miR-181a-2-3p was over-expressed relative to levels in those without this form. (PMID: 36444993) Kaplan-Meier analysis showed a positive correlation between miR-181a-2-3p expression and overall survival (OS). (PMID: 36444993) CONCLUSION: Decreased miR-181a-2-3p expression in MDS patients may be considered as one of the underlying markers reflecting MDS progression and prognosis. (PMID: 36444993)

### Literature

1. Liang X et al. (2022). *MiR-181a-2-3p as a potential diagnostic and prognostic marker for myelodysplastic syndrome.* Hematology. DOI: [10.1080/16078454.2022.2149971](https://doi.org/10.1080/16078454.2022.2149971) PMID: [36444993](https://pubmed.ncbi.nlm.nih.gov/36444993/)

2. Li J et al. (2021). *miR-181a-2-3p Stimulates Gastric Cancer Progression via Targeting MYLK.* Front Bioeng Biotechnol. DOI: [10.3389/fbioe.2021.687915](https://doi.org/10.3389/fbioe.2021.687915) PMID: [34733825](https://pubmed.ncbi.nlm.nih.gov/34733825/)

3. Liu B et al. (2024). *Hsa-miR-181a-2-3p inhibits the oncogenicity of colon cancer by directly targeting STING.* Aging (Albany NY). DOI: [10.18632/aging.206059](https://doi.org/10.18632/aging.206059) PMID: [39133165](https://pubmed.ncbi.nlm.nih.gov/39133165/)

4. Stunf Pukl S (2022). *Are miRNAs Dynamic Biomarkers in Keratoconus? A Review of the Literature.* Genes (Basel). DOI: [10.3390/genes13040588](https://doi.org/10.3390/genes13040588) PMID: [35456395](https://pubmed.ncbi.nlm.nih.gov/35456395/)

5. Dong Z et al. (2022). *Exosomal miR-181a-2-3p derived from citreoviridin-treated hepatocytes activates hepatic stellate cells trough inducing mitochondrial calcium overload.* Chem Biol Interact. DOI: [10.1016/j.cbi.2022.109899](https://doi.org/10.1016/j.cbi.2022.109899) PMID: [35305974](https://pubmed.ncbi.nlm.nih.gov/35305974/)

---

## miR-208b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +5.60 | 1.03e-02 | 58.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-208b-5p** - **90.9% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-208b-5p) | `AAGCUUUUUGCUCGCGUUAUGU` | 22 nt |
| Human (hsa-miR-208b-5p) | `AAGCUUUUUGCUCGAAUUAUGU` | 22 nt |

```
Mouse: AAGCUUUUUGCUCGCGUUAUGU
       ||||||||||||||XX||||||
Human: AAGCUUUUUGCUCGAAUUAUGU
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 15: C (mouse) -> A (human)
- Position 16: G (mouse) -> A (human)

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-208b-5p shares seed family 'UAAGACG' with miR-208b-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 186**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Ube2v2 | 2 | -0.608 |
| Vav3 | 1 | -0.584 |
| Csnk2a2 | 1 | -0.533 |
| D1Ertd622e | 1 | -0.53 |
| Lrrtm1 | 1 | -0.51 |
| Ets1 | 1 | -0.461 |
| Stc1 | 1 | -0.424 |
| Elavl4 | 2 | -0.401 |
| Bhlhe41 | 1 | -0.398 |
| Sos2 | 1 | -0.398 |

**Top target gene: Ube2v2** (ubiquitin-conjugating enzyme E2 variant 2)

*Function:* Acts upstream of or within error-free postreplication DNA repair. Predicted to be located in nucleoplasm. Predicted to be part of UBC13-MMS2 complex. Predicted to be active in nucleus. Is expressed in cerebral cortex ventricular layer; cortical plate; and embryo. Orthologous to human UBE2V2 (ubiquitin conjugating enzyme E2 V2). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [70620](https://www.ncbi.nlm.nih.gov/gene/70620)

### Biological Function Summary

Therefore, the present study aimed to determine whether miR-208b-5p could regulate NSCLC progression. (PMID: 32565956) miR-208b-5p expression level was determined by reverse transcription-quantitative polymerase chain reaction. (PMID: 32565956) Furthermore, miR-208b-5p mimics was transfected into NSCLC A549 and H1299 cells in order to upregulate miR-208b-5p expression. (PMID: 32565956) Dual-luciferase reporter assay was utilized to investigate the associations between miR-208b-5p and IL9 mRNA. (PMID: 32565956) The results demonstrated that miR-208b-5p expression decreased in NSCLC tissues and cell lines. (PMID: 32565956)

### Literature

1. Ma J et al. (2020). *miR-208b-5p inhibits invasion of non-small cell lung cancer through the STAT3 pathway by targeting interleukin-9.* Oncol Lett. DOI: [10.3892/ol.2020.11570](https://doi.org/10.3892/ol.2020.11570) PMID: [32565956](https://pubmed.ncbi.nlm.nih.gov/32565956/)

2. Yang Z et al. (2022). *Circular RNA circ_0001445 alleviates the ox-LDL-induced endothelial injury in human primary aortic endothelial cells through regulating ABCG1 via acting as a sponge of miR-208b-5p.* Gen Thorac Cardiovasc Surg. DOI: [10.1007/s11748-022-01799-2](https://doi.org/10.1007/s11748-022-01799-2) PMID: [35391605](https://pubmed.ncbi.nlm.nih.gov/35391605/)

3. Liu H et al. (2023). *Circ_0001060 Upregulates and Encourages Progression in Osteosarcoma.* DNA Cell Biol. DOI: [10.1089/dna.2022.0500](https://doi.org/10.1089/dna.2022.0500) PMID: [36580535](https://pubmed.ncbi.nlm.nih.gov/36580535/)

4. Tokłowicz M et al. (2023). *MicroRNA expression profile analysis in human skeletal muscle tissue: Selection of critical reference.* Biomed Pharmacother. DOI: [10.1016/j.biopha.2023.114682](https://doi.org/10.1016/j.biopha.2023.114682) PMID: [37031490](https://pubmed.ncbi.nlm.nih.gov/37031490/)

5. Kakimoto Y et al. (2016). *MicroRNA deep sequencing reveals chamber-specific miR-208 family expression patterns in the human heart.* Int J Cardiol. DOI: [10.1016/j.ijcard.2016.02.145](https://doi.org/10.1016/j.ijcard.2016.02.145) PMID: [26974694](https://pubmed.ncbi.nlm.nih.gov/26974694/)

---

## miR-741-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +4.73 | 1.16e-02 | 54.8 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UGAGAGAUGCCAUUCUAUGUAGA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-741-3p shares seed family 'ACAUAGA' with miR-376c-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 272**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Kcnmb2 | 1 | -0.723 |
| Gabra1 | 1 | -0.639 |
| Sh2d1a | 1 | -0.595 |
| Srp19 | 1 | -0.578 |
| Ythdf1 | 1 | -0.573 |
| Hbegf | 1 | -0.546 |
| En2 | 1 | -0.533 |
| Emc4 | 1 | -0.507 |
| Gulp1 | 1 | -0.5 |
| Arfgef1 | 2 | -0.491 |

**Top target gene: Kcnmb2** (potassium large conductance calcium-activated channel, subfamily M, beta member 2)

*Function:* Predicted to enable calcium-activated potassium channel activity and potassium channel regulator activity. Predicted to be involved in detection of calcium ion; neuronal action potential; and potassium ion transport. Predicted to be located in plasma membrane. Predicted to be part of voltage-gated potassium channel complex. Is expressed in acoustic ganglion; ascending aorta; and ductus arteriosus. Orthologous to human KCNMB2 (potassium calcium-activated channel subfamily M regulatory beta subuni...

*NCBI Gene ID:* [72413](https://www.ncbi.nlm.nih.gov/gene/72413)

### Biological Function Summary

Therefore, in our study, microRNA sequencing was used to discover differential miRNAs in the hippocampus of RBI-modeled mice, which suggested that miR-741-3p was most significantly upregulated. (PMID: 33544844) To clarify the underlying mechanism of miR-741-3p in RBI-modeled mice, an inhibitor of miR-741-3p (antagomiR-741) was delivered into the brain via the nasal passage before irradiation. (PMID: 33544844) The delivery of antagomiR-741 significantly reduced miR-741-3p levels in the hippocampus of RBI-modeled mice, and the cognitive dysfunction and neuronal apoptosis induced by radiation were also alleviated at 6 weeks postirradiation. (PMID: 33544844) Downregulation of miR-741-3p was found to improve the protrusion and branching status of microglia after irradiation and reduced the number of GFAP-positive astrocytes. (PMID: 33544844) Furthermore, Ddr2, PKCα and St8sia1 were revealed as target genes of miR-741-3p and as potential regulatory targets for RBI. (PMID: 33544844)

### Literature

1. Ou M et al. (2021). *Nasal Delivery of AntagomiR-741 Protects Against the Radiation-Induced Brain Injury in Mice.* Radiat Res. DOI: [10.1667/RADE-20-00070.1](https://doi.org/10.1667/RADE-20-00070.1) PMID: [33544844](https://pubmed.ncbi.nlm.nih.gov/33544844/)

2. Tian T et al. (2019). *miRNA profiling in the hippocampus of attention-deficit/hyperactivity disorder rats.* J Cell Biochem. DOI: [10.1002/jcb.27639](https://doi.org/10.1002/jcb.27639) PMID: [30270454](https://pubmed.ncbi.nlm.nih.gov/30270454/)

3. Wen X et al. (2022). *CircRNA-011235 Counteracts The Deleterious Effect of Irradiation Treatment on Bone Mesenchymal Stem Cells by Regulating The miR-741-3p/CDK6 Pathway.* Cell J. DOI: [10.22074/cellj.2022.7697](https://doi.org/10.22074/cellj.2022.7697) PMID: [35182060](https://pubmed.ncbi.nlm.nih.gov/35182060/)

4. Ota H et al. (2019). *Identification of the X-linked germ cell specific miRNAs (XmiRs) and their functions.* PLoS One. DOI: [10.1371/journal.pone.0211739](https://doi.org/10.1371/journal.pone.0211739) PMID: [30707741](https://pubmed.ncbi.nlm.nih.gov/30707741/)

5. Nie J et al. (2018). *Analysis of non‑alcoholic fatty liver disease microRNA expression spectra in rat liver tissues.* Mol Med Rep. DOI: [10.3892/mmr.2018.9268](https://doi.org/10.3892/mmr.2018.9268) PMID: [30015905](https://pubmed.ncbi.nlm.nih.gov/30015905/)

---

## miR-486a-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Upregulated | +3.06 | 8.90e-04 | 46.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-486-3p** - **100% identical** (21 nt)

Sequence: `CGGGGCAGCUCAGUACAGGAU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-486a-3p shares seed family 'CCUGUAC' with miR-486a-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 146**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Gm12355 | 1 | -1.322 |
| Srsf3 | 2 | -1.27 |
| Abhd17b | 2 | -0.58 |
| Snrpd1 | 1 | -0.561 |
| Tob1 | 1 | -0.497 |
| Agbl5 | 1 | -0.486 |
| Glis1 | 1 | -0.468 |
| Piga | 1 | -0.465 |
| Bivm | 1 | -0.453 |
| Ccdc117 | 1 | -0.433 |

**Top target gene: Srsf3-ps** (serine and arginine rich splicing factor 3, pseudogene)

*NCBI Gene ID:* [100502754](https://www.ncbi.nlm.nih.gov/gene/100502754)

### Biological Function Summary

Cell counting and MTS assay were used to evaluate the effect of Ang II, DHEA and miR-486a-3p on VSMCs proliferation. (PMID: 36247250) qRT-PCR was performed to detect the expression of miR-486a-3p, PCNA, IL-1β and NLRP3. (PMID: 36247250) Western blot analysis was performed to detect the expressions of PCNA, IL-1β and NLRP3 after miR-486a-3p was knocked down or overexpressed in VSMCs. (PMID: 36247250) Using miRNA microarray analysis, we found that DHEA upregulated the expression of miR-486a-3p in VSMCs. (PMID: 36247250) Further experiments indicated that DHEA promoted miR-486a-3p expression in VSMCs and in the vascular intima. (PMID: 36247250)

### Literature

1. Zhang M et al. (2022). *Dehydroepiandrosterone inhibits vascular proliferation and inflammation by modulating the miR-486a-3p/NLRP3 axis.* Am J Transl Res. PMID: [36247250](https://pubmed.ncbi.nlm.nih.gov/36247250/)

2. Niitsu Y et al. (2023). *Increased serum extracellular vesicle miR-144-3p and miR-486a-3p in a mouse model of adipose tissue regeneration promote hepatocyte proliferation by targeting Txnip.* PLoS One. DOI: [10.1371/journal.pone.0284989](https://doi.org/10.1371/journal.pone.0284989) PMID: [37141242](https://pubmed.ncbi.nlm.nih.gov/37141242/)

3. Zhang C et al. (2021). *Long noncoding RNA Kcnq1ot1 promotes sC5b-9-induced podocyte pyroptosis by inhibiting miR-486a-3p and upregulating NLRP3.* Am J Physiol Cell Physiol. DOI: [10.1152/ajpcell.00403.2020](https://doi.org/10.1152/ajpcell.00403.2020) PMID: [33296289](https://pubmed.ncbi.nlm.nih.gov/33296289/)

4. Wang W et al. (2021). *Radiation induces submandibular gland damage by affecting Cdkn1a expression and regulating expression of miR-486a-3p in a xerostomia mouse model.* Adv Clin Exp Med. DOI: [10.17219/acem/136457](https://doi.org/10.17219/acem/136457) PMID: [34498815](https://pubmed.ncbi.nlm.nih.gov/34498815/)

5. Shima T et al. (2025). *The potential contribution of light-intensity exercise-induced miR-486a-3p secretion on enhancing empathic behavior in mice: Possible involvement of brown adipose tissue.* Brain Res. DOI: [10.1016/j.brainres.2025.149923](https://doi.org/10.1016/j.brainres.2025.149923) PMID: [40902699](https://pubmed.ncbi.nlm.nih.gov/40902699/)

---

## miR-1839-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -1.72 | 6.59e-05 | 3.2 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AAGGUAGAUAGAACAGGUCUUG`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

We also evaluated expression by a reverse transcriptase-polymerase chain reaction (RT-PCR) in normal tissues of the FSD2 gene, which spans the human miR-1839-5p gene in the opposite direction. (PMID: 31408249) Human heart tissue expresses both miR-1839-5p and FSD2. (PMID: 31408249) CONCLUSIONS: Human tissues express an orthologue of mouse miR-1839-5p and, given its expression pattern, we suggest that this miRNA could be explored as a potential oncomiR or cancer marker. (PMID: 31408249) Also, according to the genomic organization of miR-1839-5p and FSD2, perfect complementarity exists between the two elements, making possible miRNA-directed cleavage in human cardiac tissue. (PMID: 31408249) When melan-a melanocytes were treated with six synthesized microRNAs, miR-342-5p, miR-1839-5p, and miR-3082-5p inhibited melanosome transport and induced melanosome aggregation around the nucleus. (PMID: 31288473)

### Literature

1. Martínez-Saucedo M et al. (2019). *Identification of human miR-1839-5p by small RNA-seq, a miRNA enriched in neoplastic tissues.* J Gene Med. DOI: [10.1002/jgm.3117](https://doi.org/10.1002/jgm.3117) PMID: [31408249](https://pubmed.ncbi.nlm.nih.gov/31408249/)

2. Lee JA et al. (2019). *Identification of MicroRNA Targeting Mlph and Affecting Melanosome Transport.* Biomolecules. DOI: [10.3390/biom9070265](https://doi.org/10.3390/biom9070265) PMID: [31288473](https://pubmed.ncbi.nlm.nih.gov/31288473/)

3. Chou HD et al. (2023). *MicroRNA-152-3p and MicroRNA-196a-5p Are Downregulated When Müller Cells Are Promoted by Components of the Internal Limiting Membrane: Implications for Macular Hole Healing.* Int J Mol Sci. DOI: [10.3390/ijms242417188](https://doi.org/10.3390/ijms242417188) PMID: [38139016](https://pubmed.ncbi.nlm.nih.gov/38139016/)

4. Uhrova V et al. (2025). *Optimal endogenous controls for microRNA analysis of visceral adipose tissue in the NAFLD mouse model.* J Biosci. PMID: [40098399](https://pubmed.ncbi.nlm.nih.gov/40098399/)

---

## miR-362-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -1.64 | 6.91e-03 | 1.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-362-5p** - **95.8% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-362-5p) | `AAUCCUUGGAACCUAGGUGUGAAU` | 24 nt |
| Human (hsa-miR-362-5p) | `AAUCCUUGGAACCUAGGUGUGAGU` | 24 nt |

```
Mouse: AAUCCUUGGAACCUAGGUGUGAAU
       ||||||||||||||||||||||X|
Human: AAUCCUUGGAACCUAGGUGUGAGU
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 23: A (mouse) -> G (human)

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 140**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Sys1 | 1 | -0.642 |
| Kcns2 | 1 | -0.525 |
| Nhlh1 | 1 | -0.483 |
| Tmem174 | 1 | -0.474 |
| Lcp1 | 1 | -0.411 |
| Dll1 | 1 | -0.397 |
| Nol4 | 1 | -0.367 |
| Prkca | 1 | -0.354 |
| Dcun1d1 | 1 | -0.348 |
| Chsy1 | 1 | -0.331 |

**Top target gene: Sys1** (SYS1 Golgi-localized integral membrane protein homolog (S. cerevisiae))

*Function:* Predicted to be involved in Golgi to endosome transport; Golgi to plasma membrane protein transport; and protein localization to Golgi apparatus. Predicted to be active in Golgi membrane and trans-Golgi network. Orthologous to human SYS1 (SYS1 golgi trafficking protein). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [66460](https://www.ncbi.nlm.nih.gov/gene/66460)

### Biological Function Summary

Next, we used the NF-κB pathway inhibitor JSH-23 and miR-362-5p inhibitor or mimic to determine the molecular mechanisms. (PMID: 40083930) Lastly, we constructed the miR-362-5p sponge to validate its targeted therapeutic potential. (PMID: 40083930) Mechanistically, we found that HCC exosomes upregulate the expression of miR-362-5p in neutrophils and activate the NF-κB signaling pathway by targeting CYLD, promoting the survival and recruitment of neutrophils. (PMID: 40083930) In HCC mice, blocking miR-362-5p suppressed neutrophil infiltration, attenuated T-cell exhaustion, and suppressed HCC progression. (PMID: 40083930) Conclusions: This study clarified the roles of HCC exosomes on neutrophil infiltration and reprogramming and identified a potential target miR-362-5p for HCC treatment. (PMID: 40083930)

### Literature

1. Bi W et al. (2025). *Tumor-derived exosomes induce neutrophil infiltration and reprogramming to promote T-cell exhaustion in hepatocellular carcinoma.* Theranostics. DOI: [10.7150/thno.104557](https://doi.org/10.7150/thno.104557) PMID: [40083930](https://pubmed.ncbi.nlm.nih.gov/40083930/)

2. Zhang J et al. (2025). *Helicobacter pylori induced miR-362-5p upregulation drives gastric cancer progression and links hepatocellular carcinoma through an exosome-dependent pathway.* Front Cell Infect Microbiol. DOI: [10.3389/fcimb.2025.1582131](https://doi.org/10.3389/fcimb.2025.1582131) PMID: [40406521](https://pubmed.ncbi.nlm.nih.gov/40406521/)

3. Li Q et al. (2022). *MiR-362-5p inhibits cartilage repair in osteoarthritis via targeting plexin B1.* J Orthop Surg (Hong Kong). DOI: [10.1177/10225536221139887](https://doi.org/10.1177/10225536221139887) PMID: [36523183](https://pubmed.ncbi.nlm.nih.gov/36523183/)

4. Aarthy R et al. (2022). *Alteration of miR-362-5p and miR-454-3p expression elicits diverse responses in breast cancer cell lines.* Mol Biol Rep. DOI: [10.1007/s11033-021-06873-1](https://doi.org/10.1007/s11033-021-06873-1) PMID: [34727290](https://pubmed.ncbi.nlm.nih.gov/34727290/)

5. Zeng JH et al. (2023). *Loss of circIGF1R Suppresses Cardiomyocytes Proliferation by Sponging miR-362-5p.* DNA Cell Biol. DOI: [10.1089/dna.2022.0590](https://doi.org/10.1089/dna.2022.0590) PMID: [37347924](https://pubmed.ncbi.nlm.nih.gov/37347924/)

---

## miR-33-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -1.99 | 9.45e-03 | 1.4 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `GUGCAUUGUAGUUGCAUUGCA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 403**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Hmga2 | 2 | -0.586 |
| Gm8787 | 1 | -0.507 |
| En2 | 1 | -0.48 |
| Grik2 | 2 | -0.469 |
| Celf2 | 2 | -0.466 |
| Rps6kb1 | 1 | -0.385 |
| Pgam5 | 1 | -0.347 |
| Foxc1 | 1 | -0.342 |
| Ywhah | 1 | -0.335 |
| Zfp281 | 2 | -0.333 |

**Top target gene: Hmga2** (high mobility group AT-hook 2)

*Function:* Enables minor groove of adenine-thymine-rich DNA binding activity. Involved in several processes, including negative regulation of cellular senescence; positive regulation of angiogenesis; and positive regulation of cell proliferation in bone marrow. Acts upstream of or within several processes, including endocrine system development; lung development; and positive regulation of cell population proliferation. Located in male germ cell nucleus and nuclear chromosome. Is expressed in several struc...

*NCBI Gene ID:* [15364](https://www.ncbi.nlm.nih.gov/gene/15364)

### Biological Function Summary

Raw264.7 macrophages were induced to form foam cells with ox-LDL, and FL's effects on the AMPKα/SREBP-1c pathway and miR-33-5p were investigated. (PMID: 39775070) FL decreased miR-33-5p expression but up-regulated PPARγ, promoting ABCA1- and ABCG1-mediated cholesterol efflux. (PMID: 39775070) However, miR-33-5p mimic reduced FL-induced cholesterol efflux, while miR-33-5p inhibitor increased it. (PMID: 39775070) CONCLUSION: FL may promote foam cell cholesterol efflux by modifying the AMPKα/SREBP-1c pathway and down-regulating miR-33-5p, which targets cholesterol metabolism genes (PPARγ, ABCA1, and ABCG1). (PMID: 39775070) In our study, we identified the role of a microRNA, miR-33-5p, in promoting chondrocyte senescence and OA progression. (PMID: 37343371)

### Literature

1. Lee DS et al. (2023). *Tcf7l2 in hepatocytes regulates de novo lipogenesis in diet-induced non-alcoholic fatty liver disease in mice.* Diabetologia. DOI: [10.1007/s00125-023-05878-8](https://doi.org/10.1007/s00125-023-05878-8) PMID: [36759348](https://pubmed.ncbi.nlm.nih.gov/36759348/)

2. Guo YQ et al. (2025). *Floralozone attenuates atherosclerotic vascular injury by regulating AMPKα/SREBP-1c pathway and down-regulating miR-33-5p.* Eur J Nutr. DOI: [10.1007/s00394-024-03578-6](https://doi.org/10.1007/s00394-024-03578-6) PMID: [39775070](https://pubmed.ncbi.nlm.nih.gov/39775070/)

3. Chai S et al. (2022). *Protective effect of miR-33-5p on the M1/M2 polarization of microglia and the underlying mechanism.* Bioengineered. DOI: [10.1080/21655979.2022.2061285](https://doi.org/10.1080/21655979.2022.2061285) PMID: [35485294](https://pubmed.ncbi.nlm.nih.gov/35485294/)

4. Liu Y et al. (2023). *Senescence-responsive miR-33-5p promotes chondrocyte senescence and osteoarthritis progression by targeting SIRT6.* Int Immunopharmacol. DOI: [10.1016/j.intimp.2023.110506](https://doi.org/10.1016/j.intimp.2023.110506) PMID: [37343371](https://pubmed.ncbi.nlm.nih.gov/37343371/)

5. Li Z et al. (2023). *MiR-33-5p alleviates spinal cord injury in rats and protects PC12 cells from lipopolysaccharide-induced apoptosis.* Kaohsiung J Med Sci. DOI: [10.1002/kjm2.12610](https://doi.org/10.1002/kjm2.12610) PMID: [36354186](https://pubmed.ncbi.nlm.nih.gov/36354186/)

---

## miR-103-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -1.15 | 1.02e-02 | 1.3 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AGCAGCAUUGUACAGGGCUAUGA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 628**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| 9130401M01Rik | 2 | -0.913 |
| Zhx1 | 2 | -0.9 |
| Sec22a | 1 | -0.842 |
| Med26 | 2 | -0.81 |
| Pde3b | 2 | -0.764 |
| Dyrk2 | 2 | -0.745 |
| Cacna2d1 | 2 | -0.718 |
| Rab40b | 2 | -0.709 |
| Micall1 | 1 | -0.7 |
| Eva1a | 1 | -0.687 |

**Top target gene: 9130401M01Rik** (RIKEN cDNA 9130401M01 gene)

*Function:* Is expressed in cerebral cortex ventricular layer; pituitary gland; and submandibular gland primordium. Orthologous to several human genes including C8orf76 (chromosome 8 open reading frame 76). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [75758](https://www.ncbi.nlm.nih.gov/gene/75758)

### Biological Function Summary

Whereas the highly abundant miR-126-5p promotes regenerative proliferation of dysadapted ECs, miR-103-3p stimulates inflammatory activation and impairs endothelial regeneration by aberrant proliferation and micronuclei formation. (PMID: 33454857) Here, we investigated the role of microRNA-103-3p (miR-103-3p) in regulating chondrocyte function and elucidated the underlying mechanism. (PMID: 40155964) METHODS: MiR-103-3p expression in interleukin-1β (IL-1β)-stimulated chondrocytes was evaluated using RT-qPCR. (PMID: 40155964) The targets of miR-103-3p predicted by online databases were verified using biotin-based pulldown assay and luciferase reporter assay. (PMID: 40155964) IL-1β stimulated-chondrocytes were transfected with miR-103-3p inhibitor along with siRNA targeting cytoplasmic polyadenylation element-binding protein3 (siCPEB3), the autophagy inhibitor 3-MA, or the PI3K agonist 740 Y-P. (PMID: 40155964)

### Literature

1. Schober A et al. (2022). *Regulatory Non-coding RNAs in Atherosclerosis.* Handb Exp Pharmacol. DOI: [10.1007/164_2020_423](https://doi.org/10.1007/164_2020_423) PMID: [33454857](https://pubmed.ncbi.nlm.nih.gov/33454857/)

2. von Eckardstein A et al. (2022). *Regulatory Non-coding RNAs in Atherosclerosis.* . DOI: [10.1007/164_2020_423](https://doi.org/10.1007/164_2020_423) PMID: [36122128](https://pubmed.ncbi.nlm.nih.gov/36122128/)

3. Li J et al. (2025). *MiR-103-3p regulates chondrocyte autophagy, apoptosis, and ECM degradation through the PI3K/Akt/mTOR pathway by targeting CPEB3.* J Orthop Surg Res. DOI: [10.1186/s13018-025-05719-x](https://doi.org/10.1186/s13018-025-05719-x) PMID: [40155964](https://pubmed.ncbi.nlm.nih.gov/40155964/)

4. Zhang X et al. (2023). *miR-103-3p Regulates the Differentiation and Autophagy of Myoblasts by Targeting MAP4.* Int J Mol Sci. DOI: [10.3390/ijms24044130](https://doi.org/10.3390/ijms24044130) PMID: [36835542](https://pubmed.ncbi.nlm.nih.gov/36835542/)

5. He Y et al. (2023). *miR-103-3p Regulates the Proliferation and Differentiation of C2C12 Myoblasts by Targeting BTG2.* Int J Mol Sci. DOI: [10.3390/ijms242015318](https://doi.org/10.3390/ijms242015318) PMID: [37894995](https://pubmed.ncbi.nlm.nih.gov/37894995/)

---

## miR-551b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -4.86 | 6.01e-05 | 1.2 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-551b-3p** - **100% identical** (21 nt)

Sequence: `GCGACCCAUACUUGGUUUCAG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 8**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Lphn1 | 1 | -0.557 |
| Zfp36 | 1 | -0.462 |
| Ctif | 1 | -0.46 |
| Osbpl6 | 1 | -0.404 |
| Mef2c | 1 | -0.312 |
| Erbb4 | 1 | -0.23 |
| Nhej1 | 1 | -0.006 |
| Scrib | 1 | -0.002 |

**Top target gene: Adgrl1** (adhesion G protein-coupled receptor L1)

*Function:* Predicted to enable cell adhesion molecule binding activity; toxic substance binding activity; and transmembrane signaling receptor activity. Acts upstream of or within positive regulation of synapse assembly. Predicted to be located in growth cone and synapse. Predicted to be active in axon; glutamatergic synapse; and presynaptic membrane. Is expressed in central nervous system and retina. Orthologous to human ADGRL1 (adhesion G protein-coupled receptor L1). [provided by Alliance of Genome Reso...

*NCBI Gene ID:* [330814](https://www.ncbi.nlm.nih.gov/gene/330814)

### Biological Function Summary

In skin photoaging samples, PVT1 and AQP3 were poorly expressed, while miR-551b-3p was highly expressed. (PMID: 37000315) Mechanistically, PVT1 could sequester miR-551b-3p to upregulate the expression of AQP3, which further inactivated the ERK/p38 MAPK signaling pathway. (PMID: 37000315) In vitro cell experiments confirmed that overexpression of PVT1 or AQP3 enhanced viability of young and senescent HDFs and inhibited HDF senescence, while miR-551b-3p upregulation counteracted the effect of PVT1. (PMID: 37000315) In conclusion, PVT1-driven suppression of miR-551b-3p induces AQP3 expression to inactivate the ERK/p38 MAPK signaling pathway, thereby inhibiting HDF senescence and ultimately delaying the skin photoaging. (PMID: 37000315) The aim of the present study was to investigate the expression of serum miR-551b-3p in patients with GC and to explore its potential as a diagnostic biomarker in GC. (PMID: 31060996)

### Literature

1. Tang H et al. (2023). *LncRNA PVT1 delays skin photoaging by sequestering miR-551b-3p to release AQP3 expression via ceRNA mechanism.* Apoptosis. DOI: [10.1007/s10495-023-01834-4](https://doi.org/10.1007/s10495-023-01834-4) PMID: [37000315](https://pubmed.ncbi.nlm.nih.gov/37000315/)

2. Bai SY et al. (2019). *Serum miR-551b-3p is a potential diagnostic biomarker for gastric cancer.* Turk J Gastroenterol. DOI: [10.5152/tjg.2019.17875](https://doi.org/10.5152/tjg.2019.17875) PMID: [31060996](https://pubmed.ncbi.nlm.nih.gov/31060996/)

3. Dracheva KV et al. (2023). *Downregulation of Exosomal hsa-miR-551b-3p in Obesity and Its Link to Type 2 Diabetes Mellitus.* Noncoding RNA. DOI: [10.3390/ncrna9060067](https://doi.org/10.3390/ncrna9060067) PMID: [37987363](https://pubmed.ncbi.nlm.nih.gov/37987363/)

4. Yuan H et al. (2018). *Molecular mechanisms of lncRNA SMARCC2/miR-551b-3p/TMPRSS4 axis in gastric cancer.* Cancer Lett. DOI: [10.1016/j.canlet.2018.01.032](https://doi.org/10.1016/j.canlet.2018.01.032) PMID: [29337109](https://pubmed.ncbi.nlm.nih.gov/29337109/)

5. Chang W et al. (2019). *MicroRNA-551b-3p inhibits tumour growth of human cholangiocarcinoma by targeting Cyclin D1.* J Cell Mol Med. DOI: [10.1111/jcmm.14312](https://doi.org/10.1111/jcmm.14312) PMID: [31199052](https://pubmed.ncbi.nlm.nih.gov/31199052/)

---

## miR-33-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -1.72 | 3.03e-02 | 1.1 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CAAUGUUUCCACAGUGCAUCAC`

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-33-3p shares seed family 'UGCAUUG' with miR-33-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 403**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Hmga2 | 2 | -0.586 |
| Gm8787 | 1 | -0.507 |
| En2 | 1 | -0.48 |
| Grik2 | 2 | -0.469 |
| Celf2 | 2 | -0.466 |
| Rps6kb1 | 1 | -0.385 |
| Pgam5 | 1 | -0.347 |
| Foxc1 | 1 | -0.342 |
| Ywhah | 1 | -0.335 |
| Zfp281 | 2 | -0.333 |

**Top target gene: Hmga2** (high mobility group AT-hook 2)

*Function:* Enables minor groove of adenine-thymine-rich DNA binding activity. Involved in several processes, including negative regulation of cellular senescence; positive regulation of angiogenesis; and positive regulation of cell proliferation in bone marrow. Acts upstream of or within several processes, including endocrine system development; lung development; and positive regulation of cell population proliferation. Located in male germ cell nucleus and nuclear chromosome. Is expressed in several struc...

*NCBI Gene ID:* [15364](https://www.ncbi.nlm.nih.gov/gene/15364)

### Biological Function Summary

MicroRNA-33-3p (miR-33-3p) has been widely investigated for its roles in lipid metabolism and mitochondrial function; however, there are few studies on miR-33-3p in the context of neurological diseases. (PMID: 34152551) In this study, we investigated the functional role of miR-33-3p in rat pheochromocytoma PC12 cells. (PMID: 34152551) A miR-33-3p mimic was transduced into PC12 cells, and its effects on proliferation, apoptosis, and differentiation were studied using the MTS assay, EdU labeling, flow cytometry, qRT-PCR, western blot, ELISA, and immunofluorescence. (PMID: 34152551) We found that miR-33-3p significantly suppressed PC12 cell proliferation, but had no effect on apoptosis. (PMID: 34152551) Furthermore, miR-33-3p promoted the differentiation of PC12 cells into Tuj1-positive and choline acetyltransferase-positive neuron-like cells. (PMID: 34152551)

### Literature

1. Shan BQ et al. (2021). *miR-33-3p Regulates PC12 Cell Proliferation and Differentiation In Vitro by Targeting Slc29a1.* Neurochem Res. DOI: [10.1007/s11064-021-03377-z](https://doi.org/10.1007/s11064-021-03377-z) PMID: [34152551](https://pubmed.ncbi.nlm.nih.gov/34152551/)

2. Zhang Y et al. (2019). *MicroRNA-33-3p Regulates Vein Endothelial Cell Apoptosis in Selenium-Deficient Broilers by Targeting E4F1.* Oxid Med Cell Longev. DOI: [10.1155/2019/6274010](https://doi.org/10.1155/2019/6274010) PMID: [31249647](https://pubmed.ncbi.nlm.nih.gov/31249647/)

3. Perdaens O et al. (2024). *MicroRNAs dysregulated in multiple sclerosis affect the differentiation of CG-4 cells, an oligodendrocyte progenitor cell line.* Front Cell Neurosci. DOI: [10.3389/fncel.2024.1336439](https://doi.org/10.3389/fncel.2024.1336439) PMID: [38486710](https://pubmed.ncbi.nlm.nih.gov/38486710/)

4. Wan N et al. (2019). *microRNA-33-3p involved in selenium deficiency-induced apoptosis via targeting ADAM10 in the chicken kidney.* J Cell Physiol. DOI: [10.1002/jcp.28050](https://doi.org/10.1002/jcp.28050) PMID: [30605240](https://pubmed.ncbi.nlm.nih.gov/30605240/)

5. Anastasilakis AD et al. (2018). *Changes of Circulating MicroRNAs in Response to Treatment With Teriparatide or Denosumab in Postmenopausal Osteoporosis.* J Clin Endocrinol Metab. DOI: [10.1210/jc.2017-02406](https://doi.org/10.1210/jc.2017-02406) PMID: [29309589](https://pubmed.ncbi.nlm.nih.gov/29309589/)

---

## miR-326-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -2.19 | 2.83e-02 | 1.1 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CCUCUGGGCCCUUCCUCCAGU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 306**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Parva | 1 | -0.879 |
| Aak1 | 1 | -0.847 |
| Plec | 1 | -0.711 |
| Tom1 | 1 | -0.698 |
| Cox14 | 1 | -0.634 |
| Grin2b | 1 | -0.62 |
| Slc9a3r2 | 1 | -0.614 |
| Cplx2 | 1 | -0.606 |
| Rpgr | 1 | -0.598 |
| St3gal3 | 1 | -0.577 |

**Top target gene: Parva** (parvin, alpha)

*Function:* Enables actin binding activity. Involved in several processes, including circulatory system development; smooth muscle cell chemotaxis; and substrate adhesion-dependent cell spreading. Acts upstream of or within cell adhesion. Located in several cellular components, including focal adhesion; lamellipodium; and nucleus. Is expressed in several structures, including alimentary system; genitourinary system; nervous system; respiratory system; and sensory organ. Orthologous to human PARVA (parvin al...

*NCBI Gene ID:* [57342](https://www.ncbi.nlm.nih.gov/gene/57342)

### Biological Function Summary

However, the role of miR-326-3p in goat brown adipocytes remains largely unclear. (PMID: 41153426) Methods: Primary brown adipocytes were isolated from goat perirenal adipose tissue and subjected to gain and loss-of-function assays using miR-326-3p mimics and inhibitors. (PMID: 41153426) Target prediction and dual-luciferase reporter assays were performed to validate direct interaction between miR-326-3p and FGF11. (PMID: 41153426) Results: Expression profiling demonstrated that miR-326-3p is more enriched in brown adipose tissue (BAT) than in white adipose tissue (WAT), and the expression level gradually decreases with adipocyte differentiation. (PMID: 41153426) miR-326-3p overexpression significantly inhibited lipid droplet accumulation and the expression of genes associated with differentiation, thermogenesis, and mitochondria, including PPARγ, FABP4, UCP1, and PGC1α, whereas inhibition produced the opposite effect. (PMID: 41153426)

### Literature

1. Zhu Y et al. (2025). *The Role of miR-326-3p in Regulating Differentiation and Thermogenesis Genes in Goat Brown Adipocytes.* Genes (Basel). DOI: [10.3390/genes16101209](https://doi.org/10.3390/genes16101209) PMID: [41153426](https://pubmed.ncbi.nlm.nih.gov/41153426/)

2. Yuan W et al. (2020). *MiR-122-5p and miR-326-3p promote cadmium-induced NRK-52E cell apoptosis by downregulating PLD1.* Environ Toxicol. DOI: [10.1002/tox.22998](https://doi.org/10.1002/tox.22998) PMID: [32697411](https://pubmed.ncbi.nlm.nih.gov/32697411/)

3. Yuan W et al. (2020). *MiR-122-5p and miR-326-3p: Potential novel biomarkers for early detection of cadmium exposure.* Gene. DOI: [10.1016/j.gene.2019.144156](https://doi.org/10.1016/j.gene.2019.144156) PMID: [31626960](https://pubmed.ncbi.nlm.nih.gov/31626960/)

4. Yang X et al. (2022). *Endothelial Cell-Derived Extracellular Vesicles Target TLR4 via miRNA-326-3p to Regulate Skin Fibroblasts Senescence.* J Immunol Res. DOI: [10.1155/2022/3371982](https://doi.org/10.1155/2022/3371982) PMID: [35647205](https://pubmed.ncbi.nlm.nih.gov/35647205/)

5. Wu H et al. (2024). *Identification of autophagy-related signatures in doxorubicin-induced cardiotoxicity.* Toxicol Appl Pharmacol. DOI: [10.1016/j.taap.2024.117082](https://doi.org/10.1016/j.taap.2024.117082) PMID: [39218162](https://pubmed.ncbi.nlm.nih.gov/39218162/)

---

## miR-744-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -1.68 | 1.92e-02 | 1.0 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-744-5p** - **100% identical** (22 nt)

Sequence: `UGCGGGGCUAGGGCUAACAGCA`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 50**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Pax2 | 2 | -1.736 |
| Scrt1 | 1 | -1.317 |
| Camk2n2 | 1 | -1.272 |
| Phldb3 | 1 | -1.136 |
| Sh3bgrl3 | 1 | -0.884 |
| Hes3 | 1 | -0.84 |
| Akt1 | 1 | -0.704 |
| Tgfb1 | 1 | -0.672 |
| Gm10300 | 2 | -0.658 |
| A530084C06Rik | 2 | -0.642 |

**Top target gene: Pax2** (paired box 2)

*Function:* Enables C2H2 zinc finger domain binding activity; DNA-binding transcription factor activity, RNA polymerase II-specific; and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in several processes, including kidney development; negative regulation of apoptotic process involved in development; and nervous system development. Acts upstream of or within several processes, including kidney development; mesenchymal to epithelial transition; and ureter morphogenes...

*NCBI Gene ID:* [18504](https://www.ncbi.nlm.nih.gov/gene/18504)

### Biological Function Summary

In the current study, we performed a differential analysis of miRNA across these subsets, identifying a distinct miRNA, hsa-miR-744-5p, characterized by progressively increasing expression levels upon T cell activation. (PMID: 38830518) Target genes of miR-744-5p were predicted, followed by Gene Ontology (GO) and Kyoto Encyclopedia of Genes and Genomes (KEGG) pathway enrichment analyses, revealing that these genes predominantly associate with pathways related to the 'Wnt signaling pathway'. (PMID: 38830518) We established that miR-744-5p directly targets STK11, influencing its expression. (PMID: 38830518) Further, we investigated the implications of miR-744-5p on T cell differentiation and functionality. (PMID: 38830518) Overexpression of miR-744-5p in T cells resulted in heightened apoptosis, reduced proliferation, an increased proportion of late-stage differentiated T cells, and elevated secretion of the cytokine TNF-α. (PMID: 38830518)

### Literature

1. Han J et al. (2024). *miR-744-5p promotes T-cell differentiation via inhibiting STK11.* Gene. DOI: [10.1016/j.gene.2024.148635](https://doi.org/10.1016/j.gene.2024.148635) PMID: [38830518](https://pubmed.ncbi.nlm.nih.gov/38830518/)

2. Xie L et al. (2024). *mir-744-5p inhibits cell growth and angiogenesis in osteosarcoma by targeting NFIX.* J Orthop Surg Res. DOI: [10.1186/s13018-024-04947-x](https://doi.org/10.1186/s13018-024-04947-x) PMID: [39152460](https://pubmed.ncbi.nlm.nih.gov/39152460/)

3. Guiot J et al. (2025). *Association of fibrotic-related extracellular vesicle microRNAs with lung involvement in systemic sclerosis.* Eur Respir J. DOI: [10.1183/13993003.00276-2024](https://doi.org/10.1183/13993003.00276-2024) PMID: [39947668](https://pubmed.ncbi.nlm.nih.gov/39947668/)

4. Qian J et al. (2024). *Sivelestat sodium alleviated sepsis-induced acute lung injury by inhibiting TGF-β/Smad signaling pathways through upregulating microRNA-744-5p.* J Thorac Dis. DOI: [10.21037/jtd-24-65](https://doi.org/10.21037/jtd-24-65) PMID: [39552870](https://pubmed.ncbi.nlm.nih.gov/39552870/)

5. Xavier G et al. (2025). *Dysregulation of miR-335-5p, miR-30d-5p, and miR-744-5p in extracellular vesicles from first-episode psychosis patients: Implications for biomarker discovery.* Schizophr Res. DOI: [10.1016/j.schres.2025.10.011](https://doi.org/10.1016/j.schres.2025.10.011) PMID: [41125054](https://pubmed.ncbi.nlm.nih.gov/41125054/)

---

## miR-10a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -2.96 | 2.36e-02 | 1.0 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-10a-5p** - **100% identical** (23 nt)

Sequence: `UACCCUGUAGAUCCGAAUUUGUG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 232**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Bdnf | 1 | -0.791 |
| Hoxa3 | 1 | -0.619 |
| Zfp367 | 1 | -0.615 |
| Map3k7 | 1 | -0.612 |
| Arsj | 1 | -0.6 |
| Rora | 2 | -0.535 |
| Vwc2l | 2 | -0.51 |
| Sobp | 2 | -0.504 |
| Nr6a1 | 2 | -0.499 |
| Rgs8 | 1 | -0.461 |

**Top target gene: Bdnf** (brain derived neurotrophic factor)

*Function:* The protein encoded by this gene is a member of the nerve growth factor family. It is involved in the growth, differentiation and survival of specific types of developing neurons both in the central nervous system (CNS) and the peripheral nervous system. It is also involved in regulating synaptic plasticity in the CNS. Expression of a similar gene in human is reduced in both Alzheimer's and Huntington disease patients. Alternative splicing results in multiple transcript variants encoding differe...

*NCBI Gene ID:* [12064](https://www.ncbi.nlm.nih.gov/gene/12064)

### Biological Function Summary

Our RNA-seq analysis revealed elevated expression of miR-10a-5p in Pla-Exos from POF rabbits. (PMID: 39069050) Moreover, our findings demonstrate that exosomal miR-10a-5p suppresses GCs proliferation and induces apoptosis via the mitochondrial pathway. (PMID: 39069050) Additionally, exosomal miR-10a-5p inhibits the TrkB/Akt/mTOR signaling pathway by downregulating BDNF expression, thereby modulating the expression levels of proteins and genes associated with the cell cycle, follicle development, and GCs senescence. (PMID: 39069050) In conclusion, our study highlights the role of Pla-Exos miR-10a-5p in promoting rabbit POF through the TrkB/Akt/mTOR signaling pathway by targeting BDNF. (PMID: 39069050) MiR-10a-5p represented over 21% of the miRNA molecules in OCCC with endometriosis and was significantly upregulated (NGS: log2fold change = 4.37, P = 2.43e-18; QPCR: 8.1-fold change, P< 0.05). (PMID: 37621654)

### Literature

1. Bao Z et al. (2024). *Plasma-derived exosome miR-10a-5p promotes premature ovarian failure by target BDNF via the TrkB/Akt/mTOR signaling pathway.* Int J Biol Macromol. DOI: [10.1016/j.ijbiomac.2024.134195](https://doi.org/10.1016/j.ijbiomac.2024.134195) PMID: [39069050](https://pubmed.ncbi.nlm.nih.gov/39069050/)

2. Collins KE et al. (2023). *Transcriptomic analyses of ovarian clear-cell carcinoma with concurrent endometriosis.* Front Endocrinol (Lausanne). DOI: [10.3389/fendo.2023.1162786](https://doi.org/10.3389/fendo.2023.1162786) PMID: [37621654](https://pubmed.ncbi.nlm.nih.gov/37621654/)

3. Lee S et al. (2024). *miR-10a regulates cell death and inflammation in adipose tissue of male mice with diet-induced obesity.* Mol Metab. DOI: [10.1016/j.molmet.2024.102039](https://doi.org/10.1016/j.molmet.2024.102039) PMID: [39342992](https://pubmed.ncbi.nlm.nih.gov/39342992/)

4. Malekan M et al. (2023). *BDNF and its signaling in cancer.* J Cancer Res Clin Oncol. DOI: [10.1007/s00432-022-04365-8](https://doi.org/10.1007/s00432-022-04365-8) PMID: [36173463](https://pubmed.ncbi.nlm.nih.gov/36173463/)

5. Baek G et al. (2025). *miR-10a-5p and miR-10b-5p restore colonic motility in aged mice.* World J Gastroenterol. DOI: [10.3748/wjg.v31.i24.104437](https://doi.org/10.3748/wjg.v31.i24.104437) PMID: [40599192](https://pubmed.ncbi.nlm.nih.gov/40599192/)

---

## miR-652-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Heart | Downregulated | -1.38 | 3.51e-02 | 1.0 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-652-3p** - **100% identical** (21 nt)

Sequence: `AAUGGCGCCACUAGGGUUGUG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 16**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Plag1 | 1 | -0.862 |
| Isl1 | 1 | -0.746 |
| Tnrc6a | 1 | -0.619 |
| Capzb | 1 | -0.598 |
| Nptn | 1 | -0.465 |
| Gm9970 | 1 | -0.463 |
| Prrx1 | 1 | -0.412 |
| Vwa3b | 1 | -0.361 |
| Rasl10b | 1 | -0.36 |
| Ube2i | 1 | -0.337 |

**Top target gene: Plag1** (pleiomorphic adenoma gene 1)

*Function:* Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Involved in negative regulation of gene expression; positive regulation of gene expression; and positive regulation of glial cell proliferation. Acts upstream of or within gland morphogenesis and prostate gland growth. Predicted to be located in centrosome; cytosol; and nuclear speck. Is expressed in several structures, i...

*NCBI Gene ID:* [56711](https://www.ncbi.nlm.nih.gov/gene/56711)

### Biological Function Summary

Studies investigating the role of one of the miRNA-miR-652-3p-detail diverse roles for this miRNA in normal cell homoeostasis and disease states, including cancers, cardiovascular disease, mental health, and central nervous system diseases. (PMID: 33712860) Here, we review recent literature surrounding miR-652-3p, discussing its known target genes and their relevance to disease progression. (PMID: 33712860) These studies demonstrate that miR-652-3p targets LLGL1 and ZEB1 to modulate cell polarity mechanisms, with impacts on cancer metastasis and asymmetric cell division. (PMID: 33712860) Inhibition of the NOTCH ligand JAG1 by miR-652-3p can have diverse effects on angiogenesis and immune cell regulation. (PMID: 33712860) Investigation of miR-652-3p and other dysregulated miRNAs identified a number of pathways potentially regulated by miR-652-3p. (PMID: 33712860)

### Literature

1. Stevens MT et al. (2021). *Targets and regulation of microRNA-652-3p in homoeostasis and disease.* J Mol Med (Berl). DOI: [10.1007/s00109-021-02060-8](https://doi.org/10.1007/s00109-021-02060-8) PMID: [33712860](https://pubmed.ncbi.nlm.nih.gov/33712860/)

2. Baloun J et al. (2023). *Circulating miRNAs in hand osteoarthritis.* Osteoarthritis Cartilage. DOI: [10.1016/j.joca.2022.10.021](https://doi.org/10.1016/j.joca.2022.10.021) PMID: [36379393](https://pubmed.ncbi.nlm.nih.gov/36379393/)

3. Chen W et al. (2023). *MiR-652-3p promotes malignancy and metastasis of cancer cells via inhibiting TNRC6A in hepatocellular carcinoma.* Biochem Biophys Res Commun. DOI: [10.1016/j.bbrc.2022.11.100](https://doi.org/10.1016/j.bbrc.2022.11.100) PMID: [36495604](https://pubmed.ncbi.nlm.nih.gov/36495604/)

4. Li M et al. (2023). *Hypoxic BMSC-derived exosomal miR-652-3p promotes proliferation and metastasis of hepatocarcinoma cancer cells via targeting TNRC6A.* Aging (Albany NY). DOI: [10.18632/aging.205025](https://doi.org/10.18632/aging.205025) PMID: [37976119](https://pubmed.ncbi.nlm.nih.gov/37976119/)

5. Zhu QL et al. (2019). *MiR-652-3p promotes bladder cancer migration and invasion by targeting KCNN3.* Eur Rev Med Pharmacol Sci. DOI: [10.26355/eurrev_201910_19275](https://doi.org/10.26355/eurrev_201910_19275) PMID: [31696467](https://pubmed.ncbi.nlm.nih.gov/31696467/)

---

## miR-10b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +6.13 | 1.06e-15 | 632.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-10b-3p** - **27.3% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-10b-3p) | `CAGAUUCGAUUCUAGGGGAAUA` | 22 nt |
| Human (hsa-miR-10b-3p) | `ACAGAUUCGAUUCUAGGGGAAU` | 22 nt |

```
Mouse: CAGAUUCGAUUCUAGGGGAAUA
       XXXXX|XXXX|XXXX|||X|XX
Human: ACAGAUUCGAUUCUAGGGGAAU
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: C (mouse) -> A (human) *(in seed region)*
- Position 2: A (mouse) -> C (human) *(in seed region)*
- Position 3: G (mouse) -> A (human) *(in seed region)*
- Position 4: A (mouse) -> G (human) *(in seed region)*
- Position 5: U (mouse) -> A (human) *(in seed region)*
- Position 7: C (mouse) -> U (human) *(in seed region)*
- Position 8: G (mouse) -> C (human) *(in seed region)*
- Position 9: A (mouse) -> G (human)
- Position 10: U (mouse) -> A (human)
- Position 12: C (mouse) -> U (human)
- Position 13: U (mouse) -> C (human)
- Position 14: A (mouse) -> U (human)
- Position 15: G (mouse) -> A (human)
- Position 19: A (mouse) -> G (human)
- Position 21: U (mouse) -> A (human)
- Position 22: A (mouse) -> U (human)

*WARNING: 7 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-10b-3p shares seed family 'ACCCUGU' with miR-10a-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 295**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Bdnf | 1 | -0.791 |
| Hoxa3 | 1 | -0.619 |
| Zfp367 | 1 | -0.615 |
| Map3k7 | 1 | -0.612 |
| Arsj | 1 | -0.6 |
| Hoxb3 | 1 | -0.558 |
| Gata6 | 1 | -0.542 |
| Rora | 2 | -0.535 |
| Vwc2l | 2 | -0.51 |
| Sobp | 2 | -0.504 |

**Top target gene: Bdnf** (brain derived neurotrophic factor)

*Function:* The protein encoded by this gene is a member of the nerve growth factor family. It is involved in the growth, differentiation and survival of specific types of developing neurons both in the central nervous system (CNS) and the peripheral nervous system. It is also involved in regulating synaptic plasticity in the CNS. Expression of a similar gene in human is reduced in both Alzheimer's and Huntington disease patients. Alternative splicing results in multiple transcript variants encoding differe...

*NCBI Gene ID:* [12064](https://www.ncbi.nlm.nih.gov/gene/12064)

### Biological Function Summary

METHODS: In this study, we found that miR-10b-3p expression was suppressed in sorafenib-resistant HCC cell lines through miRNA microarray analysis. (PMID: 35236936) RESULTS: Sorafenib-induced apoptosis in HCC cells was significantly enhanced by miR-10b-3p overexpression and partially abrogated by miR-10b-3p depletion. (PMID: 35236936) 3.5 months, p = 0.021), suggesting that high serum miR-10b-3p level in patients treated with sorafenib for advanced HCC serves as a biomarker for predicting sorafenib efficacy. (PMID: 35236936) Furthermore, we confirmed that cyclin E1, a known promoter of sorafenib resistance reported by our previous study, is the downstream target for miR-10b-3p in HCC cells. (PMID: 35236936) CONCLUSIONS: This study not only identified the molecular target for miR-10b-3p, but also provided evidence that circulating miR-10b-3p may be used as a biomarker for predicting sorafenib sensitivity in patients with HCC. (PMID: 35236936)

### Literature

1. Shao YY et al. (2022). *Low miR-10b-3p associated with sorafenib resistance in hepatocellular carcinoma.* Br J Cancer. DOI: [10.1038/s41416-022-01759-w](https://doi.org/10.1038/s41416-022-01759-w) PMID: [35236936](https://pubmed.ncbi.nlm.nih.gov/35236936/)

2. Sun K et al. (2022). *MiR-10b-3p alleviates cerebral ischemia/reperfusion injury by targeting Krüppel-like factor 5 (KLF5).* Pflugers Arch. DOI: [10.1007/s00424-021-02645-9](https://doi.org/10.1007/s00424-021-02645-9) PMID: [34989875](https://pubmed.ncbi.nlm.nih.gov/34989875/)

3. Ye X et al. (2021). *MiR-10b-3p Protects Cerebral I/R Injury through Targeting Programmed Cell Death 5 (PDCD5).* Crit Rev Eukaryot Gene Expr. DOI: [10.1615/CritRevEukaryotGeneExpr.2021039465](https://doi.org/10.1615/CritRevEukaryotGeneExpr.2021039465) PMID: [34936294](https://pubmed.ncbi.nlm.nih.gov/34936294/)

4. Zhang J et al. (2019). *miR‑10b‑3p, miR‑8112 and let‑7j as potential biomarkers for autoimmune inner ear diseases.* Mol Med Rep. DOI: [10.3892/mmr.2019.10248](https://doi.org/10.3892/mmr.2019.10248) PMID: [31115534](https://pubmed.ncbi.nlm.nih.gov/31115534/)

5. Chen R et al. (2018). *Circulating microRNAs, miR-10b-5p, miR-328-3p, miR-100 and let-7, are associated with osteoblast differentiation in osteoporosis.* Int J Clin Exp Pathol. PMID: [31938234](https://pubmed.ncbi.nlm.nih.gov/31938234/)

---

## miR-615-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +7.64 | 1.54e-08 | 452.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-615-3p** - **100% identical** (22 nt)

Sequence: `UCCGAGCCUGGGUCUCCCUCUU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 10**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Mapt | 1 | -0.967 |
| Lrrc73 | 1 | -0.896 |
| Txnrd3 | 1 | -0.657 |
| Lcor | 1 | -0.623 |
| Mef2a | 1 | -0.509 |
| Pacsin1 | 1 | -0.276 |
| Ppfia4 | 1 | -0.191 |
| Shank3 | 1 | -0.149 |
| Foxp3 | 1 | -0.084 |
| 9130213A22Rik | 1 | -0.056 |

**Top target gene: Mapt** (microtubule-associated protein tau)

*Function:* Enables DNA binding activity; microtubule binding activity; and protein kinase binding activity. Involved in DNA damage response; negative regulation of tubulin deacetylation; and regulation of cellular response to heat. Acts upstream of or within several processes, including adult walking behavior; generation of neurons; and transport along microtubule. Located in several cellular components, including cytoskeleton; membrane raft; and postsynaptic density. Is expressed in several structures, in...

*NCBI Gene ID:* [17762](https://www.ncbi.nlm.nih.gov/gene/17762)

### Biological Function Summary

Within the ceRNA network, SNHG9-hsa-miR-615-3p-ACER3, hsa-miR-212-5p and hsa-miR-5682 may play crucial roles in asthma pathogenesis. (PMID: 38297226) After SNHG9 knockdown, miR-615-3p expression was significantly upregulated, while that of ACER3 was significantly downregulated. (PMID: 38297226) In addition, SNHG9-hsa-miR-615-3p-ACER3 may be viewed as effective therapeutic targets for asthma. (PMID: 38297226) This study aimed to investigate the role of miR-615-3p in regulating odontogenic differentiation in stem cells from the apical papilla (SCAPs), offering insights into potential applications for enhancing dental tissue regeneration and repair. (PMID: 40745571) METHODS: Quantitative PCR (qPCR), Western blot analysis, alkaline phosphatase (ALP) activity assay, and Alizarin Red staining (ARS) were performed to assess odontogenic differentiation following miR-615-3p modulation in SCAPs. (PMID: 40745571)

### Literature

1. Jia Y et al. (2024). *Lipid metabolism-related genes are involved in the occurrence of asthma and regulate the immune microenvironment.* BMC Genomics. DOI: [10.1186/s12864-023-09795-3](https://doi.org/10.1186/s12864-023-09795-3) PMID: [38297226](https://pubmed.ncbi.nlm.nih.gov/38297226/)

2. Godínez-Rubí M et al. (2020). *miR-615 Fine-Tunes Growth and Development and Has a Role in Cancer and in Neural Repair.* Cells. DOI: [10.3390/cells9071566](https://doi.org/10.3390/cells9071566) PMID: [32605009](https://pubmed.ncbi.nlm.nih.gov/32605009/)

3. Yang H et al. (2025). *Inhibition of miR-615-3p enhances dentinogenesis in scap(s) via PVT1-mediated mitochondrial regulation.* Stem Cell Res Ther. DOI: [10.1186/s13287-025-04528-7](https://doi.org/10.1186/s13287-025-04528-7) PMID: [40745571](https://pubmed.ncbi.nlm.nih.gov/40745571/)

4. Yu X et al. (2024). *Mir-615-3p promotes osteosarcoma progression via the SESN2/AMPK/mTOR pathway.* Cancer Cell Int. DOI: [10.1186/s12935-024-03604-x](https://doi.org/10.1186/s12935-024-03604-x) PMID: [39702297](https://pubmed.ncbi.nlm.nih.gov/39702297/)

5. Miyamoto Y et al. (2014). *Mmu-miR-615-3p regulates lipoapoptosis by inhibiting C/EBP homologous protein.* PLoS One. DOI: [10.1371/journal.pone.0109637](https://doi.org/10.1371/journal.pone.0109637) PMID: [25314137](https://pubmed.ncbi.nlm.nih.gov/25314137/)

---

## miR-10b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +5.98 | 1.15e-07 | 292.2 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-10b-5p** - **100% identical** (23 nt)

Sequence: `UACCCUGUAGAACCGAAUUUGUG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 63**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Hoxb3 | 1 | -0.558 |
| Gata6 | 1 | -0.542 |
| Dusp3 | 1 | -0.448 |
| Dazap1 | 1 | -0.438 |
| Fign | 2 | -0.436 |
| Ago3 | 1 | -0.433 |
| Sdc1 | 1 | -0.424 |
| Klf11 | 1 | -0.408 |
| Ncor2 | 1 | -0.396 |
| Cyth1 | 1 | -0.362 |

**Top target gene: Hoxb3** (homeobox B3)

*Function:* Enables RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Acts upstream of or within several processes, including hemopoiesis; nervous system development; and skeletal system development. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. Is expressed in several structures, including branchial arch; central nervous system; embryo mesenchyme; gut; and mesoderm. Orthologous to human HOXB3 (homeobox B3). [provided by Alliance of Genome Resources...

*NCBI Gene ID:* [15410](https://www.ncbi.nlm.nih.gov/gene/15410)

### Biological Function Summary

miR-10b-5p target genes were identified and validated in mouse and human cell lines. (PMID: 33421511) For gain-of-function studies, a synthetic miR-10b-5p mimic was injected in multiple diabetic mouse models. (PMID: 33421511) RESULTS: miR-10b-5p is highly expressed in ICCs from healthy mice, but drastically depleted in ICCs from diabetic mice. (PMID: 33421511) miR-10b-5p targets the transcription factor Krüppel-like factor 11 (KLF11), which negatively regulates KIT expression. (PMID: 33421511) CONCLUSIONS: miR-10b-5p is a key regulator in diabetes and gastrointestinal dysmotility via the KLF11-KIT pathway. (PMID: 33421511)

### Literature

1. Singh R et al. (2021). *miR-10b-5p Rescues Diabetes and Gastrointestinal Dysmotility.* Gastroenterology. DOI: [10.1053/j.gastro.2020.12.062](https://doi.org/10.1053/j.gastro.2020.12.062) PMID: [33421511](https://pubmed.ncbi.nlm.nih.gov/33421511/)

2. Baek G et al. (2025). *miR-10a-5p and miR-10b-5p restore colonic motility in aged mice.* World J Gastroenterol. DOI: [10.3748/wjg.v31.i24.104437](https://doi.org/10.3748/wjg.v31.i24.104437) PMID: [40599192](https://pubmed.ncbi.nlm.nih.gov/40599192/)

3. Zogg H et al. (2023). *miR-10b-5p rescues leaky gut linked with gastrointestinal dysmotility and diabetes.* United European Gastroenterol J. DOI: [10.1002/ueg2.12463](https://doi.org/10.1002/ueg2.12463) PMID: [37723933](https://pubmed.ncbi.nlm.nih.gov/37723933/)

4. Hu Y et al. (2025). *Induction of necroptosis in lung adenocarcinoma by miR‑10b‑5p through modulation of the PKP3/RIPK3/MLKL cascade.* Oncol Rep. DOI: [10.3892/or.2025.8889](https://doi.org/10.3892/or.2025.8889) PMID: [40116080](https://pubmed.ncbi.nlm.nih.gov/40116080/)

5. Ge G et al. (2019). *miR-10b-5p Regulates C2C12 Myoblasts Proliferation and Differentiation.* Biosci Biotechnol Biochem. DOI: [10.1080/09168451.2018.1533805](https://doi.org/10.1080/09168451.2018.1533805) PMID: [30336746](https://pubmed.ncbi.nlm.nih.gov/30336746/)

---

## miR-615-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +6.20 | 1.19e-05 | 179.8 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-615-5p** - **100% identical** (22 nt)

Sequence: `GGGGGUCCCCGGUGCUCGGAUC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-615-5p shares seed family 'CCGAGCC' with miR-615-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 10**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Mapt | 1 | -0.967 |
| Lrrc73 | 1 | -0.896 |
| Txnrd3 | 1 | -0.657 |
| Lcor | 1 | -0.623 |
| Mef2a | 1 | -0.509 |
| Pacsin1 | 1 | -0.276 |
| Ppfia4 | 1 | -0.191 |
| Shank3 | 1 | -0.149 |
| Foxp3 | 1 | -0.084 |
| 9130213A22Rik | 1 | -0.056 |

**Top target gene: Mapt** (microtubule-associated protein tau)

*Function:* Enables DNA binding activity; microtubule binding activity; and protein kinase binding activity. Involved in DNA damage response; negative regulation of tubulin deacetylation; and regulation of cellular response to heat. Acts upstream of or within several processes, including adult walking behavior; generation of neurons; and transport along microtubule. Located in several cellular components, including cytoskeleton; membrane raft; and postsynaptic density. Is expressed in several structures, in...

*NCBI Gene ID:* [17762](https://www.ncbi.nlm.nih.gov/gene/17762)

### Biological Function Summary

miR-615-5p bound to 3'UTR of myelin regulator factor (MYRF), a crucial myelination transcription factor expressed in oligodendrocyte lineage cells. (PMID: 38246987) Mechanistically, exosomes from activated microglia transferred miR-615-5p to OPCs, which directly bound to MYRF and inhibited OPC maturation. (PMID: 38246987) Furthermore, an effect of AAV expressing miR-615-5p sponge in microglia was tested in experimental autoimmune encephalomyelitis (EAE) and cuprizone (CPZ)-induced demyelination model, the classical mouse models of multiple sclerosis. (PMID: 38246987) miR-615-5p sponge effectively alleviated disease progression and promoted remyelination. (PMID: 38246987) This study identifies miR-615-5p/MYRF as a new target for the therapy of demyelinating diseases. (PMID: 38246987)

### Literature

1. Ji XY et al. (2024). *Microglia-derived exosomes modulate myelin regeneration via miR-615-5p/MYRF axis.* J Neuroinflammation. DOI: [10.1186/s12974-024-03019-5](https://doi.org/10.1186/s12974-024-03019-5) PMID: [38246987](https://pubmed.ncbi.nlm.nih.gov/38246987/)

2. Godínez-Rubí M et al. (2020). *miR-615 Fine-Tunes Growth and Development and Has a Role in Cancer and in Neural Repair.* Cells. DOI: [10.3390/cells9071566](https://doi.org/10.3390/cells9071566) PMID: [32605009](https://pubmed.ncbi.nlm.nih.gov/32605009/)

3. Ghafouri-Fard S et al. (2022). *A concise review on the role of LINC00324 in different cancers.* Pathol Res Pract. DOI: [10.1016/j.prp.2022.154192](https://doi.org/10.1016/j.prp.2022.154192) PMID: [36399929](https://pubmed.ncbi.nlm.nih.gov/36399929/)

4. Mao J et al. (2024). *Transcriptome network analysis of inflammation and fibrosis in keloids.* J Dermatol Sci. DOI: [10.1016/j.jdermsci.2023.12.007](https://doi.org/10.1016/j.jdermsci.2023.12.007) PMID: [38242738](https://pubmed.ncbi.nlm.nih.gov/38242738/)

5. Silva VR et al. (2025). *MicroRNA-Mediated Regulation of Vascular Endothelium: From Pro-Inflammation to Atherosclerosis.* Int J Mol Sci. DOI: [10.3390/ijms26135919](https://doi.org/10.3390/ijms26135919) PMID: [40649699](https://pubmed.ncbi.nlm.nih.gov/40649699/)

---

## miR-196a-2-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +8.22 | 1.73e-03 | 160.1 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UCGGCAACAAGAAACUGCCUGA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

In addition, we identified three miRNAs (mmu-miR-542-5p, mmu-miR-149-5p and mmu-miR-196a-2-3p) that were upregulated with the DN group and downregulated in the germacrone-treated group. (PMID: 39738220) Subsequently, the expression level of mmu-miR-542-5p, mmu-miR-149-5p and mmu-miR-196a-2-3p were validated in a validation dataset. (PMID: 39738220)

### Literature

1. Wang B et al. (2024). *Bioinformatics analysis of miRNAs germacrone protection on diabetic nephropathy.* Sci Rep. DOI: [10.1038/s41598-024-81944-4](https://doi.org/10.1038/s41598-024-81944-4) PMID: [39738220](https://pubmed.ncbi.nlm.nih.gov/39738220/)

---

## miR-196b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +8.30 | 9.26e-04 | 129.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-196b-3p** - **100% identical** (22 nt)

Sequence: `UCGACAGCACGACACUGCCUUC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-196b-3p shares seed family 'AGGUAGU' with miR-196a-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 311**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Hoxa7 | 4 | -1.858 |
| Nr6a1 | 4 | -1.117 |
| Hmga2 | 2 | -0.963 |
| Hand1 | 1 | -0.942 |
| Hoxc8 | 3 | -0.786 |
| Hoxb7 | 1 | -0.781 |
| Foxi3 | 1 | -0.72 |
| Hoxa9 | 2 | -0.666 |
| Hoxa5 | 1 | -0.653 |
| Epc2 | 2 | -0.626 |

**Top target gene: Hoxa7** (homeobox A7)

*Function:* Enables DNA binding activity and DNA-binding transcription factor activity. Acts upstream of or within several processes, including embryonic skeletal system morphogenesis; regulation of transcription by RNA polymerase II; and stem cell differentiation. Located in nucleus. Is expressed in several structures, including central nervous system; embryo mesenchyme; genitourinary system; gut; and musculoskeletal system. Orthologous to human HOXA7 (homeobox A7). [provided by Alliance of Genome Resource...

*NCBI Gene ID:* [15404](https://www.ncbi.nlm.nih.gov/gene/15404)

### Biological Function Summary

RESULTS: In this study, we used BGISEQ-500 sequencing technology to analyze the expression of small RNAs in primary cultured IM and SC adipocytes on day 8 after adipogenic induction, and found 32-fold higher miR-196b-3p expression, as well as 8-fold lower miR-450b-3p expression in IM adipocytes t... (PMID: 37369998) Functional studies revealed that miR-196b-3p inhibits adipogenesis by targeting CD47 via the AMPK signaling pathway, and its effect was attenuated by the specific p-AMPKα activator AICAR. (PMID: 37369998) CONCLUSIONS: Our findings suggest that miR-196b-3p and miR-450b-3p are novel key regulatory factors that play opposite roles in porcine adipogenesis, helping us decipher the regulatory differences between porcine IM and SC fat deposition. (PMID: 37369998) Here, we show that an intrinsic constitutively activated feedforward signaling circuit composed of IκBα/NF-κB(p65), miR-196b-3p, Meis2, and PPP3CC is formed during the emergence of castration-resistant prostate cancer (CRPC). (PMID: 28041912) RESULTS: We identified miR-222-5p, miR-200a-5p, miR-196b-3p and miR-454-5p as biomarker candidates from the tumour tissue and embryoid body screening but the expression of these microRNAs was very low in serum and not statistically different between patients and controls. (PMID: 35181587)

### Literature

1. Wu W et al. (2023). *MiR-196b-3p and miR-450b-3p are key regulators of adipogenesis in porcine intramuscular and subcutaneous adipocytes.* BMC Genomics. DOI: [10.1186/s12864-023-09477-0](https://doi.org/10.1186/s12864-023-09477-0) PMID: [37369998](https://pubmed.ncbi.nlm.nih.gov/37369998/)

2. Jeong JH et al. (2017). *A Constitutive Intrinsic Inflammatory Signaling Circuit Composed of miR-196b, Meis2, PPP3CC, and p65 Drives Prostate Cancer Castration Resistance.* Mol Cell. DOI: [10.1016/j.molcel.2016.11.034](https://doi.org/10.1016/j.molcel.2016.11.034) PMID: [28041912](https://pubmed.ncbi.nlm.nih.gov/28041912/)

3. Myklebust MP et al. (2022). *MicroRNAs in Differentiation of Embryoid Bodies and the Teratoma Subtype of Testicular Cancer.* Cancer Genomics Proteomics. DOI: [10.21873/cgp.20313](https://doi.org/10.21873/cgp.20313) PMID: [35181587](https://pubmed.ncbi.nlm.nih.gov/35181587/)

4. Yurikova OY et al. (2019). *[The Interaction of miRNA-5p and miRNA-3p with the mRNAs of Orthologous Genes].* Mol Biol (Mosk). DOI: [10.1134/S0026898419040189](https://doi.org/10.1134/S0026898419040189) PMID: [31397443](https://pubmed.ncbi.nlm.nih.gov/31397443/)

5. Sonohara F et al. (2020). *Exploration of Exosomal Micro RNA Biomarkers Related to Epithelial-to-Mesenchymal Transition in Pancreatic Cancer.* Anticancer Res. DOI: [10.21873/anticanres.14138](https://doi.org/10.21873/anticanres.14138) PMID: [32234872](https://pubmed.ncbi.nlm.nih.gov/32234872/)

---

## miR-196a-1-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +7.54 | 9.28e-03 | 116.2 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-196a-1-3p** - **81.8% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-196a-1-3p) | `CAACGACAUCAAACCACCUGAU` | 22 nt |
| Human (hsa-miR-196a-1-3p) | `CAACAACAUUAAACCACCCGA` | 21 nt |

```
Mouse: CAACGACAUCAAACCACCUGAU
       ||||X||||X||||||||X||-
Human: CAACAACAUUAAACCACCCGA
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 5: G (mouse) -> A (human) *(in seed region)*
- Position 10: C (mouse) -> U (human)
- Position 19: U (mouse) -> C (human)

Length difference: 1 nt

*WARNING: 1 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

By analyzing the expression profile of ileal microRNAs and correlation analysis with intestinal microbiota, we found that Staphylococcus and Corynebacterium1 cooperated with miR-196a-1-3p and miR-3060-3p, respectively, to play a regulatory role in the process of high-altitude hypoxia-induced inte... (PMID: 36304467)

### Literature

1. Wan Z et al. (2022). *Lactobacillus johnsonii YH1136 plays a protective role against endogenous pathogenic bacteria induced intestinal dysfunction by reconstructing gut microbiota in mice exposed at high altitude.* Front Immunol. DOI: [10.3389/fimmu.2022.1007737](https://doi.org/10.3389/fimmu.2022.1007737) PMID: [36304467](https://pubmed.ncbi.nlm.nih.gov/36304467/)

---

## miR-187-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +2.64 | 9.85e-06 | 50.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-187-5p** - **31.8% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-187-5p) | `AGGCUACAACACAGGACCCGGG` | 22 nt |
| Human (hsa-miR-187-5p) | `GGCUACAACACAGGACCCGGGC` | 22 nt |

```
Mouse: AGGCUACAACACAGGACCCGGG
       X|XXXXX|XXXXX|XX||X||X
Human: GGCUACAACACAGGACCCGGGC
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: A (mouse) -> G (human) *(in seed region)*
- Position 3: G (mouse) -> C (human) *(in seed region)*
- Position 4: C (mouse) -> U (human) *(in seed region)*
- Position 5: U (mouse) -> A (human) *(in seed region)*
- Position 6: A (mouse) -> C (human) *(in seed region)*
- Position 7: C (mouse) -> A (human) *(in seed region)*
- Position 9: A (mouse) -> C (human)
- Position 10: C (mouse) -> A (human)
- Position 11: A (mouse) -> C (human)
- Position 12: C (mouse) -> A (human)
- Position 13: A (mouse) -> G (human)
- Position 15: G (mouse) -> A (human)
- Position 16: A (mouse) -> C (human)
- Position 19: C (mouse) -> G (human)
- Position 22: G (mouse) -> C (human)

*WARNING: 6 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-187-5p shares seed family 'CGUGUCU' with miR-187-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 17**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Nudcd3 | 1 | -0.566 |
| Prkar2a | 1 | -0.471 |
| Hipk3 | 1 | -0.467 |
| Lrfn1 | 1 | -0.443 |
| Fgf9 | 1 | -0.438 |
| Flrt2 | 1 | -0.417 |
| Apc | 1 | -0.4 |
| Kcnk10 | 1 | -0.376 |
| Zcchc2 | 1 | -0.366 |
| Acot11 | 1 | -0.33 |

**Top target gene: Nudcd3** (NudC domain containing 3)

*Function:* Predicted to enable unfolded protein binding activity. Predicted to be involved in protein folding. Predicted to be part of cytoplasmic dynein complex. Predicted to be active in cytoplasm. Orthologous to human NUDCD3 (NudC domain containing 3). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [209586](https://www.ncbi.nlm.nih.gov/gene/209586)

### Biological Function Summary

Dose-dependent upregulation of miR-155-5p and miR-187-5p was evident at opium dose >1500 g/month, with a corresponding increase of TNF-α and IL-10. (PMID: 35098407) Therefore, increasing consumption of opium probably enhances inflammation leading to immunomodulation and aberrant expression of hsa-miR-155-5p and hsa-miR-187-5p in opioid use disorder. (PMID: 35098407) In our prior study, we discovered that miR-187-5p expression was inhibited by HBx. (PMID: 37531206) To investigate the underlying molecular mechanism of HBx-mediated miR-187-5p downregulation in hepatocellular carcinoma cells, effects of HBx and miR-187-5p on hepatoma carcinoma cell were observed, as well as their interactions. (PMID: 37531206) Through in vitro and in vivo experiments, we demonstrated that overexpression of miR-187-5p inhibited proliferation, migration, and invasion. (PMID: 37531206)

### Literature

1. Purohit P et al. (2022). *Association of miR-155, miR-187 and Inflammatory Cytokines IL-6, IL-10 and TNF-α in Chronic Opium Abusers.* Inflammation. DOI: [10.1007/s10753-021-01566-0](https://doi.org/10.1007/s10753-021-01566-0) PMID: [35098407](https://pubmed.ncbi.nlm.nih.gov/35098407/)

2. Deng Y et al. (2023). *HBx promotes hepatocellular carcinoma progression by repressing the transcription level of miR-187-5p.* Aging (Albany NY). DOI: [10.18632/aging.204921](https://doi.org/10.18632/aging.204921) PMID: [37531206](https://pubmed.ncbi.nlm.nih.gov/37531206/)

3. Lin CY et al. (2021). *Lidocaine and Bupivacaine Downregulate MYB and DANCR lncRNA by Upregulating miR-187-5p in MCF-7 Cells.* Front Med (Lausanne). DOI: [10.3389/fmed.2021.732817](https://doi.org/10.3389/fmed.2021.732817) PMID: [35096852](https://pubmed.ncbi.nlm.nih.gov/35096852/)

4. Lou Y et al. (2016). *miR-187-5p Regulates Cell Growth and Apoptosis in Acute Lymphoblastic Leukemia via DKK2.* Oncol Res. DOI: [10.3727/096504016X14597766487753](https://doi.org/10.3727/096504016X14597766487753) PMID: [27296949](https://pubmed.ncbi.nlm.nih.gov/27296949/)

5. Xu Y et al. (2020). *miR-187-5p/apaf-1 axis was involved in oxidative stress-mediated apoptosis caused by ammonia via mitochondrial pathway in chicken livers.* Toxicol Appl Pharmacol. DOI: [10.1016/j.taap.2019.114869](https://doi.org/10.1016/j.taap.2019.114869) PMID: [31863799](https://pubmed.ncbi.nlm.nih.gov/31863799/)

---

## miR-670-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +4.05 | 3.09e-03 | 48.5 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-670-5p** - **86.4% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-670-5p) | `AUCCCUGAGUGUAUGUGGUGAA` | 22 nt |
| Human (hsa-miR-670-5p) | `GUCCCUGAGUGUAUGUGGUG` | 20 nt |

```
Mouse: AUCCCUGAGUGUAUGUGGUGAA
       X|||||||||||||||||||--
Human: GUCCCUGAGUGUAUGUGGUG
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: A (mouse) -> G (human) *(in seed region)*

Length difference: 2 nt

*WARNING: 1 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-670-5p shares seed family 'CCCUGAG' with miR-125b-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 846**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Nrm | 1 | -0.996 |
| Arid3a | 3 | -0.981 |
| Acer2 | 1 | -0.956 |
| Msrb3 | 1 | -0.899 |
| Bmf | 3 | -0.848 |
| Fam83h | 3 | -0.839 |
| Scn2b | 2 | -0.833 |
| Sertad3 | 1 | -0.814 |
| Lfng | 1 | -0.813 |
| Npl | 1 | -0.809 |

**Top target gene: Nrm** (nurim (nuclear envelope membrane protein))

*Function:* Predicted to be located in nuclear envelope. Predicted to be active in nuclear membrane. Is expressed in several structures, including brain ventricular layer; cranium; heart; metanephros; and nasal capsule. Human ortholog(s) of this gene implicated in alcohol dependence. Orthologous to human NRM (nurim). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [106582](https://www.ncbi.nlm.nih.gov/gene/106582)

### Biological Function Summary

However, the expression and function of miR-670-5p have not been evaluated in HCC to date. (PMID: 26796260) In this study, we examined and confirmed the over-expression of miR-670-5p in HCC and in hepatoma-derived cells Hep3B. (PMID: 26796260) At least 60% of HCC tissues showed a greater than three-fold enhance in the expression of miR-670-5p compared with paired adjacent non-cancerous tissues. (PMID: 26796260) Knockdown studies for miR-670-5p showed that the expression of miR-670-5p promoted cellular proliferation. (PMID: 26796260) In tissues and cells with high expression of miR-670-5p, decreased expression of PROX1, a miR-670-5p predicated target, was detected. (PMID: 26796260)

### Literature

1. Shi C et al. (2016). *MiR-670-5p induces cell proliferation in hepatocellular carcinoma by targeting PROX1.* Biomed Pharmacother. DOI: [10.1016/j.biopha.2015.07.030](https://doi.org/10.1016/j.biopha.2015.07.030) PMID: [26796260](https://pubmed.ncbi.nlm.nih.gov/26796260/)

2. Li HX et al. (2021). *[Effects of miR-670-5p on proliferation, migration and invasion of lung cancer cells].* Zhongguo Ying Yong Sheng Li Xue Za Zhi. DOI: [10.12047/j.cjap.6102.2021.046](https://doi.org/10.12047/j.cjap.6102.2021.046) PMID: [34816661](https://pubmed.ncbi.nlm.nih.gov/34816661/)

3. Zhang D et al. (2020). *Circular RNA SMARCA5 suppressed non-small cell lung cancer progression by regulating miR-670-5p/RBM24 axis.* Acta Biochim Biophys Sin (Shanghai). DOI: [10.1093/abbs/gmaa099](https://doi.org/10.1093/abbs/gmaa099) PMID: [33085761](https://pubmed.ncbi.nlm.nih.gov/33085761/)

4. Tang W et al. (2024). *circ-Erbb2ip from adipose-derived mesenchymal stem cell-derived exosomes promotes wound healing in diabetic mice by inducing the miR-670-5p/Nrf1 axis.* Cell Signal. DOI: [10.1016/j.cellsig.2024.111245](https://doi.org/10.1016/j.cellsig.2024.111245) PMID: [38849105](https://pubmed.ncbi.nlm.nih.gov/38849105/)

5. Zhang L et al. (2025). *Exosomal circDNAJB6 derived from decidual macrophages promotes preeclampsia progression via the miR-670-5p/TOB2 axis and by subsequently regulating the PPARγ/NF-κB pathway.* J Transl Med. DOI: [10.1186/s12967-025-07220-9](https://doi.org/10.1186/s12967-025-07220-9) PMID: [41121308](https://pubmed.ncbi.nlm.nih.gov/41121308/)

---

## miR-346-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Upregulated | +4.13 | 2.81e-02 | 35.5 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UGUCUGCCCGAGUGCCUGCCUCU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 188**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Tnfrsf12a | 1 | -0.915 |
| Rdx | 1 | -0.768 |
| Dym | 1 | -0.746 |
| Bcl6 | 2 | -0.711 |
| Gpr26 | 1 | -0.71 |
| Nr1h3 | 1 | -0.628 |
| Gm5868 | 1 | -0.599 |
| Slc43a2 | 1 | -0.599 |
| Sstr2 | 1 | -0.557 |
| Ago2 | 1 | -0.552 |

**Top target gene: Tnfrsf12a** (tumor necrosis factor receptor superfamily, member 12a)

*Function:* Involved in regulation of angiogenesis. Acts upstream of or within extrinsic apoptotic signaling pathway; positive regulation of axon extension; and substrate-dependent cell migration, cell attachment to substrate. Located in cell surface; plasma membrane; and ruffle. Is expressed in several structures, including adrenal medulla; alimentary system; genitourinary system; heart; and limb long bone. Orthologous to human TNFRSF12A (TNF receptor superfamily member 12A). [provided by Alliance of Genom...

*NCBI Gene ID:* [27279](https://www.ncbi.nlm.nih.gov/gene/27279)

### Biological Function Summary

MiR-346-5p is overexpressed in several cancers, including colorectal cancer (CRC). (PMID: 31953162) SW620 and HCT116 cells were selected and then transfected with miR-346-5p mimic, miR-346-5p inhibitor, or specific siRNAs targeting F-box/LRR-repeat protein 2 (FBXL2). (PMID: 31953162) CRC cells were co-transfected with miR-346-5p inhibitor and siFBXL2 to investigate the involvement of FBXL2. (PMID: 31953162) The effect of miR-346-5p knockdown on CRC tumorigenesis in vivo was investigated. (PMID: 31953162) Here, we found that miR-346-5p overexpression promoted, while miR-346-5p knockdown inhibited cell proliferation and G1-S transition. (PMID: 31953162)

### Literature

1. Pan S et al. (2020). *MiR-346-5p promotes colorectal cancer cell proliferation in vitro and in vivo by targeting FBXL2 and activating the β-catenin signaling pathway.* Life Sci. DOI: [10.1016/j.lfs.2020.117300](https://doi.org/10.1016/j.lfs.2020.117300) PMID: [31953162](https://pubmed.ncbi.nlm.nih.gov/31953162/)

2. Zhang Y et al. (2020). *MicroRNA-346-5p Regulates Differentiation of Bone Marrow-Derived Mesenchymal Stem Cells by Inhibiting Transmembrane Protein 9.* Biomed Res Int. DOI: [10.1155/2020/8822232](https://doi.org/10.1155/2020/8822232) PMID: [33299881](https://pubmed.ncbi.nlm.nih.gov/33299881/)

3. Shi J et al. (2021). *Hsa_circ_0069244 acts as the sponge of miR-346 to inhibit non-small cell lung cancer progression by regulating XPC expression.* Hum Cell. DOI: [10.1007/s13577-021-00573-5](https://doi.org/10.1007/s13577-021-00573-5) PMID: [34228324](https://pubmed.ncbi.nlm.nih.gov/34228324/)

4. Qiu WI et al. (2016). *[Effect of Xiaoai Jiedu Recipe on mIRNA Expression Profiles in H₂₂ Tumor-bearing Mice].* Zhongguo Zhong Xi Yi Jie He Za Zhi. PMID: [30645853](https://pubmed.ncbi.nlm.nih.gov/30645853/)

---

## miR-511-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -2.64 | 3.92e-02 | 0.8 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-511-3p** - **86.4% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-511-3p) | `AAUGUGUAGCAAAAGACAGGAU` | 22 nt |
| Human (hsa-miR-511-3p) | `AAUGUGUAGCAAAAGACAGA` | 20 nt |

```
Mouse: AAUGUGUAGCAAAAGACAGGAU
       |||||||||||||||||||X--
Human: AAUGUGUAGCAAAAGACAGA
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 20: G (mouse) -> A (human)

Length difference: 2 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-511-3p shares seed family 'AUGCCUU' with miR-532-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 217**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Gm26596 | 1 | -0.812 |
| Slc25a46 | 1 | -0.628 |
| Fhit | 1 | -0.611 |
| Cript | 1 | -0.587 |
| Bhlhb9 | 1 | -0.58 |
| Ndp | 1 | -0.551 |
| Csf1 | 1 | -0.551 |
| Ahsg | 1 | -0.549 |
| Csgalnact2 | 1 | -0.538 |
| Ccdc64 | 1 | -0.519 |

**Top target gene: Gm26596** (predicted gene, 26596)

*NCBI Gene ID:* [544737](https://www.ncbi.nlm.nih.gov/gene/544737)

### Biological Function Summary

M1 exosomes were transfected with NF-κB p50 siRNA and miR-511-3p to enhance M1 polarization and were surface-modified with IL4RPep-1, an IL4R-binding peptide, to target the IL4 receptor of TAMs (named IL4R-Exo(si/mi). (PMID: 34560422) Retraction: "Long noncoding RNA ZFPM2-AS1 is involved in lung adenocarcinoma via miR-511-3p/AFF4 pathway," by Juan Li, Jun Ge, Ye Yang, Bin Liu, Min Zheng, and Rui Shi, J Cell Biochem. (PMID: 36395200) Our previous studies have shown that miR-511-3p treatment has a beneficial effect in alleviating allergic airway inflammation. (PMID: 37996055) miR-511-3p knockout mice (miR-511-3p-/-) were generated by CRISPR/Cas and showed exacerbated airway hyper-responsiveness and Th2-associated allergic airway inflammation compared with wild-type (WT) mice after exposed to cockroach allergen. (PMID: 37996055) Intra-tracheal inhalation of Man-EV-miR-511-3p, which could effectively penetrate the airway mucus barrier and deliver functional miR-511-3p to lung macrophages, successfully reversed the increased airway inflammation observed in miR-511-3p-/- mice. (PMID: 37996055)

### Literature

1. Gunassekaran GR et al. (2021). *M1 macrophage exosomes engineered to foster M1 polarization and target the IL-4 receptor inhibit tumor growth by reprogramming tumor-associated macrophages into M1-like macrophages.* Biomaterials. DOI: [10.1016/j.biomaterials.2021.121137](https://doi.org/10.1016/j.biomaterials.2021.121137) PMID: [34560422](https://pubmed.ncbi.nlm.nih.gov/34560422/)

2. Unknown (2022). *Retraction.* J Cell Biochem. DOI: [10.1002/jcb.30337](https://doi.org/10.1002/jcb.30337) PMID: [36395200](https://pubmed.ncbi.nlm.nih.gov/36395200/)

3. Tu W et al. (2024). *Effective delivery of miR-511-3p with mannose-decorated exosomes with RNA nanoparticles confers protection against asthma.* J Control Release. DOI: [10.1016/j.jconrel.2023.11.034](https://doi.org/10.1016/j.jconrel.2023.11.034) PMID: [37996055](https://pubmed.ncbi.nlm.nih.gov/37996055/)

4. Do DC et al. (2019). *miR-511-3p protects against cockroach allergen-induced lung inflammation by antagonizing CCL2.* JCI Insight. DOI: [10.1172/jci.insight.126832](https://doi.org/10.1172/jci.insight.126832) PMID: [31536479](https://pubmed.ncbi.nlm.nih.gov/31536479/)

5. Ghafouri-Fard S et al. (2021). *The impact of non-coding RNAs on macrophage polarization.* Biomed Pharmacother. DOI: [10.1016/j.biopha.2021.112112](https://doi.org/10.1016/j.biopha.2021.112112) PMID: [34449319](https://pubmed.ncbi.nlm.nih.gov/34449319/)

---

## miR-294-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -4.74 | 3.71e-02 | 0.4 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AAAGUGCUUCCCUUUUGUGUGU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 75**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Fbxl3 | 1 | -0.502 |
| Nfib | 2 | -0.456 |
| Olig2 | 1 | -0.45 |
| Lhx6 | 2 | -0.432 |
| Smndc1 | 1 | -0.413 |
| March8 | 1 | -0.411 |
| Camk2n1 | 1 | -0.399 |
| Pbx3 | 1 | -0.391 |
| Syde1 | 1 | -0.384 |
| Mtf1 | 2 | -0.361 |

**Top target gene: Fbxl3** (F-box and leucine-rich repeat protein 3)

*Function:* Contributes to ubiquitin-protein transferase activity. Involved in several processes, including SCF-dependent proteasomal ubiquitin-dependent protein catabolic process; entrainment of circadian clock by photoperiod; and protein destabilization. Located in cytosol and nucleus. Is expressed in embryo; extraembryonic component; inner cell mass; and trophectoderm. Orthologous to human FBXL3 (F-box and leucine rich repeat protein 3). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [50789](https://www.ncbi.nlm.nih.gov/gene/50789)

### Biological Function Summary

By constructing the circ/lncRNA-miRNA-mRNA network, we found that miR-291a-3p, miR-294-3p, and miR-295-3p may serve as key targets influencing early embryo development via multiple pathways, including the Toll-like receptor signaling pathway and p53 signaling pathway. (PMID: 40307905) Inhibition of miR-294-3p/5p did not affect ZGA initiation or embryo development, whereas pri-miR-290 knockdown decreased ZGA gene expression and slowed embryonic development. (PMID: 34907414) To clarify the mechanism of action, 33 candidate miR-294-3p target genes were screened from three databases, and miR-294-3p directly targeted the 3'-untranslated region of Cdkn1a (p21) mRNA. (PMID: 34907414) The data demonstrate that SARS-CoV-2-RBD treatment in pre-existing diabetes conditions in hACE2 (T2DM + RBD) mice results in the aggravated osteoblast inflammation and downregulation of Glucose transporter 4 (Glut4) expression via upregulation of miR-294-3p expression. (PMID: 35803174) The role of one of the regulated miRNA (miR-294-3p) in L. (PMID: 30949455)

### Literature

1. Hao J et al. (2025). *Whole-transcriptome sequencing reveals the effects of acupuncture on early embryos post-IVF-ET in poor ovarian response.* J Ovarian Res. DOI: [10.1186/s13048-025-01682-7](https://doi.org/10.1186/s13048-025-01682-7) PMID: [40307905](https://pubmed.ncbi.nlm.nih.gov/40307905/)

2. Li X et al. (2022). *MiR-290 family maintains developmental potential by targeting p21 in mouse preimplantation embryos‡.* Biol Reprod. DOI: [10.1093/biolre/ioab227](https://doi.org/10.1093/biolre/ioab227) PMID: [34907414](https://pubmed.ncbi.nlm.nih.gov/34907414/)

3. Behera J et al. (2022). *Diabetic Covid-19 severity: Impaired glucose tolerance and pathologic bone loss.* Biochem Biophys Res Commun. DOI: [10.1016/j.bbrc.2022.06.043](https://doi.org/10.1016/j.bbrc.2022.06.043) PMID: [35803174](https://pubmed.ncbi.nlm.nih.gov/35803174/)

4. Fernandes JCR et al. (2019). *Melatonin and Leishmania amazonensis Infection Altered miR-294, miR-30e, and miR-302d Impacting on Tnf, Mcp-1, and Nos2 Expression.* Front Cell Infect Microbiol. DOI: [10.3389/fcimb.2019.00060](https://doi.org/10.3389/fcimb.2019.00060) PMID: [30949455](https://pubmed.ncbi.nlm.nih.gov/30949455/)

---

## miR-150-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -5.60 | 3.29e-02 | 0.2 |
| Spleen | Upregulated | +5.60 | 6.52e-13 | 338.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-150-3p** - **95.5% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-150-3p) | `CUGGUACAGGCCUGGGGGAUAG` | 22 nt |
| Human (hsa-miR-150-3p) | `CUGGUACAGGCCUGGGGGACAG` | 22 nt |

```
Mouse: CUGGUACAGGCCUGGGGGAUAG
       |||||||||||||||||||X||
Human: CUGGUACAGGCCUGGGGGACAG
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 20: U (mouse) -> C (human)

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-150-3p shares seed family 'CUCCCAA' with miR-150-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 326**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Myb | 2 | -0.752 |
| Smr3a | 1 | -0.721 |
| Gm7714 | 1 | -0.655 |
| Prorsd1 | 1 | -0.637 |
| Shisa4 | 1 | -0.614 |
| Cxcl1 | 1 | -0.532 |
| Myh1 | 1 | -0.52 |
| Pdia3 | 1 | -0.507 |
| Hilpda | 1 | -0.471 |
| Them4 | 1 | -0.468 |

**Top target gene: Myb** (Myb proto-oncogene, transcription factor)

*Function:* Enables DNA-binding transcription activator activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and WD40-repeat domain binding activity. Involved in positive regulation of transcription by RNA polymerase II. Acts upstream of or within several processes, including cellular response to cytokine stimulus; hematopoietic or lymphoid organ development; and hemopoiesis. Located in cytosol and nucleus. Part of RNA polymerase II transcript...

*NCBI Gene ID:* [17863](https://www.ncbi.nlm.nih.gov/gene/17863)

### Biological Function Summary

We also found that miR-4298, miR-296-3p, miR-150-3p, miR-493-5p, and miR-6742-5p play important roles in cancer and PD. (PMID: 39329952) EBOV-encoded miRNAs such as miR-VP-3p and miR-1-5p and anti-EBOV host cell miRNAs such as has-miR-150-3p, has-miR-103b and has-miR-145-3p might be a possible diagnostic biomarker or druggable targets. (PMID: 39184819) The transportation mechanism from FLSs to chondrocytes was studied using the EV inhibitor GW4869, and the FLSs were transfected with a miR-150-3p mimic or inhibitor. (PMID: 36078172) RESULTS: The chondrocytes could uptake fluorescent-labeled miR-150-3p mimics and FLS-EVs, and GW4869 suppressed this uptake. (PMID: 36078172) The overexpression of miR-150-3p could significantly reduce the concentrations of pro-inflammatory cytokines in the cell culture medium and the expression of the miR-150-3p target T cell receptor-interacting molecule 14 (Trim14), as well as the innate immune-related factors, including nuclear fac... (PMID: 36078172)

### Literature

1. Liu T et al. (2024). *Disulfidptosis: A New Target for Parkinson's Disease and Cancer.* Curr Issues Mol Biol. DOI: [10.3390/cimb46090600](https://doi.org/10.3390/cimb46090600) PMID: [39329952](https://pubmed.ncbi.nlm.nih.gov/39329952/)

2. Kakavandi E et al. (2024). *A Review of the Interaction between miRNAs and Ebola Virus.* Int J Mol Cell Med. DOI: [10.22088/IJMCM.BUMS.13.2.210](https://doi.org/10.22088/IJMCM.BUMS.13.2.210) PMID: [39184819](https://pubmed.ncbi.nlm.nih.gov/39184819/)

3. Wang H et al. (2022). *Extracellular Vesicle-Mediated miR-150-3p Delivery in Joint Homeostasis: A Potential Treatment for Osteoarthritis?* Cells. DOI: [10.3390/cells11172766](https://doi.org/10.3390/cells11172766) PMID: [36078172](https://pubmed.ncbi.nlm.nih.gov/36078172/)

4. Tan Z et al. (2018). *MiR-150-3p targets SP1 and suppresses the growth of glioma cells.* Biosci Rep. DOI: [10.1042/BSR20180019](https://doi.org/10.1042/BSR20180019) PMID: [29654167](https://pubmed.ncbi.nlm.nih.gov/29654167/)

5. Bueno LCM et al. (2022). *Increased Serum Mir-150-3p Expression Is Associated with Radiological Lung Injury Improvement in Patients with COVID-19.* Viruses. DOI: [10.3390/v14071363](https://doi.org/10.3390/v14071363) PMID: [35891345](https://pubmed.ncbi.nlm.nih.gov/35891345/)

---

## miR-490-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -7.56 | 1.95e-03 | 0.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-490-3p** - **100% identical** (22 nt)

Sequence: `CAACCUGGAGGACUCCAUGCUG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 201**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Nop10 | 1 | -0.925 |
| Ddx17 | 1 | -0.504 |
| Dlst | 1 | -0.488 |
| Slc35a4 | 1 | -0.484 |
| Psmd11 | 2 | -0.478 |
| Hoxc4 | 1 | -0.462 |
| Amd2 | 1 | -0.444 |
| Ppp1r2 | 1 | -0.43 |
| Amd1 | 1 | -0.417 |
| Camk2n1 | 1 | -0.406 |

**Top target gene: Nop10** (NOP10 ribonucleoprotein)

*Function:* Predicted to enable box H/ACA snoRNA binding activity and telomerase RNA binding activity. Predicted to be involved in snRNA pseudouridine synthesis; snoRNA guided rRNA pseudouridine synthesis; and telomere maintenance via telomerase. Predicted to be located in nuclear body. Predicted to be part of box H/ACA snoRNP complex and box H/ACA telomerase RNP complex. Is expressed in several structures, including alimentary system; brain; genitourinary system; hemolymphoid system; and integumental syste...

*NCBI Gene ID:* [66181](https://www.ncbi.nlm.nih.gov/gene/66181)

### Biological Function Summary

miR-490-3p and miR-490-5p possess antitumor properties. (PMID: 34345303) miR-490-3p dysfunction has been associated with malignancies including colorectal cancer, while the abnormal function of miR-490-5p has been more considerably associated with bladder cancer (for example). (PMID: 34345303) At present, there are 30 and 11 target genes of miR-490-3p and miR-490-5p, respectively, that have been experimentally verified, of which the cyclin D1 (CCND1) gene is a common target. (PMID: 34345303) Through these target genes, miR-490-3p and miR-490-5p are involved in 7 and 3 signaling pathways, respectively, of which only 2 are shared regulatory signaling pathways. (PMID: 34345303) The present review introduces two competing endogenous RNA (ceRNA) regulatory networks centered on miR-490-3p and miR-490-5p. (PMID: 34345303)

### Literature

1. Li Y et al. (2021). *MicroRNA-490-3p and -490-5p in carcinogenesis: Separate or the same goal?* Oncol Lett. DOI: [10.3892/ol.2021.12939](https://doi.org/10.3892/ol.2021.12939) PMID: [34345303](https://pubmed.ncbi.nlm.nih.gov/34345303/)

2. Jiang J et al. (2022). *miR-490-3p Alleviates Cardiomyocyte Injury via Targeting FOXO1.* Protein Pept Lett. DOI: [10.2174/0929866529666220819120736](https://doi.org/10.2174/0929866529666220819120736) PMID: [35986524](https://pubmed.ncbi.nlm.nih.gov/35986524/)

3. Li Z et al. (2020). *MiR-490-3p Inhibits the Malignant Progression of Lung Adenocarcinoma.* Cancer Manag Res. DOI: [10.2147/CMAR.S258182](https://doi.org/10.2147/CMAR.S258182) PMID: [33154676](https://pubmed.ncbi.nlm.nih.gov/33154676/)

4. Coskunpinar E et al. (2023). *Investigation of the miR-637 and miR-523-5p as candidate biomarkers in breast cancer.* Bratisl Lek Listy. DOI: [10.4149/BLL_2023_125](https://doi.org/10.4149/BLL_2023_125) PMID: [37874803](https://pubmed.ncbi.nlm.nih.gov/37874803/)

5. Xu C et al. (2025). *Prognostic Significance of CDK1 in Ovarian and Cervical Cancers.* J Cancer. DOI: [10.7150/jca.104371](https://doi.org/10.7150/jca.104371) PMID: [39991589](https://pubmed.ncbi.nlm.nih.gov/39991589/)

---

## miR-208b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -7.02 | 3.59e-02 | 0.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-208b-3p** - **100% identical** (22 nt)

Sequence: `AUAAGACGAACAAAAGGUUUGU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 77**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Ube2v2 | 2 | -0.608 |
| Vav3 | 1 | -0.584 |
| Csnk2a2 | 1 | -0.533 |
| Ets1 | 1 | -0.461 |
| Stc1 | 1 | -0.424 |
| Elavl4 | 2 | -0.401 |
| Celf2 | 1 | -0.31 |
| Ybx1 | 1 | -0.299 |
| Lin28b | 1 | -0.287 |
| Med13 | 1 | -0.276 |

**Top target gene: Ube2v2** (ubiquitin-conjugating enzyme E2 variant 2)

*Function:* Acts upstream of or within error-free postreplication DNA repair. Predicted to be located in nucleoplasm. Predicted to be part of UBC13-MMS2 complex. Predicted to be active in nucleus. Is expressed in cerebral cortex ventricular layer; cortical plate; and embryo. Orthologous to human UBE2V2 (ubiquitin conjugating enzyme E2 V2). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [70620](https://www.ncbi.nlm.nih.gov/gene/70620)

### Biological Function Summary

Upregulation of miR-208b-3p, miR-143-3p, miR-145-3p and miR-152-3p, and down-regulation of miR-183-5p were further validated in the validation group. (PMID: 36723013) In conclusion, our findings indicate that plasma EVs miR-208b-3p and miR-143-3p may serve as promising biomarkers in predicting SCD in patients with ACS, as well as postmortem forensic diagnosis of the cause of death due to ACS. (PMID: 36723013) Differential expression of miR-208b-3p is associated with myocardial injury. (PMID: 32070878) But it is unknown that aberrant expression of miR-208b-3p is implicated in myocardial protection of Dex. (PMID: 32070878) qRT-PCR was performed to detect expression levels of miR-208b-3p in H9C2 undergoing HR, Dex preconditioning, overexpression of miR-208b-3p or inhibition, and to assess expression of Med13 in H9C2 following knockdown of Med13 mRNA. (PMID: 32070878)

### Literature

1. Clément AA et al. (2025). *First trimester circulating miR-208b-3p and miR-26a-1-3p are relevant to the prediction of gestational hypertension.* BMC Pregnancy Childbirth. DOI: [10.1186/s12884-025-07349-x](https://doi.org/10.1186/s12884-025-07349-x) PMID: [40057749](https://pubmed.ncbi.nlm.nih.gov/40057749/)

2. Huang S et al. (2023). *Plasma extracellular vesicles microRNA-208b-3p and microRNA-143-3p as novel biomarkers for sudden cardiac death prediction in acute coronary syndrome.* Mol Omics. DOI: [10.1039/d2mo00257d](https://doi.org/10.1039/d2mo00257d) PMID: [36723013](https://pubmed.ncbi.nlm.nih.gov/36723013/)

3. Wang Z et al. (2020). *Dexmedetomidine protects H9C2 against hypoxia/reoxygenation injury through miR-208b-3p/Med13/Wnt signaling pathway axis.* Biomed Pharmacother. DOI: [10.1016/j.biopha.2020.110001](https://doi.org/10.1016/j.biopha.2020.110001) PMID: [32070878](https://pubmed.ncbi.nlm.nih.gov/32070878/)

4. Hupfeld J et al. (2021). *miR-208b Reduces the Expression of Kcnj5 in a Cardiomyocyte Cell Line.* Biomedicines. DOI: [10.3390/biomedicines9070719](https://doi.org/10.3390/biomedicines9070719) PMID: [34201741](https://pubmed.ncbi.nlm.nih.gov/34201741/)

5. Giménez-Escamilla I et al. (2024). *Alterations in Mitochondrial Oxidative Phosphorylation System: Relationship of Complex V and Cardiac Dysfunction in Human Heart Failure.* Antioxidants (Basel). DOI: [10.3390/antiox13030285](https://doi.org/10.3390/antiox13030285) PMID: [38539818](https://pubmed.ncbi.nlm.nih.gov/38539818/)

---

## miR-122-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -13.29 | 4.24e-04 | 0.0 |
| Liver | Upregulated | +11.54 | 2.48e-10 | 590.3 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-122-3p** - **27.3% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-122-3p) | `AAACGCCAUUAUCACACUAAAU` | 22 nt |
| Human (hsa-miR-122-3p) | `AACGCCAUUAUCACACUAAAUA` | 22 nt |

```
Mouse: AAACGCCAUUAUCACACUAAAU
       ||XXX|XX|XXXXXXXXX||XX
Human: AACGCCAUUAUCACACUAAAUA
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 3: A (mouse) -> C (human) *(in seed region)*
- Position 4: C (mouse) -> G (human) *(in seed region)*
- Position 5: G (mouse) -> C (human) *(in seed region)*
- Position 7: C (mouse) -> A (human) *(in seed region)*
- Position 8: A (mouse) -> U (human) *(in seed region)*
- Position 10: U (mouse) -> A (human)
- Position 11: A (mouse) -> U (human)
- Position 12: U (mouse) -> C (human)
- Position 13: C (mouse) -> A (human)
- Position 14: A (mouse) -> C (human)
- Position 15: C (mouse) -> A (human)
- Position 16: A (mouse) -> C (human)
- Position 17: C (mouse) -> U (human)
- Position 18: U (mouse) -> A (human)
- Position 21: A (mouse) -> U (human)
- Position 22: U (mouse) -> A (human)

*WARNING: 5 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-122-3p shares seed family 'GGAGUGU' with miR-122-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 215**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Slc25a34 | 1 | -0.899 |
| Slc1a5 | 1 | -0.761 |
| Aldoa | 1 | -0.671 |
| Vamp3 | 1 | -0.669 |
| Fundc2 | 1 | -0.668 |
| Sh2d1a | 1 | -0.664 |
| Grem2 | 1 | -0.631 |
| Ctdnep1 | 1 | -0.618 |
| P4ha1 | 1 | -0.581 |
| Slc41a1 | 1 | -0.58 |

**Top target gene: Slc25a34** (solute carrier family 25, member 34)

*Function:* Acts upstream of or within blastocyst hatching. Located in mitochondrion. Is expressed in early conceptus. Orthologous to human SLC25A34 (solute carrier family 25 member 34). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [384071](https://www.ncbi.nlm.nih.gov/gene/384071)

### Biological Function Summary

However, the specific role of miR-122-3p in pyroptosis during sepsis progression and its underlying mechanisms remain to be fully elucidated. (PMID: 37625833) We observed that overexpression of miR-122-3p effectively restored cell viability and attenuated the expression of key inflammatory markers promoted by LPS, such as caspase-1, pro-caspase-1, IL-18, IL-1β, NLRP3, apoptosis-associated speck-like protein containing CARD, and cleaved- gasdermin-D. (PMID: 37625833) Our data indicate that miR-122-3p is capable of directly bounding to NLRP1 and inhibiting its expression. (PMID: 37625833) CONCLUSIONS: These results confirmed that miR-122-3p plays a crucial role in the inhibition of sepsis by suppressing macrophage pyroptosis in an NLRP1-dependent manner. (PMID: 37625833) Therefore, miR-122-3p presents as a promising therapeutic target for sepsis. (PMID: 37625833)

### Literature

1. Li M et al. (2023). *miR-122-3p Alleviates LPS-Induced Pyroptosis of Macrophages via Targeting NLRP1.* Ann Clin Lab Sci. PMID: [37625833](https://pubmed.ncbi.nlm.nih.gov/37625833/)

2. Zhao SR et al. (2019). *Role of Hsa-miR-122-3p in steroid-induced necrosis of femoral head.* Eur Rev Med Pharmacol Sci. DOI: [10.26355/eurrev_201908_18628](https://doi.org/10.26355/eurrev_201908_18628) PMID: [31389574](https://pubmed.ncbi.nlm.nih.gov/31389574/)

3. López-Sánchez GN et al. (2022). *Hepatic mir-122-3p, mir-140-5p and mir-148b-5p expressions are correlated with cytokeratin-18 serum levels in MAFLD.* Ann Hepatol. DOI: [10.1016/j.aohep.2022.100756](https://doi.org/10.1016/j.aohep.2022.100756) PMID: [36096296](https://pubmed.ncbi.nlm.nih.gov/36096296/)

4. Song B et al. (2024). *Exosomal miR-122-3p represses the growth and metastasis of MCF-7/ADR cells by targeting GRK4-mediated activation of the Wnt/β-catenin pathway.* Cell Signal. DOI: [10.1016/j.cellsig.2024.111101](https://doi.org/10.1016/j.cellsig.2024.111101) PMID: [38365112](https://pubmed.ncbi.nlm.nih.gov/38365112/)

5. Deng W et al. (2025). *Exploring the role of glycolysis in the pathogenesis of erectile dysfunction in diabetes.* Transl Androl Urol. DOI: [10.21037/tau-2025-6](https://doi.org/10.21037/tau-2025-6) PMID: [40226065](https://pubmed.ncbi.nlm.nih.gov/40226065/)

---

## miR-122-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -13.78 | 5.18e-05 | 0.0 |
| Liver | Upregulated | +11.66 | 8.47e-13 | 750.2 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-122-5p** - **100% identical** (22 nt)

Sequence: `UGGAGUGUGACAAUGGUGUUUG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 215**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Slc25a34 | 1 | -0.899 |
| Slc1a5 | 1 | -0.761 |
| Aldoa | 1 | -0.671 |
| Vamp3 | 1 | -0.669 |
| Fundc2 | 1 | -0.668 |
| Sh2d1a | 1 | -0.664 |
| Grem2 | 1 | -0.631 |
| Ctdnep1 | 1 | -0.618 |
| P4ha1 | 1 | -0.581 |
| Slc41a1 | 1 | -0.58 |

**Top target gene: Slc25a34** (solute carrier family 25, member 34)

*Function:* Acts upstream of or within blastocyst hatching. Located in mitochondrion. Is expressed in early conceptus. Orthologous to human SLC25A34 (solute carrier family 25 member 34). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [384071](https://www.ncbi.nlm.nih.gov/gene/384071)

### Biological Function Summary

Of them, the expression of miR-122-5p was significantly upregulated in SLE exosomes, and positively correlated with systemic lupus erythematosus disease activity index (SLEDAI) and the dsDNA levels. (PMID: 39702207) Compared with SLE exosomes, inhibition of circulating exosomal miR-122-5p from SLE patients relieved lupus clinical aspects and polarization of macrophage. (PMID: 39702207) SLE exosomal miR-122-5p motivated M1 macrophage polarization by targeting FOXO3/NF-κB signaling pathway. (PMID: 39702207) Based on these findings, we conclude that SLE exosomal miR-122-5p can promote M1 macrophage polarization via targeting FOXO3/NF-κB signaling pathway and participate in pathogenesis of SLE. (PMID: 39702207) Collectively, plasma-derived exosomal miR-122-5p is a promising and effective target for treating SLE. (PMID: 39702207)

### Literature

1. Ji J et al. (2024). *Circulating plasma derived exosomes from systemic lupus erythematosus aggravate lupus nephritis through miR-122-5p/FOXO3-mediated macrophage activation.* J Nanobiotechnology. DOI: [10.1186/s12951-024-03063-6](https://doi.org/10.1186/s12951-024-03063-6) PMID: [39702207](https://pubmed.ncbi.nlm.nih.gov/39702207/)

2. Li K et al. (2022). *Anti-inflammatory and immunomodulatory effects of the extracellular vesicles derived from human umbilical cord mesenchymal stem cells on osteoarthritis via M2 macrophages.* J Nanobiotechnology. DOI: [10.1186/s12951-021-01236-1](https://doi.org/10.1186/s12951-021-01236-1) PMID: [35057811](https://pubmed.ncbi.nlm.nih.gov/35057811/)

3. Liang Y et al. (2023). *Adipose Mesenchymal Stromal Cell-Derived Exosomes Carrying MiR-122-5p Antagonize the Inhibitory Effect of Dihydrotestosterone on Hair Follicles by Targeting the TGF-β1/SMAD3 Signaling Pathway.* Int J Mol Sci. DOI: [10.3390/ijms24065703](https://doi.org/10.3390/ijms24065703) PMID: [36982775](https://pubmed.ncbi.nlm.nih.gov/36982775/)

4. Yu X et al. (2025). *Defective neutrophil-derived exosomes facilitate macrophage activation through miR-122-5p in Behçet's disease.* Nat Commun. DOI: [10.1038/s41467-025-63348-8](https://doi.org/10.1038/s41467-025-63348-8) PMID: [40897707](https://pubmed.ncbi.nlm.nih.gov/40897707/)

5. Derumeaux GA et al. (2021). *MicroRNA, miR-122-5p, Stiffens the Diabetic Heart.* JACC Cardiovasc Imaging. DOI: [10.1016/j.jcmg.2021.01.025](https://doi.org/10.1016/j.jcmg.2021.01.025) PMID: [33744152](https://pubmed.ncbi.nlm.nih.gov/33744152/)

---

## miR-295-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -7.12 | 5.62e-03 | 0.0 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AAAGUGCUACUACUUUUGAGUCU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 81**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Lcor | 3 | -0.746 |
| Phc3 | 1 | -0.654 |
| Syap1 | 1 | -0.587 |
| Btg1 | 1 | -0.574 |
| Tgfbr2 | 2 | -0.522 |
| Dcaf6 | 1 | -0.473 |
| Nr2e3 | 1 | -0.472 |
| Scnn1g | 1 | -0.46 |
| Irf2bp2 | 1 | -0.394 |
| Tfap4 | 1 | -0.387 |

**Top target gene: Lcor** (ligand dependent nuclear receptor corepressor)

*Function:* Enables chromatin binding activity. Involved in transcription initiation-coupled chromatin remodeling. Acts upstream of or within negative regulation of transcription by RNA polymerase II and transcription by RNA polymerase II. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. Is expressed in several structures, including 1st branchial arch; genitourinary system; long bone epiphysis; nervous system; and sensory organ. Orthologous to human LCOR (ligand dependent nuclear r...

*NCBI Gene ID:* [212391](https://www.ncbi.nlm.nih.gov/gene/212391)

### Biological Function Summary

By constructing the circ/lncRNA-miRNA-mRNA network, we found that miR-291a-3p, miR-294-3p, and miR-295-3p may serve as key targets influencing early embryo development via multiple pathways, including the Toll-like receptor signaling pathway and p53 signaling pathway. (PMID: 40307905) Discovery-driven experiments identified miR-295-3p within sEVs as a possible mediator of the VAT-heart axis, which impaired cardiac autophagy by binding to Ulk1 mRNA. (PMID: 41645491) Specifically, VAT-derived sEVs, miR-295-3p, and the resultant disruption of cardiac autophagy contribute significantly to the pathogenesis of HFpEF. (PMID: 41645491) In the present study, miR-25-5p, miR-105, miR-106b-5p, miR-154-3p, miR-20b-5p, miR-295-3p, miR-291-3p, miR-301b, miR-352, and miR-93-5p were predicted to target TXNIP mRNA from the databases of miRDB, Targetscan, and microT-CDS. (PMID: 36289253) Both diets altered the expression of several liver homeostasis-related microRNAs, including miR-190b-5p, miR-130b-3p, miR-376c-3p, miR-411-5p, miR-29c-3p, miR-295-3p, and miR-467d-5p, with the methionine-deficient diet causing a more substantial effect. (PMID: 35314295)

### Literature

1. Hao J et al. (2025). *Whole-transcriptome sequencing reveals the effects of acupuncture on early embryos post-IVF-ET in poor ovarian response.* J Ovarian Res. DOI: [10.1186/s13048-025-01682-7](https://doi.org/10.1186/s13048-025-01682-7) PMID: [40307905](https://pubmed.ncbi.nlm.nih.gov/40307905/)

2. Pan Q et al. (2026). *Small extracellular vesicle-mediated adipocyte-cardiomyocyte crosstalk exacerbates heart failure with preserved ejection fraction.* Cardiovasc Res. DOI: [10.1093/cvr/cvag030](https://doi.org/10.1093/cvr/cvag030) PMID: [41645491](https://pubmed.ncbi.nlm.nih.gov/41645491/)

3. Wang J et al. (2022). *MicroRNA-25-5p negatively regulates TXNIP expression and relieves inflammatory responses of brain induced by lipopolysaccharide.* Sci Rep. DOI: [10.1038/s41598-022-21169-5](https://doi.org/10.1038/s41598-022-21169-5) PMID: [36289253](https://pubmed.ncbi.nlm.nih.gov/36289253/)

4. Aissa AF et al. (2022). *Epigenetic changes induced in mice liver by methionine-supplemented and methionine-deficient diets.* Food Chem Toxicol. DOI: [10.1016/j.fct.2022.112938](https://doi.org/10.1016/j.fct.2022.112938) PMID: [35314295](https://pubmed.ncbi.nlm.nih.gov/35314295/)

5. Russo R et al. (2021). *MiRNAs Expression Profiling in Raw264.7 Macrophages after Nfatc1-Knockdown Elucidates Potential Pathways Involved in Osteoclasts Differentiation.* Biology (Basel). DOI: [10.3390/biology10111080](https://doi.org/10.3390/biology10111080) PMID: [34827073](https://pubmed.ncbi.nlm.nih.gov/34827073/)

---

## miR-1912-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -21.37 | 4.37e-05 | 0.0 |
| Lung | Upregulated | +9.40 | 1.96e-16 | 765.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-1912-5p** - **31.8% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-1912-5p) | `UGCUCAUUGCAUGGGCUGUGUA` | 22 nt |
| Human (hsa-miR-1912-5p) | `CUCAUUGCAUGGGCUGUGUAUA` | 22 nt |

```
Mouse: UGCUCAUUGCAUGGGCUGUGUA
       XX|XXXXXXXXX|XXX|||X||
Human: CUCAUUGCAUGGGCUGUGUAUA
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: U (mouse) -> C (human) *(in seed region)*
- Position 2: G (mouse) -> U (human) *(in seed region)*
- Position 4: U (mouse) -> A (human) *(in seed region)*
- Position 5: C (mouse) -> U (human) *(in seed region)*
- Position 6: A (mouse) -> U (human) *(in seed region)*
- Position 7: U (mouse) -> G (human) *(in seed region)*
- Position 8: U (mouse) -> C (human) *(in seed region)*
- Position 9: G (mouse) -> A (human)
- Position 10: C (mouse) -> U (human)
- Position 11: A (mouse) -> G (human)
- Position 12: U (mouse) -> G (human)
- Position 14: G (mouse) -> C (human)
- Position 15: G (mouse) -> U (human)
- Position 16: C (mouse) -> G (human)
- Position 20: G (mouse) -> A (human)

*WARNING: 7 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-1298-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Kidney | Downregulated | -23.89 | 3.87e-06 | 0.0 |
| Lung | Upregulated | +11.35 | 7.15e-29 | 1688.9 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-1298-5p** - **100% identical** (22 nt)

Sequence: `UUCAUUCGGCUGUCCAGAUGUA`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 121**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Eif4enif1 | 1 | -0.462 |
| Plet1 | 1 | -0.341 |
| AI317395 | 1 | -0.311 |
| Med6 | 1 | -0.301 |
| D1Ertd622e | 4 | -0.26 |
| Nacc1 | 1 | -0.252 |
| Cox17 | 1 | -0.249 |
| Drosha | 1 | -0.22 |
| Ept1 | 1 | -0.212 |
| Otud1 | 1 | -0.197 |

**Top target gene: Eif4enif1** (eukaryotic translation initiation factor 4E nuclear import factor 1)

*Function:* Enables mRNA binding activity. Acts upstream of or within negative regulation of neuron differentiation; negative regulation of translation; and stem cell population maintenance. Located in P-body; cytosol; and nucleus. Is expressed in several structures, including cerebral cortex; early conceptus; epithelium; metanephros; and ovary. Orthologous to human EIF4ENIF1 (eukaryotic translation initiation factor 4E nuclear import factor 1). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [74203](https://www.ncbi.nlm.nih.gov/gene/74203)

### Biological Function Summary

However,there are not many studies of exosomal miRNAs in sepsis and sepsis lung injury.miR-1298-5p and suppressor of cytokine signaling 6 (SOCS6) were silenced or overexpressed in human bronchial epithelial cells (BEAS-2B). (PMID: 34100174) miR-1298-5p directly targeted SOCS6. (PMID: 34100174) Overexpressing SOCS6 reversed miR-1298-5p-induced cell permeability and inflammatory response. (PMID: 34100174) Exosomes isolated from patients of sepsis lung injury increased cell permeability and inflammatory response in BEAS-2B cells through exosomal miR-1298-5p which targeted SOCS6 via STAT3 pathway. (PMID: 34100174) Furthermore, the downregulation of miR-1298-5p levels remarkably inhibited autophagy, ultimately increasing the intracellular H. (PMID: 35192930)

### Literature

1. Ma J et al. (2021). *Inhibition of miR-1298-5p attenuates sepsis lung injury by targeting SOCS6.* Mol Cell Biochem. DOI: [10.1007/s11010-021-04170-w](https://doi.org/10.1007/s11010-021-04170-w) PMID: [34100174](https://pubmed.ncbi.nlm.nih.gov/34100174/)

2. Li X et al. (2022). *MiR-1298-5p level downregulation induced by Helicobacter pylori infection inhibits autophagy and promotes gastric cancer development by targeting MAP2K6.* Cell Signal. DOI: [10.1016/j.cellsig.2022.110286](https://doi.org/10.1016/j.cellsig.2022.110286) PMID: [35192930](https://pubmed.ncbi.nlm.nih.gov/35192930/)

3. Gao S et al. (2023). *CircPKM2 aggravates the progression of non-small cell lung cancer by regulating MTDH via miR-1298-5p.* Thorac Cancer. DOI: [10.1111/1759-7714.15092](https://doi.org/10.1111/1759-7714.15092) PMID: [37675591](https://pubmed.ncbi.nlm.nih.gov/37675591/)

4. Chen X et al. (2025). *Upregulated miR-1298-5p sparks inflammatory onset and orchestrates pediatric dry eye disease progression.* Int Ophthalmol. DOI: [10.1007/s10792-025-03716-x](https://doi.org/10.1007/s10792-025-03716-x) PMID: [40938462](https://pubmed.ncbi.nlm.nih.gov/40938462/)

5. Li H et al. (2021). *Hsa_circ_0110757 upregulates ITGA1 to facilitate temozolomide resistance in glioma by suppressing hsa-miR-1298-5p.* Cell Death Dis. DOI: [10.1038/s41419-021-03533-x](https://doi.org/10.1038/s41419-021-03533-x) PMID: [33674567](https://pubmed.ncbi.nlm.nih.gov/33674567/)

---

## miR-12195-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Upregulated | +6.76 | 4.36e-19 | 613.2 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CAGACAAGACUGUUAUACCC`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-122b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Upregulated | +10.45 | 7.88e-11 | 557.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-122b-3p** - **100% identical** (22 nt)

Sequence: `AAACACCAUUGUCACACUCCAC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

RESULTS: By RNA sequencing and a miRNA-mRNA-PPI network analysis, we identified miR-615-5p and miR-122b-3p as possible miRNAs associated with keloids, as they differed most significantly in keloids. (PMID: 38242738) Relevant microRNAs included upstream regulator miR-132, enriched miR-124-3p, miR-122b-3p, miR-146-5p (HCM LV and LA), miR-370, miR-1185-5p, miR-12194-3p (HCM LV), miR-153-3p, miR-185-5p, and miR-185-3p (HCM LA). (PMID: 40725010) Based on qPCR, we validated COMMD1B, MOAP1, lncRNA CAPN15, lncRNA ALDH1L2, miR-3473b and miR-1964-3p were upregulated in thrombin-stimulated OM-MSCs, and GM20431, lncRNA GAPDH and miR-122b-3p were downregulated. (PMID: 37943469) RT-qPCR confirmed the differential expression of mmu-miR-125a-5p, mmu-miR-122b-3p, mmu-miR-139-3p, mmu-miR-330-3p, mmu-miR-3057-5p and mmu-miR-342-3p consistent with the small RNA sequence. (PMID: 38588846) Most of differentially expressed miRs in LGMD patients were up-regulated (miR-122-5p, miR-122b-3p, miR-6511a-3p, miR-192-5p, miR-574-3p, mir-885-3p, miR-29a-3p, miR-4646-3p, miR-203a-3p and miR-203b-5p) whilst only three of sequenced miRs were significantly down-regulated (miR-19b-3p, miR-7706, m... (PMID: 36575500)

### Literature

1. Mao J et al. (2024). *Transcriptome network analysis of inflammation and fibrosis in keloids.* J Dermatol Sci. DOI: [10.1016/j.jdermsci.2023.12.007](https://doi.org/10.1016/j.jdermsci.2023.12.007) PMID: [38242738](https://pubmed.ncbi.nlm.nih.gov/38242738/)

2. Joshua J et al. (2025). *Integrated MicroRNA-mRNA Sequencing Analysis Identifies Regulators and Networks Involved in Feline Hypertrophic Cardiomyopathy.* Int J Mol Sci. DOI: [10.3390/ijms26146764](https://doi.org/10.3390/ijms26146764) PMID: [40725010](https://pubmed.ncbi.nlm.nih.gov/40725010/)

3. Gao L et al. (2024). *Screening and identification of differential-expressed RNAs in thrombin-induced in vitro model of intracerebral hemorrhage.* Mol Cell Biochem. DOI: [10.1007/s11010-023-04879-w](https://doi.org/10.1007/s11010-023-04879-w) PMID: [37943469](https://pubmed.ncbi.nlm.nih.gov/37943469/)

4. Jiang W et al. (2024). *M1-type microglia-derived exosomes contribute to blood-brain barrier damage.* Brain Res. DOI: [10.1016/j.brainres.2024.148919](https://doi.org/10.1016/j.brainres.2024.148919) PMID: [38588846](https://pubmed.ncbi.nlm.nih.gov/38588846/)

5. García-Giménez JL et al. (2022). *Identification of circulating miRNAs differentially expressed in patients with Limb-girdle, Duchenne or facioscapulohumeral muscular dystrophies.* Orphanet J Rare Dis. DOI: [10.1186/s13023-022-02603-3](https://doi.org/10.1186/s13023-022-02603-3) PMID: [36575500](https://pubmed.ncbi.nlm.nih.gov/36575500/)

---

## miR-12195-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Upregulated | +7.24 | 9.33e-14 | 456.2 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UGGGUAUAACAGUCUUGGCUGG`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-1948-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Upregulated | +6.80 | 1.22e-14 | 447.8 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UUUAGGCAGAGCACUCGUACAG`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-292b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Upregulated | +8.00 | 6.59e-10 | 353.5 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AAGAGCCCCCAGUUUGAGUAU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-292b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Upregulated | +7.38 | 8.95e-10 | 310.8 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `ACUCAAAACCUGGCGGCACUUUU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-1948-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Upregulated | +6.29 | 2.72e-10 | 299.8 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AUAUGAGUAUUCUGCCUAAAU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

In vivo studies using inhibitory locked nucleic acid sequences revealed that miR-1948-5p preferentially represses female-biased messenger RNAs (mRNAs) and induces male-biased mRNAs in male liver; conversely, miR-802-5p preferentially represses male-biased mRNAs and increases levels of female-bias... (PMID: 29346554) Thus, miR-1948-5p and miR-802-5p are functional components of the GH regulatory network that shapes sex-differential gene expression in mouse liver. (PMID: 29346554)

### Literature

1. Hao P et al. (2018). *Functional Roles of Sex-Biased, Growth Hormone-Regulated MicroRNAs miR-1948 and miR-802 in Young Adult Mouse Liver.* Endocrinology. DOI: [10.1210/en.2017-03109](https://doi.org/10.1210/en.2017-03109) PMID: [29346554](https://pubmed.ncbi.nlm.nih.gov/29346554/)

---

## miR-101b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Upregulated | +4.04 | 6.35e-16 | 258.3 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-101-3p** - **4.8% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-101b-3p) | `GUACAGUACUGUGAUAGCU` | 19 nt |
| Human (hsa-miR-101-3p) | `UACAGUACUGUGAUAACUGAA` | 21 nt |

```
Mouse: GUACAGUACUGUGAUAGCU
       XXXXXXXXXXXXXXX|XXX--
Human: UACAGUACUGUGAUAACUGAA
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: G (mouse) -> U (human) *(in seed region)*
- Position 2: U (mouse) -> A (human) *(in seed region)*
- Position 3: A (mouse) -> C (human) *(in seed region)*
- Position 4: C (mouse) -> A (human) *(in seed region)*
- Position 5: A (mouse) -> G (human) *(in seed region)*
- Position 6: G (mouse) -> U (human) *(in seed region)*
- Position 7: U (mouse) -> A (human) *(in seed region)*
- Position 8: A (mouse) -> C (human) *(in seed region)*
- Position 9: C (mouse) -> U (human)
- Position 10: U (mouse) -> G (human)
- Position 11: G (mouse) -> U (human)
- Position 12: U (mouse) -> G (human)
- Position 13: G (mouse) -> A (human)
- Position 14: A (mouse) -> U (human)
- Position 15: U (mouse) -> A (human)
- Position 17: G (mouse) -> C (human)
- Position 18: C (mouse) -> U (human)
- Position 19: U (mouse) -> G (human)

Length difference: 2 nt

*WARNING: 8 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-101b-3p shares seed family 'UACAGUA' with miR-101a-3p.2. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 934**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Ube2d1 | 2 | -0.82 |
| Zfp804a | 3 | -0.771 |
| Epc1 | 1 | -0.767 |
| Atp1b1 | 2 | -0.737 |
| Zfp800 | 2 | -0.692 |
| Trappc8 | 1 | -0.626 |
| Arg2 | 1 | -0.622 |
| Nup37 | 1 | -0.6 |
| Mycn | 2 | -0.585 |
| Med4 | 1 | -0.568 |

**Top target gene: Ube2d1** (ubiquitin-conjugating enzyme E2D 1)

*Function:* Enables ubiquitin conjugating enzyme activity. Acts upstream of or within positive regulation of protein polyubiquitination and protein polyubiquitination. Predicted to be located in cytoplasm. Predicted to be part of ubiquitin ligase complex. Predicted to be active in nucleus. Is expressed in nervous system and urethra. Orthologous to human UBE2D1 (ubiquitin conjugating enzyme E2 D1). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [216080](https://www.ncbi.nlm.nih.gov/gene/216080)

### Biological Function Summary

miR-101b-3p is highly expressed after A. (PMID: 36747241) cantonensis infection; however, the role of miR-101b-3p and the transcription regulation of miR-101b-3p in A. (PMID: 36747241) RESULTS: In the present study, we found that miR-101b-3p inhibition alleviated inflammation infiltration and pyroptosis in A. (PMID: 36747241) In addition, we found that CCAAT/enhancer-binding protein alpha (CEBPα) directly bound to the - 6-k to - 3.5-k region upstream of miR-101b, and CEBPα activated miR-101b-3p expression in microglia. (PMID: 36747241) These data suggest the existence of a novel CEBPα/miR-101b-3p/pyroptosis pathway in A. (PMID: 36747241)

### Literature

1. Zeng X et al. (2023). *CEBPα/miR-101b-3p promotes meningoencephalitis in mice infected with Angiostrongylus cantonensis by promoting microglial pyroptosis.* Cell Commun Signal. DOI: [10.1186/s12964-023-01038-y](https://doi.org/10.1186/s12964-023-01038-y) PMID: [36747241](https://pubmed.ncbi.nlm.nih.gov/36747241/)

2. Zhang L et al. (2025). *TNF-α-preconditioning enhances analgesic efficacy of mesenchymal stem cell-derived extracellular vesicle in neuropathic pain via miR-101b-3p targeting Nav1.6.* Bioact Mater. DOI: [10.1016/j.bioactmat.2025.07.029](https://doi.org/10.1016/j.bioactmat.2025.07.029) PMID: [40755851](https://pubmed.ncbi.nlm.nih.gov/40755851/)

3. Yuan D et al. (2019). *Regulatory effect of host miR-101b-3p on parasitism of nematode Angiostrongylus cantonensis via superoxide dismutase 3.* Biochim Biophys Acta Gene Regul Mech. DOI: [10.1016/j.bbagrm.2019.02.004](https://doi.org/10.1016/j.bbagrm.2019.02.004) PMID: [30763737](https://pubmed.ncbi.nlm.nih.gov/30763737/)

4. Lou H et al. (2026). *Role and Mechanism of miR-101b-3p via Targeting TXNIP in Sevoflurane-Induced Cognitive Impairment in Mice.* Synapse. DOI: [10.1002/syn.70038](https://doi.org/10.1002/syn.70038) PMID: [41410154](https://pubmed.ncbi.nlm.nih.gov/41410154/)

5. Fu B et al. (2022). *MicroRNA-dependent regulation of targeted mRNAs for improved muscle texture in crisp grass carp fed with broad bean.* Food Res Int. DOI: [10.1016/j.foodres.2022.111071](https://doi.org/10.1016/j.foodres.2022.111071) PMID: [35400449](https://pubmed.ncbi.nlm.nih.gov/35400449/)

---

## miR-181b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -2.10 | 1.12e-12 | 6.8 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-181b-5p** - **95.8% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-181b-5p) | `AACAUUCAUUGCUGUCGGUGGGUU` | 24 nt |
| Human (hsa-miR-181b-5p) | `AACAUUCAUUGCUGUCGGUGGGU` | 23 nt |

```
Mouse: AACAUUCAUUGCUGUCGGUGGGUU
       |||||||||||||||||||||||-
Human: AACAUUCAUUGCUGUCGGUGGGU
```
(`|` = match, `X` = mismatch, `-` = length difference)

Length difference: 1 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 58**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| 2410141K09Rik | 3 | -5.028 |
| Rnf34 | 2 | -0.623 |
| 1700066M21Rik | 1 | -0.595 |
| Zfp867 | 1 | -0.454 |
| Gata6 | 1 | -0.391 |
| Gm4791 | 1 | -0.365 |
| Gm6871 | 1 | -0.363 |
| Pgap1 | 1 | -0.344 |
| Sowaha | 1 | -0.319 |
| Lhx9 | 1 | -0.308 |

**Top target gene: Zfp998** (zinc finger protein 998)

*Function:* Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Orthologous to several human genes including ZNF117 (zinc finger protein 117); ZNF490 (zinc finger protein 490); and ZNF595 (zinc finger protein 595). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [76803](https://www.ncbi.nlm.nih.gov/gene/76803)

### Biological Function Summary

Analysis of M2EV microRNA content revealed abundant miR-181b-5p, which regulated macrophage glucose uptake, glycolysis, and mitigated mitochondrial reactive oxygen species generation. (PMID: 36950739) Functional blockade of miR-181b-5p is detrimental to beneficial M2EV actions and resulted in failure to inhibit CCR2+ macrophage numbers and infarct size. (PMID: 36950739) Taken together, this investigation showed that M2EV rescued myocardial function, improved myocardial repair, and regulated CCR2+ macrophages via miR-181b-5p-dependent mechanisms, indicating an option for cell-free therapy for AMI. (PMID: 36950739) On the other hand, hsa-miR-181b-5p was among the top upregulated miRNAs in response to TGFB1, which is also predicted to regulate CDKN1B, TNFRSF11B, SIM1, and ARSJ in the BT-549 model. (PMID: 34326372) The expression of miR-181b-5p in HB tissues and cells was detected using quantitative real-time PCR. (PMID: 37955014)

### Literature

1. Li L et al. (2023). *M2 Macrophage-Derived sEV Regulate Pro-Inflammatory CCR2(+) Macrophage Subpopulations to Favor Post-AMI Cardiac Repair.* Adv Sci (Weinh). DOI: [10.1002/advs.202202964](https://doi.org/10.1002/advs.202202964) PMID: [36950739](https://pubmed.ncbi.nlm.nih.gov/36950739/)

2. Vishnubalaji R et al. (2021). *Epigenetic regulation of triple negative breast cancer (TNBC) by TGF-β signaling.* Sci Rep. DOI: [10.1038/s41598-021-94514-9](https://doi.org/10.1038/s41598-021-94514-9) PMID: [34326372](https://pubmed.ncbi.nlm.nih.gov/34326372/)

3. Lv Y et al. (2023). *miR-181b-5p/SOCS2/JAK2/STAT5 axis facilitates the metastasis of hepatoblastoma.* Precis Clin Med. DOI: [10.1093/pcmedi/pbad027](https://doi.org/10.1093/pcmedi/pbad027) PMID: [37955014](https://pubmed.ncbi.nlm.nih.gov/37955014/)

4. Zhang M et al. (2025). *LncRNA SNHG7/miR-181b-5p/TLR4 Activates Inflammation And Promotes Pyroptosis Through NF-κB Signaling in Diabetic Nephropathy.* Inflammation. DOI: [10.1007/s10753-025-02295-4](https://doi.org/10.1007/s10753-025-02295-4) PMID: [40372612](https://pubmed.ncbi.nlm.nih.gov/40372612/)

5. Chang L et al. (2019). *miR-181b-5p suppresses starvation-induced cardiomyocyte autophagy by targeting Hspa5.* Int J Mol Med. DOI: [10.3892/ijmm.2018.3988](https://doi.org/10.3892/ijmm.2018.3988) PMID: [30431062](https://pubmed.ncbi.nlm.nih.gov/30431062/)

---

## miR-181a-1-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -2.52 | 2.63e-06 | 3.5 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `ACCAUCGACCGUUGAUUGUACC`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

Moreover, miR-27b-3p, miR-181a-1-3p, and miR-326-5p target MIP-1β, TNF-α, and NOS2 mRNA, respectively. (PMID: 28748390) In conclusion, these data suggest that 15d-PGJ2/PPARγ axis regulates BMM activation via promoting miR-27b-3p, miR-181a-1-3p, and miR-326-5p expressions. (PMID: 28748390) 15d-PGJ2/PPARγ axis promotes expression of miR-27b-3p, miR-181a-1-3p, and miR-326-5p. (PMID: 28748390) miR-27b-3p, miR-181a-1-3p, and miR-326-5p have an inhibitory effect on BMM activation via 15d-PGJ2/PPARγ axis. (PMID: 28748390) Real-time PCR analysis revealed that five types of miRNA (miR-140-3p, miR-140-5p, miR-181a-1-3p, miR-210-3p, and miR-222-3p) were differentially expressed with changing patterns of expression during fracture healing in diabetic rats compared with controls. (PMID: 29437637)

### Literature

1. Li W et al. (2017). *miR-27b-3p, miR-181a-1-3p, and miR-326-5p are involved in the inhibition of macrophage activation in chronic liver injury.* J Mol Med (Berl). DOI: [10.1007/s00109-017-1570-0](https://doi.org/10.1007/s00109-017-1570-0) PMID: [28748390](https://pubmed.ncbi.nlm.nih.gov/28748390/)

2. Takahara S et al. (2018). *Altered expression of microRNA during fracture healing in diabetic rats.* Bone Joint Res. DOI: [10.1302/2046-3758.72.BJR-2017-0082.R1](https://doi.org/10.1302/2046-3758.72.BJR-2017-0082.R1) PMID: [29437637](https://pubmed.ncbi.nlm.nih.gov/29437637/)

3. Wang D et al. (2021). *Sevoflurane pretreatment regulates abnormal expression of MicroRNAs associated with spinal cord ischemia/reperfusion injury in rats.* Ann Transl Med. DOI: [10.21037/atm-20-7864](https://doi.org/10.21037/atm-20-7864) PMID: [34268365](https://pubmed.ncbi.nlm.nih.gov/34268365/)

4. Liu J et al. (2020). *Identification of Differentially Expressed miRNAs in the Response of Spleen CD4(+) T Cells to Electroacupuncture in Senescence-Accelerated Mice.* Cell Biochem Biophys. DOI: [10.1007/s12013-020-00900-x](https://doi.org/10.1007/s12013-020-00900-x) PMID: [32026263](https://pubmed.ncbi.nlm.nih.gov/32026263/)

---

## miR-181a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -2.42 | 2.63e-06 | 3.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-181a-5p** - **100% identical** (23 nt)

Sequence: `AACAUUCAACGCUGUCGGUGAGU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 679**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Zfp97 | 3 | -10.423 |
| Zfp960 | 2 | -10.366 |
| Gm14420 | 3 | -7.855 |
| Gm6710 | 1 | -7.048 |
| Gm14431 | 4 | -5.532 |
| Gm14295 | 1 | -5.5 |
| Zfp850 | 1 | -4.499 |
| Gm3055 | 8 | -3.95 |
| Zfp781 | 4 | -3.843 |
| Gm14391 | 1 | -3.451 |

**Top target gene: Zfp97** (zinc finger protein 97)

*Function:* Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleus. Is expressed in central nervous system and genitourinary system. [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [22759](https://www.ncbi.nlm.nih.gov/gene/22759)

### Biological Function Summary

Furthermore, LXRα activates the transcription of both miR-181a-5p and its binding protein FUS to increase the recruitment of miR-181a-5p in tumor-derived extracellular vesicles (EVs). (PMID: 38031260) Intake of miR-181a-5p in macrophages promotes their M2 polarization and enhances the taurine export by inhibiting expression of its target gene lats1, which in turn inactivates the hippo pathway and results in a Yes-associated protein (YAP) nuclear translocation for transcriptional activation of ... (PMID: 38031260) Taken together, the findings indicate a reciprocal interaction between PCa cells and TAMs as a positive feedback-loop to repress ferroptosis in PCa, mediated by TAM-secreted taurine and tumor EV-delivered miR-181a-5p. (PMID: 38031260) The present study demonstrated that highly metastatic CRC cells released more miR-181a-5p-rich EVs than cells which exhibit a low metastatic potential, in-turn promoting CRLM. (PMID: 35041299) Additionally, we verified that FUS mediated packaging of miR-181a-5p into CRC EVs, which in-turn persistently activated hepatic stellate cells (HSCs) by targeting SOCS3 and activating the IL6/STAT3 signalling pathway. (PMID: 35041299)

### Literature

1. Xiao H et al. (2024). *Taurine Inhibits Ferroptosis Mediated by the Crosstalk between Tumor Cells and Tumor-Associated Macrophages in Prostate Cancer.* Adv Sci (Weinh). DOI: [10.1002/advs.202303894](https://doi.org/10.1002/advs.202303894) PMID: [38031260](https://pubmed.ncbi.nlm.nih.gov/38031260/)

2. Zhao S et al. (2022). *Highly-metastatic colorectal cancer cell released miR-181a-5p-rich extracellular vesicles promote liver metastasis by activating hepatic stellate cells and remodelling the tumour microenvironment.* J Extracell Vesicles. DOI: [10.1002/jev2.12186](https://doi.org/10.1002/jev2.12186) PMID: [35041299](https://pubmed.ncbi.nlm.nih.gov/35041299/)

3. Li J et al. (2023). *Role of miR‑181a‑5p in cancer (Review).* Int J Oncol. DOI: [10.3892/ijo.2023.5556](https://doi.org/10.3892/ijo.2023.5556) PMID: [37539738](https://pubmed.ncbi.nlm.nih.gov/37539738/)

4. Long Z et al. (2023). *MiR-181a-5p promotes osteogenesis by targeting BMP3.* Aging (Albany NY). DOI: [10.18632/aging.204505](https://doi.org/10.18632/aging.204505) PMID: [36734882](https://pubmed.ncbi.nlm.nih.gov/36734882/)

5. Agostini S et al. (2023). *miR-23a-3p and miR-181a-5p modulate SNAP-25 expression.* PLoS One. DOI: [10.1371/journal.pone.0279961](https://doi.org/10.1371/journal.pone.0279961) PMID: [36649268](https://pubmed.ncbi.nlm.nih.gov/36649268/)

---

## miR-145a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -1.82 | 5.69e-05 | 3.0 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-145-5p** - **100% identical** (23 nt)

Sequence: `GUCCAGUUUUCCCAGGAAUCCCU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 635**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Fscn1 | 4 | -1.151 |
| Abhd17c | 2 | -1.054 |
| Fli1 | 4 | -0.813 |
| Add3 | 2 | -0.76 |
| Hnrnph2 | 1 | -0.724 |
| Abracl | 1 | -0.708 |
| Mpzl2 | 3 | -0.692 |
| Ythdf2 | 2 | -0.686 |
| Glis1 | 1 | -0.67 |
| Smcp | 1 | -0.639 |

**Top target gene: Fscn1** (fascin actin-bundling protein 1)

*Function:* Enables actin filament binding activity. Involved in cell migration and positive regulation of filopodium assembly. Acts upstream of or within actin filament bundle assembly. Located in filopodium; growth cone; and lamellipodium. Is expressed in several structures, including alimentary system; central nervous system; embryo mesenchyme; genitourinary system; and sensory organ. Orthologous to human FSCN1 (fascin actin-bundling protein 1). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [14086](https://www.ncbi.nlm.nih.gov/gene/14086)

### Biological Function Summary

Mechanistically, the reduced miR-145a-5p expression hindered the osteogenic differentiation and immunomodulatory capacity of OVX MSCs by affecting the TGF-β/Smad 2/3-Wnt/β-catenin signaling axis, resulting in the development of osteoporosis. (PMID: 39304875) WT apoVs directly transferred miR-145a-5p to OVX MSCs, which were then reused to restore their impaired biological functions. (PMID: 39304875) The differential expression of miR-145a-5p is responsible for the distinct efficacy between the two types of apoVs. (PMID: 39304875) In vivo loss-of-function and gain-of-function studies were performed to explore the role of miR-145a-5p and Nr4a2 in NASH progression. (PMID: 37463623) RNA-sequencing and bioinformatic analysis were used to investigate the targets of miR-145a-5p. (PMID: 37463623)

### Literature

1. Zhang R et al. (2024). *Apoptotic vesicles rescue impaired mesenchymal stem cells and their therapeutic capacity for osteoporosis by restoring miR-145a-5p deficiency.* J Nanobiotechnology. DOI: [10.1186/s12951-024-02829-2](https://doi.org/10.1186/s12951-024-02829-2) PMID: [39304875](https://pubmed.ncbi.nlm.nih.gov/39304875/)

2. Li B et al. (2023). *Downregulation of microRNA-145a-5p promotes steatosis-to-NASH progression through upregulation of Nr4a2.* J Hepatol. DOI: [10.1016/j.jhep.2023.06.019](https://doi.org/10.1016/j.jhep.2023.06.019) PMID: [37463623](https://pubmed.ncbi.nlm.nih.gov/37463623/)

3. Li P et al. (2024). *Transplantation of miR-145a-5p modified M2 type microglia promotes the tissue repair of spinal cord injury in mice.* J Transl Med. DOI: [10.1186/s12967-024-05492-1](https://doi.org/10.1186/s12967-024-05492-1) PMID: [39103885](https://pubmed.ncbi.nlm.nih.gov/39103885/)

4. Du J et al. (2016). *miR-145a-5p Promotes Myoblast Differentiation.* Biomed Res Int. DOI: [10.1155/2016/5276271](https://doi.org/10.1155/2016/5276271) PMID: [27239472](https://pubmed.ncbi.nlm.nih.gov/27239472/)

5. Du J et al. (2016). *Methylation of miR-145a-5p promoter mediates adipocytes differentiation.* Biochem Biophys Res Commun. DOI: [10.1016/j.bbrc.2016.05.057](https://doi.org/10.1016/j.bbrc.2016.05.057) PMID: [27179777](https://pubmed.ncbi.nlm.nih.gov/27179777/)

---

## miR-181c-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -1.95 | 3.50e-07 | 2.9 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-181c-5p** - **100% identical** (22 nt)

Sequence: `AACAUUCAACCUGUCGGUGAGU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 152**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Gm14440 | 7 | -4.111 |
| Zfp442 | 1 | -2.603 |
| Zfp937 | 1 | -1.631 |
| Zfp14 | 1 | -0.683 |
| Gskip | 2 | -0.667 |
| 4921524J17Rik | 1 | -0.514 |
| Atp1b1 | 2 | -0.512 |
| Zfand5 | 2 | -0.466 |
| Gm5113 | 1 | -0.428 |
| Mturn | 2 | -0.417 |

**Top target gene: Zfp1009** (zinc finger protein 1009)

*NCBI Gene ID:* [100503353](https://www.ncbi.nlm.nih.gov/gene/100503353)

### Biological Function Summary

Meanwhile, circFNDC3B sequestered miR-181c-5p to upregulate SERPINE1 and PROX1, which drove epithelial-mesenchymal transition (EMT) or partial-EMT (p-EMT) in OSCC cells and promoted lymphangiogenesis to accelerate LN metastasis. (PMID: 36811957) MiR-181c-5p/HMGB1 axis plays a part in anti-inflammation effects. (PMID: 37466537) So we investigated the role of miR-181c-5p in learning and memory impairment induced by SD. (PMID: 37466537) We overexpressed miR-181c-5p in the mice hippocampus by injecting lentivirus vector-miR-181c-5p (LV-miR-181c-5p) particles. (PMID: 37466537) Moreover, the expression levels of HMGB1, TLR4 and p-NF-κB in the hippocampus of overexpressed miR-181c-5p mice were reduced. (PMID: 37466537)

### Literature

1. Li X et al. (2023). *circFNDC3B Accelerates Vasculature Formation and Metastasis in Oral Squamous Cell Carcinoma.* Cancer Res. DOI: [10.1158/0008-5472.CAN-22-2585](https://doi.org/10.1158/0008-5472.CAN-22-2585) PMID: [36811957](https://pubmed.ncbi.nlm.nih.gov/36811957/)

2. Hu Y et al. (2023). *MiR-181c-5p ameliorates learning and memory in sleep-deprived mice via HMGB1/TLR4/NF-κB pathway.* An Acad Bras Cienc. DOI: [10.1590/0001-3765202320220750](https://doi.org/10.1590/0001-3765202320220750) PMID: [37466537](https://pubmed.ncbi.nlm.nih.gov/37466537/)

3. Tak H et al. (2024). *A meta-analysis of differentially expressed circulatory micro-RNAs in chronic traumatic encephalopathy and other tauopathies: A significant role of miR-181c-5p.* Ir J Med Sci. DOI: [10.1007/s11845-023-03469-5](https://doi.org/10.1007/s11845-023-03469-5) PMID: [37540332](https://pubmed.ncbi.nlm.nih.gov/37540332/)

4. Wang J et al. (2024). *MiR-181c-5p Regulates Lung Adenocarcinoma Progression via Targeting PRKN.* Biochem Genet. DOI: [10.1007/s10528-023-10459-w](https://doi.org/10.1007/s10528-023-10459-w) PMID: [37532837](https://pubmed.ncbi.nlm.nih.gov/37532837/)

5. Abd ElAziz ON et al. (2022). *In Silico and In Vivo Evaluation of microRNA-181c-5p's Role in Hepatocellular Carcinoma.* Genes (Basel). DOI: [10.3390/genes13122343](https://doi.org/10.3390/genes13122343) PMID: [36553610](https://pubmed.ncbi.nlm.nih.gov/36553610/)

---

## miR-143-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -1.58 | 1.25e-04 | 2.8 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-143-3p** - **100% identical** (21 nt)

Sequence: `UGAGAUGAAGCACUGUAGCUC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 432**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Lmo4 | 1 | -0.652 |
| Cryz | 1 | -0.647 |
| Ppp3r2 | 1 | -0.623 |
| Gigyf2 | 1 | -0.618 |
| Itm2b | 1 | -0.602 |
| Kras | 2 | -0.588 |
| Creld1 | 1 | -0.569 |
| Ccdc58 | 1 | -0.557 |
| Fgf7 | 1 | -0.553 |
| Ttpa | 1 | -0.543 |

**Top target gene: Lmo4** (LIM domain only 4)

*Function:* Enables DNA-binding transcription factor binding activity and transcription corepressor activity. Involved in several processes, including negative regulation of transcription by RNA polymerase II; nervous system development; and positive regulation of kinase activity. Acts upstream of or within several processes, including cell differentiation in spinal cord; thymus development; and ventricular septum development. Located in cell leading edge and nucleus. Part of RNA polymerase II transcription...

*NCBI Gene ID:* [16911](https://www.ncbi.nlm.nih.gov/gene/16911)

### Biological Function Summary

METHODS AND RESULTS: In FF exosomal RNA-seq analysis, a decrease in glycolysis-related pathways was identified as an important feature of the PCOS group, and the differentially expressed miR-143-3p and miR-155-5p may be regulatory factors of glycolysis. (PMID: 35534864) By determining the effects of miR-143-3p and miR-155-5p on hexokinase (HK) 2, pyruvate kinase muscle isozyme M2 (PKM2), lactate dehydrogenase A (LDHA), pyruvate, lactate and apoptosis in KGN cells, we found that upregulated miR-143-3p expression in exosomes from the PCOS group inhibited glycolysi... (PMID: 35534864) In this study, HK2 was found to be the mediator of miR-143-3p and miR-155-5p in FF-derived exosome-mediated regulation of glycolysis in KGN cells. (PMID: 35534864) CONCLUSIONS: In conclusion, these results indicate that miR-143-3p and miR-155-5p in FF-derived exosomes antagonistically regulate glycolytic-mediated follicular dysplasia of GCs in PCOS. (PMID: 35534864) Heightened levels of miR-143-3p in BMECs induce the up-regulated expression of cell adhesion molecules (CAMs) that bind to circulating neutrophils and facilitate their transendothelial cell migration (TEM) into brain. (PMID: 38044319)

### Literature

1. Cao J et al. (2022). *Follicular fluid-derived exosomal miR-143-3p/miR-155-5p regulate follicular dysplasia by modulating glycolysis in granulosa cells in polycystic ovary syndrome.* Cell Commun Signal. DOI: [10.1186/s12964-022-00876-6](https://doi.org/10.1186/s12964-022-00876-6) PMID: [35534864](https://pubmed.ncbi.nlm.nih.gov/35534864/)

2. Wu X et al. (2024). *Astrocyte-Derived Extracellular Vesicular miR-143-3p Dampens Autophagic Degradation of Endothelial Adhesion Molecules and Promotes Neutrophil Transendothelial Migration after Acute Brain Injury.* Adv Sci (Weinh). DOI: [10.1002/advs.202305339](https://doi.org/10.1002/advs.202305339) PMID: [38044319](https://pubmed.ncbi.nlm.nih.gov/38044319/)

3. Zhai M et al. (2025). *A smooth muscle cell lncRNA controls angiogenesis in chronic limb-threatening ischemia through miR-143-3p/HHIP signaling.* J Clin Invest. DOI: [10.1172/JCI188559](https://doi.org/10.1172/JCI188559) PMID: [40875440](https://pubmed.ncbi.nlm.nih.gov/40875440/)

4. Liu Q et al. (2025). *Role of miR-143-3p in the Development of Hemorrhoids and Postoperative Wound Healing.* J Invest Surg. DOI: [10.1080/08941939.2025.2480799](https://doi.org/10.1080/08941939.2025.2480799) PMID: [40114371](https://pubmed.ncbi.nlm.nih.gov/40114371/)

5. Yuan W et al. (2025). *Strontium-Alix interaction enhances exosomal miRNA selectively loading in synovial MSCs for temporomandibular joint osteoarthritis treatment.* Int J Oral Sci. DOI: [10.1038/s41368-024-00329-5](https://doi.org/10.1038/s41368-024-00329-5) PMID: [39890774](https://pubmed.ncbi.nlm.nih.gov/39890774/)

---

## miR-143-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -1.74 | 2.00e-04 | 2.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-143-5p** - **95.5% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-143-5p) | `GGUGCAGUGCUGCAUCUCUGG` | 21 nt |
| Human (hsa-miR-143-5p) | `GGUGCAGUGCUGCAUCUCUGGU` | 22 nt |

```
Mouse: GGUGCAGUGCUGCAUCUCUGG
       |||||||||||||||||||||-
Human: GGUGCAGUGCUGCAUCUCUGGU
```
(`|` = match, `X` = mismatch, `-` = length difference)

Length difference: 1 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-143-5p shares seed family 'GAGAUGA' with miR-143-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 432**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Lmo4 | 1 | -0.652 |
| Cryz | 1 | -0.647 |
| Ppp3r2 | 1 | -0.623 |
| Gigyf2 | 1 | -0.618 |
| Itm2b | 1 | -0.602 |
| Kras | 2 | -0.588 |
| Creld1 | 1 | -0.569 |
| Ccdc58 | 1 | -0.557 |
| Fgf7 | 1 | -0.553 |
| Ttpa | 1 | -0.543 |

**Top target gene: Lmo4** (LIM domain only 4)

*Function:* Enables DNA-binding transcription factor binding activity and transcription corepressor activity. Involved in several processes, including negative regulation of transcription by RNA polymerase II; nervous system development; and positive regulation of kinase activity. Acts upstream of or within several processes, including cell differentiation in spinal cord; thymus development; and ventricular septum development. Located in cell leading edge and nucleus. Part of RNA polymerase II transcription...

*NCBI Gene ID:* [16911](https://www.ncbi.nlm.nih.gov/gene/16911)

### Biological Function Summary

By qRT-PCR, we validated that the expression of rno-miR-143-5p was corresponding to our prediction. (PMID: 39806038) Sinomenine inhibited vascular smooth muscle cells (VSMCs) calcification, accompanied with miR-143-5p upregulation. (PMID: 39806038) On the contrary, miR-143-5p inhibitor increased VSMCs calcification in high phosphate condition, which was inhibited by sinomenine. (PMID: 39806038) In chronic kidney disease patients with vascular calcification, the expression level of circulating miR-143-5p was lower than those without vascular calcification. (PMID: 39806038) Circulating miR-143-5p was supposed to be a potential biomarker for vascular calcification in chronic kidney disease patients. (PMID: 39806038)

### Literature

1. Yu F et al. (2025). *Sinomenine attenuates uremia vascular calcification by miR-143-5p.* Sci Rep. DOI: [10.1038/s41598-025-86055-2](https://doi.org/10.1038/s41598-025-86055-2) PMID: [39806038](https://pubmed.ncbi.nlm.nih.gov/39806038/)

2. Wu J et al. (2024). *Biological functions and potential mechanisms of miR‑143‑3p in cancers (Review).* Oncol Rep. DOI: [10.3892/or.2024.8772](https://doi.org/10.3892/or.2024.8772) PMID: [38994765](https://pubmed.ncbi.nlm.nih.gov/38994765/)

3. Hayek H et al. (2024). *The Regulation of Fatty Acid Synthase by Exosomal miR-143-5p and miR-342-5p in Idiopathic Pulmonary Fibrosis.* Am J Respir Cell Mol Biol. DOI: [10.1165/rcmb.2023-0232OC](https://doi.org/10.1165/rcmb.2023-0232OC) PMID: [38117249](https://pubmed.ncbi.nlm.nih.gov/38117249/)

4. Huo X et al. (2025). *MSC-derived exosomes improve endometrial fibrosis via the lncRNA IGF2R/ miR-143-5p/AQP8 axis.* Stem Cell Res Ther. DOI: [10.1186/s13287-025-04611-z](https://doi.org/10.1186/s13287-025-04611-z) PMID: [40866943](https://pubmed.ncbi.nlm.nih.gov/40866943/)

5. Xu J et al. (2022). *miR-143-5p suppresses breast cancer progression by targeting the HIF-1α-related GLUT1 pathway.* Oncol Lett. DOI: [10.3892/ol.2022.13268](https://doi.org/10.3892/ol.2022.13268) PMID: [35350590](https://pubmed.ncbi.nlm.nih.gov/35350590/)

---

## miR-181d-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -1.87 | 5.45e-08 | 2.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-181d-5p** - **100% identical** (23 nt)

Sequence: `AACAUUCAUUGUUGUCGGUGGGU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 230**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| 9830147E19Rik | 4 | -5.727 |
| Gm5595 | 3 | -2.799 |
| Zfp951 | 3 | -2.622 |
| C030039L03Rik | 1 | -2.41 |
| Gm2381 | 6 | -2.311 |
| B230307C23Rik | 4 | -1.724 |
| Zfp780b | 1 | -1.698 |
| Zfp120 | 4 | -1.594 |
| Gm17067 | 3 | -1.584 |
| Zfp619 | 1 | -1.344 |

**Top target gene: Zfp976** (zinc finger protein 976)

*Function:* Predicted to enable DNA binding activity; DNA-binding transcription repressor activity, RNA polymerase II-specific; and protein-macromolecule adaptor activity. Acts upstream of or within cellular response to heat. Predicted to be located in nucleoplasm. Predicted to be active in nucleus. Orthologous to several human genes including ZNF320 (zinc finger protein 320); ZNF415 (zinc finger protein 415); and ZNF528 (zinc finger protein 528). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [208111](https://www.ncbi.nlm.nih.gov/gene/208111)

### Biological Function Summary

The beneficial effect of limb ischemic conditioning was mediated by muscle-to-liver transfer of small extracellular vesicles (sEVs) and their cargo microRNAs, leading to elevation of miR-181d-5p in the liver. (PMID: 40118054) Hepatic miR-181d-5p overexpression faithfully mirrored the molecular and histological benefits of limb ischemic conditioning by suppressing nuclear receptor 4A3 (NR4A3). (PMID: 40118054) Here, we generated two animal models of hypercholesterolemia to analyze the potential relationship between miR-181d-5p and LDL-C. (PMID: 38940622) In hypercholesterolemia model mice, adeno-associated virus (AAV)-mediated liver-directed overexpression of miR-181d-5p decreased the serum levels of cholesterol and LDL-C and the levels of cholesterol and triglyceride in the liver compared with control mice. (PMID: 38940622) Target Scan 8.0 indicated Proprotein convertase subtilisin/kexin type 9 (PCSK9) to be a possible target gene of miR-181d-5p, which was confirmed by in vitro experiments. (PMID: 38940622)

### Literature

1. Zhao Y et al. (2025). *Remote limb ischemic conditioning alleviates steatohepatitis via extracellular vesicle-mediated muscle-liver crosstalk.* Cell Metab. DOI: [10.1016/j.cmet.2025.02.009](https://doi.org/10.1016/j.cmet.2025.02.009) PMID: [40118054](https://pubmed.ncbi.nlm.nih.gov/40118054/)

2. Wang Y et al. (2024). *miR-181d-5p ameliorates hypercholesterolemia by targeting PCSK9.* J Endocrinol. DOI: [10.1530/JOE-23-0402](https://doi.org/10.1530/JOE-23-0402) PMID: [38940622](https://pubmed.ncbi.nlm.nih.gov/38940622/)

3. Mulato MGF et al. (2023). *Serum miR-181d-5p levels in response to controlled ovarian stimulation: predictive value and biological function.* JBRA Assist Reprod. DOI: [10.5935/1518-0557.20220053](https://doi.org/10.5935/1518-0557.20220053) PMID: [36952624](https://pubmed.ncbi.nlm.nih.gov/36952624/)

4. Sang M et al. (2024). *The role and diagnostics of miR-181d-5p in polycystic ovary syndrome in insulin-resistant women.* Endokrynol Pol. DOI: [10.5603/ep.99021](https://doi.org/10.5603/ep.99021) PMID: [40091327](https://pubmed.ncbi.nlm.nih.gov/40091327/)

5. Wu ZH et al. (2023). *miR-181d-5p, which is upregulated in fetal growth restriction placentas, inhibits trophoblast fusion via CREBRF.* J Assist Reprod Genet. DOI: [10.1007/s10815-023-02917-6](https://doi.org/10.1007/s10815-023-02917-6) PMID: [37610607](https://pubmed.ncbi.nlm.nih.gov/37610607/)

---

## miR-322-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -1.69 | 2.70e-04 | 2.4 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CAGCAGCAAUUCAUGUUUUGGA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 240**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Rab9b | 2 | -0.936 |
| Wap | 1 | -0.813 |
| Pth | 1 | -0.774 |
| Rbm6 | 1 | -0.769 |
| Zfp622 | 1 | -0.727 |
| Ccdc19 | 1 | -0.696 |
| Kif23 | 1 | -0.689 |
| 1110058L19Rik | 1 | -0.685 |
| Ywhah | 1 | -0.631 |
| Med26 | 1 | -0.63 |

**Top target gene: Rab9b** (RAB9B, member RAS oncogene family)

*Function:* Enables identical protein binding activity. Predicted to be involved in retrograde transport, endosome to Golgi. Predicted to be located in phagocytic vesicle membrane and plasma membrane. Predicted to be active in late endosome; lysosome; and phagocytic vesicle. Orthologous to human RAB9B (RAB9B, member RAS oncogene family). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [319642](https://www.ncbi.nlm.nih.gov/gene/319642)

### Biological Function Summary

MiR-322-5p has been revealed to play an important role in multiple diseases. (PMID: 35184431) In this study, we aimed to investigate the role and regulatory mechanism of miR-322-5p in vascular dementia. (PMID: 35184431) RESULTS: MiR-322-5p expression was significantly downregulated in the neurons exposed to OGD/R and the hippocampi of 2VO rats. (PMID: 35184431) Overexpression of miR-322-5p ameliorated cell apoptosis and the inflammatory response in vitro. (PMID: 35184431) In a mechanistic study, miR-322-5p was confirmed to directly target and negatively regulate tetraspanin 5 (TSPAN5) in cultured NRNs. (PMID: 35184431)

### Literature

1. Zheng W et al. (2022). *MiR-322-5p Alleviates Cell Injury and Impairment of Cognitive Function in Vascular Dementia by Targeting TSPAN5.* Yonsei Med J. DOI: [10.3349/ymj.2022.63.3.282](https://doi.org/10.3349/ymj.2022.63.3.282) PMID: [35184431](https://pubmed.ncbi.nlm.nih.gov/35184431/)

2. Umar T et al. (2023). *6-Gingerol via overexpression of miR-322-5p impede lipopolysaccharide-caused inflammatory response in RAW264.7 cells.* Naunyn Schmiedebergs Arch Pharmacol. DOI: [10.1007/s00210-023-02543-0](https://doi.org/10.1007/s00210-023-02543-0) PMID: [37347266](https://pubmed.ncbi.nlm.nih.gov/37347266/)

3. Ruan Y et al. (2024). *MicroRNA-322-5p protects against myocardial infarction through targeting BTG2.* Am J Med Sci. DOI: [10.1016/j.amjms.2024.02.012](https://doi.org/10.1016/j.amjms.2024.02.012) PMID: [38437946](https://pubmed.ncbi.nlm.nih.gov/38437946/)

4. Connolly M et al. (2018). *miR-322-5p targets IGF-1 and is suppressed in the heart of rats with pulmonary hypertension.* FEBS Open Bio. DOI: [10.1002/2211-5463.12369](https://doi.org/10.1002/2211-5463.12369) PMID: [29511611](https://pubmed.ncbi.nlm.nih.gov/29511611/)

5. Guo L et al. (2024). *MicroRNA-322-5p targeting Smurf2 regulates the TGF-β/Smad pathway to protect cardiac function and inhibit myocardial infarction.* Hum Cell. DOI: [10.1007/s13577-024-01062-1](https://doi.org/10.1007/s13577-024-01062-1) PMID: [38656742](https://pubmed.ncbi.nlm.nih.gov/38656742/)

---

## miR-181c-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Liver | Downregulated | -2.18 | 2.92e-07 | 2.3 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-181c-3p** - **27.3% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-181c-3p) | `ACCAUCGACCGUUGAGUGGACC` | 22 nt |
| Human (hsa-miR-181c-3p) | `AACCAUCGACCGUUGAGUGGAC` | 22 nt |

```
Mouse: ACCAUCGACCGUUGAGUGGACC
       |X|XXXXXX|XX|XXXXX|XX|
Human: AACCAUCGACCGUUGAGUGGAC
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 2: C (mouse) -> A (human) *(in seed region)*
- Position 4: A (mouse) -> C (human) *(in seed region)*
- Position 5: U (mouse) -> A (human) *(in seed region)*
- Position 6: C (mouse) -> U (human) *(in seed region)*
- Position 7: G (mouse) -> C (human) *(in seed region)*
- Position 8: A (mouse) -> G (human) *(in seed region)*
- Position 9: C (mouse) -> A (human)
- Position 11: G (mouse) -> C (human)
- Position 12: U (mouse) -> G (human)
- Position 14: G (mouse) -> U (human)
- Position 15: A (mouse) -> G (human)
- Position 16: G (mouse) -> A (human)
- Position 17: U (mouse) -> G (human)
- Position 18: G (mouse) -> U (human)
- Position 20: A (mouse) -> G (human)
- Position 21: C (mouse) -> A (human)

*WARNING: 6 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-181c-3p shares seed family 'ACAUUCA' with miR-181a-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 1119**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Zfp97 | 3 | -10.423 |
| Zfp960 | 2 | -10.366 |
| Gm14420 | 3 | -7.855 |
| Gm6710 | 1 | -7.048 |
| 9830147E19Rik | 4 | -5.727 |
| Gm14431 | 4 | -5.532 |
| Gm14295 | 1 | -5.5 |
| 2410141K09Rik | 3 | -5.028 |
| Zfp850 | 1 | -4.499 |
| Gm14440 | 7 | -4.111 |

**Top target gene: Zfp97** (zinc finger protein 97)

*Function:* Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleus. Is expressed in central nervous system and genitourinary system. [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [22759](https://www.ncbi.nlm.nih.gov/gene/22759)

### Biological Function Summary

miR-9, miR-181a-2-3p, miR-181c, miR-181c-3p, miR-486-3p, and miR-582 showed increased expression, whereas miR-223 and miR-424-3p showed decreased expression. (PMID: 34270823) The results showed that H/R significantly increased the expression of miR-181c-5p but not miR-181c-3p in H9C2 cells. (PMID: 31178952) In the article, we found that the expression of miR-181c-3p and miR-181c-5p was significantly downregulated under glucose treatment in a dose-dependent manner and in peripheral blood from diabetic patients compared with healthy participants. (PMID: 29605252) We explored the role of miR-181c-3p and miR-181c-5p in high glucose (HG)-induced dysfunction in human umbilical vein endothelial cells (HUVECs) by regulating leukemia inhibitory factor (LIF), their potential target with binding sites in 3-UTR region, that is also closely related to glucose metabo... (PMID: 29605252) In addition, miR-181c-3p and miR-181c-5p significantly enhanced HG-induced oxidative stress injury by increasing malondialdehyde (MDA) and reactive oxygen species (ROS) production and promoted HG-induced HUVECs apoptosis, confirmed by TUNEL staining. (PMID: 29605252)

### Literature

1. Wang W et al. (2022). *miR-181c regulates MCL1 and cell survival in GATA2 deficient cells.* J Leukoc Biol. DOI: [10.1002/JLB.2A1220-824R](https://doi.org/10.1002/JLB.2A1220-824R) PMID: [34270823](https://pubmed.ncbi.nlm.nih.gov/34270823/)

2. Ahlberg E et al. (2023). *Immune-related microRNAs in breast milk and their relation to regulatory T cells in breastfed children.* Pediatr Allergy Immunol. DOI: [10.1111/pai.13952](https://doi.org/10.1111/pai.13952) PMID: [37102392](https://pubmed.ncbi.nlm.nih.gov/37102392/)

3. Ge L et al. (2019). *miR-181c-5p Exacerbates Hypoxia/Reoxygenation-Induced Cardiomyocyte Apoptosis via Targeting PTPN4.* Oxid Med Cell Longev. DOI: [10.1155/2019/1957920](https://doi.org/10.1155/2019/1957920) PMID: [31178952](https://pubmed.ncbi.nlm.nih.gov/31178952/)

4. Shen X et al. (2018). *miR-181c-3p and -5p promotes high-glucose-induced dysfunction in human umbilical vein endothelial cells by regulating leukemia inhibitory factor.* Int J Biol Macromol. DOI: [10.1016/j.ijbiomac.2018.03.173](https://doi.org/10.1016/j.ijbiomac.2018.03.173) PMID: [29605252](https://pubmed.ncbi.nlm.nih.gov/29605252/)

5. Rajarajan D et al. (2019). *Genome-wide analysis reveals miR-3184-5p and miR-181c-3p as a critical regulator for adipocytes-associated breast cancer.* J Cell Physiol. DOI: [10.1002/jcp.28428](https://doi.org/10.1002/jcp.28428) PMID: [30847933](https://pubmed.ncbi.nlm.nih.gov/30847933/)

---

## miR-1264-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Upregulated | +11.82 | 8.62e-32 | 1946.5 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CAAAUCUUAUUUGAGCACCUGU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

RESULTS: In the mouse hippocampus, intermittent hypoxia altered the expression of many miRNAs, with miR-448-3p and miR-1264-3p changing over the course of more than three time periods. (PMID: 39912396) CONCLUSION: This study demonstrates that intermittent hypoxia alters the expression of miR-448-3p and miR-1264-3p, as well as the localization of the splicing factor hnRNPA2B1 in the cell nucleus. (PMID: 39912396)

### Literature

1. Liu C et al. (2025). *miR-448-3p/miR-1264-3p Participates in Intermittent Hypoxic Response in Hippocampus by Regulating Fam76b/hnRNPA2B1.* CNS Neurosci Ther. DOI: [10.1111/cns.70239](https://doi.org/10.1111/cns.70239) PMID: [39912396](https://pubmed.ncbi.nlm.nih.gov/39912396/)

---

## miR-449c-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Upregulated | +6.80 | 1.14e-41 | 1270.8 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-449c-5p** - **16.0% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-449c-5p) | `AGGCAGUGCAUUGCUAGCUGG` | 21 nt |
| Human (hsa-miR-449c-5p) | `UAGGCAGUGUAUUGCUAGCGGCUGU` | 25 nt |

```
Mouse: AGGCAGUGCAUUGCUAGCUGG
       XX|XXXXXXXX|XXXXXXX||----
Human: UAGGCAGUGUAUUGCUAGCGGCUGU
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: A (mouse) -> U (human) *(in seed region)*
- Position 2: G (mouse) -> A (human) *(in seed region)*
- Position 4: C (mouse) -> G (human) *(in seed region)*
- Position 5: A (mouse) -> C (human) *(in seed region)*
- Position 6: G (mouse) -> A (human) *(in seed region)*
- Position 7: U (mouse) -> G (human) *(in seed region)*
- Position 8: G (mouse) -> U (human) *(in seed region)*
- Position 9: C (mouse) -> G (human)
- Position 10: A (mouse) -> U (human)
- Position 11: U (mouse) -> A (human)
- Position 13: G (mouse) -> U (human)
- Position 14: C (mouse) -> G (human)
- Position 15: U (mouse) -> C (human)
- Position 16: A (mouse) -> U (human)
- Position 17: G (mouse) -> A (human)
- Position 18: C (mouse) -> G (human)
- Position 19: U (mouse) -> C (human)

Length difference: 4 nt

*WARNING: 7 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 126**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Mpp2 | 1 | -0.886 |
| Vamp2 | 3 | -0.784 |
| Mta2 | 1 | -0.742 |
| Ddx17 | 1 | -0.734 |
| Fam210b | 1 | -0.723 |
| Ppp2r5a | 1 | -0.68 |
| Dll1 | 1 | -0.651 |
| Mras | 2 | -0.646 |
| Kcne1l | 1 | -0.631 |
| Nrip3 | 1 | -0.628 |

**Top target gene: Mpp2** (membrane protein, palmitoylated 2 (MAGUK p55 subfamily member 2))

*Function:* Enables transmembrane transporter binding activity. A structural constituent of postsynaptic density. Involved in excitatory postsynaptic potential and long-term synaptic potentiation. Located in dendrite membrane; dendritic shaft; and dendritic spine. Is active in Schaffer collateral - CA1 synapse; glutamatergic synapse; and postsynaptic density membrane. Is expressed in several structures, including central nervous system; genitourinary system; gut gland; respiratory system; and retina. Orthol...

*NCBI Gene ID:* [50997](https://www.ncbi.nlm.nih.gov/gene/50997)

### Biological Function Summary

Here, we aimed to explore the function of miR-449c-5p in CAVD pathogenesis. (PMID: 28821833) In this study, we demonstrated the role of miR-449c-5p in VICs osteogenesis. (PMID: 28821833) MiRNA microarray assay and qRT-PCR results revealed miR-449c-5p was significantly down-regulated in calcified aortic valves compared with non-calcified valves. (PMID: 28821833) MiR-449c-5p overexpression inhibited VICs osteogenic differentiation in vitro, whereas down-regulation of miR-449c-5p enhanced the process. (PMID: 28821833) Target prediction analysis and dual-luciferase reporter assay confirmed Smad4 was a direct target of miR-449c-5p. (PMID: 28821833)

### Literature

1. Xu R et al. (2017). *MicroRNA-449c-5p inhibits osteogenic differentiation of human VICs through Smad4-mediated pathway.* Sci Rep. DOI: [10.1038/s41598-017-09390-z](https://doi.org/10.1038/s41598-017-09390-z) PMID: [28821833](https://pubmed.ncbi.nlm.nih.gov/28821833/)

2. Fu Q et al. (2022). *MicroRNA-449c-5p alleviates lipopolysaccharide-induced HUVECs injury via inhibiting the activation NF-κb signaling pathway by TAK1.* Mol Immunol. DOI: [10.1016/j.molimm.2022.03.123](https://doi.org/10.1016/j.molimm.2022.03.123) PMID: [35421737](https://pubmed.ncbi.nlm.nih.gov/35421737/)

3. Zhang D et al. (2022). *LncRNA SNHG8 sponges miR-449c-5p and regulates the SIRT1/FoxO1 pathway to affect microglia activation and blood-brain barrier permeability in ischemic stroke.* J Leukoc Biol. DOI: [10.1002/JLB.1A0421-217RR](https://doi.org/10.1002/JLB.1A0421-217RR) PMID: [34585441](https://pubmed.ncbi.nlm.nih.gov/34585441/)

4. Li L et al. (2024). *miRNA-449c-5p regulates the JAK-STAT pathway in inhibiting cell proliferation and invasion in human breast cancer cells by targeting ERBB2.* Cancer Rep (Hoboken). DOI: [10.1002/cnr2.1974](https://doi.org/10.1002/cnr2.1974) PMID: [38351535](https://pubmed.ncbi.nlm.nih.gov/38351535/)

5. Cui Z et al. (2021). *Circadian miR-449c-5p regulates uterine Ca(2+) transport during eggshell calcification in chickens.* BMC Genomics. DOI: [10.1186/s12864-021-08074-3](https://doi.org/10.1186/s12864-021-08074-3) PMID: [34702171](https://pubmed.ncbi.nlm.nih.gov/34702171/)

---

## miR-1264-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Upregulated | +9.39 | 2.42e-22 | 1051.6 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AGGUCCUCAAUAAGUAUUUGUU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

The expression of lnc240, miR-1264-5p, and MEF2C was analyzed with RNA-seq and further determined by qRT-PCR in HE mouse. (PMID: 36645630) The overexpression of lnc240 could significantly downregulate miR-1264-5p and upregulate MEF2C, also increasing the amplitude and frequency of mEPSC in primary cultured hippocampal neurons. (PMID: 36645630) The overexpression of miR-1264-5p reversed the effect of lnc240 on MEF2C. (PMID: 36645630) Lnc240 can regulate the expression of MEF2C through miR-1264-5p and regulate the synaptic plasticity of hippocampal neurons, thereby saving the learning and memory dysfunction in HE mice, suggesting that lnc240 might be a potential therapeutic target for the treatment of HE. (PMID: 36645630)

### Literature

1. Zhang H et al. (2023). *Overexpressing lnc240 Rescues Learning and Memory Dysfunction in Hepatic Encephalopathy Through miR-1264-5p/MEF2C Axis.* Mol Neurobiol. DOI: [10.1007/s12035-023-03205-1](https://doi.org/10.1007/s12035-023-03205-1) PMID: [36645630](https://pubmed.ncbi.nlm.nih.gov/36645630/)

---

## miR-449a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Upregulated | +7.41 | 2.23e-22 | 825.2 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UGGCAGUGUAUUGUUAGCUGGU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 79**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Syt1 | 4 | -1.198 |
| Notch1 | 1 | -1.178 |
| Numbl | 2 | -0.783 |
| Ing5 | 1 | -0.766 |
| Zfp282 | 2 | -0.619 |
| Met | 2 | -0.578 |
| Slc35g2 | 1 | -0.576 |
| Tom1 | 1 | -0.562 |
| Fam126b | 1 | -0.526 |
| Elmod1 | 1 | -0.524 |

**Top target gene: Syt1** (synaptotagmin I)

*Function:* Enables several functions, including calcium ion sensor activity; calcium-dependent phospholipid binding activity; and syntaxin-1 binding activity. Involved in modulation of chemical synaptic transmission; regulation of dopamine secretion; and synaptic vesicle exocytosis. Acts upstream of or within calcium ion-regulated exocytosis of neurotransmitter; spontaneous neurotransmitter secretion; and synchronous neurotransmitter secretion. Located in several cellular components, including Golgi appara...

*NCBI Gene ID:* [20979](https://www.ncbi.nlm.nih.gov/gene/20979)

### Biological Function Summary

Gene target analysis and our functional study with miR-449a-5p have revealed its potential as a serotherapeutic. (PMID: 36976763) Moreover, CFAR acted as a ceRNA sponge for miR-449a-5p and derepressed the expression of LOXL3, which we experimentally established as a target gene of miR-449a-5p. (PMID: 36334219) In contrast to CFAR, miR-449a-5p was found to be significantly downregulated in cardiac fibrosis, and artificial knockdown of miR-449a-5p exacerbated fibrogenesis, whereas overexpression of miR-449a-5p impeded fibrogenesis. (PMID: 36334219) Collectively, our study established CFAR as a new profibrotic factor acting through a novel miR-449a-5p/LOXL3/mTOR axis in the heart and therefore might be considered as a potential molecular target for the treatment of cardiac fibrosis and associated heart diseases. (PMID: 36334219) METHODS: MiR-449a-5p target genes were identified by Ago-RIP sequencing and validated by luciferase reporter assays and expression analyses. (PMID: 34976171)

### Literature

1. Li B et al. (2021). *miR‑449a‑5p suppresses CDK6 expression to inhibit cardiomyocyte proliferation.* Mol Med Rep. DOI: [10.3892/mmr.2020.11652](https://doi.org/10.3892/mmr.2020.11652) PMID: [33179102](https://pubmed.ncbi.nlm.nih.gov/33179102/)

2. Noureddine S et al. (2023). *microRNA-449a reduces growth hormone-stimulated senescent cell burden through PI3K-mTOR signaling.* Proc Natl Acad Sci U S A. DOI: [10.1073/pnas.2213207120](https://doi.org/10.1073/pnas.2213207120) PMID: [36976763](https://pubmed.ncbi.nlm.nih.gov/36976763/)

3. Zhang M et al. (2023). *LncRNA CFAR promotes cardiac fibrosis via the miR-449a-5p/LOXL3/mTOR axis.* Sci China Life Sci. DOI: [10.1007/s11427-021-2132-9](https://doi.org/10.1007/s11427-021-2132-9) PMID: [36334219](https://pubmed.ncbi.nlm.nih.gov/36334219/)

4. Reinkens T et al. (2022). *Ago-RIP Sequencing Identifies New MicroRNA-449a-5p Target Genes Increasing Sorafenib Efficacy in Hepatocellular Carcinoma.* J Cancer. DOI: [10.7150/jca.66016](https://doi.org/10.7150/jca.66016) PMID: [34976171](https://pubmed.ncbi.nlm.nih.gov/34976171/)

5. Jiang T et al. (2020). *MiR-449a-5p regulates the proliferation of esophageal carcinoma cell by targeting B-cell lymphoma 2.* Transl Cancer Res. DOI: [10.21037/tcr-20-2869](https://doi.org/10.21037/tcr-20-2869) PMID: [35117327](https://pubmed.ncbi.nlm.nih.gov/35117327/)

---

## miR-764-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Upregulated | +8.00 | 7.86e-15 | 555.8 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `GGUGCUCACAUGUCCUCCU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

In this study, we found that miR-764-5p is up-expressed during the osteoblast differentiation in calvarial and osteoblast progenitor cells, coupled with down-expression of CHIP protein. (PMID: 22407479) We observed that forced expression or inhibition of miR-764-5p decreased or increased the CHIP protein level through affecting its translation by targeting the 3'-UTR region. (PMID: 22407479) Perturbation of miR-764-5p resulted in altered differentiation fate of osteoblast progenitor cells and the role of miR-764-5p was reversed by overexpression of CHIP, whereas depletion of CHIP impaired the effect of miR-764-5p. (PMID: 22407479) Our data showed that miR-764-5p positively regulates osteoblast differentiation from osteoblast progenitor cells by repressing the translation of CHIP protein. (PMID: 22407479) The expressions of miR-383-5p and miR-764-5p were up-regulated after CUMS, while their expressions were down-regulated by EA intervention. (PMID: 27264487)

### Literature

1. Guo J et al. (2012). *miR-764-5p promotes osteoblast differentiation through inhibition of CHIP/STUB1 expression.* J Bone Miner Res. DOI: [10.1002/jbmr.1597](https://doi.org/10.1002/jbmr.1597) PMID: [22407479](https://pubmed.ncbi.nlm.nih.gov/22407479/)

2. Kawakita R et al. (2023). *Age‑related brainstem degeneration through microRNA modulation in mice.* Mol Med Rep. DOI: [10.3892/mmr.2023.13032](https://doi.org/10.3892/mmr.2023.13032) PMID: [37326032](https://pubmed.ncbi.nlm.nih.gov/37326032/)

3. Duan DM et al. (2016). *A microarray study of chronic unpredictable mild stress rat blood serum with electro-acupuncture intervention.* Neurosci Lett. DOI: [10.1016/j.neulet.2016.05.054](https://doi.org/10.1016/j.neulet.2016.05.054) PMID: [27264487](https://pubmed.ncbi.nlm.nih.gov/27264487/)

4. Gao B et al. (2020). *Effects of Egr1 on pancreatic acinar intracellular trypsinogen activation and the associated ceRNA network.* Mol Med Rep. DOI: [10.3892/mmr.2020.11316](https://doi.org/10.3892/mmr.2020.11316) PMID: [32705196](https://pubmed.ncbi.nlm.nih.gov/32705196/)

---

## miR-34c-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Upregulated | +6.74 | 1.24e-12 | 417.3 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-34c-5p** - **100% identical** (23 nt)

Sequence: `AGGCAGUGUAGUUAGCUGAUUGC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 18**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Trank1 | 2 | -0.965 |
| Asb1 | 1 | -0.777 |
| Gpr101 | 1 | -0.705 |
| Arfgap1 | 1 | -0.605 |
| Prex2 | 1 | -0.505 |
| Abr | 1 | -0.439 |
| Zdhhc23 | 1 | -0.388 |
| Galnt7 | 1 | -0.385 |
| Glce | 1 | -0.35 |
| Atoh1 | 1 | -0.266 |

**Top target gene: Trank1** (tetratricopeptide repeat and ankyrin repeat containing 1)

*Function:* Is expressed in adrenal cortex; central nervous system; frenulum; lung; and seminiferous cord. Orthologous to human TRANK1 (tetratricopeptide repeat and ankyrin repeat containing 1). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [320429](https://www.ncbi.nlm.nih.gov/gene/320429)

### Biological Function Summary

We selected 13 miRNAs with altered expressions in testis tissue (hsa-miR-122-5p, hsa-miR-145-5p, hsa-miR-16-5p, hsa-miR-193a-3p, hsa-miR-19a-3p, hsa-miR-23a-3p, hsa-miR-30b-5p, hsa-miR-34b-5p, hsa-miR-34c-5p, hsa-miR-374b-5p, hsa-miR-449a, hsa-miR-574-3p and hsa-miR-92a-3p), and systematically ex... (PMID: 35760398) In consideration of the currently limited research on microRNAs in BAS, this study aimed to explore the role and mechanism of miR-34c-5p in BAS. (PMID: 38374244) The expression of miR-34c-5p in BAS granulation tissues showed a significant down-regulation compared with the normal control group. (PMID: 38374244) Moreover, miR-34c-5p mimics suppressed the proliferation and differentiation of human bronchial fibroblasts (HBFs) and the epithelial-mesenchymal transition (EMT) of human bronchial epithelial cells (HBE). (PMID: 38374244) Conversely, miR-34c-5p inhibitors aggravated those effects. (PMID: 38374244)

### Literature

1. Burgos CF et al. (2022). *MicroRNA expression in male infertility.* Reprod Fertil Dev. DOI: [10.1071/RD21131](https://doi.org/10.1071/RD21131) PMID: [35760398](https://pubmed.ncbi.nlm.nih.gov/35760398/)

2. Wei J et al. (2024). *miR-34c-5p inhibited fibroblast proliferation, differentiation and epithelial-mesenchymal transition in benign airway stenosis via MDMX/p53 pathway.* Funct Integr Genomics. DOI: [10.1007/s10142-024-01317-y](https://doi.org/10.1007/s10142-024-01317-y) PMID: [38374244](https://pubmed.ncbi.nlm.nih.gov/38374244/)

3. Luo Y et al. (2020). *The role of miR-34c-5p/Notch in epithelial-mesenchymal transition (EMT) in endometriosis.* Cell Signal. DOI: [10.1016/j.cellsig.2020.109666](https://doi.org/10.1016/j.cellsig.2020.109666) PMID: [32353411](https://pubmed.ncbi.nlm.nih.gov/32353411/)

4. Wang S et al. (2025). *Ano5 Deficiency Leads to Abnormal Bone Formation via miR-34c-5p/KLF4/β-Catenin in Gnathodiaphyseal Dysplasia.* Int J Mol Sci. DOI: [10.3390/ijms26115267](https://doi.org/10.3390/ijms26115267) PMID: [40508076](https://pubmed.ncbi.nlm.nih.gov/40508076/)

5. Dorostghoal M et al. (2022). *Sperm miR-34c-5p Transcript Content and Its Association with Sperm Parameters in Unexplained Infertile Men.* Reprod Sci. DOI: [10.1007/s43032-021-00733-w](https://doi.org/10.1007/s43032-021-00733-w) PMID: [34494232](https://pubmed.ncbi.nlm.nih.gov/34494232/)

---

## miR-34b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Upregulated | +6.68 | 1.09e-11 | 380.0 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-34b-5p** - **13.0% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-34b-5p) | `AGGCAGUGUAAUUAGCUGAUUGU` | 23 nt |
| Human (hsa-miR-34b-5p) | `UAGGCAGUGUCAUUAGCUGAUUG` | 23 nt |

```
Mouse: AGGCAGUGUAAUUAGCUGAUUGU
       XX|XXXXXXXXX|XXXXXXX|XX
Human: UAGGCAGUGUCAUUAGCUGAUUG
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: A (mouse) -> U (human) *(in seed region)*
- Position 2: G (mouse) -> A (human) *(in seed region)*
- Position 4: C (mouse) -> G (human) *(in seed region)*
- Position 5: A (mouse) -> C (human) *(in seed region)*
- Position 6: G (mouse) -> A (human) *(in seed region)*
- Position 7: U (mouse) -> G (human) *(in seed region)*
- Position 8: G (mouse) -> U (human) *(in seed region)*
- Position 9: U (mouse) -> G (human)
- Position 10: A (mouse) -> U (human)
- Position 11: A (mouse) -> C (human)
- Position 12: U (mouse) -> A (human)
- Position 14: A (mouse) -> U (human)
- Position 15: G (mouse) -> A (human)
- Position 16: C (mouse) -> G (human)
- Position 17: U (mouse) -> C (human)
- Position 18: G (mouse) -> U (human)
- Position 19: A (mouse) -> G (human)
- Position 20: U (mouse) -> A (human)
- Position 22: G (mouse) -> U (human)
- Position 23: U (mouse) -> G (human)

*WARNING: 7 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 261**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Fam107a | 2 | -1.14 |
| Fam76a | 2 | -1.031 |
| Rras | 1 | -1.026 |
| Eno3 | 1 | -0.963 |
| Satb2 | 2 | -0.906 |
| Pacs1 | 2 | -0.862 |
| Shkbp1 | 1 | -0.847 |
| Tmed8 | 2 | -0.807 |
| Nsmce4a | 1 | -0.795 |
| Nudt13 | 1 | -0.78 |

**Top target gene: Fam107a** (family with sequence similarity 107, member A)

*Function:* Predicted to enable actin binding activity. Involved in several processes, including actin filament organization; negative regulation of long-term synaptic potentiation; and regulation of postsynapse assembly. Located in actin cytoskeleton; neuron projection; and synapse. Is active in glutamatergic synapse; postsynaptic actin cytoskeleton; and presynaptic actin cytoskeleton. Is expressed in nervous system and sensory organ. Orthologous to human FAM107A (family with sequence similarity 107 member...

*NCBI Gene ID:* [268709](https://www.ncbi.nlm.nih.gov/gene/268709)

### Biological Function Summary

As a member of the miRNA-34 family, miR-34b-5p serves as a powerful regulator of a suite of cellular activities, including cell growth, multiplication, development, differentiation, and apoptosis. (PMID: 36457043) This review aimed to provide an overview and update on the differential expression and function of miR-34b-5p in pathophysiologic processes, especially cancer and injury. (PMID: 36457043) Additionally, miR-34b-5p-mediated clinical trials have indicated promising consequences for the therapies of carcinomatosis and injury. (PMID: 36457043) With the application of the first tumor-targeted microRNA drug based on miR-34a mimics, it can be inferred that miR-34b-5p may become a crucial factor in the therapy of various diseases. (PMID: 36457043) We selected 13 miRNAs with altered expressions in testis tissue (hsa-miR-122-5p, hsa-miR-145-5p, hsa-miR-16-5p, hsa-miR-193a-3p, hsa-miR-19a-3p, hsa-miR-23a-3p, hsa-miR-30b-5p, hsa-miR-34b-5p, hsa-miR-34c-5p, hsa-miR-374b-5p, hsa-miR-449a, hsa-miR-574-3p and hsa-miR-92a-3p), and systematically ex... (PMID: 35760398)

### Literature

1. Bai X et al. (2022). *Role of microRNA-34b-5p in cancer and injury: how does it work?* Cancer Cell Int. DOI: [10.1186/s12935-022-02797-3](https://doi.org/10.1186/s12935-022-02797-3) PMID: [36457043](https://pubmed.ncbi.nlm.nih.gov/36457043/)

2. Burgos CF et al. (2022). *MicroRNA expression in male infertility.* Reprod Fertil Dev. DOI: [10.1071/RD21131](https://doi.org/10.1071/RD21131) PMID: [35760398](https://pubmed.ncbi.nlm.nih.gov/35760398/)

3. Tao S et al. (2022). *LncRNA PVT1 facilitates DLBCL development via miR-34b-5p/Foxp1 pathway.* Mol Cell Biochem. DOI: [10.1007/s11010-021-04335-7](https://doi.org/10.1007/s11010-021-04335-7) PMID: [35098439](https://pubmed.ncbi.nlm.nih.gov/35098439/)

4. Lu Y et al. (2024). *Sertraline-induced 5-HT dysregulation in mouse cardiomyocytes and the impact on calcium handling.* Am J Physiol Heart Circ Physiol. DOI: [10.1152/ajpheart.00692.2023](https://doi.org/10.1152/ajpheart.00692.2023) PMID: [39423037](https://pubmed.ncbi.nlm.nih.gov/39423037/)

5. Zhang L et al. (2023). *The miR-34b-5p-negative target Gnai2 aggravates fluorine combined with aluminum-induced apoptosis of rat offspring hippocampal neurons and NG108-15 cells.* Environ Sci Pollut Res Int. DOI: [10.1007/s11356-023-27135-6](https://doi.org/10.1007/s11356-023-27135-6) PMID: [37186186](https://pubmed.ncbi.nlm.nih.gov/37186186/)

---

## miR-448-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Upregulated | +7.67 | 1.16e-10 | 368.8 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UUGCAUAUGUAGGAUGUCCCAU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 610**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Lhfp | 1 | -0.894 |
| Tceal1 | 1 | -0.791 |
| Rab12 | 2 | -0.649 |
| Tmsb4x | 2 | -0.632 |
| Kctd9 | 2 | -0.58 |
| Mpc1 | 1 | -0.546 |
| Tmem55a | 1 | -0.542 |
| Glipr1l2 | 1 | -0.532 |
| Vash2 | 2 | -0.528 |
| Kcna4 | 1 | -0.513 |

**Top target gene: Lhfpl6** (LHFPL tetraspan subfamily member 6)

*Function:* Predicted to be active in membrane. Is expressed in several structures, including brain; genitourinary system; hemolymphoid system gland; skin; and spinal cord lateral wall. Orthologous to human LHFPL6 (LHFPL tetraspan subfamily member 6). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [108927](https://www.ncbi.nlm.nih.gov/gene/108927)

### Biological Function Summary

MATERIAL AND METHODS: This study compared the expression levels of miR-26a, miR-29a and miR-448-3p in 50 samples each of cerebral aneurysm tissues and normal superficial temporal artery tissues. (PMID: 36951025) RESULTS: Expression levels of miR-26a, miR-29a and miR-448-3p were increased in aneurysm tissues compared with normal vascular tissues. (PMID: 36951025) CONCLUSION: This study showed that miR-26a, miR-29a and miR-448-3p overexpression could play an important role in intracranial aneurysm development independent of aneurysm location and rupture status. (PMID: 36951025) miR-26a, miR-29a and miR-448-3p could act as potential therapeutic targets in patients with intracranial aneurysms; however, further studies are needed on this issue. (PMID: 36951025) Here, intracranial aneurysms (IAs) were surgically induced in Sprague-Dawley rats, and we found that miR-448-3p was downregulated and KLF5 was upregulated in IA rats. (PMID: 30322616)

### Literature

1. Boga Z et al. (2023). *The Role of miR-26a, miR-29a and miR-448-3p in the Development of Cerebral Aneurysm.* Turk Neurosurg. DOI: [10.5137/1019-5149.JTN.41357-22.1](https://doi.org/10.5137/1019-5149.JTN.41357-22.1) PMID: [36951025](https://pubmed.ncbi.nlm.nih.gov/36951025/)

2. Zhang JZ et al. (2018). *miR-448-3p controls intracranial aneurysm by regulating KLF5 expression.* Biochem Biophys Res Commun. DOI: [10.1016/j.bbrc.2018.10.032](https://doi.org/10.1016/j.bbrc.2018.10.032) PMID: [30322616](https://pubmed.ncbi.nlm.nih.gov/30322616/)

3. Kyrychenko S et al. (2015). *Pivotal role of miR-448 in the development of ROS-induced cardiomyopathy.* Cardiovasc Res. DOI: [10.1093/cvr/cvv238](https://doi.org/10.1093/cvr/cvv238) PMID: [26503985](https://pubmed.ncbi.nlm.nih.gov/26503985/)

4. Guan GY et al. (2020). *miR-448-3p alleviates diabetic vascular dysfunction by inhibiting endothelial-mesenchymal transition through DPP-4 dysregulation.* J Cell Physiol. DOI: [10.1002/jcp.29817](https://doi.org/10.1002/jcp.29817) PMID: [32542696](https://pubmed.ncbi.nlm.nih.gov/32542696/)

5. Liu C et al. (2025). *miR-448-3p/miR-1264-3p Participates in Intermittent Hypoxic Response in Hippocampus by Regulating Fam76b/hnRNPA2B1.* CNS Neurosci Ther. DOI: [10.1111/cns.70239](https://doi.org/10.1111/cns.70239) PMID: [39912396](https://pubmed.ncbi.nlm.nih.gov/39912396/)

---

## miR-139-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -3.21 | 6.31e-16 | 9.3 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-139-5p** - **95.7% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-139-5p) | `UCUACAGUGCACGUGUCUCCAG` | 22 nt |
| Human (hsa-miR-139-5p) | `UCUACAGUGCACGUGUCUCCAGU` | 23 nt |

```
Mouse: UCUACAGUGCACGUGUCUCCAG
       ||||||||||||||||||||||-
Human: UCUACAGUGCACGUGUCUCCAGU
```
(`|` = match, `X` = mismatch, `-` = length difference)

Length difference: 1 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 391**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Cxcr4 | 1 | -0.73 |
| Dpy30 | 1 | -0.714 |
| Cdc42 | 1 | -0.625 |
| Zranb2 | 2 | -0.549 |
| Akirin2 | 1 | -0.544 |
| Tmpo | 1 | -0.543 |
| Cdh20 | 2 | -0.527 |
| Morn4 | 1 | -0.523 |
| 2410004B18Rik | 1 | -0.521 |
| Tgif1 | 1 | -0.499 |

**Top target gene: Cxcr4** (C-X-C motif chemokine receptor 4)

*Function:* Predicted to enable several functions, including chemokine receptor activity; cytoskeletal protein binding activity; and ubiquitin protein ligase binding activity. Involved in several processes, including nervous system development; positive regulation of cold-induced thermogenesis; and positive regulation of oligodendrocyte differentiation. Acts upstream of or within several processes, including CXCL12-activated CXCR4 signaling pathway; circulatory system development; and nervous system develop...

*NCBI Gene ID:* [12767](https://www.ncbi.nlm.nih.gov/gene/12767)

### Biological Function Summary

Dual-luciferase reporter and chromatin immunoprecipitation assays were performed to investigate the targeted binding and inhibition of TOP2A 3' untranslated region (UTR) by miR-139-5p and the DNA enrichment of miR139-5p by EZH2 and H3K27me3. (PMID: 38008711) In addition, tissue microarrays were used to analyze the expression patterns and correlations among EZH2, TOP2A, and miR-139-5p expression in HCC. (PMID: 38008711) Mechanistically, EZH2 promotes TOP2A expression by regulating the H3K27me3-mediated epigenetic silencing of miR-139-5p. (PMID: 38008711) TOP2A is a direct target of miR-139-5p, and inhibition of miR-139-5p can reverse the promotion by EZH2 of TOP2A expression. (PMID: 38008711) The overexpression of miR-139-5p induces cellular senescence and inhibits proliferation of HCC cells both in vitro and in vivo. (PMID: 38008711)

### Literature

1. Wang K et al. (2023). *EZH2-H3K27me3-mediated silencing of mir-139-5p inhibits cellular senescence in hepatocellular carcinoma by activating TOP2A.* J Exp Clin Cancer Res. DOI: [10.1186/s13046-023-02855-2](https://doi.org/10.1186/s13046-023-02855-2) PMID: [38008711](https://pubmed.ncbi.nlm.nih.gov/38008711/)

2. Zhang HD et al. (2015). *MiR-139-5p: promising biomarker for cancer.* Tumour Biol. DOI: [10.1007/s13277-015-3199-3](https://doi.org/10.1007/s13277-015-3199-3) PMID: [25691250](https://pubmed.ncbi.nlm.nih.gov/25691250/)

3. Gao B et al. (2023). *miR-139-5p and miR-451a as a Diagnostic Biomarker in LUSC.* Pharmgenomics Pers Med. DOI: [10.2147/PGPM.S402750](https://doi.org/10.2147/PGPM.S402750) PMID: [37063774](https://pubmed.ncbi.nlm.nih.gov/37063774/)

4. Zhang Y et al. (2022). *MiR-139-5p/ENAH Affects Progression of Hepatocellular Carcinoma Cells.* Biochem Genet. DOI: [10.1007/s10528-022-10204-9](https://doi.org/10.1007/s10528-022-10204-9) PMID: [35254597](https://pubmed.ncbi.nlm.nih.gov/35254597/)

5. Ghafouri-Fard S et al. (2022). *Aberrant expression of miRNAs in epilepsy.* Mol Biol Rep. DOI: [10.1007/s11033-022-07188-5](https://doi.org/10.1007/s11033-022-07188-5) PMID: [35088379](https://pubmed.ncbi.nlm.nih.gov/35088379/)

---

## miR-185-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -1.48 | 3.35e-05 | 3.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-185-5p** - **100% identical** (22 nt)

Sequence: `UGGAGAGAAAGGCAGUUCCUGA`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 355**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Tram2 | 1 | -1.326 |
| Tead1 | 1 | -0.799 |
| Prrg3 | 1 | -0.798 |
| Ikzf4 | 2 | -0.766 |
| Brk1 | 1 | -0.74 |
| Cercam | 1 | -0.712 |
| Astn2 | 1 | -0.712 |
| Coro2b | 1 | -0.709 |
| Hsd3b6 | 1 | -0.69 |
| Cbfa2t3 | 1 | -0.652 |

**Top target gene: Tram2** (translocating chain-associating membrane protein 2)

*Function:* Predicted to be involved in collagen biosynthetic process and protein insertion into ER membrane. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum membrane. Is expressed in nose and skeleton. Orthologous to human TRAM2 (translocation associated membrane protein 2). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [170829](https://www.ncbi.nlm.nih.gov/gene/170829)

### Biological Function Summary

Emerging evidence implicates miR-185-5p in chronic inflammation diseases. (PMID: 35328023) However, the regulatory role of miR-185-5p in macrophage pro-inflammatory activation has not been studied previously. (PMID: 35328023) Here, we identified that miR-185-5p was one of the top genes and effectively downregulated in two macrophage miRNA expression datasets from GEO. (PMID: 35328023) Under LPS stress, miR-185-5p overexpression reduced pro-inflammatory cytokine expression, suppressed phagocytosis in RAW264.7 macrophage. (PMID: 35328023) miR-185-5p inhibitors augmented pro-inflammatory effects of LPS in macrophage. (PMID: 35328023)

### Literature

1. Ma X et al. (2022). *miR-185-5p Regulates Inflammation and Phagocytosis through CDC42/JNK Pathway in Macrophages.* Genes (Basel). DOI: [10.3390/genes13030468](https://doi.org/10.3390/genes13030468) PMID: [35328023](https://pubmed.ncbi.nlm.nih.gov/35328023/)

2. He D et al. (2024). *mmu-miR-185 regulates osteoclasts differentiation and migration by targeting Btk.* J Gene Med. DOI: [10.1002/jgm.3687](https://doi.org/10.1002/jgm.3687) PMID: [38690623](https://pubmed.ncbi.nlm.nih.gov/38690623/)

3. Lin R et al. (2022). *MiR-185-5p regulates the development of myocardial fibrosis.* J Mol Cell Cardiol. DOI: [10.1016/j.yjmcc.2021.12.011](https://doi.org/10.1016/j.yjmcc.2021.12.011) PMID: [34973276](https://pubmed.ncbi.nlm.nih.gov/34973276/)

4. Pang B et al. (2022). *MiR-185-5p suppresses acute myeloid leukemia by inhibiting GPX1.* Microvasc Res. DOI: [10.1016/j.mvr.2021.104296](https://doi.org/10.1016/j.mvr.2021.104296) PMID: [34863990](https://pubmed.ncbi.nlm.nih.gov/34863990/)

5. Ghafouri-Fard S et al. (2023). *A review on the role of LINC00152 in different disorders.* Pathol Res Pract. DOI: [10.1016/j.prp.2022.154274](https://doi.org/10.1016/j.prp.2022.154274) PMID: [36563561](https://pubmed.ncbi.nlm.nih.gov/36563561/)

---

## miR-219a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -1.80 | 3.71e-04 | 2.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-219a-5p** - **100% identical** (21 nt)

Sequence: `UGAUUGUCCAAACGCAAUUCU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 387**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Elmod2 | 2 | -0.864 |
| Gxylt1 | 2 | -0.862 |
| Rorb | 3 | -0.83 |
| Ddah1 | 1 | -0.684 |
| Ubash3b | 1 | -0.633 |
| Dazap1 | 1 | -0.602 |
| Foxj3 | 2 | -0.583 |
| Eya2 | 1 | -0.58 |
| Syt5 | 1 | -0.566 |
| Otx2 | 1 | -0.551 |

**Top target gene: Elmod2** (ELMO/CED-12 domain containing 2)

*Function:* Predicted to enable GTPase activator activity. Predicted to be involved in regulation of defense response to virus. Is expressed in several structures, including adrenal gland; genitourinary system; gut gland; nervous system; and stomach. Orthologous to human ELMOD2 (ELMO domain containing 2). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [244548](https://www.ncbi.nlm.nih.gov/gene/244548)

### Biological Function Summary

As Rorβ levels declined with differentiation, the expression of many of these miRNAs, including miR-219a-5p, was increased. (PMID: 30321475) We further demonstrated that miR-219a-5p was decreased in bone samples from old (24-month) mice, as compared with young (6-month) mice, concomitant with increased Rorβ expression. (PMID: 30321475) Importantly, we also found that miR-219a-5p expression was decreased in aged human bone biopsies compared with young controls, demonstrating that this phenomenon also occurs in aging bone in humans. (PMID: 30321475) Inhibition of miR-219a-5p in mouse calvarial osteoblasts led to increased Rorβ expression and decreased alkaline phosphatase expression and activity, whereas a miR-219a-5p mimic decreased Rorβ expression and increased osteogenic activity. (PMID: 30321475) Finally, we demonstrated that miR-219a-5p physically interacts with Rorβ mRNA in osteoblasts, defining Rorβ as a true molecular target of miR-219a-5p. (PMID: 30321475)

### Literature

1. Aquino-Martinez R et al. (2019). *miR-219a-5p Regulates Rorβ During Osteoblast Differentiation and in Age-related Bone Loss.* J Bone Miner Res. DOI: [10.1002/jbmr.3586](https://doi.org/10.1002/jbmr.3586) PMID: [30321475](https://pubmed.ncbi.nlm.nih.gov/30321475/)

2. Wang Q et al. (2022). *miR-219a-5p inhibits the pyroptosis in knee osteoarthritis by inactivating the NLRP3 signaling via targeting FBXO3.* Environ Toxicol. DOI: [10.1002/tox.23627](https://doi.org/10.1002/tox.23627) PMID: [35962723](https://pubmed.ncbi.nlm.nih.gov/35962723/)

3. Wei T et al. (2020). *miR-219a-5p enhances the radiosensitivity of non-small cell lung cancer cells through targeting CD164.* Biosci Rep. DOI: [10.1042/BSR20192795](https://doi.org/10.1042/BSR20192795) PMID: [32364222](https://pubmed.ncbi.nlm.nih.gov/32364222/)

4. Fu N et al. (2023). *Role of miR-219a-5p in regulating NMDAR in nonylphenol-induced synaptic plasticity damage.* Ecotoxicol Environ Saf. DOI: [10.1016/j.ecoenv.2023.114576](https://doi.org/10.1016/j.ecoenv.2023.114576) PMID: [36736231](https://pubmed.ncbi.nlm.nih.gov/36736231/)

5. Xiao Y et al. (2019). *miR-219a-5p Ameliorates Hepatic Ischemia/Reperfusion Injury via Impairing TP53BP2.* Dig Dis Sci. DOI: [10.1007/s10620-019-05535-4](https://doi.org/10.1007/s10620-019-05535-4) PMID: [30796685](https://pubmed.ncbi.nlm.nih.gov/30796685/)

---

## miR-1982-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -1.68 | 2.60e-03 | 1.9 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UCUCACCCUAUGUUCUCCCACAG`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-378d

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -3.41 | 5.89e-04 | 1.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-378d** - **81.8% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-378d) | `ACUGGCCUUGGAGUCAGAAGGU` | 22 nt |
| Human (hsa-miR-378d) | `ACUGGACUUGGAGUCAGAAA` | 20 nt |

```
Mouse: ACUGGCCUUGGAGUCAGAAGGU
       |||||X|||||||||||||X--
Human: ACUGGACUUGGAGUCAGAAA
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 6: C (mouse) -> A (human) *(in seed region)*
- Position 20: G (mouse) -> A (human)

Length difference: 2 nt

*WARNING: 1 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-378d shares seed family 'CUGGACU' with miR-378a-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 223**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Nme6 | 1 | -0.783 |
| Tmed5 | 1 | -0.75 |
| Psma1 | 1 | -0.677 |
| Grb2 | 1 | -0.661 |
| Gm28040 | 1 | -0.607 |
| Sbds | 1 | -0.583 |
| Grsf1 | 1 | -0.581 |
| Cables2 | 1 | -0.58 |
| Nisch | 2 | -0.561 |
| Kcnd1 | 1 | -0.556 |

**Top target gene: Nme6** (NME/NM23 nucleoside diphosphate kinase 6)

*Function:* Predicted to enable nucleoside diphosphate kinase activity. Predicted to be involved in negative regulation of cell growth and negative regulation of mitotic nuclear division. Located in mitochondrion. Is expressed in several structures, including alimentary system; genitourinary system; hemolymphoid system; nervous system; and sensory organ. Orthologous to human NME6 (NME/NM23 nucleoside diphosphate kinase 6). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [54369](https://www.ncbi.nlm.nih.gov/gene/54369)

### Biological Function Summary

Mechanistically, more circ-ZNF277 molecules could absorb more miR-378d, thereby competitively activating the NF-κB signaling pathway, promoting the release of pro-inflammatory cytokines including interleukins IL-1β and IL-6, and tumor necrosis factor-α (TNF-α), and inhibiting the survival of intr... (PMID: 39996735) Expressing miR-378d or si-Rab10 targeting the transcription of Rab10 could antagonize the effects of overexpression of circ-ZNF277, resulting in the reduced intracellular survival of Mtb. (PMID: 39996735) In summary, circ-ZNF277 inhibits the intracellular survival of Mtb via the miR-378d/Rab10 axis. (PMID: 39996735) miR-378d expression was measured by RT-qPCR in the internal cohort, and its association with clinicopathological features and prognosis was analyzed. (PMID: 40119180) MiRNA sequencing identified miR-378d as significantly downregulated in GC tissues and associated with poor prognosis. (PMID: 40119180)

### Literature

1. Zhu Y et al. (2025). *Circular RNA ZNF277 Sponges miR-378d to Inhibit the Intracellular Survival of Mycobacterium tuberculosis by Upregulating Rab10.* Cells. DOI: [10.3390/cells14040262](https://doi.org/10.3390/cells14040262) PMID: [39996735](https://pubmed.ncbi.nlm.nih.gov/39996735/)

2. Xing D et al. (2025). *miR-378d suppresses gastric cancer metastasis by targeting METTL4 to inhibit epithelial-mesenchymal transition.* J Mol Histol. DOI: [10.1007/s10735-025-10392-9](https://doi.org/10.1007/s10735-025-10392-9) PMID: [40119180](https://pubmed.ncbi.nlm.nih.gov/40119180/)

3. Yang Q et al. (2021). *Chemotherapy-elicited exosomal miR-378a-3p and miR-378d promote breast cancer stemness and chemoresistance via the activation of EZH2/STAT3 signaling.* J Exp Clin Cancer Res. DOI: [10.1186/s13046-021-01901-1](https://doi.org/10.1186/s13046-021-01901-1) PMID: [33823894](https://pubmed.ncbi.nlm.nih.gov/33823894/)

4. Peng J et al. (2021). *miR-378d suppresses malignant phenotype of ESCC cells through AKT signaling.* Cancer Cell Int. DOI: [10.1186/s12935-021-02403-y](https://doi.org/10.1186/s12935-021-02403-y) PMID: [34937563](https://pubmed.ncbi.nlm.nih.gov/34937563/)

5. Zhu Y et al. (2020). *Down-Regulation of miR-378d Increased Rab10 Expression to Help Clearance of Mycobacterium tuberculosis in Macrophages.* Front Cell Infect Microbiol. DOI: [10.3389/fcimb.2020.00108](https://doi.org/10.3389/fcimb.2020.00108) PMID: [32257967](https://pubmed.ncbi.nlm.nih.gov/32257967/)

---

## miR-378a-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -3.32 | 8.12e-04 | 1.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-378a-3p** - **95.5% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-378a-3p) | `ACUGGACUUGGAGUCAGAAGG` | 21 nt |
| Human (hsa-miR-378a-3p) | `ACUGGACUUGGAGUCAGAAGGC` | 22 nt |

```
Mouse: ACUGGACUUGGAGUCAGAAGG
       |||||||||||||||||||||-
Human: ACUGGACUUGGAGUCAGAAGGC
```
(`|` = match, `X` = mismatch, `-` = length difference)

Length difference: 1 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 217**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Nme6 | 1 | -0.783 |
| Tmed5 | 1 | -0.75 |
| Psma1 | 1 | -0.677 |
| Grb2 | 1 | -0.661 |
| Gm28040 | 1 | -0.607 |
| Sbds | 1 | -0.583 |
| Grsf1 | 1 | -0.581 |
| Cables2 | 1 | -0.58 |
| Nisch | 2 | -0.561 |
| Kcnd1 | 1 | -0.556 |

**Top target gene: Nme6** (NME/NM23 nucleoside diphosphate kinase 6)

*Function:* Predicted to enable nucleoside diphosphate kinase activity. Predicted to be involved in negative regulation of cell growth and negative regulation of mitotic nuclear division. Located in mitochondrion. Is expressed in several structures, including alimentary system; genitourinary system; hemolymphoid system; nervous system; and sensory organ. Orthologous to human NME6 (NME/NM23 nucleoside diphosphate kinase 6). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [54369](https://www.ncbi.nlm.nih.gov/gene/54369)

### Biological Function Summary

BAT-derived miR-378a-3p enhances gluconeogenesis by targeting p110α. (PMID: 37673898) miR-378 KO mice display reduced hepatic gluconeogenesis during cold exposure, while restoration of miR-378a-3p in iBAT induces the expression of gluconeogenic genes in the liver. (PMID: 37673898) This miR-378a-3p-mediated interorgan communication highlights a novel endocrine function of BAT in preventing hypoglycemia during cold stress. (PMID: 37673898) Its two mature strands, miR-378a-3p and miR-378a-5p, originate from the first intron of the peroxisome proliferator-activated receptor gamma, coactivator 1 beta (ppargc1b) gene encoding PGC-1β. (PMID: 26839547) The two strands of miR-378a, miR-378a-3p, and miR-378a-5p are encoded in the Ppargc1b gene and have an active role in the regulation of several metabolic pathways such as mitochondrial metabolism and autophagy. (PMID: 31748917)

### Literature

1. Xu J et al. (2023). *Cold-activated brown fat-derived extracellular vesicle-miR-378a-3p stimulates hepatic gluconeogenesis in male mice.* Nat Commun. DOI: [10.1038/s41467-023-41160-6](https://doi.org/10.1038/s41467-023-41160-6) PMID: [37673898](https://pubmed.ncbi.nlm.nih.gov/37673898/)

2. Krist B et al. (2015). *The Role of miR-378a in Metabolism, Angiogenesis, and Muscle Biology.* Int J Endocrinol. DOI: [10.1155/2015/281756](https://doi.org/10.1155/2015/281756) PMID: [26839547](https://pubmed.ncbi.nlm.nih.gov/26839547/)

3. Qin Y et al. (2022). *Depicting the Implication of miR-378a in Cancers.* Technol Cancer Res Treat. DOI: [10.1177/15330338221134385](https://doi.org/10.1177/15330338221134385) PMID: [36285472](https://pubmed.ncbi.nlm.nih.gov/36285472/)

4. Machado IF et al. (2020). *miR-378a: a new emerging microRNA in metabolism.* Cell Mol Life Sci. DOI: [10.1007/s00018-019-03375-z](https://doi.org/10.1007/s00018-019-03375-z) PMID: [31748917](https://pubmed.ncbi.nlm.nih.gov/31748917/)

5. He C et al. (2024). *Macrophage-derived extracellular vesicles regulate skeletal stem/progenitor Cell lineage fate and bone deterioration in obesity.* Bioact Mater. DOI: [10.1016/j.bioactmat.2024.06.035](https://doi.org/10.1016/j.bioactmat.2024.06.035) PMID: [39072285](https://pubmed.ncbi.nlm.nih.gov/39072285/)

---

## miR-378b

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -3.17 | 1.35e-03 | 1.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-378b** - **20.0% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-378b) | `CUGGACUUGGAGUCAGAAGA` | 20 nt |
| Human (hsa-miR-378b) | `ACUGGACUUGGAGGCAGAA` | 19 nt |

```
Mouse: CUGGACUUGGAGUCAGAAGA
       XXX|XXX|X|XXXXXXX|X-
Human: ACUGGACUUGGAGGCAGAA
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: C (mouse) -> A (human) *(in seed region)*
- Position 2: U (mouse) -> C (human) *(in seed region)*
- Position 3: G (mouse) -> U (human) *(in seed region)*
- Position 5: A (mouse) -> G (human) *(in seed region)*
- Position 6: C (mouse) -> A (human) *(in seed region)*
- Position 7: U (mouse) -> C (human) *(in seed region)*
- Position 9: G (mouse) -> U (human)
- Position 11: A (mouse) -> G (human)
- Position 12: G (mouse) -> A (human)
- Position 13: U (mouse) -> G (human)
- Position 14: C (mouse) -> G (human)
- Position 15: A (mouse) -> C (human)
- Position 16: G (mouse) -> A (human)
- Position 17: A (mouse) -> G (human)
- Position 19: G (mouse) -> A (human)

Length difference: 1 nt

*WARNING: 6 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-378b shares seed family 'CUGGACU' with miR-378a-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 223**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Nme6 | 1 | -0.783 |
| Tmed5 | 1 | -0.75 |
| Psma1 | 1 | -0.677 |
| Grb2 | 1 | -0.661 |
| Gm28040 | 1 | -0.607 |
| Sbds | 1 | -0.583 |
| Grsf1 | 1 | -0.581 |
| Cables2 | 1 | -0.58 |
| Nisch | 2 | -0.561 |
| Kcnd1 | 1 | -0.556 |

**Top target gene: Nme6** (NME/NM23 nucleoside diphosphate kinase 6)

*Function:* Predicted to enable nucleoside diphosphate kinase activity. Predicted to be involved in negative regulation of cell growth and negative regulation of mitotic nuclear division. Located in mitochondrion. Is expressed in several structures, including alimentary system; genitourinary system; hemolymphoid system; nervous system; and sensory organ. Orthologous to human NME6 (NME/NM23 nucleoside diphosphate kinase 6). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [54369](https://www.ncbi.nlm.nih.gov/gene/54369)

### Biological Function Summary

The goal of the present study was to elucidate the role of miR-378b in alcohol-induced hepatic insulin resistance and its underlying mechanism. (PMID: 32508647) This study has observed that miR-378b is up-regulated in National Institute on Alcohol Abuse and Alcoholism (NIAAA) alcoholic mouse models as well as in ethanol-induced L-02 cells in vitro. (PMID: 32508647) Furthermore, miR-378b overexpression impaired the insulin signaling pathway, and inhibition of miR-378b improved insulin sensitivity in vivo and in vitro. (PMID: 32508647) A mechanistic study revealed that IR and p110α are direct targets of miR-378b. (PMID: 32508647) Together, these results suggest that miR-378b controls insulin sensitivity by targeting the insulin receptor (IR) as well as p110α and possibly play an inhibitory role in the development of insulin resistance, thereby providing insights into the development of novel diagnostic and treatment methods. (PMID: 32508647)

### Literature

1. Li YY et al. (2020). *miR-378b Regulates Insulin Sensitivity by Targeting Insulin Receptor and p110α in Alcohol-Induced Hepatic Steatosis.* Front Pharmacol. DOI: [10.3389/fphar.2020.00717](https://doi.org/10.3389/fphar.2020.00717) PMID: [32508647](https://pubmed.ncbi.nlm.nih.gov/32508647/)

2. Zhang Y et al. (2022). *Methyl ferulic acid ameliorates alcohol-induced hepatic insulin resistance via miR-378b-mediated activation of PI3K-AKT pathway.* Biomed Pharmacother. DOI: [10.1016/j.biopha.2021.112462](https://doi.org/10.1016/j.biopha.2021.112462) PMID: [34844105](https://pubmed.ncbi.nlm.nih.gov/34844105/)

3. Zhao Z et al. (2021). *Circular RNA ZNF609 enhances proliferation and glycolysis during glioma progression by miR-378b/SLC2A1 axis.* Aging (Albany NY). DOI: [10.18632/aging.203331](https://doi.org/10.18632/aging.203331) PMID: [34520391](https://pubmed.ncbi.nlm.nih.gov/34520391/)

4. Konigsberg IR et al. (2024). *Multi-omic signatures of sarcoidosis and progression in bronchoalveolar lavage cells.* Respir Res. DOI: [10.1186/s12931-024-02919-7](https://doi.org/10.1186/s12931-024-02919-7) PMID: [39080656](https://pubmed.ncbi.nlm.nih.gov/39080656/)

5. Wang YZ et al. (2021). *microRNA-378b regulates ethanol-induced hepatic steatosis by targeting CaMKK2 to mediate lipid metabolism.* Bioengineered. DOI: [10.1080/21655979.2021.2003677](https://doi.org/10.1080/21655979.2021.2003677) PMID: [34898362](https://pubmed.ncbi.nlm.nih.gov/34898362/)

---

## miR-139-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -3.67 | 3.60e-04 | 1.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-139-3p** - **95.7% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-139-3p) | `UGGAGACGCGGCCCUGUUGGAG` | 22 nt |
| Human (hsa-miR-139-3p) | `UGGAGACGCGGCCCUGUUGGAGU` | 23 nt |

```
Mouse: UGGAGACGCGGCCCUGUUGGAG
       ||||||||||||||||||||||-
Human: UGGAGACGCGGCCCUGUUGGAGU
```
(`|` = match, `X` = mismatch, `-` = length difference)

Length difference: 1 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-139-3p shares seed family 'CUACAGU' with miR-139-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 391**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Cxcr4 | 1 | -0.73 |
| Dpy30 | 1 | -0.714 |
| Cdc42 | 1 | -0.625 |
| Zranb2 | 2 | -0.549 |
| Akirin2 | 1 | -0.544 |
| Tmpo | 1 | -0.543 |
| Cdh20 | 2 | -0.527 |
| Morn4 | 1 | -0.523 |
| 2410004B18Rik | 1 | -0.521 |
| Tgif1 | 1 | -0.499 |

**Top target gene: Cxcr4** (C-X-C motif chemokine receptor 4)

*Function:* Predicted to enable several functions, including chemokine receptor activity; cytoskeletal protein binding activity; and ubiquitin protein ligase binding activity. Involved in several processes, including nervous system development; positive regulation of cold-induced thermogenesis; and positive regulation of oligodendrocyte differentiation. Acts upstream of or within several processes, including CXCL12-activated CXCR4 signaling pathway; circulatory system development; and nervous system develop...

*NCBI Gene ID:* [12767](https://www.ncbi.nlm.nih.gov/gene/12767)

### Biological Function Summary

EV miR-139-3p was identified as a potential cardiac repair factor mediating macrophage polarization. (PMID: 36927608) Knockdown of miR-139-3p in MSCATV-EV significantly attenuated while overexpression of it in MSC-EV enhanced the effect on promoting M2 polarization by suppressing downstream signal transducer and activator of transcription 1 (Stat1). (PMID: 36927608) Furthermore, MSCATV-EV loaded with miR-139-3p inhibitors decreased while MSC-EV loaded with miR-139-3p mimics increased the expressions of M2 markers and cardioprotective efficacy. (PMID: 36927608) CONCLUSIONS: We uncovered a novel mechanism that MSCATV-EV remarkably facilitate cardiac repair in AMI by promoting macrophage polarization via miR-139-3p/Stat1 pathway, which has the great potential for clinical translation. (PMID: 36927608) Subsequently, we analyzed the target genes of miR-139-3p and their enrichment signaling pathways through bioinformatics. (PMID: 36917402)

### Literature

1. Ning Y et al. (2023). *Atorvastatin-pretreated mesenchymal stem cell-derived extracellular vesicles promote cardiac repair after myocardial infarction via shifting macrophage polarization by targeting microRNA-139-3p/Stat1 pathway.* BMC Med. DOI: [10.1186/s12916-023-02778-x](https://doi.org/10.1186/s12916-023-02778-x) PMID: [36927608](https://pubmed.ncbi.nlm.nih.gov/36927608/)

2. Wu Z et al. (2023). *miR-139-3p/Wnt5A Axis Inhibits Metastasis in Hepatoblastoma.* Mol Biotechnol. DOI: [10.1007/s12033-023-00714-1](https://doi.org/10.1007/s12033-023-00714-1) PMID: [36917402](https://pubmed.ncbi.nlm.nih.gov/36917402/)

3. Mao W et al. (2021). *ciRS-7 is a prognostic biomarker and potential gene therapy target for renal cell carcinoma.* Mol Cancer. DOI: [10.1186/s12943-021-01443-2](https://doi.org/10.1186/s12943-021-01443-2) PMID: [34740354](https://pubmed.ncbi.nlm.nih.gov/34740354/)

4. Ke H et al. (2022). *miR-139-3p/Kinesin family member 18B axis suppresses malignant progression of gastric cancer.* Bioengineered. DOI: [10.1080/21655979.2022.2033466](https://doi.org/10.1080/21655979.2022.2033466) PMID: [35137670](https://pubmed.ncbi.nlm.nih.gov/35137670/)

5. Sannigrahi MK et al. (2017). *Role of Host miRNA Hsa-miR-139-3p in HPV-16-Induced Carcinomas.* Clin Cancer Res. DOI: [10.1158/1078-0432.CCR-16-2936](https://doi.org/10.1158/1078-0432.CCR-16-2936) PMID: [28143871](https://pubmed.ncbi.nlm.nih.gov/28143871/)

---

## miR-378a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -3.21 | 1.75e-03 | 1.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-378a-5p** - **100% identical** (22 nt)

Sequence: `CUCCUGACUCCAGGUCCUGUGU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-378a-5p shares seed family 'CUGGACU' with miR-378a-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 223**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Nme6 | 1 | -0.783 |
| Tmed5 | 1 | -0.75 |
| Psma1 | 1 | -0.677 |
| Grb2 | 1 | -0.661 |
| Gm28040 | 1 | -0.607 |
| Sbds | 1 | -0.583 |
| Grsf1 | 1 | -0.581 |
| Cables2 | 1 | -0.58 |
| Nisch | 2 | -0.561 |
| Kcnd1 | 1 | -0.556 |

**Top target gene: Nme6** (NME/NM23 nucleoside diphosphate kinase 6)

*Function:* Predicted to enable nucleoside diphosphate kinase activity. Predicted to be involved in negative regulation of cell growth and negative regulation of mitotic nuclear division. Located in mitochondrion. Is expressed in several structures, including alimentary system; genitourinary system; hemolymphoid system; nervous system; and sensory organ. Orthologous to human NME6 (NME/NM23 nucleoside diphosphate kinase 6). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [54369](https://www.ncbi.nlm.nih.gov/gene/54369)

### Biological Function Summary

Its two mature strands, miR-378a-3p and miR-378a-5p, originate from the first intron of the peroxisome proliferator-activated receptor gamma, coactivator 1 beta (ppargc1b) gene encoding PGC-1β. (PMID: 26839547) The two strands of miR-378a, miR-378a-3p, and miR-378a-5p are encoded in the Ppargc1b gene and have an active role in the regulation of several metabolic pathways such as mitochondrial metabolism and autophagy. (PMID: 31748917) This study used miR-378a-5p overexpression and knockdown to manipulate OGD injury in nerve cells. (PMID: 39176087) The impact of astrocyte-derived exosomal miR-378a-5p on the regulation of cerebral ischemic neuroinflammation was assessed through analysis of nerve injury and pyroptosis protein expression. (PMID: 39176087) Further investigations revealed the involvement of astrocyte-derived exosomal miR-378a-5p in regulating pyroptosis by inhibiting NLRP3. (PMID: 39176087)

### Literature

1. Krist B et al. (2015). *The Role of miR-378a in Metabolism, Angiogenesis, and Muscle Biology.* Int J Endocrinol. DOI: [10.1155/2015/281756](https://doi.org/10.1155/2015/281756) PMID: [26839547](https://pubmed.ncbi.nlm.nih.gov/26839547/)

2. Qin Y et al. (2022). *Depicting the Implication of miR-378a in Cancers.* Technol Cancer Res Treat. DOI: [10.1177/15330338221134385](https://doi.org/10.1177/15330338221134385) PMID: [36285472](https://pubmed.ncbi.nlm.nih.gov/36285472/)

3. Machado IF et al. (2020). *miR-378a: a new emerging microRNA in metabolism.* Cell Mol Life Sci. DOI: [10.1007/s00018-019-03375-z](https://doi.org/10.1007/s00018-019-03375-z) PMID: [31748917](https://pubmed.ncbi.nlm.nih.gov/31748917/)

4. Sun R et al. (2024). *Astrocyte-derived exosomal miR-378a-5p mitigates cerebral ischemic neuroinflammation by modulating NLRP3-mediated pyroptosis.* Front Immunol. DOI: [10.3389/fimmu.2024.1454116](https://doi.org/10.3389/fimmu.2024.1454116) PMID: [39176087](https://pubmed.ncbi.nlm.nih.gov/39176087/)

5. Hu G et al. (2024). *MiR-378a-5p exerts a radiosensitizing effect on CRC through LRP8/β-catenin axis.* Cancer Biol Ther. DOI: [10.1080/15384047.2024.2308165](https://doi.org/10.1080/15384047.2024.2308165) PMID: [38389136](https://pubmed.ncbi.nlm.nih.gov/38389136/)

---

## miR-12191-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Lung | Downregulated | -4.73 | 2.94e-06 | 1.6 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CCCAUGGAGCUGUAGGAGCCG`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-142a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +5.22 | 3.00e-38 | 953.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-142-5p** - **100% identical** (21 nt)

Sequence: `CAUAAAGUAGAAAGCACUACU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 868**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Zfpm2 | 3 | -0.827 |
| Uba3 | 1 | -0.774 |
| Krtap20-2 | 1 | -0.612 |
| Gng13 | 1 | -0.596 |
| Atxn7l2 | 1 | -0.541 |
| Med28 | 1 | -0.528 |
| Ranbp1 | 1 | -0.5 |
| Fbxl3 | 1 | -0.496 |
| Cars2 | 1 | -0.483 |
| Ube2d1 | 1 | -0.481 |

**Top target gene: Zfpm2** (zinc finger protein, multitype 2)

*Function:* Enables transcription corepressor activity. Involved in several processes, including negative regulation of female gonad development; positive regulation of cardiac muscle cell proliferation; and positive regulation of male gonad development. Acts upstream of or within several processes, including circulatory system development; in utero embryonic development; and regulation of transcription by RNA polymerase II. Located in cytoplasm and male germ cell nucleus. Is expressed in several structures...

*NCBI Gene ID:* [22762](https://www.ncbi.nlm.nih.gov/gene/22762)

### Biological Function Summary

Further, miR-142a-5p/ mitofusin-1 (MFN1) axis was confirmed to be activated in denervated gastrocnemius, which disrupted the tubular mitochondrial network, and induced mitochondrial dysfunction, mitophagy and apoptosis. (PMID: 31938072) Furthermore, the atrophy of gastrocnemius induced by denervation was relieved through targeting miR-142a-5p/MFN1 axis. (PMID: 31938072) Conclusions: Collectively, our data revealed that miR-142a-5p was able to function as an important regulator of denervation-induced skeletal muscle atrophy by inducing mitochondrial dysfunction, mitophagy, and apoptosis via targeting MFN1. (PMID: 31938072) miR-142a-5p plays critical roles in multiple biological processes and diseases, such as inflammation and tumorigenesis. (PMID: 32700780) However, it remains to be explored if and how miR-142a-5p contributes to osteoblast differentiation. (PMID: 32700780)

### Literature

1. Yang X et al. (2020). *Denervation drives skeletal muscle atrophy and induces mitochondrial dysfunction, mitophagy and apoptosis via miR-142a-5p/MFN1 axis.* Theranostics. DOI: [10.7150/thno.40857](https://doi.org/10.7150/thno.40857) PMID: [31938072](https://pubmed.ncbi.nlm.nih.gov/31938072/)

2. Yuan H et al. (2021). *miR-142a-5p promoted osteoblast differentiation via targeting nuclear factor IA.* J Cell Physiol. DOI: [10.1002/jcp.29963](https://doi.org/10.1002/jcp.29963) PMID: [32700780](https://pubmed.ncbi.nlm.nih.gov/32700780/)

3. Cao Y et al. (2024). *CircRNA_001373 promotes liver fibrosis by regulating autophagy activation in hepatic stellate cells via the miR-142a-5p/Becn1 axis.* Hum Exp Toxicol. DOI: [10.1177/09603271241265105](https://doi.org/10.1177/09603271241265105) PMID: [39291962](https://pubmed.ncbi.nlm.nih.gov/39291962/)

4. Kim JO et al. (2018). *A novel system-level approach using RNA-sequencing data identifies miR-30-5p and miR-142a-5p as key regulators of apoptosis in myocardial infarction.* Sci Rep. DOI: [10.1038/s41598-018-33020-x](https://doi.org/10.1038/s41598-018-33020-x) PMID: [30279543](https://pubmed.ncbi.nlm.nih.gov/30279543/)

5. Zhou Z et al. (2016). *Mesenchymal Stem Cells Alleviate LPS-Induced Acute Lung Injury in Mice by MiR-142a-5p-Controlled Pulmonary Endothelial Cell Autophagy.* Cell Physiol Biochem. DOI: [10.1159/000438627](https://doi.org/10.1159/000438627) PMID: [26784440](https://pubmed.ncbi.nlm.nih.gov/26784440/)

---

## miR-142a-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +5.08 | 2.07e-26 | 628.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-142-3p** - **100% identical** (23 nt)

Sequence: `UGUAGUGUUUCCUACUUUAUGGA`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-142a-3p shares seed family 'GUAGUGU' with miR-142a-3p.1. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 312**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Samd12 | 1 | -1.2 |
| Cfl2 | 1 | -1.008 |
| Wasl | 2 | -1.007 |
| Hmga2 | 1 | -0.934 |
| Fam114a1 | 1 | -0.78 |
| Ptpn23 | 1 | -0.758 |
| Rab3a | 1 | -0.757 |
| Arntl | 1 | -0.741 |
| Rab12 | 1 | -0.731 |
| 4930402H24Rik | 2 | -0.729 |

**Top target gene: Samd12** (sterile alpha motif domain containing 12)

*Function:* Predicted to be involved in cell surface receptor protein tyrosine kinase signaling pathway. Predicted to be active in cytoplasmic side of plasma membrane. Human ortholog(s) of this gene implicated in familial adult myoclonic epilepsy 1. Orthologous to human SAMD12 (sterile alpha motif domain containing 12). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [320679](https://www.ncbi.nlm.nih.gov/gene/320679)

### Biological Function Summary

They also downregulated cellular levels of miR-142a-3p, resulting in increased levels of its target carnitine palmitoyl transferase 1A (CPT1A) which improved fatty acid oxidation (FAO) and oxidative phosphorylation (OxPHOS) in recipient cells. (PMID: 37593979) ApoE-dependent immunometabolic signaling by macrophage extracellular vesicles was dependent on transcriptional axes controlled by miR-146a-5p and miR-142a-3p that could be reproduced by infusing miR-146a mimics & miR-142a antagonists into hyperlipidemic apoE-deficient mice. (PMID: 37593979) In the present study, two novel miRNAs, miR-142a-3p and miR-155-5p, that were predicted to target Peli1 using bioinformatics were chosen, and their unique roles in METH-induced neuroinflammation via regulating Peli1 expression were identified. (PMID: 30914375) Our results showed that miR-142a-3p was significantly reduced in METH-induced neuroinflammation and was negatively associated with Peli1 expression both in BV2 cells and in the brain of mouse. (PMID: 30914375) Reciprocally, the overexpression of miR-142a-3p and miR-155-5p could directly suppress Peli1 expression and could protect against the inflammatory effects of METH treatment partially through activating p38 MAPK and NF-κB inflammatory pathways. (PMID: 30914375)

### Literature

1. Phu TA et al. (2023). *ApoE expression in macrophages communicates immunometabolic signaling that controls hyperlipidemia-driven hematopoiesis & inflammation via extracellular vesicles.* J Extracell Vesicles. DOI: [10.1002/jev2.12345](https://doi.org/10.1002/jev2.12345) PMID: [37593979](https://pubmed.ncbi.nlm.nih.gov/37593979/)

2. Yu G et al. (2019). *MiR-142a-3p and miR-155-5p reduce methamphetamine-induced inflammation: Role of the target protein Peli1.* Toxicol Appl Pharmacol. DOI: [10.1016/j.taap.2019.03.019](https://doi.org/10.1016/j.taap.2019.03.019) PMID: [30914375](https://pubmed.ncbi.nlm.nih.gov/30914375/)

3. Qi Z et al. (2022). *MiR-142a-3p: A novel ACh receptor transcriptional regulator in association with peripheral nerve injury.* Mol Ther Nucleic Acids. DOI: [10.1016/j.omtn.2022.10.005](https://doi.org/10.1016/j.omtn.2022.10.005) PMID: [36381585](https://pubmed.ncbi.nlm.nih.gov/36381585/)

4. Fan P et al. (2020). *miR-142a-3p promotes the proliferation of porcine hemagglutinating encephalomyelitis virus by targeting Rab3a.* Arch Virol. DOI: [10.1007/s00705-019-04470-z](https://doi.org/10.1007/s00705-019-04470-z) PMID: [31834525](https://pubmed.ncbi.nlm.nih.gov/31834525/)

5. Yang Y et al. (2019). *MiR-142a-3p alleviates Escherichia coli derived lipopolysaccharide-induced acute lung injury by targeting TAB2.* Microb Pathog. DOI: [10.1016/j.micpath.2019.103721](https://doi.org/10.1016/j.micpath.2019.103721) PMID: [31494298](https://pubmed.ncbi.nlm.nih.gov/31494298/)

---

## miR-3964

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +5.23 | 8.13e-20 | 479.5 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AUAAGGUAGAAAGCACUAAA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-130b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +3.96 | 6.22e-29 | 472.2 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-130b-3p** - **100% identical** (22 nt)

Sequence: `CAGUGCAAUGAUGAAAGGGCAU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 191**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Klf7 | 2 | -0.782 |
| Pik3cb | 2 | -0.781 |
| Cdk19 | 2 | -0.762 |
| St18 | 2 | -0.709 |
| B630005N14Rik | 2 | -0.692 |
| Sh3d19 | 1 | -0.668 |
| Ccdc126 | 1 | -0.626 |
| Acvr1 | 2 | -0.606 |
| Cbfb | 1 | -0.551 |
| Rnf38 | 2 | -0.544 |

**Top target gene: Klf7** (Kruppel-like transcription factor 7 (ubiquitous))

*Function:* Enables DNA binding activity and DNA-binding transcription factor activity. Acts upstream of or within axon guidance; dendrite morphogenesis; and positive regulation of DNA-templated transcription. Predicted to be located in cytosol and nucleoplasm. Is expressed in several structures, including genitourinary system; gut; immune system; nervous system; and sensory organ. Orthologous to human KLF7 (KLF transcription factor 7). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [93691](https://www.ncbi.nlm.nih.gov/gene/93691)

### Biological Function Summary

Although the role of miR-130b-3p as an oncogene that accelerates cancer progression by suppressing ferroptosis has been demonstrated, its role in the regulation of ferroptosis and cardiac injury in Lipopolysaccharide (LPS)-induced cardiomyopathy has not been fully clarified. (PMID: 37705752) In this study, we demonstrated that miR-130b-3p remarkably improved cardiac function and ameliorated morphological damage to heart tissue in LPS-induced mice. (PMID: 37705752) miR-130b-3p also improved cell viability and mitochondrial function and reduced the production of lipid ROS and ferroptosis in LPS-treated H9c2 cells. (PMID: 37705752) In addition, miR-130b-3p significantly upregulated GPX4 expression and suppressed ACSL4 activity in LPS-induced mouse heart tissue and H9c2 cells. (PMID: 37705752) Mechanistically, we used database analysis to locate miR-130b-3p and confirmed its inhibitory effects on the ferroptosis-related gene ACSL4 and autophagy-related gene PRKAA1 using a dual-luciferase reporter assay. (PMID: 37705752)

### Literature

1. Qi Z et al. (2023). *microRNA-130b-3p Attenuates Septic Cardiomyopathy by Regulating the AMPK/mTOR Signaling Pathways and Directly Targeting ACSL4 against Ferroptosis.* Int J Biol Sci. DOI: [10.7150/ijbs.82287](https://doi.org/10.7150/ijbs.82287) PMID: [37705752](https://pubmed.ncbi.nlm.nih.gov/37705752/)

2. Gan L et al. (2020). *Small Extracellular Microvesicles Mediated Pathological Communications Between Dysfunctional Adipocytes and Cardiomyocytes as a Novel Mechanism Exacerbating Ischemia/Reperfusion Injury in Diabetic Mice.* Circulation. DOI: [10.1161/CIRCULATIONAHA.119.042640](https://doi.org/10.1161/CIRCULATIONAHA.119.042640) PMID: [31918577](https://pubmed.ncbi.nlm.nih.gov/31918577/)

3. Han X et al. (2024). *Mechanism of miR-130b-3p in relieving airway inflammation in asthma through HMGB1-TLR4-DRP1 axis.* Cell Mol Life Sci. DOI: [10.1007/s00018-024-05529-0](https://doi.org/10.1007/s00018-024-05529-0) PMID: [39704848](https://pubmed.ncbi.nlm.nih.gov/39704848/)

4. Chai C et al. (2023). *BCR-ABL1-driven exosome-miR130b-3p-mediated gap-junction Cx43 MSC intercellular communications imply therapies of leukemic subclonal evolution.* Theranostics. DOI: [10.7150/thno.83178](https://doi.org/10.7150/thno.83178) PMID: [37554265](https://pubmed.ncbi.nlm.nih.gov/37554265/)

5. Song D et al. (2022). *MiR-130b-3p promotes colorectal cancer progression by targeting CHD9.* Cell Cycle. DOI: [10.1080/15384101.2022.2029240](https://doi.org/10.1080/15384101.2022.2029240) PMID: [35100082](https://pubmed.ncbi.nlm.nih.gov/35100082/)

---

## miR-211-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +5.01 | 8.13e-20 | 457.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-211-5p** - **95.5% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-211-5p) | `UUCCCUUUGUCAUCCUUUGCCU` | 22 nt |
| Human (hsa-miR-211-5p) | `UUCCCUUUGUCAUCCUUCGCCU` | 22 nt |

```
Mouse: UUCCCUUUGUCAUCCUUUGCCU
       |||||||||||||||||X||||
Human: UUCCCUUUGUCAUCCUUCGCCU
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 18: U (mouse) -> C (human)

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 158**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Zfp629 | 1 | -0.759 |
| Ssr3 | 1 | -0.616 |
| Ephb6 | 1 | -0.593 |
| Grin2b | 1 | -0.584 |
| Lsm5 | 1 | -0.567 |
| Ak4 | 2 | -0.562 |
| St7 | 1 | -0.561 |
| Mapre2 | 3 | -0.546 |
| Rnf170 | 3 | -0.544 |
| Creb3l4 | 1 | -0.522 |

**Top target gene: Zfp629** (zinc finger protein 629)

*Function:* Predicted to enable DNA binding activity and zinc ion binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. Is expressed in genitourinary system; limb mesenchyme; nervous system; and retina layer. Orthologous to human ZNF629 (zinc finger protein 629). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [320683](https://www.ncbi.nlm.nih.gov/gene/320683)

### Biological Function Summary

The dynamic decrease in miR-211-5p expression induces hypersynchronization and both nonconvulsive and convulsive seizures, and forebrain miR-211-5p suppression exacerbates long-lasting pentylenetetrazole-induced seizures. (PMID: 38191407) Additionally, in this study, induction of miR-211-5p expression or genetic-silencing of P2RX7 significantly reduced the seizure score and duration in murine models through the abovementioned pathways. (PMID: 38191407) These results suggest that the miR-211-5p/P2RX7 axis is a novel target for suppressing both ferroptosis and epilepsy. (PMID: 38191407) Mechanistically, microRNA-211-5p negatively regulates GDNF, and lncXIST serves as a miR-211-5p sponge. (PMID: 38454138) Further study demonstrates that DSGM leads to abnormal upregulation of miR-211-5p in gut-derived circulating exosomes, which inhibited the expression of meiosis-specific with coiled-coil domain (Meioc) in the testes and impaired spermatogenesis by disturbing meiosis process. (PMID: 38526201)

### Literature

1. Li X et al. (2024). *The microRNA-211-5p/P2RX7/ERK/GPX4 axis regulates epilepsy-associated neuronal ferroptosis and oxidative stress.* J Neuroinflammation. DOI: [10.1186/s12974-023-03009-z](https://doi.org/10.1186/s12974-023-03009-z) PMID: [38191407](https://pubmed.ncbi.nlm.nih.gov/38191407/)

2. Cheng K et al. (2024). *Exosomal lncRNA XIST promotes perineural invasion of pancreatic cancer cells via miR-211-5p/GDNF.* Oncogene. DOI: [10.1038/s41388-024-02994-6](https://doi.org/10.1038/s41388-024-02994-6) PMID: [38454138](https://pubmed.ncbi.nlm.nih.gov/38454138/)

3. Chen T et al. (2024). *Gut-Derived Exosomes Mediate the Microbiota Dysbiosis-Induced Spermatogenesis Impairment by Targeting Meioc in Mice.* Adv Sci (Weinh). DOI: [10.1002/advs.202310110](https://doi.org/10.1002/advs.202310110) PMID: [38526201](https://pubmed.ncbi.nlm.nih.gov/38526201/)

4. Elmizadeh K et al. (2023). *Has_circ_0008285/miR-211-5p/SIRT-1 Axis Suppress Ovarian Cancer Cells Progression.* Int J Mol Cell Med. DOI: [10.22088/IJMCM.BUMS.12.4.401](https://doi.org/10.22088/IJMCM.BUMS.12.4.401) PMID: [39006198](https://pubmed.ncbi.nlm.nih.gov/39006198/)

5. Li F et al. (2025). *The research progress of LACC1.* Front Immunol. DOI: [10.3389/fimmu.2025.1698702](https://doi.org/10.3389/fimmu.2025.1698702) PMID: [41376621](https://pubmed.ncbi.nlm.nih.gov/41376621/)

---

## miR-342-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +3.51 | 1.18e-24 | 340.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-342-5p** - **95.5% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-342-5p) | `AGGGGUGCUAUCUGUGAUUGAG` | 22 nt |
| Human (hsa-miR-342-5p) | `AGGGGUGCUAUCUGUGAUUGA` | 21 nt |

```
Mouse: AGGGGUGCUAUCUGUGAUUGAG
       |||||||||||||||||||||-
Human: AGGGGUGCUAUCUGUGAUUGA
```
(`|` = match, `X` = mismatch, `-` = length difference)

Length difference: 1 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-342-5p shares seed family 'CUCACAC' with miR-342-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 264**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Fam53c | 6 | -1.05 |
| Mmab | 2 | -0.932 |
| Diras1 | 1 | -0.931 |
| Sfn | 2 | -0.782 |
| Ube2d2a | 1 | -0.691 |
| Agpat4 | 1 | -0.672 |
| Spock2 | 1 | -0.564 |
| Kdsr | 2 | -0.551 |
| Lrp8 | 1 | -0.549 |
| Dkk1 | 1 | -0.496 |

**Top target gene: Fam53c** (family with sequence similarity 53, member C)

*Function:* Predicted to be involved in protein import into nucleus. Predicted to be active in nucleus. Orthologous to human FAM53C (family with sequence similarity 53 member C). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [66306](https://www.ncbi.nlm.nih.gov/gene/66306)

### Biological Function Summary

For AS therapy, adipose mesenchymal stem cell-derived exosomes protect endothelial cells from AS aggravation, via inhibiting miR-342-5p. (PMID: 32772195) OBJECTIVE: The aim of this research was to explore the role of miR-342-5p in EV71 replication. (PMID: 37479047) RESULTS: Transcriptome sequencing analyses know that the Wnt pathway played a role in EV71 infection, and the CTNNBIP1 gene in this pathway was the target gene of miR-342-5p. (PMID: 37479047) Whether in HMC3 cells or in the spinal cord tissue from the suckling mice, high levels of miR-342-5p markedly promoted EV71 VP1 mRNA and protein expression, elevated TNF-α, IL-6, and IL-10 levels, and inhibited IFN-β levels. (PMID: 37479047) In addition, highly expressed miR-342-5p destroyed neuronal structure in spinal cord tissues and reduced the number of glial cells. (PMID: 37479047)

### Literature

1. Wang H et al. (2020). *Exosomes: Multifaceted Messengers in Atherosclerosis.* Curr Atheroscler Rep. DOI: [10.1007/s11883-020-00871-7](https://doi.org/10.1007/s11883-020-00871-7) PMID: [32772195](https://pubmed.ncbi.nlm.nih.gov/32772195/)

2. Tang C et al. (2023). *miR-342-5p targets CTNNBIP1 to promote enterovirus 71 replication.* Microb Pathog. DOI: [10.1016/j.micpath.2023.106259](https://doi.org/10.1016/j.micpath.2023.106259) PMID: [37479047](https://pubmed.ncbi.nlm.nih.gov/37479047/)

3. Hayek H et al. (2024). *The Regulation of Fatty Acid Synthase by Exosomal miR-143-5p and miR-342-5p in Idiopathic Pulmonary Fibrosis.* Am J Respir Cell Mol Biol. DOI: [10.1165/rcmb.2023-0232OC](https://doi.org/10.1165/rcmb.2023-0232OC) PMID: [38117249](https://pubmed.ncbi.nlm.nih.gov/38117249/)

4. Veys C et al. (2022). *Tumor Suppressive Role of miR-342-5p and miR-491-5p in Human Osteosarcoma Cells.* Pharmaceuticals (Basel). DOI: [10.3390/ph15030362](https://doi.org/10.3390/ph15030362) PMID: [35337159](https://pubmed.ncbi.nlm.nih.gov/35337159/)

5. Li J et al. (2019). *Inflammation-regulatory microRNAs: Valuable targets for intracranial atherosclerosis.* J Neurosci Res. DOI: [10.1002/jnr.24487](https://doi.org/10.1002/jnr.24487) PMID: [31254290](https://pubmed.ncbi.nlm.nih.gov/31254290/)

---

## miR-130b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +3.67 | 3.04e-20 | 282.8 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-130b-5p** - **95.5% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-130b-5p) | `ACUCUUUCCCUGUUGCACUACU` | 22 nt |
| Human (hsa-miR-130b-5p) | `ACUCUUUCCCUGUUGCACUAC` | 21 nt |

```
Mouse: ACUCUUUCCCUGUUGCACUACU
       |||||||||||||||||||||-
Human: ACUCUUUCCCUGUUGCACUAC
```
(`|` = match, `X` = mismatch, `-` = length difference)

Length difference: 1 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-130b-5p shares seed family 'AGUGCAA' with miR-130b-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 799**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Skida1 | 4 | -0.959 |
| Vps37a | 2 | -0.925 |
| Mybl1 | 3 | -0.895 |
| Maf | 2 | -0.792 |
| Klf7 | 2 | -0.782 |
| Pik3cb | 2 | -0.781 |
| Pparg | 1 | -0.781 |
| Slain1 | 2 | -0.763 |
| Cdk19 | 2 | -0.762 |
| Sybu | 2 | -0.746 |

**Top target gene: Skida1** (SKI/DACH domain containing 1)

*Function:* Is expressed in several structures, including body cavity or lining; genitourinary system; nervous system; respiratory system; and vertebral axis musculature. Orthologous to human SKIDA1 (SKI/DACH domain containing 1). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [72668](https://www.ncbi.nlm.nih.gov/gene/72668)

### Biological Function Summary

Mechanistically, we found that circDlc1(2) physically interacts with some mRNAs, associated with glutamate receptor signaling (gluRNAs), and with miR-130b-5p, a translational regulator of these transcripts. (PMID: 39321023) Notably, differently from canonical microRNA (miRNA) "sponges," circDlc1(2) synergizes with miR-130b-5p to repress gluRNA expression. (PMID: 39321023) We found that circDlc1(2) is required to spatially control miR-130b-5p localization at synaptic regions where gluRNA is localized, indicating a different layer of regulation where circRNAs ensure robust control of gene expression via the correct subcellular compartmentalization of functionally li... (PMID: 39321023) The present study aimed to investigate the effect of miR-130b duplex (miR-130b-5p, miR-130b-3p) and its target gene KLF3 in regulating goat intramuscular adipocyte differentiation. (PMID: 37279650) miR-130b-5p and miR-130b-3p mimics or inhibitors and their corresponding controls were transfected into goat intramuscular preadipocytes, respectively, and differentiation was induced by 50μM oleic acid for 48 h. (PMID: 37279650)

### Literature

1. Silenzi V et al. (2024). *A tripartite circRNA/mRNA/miRNA interaction regulates glutamatergic signaling in the mouse brain.* Cell Rep. DOI: [10.1016/j.celrep.2024.114766](https://doi.org/10.1016/j.celrep.2024.114766) PMID: [39321023](https://pubmed.ncbi.nlm.nih.gov/39321023/)

2. Li Y et al. (2023). *miR-130b duplex (miR-130b-3p/miR-130b-5p) negatively regulates goat intramuscular preadipocyte lipid droplets accumulation by inhibiting Krüppel-like factor 3 expression.* J Anim Sci. DOI: [10.1093/jas/skad184](https://doi.org/10.1093/jas/skad184) PMID: [37279650](https://pubmed.ncbi.nlm.nih.gov/37279650/)

3. Feng K et al. (2024). *Critical Role of miR-130b-5p in Cardiomyocyte Proliferation and Cardiac Repair in Mice After Myocardial Infarction.* Stem Cells. DOI: [10.1093/stmcls/sxad080](https://doi.org/10.1093/stmcls/sxad080) PMID: [37933895](https://pubmed.ncbi.nlm.nih.gov/37933895/)

4. Guo L et al. (2025). *Targeting to miR-130b-5p/TLR4: How sodium danshensu suppresses inflammatory response of microglia in cerebral ischemia-reperfusion injury.* Int Immunopharmacol. DOI: [10.1016/j.intimp.2025.114497](https://doi.org/10.1016/j.intimp.2025.114497) PMID: [40121745](https://pubmed.ncbi.nlm.nih.gov/40121745/)

5. Yang X et al. (2024). *Physical exercise-induced circAnks1b upregulation promotes protective endoplasmic reticulum stress and suppresses apoptosis via miR-130b-5p/Pak2 signaling in an ischemic stroke model.* CNS Neurosci Ther. DOI: [10.1111/cns.70055](https://doi.org/10.1111/cns.70055) PMID: [39328024](https://pubmed.ncbi.nlm.nih.gov/39328024/)

---

## miR-5107-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +6.29 | 3.22e-09 | 269.7 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UGGGCAGAGGAGGCAGGGACA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

For the mechanism study, dual-luciferase reporter, fluorescence in situ hybridization (FISH), RNA immunoprecipitation (RIP), RNA pull-down, gene editing, and CUT & Tag were performed in vitro to confirm that circSV2b directly sponged miR-5107-5p and alleviated the suppression of the expression of... (PMID: 35973363) Taken together, these findings suggested that the miR-5107-5p-Foxk1-Akt1 axis might serve as a key target of circSV2b overexpression in PD treatment, and highlighted the significant change of circSV2b in serum exosomes. (PMID: 35973363) Mechanistically, miR-5107-5p, significantly enriched in EPO-EVs, is delivered to mBMSCs, where it suppresses epidermal growth factor receptor (EGFR) expression and alleviates EGFR's inhibitory effect on RhoA. (PMID: 40289904)

### Literature

1. Cheng Q et al. (2022). *CircSV2b participates in oxidative stress regulation through miR-5107-5p-Foxk1-Akt1 axis in Parkinson's disease.* Redox Biol. DOI: [10.1016/j.redox.2022.102430](https://doi.org/10.1016/j.redox.2022.102430) PMID: [35973363](https://pubmed.ncbi.nlm.nih.gov/35973363/)

2. Liu S et al. (2025). *Erythropoietin-Stimulated Macrophage-Derived Extracellular Vesicles in Chitosan Hydrogel Rescue BMSCs Fate by Targeting EGFR to Alleviate Inflammatory Bone Loss in Periodontitis.* Adv Sci (Weinh). DOI: [10.1002/advs.202500554](https://doi.org/10.1002/advs.202500554) PMID: [40289904](https://pubmed.ncbi.nlm.nih.gov/40289904/)

3. Wang Y et al. (2017). *Differentially expressed miRNAs in oxygen‑induced retinopathy newborn mouse models.* Mol Med Rep. DOI: [10.3892/mmr.2016.5993](https://doi.org/10.3892/mmr.2016.5993) PMID: [27922698](https://pubmed.ncbi.nlm.nih.gov/27922698/)

4. Zhang Y et al. (2018). *Effects of Icariin on Atherosclerosis and Predicted Function Regulatory Network in ApoE Deficient Mice.* Biomed Res Int. DOI: [10.1155/2018/9424186](https://doi.org/10.1155/2018/9424186) PMID: [30533443](https://pubmed.ncbi.nlm.nih.gov/30533443/)

---

## miR-150-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Upregulated | +4.44 | 2.41e-12 | 234.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-150-5p** - **100% identical** (22 nt)

Sequence: `UCUCCCAACCCUUGUACCAGUG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 326**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Myb | 2 | -0.752 |
| Smr3a | 1 | -0.721 |
| Gm7714 | 1 | -0.655 |
| Prorsd1 | 1 | -0.637 |
| Shisa4 | 1 | -0.614 |
| Cxcl1 | 1 | -0.532 |
| Myh1 | 1 | -0.52 |
| Pdia3 | 1 | -0.507 |
| Hilpda | 1 | -0.471 |
| Them4 | 1 | -0.468 |

**Top target gene: Myb** (Myb proto-oncogene, transcription factor)

*Function:* Enables DNA-binding transcription activator activity, RNA polymerase II-specific; RNA polymerase II cis-regulatory region sequence-specific DNA binding activity; and WD40-repeat domain binding activity. Involved in positive regulation of transcription by RNA polymerase II. Acts upstream of or within several processes, including cellular response to cytokine stimulus; hematopoietic or lymphoid organ development; and hemopoiesis. Located in cytosol and nucleus. Part of RNA polymerase II transcript...

*NCBI Gene ID:* [17863](https://www.ncbi.nlm.nih.gov/gene/17863)

### Biological Function Summary

We show that miR-328a-3p and miR-150-5p, enriched in the sEVs after TBI, promote osteogenesis by directly targeting the 3'UTR of FOXO4 or CBL, respectively, and hydrogel carrying miR-328a-3p-containing sEVs efficiently repaires bone defects in rats. (PMID: 34654817) Mechanistically, the 3D-Exos promoted the proliferation of cornea-derived cells and reduced the release of inflammatory factors via miR-150-5p targeting of the PDCD4 gene. (PMID: 39955036) Interestingly, miR-150-5p was downregulated, whereas E2F3 and BIRC5 (survivin), a cell cycle activator and an antiapoptotic regulator, respectively, were upregulated. (PMID: 40203244) Increasing miR-150-5p in PBL-1 cells induced G1 cell cycle arrest, suppressed proliferation by transcriptionally repressing E2F3, and promoted apoptosis by the downregulation of BIRC5. (PMID: 40203244) Interestingly, the miR-150-5p tumor suppressor activity was diminished in E2F3-knockdown cells. (PMID: 40203244)

### Literature

1. Xia W et al. (2021). *Damaged brain accelerates bone healing by releasing small extracellular vesicles that target osteoprogenitors.* Nat Commun. DOI: [10.1038/s41467-021-26302-y](https://doi.org/10.1038/s41467-021-26302-y) PMID: [34654817](https://pubmed.ncbi.nlm.nih.gov/34654817/)

2. Xu Y et al. (2025). *3D mesenchymal stem cell exosome-functionalized hydrogels for corneal wound healing.* J Control Release. DOI: [10.1016/j.jconrel.2025.02.030](https://doi.org/10.1016/j.jconrel.2025.02.030) PMID: [39955036](https://pubmed.ncbi.nlm.nih.gov/39955036/)

3. Verdú-Bou M et al. (2025). *The role of miR-150-5p/E2F3/survivin axis in the pathogenesis of plasmablastic lymphoma and its therapeutic potential.* Blood Adv. DOI: [10.1182/bloodadvances.2025016180](https://doi.org/10.1182/bloodadvances.2025016180) PMID: [40203244](https://pubmed.ncbi.nlm.nih.gov/40203244/)

4. Jiang H et al. (2024). *Effective delivery of miR-150-5p with nucleus pulposus cell-specific nanoparticles attenuates intervertebral disc degeneration.* J Nanobiotechnology. DOI: [10.1186/s12951-024-02561-x](https://doi.org/10.1186/s12951-024-02561-x) PMID: [38802882](https://pubmed.ncbi.nlm.nih.gov/38802882/)

5. D'Agostino DM et al. (2022). *MiR-150 in HTLV-1 infection and T-cell transformation.* Front Immunol. DOI: [10.3389/fimmu.2022.974088](https://doi.org/10.3389/fimmu.2022.974088) PMID: [36072598](https://pubmed.ncbi.nlm.nih.gov/36072598/)

---

## miR-23b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -1.85 | 1.62e-18 | 11.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-23b-3p** - **91.3% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-23b-3p) | `AUCACAUUGCCAGGGAUUACC` | 21 nt |
| Human (hsa-miR-23b-3p) | `AUCACAUUGCCAGGGAUUACCAC` | 23 nt |

```
Mouse: AUCACAUUGCCAGGGAUUACC
       |||||||||||||||||||||--
Human: AUCACAUUGCCAGGGAUUACCAC
```
(`|` = match, `X` = mismatch, `-` = length difference)

Length difference: 2 nt

*Seed region (positions 2-8) is conserved between species, indicating shared target gene regulation.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 133**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Mab21l2 | 1 | -0.703 |
| Rab39b | 2 | -0.672 |
| Rras2 | 1 | -0.624 |
| Auh | 2 | -0.573 |
| Tox3 | 2 | -0.542 |
| Chst10 | 1 | -0.527 |
| Cav2 | 1 | -0.521 |
| Clec1a | 2 | -0.519 |
| Rbm25 | 1 | -0.509 |
| Uqcrfs1 | 1 | -0.498 |

**Top target gene: Mab21l2** (mab-21-like 2)

*Function:* Acts upstream of or within camera-type eye development; embryonic body morphogenesis; and positive regulation of cell population proliferation. Located in nucleus. Is expressed in several structures, including branchial arch; central nervous system; embryo mesenchyme; limb; and sensory organ. Human ortholog(s) of this gene implicated in coloboma and syndromic microphthalmia 14. Orthologous to human MAB21L2 (mab-21 like 2). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [23937](https://www.ncbi.nlm.nih.gov/gene/23937)

### Biological Function Summary

The miR-23b-3p in extracellular vesicles promotes cartilage catabolism and inhibits anabolism by targeting OTUD4, disrupting mitophagy in chondrocytes. (PMID: 40399261) Inhibiting miR-23b-3p in osteocytes or chondrocytes reduces cartilage degeneration and osteoarthritis progression in male mice. (PMID: 40399261) Together, our findings highlight that osteocyte-derived extracellular vesicles mediate communication with chondrocytes and suggest miR-23b-3p as a potential therapeutic target for osteoarthritis. (PMID: 40399261) Concerning miRNA biomarkers, miRNA-24, miR-23b-3p, miR-195-3p, miR-29c, and mir-331-5p are promising across studies. (PMID: 38791346) The anti-inflammatory role of miR-23b-3p (miR-23b) is known in autoimmune diseases like multiple sclerosis, systemic lupus erythematosus, and rheumatoid arthritis. (PMID: 39870316)

### Literature

1. Liu N et al. (2025). *Osteocyte-derived extracellular vesicles mediate the bone-to-cartilage crosstalk and promote osteoarthritis progression.* Nat Commun. DOI: [10.1038/s41467-025-59861-5](https://doi.org/10.1038/s41467-025-59861-5) PMID: [40399261](https://pubmed.ncbi.nlm.nih.gov/40399261/)

2. Kim KY et al. (2024). *Potential Exosome Biomarkers for Parkinson's Disease Diagnosis: A Systematic Review and Meta-Analysis.* Int J Mol Sci. DOI: [10.3390/ijms25105307](https://doi.org/10.3390/ijms25105307) PMID: [38791346](https://pubmed.ncbi.nlm.nih.gov/38791346/)

3. Lin J et al. (2025). *Mannose-modified exosomes loaded with MiR-23b-3p target alveolar macrophages to alleviate acute lung injury in Sepsis.* J Control Release. DOI: [10.1016/j.jconrel.2025.01.073](https://doi.org/10.1016/j.jconrel.2025.01.073) PMID: [39870316](https://pubmed.ncbi.nlm.nih.gov/39870316/)

4. Pelisenco IA et al. (2024). *miR-23b-3p, miR-126-3p and GAS5 delivered by extracellular vesicles inhibit breast cancer xenografts in zebrafish.* Cell Commun Signal. DOI: [10.1186/s12964-024-01936-9](https://doi.org/10.1186/s12964-024-01936-9) PMID: [39558342](https://pubmed.ncbi.nlm.nih.gov/39558342/)

5. Zhang J et al. (2025). *tRNA Fragments in Diabetes Mellitus.* Clin Chim Acta. DOI: [10.1016/j.cca.2025.120405](https://doi.org/10.1016/j.cca.2025.120405) PMID: [40449709](https://pubmed.ncbi.nlm.nih.gov/40449709/)

---

## miR-27b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -1.28 | 1.56e-18 | 11.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-27b-3p** - **100% identical** (21 nt)

Sequence: `UUCACAGUGGCUAAGUUCUGC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 123**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Trim23 | 2 | -1.134 |
| Pparg | 1 | -0.741 |
| Phb | 1 | -0.606 |
| Ehf | 3 | -0.591 |
| Slitrk1 | 1 | -0.572 |
| Wisp1 | 1 | -0.546 |
| Usp42 | 2 | -0.54 |
| Ubxn2a | 1 | -0.525 |
| Atl3 | 1 | -0.52 |
| Prrg3 | 1 | -0.507 |

**Top target gene: Trim23** (tripartite motif-containing 23)

*Function:* Predicted to enable several functions, including GTPase activity; guanyl ribonucleotide binding activity; and identical protein binding activity. Predicted to be involved in several processes, including intracellular protein transport; positive regulation of metabolic process; and protein ubiquitination. Located in cytoplasm and nucleus. Is expressed in ureter. Orthologous to human TRIM23 (tripartite motif containing 23). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [81003](https://www.ncbi.nlm.nih.gov/gene/81003)

### Biological Function Summary

Mechanically, RNA-sequencing and fluorescence in situ hybridization (FISH) indicated that miR-27b-3p was enriched in MSC-ex and exosomal miR-27b-3p repressed Yes-associated protein (YAP) expression by targeting its 3' untranslated region in LX-2. (PMID: 37328872) Additionally, the miR-27b-3p inhibitor abrogated the anti-LOXL2 abilities of MSC-ex and diminished the antifibrotic efficacy. (PMID: 37328872) miR-27b-3p overexpression promoted MSC-ex mediated YAP/LOXL2 inhibition. (PMID: 37328872) Thus, MSC-ex may suppress LOXL2 expression through exosomal miR-27b-3p mediated YAP down-regulation. (PMID: 37328872) Importantly, exosomal miR-27b-3p efficiently enters into the vascular endothelial cells and activates the NF-κB pathway by downregulating PPARα. (PMID: 36640325)

### Literature

1. Cheng F et al. (2023). *Mesenchymal stem cell-derived exosomal miR-27b-3p alleviates liver fibrosis via downregulating YAP/LOXL2 pathway.* J Nanobiotechnology. DOI: [10.1186/s12951-023-01942-y](https://doi.org/10.1186/s12951-023-01942-y) PMID: [37328872](https://pubmed.ncbi.nlm.nih.gov/37328872/)

2. Tang Y et al. (2023). *Exosomal miR-27b-3p secreted by visceral adipocytes contributes to endothelial inflammation and atherogenesis.* Cell Rep. DOI: [10.1016/j.celrep.2022.111948](https://doi.org/10.1016/j.celrep.2022.111948) PMID: [36640325](https://pubmed.ncbi.nlm.nih.gov/36640325/)

3. Lee CW et al. (2025). *Ginkgolide B increases healthspan and lifespan of female mice.* Nat Aging. DOI: [10.1038/s43587-024-00802-0](https://doi.org/10.1038/s43587-024-00802-0) PMID: [39890935](https://pubmed.ncbi.nlm.nih.gov/39890935/)

4. Castaño C et al. (2018). *Obesity-associated exosomal miRNAs modulate glucose and lipid metabolism in mice.* Proc Natl Acad Sci U S A. DOI: [10.1073/pnas.1808855115](https://doi.org/10.1073/pnas.1808855115) PMID: [30429322](https://pubmed.ncbi.nlm.nih.gov/30429322/)

5. Feng Z et al. (2021). *Epithelium- and endothelium-derived exosomes regulate the alveolar macrophages by targeting RGS1 mediated calcium signaling-dependent immune response.* Cell Death Differ. DOI: [10.1038/s41418-021-00750-x](https://doi.org/10.1038/s41418-021-00750-x) PMID: [33753901](https://pubmed.ncbi.nlm.nih.gov/33753901/)

---

## miR-30c-2-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -2.98 | 1.06e-21 | 11.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-30c-2-3p** - **100% identical** (22 nt)

Sequence: `CUGGGAGAAGGCUGUUUACUCU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

Circulating miR-30c-2-3p has been closely related to vascular diseases, however, its role and underlying mechanisms in ischemic stroke remained unclear. (PMID: 39511683) Further investigation revealed that these exosomal miR-30c-2-3p primarily originated from macrophages within atherosclerotic plaques, exacerbating ischemic stroke by targeting microglia. (PMID: 39511683) Exosomes enriched with miR-30c-2-3p increased microglial inflammatory properties in vivo and aggravated neuroinflammation by inhibiting SMAD2. (PMID: 39511683) miR-324-5p and miR-30c-2-3p expression are increased under hypertonicity in KC3AC1 cells. (PMID: 35563683) Overexpression of miR-324-5p and miR-30c-2-3p alter MR expression and signaling in KC3AC1 cells with blunted responses in terms of aldosterone-regulated genes expression. (PMID: 35563683)

### Literature

1. Tang Y et al. (2024). *Macrophage exosomal miR-30c-2-3p in atherosclerotic plaques aggravates microglial neuroinflammation during large-artery atherosclerotic stroke via TGF-β/SMAD2 pathway.* J Neuroinflammation. DOI: [10.1186/s12974-024-03281-7](https://doi.org/10.1186/s12974-024-03281-7) PMID: [39511683](https://pubmed.ncbi.nlm.nih.gov/39511683/)

2. Vu TA et al. (2022). *miR-324-5p and miR-30c-2-3p Alter Renal Mineralocorticoid Receptor Signaling under Hypertonicity.* Cells. DOI: [10.3390/cells11091377](https://doi.org/10.3390/cells11091377) PMID: [35563683](https://pubmed.ncbi.nlm.nih.gov/35563683/)

3. Huang X et al. (2023). *miR-30c-2-3p suppresses the proliferation of human renal cell carcinoma cells by targeting TOP2A.* Asian Biomed (Res Rev News). DOI: [10.2478/abm-2023-0052](https://doi.org/10.2478/abm-2023-0052) PMID: [37818158](https://pubmed.ncbi.nlm.nih.gov/37818158/)

4. Zheng L et al. (2022). *MicroRNA-30c-2-3p represses malignant progression of gastric adenocarcinoma cells via targeting ARHGAP11A.* Bioengineered. DOI: [10.1080/21655979.2022.2090222](https://doi.org/10.1080/21655979.2022.2090222) PMID: [35754342](https://pubmed.ncbi.nlm.nih.gov/35754342/)

5. Mitsueda R et al. (2023). *Oncogenic Targets Regulated by Tumor-Suppressive miR-30c-1-3p and miR-30c-2-3p: TRIP13 Facilitates Cancer Cell Aggressiveness in Breast Cancer.* Cancers (Basel). DOI: [10.3390/cancers15164189](https://doi.org/10.3390/cancers15164189) PMID: [37627217](https://pubmed.ncbi.nlm.nih.gov/37627217/)

---

## miR-30a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -3.34 | 1.58e-20 | 9.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-30a-5p** - **100% identical** (22 nt)

Sequence: `UGUAAACAUCCUCGACUGGAAG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 325**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Srsf7 | 1 | -0.628 |
| Rab4b | 1 | -0.553 |
| Slc7a10 | 1 | -0.529 |
| Cysltr1 | 1 | -0.528 |
| Cthrc1 | 1 | -0.505 |
| Runx2 | 2 | -0.461 |
| A930009A15Rik | 1 | -0.461 |
| Rqcd1 | 2 | -0.459 |
| Ccdc71l | 1 | -0.429 |
| Mical1 | 1 | -0.423 |

**Top target gene: Srsf7** (serine and arginine-rich splicing factor 7)

*Function:* The protein encoded by this gene is a member of the serine/arginine (SR)-rich family of pre-mRNA splicing factors, which constitute part of the spliceosome. Each of these factors contains an RNA recognition motif (RRM) for binding RNA and an RS domain for binding other proteins. The RS domain is rich in serine and arginine residues and facilitates interaction between different SR splicing factors. In addition to being critical for mRNA splicing, the SR proteins have also been shown to be involve...

*NCBI Gene ID:* [225027](https://www.ncbi.nlm.nih.gov/gene/225027)

### Biological Function Summary

This study aimed to characterize the role and mechanism of action of miR-30a-5p in cardiac senescence. (PMID: 39511427) miR-30a-5p was downregulated in aged mouse hearts and neonatal rat cardiomyocytes (NRCMs). (PMID: 39511427) In vivo, using a combination of echocardiography and different molecular biological approaches, we investigated the role of miR-30a-5p knockout or overexpression in natural- or D-galactose-induced heart aging in mice. (PMID: 39511427) In vitro, using RNA sequencing and a series of molecular biology methods, the mechanism by which miR-30a-5p regulates cardiac senescence was explored in cardiomyocytes. (PMID: 39511427) miR-30a-5p knockout mice showed aggravated natural- or D-galactose-induced heart aging compared to wild-type littermate mice, with significantly decreased heart function, an increased number of γH2AX-positive cells, reduced telomere length, and upregulated p21 and p53 expression. (PMID: 39511427)

### Literature

1. Hong YX et al. (2024). *SUMOylation of TP53INP1 is involved in miR-30a-5p-regulated heart senescence.* Exp Mol Med. DOI: [10.1038/s12276-024-01347-3](https://doi.org/10.1038/s12276-024-01347-3) PMID: [39511427](https://pubmed.ncbi.nlm.nih.gov/39511427/)

2. Li T et al. (2025). *Nondigestible stachyose binds membranous HSP90β on small intestinal epithelium to regulate the exosomal miRNAs: A new function and mechanism.* Cell Metab. DOI: [10.1016/j.cmet.2024.10.012](https://doi.org/10.1016/j.cmet.2024.10.012) PMID: [39561765](https://pubmed.ncbi.nlm.nih.gov/39561765/)

3. Tsai HC et al. (2025). *Acrolein Induces the Exosomal miR-30a-5p/NCAM1 Axis Promoting Glioma Progression.* Mol Cancer Ther. DOI: [10.1158/1535-7163.MCT-25-0117](https://doi.org/10.1158/1535-7163.MCT-25-0117) PMID: [40512746](https://pubmed.ncbi.nlm.nih.gov/40512746/)

4. Ryu G et al. (2021). *Epithelial-to-mesenchymal transition in neutrophilic chronic rhinosinusitis.* Curr Opin Allergy Clin Immunol. DOI: [10.1097/ACI.0000000000000701](https://doi.org/10.1097/ACI.0000000000000701) PMID: [33284158](https://pubmed.ncbi.nlm.nih.gov/33284158/)

5. Huang Q et al. (2024). *Bushenhuoluo Decoction improves polycystic ovary syndrome by regulating exosomal miR-30a-5p/ SOCS3/mTOR/NLRP3 signaling-mediated autophagy and pyroptosis.* J Ovarian Res. DOI: [10.1186/s13048-024-01355-x](https://doi.org/10.1186/s13048-024-01355-x) PMID: [38302986](https://pubmed.ncbi.nlm.nih.gov/38302986/)

---

## miR-30a-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -2.97 | 4.46e-16 | 8.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-30a-3p** - **100% identical** (22 nt)

Sequence: `CUUUCAGUCGGAUGUUUGCAGC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-30a-3p shares seed family 'GUAAACA' with miR-30e-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 1359**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Mkrn3 | 3 | -0.827 |
| Pip4k2a | 3 | -0.752 |
| Foxg1 | 2 | -0.716 |
| Lhx8 | 2 | -0.71 |
| Klhl28 | 3 | -0.689 |
| Yod1 | 3 | -0.67 |
| Cth | 1 | -0.645 |
| Bnip3l | 2 | -0.642 |
| Cyp24a1 | 1 | -0.636 |
| Tmem170b | 2 | -0.632 |

**Top target gene: Mkrn3** (makorin, ring finger protein, 3)

*Function:* Predicted to enable identical protein binding activity and ubiquitin protein ligase activity. Predicted to be involved in protein ubiquitination. Predicted to be located in nucleus. Is expressed in gut; nervous system; and sensory organ. Used to study central precocious puberty 2. Human ortholog(s) of this gene implicated in central precocious puberty 2. Orthologous to human MKRN3 (makorin ring finger protein 3). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [22652](https://www.ncbi.nlm.nih.gov/gene/22652)

### Biological Function Summary

The miRNA deep sequencing results showed that miR-30a-3p was enriched in sEVs from steatotic hepatocytes. (PMID: 37678722) miR-30a-3p directly targeted the 3' untranslated region of ABCA1 to inhibit ABCA1 expression and cholesterol efflux. (PMID: 37678722) Moreover, serum sEVs from patients with NAFLD and sEV-miR-30a-3p expression were associated with decreased cholesterol efflux levels in foam cells. (PMID: 37678722) CONCLUSION: Steatotic hepatocyte-derived sEVs promote foam cell formation and facilitate atherogenesis via the miR-30a-3p/ABCA1 axis. (PMID: 37678722) Reducing sEV secretion by steatotic hepatocytes or targeting miR-30a-3p may be potential therapeutic approaches to slow the progression of NAFLD-driven atherosclerosis. (PMID: 37678722)

### Literature

1. Chen X et al. (2023). *Hepatic steatosis aggravates atherosclerosis via small extracellular vesicle-mediated inhibition of cellular cholesterol efflux.* J Hepatol. DOI: [10.1016/j.jhep.2023.08.023](https://doi.org/10.1016/j.jhep.2023.08.023) PMID: [37678722](https://pubmed.ncbi.nlm.nih.gov/37678722/)

2. Tang YF et al. (2024). *circ_PPAPDC1A promotes Osimertinib resistance by sponging the miR-30a-3p/ IGF1R pathway in non-small cell lung cancer (NSCLC).* Mol Cancer. DOI: [10.1186/s12943-024-01998-w](https://doi.org/10.1186/s12943-024-01998-w) PMID: [38715012](https://pubmed.ncbi.nlm.nih.gov/38715012/)

3. Liu S et al. (2025). *Inhalable Hsa-miR-30a-3p Liposomes Attenuate Pulmonary Fibrosis.* Adv Sci (Weinh). DOI: [10.1002/advs.202405434](https://doi.org/10.1002/advs.202405434) PMID: [40119620](https://pubmed.ncbi.nlm.nih.gov/40119620/)

4. Liu S et al. (2023). *Breast adipose tissue-derived extracellular vesicles from obese women alter tumor cell metabolism.* EMBO Rep. DOI: [10.15252/embr.202357339](https://doi.org/10.15252/embr.202357339) PMID: [37929643](https://pubmed.ncbi.nlm.nih.gov/37929643/)

5. Mitsueda R et al. (2024). *Identification of Tumor-Suppressive miR-30a-3p Controlled Genes: ANLN as a Therapeutic Target in Breast Cancer.* Noncoding RNA. DOI: [10.3390/ncrna10060060](https://doi.org/10.3390/ncrna10060060) PMID: [39728605](https://pubmed.ncbi.nlm.nih.gov/39728605/)

---

## miR-30c-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -2.93 | 8.32e-10 | 4.9 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-30c-5p** - **100% identical** (23 nt)

Sequence: `UGUAAACAUCCUACACUCUCAGC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 22**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Yod1 | 3 | -0.67 |
| R3hdm1 | 1 | -0.463 |
| Wipf1 | 1 | -0.45 |
| Ppp4r4 | 1 | -0.4 |
| Hoxb8 | 1 | -0.352 |
| Polr3g | 2 | -0.326 |
| Fkbp3 | 1 | -0.314 |
| Calcr | 1 | -0.306 |
| Pank3 | 1 | -0.274 |
| Mttp | 1 | -0.264 |

**Top target gene: Yod1** (YOD1 deubiquitinase)

*Function:* Predicted to enable K48-linked deubiquitinase activity; cysteine-type deubiquitinase activity; and ubiquitin protein ligase binding activity. Predicted to be involved in several processes, including ERAD pathway; negative regulation of retrograde protein transport, ER to cytosol; and protein deubiquitination. Predicted to be located in cytoplasm. Is expressed in several structures, including adrenal gland; alimentary system; brain; genitourinary system; and respiratory system. Orthologous to hum...

*NCBI Gene ID:* [226418](https://www.ncbi.nlm.nih.gov/gene/226418)

### Biological Function Summary

The downstream signaling pathways of S1PR1 was detected to clarify the specific pathways to regulates miR-30c-5p. (PMID: 39551792) S1PR1 inhibits the expression of FOXA1 through p-STAT1/miR-30c-5p, thereby suppressing the malignant function of LUAD cells. (PMID: 39551792) S1PR1 regulates the malignant function of LUAD cells by inhibiting the expression of COL5A1, MMP1 and SERPINE1 through the p-STAT1/miR-30c-5p/FOXA1 signaling pathway. (PMID: 39551792) Only three studies have explored the therapeutic potential of sEV-miRNAs in vivo in mice-two looked into the role of sEV-hsa-miR-214-3p in decreasing fibrosis, and one investigated sEV-hsa-miR-30c-5p in suppressing the invasive and migratory potential of endometriotic lesions. (PMID: 37877421) Specifically, miR-125b-5p/miR-30c-5p and miR-23a-3p inhibit the expression of smad2 and smad3 by targeting their 3'-untranslated regions, resulting in the downregulation of the transforming growth factor-β (TGF-β)/smad signaling pathway and the reversal of fibrosis. (PMID: 38241636)

### Literature

1. Chai Y et al. (2024). *S1PR1 suppresses lung adenocarcinoma progression through p-STAT1/miR-30c-5 p/FOXA1 pathway.* J Exp Clin Cancer Res. DOI: [10.1186/s13046-024-03230-5](https://doi.org/10.1186/s13046-024-03230-5) PMID: [39551792](https://pubmed.ncbi.nlm.nih.gov/39551792/)

2. Nazri HM et al. (2023). *The role of small extracellular vesicle-miRNAs in endometriosis.* Hum Reprod. DOI: [10.1093/humrep/dead216](https://doi.org/10.1093/humrep/dead216) PMID: [37877421](https://pubmed.ncbi.nlm.nih.gov/37877421/)

3. Liu H et al. (2024). *Mesenchymal Stem Cell Derived Exosomes Repair Uterine Injury by Targeting Transforming Growth Factor-β Signaling.* ACS Nano. DOI: [10.1021/acsnano.3c10884](https://doi.org/10.1021/acsnano.3c10884) PMID: [38241636](https://pubmed.ncbi.nlm.nih.gov/38241636/)

4. Rodrigues AC et al. (2024). *Extracellular vesicle-encapsulated miR-30c-5p reduces aging-related liver fibrosis.* Aging Cell. DOI: [10.1111/acel.14310](https://doi.org/10.1111/acel.14310) PMID: [39269881](https://pubmed.ncbi.nlm.nih.gov/39269881/)

5. Yu P et al. (2023). *Downregulation of apoptotic repressor AVEN exacerbates cardiac injury after myocardial infarction.* Proc Natl Acad Sci U S A. DOI: [10.1073/pnas.2302482120](https://doi.org/10.1073/pnas.2302482120) PMID: [37816050](https://pubmed.ncbi.nlm.nih.gov/37816050/)

---

## miR-30b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -2.27 | 3.65e-08 | 4.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-30b-5p** - **100% identical** (22 nt)

Sequence: `UGUAAACAUCCUACACUCAGCU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 403**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Mkrn3 | 3 | -0.827 |
| Pip4k2a | 3 | -0.752 |
| Lhx8 | 2 | -0.71 |
| Tnrc6a | 4 | -0.627 |
| Lin28b | 3 | -0.62 |
| Josd1 | 2 | -0.609 |
| Actc1 | 1 | -0.598 |
| Eed | 1 | -0.571 |
| Nap1l5 | 2 | -0.55 |
| Larp1b | 1 | -0.527 |

**Top target gene: Mkrn3** (makorin, ring finger protein, 3)

*Function:* Predicted to enable identical protein binding activity and ubiquitin protein ligase activity. Predicted to be involved in protein ubiquitination. Predicted to be located in nucleus. Is expressed in gut; nervous system; and sensory organ. Used to study central precocious puberty 2. Human ortholog(s) of this gene implicated in central precocious puberty 2. Orthologous to human MKRN3 (makorin ring finger protein 3). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [22652](https://www.ncbi.nlm.nih.gov/gene/22652)

### Biological Function Summary

Mechanistically, AVEN 3' UTR lengthening provides additional binding sites for miR-30b-5p and miR-30c-5p, thus reducing AVEN expression. (PMID: 37816050) The results demonstrated that plasma EVs showed widespread deregulation of specific miRNAs (miR-106a-5p, miR-16-5p, miR-17-5p, miR-195-5p, miR-19b-3p, miR-20a-5p, miR-223-3p, miR-25-3p, miR-296-5p, miR-30b-5p, miR-532-3p, miR-92a-3p, and miR-451a), some of which were already known to be associate... (PMID: 37834197) We selected 13 miRNAs with altered expressions in testis tissue (hsa-miR-122-5p, hsa-miR-145-5p, hsa-miR-16-5p, hsa-miR-193a-3p, hsa-miR-19a-3p, hsa-miR-23a-3p, hsa-miR-30b-5p, hsa-miR-34b-5p, hsa-miR-34c-5p, hsa-miR-374b-5p, hsa-miR-449a, hsa-miR-574-3p and hsa-miR-92a-3p), and systematically ex... (PMID: 35760398) This study was to identify the function of the miR-30b-5p/BCL6 axis in osteogenic differentiation of hBMSCs. (PMID: 35100079) Realtime-quantitative PCR (RT-qPCR) and Western blotting were used to measure the relative expression of ALP, OCN, RUNX2, miR-30b-5p, and BCL6 during osteogenic differentiation of hBMSCs. (PMID: 35100079)

### Literature

1. Yu P et al. (2023). *Downregulation of apoptotic repressor AVEN exacerbates cardiac injury after myocardial infarction.* Proc Natl Acad Sci U S A. DOI: [10.1073/pnas.2302482120](https://doi.org/10.1073/pnas.2302482120) PMID: [37816050](https://pubmed.ncbi.nlm.nih.gov/37816050/)

2. Visconte C et al. (2023). *Altered Extracellular Vesicle miRNA Profile in Prodromal Alzheimer's Disease.* Int J Mol Sci. DOI: [10.3390/ijms241914749](https://doi.org/10.3390/ijms241914749) PMID: [37834197](https://pubmed.ncbi.nlm.nih.gov/37834197/)

3. Burgos CF et al. (2022). *MicroRNA expression in male infertility.* Reprod Fertil Dev. DOI: [10.1071/RD21131](https://doi.org/10.1071/RD21131) PMID: [35760398](https://pubmed.ncbi.nlm.nih.gov/35760398/)

4. Luo Y et al. (2022). *miR-30b-5p inhibits osteoblast differentiation through targeting BCL6.* Cell Cycle. DOI: [10.1080/15384101.2022.2031428](https://doi.org/10.1080/15384101.2022.2031428) PMID: [35100079](https://pubmed.ncbi.nlm.nih.gov/35100079/)

5. Liu B et al. (2025). *MiR-30b-5p ameliorates experimental autoimmune uveitis by inhibiting the Atg5/Atg12/Becn1 Axis.* Int Immunopharmacol. DOI: [10.1016/j.intimp.2025.114370](https://doi.org/10.1016/j.intimp.2025.114370) PMID: [40020463](https://pubmed.ncbi.nlm.nih.gov/40020463/)

---

## miR-335-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -2.39 | 7.21e-08 | 4.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-335-5p** - **100% identical** (23 nt)

Sequence: `UCAAGAGCAAUAACGAAAAAUGU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 254**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Hand1 | 1 | -0.643 |
| A330008L17Rik | 1 | -0.544 |
| Mpc1 | 1 | -0.538 |
| Prss46 | 1 | -0.532 |
| Tmem184c | 1 | -0.531 |
| Rprm | 1 | -0.518 |
| Ubl4 | 1 | -0.508 |
| Hoxd12 | 1 | -0.496 |
| Fam107b | 1 | -0.484 |
| Kcnj4 | 1 | -0.467 |

**Top target gene: Hand1** (heart and neural crest derivatives expressed 1)

*Function:* Enables several functions, including DNA-binding transcription activator activity, RNA polymerase II-specific; bHLH transcription factor binding activity; and protein homodimerization activity. Involved in negative regulation of transcription by RNA polymerase II and positive regulation of transcription by RNA polymerase II. Acts upstream of or within several processes, including circulatory system development; negative regulation of DNA-binding transcription factor activity; and trophoblast gia...

*NCBI Gene ID:* [15110](https://www.ncbi.nlm.nih.gov/gene/15110)

### Biological Function Summary

Retraction: "Upregulated expression of ROCK1 promotes cell proliferation by functioning as a target of miR-335-5p in non-small cell lung cancer," by Haicheng Tang, Wenwen Du, Yongqian Jiang, Hongmiao Li, Hongjian Bo, and Shu Song. (PMID: 34957558) Interestingly, 4 miRNAs (miR-335-5p, miR-17-5p, miR-486-5p and miR-484) were significantly upregulated in ARMS samples compared to ERMS. (PMID: 39385294) In the validation analysis performed in a larger group of patients only three miRNAs (miR-483-5p, miR-335-5p and miR-484) were differentially significantly expressed in RMS patients compared to HC. (PMID: 39385294) MiR-335-5p was upregulated in RMS tumor tissues respect to normal tissues (p = 0.00202) and upregulated significantly between ARMS and ERMS (p = 0.04). (PMID: 39385294) By performing in situ hybridization, we observed that miR-335-5p signal was exclusively in the cytoplasm of cancer cells. (PMID: 39385294)

### Literature

1. Unknown (2022). *Retraction.* J Cell Physiol. DOI: [10.1002/jcp.30674](https://doi.org/10.1002/jcp.30674) PMID: [34957558](https://pubmed.ncbi.nlm.nih.gov/34957558/)

2. Bridgewood C et al. (2022). *T Helper 2 IL-4/IL-13 Dual Blockade with Dupilumab Is Linked to Some Emergent T Helper 17‒Type Diseases, Including Seronegative Arthritis and Enthesitis/Enthesopathy, but Not to Humoral Autoimmune Diseases.* J Invest Dermatol. DOI: [10.1016/j.jid.2022.03.013](https://doi.org/10.1016/j.jid.2022.03.013) PMID: [35395222](https://pubmed.ncbi.nlm.nih.gov/35395222/)

3. Di Paolo V et al. (2024). *Plasma-derived extracellular vesicles miR-335-5p as potential diagnostic biomarkers for fusion-positive rhabdomyosarcoma.* J Exp Clin Cancer Res. DOI: [10.1186/s13046-024-03197-3](https://doi.org/10.1186/s13046-024-03197-3) PMID: [39385294](https://pubmed.ncbi.nlm.nih.gov/39385294/)

4. Tao T et al. (2025). *Elevated Hsa-miR-335-5p impairs trophoblast function and fetal growth in preeclampsia.* Cell Signal. DOI: [10.1016/j.cellsig.2025.111911](https://doi.org/10.1016/j.cellsig.2025.111911) PMID: [40447128](https://pubmed.ncbi.nlm.nih.gov/40447128/)

5. Zhang S et al. (2023). *Role and mechanism of miR-335-5p in the pathogenesis and treatment of polycystic ovary syndrome.* Transl Res. DOI: [10.1016/j.trsl.2022.07.007](https://doi.org/10.1016/j.trsl.2022.07.007) PMID: [35931409](https://pubmed.ncbi.nlm.nih.gov/35931409/)

---

## miR-99a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -1.91 | 2.52e-05 | 3.2 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-99a-5p** - **100% identical** (22 nt)

Sequence: `AACCCGUAGAUCCGAUCUUGUG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 17**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Ap1ar | 1 | -0.796 |
| Hs3st2 | 1 | -0.761 |
| Fgfr3 | 1 | -0.576 |
| Epdr1 | 1 | -0.47 |
| Hoxa1 | 1 | -0.461 |
| Seh1l | 1 | -0.367 |
| Ppp3ca | 1 | -0.364 |
| Raver2 | 1 | -0.348 |
| Mtmr3 | 1 | -0.331 |
| Mbnl1 | 1 | -0.316 |

**Top target gene: Ap1ar** (adaptor-related protein complex 1 associated regulatory protein)

*Function:* Predicted to enable AP-1 adaptor complex binding activity; Arp2/3 complex binding activity; and kinesin binding activity. Acts upstream of or within several processes, including negative regulation of cell motility; negative regulation of substrate adhesion-dependent cell spreading; and regulation of Arp2/3 complex-mediated actin nucleation. Located in endosome. Is expressed in several structures, including cardiovascular system; genitourinary system; gut; integumental system; and nervous system...

*NCBI Gene ID:* [211556](https://www.ncbi.nlm.nih.gov/gene/211556)

### Biological Function Summary

Mechanistically, EV-packaged miR-99a-5p (EV-miR-99a) specifically targeted NLRP2 mRNA in fibroblasts and activated the proinflammatory NFκB signaling pathway, thereby converting normal fibroblasts into cancer-associated fibroblasts (CAF). (PMID: 40991395) Among the downstream miRNAs we identified, miR-99a-5p was found to be downregulated in breast cancer tissue. (PMID: 40264026) Inhibition of miR-99a-5p partially reversed the effects of FOXO1 overexpression on cell proliferation and apoptosis. (PMID: 40264026) E2F7, a target mRNA of miR-99a-5p, showed a negative correlation with FOXO1 expression in breast cancer mRNAs we screened. (PMID: 40264026) Silencing E2F7 partially mitigated the inhibitory effects of miR-99a-5p on proliferation and apoptosis in FOXO1-overexpressing cells. (PMID: 40264026)

### Literature

1. Zhou M et al. (2026). *Extracellular Vesicle-Packaged miR-99a Reprograms Fibroblasts to Create an Inflammatory Niche That Drives Colorectal Cancer Metastasis.* Cancer Res. DOI: [10.1158/0008-5472.CAN-25-0663](https://doi.org/10.1158/0008-5472.CAN-25-0663) PMID: [40991395](https://pubmed.ncbi.nlm.nih.gov/40991395/)

2. Zhang Y et al. (2025). *FOXO1 mediates miR-99a-5p/E2F7 to restrain breast cancer cell proliferation and induce apoptosis.* BMC Cancer. DOI: [10.1186/s12885-025-14111-1](https://doi.org/10.1186/s12885-025-14111-1) PMID: [40264026](https://pubmed.ncbi.nlm.nih.gov/40264026/)

3. Xiao Y et al. (2022). *Macrophage-derived extracellular vesicles regulate follicular activation and improve ovarian function in old mice by modulating local environment.* Clin Transl Med. DOI: [10.1002/ctm2.1071](https://doi.org/10.1002/ctm2.1071) PMID: [36229897](https://pubmed.ncbi.nlm.nih.gov/36229897/)

4. Hao X et al. (2024). *Mesenchymal Stem Cell-Exosomal miR-99a Attenuate Silica-Induced Lung Fibrosis by Inhibiting Pulmonary Fibroblast Transdifferentiation.* Int J Mol Sci. DOI: [10.3390/ijms252312626](https://doi.org/10.3390/ijms252312626) PMID: [39684337](https://pubmed.ncbi.nlm.nih.gov/39684337/)

5. LE Y et al. (2019). *[Expression and Function of miR-99a-5p in Bone Marrow of Patients with MDS].* Zhongguo Shi Yan Xue Ye Xue Za Zhi. DOI: [10.7534/j.issn.1009-2137.2019.01.022](https://doi.org/10.7534/j.issn.1009-2137.2019.01.022) PMID: [30738460](https://pubmed.ncbi.nlm.nih.gov/30738460/)

---

## let-7b-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Spleen | Downregulated | -1.74 | 3.16e-06 | 3.1 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-let-7b-3p** - **100% identical** (22 nt)

Sequence: `CUAUACAACCUACUGCCUUCCC`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: let-7b-3p shares seed family 'GAGGUAG' with let-7d-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 1076**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Hmga2 | 7 | -2.59 |
| Nr6a1 | 4 | -2.08 |
| Trim71 | 6 | -1.782 |
| Arid3b | 3 | -1.518 |
| Lin28b | 5 | -1.342 |
| Fign | 6 | -1.228 |
| Vstm5 | 2 | -1.225 |
| Arid3a | 3 | -1.174 |
| Fignl2 | 3 | -1.128 |
| Adrb3 | 2 | -1.072 |

**Top target gene: Hmga2** (high mobility group AT-hook 2)

*Function:* Enables minor groove of adenine-thymine-rich DNA binding activity. Involved in several processes, including negative regulation of cellular senescence; positive regulation of angiogenesis; and positive regulation of cell proliferation in bone marrow. Acts upstream of or within several processes, including endocrine system development; lung development; and positive regulation of cell population proliferation. Located in male germ cell nucleus and nuclear chromosome. Is expressed in several struc...

*NCBI Gene ID:* [15364](https://www.ncbi.nlm.nih.gov/gene/15364)

### Biological Function Summary

Some overexpressed miRNAs (mmu-let-7f-1-3p, mmu-let-7a-1-3p, mmu-let-7b-3p, mmu-let-7b-5p, mmu-miR-330-3p) regulate genes encoding for protein involved in biological, homeostatic, biosynthetic and small molecule metabolic processes, embryo development and cell differentiation, all phenomena relev... (PMID: 37419964) RESULTS: Our quantitative reverse transcription PCR results revealed that let-7b-3p was significantly overexpressed in brain tissues of the methamphetamine-user group. (PMID: 37075366) CONCLUSION: We have shown for the first time in the literature the differential expression of let-7b-3p in samples from methamphetamine-addicted individuals. (PMID: 37075366) Our results showed that differentially expressed let-7b-3p in methamphetamine users could be used as a diagnostic and therapeutic marker. (PMID: 37075366) Additionally, validated hsa-miR-6826-5p, hsa-let-7b-3p, hsa-miR-7846, and hsa-miR-451a emerged as promising miRNAs that are deregulated with aging and should be further investigated. (PMID: 39684581)

### Literature

1. Fiorani F et al. (2023). *Ceramide releases exosomes with a specific miRNA signature for cell differentiation.* Sci Rep. DOI: [10.1038/s41598-023-38011-1](https://doi.org/10.1038/s41598-023-38011-1) PMID: [37419964](https://pubmed.ncbi.nlm.nih.gov/37419964/)

2. Demirel G et al. (2023). *Evaluation of microRNA let-7b-3p expression levels in methamphetamine abuse.* Rev Assoc Med Bras (1992). DOI: [10.1590/1806-9282.20221391](https://doi.org/10.1590/1806-9282.20221391) PMID: [37075366](https://pubmed.ncbi.nlm.nih.gov/37075366/)

3. Alberro A et al. (2024). *Age-Related sncRNAs in Human Hippocampal Tissue Samples: Focusing on Deregulated miRNAs.* Int J Mol Sci. DOI: [10.3390/ijms252312872](https://doi.org/10.3390/ijms252312872) PMID: [39684581](https://pubmed.ncbi.nlm.nih.gov/39684581/)

4. Li Y et al. (2021). *Let-7b-3p inhibits tumor growth and metastasis by targeting the BRF2-mediated MAPK/ERK pathway in human lung adenocarcinoma.* Transl Lung Cancer Res. DOI: [10.21037/tlcr-21-299](https://doi.org/10.21037/tlcr-21-299) PMID: [34012797](https://pubmed.ncbi.nlm.nih.gov/34012797/)

5. Florian IA et al. (2021). *An Insight into the microRNAs Associated with Arteriovenous and Cavernous Malformations of the Brain.* Cells. DOI: [10.3390/cells10061373](https://doi.org/10.3390/cells10061373) PMID: [34199498](https://pubmed.ncbi.nlm.nih.gov/34199498/)

---

## miR-125b-1-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +7.15 | 3.94e-41 | 1495.3 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-125b-1-3p** - **100% identical** (22 nt)

Sequence: `ACGGGUUAGGCUCUUGGGAGCU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

miR-125b-1-3p overexpression significantly reduced atherosclerotic plaque development in mice; it also led to decreased lipid uptake and deposition in VSMCs, enhanced autophagy, and suppression of smooth muscle cell phenotypic changes in-vitro. (PMID: 38471617) An interaction between miR-125b-1-3p and the RRAGD/mTOR/ULK1 pathway was revealed, elucidating its role in promoting autophagy. (PMID: 38471617) Therefore, miR-125b-1-3p plays a pivotal role in enhancing autophagic processes, inhibiting foam cell formation in VSMCs and mitigating atherosclerosis progression, partly through RRAGD/mTOR/ULK1 signaling axis modulation. (PMID: 38471617) Thus, miR-125b-1-3p is a promising target for preventive and therapeutic strategies for atherosclerosis. (PMID: 38471617) The expressions of miR-30b-3p and miR-125b-1-3p were determined by quantitative real-time PCR. (PMID: 35931990)

### Literature

1. Chen X et al. (2024). *microRNA-125b-1-3p mediates autophagy via the RRAGD/mTOR/ULK1 signaling pathway and mitigates atherosclerosis progression.* Cell Signal. DOI: [10.1016/j.cellsig.2024.111136](https://doi.org/10.1016/j.cellsig.2024.111136) PMID: [38471617](https://pubmed.ncbi.nlm.nih.gov/38471617/)

2. Zhu J et al. (2022). *The expression and clinical significance of miR-30b-3p and miR-125b-1-3p in patients with periodontitis.* BMC Oral Health. DOI: [10.1186/s12903-022-02360-6](https://doi.org/10.1186/s12903-022-02360-6) PMID: [35931990](https://pubmed.ncbi.nlm.nih.gov/35931990/)

3. Lu S et al. (2024). *MiR-125b-1-3p-mediated UQCRB inhibition facilitates mitochondrial metabolism disorders in a rat cellular senescencemodel.* Mol Cell Probes. DOI: [10.1016/j.mcp.2024.101979](https://doi.org/10.1016/j.mcp.2024.101979) PMID: [39117291](https://pubmed.ncbi.nlm.nih.gov/39117291/)

4. Szabó MR et al. (2020). *Hypercholesterolemia Interferes with Induction of miR-125b-1-3p in Preconditioned Hearts.* Int J Mol Sci. DOI: [10.3390/ijms21113744](https://doi.org/10.3390/ijms21113744) PMID: [32466450](https://pubmed.ncbi.nlm.nih.gov/32466450/)

5. Zhang X et al. (2018). *MiR-125b-1-3p Exerts Antitumor Functions in Lung Carcinoma Cells by Targeting S1PR1.* Chin Med J (Engl). DOI: [10.4103/0366-6999.238135](https://doi.org/10.4103/0366-6999.238135) PMID: [30082521](https://pubmed.ncbi.nlm.nih.gov/30082521/)

---

## miR-1190

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +8.35 | 7.35e-10 | 378.0 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UCAGCUGAGGUUCCCCUCUGUC`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-694

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +4.18 | 2.70e-19 | 321.5 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CUGAAAAUGUUGCCUGAAG`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

miR-mRNA integrated analysis revealed that miR-694 was downregulated while its target gene tumor necrosis factor α-induced protein 3 (Tnfaip3) was upregulated, as confirmed by qPCR. (PMID: 25333455) Herein, we first report that Lass2 deficiency caused the downregulation of miR-694 and the upregulation of its target gene Tnfaip3 in vivo in mice, which may be related to a high risk of occurrence of HCC. (PMID: 25333455) Using miRXplore microarrays containing 634 mouse miRNAs in combination with quantitative RT-PCR, the liver is found to respond to primary infections with an upregulation of the three miRNA species miR-26b, MCMV-miR-M23-1-5p, and miR-1274a, and a downregulation of the 16 miRNA species miR-101b, le... (PMID: 21085987) Three miRNAs (miR-310-3p, miR-92, and miR-127) were found to be up-regulated and four miRNAs (miR-92d-3p, miR-375-5p, miR-146-3p, and miR-694) were found to be down-regulated in the S. (PMID: 28219342)

### Literature

1. Lu X et al. (2014). *Knockout of the HCC suppressor gene Lass2 downregulates the expression level of miR-694.* Oncol Rep. DOI: [10.3892/or.2014.3527](https://doi.org/10.3892/or.2014.3527) PMID: [25333455](https://pubmed.ncbi.nlm.nih.gov/25333455/)

2. Delić D et al. (2011). *Hepatic miRNA expression reprogrammed by Plasmodium chabaudi malaria.* Parasitol Res. DOI: [10.1007/s00436-010-2152-z](https://doi.org/10.1007/s00436-010-2152-z) PMID: [21085987](https://pubmed.ncbi.nlm.nih.gov/21085987/)

3. Qiang J et al. (2017). *Effects of exposure to Streptococcus iniae on microRNA expression in the head kidney of genetically improved farmed tilapia (Oreochromis niloticus).* BMC Genomics. DOI: [10.1186/s12864-017-3591-z](https://doi.org/10.1186/s12864-017-3591-z) PMID: [28219342](https://pubmed.ncbi.nlm.nih.gov/28219342/)

---

## miR-1187

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +5.82 | 3.52e-11 | 289.1 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UAUGUGUGUGUGUAUGUGUGUAA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

This study aimed to investigate the role and regulation mechanism of miR-1187 during the development of DN and podocyte injury. (PMID: 37208852) The content of miR-1187 in podocytes was up-regulated under high glucose (HG) treatment and increased in kidney tissue of db/db mice (DN model mice) compared with control db/m mice. (PMID: 37208852) The administration of miR-1187 inhibitor could decrease podocyte apoptosis induced by HG and attenuate the decline in renal function and reduce proteinuria as well as glomerular apoptosis in db/db mice. (PMID: 37208852) Mechanistically, miR-1187 could inhibit the autophagy level in HG-exposed podocytes and glomerulus of DN mice. (PMID: 37208852) Moreover, miR-1187 inhibitor could reduce HG-stimulated podocyte injury and autophagy flux inhibition. (PMID: 37208852)

### Literature

1. Chen B et al. (2023). *miR-1187 induces podocyte injury and diabetic nephropathy through autophagy.* Diab Vasc Dis Res. DOI: [10.1177/14791641231172139](https://doi.org/10.1177/14791641231172139) PMID: [37208852](https://pubmed.ncbi.nlm.nih.gov/37208852/)

2. Qin L et al. (2025). *Low-Intensity Pulsed Ultrasound Promotes Osteogenesis in Porous Titanium Alloys Through miR-1187/BMP4 Pathway.* FASEB J. DOI: [10.1096/fj.202403395RR](https://doi.org/10.1096/fj.202403395RR) PMID: [40317956](https://pubmed.ncbi.nlm.nih.gov/40317956/)

3. Günay N et al. (2023). *Male- and female-specific microRNA expression patterns in a mouse model of methanol poisoning.* Food Chem Toxicol. DOI: [10.1016/j.fct.2023.113666](https://doi.org/10.1016/j.fct.2023.113666) PMID: [36780935](https://pubmed.ncbi.nlm.nih.gov/36780935/)

4. John AA et al. (2018). *Identification of novel microRNA inhibiting actin cytoskeletal rearrangement thereby suppressing osteoblast differentiation.* J Mol Med (Berl). DOI: [10.1007/s00109-018-1624-y](https://doi.org/10.1007/s00109-018-1624-y) PMID: [29523914](https://pubmed.ncbi.nlm.nih.gov/29523914/)

5. Yu DS et al. (2012). *The regulatory role of microRNA-1187 in TNF-α-mediated hepatocyte apoptosis in acute liver failure.* Int J Mol Med. DOI: [10.3892/ijmm.2012.888](https://doi.org/10.3892/ijmm.2012.888) PMID: [22266786](https://pubmed.ncbi.nlm.nih.gov/22266786/)

---

## miR-182-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +5.86 | 2.34e-10 | 274.8 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-182-3p** - **23.8% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-182-3p) | `GUGGUUCUAGACUUGCCAACU` | 21 nt |
| Human (hsa-miR-182-3p) | `UGGUUCUAGACUUGCCAACUA` | 21 nt |

```
Mouse: GUGGUUCUAGACUUGCCAACU
       XX|X|XXXXXXX|XX|X|XXX
Human: UGGUUCUAGACUUGCCAACUA
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: G (mouse) -> U (human) *(in seed region)*
- Position 2: U (mouse) -> G (human) *(in seed region)*
- Position 4: G (mouse) -> U (human) *(in seed region)*
- Position 6: U (mouse) -> C (human) *(in seed region)*
- Position 7: C (mouse) -> U (human) *(in seed region)*
- Position 8: U (mouse) -> A (human) *(in seed region)*
- Position 9: A (mouse) -> G (human)
- Position 10: G (mouse) -> A (human)
- Position 11: A (mouse) -> C (human)
- Position 12: C (mouse) -> U (human)
- Position 14: U (mouse) -> G (human)
- Position 15: G (mouse) -> C (human)
- Position 17: C (mouse) -> A (human)
- Position 19: A (mouse) -> C (human)
- Position 20: C (mouse) -> U (human)
- Position 21: U (mouse) -> A (human)

*WARNING: 6 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-182-3p shares seed family 'UUGGCAA' with miR-182-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 1130**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Palld | 1 | -0.877 |
| Satb2 | 2 | -0.828 |
| Wfdc9 | 1 | -0.823 |
| Arf4 | 2 | -0.812 |
| Bcl2l12 | 1 | -0.805 |
| Tmem145 | 2 | -0.779 |
| Prrg3 | 2 | -0.755 |
| Vamp3 | 3 | -0.744 |
| Frs2 | 3 | -0.739 |
| Cacna2d1 | 1 | -0.725 |

**Top target gene: Palld** (palladin, cytoskeletal associated protein)

*Function:* Predicted to enable axon guidance receptor activity and cytoskeletal protein binding activity. Acts upstream of or within actin cytoskeleton organization; epithelial cell morphogenesis; and keratinocyte development. Located in Z disc; focal adhesion; and stress fiber. Is expressed in several structures, including alimentary system; embryo mesenchyme; genitourinary system; heart; and hemolymphoid system gland. Human ortholog(s) of this gene implicated in pancreatic cancer. Orthologous to human PA...

*NCBI Gene ID:* [72333](https://www.ncbi.nlm.nih.gov/gene/72333)

### Biological Function Summary

The following miRNAs have been identified as potential biomarkers for preterm birth and gestational diabetes mellitus: miR-197-3p and miR-520h, miR-1323, miR-342-3p, miR-132-3p, miR-182-3p, miR-517-3p, miR-222-3p, miR-16-5p and miR-126-3p. (PMID: 39596014) By performing a high-throughput luciferase screening of 54 candidate miRNAs, we identified miR-182-3p as a specific and efficient post-transcriptional regulator of TRF2. (PMID: 36426578) Ectopic expression of miR-182-3p drastically reduced TRF2 protein levels in a panel of telomerase- or alternative lengthening of telomeres (ALT)-positive cancer cell lines. (PMID: 36426578) Moreover, miR-182-3p induced DNA damage at telomeric and pericentromeric sites, eventually leading to strong apoptosis activation. (PMID: 36426578) We also observed that treatment with lipid nanoparticles (LNPs) containing miR-182-3p impaired tumor growth in triple-negative breast cancer (TNBC) models, including patient-derived tumor xenografts (PDTXs), without affecting mouse survival or tissue function. (PMID: 36426578)

### Literature

1. Popova AK et al. (2024). *Extracellular Vesicles as Biomarkers of Pregnancy Complications.* Int J Mol Sci. DOI: [10.3390/ijms252211944](https://doi.org/10.3390/ijms252211944) PMID: [39596014](https://pubmed.ncbi.nlm.nih.gov/39596014/)

2. Dinami R et al. (2023). *MiR-182-3p targets TRF2 and impairs tumor growth of triple-negative breast cancer.* EMBO Mol Med. DOI: [10.15252/emmm.202216033](https://doi.org/10.15252/emmm.202216033) PMID: [36426578](https://pubmed.ncbi.nlm.nih.gov/36426578/)

3. Zheng HC et al. (2022). *The roles of the tumor suppressor parafibromin in cancer.* Front Cell Dev Biol. DOI: [10.3389/fcell.2022.1006400](https://doi.org/10.3389/fcell.2022.1006400) PMID: [36211470](https://pubmed.ncbi.nlm.nih.gov/36211470/)

4. Rao J et al. (2022). *Inhibiting miR-182-3p Alleviates Gestational Diabetes Mellitus by Improving Insulin Resistance in Skeletal Muscle.* Balkan Med J. DOI: [10.4274/balkanmedj.galenos.2021.2021-8-140](https://doi.org/10.4274/balkanmedj.galenos.2021.2021-8-140) PMID: [35330559](https://pubmed.ncbi.nlm.nih.gov/35330559/)

5. Sun L et al. (2020). *miR-182-3p/Myadm contribute to pulmonary artery hypertension vascular remodeling via a KLF4/p21-dependent mechanism.* Theranostics. DOI: [10.7150/thno.44687](https://doi.org/10.7150/thno.44687) PMID: [32373233](https://pubmed.ncbi.nlm.nih.gov/32373233/)

---

## miR-181d-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +3.98 | 2.01e-13 | 205.6 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-181d-3p** - **38.1% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-181d-3p) | `CCCACCGGGGGAUGAAUGUCA` | 21 nt |
| Human (hsa-miR-181d-3p) | `CCACCGGGGGAUGAAUGUCAC` | 21 nt |

```
Mouse: CCCACCGGGGGAUGAAUGUCA
       ||XX|X||||XXXX|XXXXXX
Human: CCACCGGGGGAUGAAUGUCAC
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 3: C (mouse) -> A (human) *(in seed region)*
- Position 4: A (mouse) -> C (human) *(in seed region)*
- Position 6: C (mouse) -> G (human) *(in seed region)*
- Position 11: G (mouse) -> A (human)
- Position 12: A (mouse) -> U (human)
- Position 13: U (mouse) -> G (human)
- Position 14: G (mouse) -> A (human)
- Position 16: A (mouse) -> U (human)
- Position 17: U (mouse) -> G (human)
- Position 18: G (mouse) -> U (human)
- Position 19: U (mouse) -> C (human)
- Position 20: C (mouse) -> A (human)
- Position 21: A (mouse) -> C (human)

*WARNING: 3 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-181d-3p shares seed family 'ACAUUCA' with miR-181a-5p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 1119**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Zfp97 | 3 | -10.423 |
| Zfp960 | 2 | -10.366 |
| Gm14420 | 3 | -7.855 |
| Gm6710 | 1 | -7.048 |
| 9830147E19Rik | 4 | -5.727 |
| Gm14431 | 4 | -5.532 |
| Gm14295 | 1 | -5.5 |
| 2410141K09Rik | 3 | -5.028 |
| Zfp850 | 1 | -4.499 |
| Gm14440 | 7 | -4.111 |

**Top target gene: Zfp97** (zinc finger protein 97)

*Function:* Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Located in nucleus. Is expressed in central nervous system and genitourinary system. [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [22759](https://www.ncbi.nlm.nih.gov/gene/22759)

### Biological Function Summary

ADAM12 and miR-181d-3p expressions in OSCC cells with Circ_0046336 knockdown were quantified. (PMID: 40760847) Circ_0046336 targeted miR-181d-3p and miR-181d-3p targeted ADAM12 in OSCC cells. (PMID: 40760847) Circ_0046336 silencing facilitated apoptosis, and suppressed viability, migration and invasion of OSCC cells, while upregulating miR-181d-3p and downregulating ADAM12. (PMID: 40760847) MiR-181d-3p deficiency reversed the regulatory role of Circ_0046336 in biological behaviors of OSCC cells. (PMID: 40760847) Circ_0046336 silencing promoted E-cadherin expression and inhibited N-cadherin and Vimentin expressions, but such effects were reversed by miR-181d-3p downregulation.ConclusionCirc_0046336 acts as a ceRNA to regulate apoptosis, migration, invasion and EMT of OSCC cells via miR-181d-3p/ADAM12 axis. (PMID: 40760847)

### Literature

1. Chen YY et al. (2018). *Upregulation of miR-125b, miR-181d, and miR-221 Predicts Poor Prognosis in MGMT Promoter-Unmethylated Glioblastoma Patients.* Am J Clin Pathol. DOI: [10.1093/ajcp/aqy008](https://doi.org/10.1093/ajcp/aqy008) PMID: [29538610](https://pubmed.ncbi.nlm.nih.gov/29538610/)

2. Chen J et al. (2025). *A new target for the treatment of oral squamous cell carcinoma: Circ_0046336.* Technol Health Care. DOI: [10.1177/09287329251363708](https://doi.org/10.1177/09287329251363708) PMID: [40760847](https://pubmed.ncbi.nlm.nih.gov/40760847/)

3. Zeng M et al. (2023). *Circular RNA transcriptome across multiple tissues reveal skeletal muscle-specific circPSME4 regulating myogenesis.* Int J Biol Macromol. DOI: [10.1016/j.ijbiomac.2023.126322](https://doi.org/10.1016/j.ijbiomac.2023.126322) PMID: [37591436](https://pubmed.ncbi.nlm.nih.gov/37591436/)

4. Kalmaz M et al. (2025). *Decoding the Potential Impact of Plasma hsa-miR-24-3p and hsa-miR-181 d-3p Expression, Plasma IFN-γ Levels, and IFNG rs2069727 T/C Genetic Variant on Multiple Sclerosis Risk and Glatiramer Acetate Treatment.* Mol Neurobiol. DOI: [10.1007/s12035-025-05027-9](https://doi.org/10.1007/s12035-025-05027-9) PMID: [40457027](https://pubmed.ncbi.nlm.nih.gov/40457027/)

---

## miR-466f-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +4.46 | 6.60e-11 | 202.2 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CAUACACACACACAUACACAC`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

Among enriched miRNA cargo in exosomes, miR-466f-3p was primarily responsible for the protective effects via inhibition of AKT/GSK3β pathway. (PMID: 35392967) Our mechanistic study further demonstrated that c-MET was the direct target of miR-466f-3p, whose restoration partially abrogated mMSCs-Exo-mediated inhibition in both EMT process and AKT/GSK3β signaling activity induced by radiation. (PMID: 35392967) CONCLUSIONS: Our findings indicated that exosomal miR-466f-3p derived from mMSCs may possess anti-fibrotic properties and prevent radiation-induced EMT through inhibition of AKT/GSK3β via c-MET, providing a promising therapeutic modality for radiation-induced lung fibrosis. (PMID: 35392967) In vitro, western blotting, transmission electron microscopy (TEM), immunofluorescence (IF) staining and qPCR were performed to verify the biological functions of NEAT1, miR-466f-3p and HK2. (PMID: 36169673) Additionally, rescue assays were conducted on osteoblasts to clarify the regulatory network of the NEAT1/miR-466f-3p/HK2 signalling pathway. (PMID: 36169673)

### Literature

1. Li Y et al. (2022). *Mouse mesenchymal stem cell-derived exosomal miR-466f-3p reverses EMT process through inhibiting AKT/GSK3β pathway via c-MET in radiation-induced lung injury.* J Exp Clin Cancer Res. DOI: [10.1186/s13046-022-02351-z](https://doi.org/10.1186/s13046-022-02351-z) PMID: [35392967](https://pubmed.ncbi.nlm.nih.gov/35392967/)

2. Zhao X et al. (2022). *A novel ceRNA regulatory network involving the long noncoding NEAT1, miRNA-466f-3p and its mRNA target in osteoblast autophagy and osteoporosis.* J Mol Med (Berl). DOI: [10.1007/s00109-022-02255-7](https://doi.org/10.1007/s00109-022-02255-7) PMID: [36169673](https://pubmed.ncbi.nlm.nih.gov/36169673/)

3. Besharat ZM et al. (2018). *Low Expression of miR-466f-3p Sustains Epithelial to Mesenchymal Transition in Sonic Hedgehog Medulloblastoma Stem Cells Through Vegfa-Nrp2 Signaling Pathway.* Front Pharmacol. DOI: [10.3389/fphar.2018.01281](https://doi.org/10.3389/fphar.2018.01281) PMID: [30483126](https://pubmed.ncbi.nlm.nih.gov/30483126/)

4. Sterling KM (2011). *The procollagen type III, alpha 1 (COL3A1) gene first intron expresses poly-A+ RNA corresponding to multiple ESTs and putative miRNAs.* J Cell Biochem. DOI: [10.1002/jcb.22944](https://doi.org/10.1002/jcb.22944) PMID: [21268075](https://pubmed.ncbi.nlm.nih.gov/21268075/)

5. Wang IF et al. (2021). *Activation of a hippocampal CREB-pCREB-miRNA-MEF2 axis modulates individual variation of spatial learning and memory capability.* Cell Rep. DOI: [10.1016/j.celrep.2021.109477](https://doi.org/10.1016/j.celrep.2021.109477) PMID: [34348143](https://pubmed.ncbi.nlm.nih.gov/34348143/)

---

## miR-466m-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +4.66 | 3.19e-10 | 198.7 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UACAUACACACAUACACACGCA`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

Further results showed that Hsp4 positively regulated the expression of miR-466m-3p. (PMID: 32976821) Knockdown of miR-466m-3p reversed LPS-induced cell apoptosis via increasing the levels of DNAjb6 which was confirmed to be the target gene of miR-466m-3p. (PMID: 32976821)

### Literature

1. Ji Q et al. (2020). *Long non-coding RNA Hsp4 alleviates lipopolysaccharide-induced apoptosis of lung epithelial cells via miRNA-466m-3p/DNAjb6 axis.* Exp Mol Pathol. DOI: [10.1016/j.yexmp.2020.104547](https://doi.org/10.1016/j.yexmp.2020.104547) PMID: [32976821](https://pubmed.ncbi.nlm.nih.gov/32976821/)

---

## miR-669p-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +4.54 | 1.68e-09 | 176.2 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `CAUAACAUACACACACACACGUAU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-669k-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Upregulated | +5.70 | 1.11e-06 | 149.1 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UGUGCAUGUGUGUAUAGUUGUGUGC`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-140-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -1.95 | 1.35e-11 | 6.4 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-140-5p** - **100% identical** (22 nt)

Sequence: `CAGUGGUUUUACCCUAUGGUAG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 330**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Msmp | 1 | -0.787 |
| Fgf9 | 1 | -0.753 |
| Tssk2 | 1 | -0.705 |
| Wnt9a | 2 | -0.691 |
| Katnbl1 | 1 | -0.68 |
| Zfp800 | 2 | -0.604 |
| Slc16a6 | 1 | -0.598 |
| Egr2 | 1 | -0.585 |
| Klf9 | 2 | -0.57 |
| Epb4.1l2 | 1 | -0.55 |

**Top target gene: Msmp** (microseminoprotein, prostate associated)

*Function:* Predicted to enable CCR2 chemokine receptor binding activity. Predicted to be involved in lymphocyte chemotaxis and monocyte chemotaxis. Predicted to be active in cytoplasm and extracellular space. Is expressed in femur; humerus; radius; tibia; and ulna. Orthologous to human MSMP (microseminoprotein, prostate associated). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [100039672](https://www.ncbi.nlm.nih.gov/gene/100039672)

### Biological Function Summary

Interestingly, the presence of long non-coding RNAs (lncRNAs) as well as microRNAs (miRNAs), such as PlncRNA-1, miR-22-3p, miR-526b, LncRNA NKILA, miR-140-5p and miR-214, which are implicated in the pathogenesis of SA-AKI, may also serve as potential therapeutic targets. (PMID: 38541160) Exosomes derived from miR-140-5p-overexpressing synovial mesenchymal stem cells (SMSC-140s) may be effective in treating OA. (PMID: 28042326) Highly-expressed miR-140-5p blocked this side-effect via RalA. (PMID: 28042326) PURPOSE: To assess the effect of exosomes derived from human urine-derived stem cells (hUSCs) overexpressing miR-140-5p (miR means microRNA) on KOA in an in vitro interleukin 1β (IL-1β)-induced osteoarthritis (OA) model and an in vivo rat KOA model. (PMID: 35179989) CONCLUSION: Our results demonstrated the superiority of hUSC-Exos overexpressing miR-140-5p for treating OA compared with the hUSC-Exos. (PMID: 35179989)

### Literature

1. Kounatidis D et al. (2024). *Sepsis-Associated Acute Kidney Injury: Where Are We Now?* Medicina (Kaunas). DOI: [10.3390/medicina60030434](https://doi.org/10.3390/medicina60030434) PMID: [38541160](https://pubmed.ncbi.nlm.nih.gov/38541160/)

2. Tao SC et al. (2017). *Exosomes derived from miR-140-5p-overexpressing human synovial mesenchymal stem cells enhance cartilage tissue regeneration and prevent osteoarthritis of the knee in a rat model.* Theranostics. DOI: [10.7150/thno.17133](https://doi.org/10.7150/thno.17133) PMID: [28042326](https://pubmed.ncbi.nlm.nih.gov/28042326/)

3. Liu Y et al. (2022). *Exosomes Derived From Human Urine-Derived Stem Cells Overexpressing miR-140-5p Alleviate Knee Osteoarthritis Through Downregulation of VEGFA in a Rat Model.* Am J Sports Med. DOI: [10.1177/03635465221073991](https://doi.org/10.1177/03635465221073991) PMID: [35179989](https://pubmed.ncbi.nlm.nih.gov/35179989/)

4. Gregorius J et al. (2021). *Small extracellular vesicles obtained from hypoxic mesenchymal stromal cells have unique characteristics that promote cerebral angiogenesis, brain remodeling and neurological recovery after focal cerebral ischemia in mice.* Basic Res Cardiol. DOI: [10.1007/s00395-021-00881-9](https://doi.org/10.1007/s00395-021-00881-9) PMID: [34105014](https://pubmed.ncbi.nlm.nih.gov/34105014/)

5. Toury L et al. (2022). *miR-140-5p and miR-140-3p: Key Actors in Aging-Related Diseases?* Int J Mol Sci. DOI: [10.3390/ijms231911439](https://doi.org/10.3390/ijms231911439) PMID: [36232738](https://pubmed.ncbi.nlm.nih.gov/36232738/)

---

## miR-3068-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -1.55 | 3.49e-10 | 5.7 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UUGGAGUUCAUGCAAGUUCUAACC`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

Surprisingly, miR-3068-5p was upregulated following overexpression of Ago2 and downregulated by silencing Ago2 in the NAc. (PMID: 34483916) These findings demonstrated that dysregulated Ago2 in neurons in the NAc is capable of regulating METH sensitization and suggested a potential role of Ago2-dependent miR-3068-5p in METH sensitization. (PMID: 34483916) Overexpression of Gm28309 or inhibition of miR-3068-5p repressed p65 phosphorylation and reduced NLRP3 inflammasome and IL-1β and IL-18 secretion. (PMID: 33414782) Mechanistically, Gm28309 acted as a ceRNA of miR-3068-5p to activate NF-κB pathway by targeting κB-Ras2, an inhibitor of NF-κB signaling. (PMID: 33414782) Moreover, the number of intracellular Brucella was higher when Gm28309 was overexpressed or when miR-3068-5p or p65 was inhibited. (PMID: 33414782)

### Literature

1. Liu D et al. (2021). *Potential Ago2/miR-3068-5p Cascades in the Nucleus Accumbens Contribute to Methamphetamine-Induced Locomotor Sensitization of Mice.* Front Pharmacol. DOI: [10.3389/fphar.2021.708034](https://doi.org/10.3389/fphar.2021.708034) PMID: [34483916](https://pubmed.ncbi.nlm.nih.gov/34483916/)

2. Deng X et al. (2020). *Brucella-Induced Downregulation of lncRNA Gm28309 Triggers Macrophages Inflammatory Response Through the miR-3068-5p/NF-κB Pathway.* Front Immunol. DOI: [10.3389/fimmu.2020.581517](https://doi.org/10.3389/fimmu.2020.581517) PMID: [33414782](https://pubmed.ncbi.nlm.nih.gov/33414782/)

3. Deng X et al. (2021). *Corrigendum: Brucella-Induced Downregulation of lncRNA Gm28309 Triggers Macrophages Inflammatory Response Through the miR-3068-5p/NF-κB Pathway.* Front Immunol. DOI: [10.3389/fimmu.2021.805275](https://doi.org/10.3389/fimmu.2021.805275) PMID: [34966394](https://pubmed.ncbi.nlm.nih.gov/34966394/)

4. Zhang L et al. (2023). *Gypenosides suppress fibrosis of the renal NRK-49F cells by targeting miR-378a-5p through the PI3K/AKT signaling pathway.* J Ethnopharmacol. DOI: [10.1016/j.jep.2023.116466](https://doi.org/10.1016/j.jep.2023.116466) PMID: [37031821](https://pubmed.ncbi.nlm.nih.gov/37031821/)

---

## miR-191-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -2.05 | 2.79e-10 | 5.5 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-191-5p** - **100% identical** (23 nt)

Sequence: `CAACGGAAUCCCAAAAGCAGCUG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 69**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Chmp5 | 1 | -0.811 |
| Tmod2 | 1 | -0.679 |
| Taf5 | 1 | -0.623 |
| Plcd1 | 1 | -0.621 |
| Zcchc14 | 1 | -0.506 |
| Neurl4 | 1 | -0.483 |
| Map3k12 | 1 | -0.461 |
| Cebpb | 1 | -0.46 |
| Tjp1 | 1 | -0.428 |
| Mapre3 | 1 | -0.424 |

**Top target gene: Chmp5** (charged multivesicular body protein 5)

*Function:* Acts upstream of or within several processes, including endosome to lysosome transport; erythrocyte differentiation; and regulation of receptor recycling. Located in nucleus. Is expressed in telencephalon. Orthologous to human CHMP5 (charged multivesicular body protein 5). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [76959](https://www.ncbi.nlm.nih.gov/gene/76959)

### Biological Function Summary

The lack of DNMT2/TRDMT1 gene in DOX-treated four cancer cell lines resulted in decreased levels of four microRNAs, namely, miR-23a-3p, miR-93-5p, miR-125a-5p and miR-191-5p involved in the regulation of several pathways such as ubiquitin-mediated proteolysis, amino acid degradation and translati... (PMID: 36273376) MiR-191-5p has been proven to have high expression in breast cancer (BC), while its biological role and potential regulatory mechanisms in BC remain an open issue. (PMID: 37545272) OBJECTIVE: Bioinformatics was utilized to assay miR-191-5p level in BC tissues and predict its downstream target gene as well as the enriched signaling pathways of the target gene. (PMID: 37545272) RESULTS: Upregulated miR-191-5p expression and downregulated KLF6 expression were observed in BC cells. (PMID: 37545272) There was a targeting relationship between miR-191-5p and KLF6. (PMID: 37545272)

### Literature

1. Adamczyk-Grochala J et al. (2023). *DNMT2/TRDMT1 gene knockout compromises doxorubicin-induced unfolded protein response and sensitizes cancer cells to ER stress-induced apoptosis.* Apoptosis. DOI: [10.1007/s10495-022-01779-0](https://doi.org/10.1007/s10495-022-01779-0) PMID: [36273376](https://pubmed.ncbi.nlm.nih.gov/36273376/)

2. Pan L et al. (2023). *MiR-191-5p inhibits KLF6 to promote epithelial-mesenchymal transition in breast cancer.* Technol Health Care. DOI: [10.3233/THC-230217](https://doi.org/10.3233/THC-230217) PMID: [37545272](https://pubmed.ncbi.nlm.nih.gov/37545272/)

3. Singh A et al. (2026). *20 years of miR-191 research- tracing footsteps and road to its clinical utility in cancer.* Biochim Biophys Acta Rev Cancer. DOI: [10.1016/j.bbcan.2026.189584](https://doi.org/10.1016/j.bbcan.2026.189584) PMID: [41935674](https://pubmed.ncbi.nlm.nih.gov/41935674/)

4. Xu W et al. (2024). *Identification of miRNA signature in cancer-associated fibroblast to predict recurrent prostate cancer.* Comput Biol Med. DOI: [10.1016/j.compbiomed.2024.108989](https://doi.org/10.1016/j.compbiomed.2024.108989) PMID: [39142223](https://pubmed.ncbi.nlm.nih.gov/39142223/)

5. Porcel-Pastrana F et al. (2025). *miR-191-5p: A tumour suppressor miRNA and a personalized biomarker and potential therapeutic tool connecting prostate cancer and obesity.* Biomed Pharmacother. DOI: [10.1016/j.biopha.2025.118330](https://doi.org/10.1016/j.biopha.2025.118330) PMID: [40618585](https://pubmed.ncbi.nlm.nih.gov/40618585/)

---

## miR-1843b-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -2.85 | 3.09e-11 | 4.9 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AUGGAGGUCUCUGUCUGACUU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

No functional summary could be generated from available literature.

### Literature

No relevant publications found in PubMed.

---

## miR-152-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -5.57 | 8.38e-34 | 4.8 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-152-3p** - **100% identical** (21 nt)

Sequence: `UCAGUGCAUGACAGAACUUGG`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 52**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| B4galt5 | 1 | -0.69 |
| Gfra4 | 1 | -0.665 |
| Dock6 | 1 | -0.558 |
| Prune | 1 | -0.554 |
| Zfp110 | 1 | -0.538 |
| Ppp6r1 | 1 | -0.506 |
| 8030462N17Rik | 2 | -0.493 |
| Rictor | 2 | -0.486 |
| Wasl | 2 | -0.463 |
| Dnmt1 | 1 | -0.44 |

**Top target gene: B4galt5** (UDP-Gal:betaGlcNAc beta 1,4-galactosyltransferase, polypeptide 5)

*Function:* Enables N-acetyllactosamine synthase activity and UDP-galactose:glucosylceramide beta-1,4-galactosyltransferase activity. Involved in several processes, including ganglioside biosynthetic process via lactosylceramide; neurogenesis; and positive regulation of embryonic development. Acts upstream of or within poly-N-acetyllactosamine biosynthetic process. Predicted to be located in Golgi cisterna membrane. Predicted to be active in Golgi apparatus. Is expressed in several structures, including epi...

*NCBI Gene ID:* [56336](https://www.ncbi.nlm.nih.gov/gene/56336)

### Biological Function Summary

Mechanistically, PDIA3P1 competes with miR-152-3p to prevent degradation of glucose transporter 1 (GLUT1) mRNA, and disrupts the binding between membrane-associated RING-CH 8 (MARCH8) and hexokinase 2 (HK2) to reduce ubiquitination degradation of HK2, thereby promoting glycolysis. (PMID: 40470706) MiRNA sequencing identified miR-152-3p as a key regulator. (PMID: 40075158) Further investigation using dual-luciferase reporter assays, qRT-PCR, and Western blot revealed that miR-152-3p inhibits the expression of FGFR3 by binding to its 3' UTR. (PMID: 40075158) Meanwhile, functional assays, including angiogenesis assays, Transwell assays, and wound healing assays, were performed to evaluate the effects of miR-152-3p on angiogenesis. (PMID: 40075158) We confirmed the significant role of SLC7A7 in BCa progression, specifically in promoting angiogenesis, through the involvement of exosomes and the regulatory axis of miR-152-3p/ FGFR3. (PMID: 40075158)

### Literature

1. Huang T et al. (2025). *WTAP Mediated m6A Modification Stabilizes PDIA3P1 and Promotes Tumor Progression Driven by Histone Lactylation in Esophageal Squamous Cell Carcinoma.* Adv Sci (Weinh). DOI: [10.1002/advs.202506529](https://doi.org/10.1002/advs.202506529) PMID: [40470706](https://pubmed.ncbi.nlm.nih.gov/40470706/)

2. Cao C et al. (2025). *Exosomes containing miR-152-3p targeting FGFR3 mediate SLC7A7-induced angiogenesis in bladder cancer.* NPJ Precis Oncol. DOI: [10.1038/s41698-025-00859-z](https://doi.org/10.1038/s41698-025-00859-z) PMID: [40075158](https://pubmed.ncbi.nlm.nih.gov/40075158/)

3. Di W et al. (2025). *Exosome miR-152-3p derived from small intestinal epithelium modulates aging process in adipocytes.* 3 Biotech. DOI: [10.1007/s13205-025-04346-x](https://doi.org/10.1007/s13205-025-04346-x) PMID: [40375937](https://pubmed.ncbi.nlm.nih.gov/40375937/)

4. Li Y et al. (2022). *miR-152-3p Represses the Proliferation of the Thymic Epithelial Cells by Targeting Smad2.* Genes (Basel). DOI: [10.3390/genes13040576](https://doi.org/10.3390/genes13040576) PMID: [35456382](https://pubmed.ncbi.nlm.nih.gov/35456382/)

5. Song Y et al. (2020). *EPAS1 targeting by miR-152-3p in Paclitaxel-resistant Breast Cancer.* J Cancer. DOI: [10.7150/jca.46898](https://doi.org/10.7150/jca.46898) PMID: [32913475](https://pubmed.ncbi.nlm.nih.gov/32913475/)

---

## miR-1843a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -3.33 | 2.68e-12 | 4.6 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `UAUGGAGGUCUCUGUCUGACU`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

By integrating miRNA-mRNA regulatory networks, mmu-miR-1843a-5p, mmu-miR-193a-5p, mmu-miR-194-2-3p, and mmu-miR-30c-2-3p were identified as lysyl oxidases-specific miRNAs that were correlated with fibrosis reversal. (PMID: 34367261) RESULTS: Fourteen microRNAs, including miR-18a-5p, miR-376c-3p, miR-136-5p, miR-467c-5p, miR-467b-5p, miR-5104, miR-3098-3p, miR-30a-3p, miR-302b-3p, miR-18a-3p, miR-19b-1-5p, miR-19a-5p, miR-20a-5p, miR-155-5p, were up-regulated, while twenty-six microRNAs, including miR-200b-3p, miR-450a-1-3p, ... (PMID: 28816269) Furthermore, OI-EVs and BMSCs RNAs bioinformatics analysis indicated that OI-EVs play roles through transporting pivotal lncRNA acting as a "sponge" to compete with Mob3a for miR-1843a-5p to promote YAP dephosphorylation and nuclear translocation, ultimately resulting in elevated proliferation an... (PMID: 38311197) Clarification of potential OI-EVs lncRNA ceRNA regulatory mechanism in senescent bone regeneration OI-EVs play important roles through transferring lncRNA-ENSRNOG00000056625 sponging miR-1843a-5p that targeted Mob3a to activate YAP translocation into nucleus, ultimately alleviate senescence, prom... (PMID: 38311197)

### Literature

1. Tai Y et al. (2021). *Integrated Analysis of Hepatic miRNA and mRNA Expression Profiles in the Spontaneous Reversal Process of Liver Fibrosis.* Front Genet. DOI: [10.3389/fgene.2021.706341](https://doi.org/10.3389/fgene.2021.706341) PMID: [34367261](https://pubmed.ncbi.nlm.nih.gov/34367261/)

2. Cai Y et al. (2017). *[MicroRNA differential expression profile in tuberous sclerosis complex cell line TSC2(-/-) MEFs and normal cell line TSC2(+/+) MEFs].* Beijing Da Xue Xue Bao Yi Xue Ban. PMID: [28816269](https://pubmed.ncbi.nlm.nih.gov/28816269/)

3. Qi L et al. (2024). *Mesoporous bioactive glass scaffolds for the delivery of bone marrow stem cell-derived osteoinductive extracellular vesicles lncRNA promote senescent bone defect repair by targeting the miR-1843a-5p/Mob3a/YAP axis.* Acta Biomater. DOI: [10.1016/j.actbio.2024.01.044](https://doi.org/10.1016/j.actbio.2024.01.044) PMID: [38311197](https://pubmed.ncbi.nlm.nih.gov/38311197/)

---

## miR-26a-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -3.43 | 4.48e-11 | 4.0 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-26a-5p** - **100% identical** (22 nt)

Sequence: `UUCAAGUAAUCCAGGAUAGGCU`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

**Total predicted target genes: 716**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Nap1l5 | 2 | -0.735 |
| Mab21l1 | 2 | -0.653 |
| Srp19 | 1 | -0.641 |
| Mtx2 | 1 | -0.631 |
| Nabp1 | 1 | -0.612 |
| Cdk8 | 3 | -0.603 |
| Nab1 | 1 | -0.6 |
| Palm3 | 1 | -0.589 |
| Grtp1 | 1 | -0.579 |
| Ghsr | 1 | -0.573 |

**Top target gene: Nap1l5** (nucleosome assembly protein 1-like 5)

*Function:* Predicted to be involved in nucleosome assembly. Predicted to be located in nucleus. Is expressed in several structures, including brain; extraembryonic component; liver; reproductive system; and spinal cord. Orthologous to human NAP1L5 (nucleosome assembly protein 1 like 5). [provided by Alliance of Genome Resources, Jul 2025]

*NCBI Gene ID:* [58243](https://www.ncbi.nlm.nih.gov/gene/58243)

### Biological Function Summary

Finally, in addition to activating the repair properties of renal progenitor/stem cells, we uncovered a role for MSC-derived miR-26a-5p in mediating the therapeutic effects of MSCs by inhibiting Zeb2 expression and suppressing pro-fibrotic TECs and its subsequent recruitment of immune cell subpop... (PMID: 37533253) The effects of miR-26a-5p were tested after transfecting miR-26a-5p over-expressive lentivirus. (PMID: 39749190) BMDM-derived exosomes (BMDM-exo) increased miR-26a-5p and decreased PTGS2 expressions, inhibited the NF-κB signaling pathway and regulated macrophage polarization in vivo. (PMID: 39749190) Dual luciferase reporter assay results showed that miR-26a-5p directly binds to the 3'-UTR of PTGS2 mRNA and regulates the expression of PTGS2. (PMID: 39749190) The miR-26a-5p of BMDM-exo played a key role in macrophage polarization. (PMID: 39749190)

### Literature

1. Wang W et al. (2023). *Single-cell dissection of cellular and molecular features underlying mesenchymal stem cell therapy in ischemic acute kidney injury.* Mol Ther. DOI: [10.1016/j.ymthe.2023.07.024](https://doi.org/10.1016/j.ymthe.2023.07.024) PMID: [37533253](https://pubmed.ncbi.nlm.nih.gov/37533253/)

2. He W et al. (2024). *Qingre Huoxue Decoction Alleviates Atherosclerosis by Regulating Macrophage Polarization Through Exosomal miR-26a-5p.* Drug Des Devel Ther. DOI: [10.2147/DDDT.S487476](https://doi.org/10.2147/DDDT.S487476) PMID: [39749190](https://pubmed.ncbi.nlm.nih.gov/39749190/)

3. Zhu J et al. (2024). *The Role of lncRNA-miR-26a-mRNA Network in Cancer Progression and Treatment.* Biochem Genet. DOI: [10.1007/s10528-023-10475-w](https://doi.org/10.1007/s10528-023-10475-w) PMID: [37730965](https://pubmed.ncbi.nlm.nih.gov/37730965/)

4. He M et al. (2024). *M(7)G modification of FTH1 and pri-miR-26a regulates ferroptosis and chemotherapy resistance in osteosarcoma.* Oncogene. DOI: [10.1038/s41388-023-02882-5](https://doi.org/10.1038/s41388-023-02882-5) PMID: [38040806](https://pubmed.ncbi.nlm.nih.gov/38040806/)

5. Ayaz G et al. (2025). *Association of glycoprotein 1b and miR-26a-5p levels with platelet function in Alzheimer's disease.* J Alzheimers Dis. DOI: [10.1177/13872877251326204](https://doi.org/10.1177/13872877251326204) PMID: [40112326](https://pubmed.ncbi.nlm.nih.gov/40112326/)

---

## miR-101a-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -3.54 | 8.08e-11 | 3.7 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-101-3p** - **100% identical** (21 nt)

Sequence: `UACAGUACUGUGAUAACUGAA`

The mature miRNA sequence is perfectly conserved between mouse and human, suggesting direct translational relevance of findings to human biology.

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-101a-3p shares seed family 'UACAGUA' with miR-101a-3p.2. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 934**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Ube2d1 | 2 | -0.82 |
| Zfp804a | 3 | -0.771 |
| Epc1 | 1 | -0.767 |
| Atp1b1 | 2 | -0.737 |
| Zfp800 | 2 | -0.692 |
| Trappc8 | 1 | -0.626 |
| Arg2 | 1 | -0.622 |
| Nup37 | 1 | -0.6 |
| Mycn | 2 | -0.585 |
| Med4 | 1 | -0.568 |

**Top target gene: Ube2d1** (ubiquitin-conjugating enzyme E2D 1)

*Function:* Enables ubiquitin conjugating enzyme activity. Acts upstream of or within positive regulation of protein polyubiquitination and protein polyubiquitination. Predicted to be located in cytoplasm. Predicted to be part of ubiquitin ligase complex. Predicted to be active in nucleus. Is expressed in nervous system and urethra. Orthologous to human UBE2D1 (ubiquitin conjugating enzyme E2 D1). [provided by Alliance of Genome Resources, Apr 2025]

*NCBI Gene ID:* [216080](https://www.ncbi.nlm.nih.gov/gene/216080)

### Biological Function Summary

Elevated ethanolamine increased the expression of microRNA-miR-101a-3p by enhancing ARID3a binding on the miR promoter. (PMID: 36948576) Increased miR-101a-3p decreased the stability of zona occludens-1 (Zo1) mRNA, which in turn, weakened intestinal barriers and induced gut permeability, inflammation and abnormalities in glucose metabolism. (PMID: 36948576) miR-101a-3p was validated as a synaptic miRNA upregulated in aSyn Tg mice and in the cortex of dementia with Lewy bodies patients. (PMID: 36744345) Mice and primary cultured neurons overexpressing miR-101a-3p showed downregulation of postsynaptic proteins GABA Ab2 and SAPAP3 and altered dendritic morphology resembling synaptic plasticity impairments and/or synaptic damage. (PMID: 36744345) Finally, a dynamic role of miR-101a-3p in synapse plasticity was shown by identifying downregulation of miR-101a-3p in a condition of enhanced synaptic plasticity modelled in Wt animals housed in enriched environment. (PMID: 36744345)

### Literature

1. Mishra SP et al. (2023). *A mechanism by which gut microbiota elevates permeability and inflammation in obese/diabetic mice and human gut.* Gut. DOI: [10.1136/gutjnl-2022-327365](https://doi.org/10.1136/gutjnl-2022-327365) PMID: [36948576](https://pubmed.ncbi.nlm.nih.gov/36948576/)

2. Xylaki M et al. (2023). *miR-101a-3p Impairs Synaptic Plasticity and Contributes to Synucleinopathy.* J Parkinsons Dis. DOI: [10.3233/JPD-225055](https://doi.org/10.3233/JPD-225055) PMID: [36744345](https://pubmed.ncbi.nlm.nih.gov/36744345/)

3. Tao X et al. (2024). *miR-101a-3p/ROCK2 axis regulates neuronal injury in Parkinson's disease models.* Aging (Albany NY). DOI: [10.18632/aging.205836](https://doi.org/10.18632/aging.205836) PMID: [38775730](https://pubmed.ncbi.nlm.nih.gov/38775730/)

4. Geng J et al. (2021). *MiR-101a-3p Attenuated Pilocarpine-Induced Epilepsy by Downregulating c-FOS.* Neurochem Res. DOI: [10.1007/s11064-021-03245-w](https://doi.org/10.1007/s11064-021-03245-w) PMID: [33559830](https://pubmed.ncbi.nlm.nih.gov/33559830/)

5. Ghafouri-Fard S et al. (2022). *Aberrant expression of miRNAs in epilepsy.* Mol Biol Rep. DOI: [10.1007/s11033-022-07188-5](https://doi.org/10.1007/s11033-022-07188-5) PMID: [35088379](https://pubmed.ncbi.nlm.nih.gov/35088379/)

---

## miR-1839-3p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -2.27 | 5.00e-07 | 3.5 |

### Human Ortholog (miRBase Sequence Comparison)

**No human ortholog found.**

Mouse sequence: `AGACCUACUUAUCUACCAACAGC`

### Predicted Gene Targets (TargetScan Mouse 8.0)

No predicted targets found in TargetScan Mouse 8.0 conserved predictions.

### Biological Function Summary

Microarray analysis (758 miRNAs) identified beneficial changes in nine oncogenic/tumor-suppressive miRNAs, including miR-10a-5p, miR-322-5p, miR-450a-5p, miR-142-5p, miR-148b-3p, miR-1839-3p, miR-18a-5p, miR-1949, and miR-347. (PMID: 40371330)

### Literature

1. Dvorska D et al. (2025). *Chemopreventive and therapeutic effects of Hippophae rhamnoides L. fruit peels evaluated in preclinical models of breast carcinoma.* Front Pharmacol. DOI: [10.3389/fphar.2025.1561436](https://doi.org/10.3389/fphar.2025.1561436) PMID: [40371330](https://pubmed.ncbi.nlm.nih.gov/40371330/)

2. Zhang C et al. (2024). *The Role of Thyroid Hormone Synthesis Gene-Related miRNAs Profiling in Structural and Functional Changes of The Thyroid Gland Induced by Excess Iodine.* Biol Trace Elem Res. DOI: [10.1007/s12011-023-03691-3](https://doi.org/10.1007/s12011-023-03691-3) PMID: [37243879](https://pubmed.ncbi.nlm.nih.gov/37243879/)

---

## miR-152-5p

### Biomarker Context

| Group | Direction | log2FC | FDR | Biomarker Score |
|-------|-----------|--------|-----|----------------|
| Cells (4T1) | Downregulated | -4.69 | 3.68e-15 | 3.5 |

### Human Ortholog (miRBase Sequence Comparison)

**Human ortholog: hsa-miR-152-5p** - **12.5% identity**

| | Sequence | Length |
|---|---|---|
| Mouse (mmu-miR-152-5p) | `UAGGUUCUGUGAUACACUCCGACU` | 24 nt |
| Human (hsa-miR-152-5p) | `AGGUUCUGUGAUACACUCCGACU` | 23 nt |

```
Mouse: UAGGUUCUGUGAUACACUCCGACU
       XX|X|XXXXXXXXXXXXX|XXXX-
Human: AGGUUCUGUGAUACACUCCGACU
```
(`|` = match, `X` = mismatch, `-` = length difference)

**Mismatches:**

- Position 1: U (mouse) -> A (human) *(in seed region)*
- Position 2: A (mouse) -> G (human) *(in seed region)*
- Position 4: G (mouse) -> U (human) *(in seed region)*
- Position 6: U (mouse) -> C (human) *(in seed region)*
- Position 7: C (mouse) -> U (human) *(in seed region)*
- Position 8: U (mouse) -> G (human) *(in seed region)*
- Position 9: G (mouse) -> U (human)
- Position 10: U (mouse) -> G (human)
- Position 11: G (mouse) -> A (human)
- Position 12: A (mouse) -> U (human)
- Position 13: U (mouse) -> A (human)
- Position 14: A (mouse) -> C (human)
- Position 15: C (mouse) -> A (human)
- Position 16: A (mouse) -> C (human)
- Position 17: C (mouse) -> U (human)
- Position 18: U (mouse) -> C (human)
- Position 20: C (mouse) -> G (human)
- Position 21: G (mouse) -> A (human)
- Position 22: A (mouse) -> C (human)
- Position 23: C (mouse) -> U (human)

Length difference: 1 nt

*WARNING: 6 mismatch(es) in the seed region (positions 2-8), which may result in different target gene specificity between species.*

### Predicted Gene Targets (TargetScan Mouse 8.0)

> Note: miR-152-5p shares seed family 'CAGUGCA' with miR-148a-3p. These miRNAs have identical seed sequences and are predicted to regulate the same targets.

**Total predicted target genes: 647**

**Top 10 predicted targets (by weighted context++ score):**

| Gene Symbol | Total num conserved sites | Cumulative weighted context++ score |
| --- | --- | --- |
| Meox2 | 2 | -0.933 |
| Arl6ip1 | 1 | -0.876 |
| Snn | 3 | -0.861 |
| Gadd45a | 1 | -0.83 |
| Eogt | 1 | -0.792 |
| Tmem54 | 1 | -0.767 |
| Arrdc3 | 2 | -0.765 |
| Nptn | 1 | -0.734 |
| S1pr1 | 2 | -0.726 |
| Szrd1 | 2 | -0.705 |

**Top target gene: Meox2** (mesenchyme homeobox 2)

*Function:* Predicted to enable DNA-binding transcription activator activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Acts upstream of or within several processes, including angiogenesis; skeletal muscle tissue development; and somite specification. Predicted to be located in cytoplasm. Predicted to be active in nucleus. Is expressed in several structures, including alimentary system; embryo mesenchyme; genitourinary system; heart; and m...

*NCBI Gene ID:* [17286](https://www.ncbi.nlm.nih.gov/gene/17286)

### Biological Function Summary

RT-qPCR verified the significant differential expression of miR-152-5p and miR-3681-5p between STEMI and NSTEM groups. (PMID: 35751950) Exosomal miR-152-5p and miR-3681-5p may serve as potential biomarkers for ST-segment elevation myocardial infarction. (PMID: 35751950) In the present study, miRNA sequencing and reverse transcription-quantitative polymerase chain reaction techniques revealed that the expression of exosome derived miR-152-5p was significantly downregulated in patients with AMI compared with healthy controls. (PMID: 36936709) Following transfection of the cardiomyocytes using an miR-152-5p inhibitor, immunofluorescence staining of a-smooth muscle actin revealed a marked increase in fibrosis. (PMID: 36936709) The transfection of cardiomyocytes with miR-152-5p mimics was found to inhibit the activation of ARHGAP6 and Rho-associated coiled-coil containing kinase 2 (ROCK2). (PMID: 36936709)

### Literature

1. Chen X et al. (2022). *Exosomal miR-152-5p and miR-3681-5p function as potential biomarkers for ST-segment elevation myocardial infarction.* Clinics (Sao Paulo). DOI: [10.1016/j.clinsp.2022.100038](https://doi.org/10.1016/j.clinsp.2022.100038) PMID: [35751950](https://pubmed.ncbi.nlm.nih.gov/35751950/)

2. Chen S et al. (2023). *Exosomal miR‑152‑5p/ARHGAP6/ROCK axis regulates apoptosis and fibrosis in cardiomyocytes.* Exp Ther Med. DOI: [10.3892/etm.2023.11864](https://doi.org/10.3892/etm.2023.11864) PMID: [36936709](https://pubmed.ncbi.nlm.nih.gov/36936709/)

3. Li S et al. (2022). *MiR-152-5p suppresses osteogenic differentiation of mandible mesenchymal stem cells by regulating ATG14-mediated autophagy.* Stem Cell Res Ther. DOI: [10.1186/s13287-022-03018-4](https://doi.org/10.1186/s13287-022-03018-4) PMID: [35883156](https://pubmed.ncbi.nlm.nih.gov/35883156/)

4. Kong S et al. (2020). *miR-152-5p suppresses glioma progression and tumorigenesis and potentiates temozolomide sensitivity by targeting FBXL7.* J Cell Mol Med. DOI: [10.1111/jcmm.15114](https://doi.org/10.1111/jcmm.15114) PMID: [32150671](https://pubmed.ncbi.nlm.nih.gov/32150671/)

5. You W et al. (2018). *MiR-152-5p as a microRNA passenger strand special functions in human gastric cancer cells.* Int J Biol Sci. DOI: [10.7150/ijbs.25272](https://doi.org/10.7150/ijbs.25272) PMID: [29904279](https://pubmed.ncbi.nlm.nih.gov/29904279/)

---

## Data Sources

- **TargetScan Mouse 8.0**: Agarwal V, Bell GW, Nam JW, Bartel DP. Predicting effective microRNA target sites in mammalian mRNAs. *eLife*. 2015;4:e05005. DOI: [10.7554/eLife.05005](https://doi.org/10.7554/eLife.05005)

- **miRBase (Release 22.1)**: Kozomara A, Birgaoanu M, Griffiths-Jones S. miRBase: from microRNA sequences to function. *Nucleic Acids Research*. 2019;47(D1):D155-D162. DOI: [10.1093/nar/gky1141](https://doi.org/10.1093/nar/gky1141)

- **NCBI PubMed/Gene**: National Center for Biotechnology Information. https://www.ncbi.nlm.nih.gov/

