---
type: summary
title: "Summary: 1-day08-rag-pipeline-v2.pdf"
description: "A detailed summary of the Day 8 RAG Pipeline v2 slides focusing on bridging retrieval, augmentation, and generation, alongside pre-RAG query transformations and evaluation techniques."
tags: [ai, 20k, day8, rag, pipeline, augmentation]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/1-day08-rag-pipeline-v2.pdf"]
---
# Summary: RAG Pipeline v2

## Overview

## 1. Moving from Retrieval to RAG
- **Why RAG?** LLMs have knowledge cutoffs and are probabilistic by nature, leading to hallucinations. RAG solves this by providing dynamic, grounded context (like an open-book exam) instead of relying on expensive and static fine-tuning.
- **The R-A-G Triad:**
  - **Retrieval (R):** Finding the right evidence (Dense, Sparse, Hybrid search).
  - **Augmentation (A):** Structuring the context to mitigate "lost in the middle" effects and noise.
  - **Generation (G):** Producing a grounded answer with strict citations and self-checks.

## 2. Retrieval Deep Dive
- **Semantic vs. Lexical Search:**
  - *Dense Vector (Semantic):* Captures meaning, paraphrases, but struggles with exact keywords like IDs or codes.
  - *Sparse Vector (BM25):* Matches exact keywords fast but ignores context and synonyms.
- **Hybrid Search & Fusion:**
  - Combines both methods using **RRF (Reciprocal Rank Fusion)** or Alpha-weighting.
- **Reranking & MMR:**
  - After a broad top-K search, use a **Cross-Encoder** for precise relevance scoring.
  - Apply **MMR (Maximum Marginal Relevance)** to reduce redundant chunks and retain diverse context.

## 3. Augmentation Strategies
- **Context Injection:**
  - **Document Reordering:** Since LLMs recall the beginning and end of prompts better, place the most relevant documents at the boundaries `[1, 3, 5, 4, 2]`.
- **Grounding and Verification:**
  - Isolate System Rules, Context, and User Questions via XML tags.
  - Implement **Metadata Integration** and **Citation Formatting** to ensure accountability.
- **Token Budget Management:** Keep context under 60% of the token limit to avoid diluting the instruction. Use Context Compression if necessary.

## 4. Generation & Output Control
- **Model Selection & Formatting:** Choose models based on task complexity (e.g., local small models vs. large enterprise APIs). Standardize output via Markdown or JSON.
- **Safety and Alignment:** Filter PII and apply abstention rules ("Graceful Degradation" - admitting "I don't know" when context is missing).
- **Self-Correction & CoT:**
  - Use **Chain-of-Thought (CoT)** (`<thought_process>`) to force step-by-step reasoning before answering.
  - Implement self-checks against the context before presenting the final answer.
- **User Experience (UX):** Output format matters. Scannable text, inline citations, source popups, and streaming generation build user trust.

## 5. Pre-RAG & Agentic RAG
- **Query Transformation:**
  - Use LLMs to pre-process queries before vector searches: *Multi-Query* (variations), *HyDE* (hallucinated answers), *Query Expansion* (synonyms), *Decomposition* (splitting multi-hop queries), and *Step-Back Prompting* (abstraction).
  - Pre-filtering via metadata massively speeds up and focuses the search.
- **Agentic RAG:** Elevates the system to self-query, self-correct (C-RAG), and adapt. Retrieval becomes just one of many "tools" in a multi-agent system.

## 6. RAG Evaluation (RAGAS)
A "vibe check" is inadequate. A rigorous, automated evaluation framework involves three axes:
1. **Context Recall:** Did the retriever fetch the necessary documents?
2. **Faithfulness:** Is the LLM's answer loyal to the retrieved context?
3. **Answer Relevance:** Did the answer satisfy the user's prompt without wandering?
- Implementing CI/CD pipelines for AI involves testing the "behavior" of the AI against a Golden Dataset.
