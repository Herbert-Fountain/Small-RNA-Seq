#!/usr/bin/env python3
"""
miRNA Biomarker Analysis Pipeline
==================================
Interactive analysis of differential miRNA expression from small RNA-seq data.
Generates interactive Plotly HTML plots for exploring potential biomarkers.

Groups: Cells (4T1), Heart (He), Kidney (Ki), Liver (Li), Lung (Lu), Spleen (Sp)
"""

import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import os

# =============================================================================
# 1. DATA PARSING
# =============================================================================

def parse_signatures_sheet(filepath):
    """Parse the signatures DE genes table (one-vs-rest comparisons)."""
    df_raw = pd.read_excel(filepath, sheet_name="signatures DE genes table", header=None)
    data = df_raw.iloc[5:].copy()
    data.columns = range(len(data.columns))
    data = data.reset_index(drop=True)

    # Gene info
    genes = pd.DataFrame({
        'Index': pd.to_numeric(data[0], errors='coerce'),
        'SortOrder': data[1],
        'GeneID': data[2],
        'Tests': pd.to_numeric(data[3], errors='coerce'),
        'Significant': pd.to_numeric(data[4], errors='coerce'),
        'DIFF': pd.to_numeric(data[5], errors='coerce'),
        'MaxLog2FC': pd.to_numeric(data[6], errors='coerce'),
    })

    # Comparison blocks (11 columns each)
    comparisons_info = [
        ('He_vs_nonHe', 7),
        ('Ki_vs_nonKi', 18),
        ('Li_vs_nonLi', 29),
        ('Lu_vs_nonLu', 40),
        ('Sp_vs_nonSp', 51),
        ('Cells_vs_Organs', 62),
    ]

    comparisons = {}
    for comp_name, sc in comparisons_info:
        comp_df = pd.DataFrame({
            'GeneID': data[2],
            'avg_group1': pd.to_numeric(data[sc], errors='coerce'),
            'avg_group2': pd.to_numeric(data[sc+1], errors='coerce'),
            'log2avg': pd.to_numeric(data[sc+2], errors='coerce'),
            'log2FC': pd.to_numeric(data[sc+3], errors='coerce'),
            'abs_log2FC': pd.to_numeric(data[sc+4], errors='coerce'),
            'pvalue': pd.to_numeric(data[sc+5], errors='coerce'),
            'padj': pd.to_numeric(data[sc+6], errors='coerce'),
            'significant': data[sc+7],
            'min_nCount': pd.to_numeric(data[sc+8], errors='coerce'),
            'min_log2FC': pd.to_numeric(data[sc+9], errors='coerce'),
            'DIFF_EXP': pd.to_numeric(data[sc+10], errors='coerce'),
        })
        comparisons[comp_name] = comp_df

    # Group averages
    group_avg = pd.DataFrame({
        'GeneID': data[2],
        'baseMean': pd.to_numeric(data[73], errors='coerce'),
        'avg_Cells': pd.to_numeric(data[74], errors='coerce'),
        'avg_He': pd.to_numeric(data[75], errors='coerce'),
        'avg_Lu': pd.to_numeric(data[76], errors='coerce'),
        'avg_Li': pd.to_numeric(data[77], errors='coerce'),
        'avg_Sp': pd.to_numeric(data[78], errors='coerce'),
        'avg_Ki': pd.to_numeric(data[79], errors='coerce'),
    })

    # Individual samples
    sample_counts = pd.DataFrame({
        'GeneID': data[2],
        '4T1.1': pd.to_numeric(data[80], errors='coerce'),
        '4T1.2': pd.to_numeric(data[81], errors='coerce'),
        '4T1.3': pd.to_numeric(data[82], errors='coerce'),
        'He.4': pd.to_numeric(data[83], errors='coerce'),
        'He.5': pd.to_numeric(data[84], errors='coerce'),
        'Lu.4': pd.to_numeric(data[85], errors='coerce'),
        'Lu.5': pd.to_numeric(data[86], errors='coerce'),
        'Lu.3': pd.to_numeric(data[87], errors='coerce'),
        'Li.4': pd.to_numeric(data[88], errors='coerce'),
        'Li.5': pd.to_numeric(data[89], errors='coerce'),
        'Li.3': pd.to_numeric(data[90], errors='coerce'),
        'Sp.4': pd.to_numeric(data[91], errors='coerce'),
        'Sp.5': pd.to_numeric(data[92], errors='coerce'),
        'Sp.3': pd.to_numeric(data[93], errors='coerce'),
        'Ki.4': pd.to_numeric(data[94], errors='coerce'),
        'Ki.5': pd.to_numeric(data[95], errors='coerce'),
    })

    return genes, comparisons, group_avg, sample_counts


# =============================================================================
# 2. INTERACTIVE VOLCANO PLOTS
# =============================================================================

def create_volcano_plot(comp_df, comp_name, fdr_cutoff=0.05, fc_cutoff=1.0):
    """Create an interactive volcano plot for a single comparison.
    Labels are draggable annotations with leader lines. Text sizes
    are adjustable via dropdown menus in the plot."""
    df = comp_df.dropna(subset=['log2FC', 'padj']).copy()
    df = df[df['padj'] > 0]  # remove zero p-values for log transform
    df['neg_log10_padj'] = -np.log10(df['padj'])

    # Classify points
    conditions = [
        (df['padj'] <= fdr_cutoff) & (df['log2FC'] >= fc_cutoff),
        (df['padj'] <= fdr_cutoff) & (df['log2FC'] <= -fc_cutoff),
        (df['padj'] <= fdr_cutoff) & (df['log2FC'].abs() < fc_cutoff),
    ]
    choices = ['Up', 'Down', 'Sig (low FC)']
    df['category'] = np.select(conditions, choices, default='Not Sig')

    color_map = {
        'Up': '#e74c3c',
        'Down': '#3498db',
        'Sig (low FC)': '#95a5a6',
        'Not Sig': '#d5d8dc'
    }

    fig = go.Figure()

    for cat in ['Not Sig', 'Sig (low FC)', 'Down', 'Up']:
        subset = df[df['category'] == cat]
        if len(subset) == 0:
            continue
        fig.add_trace(go.Scattergl(
            x=subset['log2FC'],
            y=subset['neg_log10_padj'],
            mode='markers',
            name=f'{cat} ({len(subset)})',
            marker=dict(color=color_map[cat], size=5, opacity=0.7),
            text=subset['GeneID'],
            customdata=np.stack([
                subset['avg_group1'].values,
                subset['avg_group2'].values,
                subset['padj'].values,
                subset['log2FC'].values
            ], axis=-1),
            hovertemplate=(
                '<b>%{text}</b><br>'
                'log2FC: %{customdata[3]:.3f}<br>'
                'FDR: %{customdata[2]:.2e}<br>'
                'Avg Group1: %{customdata[0]:.0f}<br>'
                'Avg Group2: %{customdata[1]:.0f}<br>'
                '<extra></extra>'
            ),
        ))

    # Add threshold lines
    fig.add_hline(y=-np.log10(fdr_cutoff), line_dash="dash", line_color="gray",
                  annotation_text=f"FDR={fdr_cutoff}")
    fig.add_vline(x=fc_cutoff, line_dash="dash", line_color="gray")
    fig.add_vline(x=-fc_cutoff, line_dash="dash", line_color="gray")

    # Label top hits as draggable annotations with leader lines
    top_up = df[(df['category'] == 'Up')].nlargest(5, 'neg_log10_padj')
    top_down = df[(df['category'] == 'Down')].nlargest(5, 'neg_log10_padj')
    top_hits = pd.concat([top_up, top_down])

    default_label_size = 10
    for _, row in top_hits.iterrows():
        label = row['GeneID'].replace('mmu-', '')
        fig.add_annotation(
            x=row['log2FC'],
            y=row['neg_log10_padj'],
            text=label,
            font=dict(size=default_label_size, color='black'),
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1,
            arrowcolor='gray',
            ax=0,
            ay=-30,
            bgcolor='rgba(255,255,255,0.7)',
            borderpad=2,
        )

    pretty_name = comp_name.replace('_', ' ').replace('vs', 'vs.')
    n_up = (df['category'] == 'Up').sum()
    n_down = (df['category'] == 'Down').sum()

    fig.update_layout(
        title=dict(
            text=(f'Volcano Plot: {pretty_name}<br>'
                  f'<sub>{n_up} up, {n_down} down '
                  f'(FDR<{fdr_cutoff}, |log2FC|>{fc_cutoff})</sub>'),
            font=dict(size=16),
            x=0.5,
            xanchor='center',
        ),
        xaxis_title='log2(Fold Change)',
        yaxis_title='-log10(FDR)',
        template='plotly_white',
        width=900,
        height=650,
        legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)'),
    )
    return fig


def _write_interactive_html(fig, filepath, has_annotations=True, default_filename="plot"):
    """Write a Plotly figure to an HTML file with an external control panel.
    Controls use JavaScript to update individual properties without
    resetting other settings.
    If has_annotations=False, annotation/arrow controls are hidden."""
    plot_div = fig.to_html(full_html=False, include_plotlyjs='cdn',
                           config={'editable': True})
    # Find the div id
    import re as _re
    div_match = _re.search(r'id="([^"]+)"', plot_div)
    div_id = div_match.group(1) if div_match else 'plot'

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>
  body {{ margin: 0; font-family: Arial, sans-serif; background: #fafafa; }}
  .container {{ display: flex; gap: 0; }}
  .plot-area {{ flex: 1; min-width: 0; }}
  .controls {{
    width: 220px; min-width: 220px; padding: 14px 16px;
    background: #f5f5f5; border-left: 1px solid #ddd;
    overflow-y: auto; max-height: 100vh; box-sizing: border-box;
  }}
  .controls h3 {{
    margin: 0 0 12px 0; font-size: 14px; color: #333;
    border-bottom: 2px solid #999; padding-bottom: 6px;
  }}
  .ctrl-group {{
    margin-bottom: 10px;
  }}
  .ctrl-group label {{
    display: block; font-size: 11px; color: #666;
    margin-bottom: 3px; font-weight: 600; text-transform: uppercase;
    letter-spacing: 0.5px;
  }}
  .ctrl-group select, .ctrl-group input[type=range] {{
    width: 100%; box-sizing: border-box; font-size: 12px;
    padding: 4px 6px; border: 1px solid #ccc; border-radius: 3px;
    background: white;
  }}
  .ctrl-group input[type=color] {{
    width: 100%; height: 28px; border: 1px solid #ccc;
    border-radius: 3px; cursor: pointer; padding: 2px;
  }}
  .ctrl-group .val-display {{
    font-size: 10px; color: #888; text-align: right; margin-top: 1px;
  }}
  hr.sep {{ border: none; border-top: 1px solid #ddd; margin: 12px 0; }}
</style>
</head><body>
<div class="container">
  <div class="plot-area">{plot_div}</div>
  <div class="controls">
    <h3>Display Controls</h3>

    {'<div class="ctrl-group"><label>Label Font Size</label><input type="range" id="labelSize" min="6" max="20" value="10" step="1"><div class="val-display" id="labelSizeVal">10pt</div></div>' if has_annotations else ''}

    <div class="ctrl-group">
      <label>Title Font Size</label>
      <input type="range" id="titleSize" min="10" max="28" value="16" step="1">
      <div class="val-display" id="titleSizeVal">16pt</div>
    </div>

    <div class="ctrl-group">
      <label>Subtitle Font Size</label>
      <input type="range" id="subtitleSize" min="8" max="22" value="12" step="1">
      <div class="val-display" id="subtitleSizeVal">12pt</div>
    </div>

    <div class="ctrl-group">
      <label>Axis Label Size</label>
      <input type="range" id="axisSize" min="8" max="22" value="14" step="1">
      <div class="val-display" id="axisSizeVal">14pt</div>
    </div>

    <div class="ctrl-group">
      <label>Group Label Size (X-axis)</label>
      <input type="range" id="xTickSize" min="6" max="24" value="12" step="1">
      <div class="val-display" id="xTickSizeVal">12pt</div>
    </div>

    <div class="ctrl-group">
      <label>miRNA Label Size (Y-axis)</label>
      <input type="range" id="yTickSize" min="6" max="24" value="9" step="1">
      <div class="val-display" id="yTickSizeVal">9pt</div>
    </div>

    <div class="ctrl-group">
      <label>X-Axis Title Offset</label>
      <input type="range" id="xTitleStandoff" min="0" max="40" value="15" step="2">
      <div class="val-display" id="xTitleStandoffVal">15px</div>
    </div>

    <div class="ctrl-group">
      <label>Y-Axis Title Offset</label>
      <input type="range" id="yTitleStandoff" min="0" max="80" value="40" step="2">
      <div class="val-display" id="yTitleStandoffVal">40px</div>
    </div>

    {'<hr class="sep">' if has_annotations else ''}

    {'<div class="ctrl-group"><label>Arrow Size</label><input type="range" id="arrowSize" min="0.5" max="4" value="1" step="0.25"><div class="val-display" id="arrowSizeVal">1x</div></div>' if has_annotations else ''}

    {'<div class="ctrl-group"><label>Arrow Width</label><input type="range" id="arrowWidth" min="0.5" max="4" value="1" step="0.5"><div class="val-display" id="arrowWidthVal">1px</div></div>' if has_annotations else ''}

    {'<div class="ctrl-group"><label>Arrowhead Style</label><select id="arrowHead"><option value="0">None</option><option value="1">Thin</option><option value="2" selected>Arrow</option><option value="3">Barbed</option><option value="4">Wide</option><option value="5">Diamond</option><option value="6">Dot</option><option value="7">Open arrow</option></select></div>' if has_annotations else ''}

    {'<div class="ctrl-group"><label>Arrow Color</label><input type="color" id="arrowColor" value="#808080"></div>' if has_annotations else ''}

    {'<div class="ctrl-group"><label>Label Text Color</label><input type="color" id="labelColor" value="#000000"></div>' if has_annotations else ''}

    <div class="ctrl-group">
      <label>Title Text Color</label>
      <input type="color" id="titleColor" value="#000000">
    </div>

    <div class="ctrl-group">
      <label>All Text Color</label>
      <input type="color" id="allTextColor" value="#000000">
    </div>

    <hr class="sep">

    <div class="ctrl-group">
      <label>Colorbar Tick Size</label>
      <input type="range" id="cbarTickSize" min="6" max="22" value="12" step="1">
      <div class="val-display" id="cbarTickSizeVal">12pt</div>
    </div>

    <div class="ctrl-group">
      <label>Colorbar Title Size</label>
      <input type="range" id="cbarTitleSize" min="8" max="24" value="14" step="1">
      <div class="val-display" id="cbarTitleSizeVal">14pt</div>
    </div>

    <div class="ctrl-group">
      <label>Colorbar X Position</label>
      <input type="range" id="cbarX" min="0.8" max="1.2" value="1.02" step="0.01">
      <div class="val-display" id="cbarXVal">1.02</div>
    </div>

    <div class="ctrl-group">
      <label>Colorbar Y Position</label>
      <input type="range" id="cbarY" min="0.0" max="1.0" value="0.5" step="0.05">
      <div class="val-display" id="cbarYVal">0.5</div>
    </div>

    <hr class="sep">

    <div class="ctrl-group">
      <label>Title Position</label>
      <select id="titlePos">
        <option value="0">Left</option>
        <option value="0.5" selected>Center</option>
        <option value="1">Right</option>
      </select>
    </div>

    <div class="ctrl-group">
      <label>Title Y Position</label>
      <input type="range" id="titleY" min="0.85" max="1.15" value="0.98" step="0.01">
      <div class="val-display" id="titleYVal">0.98</div>
    </div>

    <div class="ctrl-group">
      <label>Legend Font Size</label>
      <input type="range" id="legendSize" min="8" max="18" value="12" step="1">
      <div class="val-display" id="legendSizeVal">12pt</div>
    </div>

    <hr class="sep">

    <div class="ctrl-group">
      <label>Edit Plot Title</label>
      <textarea id="titleText" rows="3" style="width:100%;box-sizing:border-box;font-size:12px;padding:4px 6px;border:1px solid #ccc;border-radius:3px;resize:vertical;"></textarea>
      <button id="titleApply" style="margin-top:4px;width:100%;padding:5px;font-size:12px;cursor:pointer;border:1px solid #aaa;border-radius:3px;background:#e8e8e8;">Apply Title</button>
    </div>

    <div class="ctrl-group">
      <label>Edit Subtitle</label>
      <textarea id="subtitleText" rows="2" style="width:100%;box-sizing:border-box;font-size:11px;padding:4px 6px;border:1px solid #ccc;border-radius:3px;resize:vertical;"></textarea>
      <button id="subtitleApply" style="margin-top:4px;width:100%;padding:5px;font-size:12px;cursor:pointer;border:1px solid #aaa;border-radius:3px;background:#e8e8e8;">Apply Subtitle</button>
    </div>

    <hr class="sep">

    <div class="ctrl-group">
      <label>Export Resolution</label>
      <select id="exportScale">
        <option value="1">1x (standard)</option>
        <option value="2">2x (high)</option>
        <option value="3" selected>3x (publication)</option>
        <option value="4">4x (poster)</option>
        <option value="5">5x (max)</option>
      </select>
    </div>

    <div class="ctrl-group">
      <label>Export Width (px)</label>
      <input type="number" id="exportWidth" value="1800" min="400" max="6000" step="100"
             style="width:100%;box-sizing:border-box;font-size:12px;padding:4px 6px;border:1px solid #ccc;border-radius:3px;">
    </div>

    <div class="ctrl-group">
      <label>Export Height (px)</label>
      <input type="number" id="exportHeight" value="1300" min="300" max="5000" step="100"
             style="width:100%;box-sizing:border-box;font-size:12px;padding:4px 6px;border:1px solid #ccc;border-radius:3px;">
    </div>

    <div class="ctrl-group">
      <button id="exportPNG" style="width:100%;padding:8px;font-size:13px;cursor:pointer;border:1px solid #27ae60;border-radius:4px;background:#2ecc71;color:white;font-weight:bold;">Export PNG</button>
    </div>

    <div class="ctrl-group">
      <button id="exportSVG" style="width:100%;padding:8px;font-size:13px;cursor:pointer;border:1px solid #2980b9;border-radius:4px;background:#3498db;color:white;font-weight:bold;">Export SVG</button>
    </div>
  </div>
</div>

<script>
var gd = document.getElementById('{div_id}');

// Helper: update only miRNA label annotations (those with showarrow=true and font)
function updateAnnotProp(prop, value) {{
  var annots = gd.layout.annotations;
  var update = {{}};
  for (var i = 0; i < annots.length; i++) {{
    if (annots[i].showarrow && annots[i].font) {{
      update['annotations[' + i + '].' + prop] = value;
    }}
  }}
  Plotly.relayout(gd, update);
}}

// Slider helpers
function bindSlider(id, valId, suffix, callback) {{
  var el = document.getElementById(id);
  var valEl = document.getElementById(valId);
  if (!el) return;
  el.addEventListener('input', function() {{
    if (valEl) valEl.textContent = el.value + suffix;
    callback(parseFloat(el.value));
  }});
}}

if (document.getElementById('labelSize')) {{
  bindSlider('labelSize', 'labelSizeVal', 'pt', function(v) {{
    updateAnnotProp('font.size', v);
  }});
}}

bindSlider('titleSize', 'titleSizeVal', 'pt', function(v) {{
  Plotly.relayout(gd, {{'title.font.size': v}});
}});

bindSlider('axisSize', 'axisSizeVal', 'pt', function(v) {{
  Plotly.relayout(gd, {{
    'xaxis.title.font.size': v,
    'yaxis.title.font.size': v
  }});
}});

bindSlider('xTickSize', 'xTickSizeVal', 'pt', function(v) {{
  Plotly.relayout(gd, {{
    'xaxis.tickfont.size': v,
    'xaxis.automargin': false,
    'margin.b': Math.max(60, v * 4 + 20)
  }});
}});

bindSlider('yTickSize', 'yTickSizeVal', 'pt', function(v) {{
  var estLabelWidth = v * 0.6 * 15 + 50;
  var newMargin = Math.max(140, Math.ceil(estLabelWidth));
  var nTicks = (gd.data[0] && gd.data[0].y) ? gd.data[0].y.length : 60;
  var newHeight = Math.max(700, nTicks * (v * 1.4 + 2) + 160);
  Plotly.relayout(gd, {{
    'yaxis.tickfont.size': v,
    'yaxis.dtick': 1,
    'yaxis.automargin': false,
    'margin.l': newMargin,
    'height': newHeight
  }});
}});

bindSlider('xTitleStandoff', 'xTitleStandoffVal', 'px', function(v) {{
  Plotly.relayout(gd, {{'xaxis.title.standoff': v}});
}});

bindSlider('yTitleStandoff', 'yTitleStandoffVal', 'px', function(v) {{
  Plotly.relayout(gd, {{'yaxis.title.standoff': v}});
}});

bindSlider('subtitleSize', 'subtitleSizeVal', 'pt', function(v) {{
  // Update subtitle size by modifying the <sub> tag style in the title
  var titleEl = gd.layout.title;
  var currentText = (titleEl && titleEl.text) ? titleEl.text : '';
  // Replace any existing font-size style in <sub>, or add one
  var newText = currentText.replace(
    /<sub[^>]*>/,
    '<sub style="font-size:' + v + 'px">'
  );
  // If there was no <sub> tag with style, try plain <sub>
  if (newText === currentText && currentText.indexOf('<sub>') >= 0) {{
    newText = currentText.replace('<sub>', '<sub style="font-size:' + v + 'px">');
  }}
  if (newText !== currentText) {{
    Plotly.relayout(gd, {{'title.text': newText}});
  }}
  // Also update the subtitle textarea to reflect
  var parts = newText.split('<br>');
  if (parts.length > 1) {{
    var sub = parts.slice(1).join('<br>').replace(/<sub[^>]*>/g,'').replace(/<\/sub>/g,'');
    var subEl = document.getElementById('subtitleText');
    if (subEl) subEl.value = sub;
  }}
}});

if (document.getElementById('arrowSize')) {{
  bindSlider('arrowSize', 'arrowSizeVal', 'x', function(v) {{
    updateAnnotProp('arrowsize', v);
  }});
  bindSlider('arrowWidth', 'arrowWidthVal', 'px', function(v) {{
    updateAnnotProp('arrowwidth', v);
  }});
  document.getElementById('arrowHead').addEventListener('change', function() {{
    updateAnnotProp('arrowhead', parseInt(this.value));
  }});
  document.getElementById('arrowColor').addEventListener('input', function() {{
    updateAnnotProp('arrowcolor', this.value);
  }});
}}

document.getElementById('titlePos').addEventListener('change', function() {{
  Plotly.relayout(gd, {{'title.x': parseFloat(this.value)}});
}});

bindSlider('titleY', 'titleYVal', '', function(v) {{
  Plotly.relayout(gd, {{'title.y': v, 'title.yanchor': 'top'}});
}});

bindSlider('legendSize', 'legendSizeVal', 'pt', function(v) {{
  Plotly.relayout(gd, {{'legend.font.size': v}});
}});

if (document.getElementById('labelColor')) {{
  document.getElementById('labelColor').addEventListener('input', function() {{
    updateAnnotProp('font.color', this.value);
  }});
}}

document.getElementById('titleColor').addEventListener('input', function() {{
  Plotly.relayout(gd, {{'title.font.color': this.value}});
}});

bindSlider('cbarTickSize', 'cbarTickSizeVal', 'pt', function(v) {{
  // Update colorbar tick font size on first trace
  if (gd.data.length > 0 && gd.data[0].colorbar) {{
    Plotly.restyle(gd, {{'colorbar.tickfont.size': v}}, [0]);
  }}
}});

bindSlider('cbarTitleSize', 'cbarTitleSizeVal', 'pt', function(v) {{
  if (gd.data.length > 0 && gd.data[0].colorbar) {{
    Plotly.restyle(gd, {{'colorbar.title.font.size': v}}, [0]);
  }}
}});

bindSlider('cbarX', 'cbarXVal', '', function(v) {{
  if (gd.data.length > 0 && gd.data[0].colorbar) {{
    Plotly.restyle(gd, {{'colorbar.x': v}}, [0]);
  }}
}});

bindSlider('cbarY', 'cbarYVal', '', function(v) {{
  if (gd.data.length > 0 && gd.data[0].colorbar) {{
    Plotly.restyle(gd, {{'colorbar.y': v}}, [0]);
  }}
}});

document.getElementById('allTextColor').addEventListener('input', function() {{
  var c = this.value;
  // Update label annotations
  updateAnnotProp('font.color', c);
  // Update title, axis titles, axis ticks, legend
  Plotly.relayout(gd, {{
    'title.font.color': c,
    'xaxis.title.font.color': c,
    'yaxis.title.font.color': c,
    'xaxis.tickfont.color': c,
    'yaxis.tickfont.color': c,
    'legend.font.color': c
  }});
  // Sync the individual pickers
  if (document.getElementById('labelColor')) document.getElementById('labelColor').value = c;
  document.getElementById('titleColor').value = c;
}});

// Populate title fields from current plot
var currentTitle = gd.layout.title.text || '';
var parts = currentTitle.split('<br>');
var mainTitle = parts[0] || '';
var subTitle = '';
if (parts.length > 1) {{
  subTitle = parts.slice(1).join('<br>').replace(/<sub>/g,'').replace(/<\/sub>/g,'');
}}
document.getElementById('titleText').value = mainTitle;
document.getElementById('subtitleText').value = subTitle;

document.getElementById('titleApply').addEventListener('click', function() {{
  var main = document.getElementById('titleText').value;
  var sub = document.getElementById('subtitleText').value;
  var full = main;
  if (sub) full += '<br><sub>' + sub + '</sub>';
  Plotly.relayout(gd, {{'title.text': full}});
}});

document.getElementById('subtitleApply').addEventListener('click', function() {{
  var main = document.getElementById('titleText').value;
  var sub = document.getElementById('subtitleText').value;
  var full = main;
  if (sub) full += '<br><sub>' + sub + '</sub>';
  Plotly.relayout(gd, {{'title.text': full}});
}});

function exportPlot(format) {{
  var scale = parseFloat(document.getElementById('exportScale').value);
  var w = parseInt(document.getElementById('exportWidth').value);
  var h = parseInt(document.getElementById('exportHeight').value);

  // Save current layout state
  var layout = gd.layout;
  var origWidth = layout.width;
  var origHeight = layout.height;

  var saved = {{
    titleSize: (layout.title && layout.title.font) ? layout.title.font.size : 16,
    xTitleSize: (layout.xaxis && layout.xaxis.title && layout.xaxis.title.font) ? layout.xaxis.title.font.size : 14,
    yTitleSize: (layout.yaxis && layout.yaxis.title && layout.yaxis.title.font) ? layout.yaxis.title.font.size : 14,
    xTickSize: (layout.xaxis && layout.xaxis.tickfont) ? layout.xaxis.tickfont.size : 12,
    yTickSize: (layout.yaxis && layout.yaxis.tickfont) ? layout.yaxis.tickfont.size : 12,
    legendSize: (layout.legend && layout.legend.font) ? layout.legend.font.size : 12,
    markerSize: (gd.data[0] && gd.data[0].marker) ? gd.data[0].marker.size : 5,
    annots: []
  }};
  var annots = layout.annotations || [];
  for (var i = 0; i < annots.length; i++) {{
    saved.annots.push({{
      fontSize: annots[i].font ? annots[i].font.size : null,
      arrowwidth: annots[i].arrowwidth != null ? annots[i].arrowwidth : 1,
      arrowsize: annots[i].arrowsize != null ? annots[i].arrowsize : 1,
      ay: annots[i].ay != null ? annots[i].ay : -30
    }});
  }}

  var s = (format === 'svg') ? 1 : scale;

  // Build scaled layout
  var upd = {{
    'width': w * s,
    'height': h * s,
    'title.font.size': saved.titleSize * s,
    'xaxis.title.font.size': saved.xTitleSize * s,
    'yaxis.title.font.size': saved.yTitleSize * s,
    'xaxis.tickfont.size': saved.xTickSize * s,
    'yaxis.tickfont.size': saved.yTickSize * s,
    'legend.font.size': saved.legendSize * s,
    'margin.l': (layout.margin ? layout.margin.l || 80 : 80) * s,
    'margin.r': (layout.margin ? layout.margin.r || 80 : 80) * s,
    'margin.t': (layout.margin ? layout.margin.t || 100 : 100) * s,
    'margin.b': (layout.margin ? layout.margin.b || 80 : 80) * s
  }};
  for (var i = 0; i < annots.length; i++) {{
    if (saved.annots[i].fontSize) {{
      upd['annotations[' + i + '].font.size'] = saved.annots[i].fontSize * s;
    }}
    upd['annotations[' + i + '].arrowwidth'] = saved.annots[i].arrowwidth * s;
    upd['annotations[' + i + '].arrowsize'] = saved.annots[i].arrowsize;
    upd['annotations[' + i + '].ay'] = saved.annots[i].ay * s;
  }}

  // Also scale marker sizes in data traces
  var traceUpdates = [];
  for (var t = 0; t < gd.data.length; t++) {{
    traceUpdates.push({{'marker.size': (gd.data[t].marker ? gd.data[t].marker.size || 5 : 5) * s}});
  }}

  // Disable editable during export to avoid interference
  Plotly.relayout(gd, upd).then(function() {{
    var restyle = [];
    for (var t = 0; t < traceUpdates.length; t++) {{
      restyle.push(Plotly.restyle(gd, traceUpdates[t], [t]));
    }}
    return Promise.all(restyle);
  }}).then(function() {{
    // Use toImage to get data URL, then trigger download
    return Plotly.toImage(gd, {{
      format: format,
      width: w * s,
      height: h * s
    }});
  }}).then(function(dataUrl) {{
    // Create download link
    var a = document.createElement('a');
    a.href = dataUrl;
    a.download = '{default_filename}.' + format;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);

    // Restore everything
    var restore = {{
      'width': origWidth,
      'height': origHeight,
      'title.font.size': saved.titleSize,
      'xaxis.title.font.size': saved.xTitleSize,
      'yaxis.title.font.size': saved.yTitleSize,
      'xaxis.tickfont.size': saved.xTickSize,
      'yaxis.tickfont.size': saved.yTickSize,
      'legend.font.size': saved.legendSize,
      'margin.l': layout.margin ? layout.margin.l : 80,
      'margin.r': layout.margin ? layout.margin.r : 80,
      'margin.t': layout.margin ? layout.margin.t : 100,
      'margin.b': layout.margin ? layout.margin.b : 80
    }};
    for (var i = 0; i < annots.length; i++) {{
      if (saved.annots[i].fontSize) {{
        restore['annotations[' + i + '].font.size'] = saved.annots[i].fontSize;
      }}
      restore['annotations[' + i + '].arrowwidth'] = saved.annots[i].arrowwidth;
      restore['annotations[' + i + '].arrowsize'] = saved.annots[i].arrowsize;
      restore['annotations[' + i + '].ay'] = saved.annots[i].ay;
    }}
    return Plotly.relayout(gd, restore);
  }}).then(function() {{
    var restoreTraces = [];
    for (var t = 0; t < gd.data.length; t++) {{
      var origSize = gd.data[t].marker ? gd.data[t].marker.size / s : 5;
      restoreTraces.push(Plotly.restyle(gd, {{'marker.size': origSize}}, [t]));
    }}
    return Promise.all(restoreTraces);
  }});
}}

document.getElementById('exportPNG').addEventListener('click', function() {{
  exportPlot('png');
}});

document.getElementById('exportSVG').addEventListener('click', function() {{
  exportPlot('svg');
}});
</script>
</body></html>"""

    with open(filepath, 'w') as f:
        f.write(html)


def create_all_volcano_plots(comparisons, output_dir):
    """Create volcano plots for all comparisons in a single HTML."""
    from plotly.subplots import make_subplots

    figs = {}
    for comp_name, comp_df in comparisons.items():
        comp_df = comp_df.copy()
        # Cells_vs_Organs has group1=Organs, group2=Cells (reversed)
        if comp_name == 'Cells_vs_Organs':
            comp_df['log2FC'] = -comp_df['log2FC']
        fig = create_volcano_plot(comp_df, comp_name)
        figs[comp_name] = fig
        _write_interactive_html(fig, os.path.join(output_dir, f'volcano_{comp_name}.html'),
                                has_annotations=True, default_filename=f'volcano_{comp_name}')

    # Combined with dropdown
    combined = go.Figure()
    comp_names = list(comparisons.keys())

    for i, (comp_name, comp_df) in enumerate(comparisons.items()):
        df = comp_df.dropna(subset=['log2FC', 'padj']).copy()
        df = df[df['padj'] > 0]
        if comp_name == 'Cells_vs_Organs':
            df['log2FC'] = -df['log2FC']
        df['neg_log10_padj'] = -np.log10(df['padj'])

        conditions = [
            (df['padj'] <= 0.05) & (df['log2FC'] >= 1.0),
            (df['padj'] <= 0.05) & (df['log2FC'] <= -1.0),
        ]
        choices = ['Up', 'Down']
        df['category'] = np.select(conditions, choices, default='NS')

        color_map = {'Up': '#e74c3c', 'Down': '#3498db', 'NS': '#d5d8dc'}
        visible = (i == 0)

        for cat in ['NS', 'Down', 'Up']:
            subset = df[df['category'] == cat]
            if len(subset) == 0:
                continue
            combined.add_trace(go.Scattergl(
                x=subset['log2FC'],
                y=subset['neg_log10_padj'],
                mode='markers',
                name=f'{cat} ({len(subset)})',
                marker=dict(color=color_map[cat], size=5, opacity=0.7),
                text=subset['GeneID'],
                hovertemplate='<b>%{text}</b><br>log2FC: %{x:.3f}<br>-log10(FDR): %{y:.2f}<extra></extra>',
                visible=visible,
            ))

    # Build visibility toggles for dropdown
    traces_per_comp = []
    idx = 0
    for comp_name, comp_df in comparisons.items():
        df = comp_df.dropna(subset=['log2FC', 'padj']).copy()
        df = df[df['padj'] > 0]
        if comp_name == 'Cells_vs_Organs':
            df['log2FC'] = -df['log2FC']
        conditions = [
            (df['padj'] <= 0.05) & (df['log2FC'] >= 1.0),
            (df['padj'] <= 0.05) & (df['log2FC'] <= -1.0),
        ]
        df['category'] = np.select(conditions, ['Up', 'Down'], default='NS')
        n_cats = sum(1 for cat in ['NS', 'Down', 'Up'] if (df['category'] == cat).sum() > 0)
        traces_per_comp.append(n_cats)

    total_traces = sum(traces_per_comp)
    buttons = []
    offset = 0
    for i, comp_name in enumerate(comp_names):
        vis = [False] * total_traces
        for j in range(traces_per_comp[i]):
            vis[offset + j] = True
        offset += traces_per_comp[i]
        pretty = comp_name.replace('_', ' ').replace('vs', 'vs.')
        buttons.append(dict(label=pretty, method='update',
                            args=[{'visible': vis},
                                  {'title': f'Volcano Plot: {pretty}'}]))

    combined.update_layout(
        updatemenus=[dict(buttons=buttons, direction='down',
                          x=0.01, xanchor='left', y=1.15, yanchor='top')],
        title='Volcano Plot: ' + comp_names[0].replace('_', ' ').replace('vs', 'vs.'),
        xaxis_title='log2(Fold Change)',
        yaxis_title='-log10(FDR)',
        template='plotly_white',
        width=900, height=650,
    )
    combined.write_html(os.path.join(output_dir, 'volcano_all_comparisons.html'))
    return figs


# =============================================================================
# 3. INTERACTIVE HEATMAP
# =============================================================================

def create_heatmap(group_avg, genes, comparisons, output_dir, top_n=50):
    """Create an interactive heatmap of top DE miRNAs across all groups."""
    # Select top DE miRNAs: those with highest DIFF count and highest fold change
    gene_info = genes[genes['DIFF'] > 0].copy()
    gene_info = gene_info.sort_values(['DIFF', 'MaxLog2FC'], ascending=[False, False])
    top_genes = gene_info.head(top_n)['GeneID'].tolist()

    avg_cols = ['avg_Cells', 'avg_He', 'avg_Ki', 'avg_Li', 'avg_Lu', 'avg_Sp']
    display_names = ['NIH 4T1 Cells', 'Heart', 'Kidney', 'Liver', 'Lung', 'Spleen']

    heatmap_data = group_avg[group_avg['GeneID'].isin(top_genes)].copy()
    heatmap_data = heatmap_data.set_index('GeneID')

    # Log2 transform (add pseudocount)
    expr = heatmap_data[avg_cols] + 1
    log2_expr = np.log2(expr)

    # Z-score normalize per gene (row)
    z_scores = log2_expr.subtract(log2_expr.mean(axis=1), axis=0).divide(log2_expr.std(axis=1), axis=0)
    z_scores.columns = display_names

    # Reorder by clustering-like sort: group by max expression group
    z_scores['max_group'] = z_scores.idxmax(axis=1)
    group_order = ['NIH 4T1 Cells', 'Heart', 'Kidney', 'Liver', 'Lung', 'Spleen']
    z_scores['sort_key'] = z_scores['max_group'].map({g: i for i, g in enumerate(group_order)})
    z_scores = z_scores.sort_values(['sort_key', 'max_group'])
    z_scores = z_scores.drop(columns=['max_group', 'sort_key'])

    # Build hover text with raw counts
    raw_for_hover = heatmap_data.loc[z_scores.index, avg_cols]
    raw_for_hover.columns = display_names
    hover_text = []
    for gene in z_scores.index:
        row = []
        for grp in display_names:
            row.append(f'{gene}<br>{grp}<br>Z-score: {z_scores.loc[gene, grp]:.2f}<br>Avg count: {raw_for_hover.loc[gene, grp]:.0f}')
        hover_text.append(row)

    fig = go.Figure(data=go.Heatmap(
        z=z_scores.values,
        x=display_names,
        y=[g.replace('mmu-', '') for g in z_scores.index],
        colorscale='RdBu_r',
        zmid=0,
        text=hover_text,
        hoverinfo='text',
        colorbar=dict(title='Z-score'),
    ))

    fig.update_layout(
        title=dict(
            text=f'Top {len(z_scores)} Differentially Expressed miRNAs (Z-score normalized)',
            font=dict(size=16),
            x=0.5,
            xanchor='center',
        ),
        xaxis=dict(title='Group', automargin=False,
                    showgrid=False, showline=True, linecolor='#ccc'),
        yaxis=dict(title='miRNA', tickfont=dict(size=9), automargin=False,
                    showgrid=False, showline=True, linecolor='#ccc',
                    dtick=1),
        template=None,
        plot_bgcolor='white',
        paper_bgcolor='white',
        width=900,
        height=max(700, len(z_scores) * 20),
        margin=dict(l=160, b=80, t=80),
        legend=dict(font=dict(size=12)),
    )
    _write_interactive_html(fig, os.path.join(output_dir, 'heatmap_top_DE_miRNAs.html'),
                            has_annotations=False, default_filename='heatmap_top_DE_miRNAs')
    return fig


# =============================================================================
# 4. GROUP-SPECIFIC BIOMARKER IDENTIFICATION
# =============================================================================

def identify_biomarkers(comparisons, group_avg, sample_counts, fdr_cutoff=0.05, fc_cutoff=1.0, min_count=10):
    """
    Identify group-specific biomarker miRNAs.

    A group-specific biomarker is a miRNA that is:
    1. Significantly DE (FDR < cutoff) in the one-vs-rest comparison
    2. Has |log2FC| > fc_cutoff
    3. Has sufficient expression (min_count in at least one group)

    Returns a dict of DataFrames, one per group.
    """
    group_map = {
        'He_vs_nonHe': ('Heart', 'avg_He'),
        'Ki_vs_nonKi': ('Kidney', 'avg_Ki'),
        'Li_vs_nonLi': ('Liver', 'avg_Li'),
        'Lu_vs_nonLu': ('Lung', 'avg_Lu'),
        'Sp_vs_nonSp': ('Spleen', 'avg_Sp'),
        'Cells_vs_Organs': ('Cells (4T1)', 'avg_Cells'),
    }

    # Sample groupings for CV calculation
    sample_groups = {
        'Cells (4T1)': ['4T1.1', '4T1.2', '4T1.3'],
        'Heart': ['He.4', 'He.5'],
        'Kidney': ['Ki.4', 'Ki.5'],
        'Liver': ['Li.4', 'Li.5', 'Li.3'],
        'Lung': ['Lu.4', 'Lu.5', 'Lu.3'],
        'Spleen': ['Sp.4', 'Sp.5', 'Sp.3'],
    }

    biomarkers = {}

    for comp_name, (group_label, avg_col) in group_map.items():
        df = comparisons[comp_name].copy()
        df = df.dropna(subset=['padj', 'log2FC'])

        # Cells_vs_Organs has group1=Organs, group2=Cells (reversed),
        # so flip the fold change to make positive = up in Cells
        if comp_name == 'Cells_vs_Organs':
            df['log2FC'] = -df['log2FC']

        # Filter for significant with sufficient FC
        mask = (df['padj'] <= fdr_cutoff) & (df['abs_log2FC'] >= fc_cutoff)

        # Filter for minimum expression
        # For upregulated markers: require sufficient expression in the target group
        # For downregulated markers: require sufficient expression in other groups
        #   (absence in the target group is the signal)
        avg_data = group_avg.set_index('GeneID')
        other_avg_cols = [c for c in ['avg_Cells', 'avg_He', 'avg_Ki', 'avg_Li', 'avg_Lu', 'avg_Sp']
                          if c != avg_col]

        def passes_min_count(gene, log2fc):
            if gene not in avg_data.index:
                return False
            if log2fc > 0:
                return avg_data.loc[gene, avg_col] >= min_count
            else:
                return avg_data.loc[gene, other_avg_cols].max() >= min_count

        mask_count = df.apply(lambda r: passes_min_count(r['GeneID'], r['log2FC']), axis=1)
        mask = mask & mask_count

        sig_df = df[mask].copy()

        # Add group average expression
        sig_df = sig_df.merge(group_avg[['GeneID', 'baseMean', avg_col]], on='GeneID', how='left')

        # Calculate specificity score: ratio of group avg to overall baseMean
        sig_df['specificity'] = sig_df[avg_col] / (sig_df['baseMean'] + 1)

        # Direction
        sig_df['direction'] = np.where(sig_df['log2FC'] > 0, 'UP in ' + group_label, 'DOWN in ' + group_label)

        # Calculate CV within the group
        cvs = []
        for gene in sig_df['GeneID']:
            samples = sample_groups[group_label]
            vals = sample_counts[sample_counts['GeneID'] == gene][samples].values.flatten()
            vals = vals[~np.isnan(vals)]
            if len(vals) > 1 and np.mean(vals) > 0:
                cvs.append(np.std(vals) / np.mean(vals))
            else:
                cvs.append(np.nan)
        sig_df['CV'] = cvs

        # Biomarker score: combine significance, fold change, and specificity
        sig_df['biomarker_score'] = (
            -np.log10(sig_df['padj'] + 1e-300) *
            sig_df['abs_log2FC'] *
            np.clip(sig_df['specificity'], 0, 10)
        )

        sig_df = sig_df.sort_values('biomarker_score', ascending=False)
        biomarkers[group_label] = sig_df

    return biomarkers


def create_biomarker_summary(biomarkers, output_dir):
    """Create summary table and export to CSV."""
    all_markers = []
    for group, df in biomarkers.items():
        top = df.head(20).copy()
        top['Group'] = group
        all_markers.append(top)

    summary = pd.concat(all_markers, ignore_index=True)
    cols = ['Group', 'GeneID', 'log2FC', 'padj', 'avg_group1', 'avg_group2',
            'direction', 'specificity', 'CV', 'biomarker_score']
    summary = summary[[c for c in cols if c in summary.columns]]
    summary.to_csv(os.path.join(output_dir, 'biomarker_candidates.csv'), index=False)
    return summary


def create_group_summary_tables(biomarkers, group_avg, output_dir, top_n=10):
    """
    Create per-group summary tables (top N up and top N down) with
    average counts and z-scores across all groups, exported to CSV.
    """
    avg_cols = ['avg_Cells', 'avg_He', 'avg_Ki', 'avg_Li', 'avg_Lu', 'avg_Sp']
    display_names = ['Cells (4T1)', 'Heart', 'Kidney', 'Liver', 'Lung', 'Spleen']

    avg_data = group_avg.set_index('GeneID')

    # Compute z-scores for all genes
    log2_expr = np.log2(avg_data[avg_cols] + 1)
    z_all = log2_expr.subtract(log2_expr.mean(axis=1), axis=0).divide(log2_expr.std(axis=1), axis=0)
    z_all.columns = [f'zscore_{n}' for n in display_names]

    # Rename avg columns for clarity
    count_rename = {c: f'count_{n}' for c, n in zip(avg_cols, display_names)}

    all_tables = []
    for group, df in biomarkers.items():
        for direction in ['up', 'down']:
            if direction == 'up':
                hits = df[df['log2FC'] > 0].head(top_n)
            else:
                hits = df[df['log2FC'] < 0].head(top_n)

            if len(hits) == 0:
                continue

            rows = []
            for _, row in hits.iterrows():
                gene = row['GeneID']
                if gene not in avg_data.index:
                    continue
                entry = {
                    'Group': group,
                    'Direction': 'Upregulated' if direction == 'up' else 'Downregulated',
                    'miRNA': gene.replace('mmu-', ''),
                    'GeneID': gene,
                    'log2FC': row['log2FC'],
                    'padj': row['padj'],
                    'biomarker_score': row['biomarker_score'],
                }
                for col, name in zip(avg_cols, display_names):
                    entry[f'count_{name}'] = avg_data.loc[gene, col]
                    entry[f'zscore_{name}'] = z_all.loc[gene, f'zscore_{name}']
                rows.append(entry)

            all_tables.extend(rows)

    result = pd.DataFrame(all_tables)
    result.to_csv(os.path.join(output_dir, 'biomarker_summary_tables.csv'), index=False)
    return result


# =============================================================================
# 5. EXPRESSION PROFILE PLOTS
# =============================================================================

def create_expression_dotplot(biomarkers, group_avg, output_dir, top_per_group=10,
                             direction='up'):
    """
    Create an interactive dot plot showing expression of top biomarkers across groups.
    Dot size = expression level, color = z-score.

    Parameters
    ----------
    direction : str
        'up' to select upregulated biomarkers (log2FC > 0),
        'down' to select downregulated biomarkers (log2FC < 0).
    """
    avg_cols = ['avg_Cells', 'avg_He', 'avg_Ki', 'avg_Li', 'avg_Lu', 'avg_Sp']
    display_names = ['Cells (4T1)', 'Heart', 'Kidney', 'Liver', 'Lung', 'Spleen']

    # Collect top biomarkers per group in the requested direction
    selected_genes = []
    gene_groups = []
    for group, df in biomarkers.items():
        if direction == 'up':
            hits = df[df['log2FC'] > 0].head(top_per_group)
        else:
            hits = df[df['log2FC'] < 0].head(top_per_group)
        for g in hits['GeneID']:
            if g not in selected_genes:
                selected_genes.append(g)
                gene_groups.append(group)

    if not selected_genes:
        return None

    # Get expression data
    expr_data = group_avg[group_avg['GeneID'].isin(selected_genes)].copy()
    expr_data = expr_data.set_index('GeneID')
    expr_data = expr_data.loc[[g for g in selected_genes if g in expr_data.index]]

    log2_expr = np.log2(expr_data[avg_cols] + 1)
    z_scores = log2_expr.subtract(log2_expr.mean(axis=1), axis=0).divide(log2_expr.std(axis=1), axis=0)

    # Build the dot plot
    fig = go.Figure()

    genes_display = [g.replace('mmu-', '') for g in expr_data.index]
    for j, (col, name) in enumerate(zip(avg_cols, display_names)):
        sizes = np.log2(expr_data[col].values + 1)
        sizes = np.clip(sizes * 2, 3, 30)  # scale for visibility

        fig.add_trace(go.Scatter(
            x=[name] * len(genes_display),
            y=genes_display,
            mode='markers',
            name=name,
            marker=dict(
                size=sizes,
                color=z_scores.iloc[:, j].values,
                colorscale='RdBu_r',
                cmid=0,
                cmin=-3, cmax=3,
                showscale=(j == 0),
                colorbar=dict(
                    title=dict(text='Z-score', font=dict(size=13), side='top'),
                    tickfont=dict(size=11),
                    len=0.4,
                    thickness=15,
                    x=1.02,
                    y=1.0,
                    yanchor='top',
                ) if j == 0 else None,
                line=dict(width=0.5, color='black'),
                opacity=0.85,
            ),
            customdata=np.stack([
                expr_data[col].values,
                z_scores.iloc[:, j].values,
            ], axis=-1),
            hovertemplate=(
                '<b>%{y}</b> in %{x}<br>'
                'Avg count: %{customdata[0]:.0f}<br>'
                'Z-score: %{customdata[1]:.2f}<br>'
                '<extra></extra>'
            ),
        ))

    dir_label = 'Upregulated' if direction == 'up' else 'Downregulated'
    n_genes = len(genes_display)
    fig.update_layout(
        title=dict(
            text=f'Top {top_per_group} {dir_label} Biomarker Candidates per Group',
            font=dict(size=16, color='black'),
            x=0.5,
            xanchor='center',
        ),
        xaxis=dict(
            title=dict(text='Group', font=dict(size=14)),
            tickfont=dict(size=12),
        ),
        yaxis=dict(
            title=dict(text='miRNA', font=dict(size=14)),
            tickfont=dict(size=10),
            automargin=True,
        ),
        template='plotly_white',
        width=700,
        height=max(700, n_genes * 18 + 120),
        showlegend=False,
        margin=dict(l=120, r=80, t=60, b=60),
        plot_bgcolor='white',
        paper_bgcolor='white',
    )
    suffix = 'upregulated' if direction == 'up' else 'downregulated'
    fig.write_html(os.path.join(output_dir, f'biomarker_dotplot_{suffix}.html'))
    return fig


def create_individual_expression_plots(biomarkers, sample_counts, output_dir, top_per_group=5):
    """
    Create box/strip plots for top biomarker candidates showing individual sample values.
    """
    sample_groups = {
        'Cells (4T1)': ['4T1.1', '4T1.2', '4T1.3'],
        'Heart': ['He.4', 'He.5'],
        'Kidney': ['Ki.4', 'Ki.5'],
        'Liver': ['Li.4', 'Li.5', 'Li.3'],
        'Lung': ['Lu.4', 'Lu.5', 'Lu.3'],
        'Spleen': ['Sp.4', 'Sp.5', 'Sp.3'],
    }
    group_colors = {
        'Cells (4T1)': '#e74c3c',
        'Heart': '#e67e22',
        'Kidney': '#2ecc71',
        'Liver': '#9b59b6',
        'Lung': '#3498db',
        'Spleen': '#1abc9c',
    }
    group_order = ['Cells (4T1)', 'Heart', 'Kidney', 'Liver', 'Lung', 'Spleen']

    # Collect top genes
    all_top_genes = []
    for group, df in biomarkers.items():
        top = df[df['log2FC'] > 0].head(top_per_group)
        for g in top['GeneID'].values:
            if g not in all_top_genes:
                all_top_genes.append(g)

    if not all_top_genes:
        return None

    n_genes = len(all_top_genes)
    n_cols = 3
    n_rows = (n_genes + n_cols - 1) // n_cols

    fig = make_subplots(rows=n_rows, cols=n_cols,
                        subplot_titles=[g.replace('mmu-', '') for g in all_top_genes],
                        vertical_spacing=0.06)

    for idx, gene in enumerate(all_top_genes):
        row = idx // n_cols + 1
        col = idx % n_cols + 1

        gene_data = sample_counts[sample_counts['GeneID'] == gene]
        if len(gene_data) == 0:
            continue

        for group_name in group_order:
            samples = sample_groups[group_name]
            vals = gene_data[samples].values.flatten()
            vals = vals[~np.isnan(vals)]

            fig.add_trace(go.Box(
                y=vals,
                name=group_name,
                marker_color=group_colors[group_name],
                boxpoints='all',
                jitter=0.3,
                pointpos=0,
                showlegend=(idx == 0),
                legendgroup=group_name,
            ), row=row, col=col)

    fig.update_layout(
        title='Individual Sample Expression: Top Biomarker Candidates',
        template='plotly_white',
        width=1100,
        height=max(400, n_rows * 300),
        boxmode='group',
    )
    fig.write_html(os.path.join(output_dir, 'biomarker_expression_boxplots.html'))
    return fig


# =============================================================================
# 6. MA PLOT
# =============================================================================

def create_ma_plots(comparisons, output_dir):
    """Create MA plots (log2FC vs mean expression) for each comparison.
    Includes draggable labels for top DE miRNAs and interactive controls."""
    for comp_name, comp_df in comparisons.items():
        df = comp_df.dropna(subset=['log2FC', 'padj', 'log2avg']).copy()

        # Cells_vs_Organs has group1=Organs, group2=Cells (reversed)
        if comp_name == 'Cells_vs_Organs':
            df['log2FC'] = -df['log2FC']

        df['significant'] = np.where(
            (df['padj'] <= 0.05) & (df['abs_log2FC'] >= 1.0), 'DE', 'Not DE'
        )

        fig = go.Figure()
        for cat, color in [('Not DE', '#d5d8dc'), ('DE', '#e74c3c')]:
            subset = df[df['significant'] == cat]
            fig.add_trace(go.Scattergl(
                x=subset['log2avg'],
                y=subset['log2FC'],
                mode='markers',
                name=f'{cat} ({len(subset)})',
                marker=dict(color=color, size=4, opacity=0.6),
                text=subset['GeneID'],
                hovertemplate='<b>%{text}</b><br>log2(avg): %{x:.2f}<br>log2FC: %{y:.3f}<extra></extra>',
            ))

        fig.add_hline(y=0, line_color='black', line_width=0.5)
        fig.add_hline(y=1, line_dash='dash', line_color='gray')
        fig.add_hline(y=-1, line_dash='dash', line_color='gray')

        # Label top DE hits as draggable annotations
        de = df[df['significant'] == 'DE'].copy()
        de['abs_fc'] = de['log2FC'].abs()
        top_up = de[de['log2FC'] > 0].nlargest(5, 'abs_fc')
        top_down = de[de['log2FC'] < 0].nlargest(5, 'abs_fc')
        top_hits = pd.concat([top_up, top_down])

        for _, row in top_hits.iterrows():
            label = row['GeneID'].replace('mmu-', '')
            fig.add_annotation(
                x=row['log2avg'],
                y=row['log2FC'],
                text=label,
                font=dict(size=10, color='black'),
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=1,
                arrowcolor='gray',
                ax=0,
                ay=-30,
                bgcolor='rgba(255,255,255,0.7)',
                borderpad=2,
            )

        pretty = comp_name.replace('_', ' ').replace('vs', 'vs.')
        n_de = (df['significant'] == 'DE').sum()
        fig.update_layout(
            title=dict(
                text=f'MA Plot: {pretty}<br><sub>{n_de} DE miRNAs (FDR<0.05, |log2FC|>1.0)</sub>',
                font=dict(size=16),
                x=0.5,
                xanchor='center',
            ),
            xaxis_title='log2(Mean Expression)',
            yaxis_title='log2(Fold Change)',
            template='plotly_white',
            width=800, height=550,
            legend=dict(x=0.01, y=0.99, bgcolor='rgba(255,255,255,0.8)'),
        )
        _write_interactive_html(fig, os.path.join(output_dir, f'ma_plot_{comp_name}.html'),
                                has_annotations=True, default_filename=f'ma_plot_{comp_name}')


# =============================================================================
# MAIN
# =============================================================================

def main():
    filepath = "Updated 7066_DEmiRNAs.xlsx"
    output_dir = "results"
    os.makedirs(output_dir, exist_ok=True)

    print("=" * 60)
    print("miRNA Biomarker Analysis Pipeline")
    print("=" * 60)

    # 1. Parse data
    print("\n[1/6] Parsing data...")
    genes, comparisons, group_avg, sample_counts = parse_signatures_sheet(filepath)
    print(f"  Loaded {len(genes)} miRNAs, {len(comparisons)} comparisons")

    # 2. Volcano plots
    print("[2/6] Creating interactive volcano plots...")
    create_all_volcano_plots(comparisons, output_dir)
    print("  -> volcano_all_comparisons.html + individual volcano plots")

    # 3. Heatmap
    print("[3/6] Creating interactive heatmap...")
    create_heatmap(group_avg, genes, comparisons, output_dir, top_n=60)
    print("  -> heatmap_top_DE_miRNAs.html")

    # 4. Biomarker identification
    print("[4/6] Identifying group-specific biomarkers...")
    biomarkers = identify_biomarkers(comparisons, group_avg, sample_counts)

    print("\n  === BIOMARKER SUMMARY ===")
    for group, df in biomarkers.items():
        n_total = len(df)
        n_up = (df['log2FC'] > 0).sum()
        n_down = (df['log2FC'] < 0).sum()
        print(f"\n  {group}: {n_total} biomarker candidates ({n_up} up, {n_down} down)")
        if n_up > 0:
            top_up = df[df['log2FC'] > 0].head(5)
            print(f"    Top UP-regulated:")
            for _, row in top_up.iterrows():
                print(f"      {row['GeneID']:30s} log2FC={row['log2FC']:+.2f}  FDR={row['padj']:.2e}  score={row['biomarker_score']:.1f}")
        if n_down > 0:
            top_down = df[df['log2FC'] < 0].head(5)
            print(f"    Top DOWN-regulated:")
            for _, row in top_down.iterrows():
                print(f"      {row['GeneID']:30s} log2FC={row['log2FC']:+.2f}  FDR={row['padj']:.2e}  score={row['biomarker_score']:.1f}")

    summary = create_biomarker_summary(biomarkers, output_dir)
    print(f"\n  -> biomarker_candidates.csv ({len(summary)} candidates)")

    group_tables = create_group_summary_tables(biomarkers, group_avg, output_dir)
    print(f"  -> biomarker_summary_tables.csv ({len(group_tables)} entries)")
    # 5. Expression plots
    print("\n[5/6] Creating expression profile plots...")
    create_expression_dotplot(biomarkers, group_avg, output_dir, direction='up')
    print("  -> biomarker_dotplot_upregulated.html")
    create_expression_dotplot(biomarkers, group_avg, output_dir, direction='down')
    print("  -> biomarker_dotplot_downregulated.html")

    create_individual_expression_plots(biomarkers, sample_counts, output_dir)
    print("  -> biomarker_expression_boxplots.html")

    # 6. MA plots
    print("[6/6] Creating MA plots...")
    create_ma_plots(comparisons, output_dir)
    print("  -> MA plots for each comparison")

    print("\n" + "=" * 60)
    print("ANALYSIS COMPLETE")
    print(f"All outputs saved to: {output_dir}/")
    print("=" * 60)
    print("\nGenerated files:")
    for f in sorted(os.listdir(output_dir)):
        size = os.path.getsize(os.path.join(output_dir, f))
        print(f"  {f:45s} ({size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
