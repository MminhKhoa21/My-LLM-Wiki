import pypdf
import os
import json

pdf_dir = r'D:\Obsidian\My Wiki\raw\AI_20K_2A202600974\20'
result = {}

for f in os.listdir(pdf_dir):
    if f.endswith('.pdf'):
        try:
            reader = pypdf.PdfReader(os.path.join(pdf_dir, f))
            text = ''
            for page in reader.pages:
                text += page.extract_text() + '\n'
            result[f] = text
        except Exception as e:
            result[f] = f"Error: {e}"

with open('extracted_texts.json', 'w', encoding='utf-8') as out:
    json.dump(result, out, ensure_ascii=False, indent=2)
