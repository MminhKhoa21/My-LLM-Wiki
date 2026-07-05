# LLM Wiki Workspace Guidelines

You are the maintainer of this LLM Wiki workspace. Follow these rules and schema requirements strictly whenever ingesting new sources, answering queries, or editing wiki pages.

---

## 1. Directory Structure

- `raw/`: Raw learning materials and sources. Immutable. Do NOT modify.
- `wiki/`: Core wiki pages. You have full edit access here.
  - `wiki/index.md`: Auto-generated content catalog (do NOT edit manually, run the indexer script instead).
  - `wiki/log.md`: Chronological log of operations. Append new entries here.
  - `wiki/overview.md`: High-level landing page summarizing the current state of knowledge.
  - `wiki/*.md`: Individual concept, topic, or summary pages.

---

## 2. File Schema & Metadata

Every markdown file in `wiki/` (except `index.md` and `log.md`) MUST start with a YAML frontmatter block containing precisely the following fields:

```yaml
---
type: concept | entity | summary | overview
title: "Clear, concise title of the page"
description: "A brief one-sentence summary of the page content"
tags: [tag1, tag2, tag3]
timestamp: YYYY-MM-DD
sources: ["relative/path/to/raw/source.txt", "optional external URL"]
---
```

### Definitions:
- `type`:
  - `concept`: A general idea, theorem, formula, or topic (e.g., "Backpropagation", "Linear Algebra Limits").
  - `entity`: A specific person, tool, model, database, or project (e.g., "PyTorch", "Andrej Karpathy").
  - `summary`: A structured summary of a specific raw source document.
  - `overview`: High-level summaries pointing to concepts and entities.
- `timestamp`: The date the page was created or last updated (in `YYYY-MM-DD` format).
- `sources`: An array of file paths in `raw/` or external URLs that this page is based on.

---

## 3. Linking Conventions

- Use standard Obsidian-style double bracket wikilinks: `[[target_page]]` (without `.md` extension) to link to other pages in the wiki directory.
- Alternatively, use standard relative markdown links: `[Anchor Text](target_page.md)`.
- Link to raw files using relative paths: `[Source Document](../raw/document.txt)`.
- When writing about a concept or entity that is mentioned elsewhere, check if a page exists. If it does, link to it. If it doesn't, write its name as `[[concept_name]]` to mark it as a future page to be created.

---

## 4. Operation Workflows

### Ingestion Workflow (Adding new sources)
1. Add the source document to `raw/` (or locate it if already added).
2. Read the source file.
3. Extract key concepts, formulas, entities, and definitions.
4. Create a `summary` page for the source, e.g., `wiki/summary_source_name.md`.
5. Identify existing `concept` or `entity` pages that should be updated. Update them to integrate the new knowledge. Ensure you update their `timestamp` and append the new source to their `sources` list.
6. If a new concept or entity is introduced, create a new `concept` or `entity` page for it with proper YAML frontmatter.
7. Run the indexer script: `python scripts/indexer.py` (this automatically updates `wiki/index.md`).
8. Append an entry to `wiki/log.md` detailing the ingestion (e.g., `## [YYYY-MM-DD] ingest | Title of source`).
9. Run the linter script: `python scripts/linter.py` to ensure everything is healthy.

### Query Workflow (Answering questions)
1. Search the wiki for relevant pages using the search script: `python scripts/search.py --query "keyword"`.
2. Read the relevant pages.
3. Formulate a synthesized response. Cite the relevant wiki pages using `[[page_name]]`.
4. If the query results in a valuable comparison, synthesis, or new concept, ask the user if you should save it as a new page in `wiki/`.

### Linting Workflow (Health check)
1. Run `python scripts/linter.py`.
2. Review the output report.
3. Address schema errors, broken links, and orphan pages. Do NOT delete files without user permission.
