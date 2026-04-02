# Figure Captions

## Volcano Plots

**Figure 1. Volcano plot of differentially expressed miRNAs in Heart vs. non-Heart (He_vs_nonHe).** Each point represents one miRNA, plotted by log2 fold change (x-axis) against statistical significance as -log10(FDR) (y-axis). Red points indicate significantly upregulated miRNAs in Heart (FDR <= 0.05, log2FC >= 1.0; n = 33), blue points indicate significantly downregulated miRNAs (FDR <= 0.05, log2FC <= -1.0; n = 69), and gray points are not significant or have low fold change. Dashed lines mark the significance threshold (FDR = 0.05) and fold change cutoffs (log2FC = +/-1.0). The top 5 most significant miRNAs in each direction are labeled. Total miRNAs tested: 989.

**Figure 2. Volcano plot of differentially expressed miRNAs in Kidney vs. non-Kidney (Ki_vs_nonKi).** Each point represents one miRNA, plotted by log2 fold change (x-axis) against statistical significance as -log10(FDR) (y-axis). Red points indicate significantly upregulated miRNAs in Kidney (n = 16), blue points indicate significantly downregulated miRNAs (n = 14). Kidney shows the fewest differentially expressed miRNAs of all groups, consistent with a relatively conserved miRNA profile compared to other tissues. Total miRNAs tested: 870.

**Figure 3. Volcano plot of differentially expressed miRNAs in Liver vs. non-Liver (Li_vs_nonLi).** Each point represents one miRNA, plotted by log2 fold change (x-axis) against statistical significance as -log10(FDR) (y-axis). Red points indicate significantly upregulated miRNAs in Liver (n = 77), blue points indicate significantly downregulated miRNAs (n = 94). The Liver comparison shows several miRNAs with extremely large fold changes (log2FC > 10), including miR-122-5p and miR-122-3p, which are well-established liver-specific miRNAs. Total miRNAs tested: 1,080.

**Figure 4. Volcano plot of differentially expressed miRNAs in Lung vs. non-Lung (Lu_vs_nonLu).** Each point represents one miRNA, plotted by log2 fold change (x-axis) against statistical significance as -log10(FDR) (y-axis). Red points indicate significantly upregulated miRNAs in Lung (n = 50), blue points indicate significantly downregulated miRNAs (n = 65). Total miRNAs tested: 918.

**Figure 5. Volcano plot of differentially expressed miRNAs in Spleen vs. non-Spleen (Sp_vs_nonSp).** Each point represents one miRNA, plotted by log2 fold change (x-axis) against statistical significance as -log10(FDR) (y-axis). Red points indicate significantly upregulated miRNAs in Spleen (n = 189), blue points indicate significantly downregulated miRNAs (n = 143). Spleen shows the largest number of differentially expressed miRNAs among the organ tissues, reflecting its distinct immune cell composition and associated miRNA repertoire. Total miRNAs tested: 1,278.

**Figure 6. Volcano plot of differentially expressed miRNAs in Cells (4T1) vs. Organs (Cells_vs_Organs).** Each point represents one miRNA, plotted by log2 fold change (x-axis) against statistical significance as -log10(FDR) (y-axis). Positive log2FC indicates higher expression in 4T1 cells relative to the average of all five organ tissues. Red points indicate significantly upregulated miRNAs in Cells (n = 206), blue points indicate significantly downregulated miRNAs (n = 376). Note: the log2FC values are negated from the source data to correct for a reversed group assignment in the upstream analysis (see Methods, Note on the Cells_vs_Organs Comparison). Total miRNAs tested: 1,156.

**Figure 7. Combined interactive volcano plot with comparison selector.** Dropdown menu allows switching between all six one-vs-rest comparisons. Each view displays the same classification scheme as the individual volcano plots (Figures 1-6). This combined view facilitates rapid comparison of differential expression patterns across tissue groups without opening separate files.

---

## Heatmap

**Figure 8. Heatmap of top 60 differentially expressed miRNAs across all tissue groups.** Rows represent individual miRNAs (selected as the top 60 by number of significant comparisons and maximum fold change), and columns represent the six biological groups. Color intensity represents the z-score of log2-transformed average normalized counts, computed per miRNA across all groups (red = above-average expression, blue = below-average expression, white = mean expression). miRNAs are ordered by the group in which they show maximum expression, producing visible blocks of tissue-specific expression. Hover text displays the miRNA name, group, z-score, and raw average count.

---

## Biomarker Dot Plots

**Figure 9. Dot plot of top 10 upregulated biomarker candidates per tissue group.** Each row represents a miRNA selected as a top upregulated biomarker for one of the six groups (based on composite biomarker score combining statistical significance, fold change, and tissue specificity). Each column represents a tissue group. Dot size is proportional to log2(average normalized count + 1), reflecting absolute expression level. Dot color represents the z-score of expression across all six groups (red = above-average, blue = below-average, scale clamped to [-3, +3]). A strong upregulated biomarker appears as a large red dot in its focal group column and as smaller blue dots in other columns.

**Figure 10. Dot plot of top 10 downregulated biomarker candidates per tissue group.** Layout and encoding are identical to Figure 9, but miRNAs are selected based on significant downregulation (negative log2FC) in the focal group. A strong downregulated biomarker appears as a small blue dot (or absent) in its focal group column, indicating low or undetectable expression, while appearing as larger red dots in other groups where it is more highly expressed. This pattern is particularly informative for identifying miRNAs whose absence characterizes a tissue type.

---

## Box Plots

**Figure 11. Individual sample expression distributions for top biomarker candidates.** Each subplot shows the normalized count distribution for one miRNA across all six biological groups. The top 5 upregulated biomarker candidates from each group are included. Box plots display the median, interquartile range, and individual replicate values (overlaid as jittered points). Groups are color-coded consistently across all subplots. Strong biomarker candidates show clear separation between the focal group and all other groups, with low within-group variability.

---

## MA Plots

**Figure 12. MA plot for Heart vs. non-Heart (He_vs_nonHe).** Each point represents one miRNA, plotted by log2 mean expression (x-axis) against log2 fold change (y-axis). Red points are significantly differentially expressed (FDR <= 0.05, abs(log2FC) >= 1.0), and gray points are not significant. Horizontal dashed lines indicate log2FC = +/-1.0 thresholds. The MA plot reveals whether differential expression is biased toward highly or lowly expressed miRNAs.

**Figure 13. MA plot for Kidney vs. non-Kidney (Ki_vs_nonKi).** Layout and encoding are identical to Figure 12. The smaller number of significant miRNAs (red points) compared to other tissues is consistent with the volcano plot (Figure 2).

**Figure 14. MA plot for Liver vs. non-Liver (Li_vs_nonLi).** Layout and encoding are identical to Figure 12. Several highly expressed miRNAs show extreme fold changes, consistent with the known tissue-specific expression of liver miRNAs such as miR-122.

**Figure 15. MA plot for Lung vs. non-Lung (Lu_vs_nonLu).** Layout and encoding are identical to Figure 12.

**Figure 16. MA plot for Spleen vs. non-Spleen (Sp_vs_nonSp).** Layout and encoding are identical to Figure 12. The large number of significant miRNAs is consistent with the distinct immune-associated miRNA profile of the spleen.

**Figure 17. MA plot for Cells (4T1) vs. Organs (Cells_vs_Organs).** Layout and encoding are identical to Figure 12. Positive log2FC indicates higher expression in 4T1 cells. The log2FC values have been negated from the source data to correct for a reversed group assignment (see Methods).

---

## Summary Tables

**Table 1. Biomarker candidates summary (biomarker_candidates.csv).** Top 20 biomarker candidates per tissue group ranked by composite biomarker score. Columns include group assignment, miRNA identifier, log2 fold change, adjusted p-value (FDR), average normalized counts for the focal group and comparison group, direction of regulation, tissue specificity score, coefficient of variation among biological replicates, and composite biomarker score.

**Table 2. Detailed biomarker expression profiles (biomarker_summary_tables.csv).** Top 10 upregulated and top 10 downregulated biomarker candidates per group with expression data across all six tissue groups. For each miRNA, the table reports the average normalized count and z-score in every group, enabling direct comparison of expression specificity. Z-scores are computed from log2-transformed counts, normalized per miRNA across all groups.
