import os
import re
from pathlib import Path

WIKI_DIR = Path(r"D:\Wiki\wiki\AI_20K_2A202600974")

VI_CHARS = set('áàảãạăắằẳẵặâấầẩẫậđéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ')

def is_vietnamese(text):
    count = sum(1 for c in text.lower() if c in VI_CHARS)
    return count > 0

def split_file(filepath):
    # Don't process already split files
    if filepath.name.endswith('.en.md') or filepath.name.endswith('.vi.md'):
        return

    content = filepath.read_text(encoding="utf-8")
    
    # Extract YAML frontmatter
    frontmatter = ""
    body = content
    match = re.match(r'^---\n.*?\n---\n', content, re.DOTALL)
    if match:
        frontmatter = match.group(0)
        body = content[match.end():]

    lines = body.split('\n')
    
    en_lines = []
    vi_lines = []
    
    in_code_block = False
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_code_block = not in_code_block
            en_lines.append(line)
            vi_lines.append(line)
            continue
            
        if in_code_block:
            en_lines.append(line)
            vi_lines.append(line)
            continue
            
        if not stripped:
            en_lines.append(line)
            vi_lines.append(line)
            continue
            
        # Images should be in both
        if re.match(r'^!\[.*?\]\(.*?\)$', stripped):
            en_lines.append(line)
            vi_lines.append(line)
            continue
            
        if is_vietnamese(line):
            vi_lines.append(line)
        else:
            # Check if it has any alphabet characters
            has_alpha = any(c.isalpha() for c in line)
            if not has_alpha:
                # E.g. symbols, separators like ---
                en_lines.append(line)
                vi_lines.append(line)
            else:
                en_lines.append(line)

    en_content = frontmatter + '\n'.join(en_lines)
    vi_content = frontmatter + '\n'.join(vi_lines)
    
    # Save the split files
    en_path = filepath.with_name(filepath.stem + '.en.md')
    vi_path = filepath.with_name(filepath.stem + '.vi.md')
    
    en_path.write_text(en_content, encoding="utf-8")
    vi_path.write_text(vi_content, encoding="utf-8")
    
    # Delete original
    filepath.unlink()

def main():
    count = 0
    for md_file in WIKI_DIR.rglob("*.md"):
        split_file(md_file)
        count += 1
    print(f"Finished splitting {count} files.")

if __name__ == "__main__":
    main()
