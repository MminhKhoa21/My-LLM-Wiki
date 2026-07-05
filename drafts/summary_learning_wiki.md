<!-- target: wiki/summary_learning_wiki.md -->
<!-- title: Learning Wiki Overview -->
---
type: summary
title: "Learning Wiki Overview"
description: "The primary entry point and high-level summary of your personal learning wiki."
tags: [learning, meta, documentation]
timestamp: 2026-07-05
sources: ["raw/test_overview.txt"]
---

# Personal Learning Wiki

This wiki is an AI-managed knowledge base that compiles and aggregates information from raw study materials (lecture notes, textbook chapters, articles) into a structured, interlinked set of notes.

## How It Works
1. **Raw Materials**: New learning documents are placed in the `raw/` directory.
2. **[[LLM Synthesis]]**: The LLM reads these sources and synthesizes them into structured markdown notes in the `wiki/` directory.
3. **[[Automated Indexing]]**: Deterministic Python scripts maintain a catalog of concepts and entities in the index file.
4. **Link Integrity**: Everything is interlinked using `[[wiki-links]]` to form a graph of knowledge.

## Quick Links
- [[index]] – The full auto-generated index of all concepts, entities, and summaries.
- [[log]] – Chronological log of ingestion, query, and maintenance operations.

## Major Learning Areas
### Mathematics (Calculus)
- [[summary_calculus_derivatives]] – Summary of Calculus Derivatives Study Guide.
- [[summary_calculus_integrals]] – Summary of Calculus Integrals Study Guide.
- [[derivative]] – Definition and core principles of the derivative.
- [[integral]] – Definition and core principles of the integral.
- [[differentiation_rules]] – Standard algebraic rules for differentiation.