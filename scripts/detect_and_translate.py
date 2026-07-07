import os
import re
import json
import urllib.request
import urllib.parse
from pathlib import Path
from dotenv import load_dotenv

WORKSPACE_ROOT = Path(r"D:\Wiki")
load_dotenv(WORKSPACE_ROOT / ".env")

API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = os.getenv("DEEPSEEK_API_URL", "https://api.deepseek.com")
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
WIKI_DIR = WORKSPACE_ROOT / "wiki" / "AI_20K_2A202600974"

def detect_missing_language(content):
    # Remove frontmatter
    content_body = re.sub(r"^---[\s\S]*?---\n", "", content)
    
    # Vietnamese specific characters
    vn_chars = "áàảãạăắằẳẵặâấầẩẫậđéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵ"
    vn_count = sum(1 for c in content_body.lower() if c in vn_chars)
    
    # Common English stop words
    en_words = {"the", "is", "are", "and", "in", "to", "of", "for", "with", "this", "that", "it"}
    words = re.findall(r'\b[a-zA-Z]+\b', content_body.lower())
    en_count = sum(1 for w in words if w in en_words)
    
    total_chars = len(content_body)
    total_words = len(words)
    
    if total_chars == 0 or total_words == 0:
        return "Bilingual" # Skip empty
        
    vn_ratio = vn_count / total_chars
    en_ratio = en_count / total_words
    
    # Heuristics
    # If vn_ratio < 0.005 (0.5%), it's missing Vietnamese
    if vn_ratio < 0.005:
        return "Missing Vietnamese"
        
    # If en_ratio < 0.02 (2%), it's missing English
    if en_ratio < 0.01:
        return "Missing English"
        
    return "Bilingual"

def translate_content(content, missing_lang, filename):
    content_body = re.sub(r"^---[\s\S]*?---\n", "", content)
    frontmatter_match = re.match(r"^---[\s\S]*?---\n", content)
    frontmatter = frontmatter_match.group(0) if frontmatter_match else ""
    
    prompt = f"""
Bạn là một dịch giả chuyên nghiệp. Dưới đây là nội dung của file `{filename}`.
File này đang bị thiếu ngôn ngữ ({missing_lang}).
Nhiệm vụ của bạn: Hãy làm cho nội dung này trở thành SONG NGỮ (Anh - Việt).
Quy tắc:
- Giữ nguyên định dạng Markdown (headers, lists, code blocks, tables).
- Với mỗi đoạn văn, câu hỏi hoặc gạch đầu dòng, hãy trình bày tiếng Anh trước, và ngay bên dưới là bản dịch tiếng Việt in nghiêng (hoặc ngược lại tùy bạn, miễn là rõ ràng có cả 2).
- Không dịch nội dung của YAML frontmatter, tôi sẽ tự lo phần đó. Chỉ dịch nội dung chính dưới đây.

Nội dung:
{content_body}
"""

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2
    }
    
    req = urllib.request.Request(
        f"{API_URL.rstrip('/')}/chat/completions",
        data=json.dumps(data).encode('utf-8'),
        headers=headers
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            translated = result['choices'][0]['message']['content']
            # Make sure we don't duplicate frontmatter if AI added it
            translated = re.sub(r"^---[\s\S]*?---\n", "", translated)
            return frontmatter + translated + "\n"
    except Exception as e:
        print(f"Error translating {filename}: {e}")
        return None

def main():
    if not API_KEY:
        print("API Key not found.")
        return

    files_to_translate = []
    
    # Scan all markdown files
    for filepath in WIKI_DIR.glob("*.md"):
        content = filepath.read_text(encoding="utf-8")
        status = detect_missing_language(content)
        
        if status != "Bilingual":
            files_to_translate.append((filepath, status))
            
    print(f"Found {len(files_to_translate)} files that need translation.")
    for f, status in files_to_translate:
        print(f"- {f.name}: {status}")
        
    print("\nStarting translation process...")
    for filepath, status in files_to_translate:
        print(f"Processing {filepath.name} ({status})...")
        content = filepath.read_text(encoding="utf-8")
        new_content = translate_content(content, status, filepath.name)
        if new_content:
            filepath.write_text(new_content, encoding="utf-8")
            print(f"-> Translated and saved {filepath.name}")
            
    print("\nDone!")

if __name__ == "__main__":
    main()
