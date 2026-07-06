import os
import json
import re
from pathlib import Path
import urllib.request
import urllib.parse
from dotenv import load_dotenv

# Hardcode workspace root for reliability
WORKSPACE_ROOT = Path(r"D:\Wiki")

# Load environment variables
load_dotenv(WORKSPACE_ROOT / ".env")

API_KEY = os.getenv("DEEPSEEK_API_KEY")
API_URL = os.getenv("DEEPSEEK_API_URL", "https://api.deepseek.com")
MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

if not API_KEY:
    print("DEEPSEEK_API_KEY not found in D:\\Wiki\\.env")
    exit(1)

WIKI_DIR = WORKSPACE_ROOT / "wiki" / "AI_20K_2A202600974"

def generate_questions(content, track_name, day_num):
    prompt = f"""
Bạn là một trợ lý giảng dạy chuyên nghiệp.
Dưới đây là nội dung bài giảng của Ngày {day_num} thuộc {track_name}.
Hãy sinh ra 3-5 câu hỏi trắc nghiệm ngắn gọn để ôn tập kiến thức cốt lõi.
Bắt buộc định dạng theo Markdown, không cần chào hỏi.
Định dạng:
### Câu hỏi ôn tập Ngày {day_num}
1. [Câu hỏi]
   - A. ...
   - B. ...
   - C. ...
   - D. ...
   **Đáp án:** ...
   
Nội dung bài giảng:
{content}
"""
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    
    data = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }
    
    req = urllib.request.Request(
        f"{API_URL.rstrip('/')}/chat/completions",
        data=json.dumps(data).encode('utf-8'),
        headers=headers
    )
    
    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read().decode('utf-8'))
            return result['choices'][0]['message']['content']
    except Exception as e:
        print(f"Error generating questions for Day {day_num} {track_name}: {e}")
        return None

def main():
    tracks = ["track1", "track2", "track3"]
    
    for track in tracks:
        print(f"Processing {track}...")
        all_questions = [f"---\ntype: summary\ntitle: \"Câu hỏi ôn tập - {track.capitalize()}\"\ndescription: \"Bộ câu hỏi ôn tập tổng hợp cho {track.capitalize()}\"\ntags: [review, {track}]\ntimestamp: 2026-07-06\nsources: []\n---\n\n# Bộ câu hỏi ôn tập {track.capitalize()}\n"]
        
        has_content = False
        
        for day in range(1, 29):
            file_name = f"day{day}_{track}.md"
            file_path = WIKI_DIR / file_name
            
            if not file_path.exists():
                continue
                
            print(f"  Reading {file_name}...")
            content = file_path.read_text(encoding="utf-8")
            
            # Extract content without frontmatter to save tokens
            content_body = re.sub(r"^---[\s\S]*?---\n", "", content)
            
            questions = generate_questions(content_body, track, day)
            if questions:
                all_questions.append(questions)
                all_questions.append("\n---\n")
                has_content = True
                
        if has_content:
            out_file = WIKI_DIR / f"review_questions_{track}.md"
            out_file.write_text("\n".join(all_questions), encoding="utf-8")
            print(f"-> Saved {out_file.name}")

if __name__ == "__main__":
    main()
