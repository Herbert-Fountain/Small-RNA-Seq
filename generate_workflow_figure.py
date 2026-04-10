#!/usr/bin/env python3
"""
Generate a workflow diagram for the miRNA biomarker analysis pipeline.
Produces both PNG and SVG outputs.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np


def draw_workflow():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Color scheme
    colors = {
        'input': '#3498db',
        'preprocess': '#e67e22',
        'alignment': '#27ae60',
        'quantification': '#8e44ad',
        'de_analysis': '#c0392b',
        'biomarker': '#2c3e50',
        'output': '#16a085',
        'text': 'white',
    }

    def add_box(x, y, w, h, label, sublabel, color, fontsize=11):
        box = FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="round,pad=0.15",
            facecolor=color, edgecolor='white', linewidth=2,
            alpha=0.95, zorder=3
        )
        ax.add_patch(box)
        ax.text(x, y + 0.12, label, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', color='white', zorder=4)
        if sublabel:
            ax.text(x, y - 0.22, sublabel, ha='center', va='center',
                    fontsize=8, color='#ecf0f1', style='italic', zorder=4)

    def add_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#7f8c8d',
                                    lw=2, connectionstyle='arc3,rad=0'),
                    zorder=2)

    def add_side_box(x, y, w, h, label, color='#ecf0f1', text_color='#2c3e50'):
        box = FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="round,pad=0.1",
            facecolor=color, edgecolor='#bdc3c7', linewidth=1.5,
            alpha=0.9, zorder=3
        )
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=7.5, color=text_color, zorder=4)

    def add_dashed_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#bdc3c7',
                                    lw=1.2, linestyle='dashed'),
                    zorder=2)

    # =========================================================================
    # TITLE
    # =========================================================================
    ax.text(7, 9.6, 'Small RNA-Seq Analysis Pipeline', ha='center', va='center',
            fontsize=18, fontweight='bold', color='#2c3e50')
    ax.text(7, 9.25, 'Differential miRNA Expression & Biomarker Discovery',
            ha='center', va='center', fontsize=11, color='#7f8c8d')

    # =========================================================================
    # MAIN PIPELINE (vertical flow down the center)
    # =========================================================================
    cx = 5.5  # center x for main pipeline

    # Step 1: Input
    add_box(cx, 8.4, 3.2, 0.7, 'Raw FASTQ Reads',
            '16 samples across 6 groups', colors['input'])

    # Arrow 1->2
    add_arrow(cx, 8.05, cx, 7.55)

    # Step 2: Pre-processing
    add_box(cx, 7.2, 3.2, 0.7, 'Quality Control & Trimming',
            'fastp', colors['preprocess'])

    # Arrow 2->3
    add_arrow(cx, 6.85, cx, 6.35)

    # Step 3: Alignment
    add_box(cx, 6.0, 3.2, 0.7, 'Alignment & Quantification',
            'miRDeep2 (mmu genome, miRBase)', colors['alignment'])

    # Arrow 3->4
    add_arrow(cx, 5.65, cx, 5.15)

    # Step 4: Normalization & DE
    add_box(cx, 4.8, 3.2, 0.7, 'Normalization & DE Analysis',
            'DESeq2 / SARTools', colors['de_analysis'])

    # Arrow 4->5
    add_arrow(cx, 4.45, cx, 3.95)

    # Step 5: Biomarker Analysis
    add_box(cx, 3.6, 3.2, 0.7, 'Biomarker Identification',
            'One vs. rest signature analysis', colors['biomarker'])

    # Arrow 5->6
    add_arrow(cx, 3.25, cx, 2.75)

    # Step 6: Visualization
    add_box(cx, 2.4, 3.2, 0.7, 'Interactive Visualization',
            'Plotly (volcano, heatmap, dot/box plots)', colors['output'])

    # =========================================================================
    # SIDE ANNOTATIONS: left side (details for each step)
    # =========================================================================
    left_x = 1.8

    # Pre-processing details
    add_side_box(left_x, 7.55, 2.6, 0.35, 'Low quality read trimming')
    add_dashed_arrow(3.1, 7.55, 3.9, 7.35)
    add_side_box(left_x, 7.1, 2.6, 0.35, '2-color chemistry correction')
    add_dashed_arrow(3.1, 7.1, 3.9, 7.2)
    add_side_box(left_x, 6.65, 2.6, 0.35, 'Adapter & short fragment removal')
    add_dashed_arrow(3.1, 6.65, 3.9, 7.05)

    # =========================================================================
    # SIDE ANNOTATIONS: right side
    # =========================================================================
    right_x = 10.5

    # Sample info box
    sample_box = FancyBboxPatch(
        (8.8, 7.7), 3.6, 1.4,
        boxstyle="round,pad=0.15",
        facecolor='#f8f9fa', edgecolor='#dee2e6', linewidth=1.5,
        alpha=0.95, zorder=3
    )
    ax.add_patch(sample_box)
    ax.text(10.6, 8.85, 'Experimental Design', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#2c3e50', zorder=4)

    sample_text = (
        "4T1 Cells:  n = 3\n"
        "Heart:       n = 2\n"
        "Kidney:      n = 2\n"
        "Liver:        n = 3\n"
        "Lung:        n = 3\n"
        "Spleen:     n = 3"
    )
    ax.text(10.6, 8.15, sample_text, ha='center', va='center',
            fontsize=7.5, color='#495057', family='monospace', zorder=4,
            linespacing=1.3)
    add_dashed_arrow(8.8, 8.4, 7.1, 8.4)

    # DE analysis details
    de_box = FancyBboxPatch(
        (8.8, 4.0), 3.6, 1.3,
        boxstyle="round,pad=0.15",
        facecolor='#f8f9fa', edgecolor='#dee2e6', linewidth=1.5,
        alpha=0.95, zorder=3
    )
    ax.add_patch(de_box)
    ax.text(10.6, 4.95, 'Pairwise Comparisons', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#2c3e50', zorder=4)

    de_text = (
        "6 signature tests (1 vs. rest)\n"
        "15 pairwise tests (all pairs)\n"
        "FDR < 0.05, |log2FC| > 1.0\n"
        "1,978 miRNAs tested"
    )
    ax.text(10.6, 4.3, de_text, ha='center', va='center',
            fontsize=7.5, color='#495057', zorder=4, linespacing=1.4)
    add_dashed_arrow(8.8, 4.8, 7.1, 4.8)
    add_dashed_arrow(8.8, 4.3, 7.1, 3.6)

    # Output details
    output_box = FancyBboxPatch(
        (8.8, 1.6), 3.6, 1.3,
        boxstyle="round,pad=0.15",
        facecolor='#f8f9fa', edgecolor='#dee2e6', linewidth=1.5,
        alpha=0.95, zorder=3
    )
    ax.add_patch(output_box)
    ax.text(10.6, 2.65, 'Outputs', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#2c3e50', zorder=4)

    output_text = (
        "Volcano & MA plots\n"
        "Expression heatmap (Z-score)\n"
        "Biomarker dot & box plots\n"
        "Ranked candidate table (CSV)"
    )
    ax.text(10.6, 2.0, output_text, ha='center', va='center',
            fontsize=7.5, color='#495057', zorder=4, linespacing=1.4)
    add_dashed_arrow(8.8, 2.4, 7.1, 2.4)

    # =========================================================================
    # Biomarker scoring formula note
    # =========================================================================
    formula_box = FancyBboxPatch(
        (0.3, 2.7), 3.2, 1.1,
        boxstyle="round,pad=0.12",
        facecolor='#fff3cd', edgecolor='#ffc107', linewidth=1.5,
        alpha=0.9, zorder=3
    )
    ax.add_patch(formula_box)
    ax.text(1.9, 3.45, 'Biomarker Score', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#856404', zorder=4)
    ax.text(1.9, 3.05, 'log10(FDR)', ha='center', va='center',
            fontsize=8, color='#856404', zorder=4)
    ax.text(1.9, 2.8, ' x  |log2FC|  x  Specificity', ha='center', va='center',
            fontsize=8, color='#856404', zorder=4)
    add_dashed_arrow(3.5, 3.2, 3.9, 3.6)

    # =========================================================================
    # Step numbers
    # =========================================================================
    steps = [(cx, 8.4), (cx, 7.2), (cx, 6.0), (cx, 4.8), (cx, 3.6), (cx, 2.4)]
    for i, (sx, sy) in enumerate(steps, 1):
        circle = plt.Circle((sx - 1.85, sy), 0.18, color='white',
                             ec='#7f8c8d', linewidth=1.5, zorder=5)
        ax.add_patch(circle)
        ax.text(sx - 1.85, sy, str(i), ha='center', va='center',
                fontsize=9, fontweight='bold', color='#7f8c8d', zorder=6)

    # =========================================================================
    # Bottom annotation
    # =========================================================================
    ax.text(7, 0.7, 'Tools: fastp | miRDeep2 | DESeq2 | SARTools | Python (Pandas, Plotly, scikit-learn)',
            ha='center', va='center', fontsize=8, color='#95a5a6', style='italic')
    ax.text(7, 0.35, 'Reference: Mus musculus (mmu) genome, miRBase mature miRNA annotations',
            ha='center', va='center', fontsize=8, color='#95a5a6', style='italic')

    plt.tight_layout()
    return fig


if __name__ == "__main__":
    fig = draw_workflow()
    fig.savefig('results/pipeline_workflow.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    fig.savefig('results/pipeline_workflow.svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Saved: results/pipeline_workflow.png")
    print("Saved: results/pipeline_workflow.svg")
