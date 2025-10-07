#!/usr/bin/env python3
"""
PDF Splitter for Duplex Printing with Color and B/W Separation

This script analyzes a PDF, identifies color and B/W pages, and creates two PDFs:
1. A color PDF with pages grouped in pairs (for duplex printing)
2. A B/W PDF with all remaining B/W pages

The script ensures:
- The first page (title page) is always in the color PDF with a blank page after it
- Color pages are grouped in pairs, borrowing adjacent B/W pages if needed
- The B/W PDF contains only pages not used in the color PDF
- Both PDFs are ready for duplex (recto-verso) printing and can be reassembled

Usage:
    python split_pdf_for_printing.py input.pdf [--dpi 150] [--threshold 10]
"""

import argparse
import sys
from pathlib import Path
from typing import List, Tuple, Set

try:
    from PyPDF2 import PdfReader, PdfWriter
except ImportError:
    print("Error: PyPDF2 is not installed.")
    print("Install it with: pip install PyPDF2>=3.0.0")
    sys.exit(1)

try:
    from pdf2image import convert_from_path
except ImportError:
    print("Error: pdf2image is not installed.")
    print("Install it with: pip install pdf2image>=1.16.0")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("Error: Pillow is not installed.")
    print("Install it with: pip install Pillow>=10.0.0")
    sys.exit(1)

try:
    import numpy as np
except ImportError:
    print("Error: numpy is not installed.")
    print("Install it with: pip install numpy>=1.24.0")
    sys.exit(1)


def is_page_color(image: Image.Image, threshold: int = 10) -> bool:
    """
    Determine if a page is in color or black & white.
    
    Args:
        image: PIL Image object of the page
        threshold: Maximum difference between RGB channels to consider grayscale
        
    Returns:
        True if the page has color, False if it's grayscale/B&W
    """
    # Convert to RGB if not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Convert to numpy array
    img_array = np.array(image)
    
    # Get RGB channels
    r = img_array[:, :, 0].astype(np.int16)
    g = img_array[:, :, 1].astype(np.int16)
    b = img_array[:, :, 2].astype(np.int16)
    
    # Calculate differences between channels
    rg_diff = np.abs(r - g)
    rb_diff = np.abs(r - b)
    gb_diff = np.abs(g - b)
    
    # If any significant differences exist, it's a color page
    max_diff = np.maximum(np.maximum(rg_diff, rb_diff), gb_diff)
    
    # Check if any pixel has a difference above threshold
    has_color = np.any(max_diff > threshold)
    
    return has_color


def analyze_pdf_colors(pdf_path: str, dpi: int = 150, threshold: int = 10) -> List[bool]:
    """
    Analyze all pages in a PDF and determine which are color vs B/W.
    
    Args:
        pdf_path: Path to the PDF file
        dpi: Resolution for rendering pages (higher = more accurate but slower)
        threshold: Color detection threshold
        
    Returns:
        List of booleans, True for color pages, False for B/W pages
    """
    print(f"Analyzing PDF: {pdf_path}")
    
    # Get total page count
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)
    print(f"Total pages: {total_pages}")
    
    # Convert PDF to images
    print(f"Converting pages to images (DPI: {dpi})...")
    images = convert_from_path(pdf_path, dpi=dpi)
    
    # Analyze each page
    color_flags = []
    print("\nAnalyzing pages for color content:")
    for i, image in enumerate(images, 1):
        is_color = is_page_color(image, threshold)
        color_flags.append(is_color)
        status = "COLOR" if is_color else "B/W"
        print(f"  Page {i:3d}: {status}")
    
    return color_flags


def create_blank_page(reader: PdfReader) -> PdfWriter:
    """Create a blank page matching the size of the first page."""
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter
    from io import BytesIO
    
    # Get dimensions from first page
    first_page = reader.pages[0]
    width = float(first_page.mediabox.width)
    height = float(first_page.mediabox.height)
    
    # Create a blank PDF in memory
    packet = BytesIO()
    c = canvas.Canvas(packet, pagesize=(width, height))
    c.save()
    packet.seek(0)
    
    # Read the blank PDF
    blank_reader = PdfReader(packet)
    return blank_reader.pages[0]


def group_color_pages(color_flags: List[bool]) -> Tuple[List[Tuple[int, int]], Set[int]]:
    """
    Group color pages into pairs for duplex printing.
    
    Strategy:
    - First page is always color, followed by a blank page
    - For other color pages, pair them with adjacent B/W pages or each other
    - Return list of page pairs and set of all pages used in color PDF
    
    Args:
        color_flags: List of booleans indicating color (True) or B/W (False)
        
    Returns:
        Tuple of (pairs_list, pages_in_color_pdf)
        - pairs_list: List of tuples (page1_idx, page2_idx) for color PDF
        - pages_in_color_pdf: Set of all page indices included in color PDF
    """
    pairs = []
    used_pages = set()
    
    # First page (index 0) is always in color PDF with a blank page after it
    pairs.append((0, -1))  # -1 indicates blank page
    used_pages.add(0)
    
    # Find remaining color pages
    color_pages = [i for i in range(1, len(color_flags)) if color_flags[i]]
    
    i = 0
    while i < len(color_pages):
        page_idx = color_pages[i]
        
        # Check if next color page is adjacent (can pair them together)
        if i + 1 < len(color_pages) and color_pages[i + 1] == page_idx + 1:
            # Two consecutive color pages - pair them
            pairs.append((page_idx, page_idx + 1))
            used_pages.add(page_idx)
            used_pages.add(page_idx + 1)
            i += 2
        else:
            # Single color page - find a B/W companion
            companion = None
            
            # Try page after
            if page_idx + 1 < len(color_flags) and not color_flags[page_idx + 1]:
                if page_idx + 1 not in used_pages:
                    companion = page_idx + 1
            
            # Try page before if no companion found
            if companion is None and page_idx - 1 >= 0 and not color_flags[page_idx - 1]:
                if page_idx - 1 not in used_pages:
                    companion = page_idx - 1
            
            if companion is not None:
                # Pair color page with B/W companion (maintain order)
                if companion < page_idx:
                    pairs.append((companion, page_idx))
                else:
                    pairs.append((page_idx, companion))
                used_pages.add(page_idx)
                used_pages.add(companion)
            else:
                # No B/W companion available, add color page alone with blank
                pairs.append((page_idx, -1))  # -1 for blank page
                used_pages.add(page_idx)
            
            i += 1
    
    return pairs, used_pages


def split_pdf(pdf_path: str, color_flags: List[bool], output_prefix: str = None):
    """
    Split PDF into color and B/W PDFs for duplex printing.
    
    Args:
        pdf_path: Path to input PDF
        color_flags: List of booleans indicating color pages
        output_prefix: Prefix for output files (default: input filename)
    """
    reader = PdfReader(pdf_path)
    
    if output_prefix is None:
        output_prefix = Path(pdf_path).stem
    
    # Group color pages into pairs
    print("\nGrouping pages for duplex printing...")
    color_pairs, pages_in_color_pdf = group_color_pages(color_flags)
    
    # Create color PDF
    print(f"\nCreating color PDF...")
    color_writer = PdfWriter()
    
    for pair_idx, (page1, page2) in enumerate(color_pairs, 1):
        if page1 >= 0:
            color_writer.add_page(reader.pages[page1])
            print(f"  Pair {pair_idx}: Page {page1 + 1}", end="")
        
        if page2 == -1:
            # Add blank page
            try:
                from reportlab.pdfgen import canvas
                from io import BytesIO
                
                first_page = reader.pages[0]
                width = float(first_page.mediabox.width)
                height = float(first_page.mediabox.height)
                
                packet = BytesIO()
                c = canvas.Canvas(packet, pagesize=(width, height))
                c.showPage()  # Important: must call showPage to create a page
                c.save()
                packet.seek(0)
                
                blank_reader = PdfReader(packet)
                color_writer.add_page(blank_reader.pages[0])
                print(" + Blank page")
            except (ImportError, IndexError) as e:
                print(f" + (blank page skipped - error: {e})")
        else:
            color_writer.add_page(reader.pages[page2])
            print(f" + Page {page2 + 1}")
    
    color_output = f"{output_prefix}_color.pdf"
    with open(color_output, 'wb') as f:
        color_writer.write(f)
    print(f"\nColor PDF saved: {color_output}")
    print(f"Total pages in color PDF: {len(color_writer.pages)}")
    
    # Create B/W PDF with remaining pages
    print(f"\nCreating B/W PDF...")
    bw_writer = PdfWriter()
    bw_pages = []
    
    for i in range(len(reader.pages)):
        if i not in pages_in_color_pdf:
            bw_writer.add_page(reader.pages[i])
            bw_pages.append(i + 1)  # 1-indexed for display
    
    bw_output = f"{output_prefix}_bw.pdf"
    with open(bw_output, 'wb') as f:
        bw_writer.write(f)
    print(f"B/W PDF saved: {bw_output}")
    print(f"Total pages in B/W PDF: {len(bw_writer.pages)}")
    
    # Print summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Original PDF: {len(reader.pages)} pages")
    print(f"Color PDF: {len(color_writer.pages)} pages ({len(color_pairs)} duplex sheets)")
    print(f"B/W PDF: {len(bw_writer.pages)} pages")
    print(f"\nPages in color PDF: {sorted(list(pages_in_color_pdf), key=lambda x: x + 1)}")
    if bw_pages:
        print(f"Pages in B/W PDF: {bw_pages}")
    print("\nPrinting instructions:")
    print(f"1. Print '{color_output}' in COLOR with DUPLEX (recto-verso)")
    print(f"2. Print '{bw_output}' in BLACK & WHITE with DUPLEX (recto-verso)")
    print("3. Reassemble pages in order based on the page numbers above")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Split PDF into color and B/W PDFs for cost-effective duplex printing",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python split_pdf_for_printing.py main.pdf
  python split_pdf_for_printing.py main.pdf --dpi 200 --threshold 15
  python split_pdf_for_printing.py Eljadiri_Masterarbeit.pdf

The script creates two files:
  - {filename}_color.pdf: Pages with color content, grouped in pairs for duplex
  - {filename}_bw.pdf: Remaining B/W pages for duplex printing
        """
    )
    
    parser.add_argument('pdf_path', help='Path to the PDF file to analyze')
    parser.add_argument('--dpi', type=int, default=150,
                       help='DPI for page rendering (default: 150, higher = more accurate)')
    parser.add_argument('--threshold', type=int, default=10,
                       help='Color detection threshold (default: 10)')
    parser.add_argument('--output', type=str, default=None,
                       help='Output file prefix (default: input filename)')
    
    args = parser.parse_args()
    
    # Check if file exists
    if not Path(args.pdf_path).exists():
        print(f"Error: File not found: {args.pdf_path}")
        sys.exit(1)
    
    try:
        # Analyze PDF for color pages
        color_flags = analyze_pdf_colors(args.pdf_path, args.dpi, args.threshold)
        
        # Split PDF
        split_pdf(args.pdf_path, color_flags, args.output)
        
    except Exception as e:
        print(f"\nError: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
