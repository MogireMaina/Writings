#!/usr/bin/env python3
"""
Script to extract text from PDF files in the sources folder
"""
import os
import sys
from pathlib import Path
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file"""
    try:
        reader = PdfReader(pdf_path)
        text = []

        print(f"\n{'='*80}")
        print(f"Processing: {pdf_path.name}")
        print(f"Number of pages: {len(reader.pages)}")
        print(f"{'='*80}\n")

        for page_num, page in enumerate(reader.pages, 1):
            page_text = page.extract_text()
            if page_text.strip():
                text.append(f"--- Page {page_num} ---\n{page_text}\n")

        return "\n".join(text)

    except Exception as e:
        print(f"Error processing {pdf_path.name}: {str(e)}", file=sys.stderr)
        return None

def main():
    # Directory containing the PDFs
    pdf_dir = Path("/home/user/Writings/KCL003, Intelligence in Conflict, Summative Assessment, 2700w/sources (1)/sources")
    output_dir = pdf_dir / "extracted_texts"

    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Get all PDF files
    pdf_files = sorted(pdf_dir.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in the directory.")
        return

    print(f"Found {len(pdf_files)} PDF files to process.\n")

    # Process each PDF
    for pdf_path in pdf_files:
        text = extract_text_from_pdf(pdf_path)

        if text:
            # Create output filename
            output_filename = pdf_path.stem + ".txt"
            output_path = output_dir / output_filename

            # Save extracted text
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(f"Source: {pdf_path.name}\n")
                f.write(f"{'='*80}\n\n")
                f.write(text)

            print(f"✓ Saved to: {output_path}\n")

    print(f"\n{'='*80}")
    print(f"Extraction complete! Text files saved in: {output_dir}")
    print(f"{'='*80}")

if __name__ == "__main__":
    main()
