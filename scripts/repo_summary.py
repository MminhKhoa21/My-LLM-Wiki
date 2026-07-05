#!/usr/bin/env python3
"""
repo_summary.py — GitHub Repository Quick Summary Generator
Generates a beautiful Vietnamese HTML report for any GitHub repository.
"""
import sys
import re
import io
import json
import zipfile
import urllib.request
import urllib.error
import argparse
from pathlib import Path
from datetime import datetime

ROOT_DIR = Path("D:/Obsidian/My Wiki")
REPORTS_DIR = ROOT_DIR / "reports"
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"

REPORTS_DIR.mkdir(parents=True, exist_ok=True)

def load_env():
    env_vars = {}
    if ENV_PATH.exists():
        try:
            with open(ENV_PATH, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        k, v = line.split("=", 1)
                        env_vars[k.strip()] = v.strip()
        except Exception as e:
            print(f"[WARN] Failed to read .env: {e}")
    return env_vars

def sanitize_filename(name):
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "_", name)
    return name.lower().strip("_")

def extract_repo_info(url):
    """Parse owner/repo from GitHub URL."""
    match = re.match(r"https?://github\.com/([^/]+)/([^/?\s]+)", url.rstrip("/"))
    if not match:
        return None, None
    owner = match.group(1)
    repo = match.group(2).replace(".git", "")
    return owner, repo

def download_repo_content(owner, repo):
    """Download repo ZIP and extract key markdown/text files."""
    zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/main.zip"
    fallback_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/master.zip"
    
    content_parts = []
    
    for attempt_url in [zip_url, fallback_url]:
        try:
            req = urllib.request.Request(
                attempt_url,
                headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                zip_data = io.BytesIO(response.read())
                
            with zipfile.ZipFile(zip_data, "r") as zf:
                # Priority: README first, then docs, then other .md files
                names = zf.namelist()
                priority_files = []
                other_md = []
                
                for name in names:
                    lower = name.lower()
                    basename = name.split("/")[-1].lower()
                    # Skip deeply nested, binary, node_modules, vendor
                    if any(skip in lower for skip in ["node_modules", "vendor", ".git", "__pycache__"]):
                        continue
                    if basename in ["readme.md", "readme.txt", "readme.rst"]:
                        priority_files.insert(0, name)
                    elif basename in ["contributing.md", "changelog.md", "getting-started.md", "quickstart.md", "introduction.md"]:
                        priority_files.append(name)
                    elif lower.endswith(".md") and len(name.split("/")) <= 4:
                        other_md.append(name)

                selected = (priority_files + other_md)[:8]
                
                for fname in selected:
                    try:
                        text = zf.read(fname).decode("utf-8", errors="replace")
                        rel = "/".join(fname.split("/")[1:])
                        content_parts.append(f"### File: {rel}\n\n{text[:3000]}")
                    except Exception:
                        continue
                        
            if content_parts:
                return "\n\n---\n\n".join(content_parts)
        except Exception:
            continue
    
    return None

def call_mistral(prompt, system_prompt, env_vars):
    """Call Mistral AI API."""
    api_key = env_vars.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("No MISTRAL_API_KEY found in .env file.")
    
    model = env_vars.get("MISTRAL_MODEL", "mistral-small-latest")
    api_url = "https://api.mistral.ai/v1/chat/completions"
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4,
        "max_tokens": 2500
    }
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(api_url, data=data, headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=60) as response:
        res_body = response.read().decode("utf-8")
        res_data = json.loads(res_body)
        return res_data["choices"][0]["message"]["content"]

def generate_html_report(repo_url, owner, repo, ai_content, today):
    """Wrap AI content in a beautiful styled HTML report."""
    # Convert markdown-like AI output to basic HTML
    def md_to_html(text):
        # Headers
        text = re.sub(r"^### (.+)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)
        text = re.sub(r"^## (.+)$", r"<h2>\1</h2>", text, flags=re.MULTILINE)
        text = re.sub(r"^# (.+)$", r"<h1>\1</h1>", text, flags=re.MULTILINE)
        # Bold
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        # Italic
        text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
        # Inline code
        text = re.sub(r"`(.+?)`", r"<code>\1</code>", text)
        # Bullet points
        text = re.sub(r"^[-*] (.+)$", r"<li>\1</li>", text, flags=re.MULTILINE)
        # Numbered list
        text = re.sub(r"^\d+\. (.+)$", r"<li>\1</li>", text, flags=re.MULTILINE)
        # Wrap consecutive <li> in <ul>
        text = re.sub(r"(<li>.*?</li>\n?)+", lambda m: f"<ul>{m.group(0)}</ul>", text, flags=re.DOTALL)
        # Paragraphs
        paragraphs = []
        for block in text.split("\n\n"):
            block = block.strip()
            if not block:
                continue
            if block.startswith("<h") or block.startswith("<ul") or block.startswith("<ol"):
                paragraphs.append(block)
            else:
                paragraphs.append(f"<p>{block.replace(chr(10), '<br>')}</p>")
        return "\n".join(paragraphs)

    html_body = md_to_html(ai_content)
    
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Báo cáo: {owner}/{repo}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Inter', sans-serif;
            background: #0f1117;
            color: #e2e8f0;
            line-height: 1.7;
            min-height: 100vh;
        }}
        
        .report-wrapper {{
            max-width: 860px;
            margin: 0 auto;
            padding: 40px 24px;
        }}
        
        .report-header {{
            background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid rgba(99, 102, 241, 0.3);
            border-radius: 16px;
            padding: 32px;
            margin-bottom: 32px;
            position: relative;
            overflow: hidden;
        }}
        
        .report-header::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -20%;
            width: 300px;
            height: 300px;
            background: radial-gradient(circle, rgba(99,102,241,0.15) 0%, transparent 70%);
        }}
        
        .report-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(99, 102, 241, 0.15);
            border: 1px solid rgba(99, 102, 241, 0.3);
            color: #818cf8;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 11px;
            font-weight: 600;
            letter-spacing: 0.05em;
            text-transform: uppercase;
            margin-bottom: 16px;
        }}
        
        .report-title {{
            font-size: 28px;
            font-weight: 700;
            color: #f1f5f9;
            margin-bottom: 8px;
        }}
        
        .report-subtitle {{
            font-size: 14px;
            color: #94a3b8;
            margin-bottom: 20px;
        }}
        
        .report-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 12px;
        }}
        
        .meta-chip {{
            display: flex;
            align-items: center;
            gap: 6px;
            background: rgba(255,255,255,0.05);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 8px;
            padding: 6px 12px;
            font-size: 12px;
            color: #cbd5e1;
        }}
        
        .meta-chip a {{
            color: #818cf8;
            text-decoration: none;
        }}
        
        .meta-chip a:hover {{ text-decoration: underline; }}
        
        .report-body {{
            background: #1e293b;
            border: 1px solid rgba(255,255,255,0.08);
            border-radius: 16px;
            padding: 32px;
        }}
        
        h1, h2, h3 {{
            color: #f1f5f9;
            font-weight: 600;
            margin: 24px 0 12px 0;
        }}
        
        h1 {{ font-size: 22px; color: #818cf8; border-bottom: 1px solid rgba(99,102,241,0.3); padding-bottom: 8px; }}
        h2 {{ font-size: 18px; }}
        h3 {{ font-size: 15px; color: #a5b4fc; }}
        
        p {{ color: #cbd5e1; margin-bottom: 12px; }}
        
        ul, ol {{
            padding-left: 20px;
            margin-bottom: 16px;
        }}
        
        li {{
            color: #cbd5e1;
            margin-bottom: 6px;
        }}
        
        strong {{ color: #e2e8f0; font-weight: 600; }}
        em {{ color: #94a3b8; font-style: italic; }}
        
        code {{
            background: rgba(99,102,241,0.15);
            border: 1px solid rgba(99,102,241,0.2);
            border-radius: 4px;
            padding: 1px 6px;
            font-family: 'Fira Code', monospace;
            font-size: 12px;
            color: #a5b4fc;
        }}
        
        .source-link {{
            margin-top: 32px;
            padding: 16px 20px;
            background: rgba(99,102,241,0.08);
            border: 1px solid rgba(99,102,241,0.2);
            border-radius: 10px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .source-link span {{ font-size: 13px; color: #94a3b8; }}
        .source-link a {{
            color: #818cf8;
            text-decoration: none;
            font-weight: 500;
            font-size: 13px;
            word-break: break-all;
        }}
        .source-link a:hover {{ text-decoration: underline; }}
        
        .print-btn {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(135deg, #6366f1, #8b5cf6);
            color: white;
            border: none;
            border-radius: 50px;
            padding: 12px 24px;
            font-size: 14px;
            font-weight: 600;
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(99,102,241,0.4);
            display: flex;
            align-items: center;
            gap: 8px;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .print-btn:hover {{ transform: translateY(-2px); box-shadow: 0 12px 32px rgba(99,102,241,0.5); }}
        
        @media print {{
            body {{ background: white; color: #1e293b; }}
            .report-header {{ background: #f8fafc; border-color: #e2e8f0; }}
            .report-body {{ background: white; border-color: #e2e8f0; }}
            .print-btn {{ display: none; }}
            h1, h2, h3 {{ color: #1e293b; }}
            p, li {{ color: #475569; }}
            .report-title {{ color: #1e293b; }}
            .report-badge {{ background: #ede9fe; color: #6d28d9; border-color: #c4b5fd; }}
            code {{ background: #f1f5f9; border-color: #e2e8f0; color: #6366f1; }}
        }}
    </style>
</head>
<body>
    <div class="report-wrapper">
        <div class="report-header">
            <div class="report-badge">📦 Báo cáo GitHub Repository</div>
            <div class="report-title">{owner} / {repo}</div>
            <div class="report-subtitle">Phân tích và tóm tắt tự động bởi AI — bằng Tiếng Việt</div>
            <div class="report-meta">
                <div class="meta-chip">📅 {today}</div>
                <div class="meta-chip">🔗 <a href="{repo_url}" target="_blank">{repo_url}</a></div>
            </div>
        </div>
        
        <div class="report-body">
            {html_body}
            
            <div class="source-link">
                <span>🔗 Nguồn gốc:</span>
                <a href="{repo_url}" target="_blank">{repo_url}</a>
            </div>
        </div>
    </div>
    
    <button class="print-btn" onclick="window.print()">🖨️ In / Lưu PDF</button>
</body>
</html>"""

def generate_report(url):
    owner, repo = extract_repo_info(url)
    if not owner:
        print(f"Error: Invalid GitHub URL: {url}", file=sys.stderr)
        sys.exit(1)
    
    print(f"Đang tải nội dung từ {owner}/{repo}...")
    content = download_repo_content(owner, repo)
    
    if not content:
        print("Error: Could not download repository content.", file=sys.stderr)
        sys.exit(1)
    
    print(f"Đã tải {len(content)} ký tự. Đang gửi cho AI phân tích...")
    
    env_vars = load_env()
    
    system_prompt = (
        "Bạn là một chuyên gia phân tích mã nguồn và giáo dục công nghệ.\n"
        "Nhiệm vụ của bạn là đọc nội dung tài liệu từ một GitHub repository và viết một BÁO CÁO PHÂN TÍCH bằng TIẾNG VIỆT tự nhiên, rõ ràng.\n\n"
        "Báo cáo PHẢI có các phần sau (sử dụng heading ##):\n"
        "## 1. Tổng quan\n"
        "Repo này là gì? Giải quyết vấn đề gì? Ai là đối tượng sử dụng?\n\n"
        "## 2. Các tính năng chính\n"
        "Liệt kê bullet point các chức năng/tính năng chính của repo.\n\n"
        "## 3. Công nghệ & Ngôn ngữ sử dụng\n"
        "Tech stack, thư viện, framework, ngôn ngữ lập trình được sử dụng.\n\n"
        "## 4. Cấu trúc & Các thành phần quan trọng\n"
        "Mô tả các module, thư mục, hoặc file quan trọng trong repo.\n\n"
        "## 5. Độ khó & Phù hợp để học gì\n"
        "Đánh giá mức độ phức tạp (Mới học / Trung cấp / Nâng cao). Phù hợp để học kỹ năng gì?\n\n"
        "## 6. Điểm nổi bật & Nhận xét\n"
        "Những điểm đặc biệt hoặc thú vị của repo này. Có nên tham khảo không?\n\n"
        "Viết ngắn gọn, súc tích, dễ hiểu. Giữ thuật ngữ kỹ thuật trong ngoặc đơn tiếng Anh khi cần (ví dụ: Hàng đợi (Queue)).\n"
        "KHÔNG được viết bằng tiếng Anh. Toàn bộ nội dung phải bằng Tiếng Việt."
    )
    
    prompt = (
        f"Phân tích GitHub repository sau và viết báo cáo theo định dạng đã yêu cầu.\n"
        f"URL Repository: {url}\n\n"
        f"--- NỘI DUNG TÀI LIỆU ---\n"
        f"{content[:9000]}"
    )
    
    ai_content = call_mistral(prompt, system_prompt, env_vars)
    
    today = datetime.now().strftime("%Y-%m-%d")
    html = generate_html_report(url, owner, repo, ai_content, today)
    
    safe_repo = sanitize_filename(repo)
    filename = f"report_{safe_repo}_{today}.html"
    output_path = REPORTS_DIR / filename
    output_path.write_text(html, encoding="utf-8")
    
    print(f"SUCCESS: {filename}")
    print(f"PATH: {output_path}")
    print(f"AI_CONTENT_START")
    print(ai_content)
    print(f"AI_CONTENT_END")
    return str(output_path)

def main():
    parser = argparse.ArgumentParser(description="Generate Vietnamese HTML summary report for a GitHub repository.")
    parser.add_argument("--url", "-u", required=True, help="GitHub repository URL")
    args = parser.parse_args()
    generate_report(args.url)

if __name__ == "__main__":
    main()
