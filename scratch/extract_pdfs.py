import os
from pypdf import PdfReader

pdf_dir = r"D:\Obsidian\My Wiki\raw\AI_20K_2A202600974\27"
output_dir = r"D:\Wiki\scratch"

for filename in os.listdir(pdf_dir):
    if filename.endswith(".pdf"):
        filepath = os.path.join(pdf_dir, filename)
        try:
            with open(filepath, 'rb') as f:
                reader = PdfReader(f)
                text = ""
                for page in reader.pages:
                    extracted = page.extract_text()
                    if extracted:
                        text += extracted + "\n"
            
            out_name = filename.replace('.pdf', '.txt')
            out_path = os.path.join(output_dir, out_name)
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(text)
            print(f"Extracted: {filename} to {out_name}")
        except Exception as e:
            print(f"Error on {filename}: {e}")
