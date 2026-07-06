import pypdf
import sys
import os

pdf_path = sys.argv[1]
output_path = sys.argv[2]

try:
    with open(pdf_path, 'rb') as f:
        reader = pypdf.PdfReader(f)
        text = ''
        for i, page in enumerate(reader.pages):
            text += f"--- Page {i+1} ---\n"
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
        
        with open(output_path, 'w', encoding='utf-8') as out_f:
            out_f.write(text)
except Exception as e:
    print(f"Error processing {pdf_path}: {e}")
