#!/usr/bin/env python3
"""
PDF Color Analysis Script

Analyzes a PDF file to determine:
- Total number of pages
- Number of black and white pages
- Number of color pages
- List of pages that contain color

Usage:
    python analyze_pdf_colors.py main.pdf
"""

import sys
from pathlib import Path

try:
    import PyPDF2
    from pdf2image import convert_from_path
    from PIL import Image
    import numpy as np
except ImportError as e:
    print(f"Error: Missing required library. Please install dependencies:")
    print("pip install PyPDF2 pdf2image Pillow numpy")
    print("Also ensure poppler-utils is installed (system package)")
    sys.exit(1)


def is_page_color(image, threshold=10):
    """
    Determine if a page image contains color.
    
    Args:
        image: PIL Image object
        threshold: Color detection sensitivity (higher = more strict)
    
    Returns:
        bool: True if page contains color, False if grayscale/B&W
    """
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Convert to numpy array
    img_array = np.array(image)
    
    # Get RGB channels
    r, g, b = img_array[:,:,0], img_array[:,:,1], img_array[:,:,2]
    
    # Calculate differences between channels
    rg_diff = np.abs(r.astype(int) - g.astype(int))
    rb_diff = np.abs(r.astype(int) - b.astype(int))
    gb_diff = np.abs(g.astype(int) - b.astype(int))
    
    # If any significant difference exists between channels, it's color
    max_diff = np.max([rg_diff, rb_diff, gb_diff])
    
    return max_diff > threshold


def analyze_pdf_colors(pdf_path, dpi=150):
    """
    Analyze PDF file for color usage.
    
    Args:
        pdf_path: Path to PDF file
        dpi: Resolution for rendering pages (default: 150)
    
    Returns:
        dict: Analysis results
    """
    pdf_path = Path(pdf_path)
    
    if not pdf_path.exists():
        print(f"Error: File '{pdf_path}' not found!")
        sys.exit(1)
    
    print(f"Analyzing PDF: {pdf_path.name}")
    print(f"This may take a few minutes for large documents...\n")
    
    # Get total pages using PyPDF2
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        total_pages = len(pdf_reader.pages)
    
    print(f"Total pages: {total_pages}")
    print("Converting pages to images and analyzing colors...")
    
    # Convert PDF pages to images
    images = convert_from_path(pdf_path, dpi=dpi)
    
    color_pages = []
    bw_pages = []
    
    # Analyze each page
    for page_num, image in enumerate(images, start=1):
        print(f"Analyzing page {page_num}/{total_pages}...", end='\r')
        
        if is_page_color(image):
            color_pages.append(page_num)
        else:
            bw_pages.append(page_num)
    
    print()  # New line after progress
    
    results = {
        'total_pages': total_pages,
        'color_pages': len(color_pages),
        'bw_pages': len(bw_pages),
        'color_page_list': color_pages
    }
    
    return results


def print_results(results):
    """Print analysis results in a formatted way."""
    print("\n" + "="*60)
    print("PDF COLOR ANALYSIS RESULTS")
    print("="*60)
    print(f"Total pages:           {results['total_pages']}")
    print(f"Black & White pages:   {results['bw_pages']}")
    print(f"Color pages:           {results['color_pages']}")
    print("\nPages with color:")
    
    if results['color_page_list']:
        # Group consecutive pages
        color_list = results['color_page_list']
        ranges = []
        start = color_list[0]
        end = color_list[0]
        
        for i in range(1, len(color_list)):
            if color_list[i] == end + 1:
                end = color_list[i]
            else:
                if start == end:
                    ranges.append(f"{start}")
                else:
                    ranges.append(f"{start}-{end}")
                start = color_list[i]
                end = color_list[i]
        
        # Add last range
        if start == end:
            ranges.append(f"{start}")
        else:
            ranges.append(f"{start}-{end}")
        
        print(f"  {', '.join(ranges)}")
        print(f"\nDetailed list: {color_list}")
    else:
        print("  None - Document is entirely black & white")
    
    print("="*60)


def main():
    if len(sys.argv) != 2:
        print("Usage: python analyze_pdf_colors.py <pdf_file>")
        print("Example: python analyze_pdf_colors.py main.pdf")
        sys.exit(1)
    
    pdf_file = sys.argv[1]
    
    try:
        results = analyze_pdf_colors(pdf_file)
        print_results(results)
        
        # Save results to text file
        output_file = Path(pdf_file).stem + "_color_analysis.txt"
        with open(output_file, 'w') as f:
            f.write("PDF Color Analysis Results\n")
            f.write("="*60 + "\n")
            f.write(f"PDF File: {pdf_file}\n")
            f.write(f"Total pages: {results['total_pages']}\n")
            f.write(f"Black & White pages: {results['bw_pages']}\n")
            f.write(f"Color pages: {results['color_pages']}\n")
            f.write(f"\nColor page numbers: {results['color_page_list']}\n")
        
        print(f"\nResults saved to: {output_file}")
        
    except Exception as e:
        print(f"\nError during analysis: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
