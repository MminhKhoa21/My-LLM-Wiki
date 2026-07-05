#!/usr/bin/env python3
import sys
import re
import argparse
import urllib.request
import urllib.parse
from pathlib import Path

def sanitize_filename(name):
    # Keep only alphanumeric, space, hyphens, and underscores
    name = re.sub(r"[^\w\s-]", "", name)
    name = re.sub(r"\s+", "_", name)
    return name.lower().strip("_")

def clean_html(html_text):
    # Remove comments
    html_text = re.sub(r"<!--.*?-->", "", html_text, flags=re.DOTALL)
    # Remove script, style, and head
    html_text = re.sub(r"<head.*?>.*?</head>", "", html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r"<script.*?>.*?</script>", "", html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r"<style.*?>.*?</style>", "", html_text, flags=re.IGNORECASE | re.DOTALL)
    
    # Simple tag conversion to plain text structures
    html_text = re.sub(r"<h[1-6].*?>(.*?)</h[1-6]>", r"\n\n\1\n" + "="*15 + "\n", html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r"<p.*?>(.*?)</p>", r"\n\n\1\n", html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r"<li.*?>(.*?)</li>", r"\n- \1", html_text, flags=re.IGNORECASE | re.DOTALL)
    html_text = re.sub(r"<br\s*/?>", r"\n", html_text, flags=re.IGNORECASE)
    
    # Strip remaining HTML tags
    clean_text = re.sub(r"<.*?>", "", html_text)
    
    # Replace common HTML entities
    entities = {
        "&nbsp;": " ",
        "&amp;": "&",
        "&lt;": "<",
        "&gt;": ">",
        "&quot;": "\"",
        "&#39;": "'",
        "&rsquo;": "'",
        "&lsquo;": "'",
        "&ldquo;": "\"",
        "&rdquo;": "\"",
        "&ndash;": "-",
        "&mdash;": "--"
    }
    for ent, char in entities.items():
        clean_text = clean_text.replace(ent, char)
        
    # Collapse multiple blank lines
    clean_text = re.sub(r"\n\s*\n\s*\n+", "\n\n", clean_text)
    
    return clean_text.strip()

def main():
    parser = argparse.ArgumentParser(description="Download and clean web pages into raw text.")
    parser.add_argument("--url", "-u", required=True, help="URL to download")
    parser.add_argument("--name", "-n", help="Output file name (excluding path and extension)")
    args = parser.parse_args()
    
    root_dir = Path(__file__).parent.parent
    raw_dir = root_dir / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Fetching URL: {args.url}...")
    try:
        # Pretend to be a modern browser to avoid basic HTTP 403 blocks
        req = urllib.request.Request(
            args.url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)
        
    # Extract Title if not provided
    filename = args.name
    if not filename:
        title_match = re.search(r"<title.*?>(.*?)</title>", html, re.IGNORECASE)
        if title_match:
            filename = title_match.group(1)
        else:
            filename = "clipped_page"
            
    filename = sanitize_filename(filename)
    if not filename:
        filename = "clipped_page"
        
    clean_text = clean_html(html)
    
    output_path = raw_dir / f"{filename}.txt"
    try:
        output_path.write_text(clean_text, encoding="utf-8")
        print(f"Successfully clipped page and saved to: raw/{filename}.txt")
    except Exception as e:
        print(f"Error saving file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
