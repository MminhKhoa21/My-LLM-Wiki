<!-- target: wiki/automated_indexing.md -->
<!-- title: Automated Indexing -->
---
type: concept
title: "Automated Indexing"
description: "The process of maintaining a catalog of concepts and entities in the index file via deterministic scripts."
tags: [process, indexing, catalog]
timestamp: 2026-07-05
sources: ["raw/test_overview.txt"]
---

# Automated Indexing

Automated Indexing is the third step of the [[summary_learning_wiki|learning wiki workflow]]. After [[LLM Synthesis]] creates structured notes, a set of deterministic Python scripts scans the `wiki/` directory and updates the [[index]] file.

- **Purpose**: To provide a single, searchable catalog of all concepts, entities, and summaries present in the wiki.
- **Method**: The scripts parse YAML frontmatter and `[[wiki-links]]` to extract tags, titles, and cross‑references.
- **Output**: A living [[index]] file that lists every page and its relationships, enabling quick navigation and graph‑based knowledge discovery.

Automated Indexing ensures link integrity and makes the entire wiki navigable without manual effort.