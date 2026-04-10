#!/usr/bin/env python3
"""
Generate workflow diagram for the Cross-Study Senescence miRNA Analysis Pipeline.
Based on the analysis described in Herbert-Fountain/Senolytic-Logic-Gates.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np


def draw_senescence_workflow():
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis('off')

    # Color scheme
    c = {
        'lit':        '#6c5ce7',   # literature/candidate ID
        'data':       '#0984e3',   # data acquisition
        'norm':       '#e17055',   # normalization
        'fc':         '#00b894',   # fold change
        'concordance':'#fdcb6e',   # cross-dataset concordance
        'circuit':    '#2d3436',   # circuit viability
        'dataset':    '#dfe6e9',   # dataset boxes
        'finding':    '#ffeaa7',   # key finding callout
        'warning':    '#fab1a0',   # caution callout
    }

    def add_box(x, y, w, h, label, sublabel, color, fontsize=12, sublabel_size=8.5):
        box = FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="round,pad=0.15",
            facecolor=color, edgecolor='white', linewidth=2.5,
            alpha=0.95, zorder=3
        )
        ax.add_patch(box)
        ax.text(x, y + 0.15, label, ha='center', va='center',
                fontsize=fontsize, fontweight='bold', color='white', zorder=4)
        if sublabel:
            ax.text(x, y - 0.22, sublabel, ha='center', va='center',
                    fontsize=sublabel_size, color='#ecf0f1', style='italic', zorder=4)

    def add_arrow(x1, y1, x2, y2, color='#636e72'):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color=color,
                                    lw=2.5, connectionstyle='arc3,rad=0'),
                    zorder=2)

    def add_side_panel(x, y, w, h, title, body, border_color='#b2bec3',
                       bg_color='#f8f9fa', title_color='#2d3436'):
        box = FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle="round,pad=0.12",
            facecolor=bg_color, edgecolor=border_color, linewidth=1.5,
            alpha=0.95, zorder=3
        )
        ax.add_patch(box)
        ax.text(x, y + h/2 - 0.25, title, ha='center', va='center',
                fontsize=9, fontweight='bold', color=title_color, zorder=4)
        ax.text(x, y - 0.1, body, ha='center', va='center',
                fontsize=7.5, color='#495057', zorder=4, linespacing=1.35)

    def add_dashed_arrow(x1, y1, x2, y2):
        ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle='->', color='#b2bec3',
                                    lw=1.2, linestyle='dashed'),
                    zorder=2)

    # =========================================================================
    # TITLE
    # =========================================================================
    ax.text(8, 11.6, 'Cross-Study miRNA Synthesis Pipeline', ha='center', va='center',
            fontsize=20, fontweight='bold', color='#2d3436')
    ax.text(8, 11.2, 'Senescence & Aging miRNA Landscape for Logic Gate Circuit Design',
            ha='center', va='center', fontsize=11, color='#636e72')

    # =========================================================================
    # MAIN PIPELINE (vertical, center)
    # =========================================================================
    cx = 6.0
    box_w = 3.8
    box_h = 0.8

    # Step 1: Literature & Candidate ID
    add_box(cx, 10.2, box_w, box_h,
            'Candidate miRNA Identification',
            'Senescence & aging literature review', c['lit'])

    add_arrow(cx, 9.8, cx, 9.25)

    # Step 2: Data Acquisition
    add_box(cx, 8.85, box_w, box_h,
            'Public Dataset Acquisition',
            '11 datasets from NCBI GEO', c['data'])

    add_arrow(cx, 8.45, cx, 7.9)

    # Step 3: CPM Normalization
    add_box(cx, 7.5, box_w, box_h,
            'CPM Normalization',
            'Library size correction per sample', c['norm'])

    add_arrow(cx, 7.1, cx, 6.55)

    # Step 4: Fold Change Computation
    add_box(cx, 6.15, box_w, box_h,
            'Fold Change Computation',
            'Senescent/aged vs. control/young per dataset', c['fc'])

    add_arrow(cx, 5.75, cx, 5.2)

    # Step 5: Cross-Dataset Concordance
    add_box(cx, 4.8, box_w, box_h,
            'Cross-Dataset Concordance',
            'Direction & magnitude across 11 datasets', c['concordance'],
            fontsize=11, sublabel_size=8.5)
    # Override text color for yellow background
    # Re-draw text in dark color
    ax.texts[-1].set_color('#856404')
    ax.texts[-2].set_color('#2d3436')

    add_arrow(cx, 4.4, cx, 3.85)

    # Step 6: Circuit Viability
    add_box(cx, 3.45, box_w, box_h,
            'Circuit Viability Assessment',
            'ON/OFF switch candidate ranking', c['circuit'])

    # =========================================================================
    # Step numbers
    # =========================================================================
    steps_y = [10.2, 8.85, 7.5, 6.15, 4.8, 3.45]
    for i, sy in enumerate(steps_y, 1):
        circle = plt.Circle((cx - 2.2, sy), 0.2, color='white',
                             ec='#636e72', linewidth=1.5, zorder=5)
        ax.add_patch(circle)
        ax.text(cx - 2.2, sy, str(i), ha='center', va='center',
                fontsize=10, fontweight='bold', color='#636e72', zorder=6)

    # =========================================================================
    # RIGHT SIDE: Dataset Panel
    # =========================================================================
    ds_text = (
        "GSE299871  WI-38 fibroblasts (DXR/SDS/RS)\n"
        "GSE94410    HUVEC endothelial (replicative)\n"
        "GSE202120  HAEC endothelial (irradiation)\n"
        "GSE117818  MRC-5 fibroblasts (replicative)\n"
        "GSE200330  Synovial fibroblast EVs (irr.)\n"
        "GSE217458  16 mouse tissues (aging)\n"
        "GSE55164    Mouse muscle (aging)\n"
        "GSE172269  11 rat organs (aging)\n"
        "GSE136926  Human heart (aging)\n"
        "GSE111281  Human skin (aging)\n"
        "GSE111174  Human blood (aging)"
    )
    add_side_panel(12.2, 8.85, 5.4, 3.2, '11 Datasets  |  1,300+ Samples  |  3 Organisms',
                   ds_text, border_color='#74b9ff', bg_color='#f0f7ff',
                   title_color='#0984e3')
    add_dashed_arrow(9.5, 8.85, 9.9, 8.85)

    # =========================================================================
    # RIGHT SIDE: CPM Explanation
    # =========================================================================
    cpm_text = (
        "CPM = (raw counts / total library) x 1,000,000\n\n"
        "Corrects sequencing depth bias between samples\n"
        "Eliminated 2 false candidates:\n"
        "  miR-29a-3p: 1.56x raw  -->  0.96x CPM (artifact)\n"
        "  miR-21-5p:  1.79x raw  -->  1.09x CPM (artifact)"
    )
    add_side_panel(12.2, 6.85, 5.4, 1.7, 'CPM Normalization Impact',
                   cpm_text, border_color='#e17055', bg_color='#fff5f2',
                   title_color='#e17055')
    add_dashed_arrow(9.5, 7.5, 9.9, 7.1)

    # =========================================================================
    # LEFT SIDE: Key Findings Panel
    # =========================================================================
    findings_text = (
        "ON Switch (UP in senescence):\n"
        "  miR-34a-5p: UP in 18/21 analyses\n"
        "  1.5x FC (CPM), ~45 copies/cell\n"
        "  p53 target, conserved across 3 species\n\n"
        "OFF Switch (DOWN in senescence):\n"
        "  miR-155-5p: 0.09x (fibroblast only)\n"
        "  miR-92a-3p: 0.26x (cross-tissue)\n"
        "  miR-16-5p:   0.37x (fibroblast + kidney)\n"
        "  miR-17-5p:   0.19x (fibroblast specific)"
    )
    add_side_panel(12.2, 4.25, 5.4, 2.6, 'Key Biomarker Candidates',
                   findings_text, border_color='#00b894', bg_color='#f0fff8',
                   title_color='#00b894')
    add_dashed_arrow(9.5, 4.8, 9.9, 4.7)

    # =========================================================================
    # LEFT SIDE: Concordance Criteria
    # =========================================================================
    conc_text = (
        "4 senescence inducers compared\n"
        "(DXR, SDS, irradiation, replicative)\n\n"
        "4 human cell types tested\n"
        "(WI-38, MRC-5, HUVEC, HAEC)\n\n"
        "In vitro vs. in vivo aging\n"
        "compared across tissues"
    )
    add_side_panel(1.8, 5.5, 3.2, 2.4, 'Concordance Assessment',
                   conc_text, border_color='#fdcb6e', bg_color='#fffdf0',
                   title_color='#856404')
    add_dashed_arrow(3.4, 5.5, 4.1, 5.2)

    # =========================================================================
    # LEFT SIDE: Limitations
    # =========================================================================
    lim_text = (
        "n=2 in GSE299871 (hypothesis generating)\n"
        "Bulk tissue confounding (inflammaging)\n"
        "Blood vs. tissue divergence\n"
        "In vitro/in vivo fold change gap"
    )
    add_side_panel(1.8, 3.45, 3.2, 1.4, 'Key Limitations',
                   lim_text, border_color='#e17055', bg_color='#fff5f2',
                   title_color='#d63031')
    add_dashed_arrow(3.4, 3.45, 4.1, 3.45)

    # =========================================================================
    # BOTTOM: Circuit Architectures
    # =========================================================================
    # Three circuit boxes at bottom
    circ_y = 1.8

    # Universal
    box_u = FancyBboxPatch(
        (1.0, circ_y - 0.55), 3.8, 1.1,
        boxstyle="round,pad=0.12",
        facecolor='#dfe6e9', edgecolor='#636e72', linewidth=1.5,
        alpha=0.95, zorder=3
    )
    ax.add_patch(box_u)
    ax.text(2.9, circ_y + 0.3, 'Universal (U3)', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#2d3436', zorder=4)
    ax.text(2.9, circ_y - 0.0, 'miR-34a + miR-16 + miR-92a', ha='center', va='center',
            fontsize=8, color='#636e72', zorder=4)
    ax.text(2.9, circ_y - 0.25, 'Selectivity: 4-15x', ha='center', va='center',
            fontsize=8, color='#636e72', style='italic', zorder=4)

    # Fibroblast F1
    box_f1 = FancyBboxPatch(
        (5.6, circ_y - 0.55), 3.8, 1.1,
        boxstyle="round,pad=0.12",
        facecolor='#dfe6e9', edgecolor='#636e72', linewidth=1.5,
        alpha=0.95, zorder=3
    )
    ax.add_patch(box_f1)
    ax.text(7.5, circ_y + 0.3, 'Fibroblast (F1)', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#2d3436', zorder=4)
    ax.text(7.5, circ_y - 0.0, 'miR-34a + miR-155', ha='center', va='center',
            fontsize=8, color='#636e72', zorder=4)
    ax.text(7.5, circ_y - 0.25, 'Selectivity: ~16x', ha='center', va='center',
            fontsize=8, color='#636e72', style='italic', zorder=4)

    # Fibroblast F4
    box_f4 = FancyBboxPatch(
        (10.2, circ_y - 0.55), 3.8, 1.1,
        boxstyle="round,pad=0.12",
        facecolor='#dfe6e9', edgecolor='#636e72', linewidth=1.5,
        alpha=0.95, zorder=3
    )
    ax.add_patch(box_f4)
    ax.text(12.1, circ_y + 0.3, 'Fibroblast (F4)', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#2d3436', zorder=4)
    ax.text(12.1, circ_y - 0.0, 'miR-34a + miR-155 + miR-92a', ha='center', va='center',
            fontsize=8, color='#636e72', zorder=4)
    ax.text(12.1, circ_y - 0.25, 'Selectivity: ~63x', ha='center', va='center',
            fontsize=8, color='#636e72', style='italic', zorder=4)

    # Label
    ax.text(8, circ_y + 0.8, 'Proposed Circuit Architectures (L7Ae/K-turn AND Gates)',
            ha='center', va='center', fontsize=11, fontweight='bold', color='#2d3436')

    # Arrows from step 6 to circuits
    add_arrow(cx, 3.05, 2.9, circ_y + 0.55)
    add_arrow(cx, 3.05, 7.5, circ_y + 0.55)
    add_arrow(cx + 2, 3.05, 12.1, circ_y + 0.55)

    # =========================================================================
    # Footer
    # =========================================================================
    ax.text(8, 0.6, 'Data: 11 GEO datasets  |  Normalization: CPM  |  Organisms: Human, Mouse, Rat',
            ha='center', va='center', fontsize=8.5, color='#95a5a6', style='italic')
    ax.text(8, 0.3, 'Reference: cross_study_synthesis.md (Herbert-Fountain/Senolytic-Logic-Gates)',
            ha='center', va='center', fontsize=8, color='#b2bec3', style='italic')

    plt.tight_layout()
    return fig


if __name__ == "__main__":
    fig = draw_senescence_workflow()
    fig.savefig('results/senescence_pipeline_workflow.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    fig.savefig('results/senescence_pipeline_workflow.svg', bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print("Saved: results/senescence_pipeline_workflow.png")
    print("Saved: results/senescence_pipeline_workflow.svg")
