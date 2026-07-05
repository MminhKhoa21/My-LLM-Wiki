#!/usr/bin/env python3
import sys
import re
import argparse
import urllib.request
import urllib.parse
import io
import zipfile
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

def fetch_and_save_single_file(raw_url, name, raw_dir):
    try:
        req = urllib.request.Request(
            raw_url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode("utf-8", errors="replace")
            
        filename = sanitize_filename(name)
        output_path = raw_dir / f"{filename}.txt"
        output_path.write_text(content, encoding="utf-8")
        print(f"Successfully clipped page and saved to: raw/{filename}.txt")
        return True
    except Exception as e:
        print(f"Error fetching raw file: {e}")
        return False

def handle_github_url(url, raw_dir):
    parsed = urllib.parse.urlparse(url)
    path_parts = [p for p in parsed.path.strip("/").split("/") if p]
    
    if parsed.netloc != "github.com" or len(path_parts) < 2:
        return False
        
    owner = path_parts[0]
    repo = path_parts[1]
    
    # 1. Check if it's a file blob URL: github.com/owner/repo/blob/branch/path/to/file
    if len(path_parts) >= 4 and path_parts[2] == "blob":
        branch = path_parts[3]
        file_path = "/".join(path_parts[4:])
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{file_path}"
        print(f"Detected GitHub blob URL. Rewriting to raw: {raw_url}")
        return fetch_and_save_single_file(raw_url, file_path.replace("/", "_"), raw_dir)
        
    # 2. Check if it's a repository root or a branch tree: github.com/owner/repo or github.com/owner/repo/tree/branch
    is_repo = False
    branch = "main"
    
    if len(path_parts) == 2:
        is_repo = True
    elif len(path_parts) >= 4 and path_parts[2] == "tree":
        is_repo = True
        branch = path_parts[3]
        
    if is_repo:
        print(f"Detected GitHub repository: {owner}/{repo} (branch: {branch})")
        zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip"
        
        # Download ZIP in-memory
        try:
            print(f"Downloading repository ZIP in-memory: {zip_url}...")
            req = urllib.request.Request(
                zip_url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            with urllib.request.urlopen(req, timeout=30) as response:
                zip_data = response.read()
        except Exception as e:
            if branch == "main":
                branch = "master"
                zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/master.zip"
                print(f"Main branch download failed. Retrying with master branch: {zip_url}...")
                try:
                    req = urllib.request.Request(
                        zip_url,
                        headers={'User-Agent': 'Mozilla/5.0'}
                    )
                    with urllib.request.urlopen(req, timeout=30) as response:
                        zip_data = response.read()
                except Exception as ex:
                    print(f"Error downloading repository ZIP: {ex}")
                    return False
            else:
                print(f"Error downloading repository ZIP: {e}")
                return False
                
        # Parse ZIP in-memory — combine ALL content into ONE single raw file
        try:
            print("Extracting markdown files from ZIP in-memory...")
            with zipfile.ZipFile(io.BytesIO(zip_data)) as z:
                md_files = [f for f in z.namelist() if f.lower().endswith(".md")]
                
                if not md_files:
                    print("No markdown files found in the repository.")
                    return False
                    
                # Sort: README.md first, then docs/, then others
                def sort_key(f):
                    f_lower = f.lower()
                    if "readme" in f_lower:
                        return (0, f)
                    if "docs/" in f_lower or "doc/" in f_lower:
                        return (1, f)
                    return (2, f)
                    
                md_files.sort(key=sort_key)
                files_to_extract = md_files[:20]  # top 20 docs
                print(f"Found {len(md_files)} markdown files. Combining top {len(files_to_extract)} into one source file...")
                
                # Combine ALL content into ONE file
                combined_parts = [
                    f"# GitHub Repository: {owner}/{repo}",
                    f"Source URL: https://github.com/{owner}/{repo}",
                    f"Branch: {branch}",
                    "---"
                ]
                for f in files_to_extract:
                    with z.open(f) as file_in_zip:
                        file_content = file_in_zip.read().decode("utf-8", errors="replace")
                    rel_path = "/".join(f.split("/")[1:])
                    if not rel_path:
                        continue
                    combined_parts.append(f"\n\n## [{rel_path}]\n\n{file_content[:4000]}")
                
                combined_text = "\n".join(combined_parts)
                output_filename = f"github_{sanitize_filename(repo)}.txt"
                output_path = raw_dir / output_filename
                output_path.write_text(combined_text, encoding="utf-8")
                print(f"Successfully combined into: raw/{output_filename}")
                return True
        except Exception as e:
            print(f"Error processing ZIP file: {e}")
            return False
            
    return False

def main():
    parser = argparse.ArgumentParser(description="Download and clean web pages into raw text.")
    parser.add_argument("--url", "-u", required=True, help="URL to download")
    parser.add_argument("--name", "-n", help="Output file name (excluding path and extension)")
    args = parser.parse_args()
    
    raw_dir = Path("D:/Obsidian/My Wiki/raw")
    raw_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Handle GitHub URLs (repositories or file paths)
    if handle_github_url(args.url, raw_dir):
        sys.exit(0)
        
    # 2. Fallback to standard Web Page Clipper
    print(f"Fetching URL: {args.url}...")
    try:
        req = urllib.request.Request(
            args.url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        )
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode("utf-8", errors="replace")
    except Exception as e:
        print(f"Error fetching URL: {e}")
        sys.exit(1)
        
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
