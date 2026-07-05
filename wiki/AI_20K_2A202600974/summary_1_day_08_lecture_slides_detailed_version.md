---
type: summary
title: "Summary: 1-Day 08 Lecture Slides_Detailed version.pdf"
description: "A detailed summary of the Day 8 lecture slides covering the complete Retrieval-Augmented Generation (RAG) paradigm, from indexing and retrieval to generation and evaluation."
tags: [ai, 20k, day8, rag, retrieval, generation, evaluation]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/1-Day 08 Lecture Slides_Detailed version.pdf"]
---

# Summary: Day 8 Lecture Slides - Detailed Version

## Overview
This document summarizes the comprehensive lecture slides for Day 8 on the **RAG (Retrieval-Augmented Generation) Pipeline**. The lecture emphasizes that RAG is not just about adding context but is a synergistic orchestration of three main systems: Indexing, Retrieval, and Generation. It also covers evaluation frameworks, emphasizing that retrieval quality often dictates the final answer's quality.

## 1. The RAG Paradigm & Indexing Architecture
- **Why RAG?** LLMs suffer from "Knowledge Cutoff" and "Hallucination." Fine-tuning is expensive and poor at injecting factual data, whereas RAG acts like an "open-book exam," providing grounded facts, access control, and real-time updates.
- **Data-Centric AI:** The true bottleneck is often the retrieval system (80% of errors) rather than the LLM (20% of errors).
- **Indexing Pipeline:**
  - **Parsing:** Real-world data is messy (PDF layouts, tables). Solutions involve specialized parsers (LlamaParse, Unstructured) or Vision LLMs (Multimodal Parsing) to extract structural elements like Markdown/HTML.
  - **Data Cleaning:** Normalization and Redaction (che mờ PII).
  - **Ingestion Strategies:** Batch processing vs. Event-driven (Delta Sync) via webhooks to handle dynamic updates.
- **Advanced Chunking Strategies:**
  - *Fixed-Size:* Cuts mechanically, risks breaking semantic meaning.
  - *Recursive Chunking:* The standard approach (LangChain), respects paragraph and sentence boundaries.
  - *Semantic/Structural Chunking:* Uses Markdown headings or Abstract Syntax Trees (AST) for code.
  - *Small-to-Big Retrieval (Parent-Child):* Searches using small chunks for precision, but feeds the larger parent context to the LLM.
- **Embeddings & Metadata:**
  - *Vector Search* excels at semantics and paraphrase but fails at exact keyword matches (e.g., error codes like ERR-x09).
  - *Metadata Filtering:* Pre-filtering vs. Post-filtering. Pre-filtering is safer and faster.

## 2. Query Processing & Advanced Retrieval
- **Query Transformation:**
  - *Query Expansion:* Adds synonyms to fix user vocabulary gaps.
  - *Query Decomposition:* Splits multi-hop queries.
  - *Step-Back Prompting:* Abstracts overly detailed questions.
  - *HyDE (Hypothetical Document Embeddings):* Generates a fake answer and embeds it to find semantically similar real documents.
- **Dense vs. Sparse Retrieval:**
  - *Sparse (BM25):* Exact match, high weights for rare words, fast but blind to synonyms.
  - *Dense (Vector):* Semantic search, paraphrase-friendly, but misses exact IDs.
- **Hybrid Search & Reranking:**
  - Combines Dense and Sparse searches using **RRF (Reciprocal Rank Fusion)** or Alpha-tuning.
  - **Two-stage Reranking:** Uses broad Hybrid Search for Top-100, then applies a **Cross-Encoder** to deeply score relevance for the Top-5.
  - **MMR (Maximum Marginal Relevance):** Prevents redundancy in context windows by penalizing overly similar chunks.

## 3. Generation, Grounding & UX
- **Context Injection:**
  - The "Lost in the Middle" effect: LLMs remember the start and end of prompts best. Solution: **Document Reordering** (placing top results at the boundaries).
  - Use structured XML tags or Markdown to delineate system rules, context, and user questions. Limit context to ~60% of the token budget.
- **Prompt Engineering for Strict Grounding:**
  - Enforce citations (e.g., `[doc_1]`).
  - Graceful Degradation: Instruct the LLM to explicitly say "I don't know" or suggest alternatives when context is insufficient.
  - **Chain-of-Thought (CoT):** Force the LLM to outline its reasoning before generating the final answer.
- **Output UX:**
  - Create scannable outputs with inline citations, source blocks, and confidence scores.
  - Use streaming states ("Đang tìm kiếm...") to improve perceived latency.
- **Common Generation Failures:**
  - *Conflicting Context:* Instruct the LLM to prefer the most recent date.
  - *Over-extrapolation:* Enforce strict grounding to prevent the LLM from guessing outside the facts.

## 4. Evaluation, Production & Next Steps
- **The RAG Evaluation Triad (RAGAS):**
  1. **Context Recall:** Did the retriever find all necessary evidence?
  2. **Faithfulness:** Did the generator stick strictly to the retrieved facts without hallucinating?
  3. **Answer Relevance:** Did the answer actually address the user's question?
- **LLM-as-a-Judge:** Automating evaluation by having a powerful LLM grade the RAG outputs against a Golden Dataset.
- **A/B Testing:** Evaluate ROI for advanced features (e.g., Cross-encoder adds 5% relevance but increases latency by 3s). Implement data CI/CD to block deployments if metrics drop.
- **Agentic Future:** Single-pass RAG is evolving into Multi-Agent systems (using LangGraph) where Retrieval becomes just one of many tools an LLM can invoke.
