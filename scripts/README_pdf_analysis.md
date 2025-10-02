# PDF Color Analysis Script

This script analyzes a PDF file to determine which pages contain color and which are black & white.

## Installation

### Step 1: Install system dependencies (poppler-utils)

**Ubuntu/Debian:**
```bash
sudo apt-get install poppler-utils
```

**macOS:**
```bash
brew install poppler
```

**Windows:**
Download and install poppler from: https://github.com/oschwartz10612/poppler-windows/releases/

### Step 2: Install Python dependencies

```bash
pip install -r requirements.txt
```

## Usage

```bash
python analyze_pdf_colors.py main.pdf
```

Or from the parent directory:
```bash
python scripts/analyze_pdf_colors.py main.pdf
```

## Output

The script will display:
- Total number of pages
- Number of black & white pages
- Number of color pages
- List of page numbers that contain color (grouped into ranges)

It also saves the results to a text file: `main_color_analysis.txt`

## Example Output

```
Analyzing PDF: main.pdf
Total pages: 150
Converting pages to images and analyzing colors...

============================================================
PDF COLOR ANALYSIS RESULTS
============================================================
Total pages:           150
Black & White pages:   145
Color pages:           5

Pages with color:
  12, 15-17, 45

Detailed list: [12, 15, 16, 17, 45]
============================================================

Results saved to: main_color_analysis.txt
```

## Notes

- The script renders each page as an image at 150 DPI (can be adjusted in code)
- Processing time depends on document size (typically 1-2 seconds per page)
- Color detection uses a threshold to distinguish true color from grayscale
