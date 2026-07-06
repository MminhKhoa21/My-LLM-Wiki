import os
import sys

try:
    import pypdf
except ImportError:
    os.system(sys.executable + " -m pip install pypdf")
    import pypdf

pdf_dir = r"D:\Obsidian\My Wiki\raw\AI_20K_2A202600974\21"
files = ["d21-slide-v0.pdf", "day06-fine-tuning-llms-tu-full-fine-tune-en-loraqlora.pdf", "day21-lab-instruction.pdf"]

for file in files:
    path = os.path.join(pdf_dir, file)
    try:
        reader = pypdf.PdfReader(path)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
        out_path = os.path.join(pdf_dir, file + ".txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"Extracted {file}")
    except Exception as e:
        print(f"Failed to extract {file}: {e}")
