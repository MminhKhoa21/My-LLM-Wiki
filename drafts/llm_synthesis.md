<!-- target: wiki/llm_synthesis.md -->
<!-- title: LLM Synthesis -->
---
type: concept
title: "LLM Synthesis"
description: "The process by which the LLM reads raw study materials and produces structured markdown notes."
tags: [process, LLM, synthesis]
timestamp: 2026-07-05
sources: ["raw/test_overview.txt"]
---

# LLM Synthesis

LLM Synthesis is the second step of the [[summary_learning_wiki|learning wiki workflow]]. The language model ingests raw documents (e.g., lecture notes, textbook excerpts) from the `raw/` directory and generates formatted markdown files in the `wiki/` directory.

- **Input**: Unstructured or semi‑structured text from raw study materials.
- **Output**: Structured notes with YAML frontmatter, consistent tagging, and interlinks to other wiki pages.
- **Automation**: The LLM performs this task deterministically based on prompt instructions, ensuring that each source is turned into one or more wiki notes.

LLM Synthesis works in concert with [[Automated Indexing]] to keep the growing knowledge base organized and searchable.