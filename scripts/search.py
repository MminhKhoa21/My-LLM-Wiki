#!/usr/bin/env python3
import os
import argparse
from pathlib import Path

def search_files(query, search_dir, folder_label):
    results = []
    query_lower = query.lower()
    
    for file_path in search_dir.rglob("*"):
        if not file_path.is_file() or file_path.suffix not in [".md", ".txt", ".html"]:
            continue
            
        try:
            content = file_path.read_text(encoding="utf-8")
            lines = content.splitlines()
            matches = []
            
            # Check title first (especially for wiki markdown files)
            title_match = query_lower in file_path.name.lower()
            
            for idx, line in enumerate(lines, 1):
                if query_lower in line.lower():
                    matches.append((idx, line.strip()))
                    
            if title_match or matches:
                results.append({
                    "file_path": file_path,
                    "rel_path": file_path.relative_to(search_dir.parent),
                    "title_match": title_match,
                    "matches": matches
                })
        except Exception as e:
            # Skip binary or unreadable files silently
            pass
            
    return results

def main():
    parser = argparse.ArgumentParser(description="Search LLM Wiki and Raw sources.")
    parser.add_argument("--query", "-q", required=True, help="Search query string")
    args = parser.parse_args()
    
    root_dir = Path(__file__).parent.parent
    raw_dir = root_dir / "raw"
    wiki_dir = root_dir / "wiki"
    
    print(f"Searching for: '{args.query}' in {root_dir.resolve()}...\n")
    
    raw_results = search_files(args.query, raw_dir, "raw")
    wiki_results = search_files(args.query, wiki_dir, "wiki")
    
    print(f"=== Wiki Pages ({len(wiki_results)} matched) ===")
    for res in wiki_results:
        print(f"[WIKI] {res['rel_path']}")
        if res['title_match']:
            print("  -> File name matches query")
        for line_num, snippet in res['matches'][:5]: # Limit to 5 snippets per file
            print(f"  [{line_num}]: {snippet}")
        if len(res['matches']) > 5:
            print(f"  ... and {len(res['matches']) - 5} more matches.")
        print()
        
    print(f"=== Raw Sources ({len(raw_results)} matched) ===")
    for res in raw_results:
        print(f"[RAW] {res['rel_path']}")
        if res['title_match']:
            print("  -> File name matches query")
        for line_num, snippet in res['matches'][:5]:
            print(f"  [{line_num}]: {snippet}")
        if len(res['matches']) > 5:
            print(f"  ... and {len(res['matches']) - 5} more matches.")
        print()

if __name__ == "__main__":
    main()
