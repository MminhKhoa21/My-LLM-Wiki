import os
import pypdf

pdf_dir = r"D:\Obsidian\My Wiki\raw\AI_20K_2A202600974\23"
output_file = r"D:\Obsidian\My Wiki\raw\AI_20K_2A202600974\23\extracted_text.txt"

pdf_files = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]

with open(output_file, 'w', encoding='utf-8') as out:
    for pdf in pdf_files:
        path = os.path.join(pdf_dir, pdf)
        out.write(f"--- START OF {pdf} ---\n")
        try:
            reader = pypdf.PdfReader(path)
            out.write(f"Total Pages: {len(reader.pages)}\n")
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    out.write(text + "\n")
        except Exception as e:
            out.write(f"Error reading {pdf}: {e}\n")
        out.write(f"--- END OF {pdf} ---\n\n")

print(f"Extraction done. Check {output_file}")
