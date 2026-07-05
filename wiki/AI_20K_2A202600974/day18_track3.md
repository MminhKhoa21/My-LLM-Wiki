---
type: summary
title: "Day 18 Track 3: Production RAG"
description: "Summary of building production-grade RAG systems, spanning offline ingestion, online retrieval, and RAGAS evaluation."
tags: [RAG, Retrieval Augmented Generation, Embeddings, Chunking, Hybrid Search, RAGAS]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-day18-production-rag.pdf"]
---

# Production RAG (Day 18 - Track 3)

**Instructor:** Tran Quang Thien

## 1. Map & Compass (RAG Architecture)
A production RAG pipeline consists of two main phases:
- **OFFLINE (Ingestion - 1 time):** Parse -> Chunk -> Enrich -> Embed -> Index. This phase sets the absolute ceiling for retrieval quality.
- **ONLINE (Querying - per query):** PreRAG -> Retrieve -> Rerank -> Augment -> Generate -> PostRAG.

## 2. OFFLINE Phase: Ingestion and Enrichment
- **Chunking Strategies:**
  - *Fixed-size:* Baseline.
  - *Semantic:* Splits by topic shifts.
  - *Hierarchical:* Finds small "child" chunks (e.g., 256 tokens) but injects the larger "parent" chunk (e.g., 2048 tokens) into the LLM for full context.
  - *Late Chunking:* Embeds the entire document first to capture global context, then pools embeddings for chunks.
  - *RAPTOR:* A recursive tree of summaries to answer high-level synthesis questions.
- **Enrichment Techniques:**
  - *Contextual Embeddings:* Using an LLM to prepend a context sentence to each chunk before embedding.
  - *Hypothetical Q&A:* Using an LLM to generate questions the chunk answers, then embedding the questions alongside the chunk.
  - *Matryoshka Representation Learning (MRL):* Flexible embedding dimensions to balance cost, latency, and precision.

## 3. ONLINE Phase: Retrieval and Reranking
- **Retrieval:**
  - *Hybrid + RRF:* Combines exact match (BM25) and semantic match (Dense Embeddings).
  - *Advanced Retrieval:* ColBERT (Token-level MaxSim), SPLADE (Learned sparse expansions), and ColPali (Vision-based retrieval that skips text parsing).
- **Reranking:**
  - Uses Cross-Encoders to re-score the top-K chunks from retrieval. Highly cost-effective way to boost precision (e.g., top-20 to top-3) at the cost of a slight latency increase (30-50ms).
- **PreRAG (Query Transformations):**
  - *HyDE:* Generates a hypothetical answer to embed and search.
  - *Multi-Query:* Breaks complex questions into simpler sub-queries.
  - *Corrective RAG (CRAG):* Evaluates retrieved chunks and decides whether to route to web search or rewrite the query.
- **Augmentation:** Filtering out contradictions (NLI), compressing context, and injecting citations.

## 4. Closing the Loop: Evaluation with RAGAS
Measure system health using RAGAS to pinpoint exactly which layer needs fixing.
- **Retrieval Metrics:**
  - *Context Recall:* Did we retrieve all necessary information? (Fix: Hybrid search, HyDE, metadata filtering)
  - *Context Precision:* Are relevant chunks ranked at the top? (Fix: Reranking)
- **Generation Metrics:**
  - *Faithfulness:* Does the answer stick to the provided context? (Fix: Prompt tuning, lowering temperature, citations)
  - *Answer Relevancy:* Does it directly answer the user's question? (Fix: Better prompts)

## 5. Embedding Limitations
Embeddings inherently struggle with:
- **Negation Insensitivity** (e.g., "allowed" vs "not allowed")
- **Entity Swapping**
- **Temporal Blindness** (e.g., policies from 2024 vs 2026)
- **Numerical Blindness**
*Solutions:* Use metadata filtering, post-retrieval NLI verification, and precise chunk enrichment.
