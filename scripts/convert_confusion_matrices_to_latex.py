#!/usr/bin/env python3
"""
Convert confusion matrix Markdown files to LaTeX longtable format.
"""

import re
from pathlib import Path

def parse_markdown_table(lines, start_idx):
    """Parse a markdown table starting at start_idx."""
    # Find table start
    header_idx = start_idx
    while header_idx < len(lines) and not lines[header_idx].strip().startswith('|'):
        header_idx += 1
    
    if header_idx >= len(lines):
        return None, start_idx
    
    # Get header
    header = lines[header_idx].strip()
    
    # Skip separator line
    sep_idx = header_idx + 1
    
    # Collect data rows
    data_rows = []
    row_idx = sep_idx + 1
    while row_idx < len(lines) and lines[row_idx].strip().startswith('|'):
        data_rows.append(lines[row_idx].strip())
        row_idx += 1
    
    return (header, data_rows), row_idx

def escape_latex(text):
    """Escape special LaTeX characters."""
    replacements = {
        '&': r'\&',
        '%': r'\%',
        '$': r'\$',
        '#': r'\#',
        '_': r'\_',
        '{': r'\{',
        '}': r'\}',
        '~': r'\textasciitilde{}',
        '^': r'\^{}',
    }
    for char, escaped in replacements.items():
        text = text.replace(char, escaped)
    return text

def convert_table_to_latex(header, data_rows, caption, label):
    """Convert markdown table to LaTeX longtable."""
    # Parse header to get column alignment
    header_parts = [h.strip() for h in header.split('|') if h.strip()]
    
    # Filter columns: Keep Label, F1, Support, TP, FP, FN, TN (remove Precision and Recall)
    # Original order: Label | F1 | Precision | Recall | Support | TP | FP | FN | TN
    # Keep indices: 0, 1, 4, 5, 6, 7, 8
    keep_indices = [0, 1, 4, 5, 6, 7, 8]
    filtered_header_parts = [header_parts[i] for i in keep_indices if i < len(header_parts)]
    num_cols = len(filtered_header_parts)
    
    # Create column specification (first column left-aligned, rest right-aligned for numbers)
    col_spec = 'l' + 'r' * (num_cols - 1)
    
    latex_lines = []
    # Use small font and adjust spacing for better fit
    latex_lines.append(r'{\small')
    latex_lines.append(r'\setlength{\tabcolsep}{4pt}')
    latex_lines.append(r'\begin{longtable}{' + col_spec + '}')
    latex_lines.append(r'\caption{' + caption + r'}')
    latex_lines.append(r'\label{' + label + r'} \\')
    latex_lines.append(r'\toprule')
    
    # Add header
    header_cells = [r'\textbf{' + escape_latex(h) + r'}' for h in filtered_header_parts]
    latex_lines.append(' & '.join(header_cells) + r' \\')
    latex_lines.append(r'\midrule')
    latex_lines.append(r'\endfirsthead')
    
    # Continuation header
    latex_lines.append(r'\multicolumn{' + str(num_cols) + r'}{c}%')
    latex_lines.append(r'{{Table \thetable\ continued from previous page}} \\')
    latex_lines.append(r'\toprule')
    latex_lines.append(' & '.join(header_cells) + r' \\')
    latex_lines.append(r'\midrule')
    latex_lines.append(r'\endhead')
    
    # Footer
    latex_lines.append(r'\midrule')
    latex_lines.append(r'\multicolumn{' + str(num_cols) + r'}{r}{{Continued on next page}} \\')
    latex_lines.append(r'\endfoot')
    latex_lines.append(r'\bottomrule')
    latex_lines.append(r'\endlastfoot')
    
    # Add data rows
    for row in data_rows:
        cells = [c.strip() for c in row.split('|') if c.strip()]
        # Filter cells to keep only selected columns
        filtered_cells = [cells[i] for i in keep_indices if i < len(cells)]
        
        # Escape first cell (label name), keep numbers as-is
        # Truncate very long label names
        first_cell = escape_latex(filtered_cells[0])
        if len(first_cell) > 70:
            first_cell = first_cell[:67] + '...'
        escaped_cells = [first_cell] + filtered_cells[1:]
        latex_lines.append(' & '.join(escaped_cells) + r' \\')
    
    latex_lines.append(r'\end{longtable}')
    latex_lines.append(r'}')  # Close the font size group
    
    return '\n'.join(latex_lines)

def process_confusion_matrix_file(input_file, output_file, config_name):
    """Process a confusion matrix markdown file and convert to LaTeX."""
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    output_lines = []
    output_lines.append(f'% Confusion matrices for {config_name}')
    output_lines.append(f'% Auto-generated from {input_file.name}')
    output_lines.append('')
    
    i = 0
    table_count = 0
    current_language = None
    current_level = None  # 'Narratives' or 'Subnarratives'
    
    while i < len(lines):
        line = lines[i].strip()
        
        # Detect language section
        if line.startswith('### ') and ' - Narratives' in line:
            current_language = line.split('###')[1].split('-')[0].strip()
            current_level = 'Narratives'
            output_lines.append(f'\n\\subsubsection{{{current_language} - Narrative Level}}')
            i += 1
            continue
        elif line.startswith('### ') and ' - Subnarratives' in line:
            current_language = line.split('###')[1].split('-')[0].strip()
            current_level = 'Subnarratives'
            output_lines.append(f'\n\\subsubsection{{{current_language} - Subnarrative Level}}')
            i += 1
            continue
        
        # Detect table
        if '#### Confusion Matrix Summary Table' in line:
            # Extract metadata from preceding lines
            meta_info = []
            for j in range(max(0, i-10), i):
                if lines[j].strip().startswith('**'):
                    meta_info.append(lines[j].strip())
            
            # Parse table
            table_data, next_i = parse_markdown_table(lines, i + 1)
            if table_data:
                header, data_rows = table_data
                table_count += 1
                
                caption = f'Confusion matrix for {current_language} {current_level} ({config_name})'
                label = f'tab:confusion-{config_name.lower().replace(" ", "-")}-{current_language.lower()}-{current_level.lower()}'
                
                latex_table = convert_table_to_latex(header, data_rows, caption, label)
                output_lines.append('\n' + latex_table + '\n')
                
                i = next_i
                continue
        
        i += 1
    
    # Write output
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output_lines))
    
    print(f'Converted {table_count} tables from {input_file.name} to {output_file.name}')

if __name__ == '__main__':
    base_dir = Path(__file__).parent.parent
    
    # Process no-validation confusion matrices
    input_file1 = base_dir / 'gemini25_flash_devset_evaluation' / 'gemini_confusion_matrices.md'
    output_file1 = base_dir / 'chapters' / 'appendix_confusion_no_val.tex'
    process_confusion_matrix_file(input_file1, output_file1, 'No Validation')
    
    # Process subnarrative-validation confusion matrices
    input_file2 = base_dir / 'gemini25_flash_subnarr_val_evaluation' / 'gemini_subnarr_val_confusion_matrices.md'
    output_file2 = base_dir / 'chapters' / 'appendix_confusion_subnarr_val.tex'
    process_confusion_matrix_file(input_file2, output_file2, 'Subnarrative Validation')
    
    print('\nConversion complete!')
