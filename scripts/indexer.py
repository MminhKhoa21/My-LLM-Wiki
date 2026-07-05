#!/usr/bin/env python3
import os
import re
from pathlib import Path

def parse_frontmatter(content):
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
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
            # Clean quotes
            if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
                val = val[1:-1]
            # Parse list if brackets [item1, item2]
            if val.startswith('[') and val.endswith(']'):
                items = [item.strip().strip('"').strip("'") for item in val[1:-1].split(",") if item.strip()]
                val = items
            metadata[key] = val
    return metadata

def generate_index():
    wiki_dir = Path(__file__).parent.parent / "wiki"
    if not wiki_dir.exists():
        print(f"Error: wiki directory does not exist at {wiki_dir}")
        return

    pages = []
    
    # Scan all markdown files in wiki/
    for file_path in wiki_dir.glob("*.md"):
        if file_path.name in ["index.md", "log.md"]:
            continue
        
        try:
            content = file_path.read_text(encoding="utf-8")
            meta = parse_frontmatter(content)
            if meta:
                pages.append({
                    "file_name": file_path.stem,
                    "title": meta.get("title", file_path.stem),
                    "description": meta.get("description", "No description provided."),
                    "type": meta.get("type", "unknown").lower(),
                    "tags": meta.get("tags", []),
                    "sources": meta.get("sources", []),
                    "timestamp": meta.get("timestamp", "")
                })
        except Exception as e:
            print(f"Warning: Failed to parse {file_path.name}: {e}")

    # Group pages by type
    groups = {}
    for page in pages:
        ptype = page["type"]
        if ptype not in groups:
            groups[ptype] = []
        groups[ptype].append(page)

    # Sort pages within groups alphabetically by title
    for ptype in groups:
        groups[ptype].sort(key=lambda x: x["title"].lower())

    # Build the index.md content
    lines = [
        "# Wiki Index",
        "",
        "Welcome to your LLM-maintained Knowledge Base index. This page is automatically updated by `scripts/indexer.py`.",
        "",
    ]

    # Order of sections to display
    type_order = ["overview", "summary", "concept", "entity", "unknown"]
    all_types = sorted(list(groups.keys()))
    for t in type_order:
        if t in all_types:
            all_types.remove(t)
            all_types.append(t) # Put ordered types first, others at the end

    type_labels = {
        "overview": "Overviews",
        "summary": "Source Summaries",
        "concept": "Concepts & Topics",
        "entity": "Entities & Tools",
        "unknown": "Unclassified Pages"
    }

    for ptype in type_order:
        if ptype not in groups or not groups[ptype]:
            continue
        
        label = type_labels.get(ptype, ptype.capitalize())
        lines.append(f"## {label}")
        lines.append("")
        
        # We can use markdown tables or list format. Let's use bullet list for cleaner view in Obsidian.
        for page in groups[ptype]:
            tags_str = f" *(Tags: {', '.join(page['tags'])})*" if page["tags"] else ""
            lines.append(f"- [[{page['file_name']}]] - **{page['title']}**: {page['description']}{tags_str}")
        lines.append("")

    # Write out index.md
    index_path = wiki_dir / "index.md"
    index_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"Successfully updated index.md with {len(pages)} pages.")

if __name__ == "__main__":
    generate_index()
