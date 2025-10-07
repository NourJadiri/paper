#!/usr/bin/env python3
"""Quick script to plot F1 scores for Gemini 2.5 Flash across validation states"""

import pandas as pd
import matplotlib.pyplot as plt
import json
from pathlib import Path

# Languages to process
languages = ['EN', 'BG', 'HI', 'PT', 'RU']

# Validation states and their folders
validation_states = {
    'No Validation': 'gemini25_flash_devset_evaluation',
    'Narrative Validation': 'gemini25_flash_narr_val_evaluation',
    'Subnarrative Validation': 'gemini25_flash_subnarr_val_evaluation'
}

# Collect data for both levels
data_narr = []
data_subnarr = []

for val_name, folder in validation_states.items():
    for lang in languages:
        file_path = Path(folder) / f"{lang}_performance_summary.csv"
        if file_path.exists():
            df = pd.read_csv(file_path)
            
            # Get narrative F1 score
            narr_row = df[df['Label_Type'] == 'narratives']
            if not narr_row.empty:
                f1_score = narr_row['F1_Samples'].values[0]
                data_narr.append({
                    'Language': lang,
                    'Validation': val_name,
                    'F1 Score': f1_score
                })
            
            # Get subnarrative F1 score
            subnарr_row = df[df['Label_Type'] == 'subnarratives']
            if not subnарr_row.empty:
                f1_score = subnарr_row['F1_Samples'].values[0]
                data_subnarr.append({
                    'Language': lang,
                    'Validation': val_name,
                    'F1 Score': f1_score
                })
                print(f"{folder}/{lang} - Narr: {data_narr[-1]['F1 Score']:.4f}, Subnarr: {f1_score:.4f}")

# Create DataFrames
df_narr = pd.DataFrame(data_narr)
df_subnarr = pd.DataFrame(data_subnarr)

# Create plot with 2 subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Set up bar positions
x = range(len(languages))
width = 0.25
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']

# Plot NARRATIVE level
for i, (val_name, color) in enumerate(zip(validation_states.keys(), colors)):
    val_data = df_narr[df_narr['Validation'] == val_name]
    f1_scores = [val_data[val_data['Language'] == lang]['F1 Score'].values[0] 
                 if len(val_data[val_data['Language'] == lang]) > 0 else 0 
                 for lang in languages]
    
    positions = [xi + (i - 1) * width for xi in x]
    ax1.bar(positions, f1_scores, width, label=val_name, color=color, alpha=0.8)

# Customize narrative plot
ax1.set_xlabel('Language', fontsize=12, fontweight='bold')
ax1.set_ylabel('F1 Score', fontsize=12, fontweight='bold')
ax1.set_title('Narrative Level F1 Scores', fontsize=14, fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(languages)
ax1.legend(loc='best', framealpha=0.9)
ax1.grid(axis='y', alpha=0.3, linestyle='--')
ax1.set_ylim(0, 1.0)

# Add value labels on narrative bars
for container in ax1.containers:
    ax1.bar_label(container, fmt='%.3f', fontsize=7, padding=2)

# Plot SUBNARRATIVE level
for i, (val_name, color) in enumerate(zip(validation_states.keys(), colors)):
    val_data = df_subnarr[df_subnarr['Validation'] == val_name]
    f1_scores = [val_data[val_data['Language'] == lang]['F1 Score'].values[0] 
                 if len(val_data[val_data['Language'] == lang]) > 0 else 0 
                 for lang in languages]
    
    positions = [xi + (i - 1) * width for xi in x]
    ax2.bar(positions, f1_scores, width, label=val_name, color=color, alpha=0.8)

# Customize subnarrative plot
ax2.set_xlabel('Language', fontsize=12, fontweight='bold')
ax2.set_ylabel('F1 Score', fontsize=12, fontweight='bold')
ax2.set_title('Subnarrative Level F1 Scores', fontsize=14, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(languages)
ax2.legend(loc='best', framealpha=0.9)
ax2.grid(axis='y', alpha=0.3, linestyle='--')
ax2.set_ylim(0, 1.0)

# Add value labels on subnarrative bars
for container in ax2.containers:
    ax2.bar_label(container, fmt='%.3f', fontsize=7, padding=2)

plt.suptitle('Gemini 2.5 Flash: F1 Scores Across Validation States', fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()

# Save plot
output_path = 'gemini_flash_validation_comparison.png'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"\nPlot saved to: {output_path}")

plt.show()
