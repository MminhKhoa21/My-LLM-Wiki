import os
from pypdf import PdfReader

pdf_dir = r"D:\Obsidian\My Wiki\raw\AI_20K_2A202600974\25"
out_dir = r"D:\Wiki\scratch_pdfs"

os.makedirs(out_dir, exist_ok=True)

for file in os.listdir(pdf_dir):
    if file.endswith(".pdf"):
        path = os.path.join(pdf_dir, file)
        try:
            reader = PdfReader(path)
            text = ""
            for i, page in enumerate(reader.pages):
                text += f"--- Page {i+1} ---\n"
                text += page.extract_text() + "\n"
            
            out_name = file.replace(".pdf", ".txt")
            out_path = os.path.join(out_dir, out_name)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Extracted {file} to {out_name}")
        except Exception as e:
            print(f"Error extracting {file}: {e}")
