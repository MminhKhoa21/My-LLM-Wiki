#!/usr/bin/env python3
import os
import re
from pathlib import Path

# Regex definitions
YAML_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(\.?/?([^)]+\.md)\)")

def parse_frontmatter(content):
    match = YAML_RE.match(content)
    if not match:
        return None
    yaml_text = match.group(1)
    metadata = {}
    for line in yaml_text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, val = line.split(":", 1)
            key = key.strip()
            val = val.strip()
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            if val.startswith('[') and val.endswith(']'):
                items = [item.strip().strip('"').strip("'") for item in val[1:-1].split(",") if item.strip()]
                val = items
            metadata[key] = val
    return metadata

def run_lint():
    wiki_dir = Path(__file__).parent.parent / "wiki"
    if not wiki_dir.exists():
        print(f"Error: wiki directory does not exist at {wiki_dir}")
        return False

    pages = {} # stem -> metadata and links
    all_stems = set()
    errors = []
    warnings = []
    
    # 1. Collect all pages
    for file_path in wiki_dir.glob("*.md"):
        stem = file_path.stem
        all_stems.add(stem)
        
        if stem in ["index", "log"]:
            continue
            
        try:
            content = file_path.read_text(encoding="utf-8")
            meta = parse_frontmatter(content)
            
            # Check schema integrity
            schema_errors = []
            required_fields = ["type", "title", "description", "tags", "timestamp", "sources"]
            if not meta:
                schema_errors.append("Missing YAML frontmatter block entirely.")
            else:
                for field in required_fields:
                    if field not in meta:
                        schema_errors.append(f"Missing required field: '{field}'")
                    else:
                        val = meta[field]
                        if field in ["tags", "sources"]:
                            if not isinstance(val, list):
                                schema_errors.append(f"Field '{field}' must be a list (got {type(val).__name__})")
                        else:
                            if val is None or val == "":
                                schema_errors.append(f"Field '{field}' is empty.")
            
            if schema_errors:
                errors.append((file_path.name, "Schema", schema_errors))
            
            # Extract links (strip code blocks and inline code first)
            clean_content = re.sub(r"```.*?```", "", content, flags=re.DOTALL)
            clean_content = re.sub(r"`.*?`", "", clean_content)
            
            wikilinks = WIKILINK_RE.findall(clean_content)
            md_links = MARKDOWN_LINK_RE.findall(clean_content)
            
            # Convert markdown links (e.g. 'neural_networks.md' -> 'neural_networks')
            normalized_md_links = []
            for link in md_links:
                link_stem = Path(link).stem
                normalized_md_links.append(link_stem)
                
            all_outbound = set(wikilinks + normalized_md_links)
            
            pages[stem] = {
                "file_name": file_path.name,
                "title": meta.get("title", stem) if meta else stem,
                "outbound_links": all_outbound,
                "meta": meta
            }
        except Exception as e:
            errors.append((file_path.name, "ReadError", [str(e)]))

    # 2. Link Integrity & Orphan Checks
    inbound_links = {stem: set() for stem in all_stems}
    
    for stem, data in pages.items():
        for target in data["outbound_links"]:
            # Clean target name (trim whitespaces, convert spaces to underscores if needed)
            # Standard Obsidian links might use spaces, but we encourage underscore or exact matches.
            target_clean = target.strip()
            
            # Check if link target exists in all_stems
            if target_clean not in all_stems:
                # Obsidian links with spaces can map to files with spaces or underscores. Let's check both
                target_alt = target_clean.replace(" ", "_")
                if target_alt in all_stems:
                    inbound_links[target_alt].add(stem)
                else:
                    errors.append((data["file_name"], "BrokenLink", [f"Link target [[{target}]] does not exist."]))
            else:
                inbound_links[target_clean].add(stem)

    # Orphan check (pages with 0 inbound links, ignoring index, log, overview)
    for stem, data in pages.items():
        if stem in ["overview"]:
            continue
        
        inbound = inbound_links.get(stem, set())
        # Filter out links from the page itself
        inbound_filtered = {lnk for lnk in inbound if lnk != stem}
        if not inbound_filtered:
            warnings.append((data["file_name"], "Orphan", ["This page has no inbound links from other pages."]))

    # Duplicate check (same title)
    titles = {}
    for stem, data in pages.items():
        title = data["title"].lower().strip()
        if title in titles:
            titles[title].append(data["file_name"])
        else:
            titles[title] = [data["file_name"]]
            
    for title, files in titles.items():
        if len(files) > 1:
            warnings.append((", ".join(files), "DuplicateTitle", [f"Multiple files share the title '{title}'"]))

    # 3. Output Report
    print("# Wiki Lint Report")
    print("=" * 30)
    print(f"Total Pages Scanned: {len(all_stems)}")
    print(f"Errors: {len(errors)} | Warnings: {len(warnings)}")
    print()
    
    if errors:
        print("## [ERROR] Errors (Required Fixes)")
        for file, category, msgs in errors:
            print(f"- **{file}** [{category}]:")
            for msg in msgs:
                print(f"  - {msg}")
        print()
        
    if warnings:
        print("## [WARN] Warnings (Optional Improvements)")
        for file, category, msgs in warnings:
            print(f"- **{file}** [{category}]:")
            for msg in msgs:
                print(f"  - {msg}")
        print()

    if not errors and not warnings:
        print("[OK] Wiki is healthy and structurally clean!")
        print()
        
    return len(errors) == 0

if __name__ == "__main__":
    import sys
    success = run_lint()
    sys.exit(0 if success else 1)
