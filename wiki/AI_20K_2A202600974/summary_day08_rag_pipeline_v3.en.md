---
type: summary
title: "Summary: day08-rag-pipeline-v3.pdf"
description: "A comprehensive summary of the Day 8 RAG Pipeline v3 slides outlining core concepts of retrieval, prompt augmentation, generative self-correction, and rigorous evaluation using RAGAS."
tags: [ai, 20k, day8, rag, pipeline, evaluation, hybrid_search]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/day08-rag-pipeline-v3.pdf"]
---

# Summary: RAG Pipeline v3

## Overview

## 1. Fundamentals of RAG
- **The "Why" of RAG:** LLMs inherently lack real-time internal data, have knowledge cutoffs, and tend to hallucinate to cover up missing facts. Fine-tuning models to memorize enterprise data is costly and inefficient. RAG circumvents this by fetching grounded evidence dynamically.
- **Core Components:**
  - **R (Retrieval):** Fetching accurate, relevant chunks using semantic and lexical search.
  - **A (Augmentation):** Formatting the raw context to prevent cognitive overload for the LLM.
  - **G (Generation):** Formulating a constrained, factual response complete with citations.

## 2. Advanced Retrieval Mechanics
- **Dense vs. Sparse Search:**
  - *Dense Vectors:* Good for general semantic matching (captures paraphrasing).
  - *Sparse Vectors (BM25):* Critical for exact matches like product codes, SKUs, and specific names.
- **Hybrid Search Strategy:** Unifies Dense and Sparse using **Reciprocal Rank Fusion (RRF)** or **Alpha Weighting** to score documents optimally.
- **Reranking:** To solve the problem of precise relevance, a two-stage approach is used. A broad search retrieves Top-100 items, and a slower, more accurate **Cross-Encoder** reranks them to present the Top-5.
- **MMR (Maximum Marginal Relevance):** An algorithm used to select chunks that are not only relevant but also diverse, reducing redundant context chunks.

## 3. Augmentation and Prompt Strategies
- **Context Injection & The "Lost in the Middle" Effect:**
  - LLMs tend to ignore information buried in the middle of a large prompt.
  - Solution: **Document Reordering** to place the most critical chunks at the top and bottom of the prompt array.
- **Token Budget Management:** Keeping context data within 60% of the token limit allows the model sufficient headroom for instructions and generated output.
- **Instruction Tuning:** Use clear delimitations (like XML tags `<context>...</context>`) to separate system rules from raw evidence.

## 4. Grounded Generation
- **Strict Grounding:** The model must be explicitly instructed to answer *only* from the provided context. If the data is absent, it must trigger a "Graceful Degradation" (i.e., gracefully declining to answer).
- **Forcing Citations:** Responses must be tied directly back to `[doc_id]`s to ensure auditability.
- **Self-Correction & CoT:** Prompting the LLM to write out a `<thought_process>` before finalizing its answer drastically reduces reasoning errors, especially on conflicting documents.

## 5. Pre-RAG Query Transformations
- Queries are often short, ambiguous, or poorly phrased.
- **Techniques to clean queries:**
  - *Pre-Filtering:* Utilizing metadata to narrow the search scope.
  - *HyDE & Multi-Query:* Expanding queries artificially or hallucinating ideal answers to act as better vector targets.
  - *Decomposition & Step-Back:* Breaking down multi-hop questions into parallel queries or abstracting overly detailed requests.

## 6. The RAG Evaluation Triad
- Replacing human "Vibe Checks" with automated, metrics-driven evaluations using frameworks like **RAGAS**.
- **The Triad:**
  1. **Context Recall:** Did we fetch all the necessary facts? (Low score -> Fix Retriever)
  2. **Faithfulness:** Is the answer hallucination-free? (Low score -> Fix Generation/Prompt)
  3. **Answer Relevance:** Is the answer on-topic?
- Implementing an "LLM-as-a-Judge" pipeline allows for rapid, continuous CI/CD evaluation of the RAG system against a Golden Dataset.
