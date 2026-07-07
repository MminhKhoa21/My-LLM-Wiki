---
type: concept
title: "Retrieval-Augmented Generation (RAG)"
description: "Tổng hợp kiến thức về RAG qua các ngày trong khóa học AI 20K."
tags: [ai, 20k, concept, rag]
timestamp: 2026-07-05
sources: []
---
# Retrieval-Augmented Generation (RAG)

**English:**  
This page consolidates the knowledge about RAG that is scattered throughout the course.

*Vietnamese:*  

> **English:**  
> **RAG (Retrieval-Augmented Generation)** is a method that combines the power of retrieving information from external databases with the text generation capabilities of LLMs, helping to reduce hallucination and provide accurate context.  
> 
> *Vietnamese:*  

---

## The Evolution of RAG in the Course

**English:**  
RAG was introduced from the early days and has been continuously upgraded:

*Vietnamese:*  

1. **Basic RAG (Day 8)**  
   - **English:** Basic concepts: Chunking, Embedding, Vector Database.  
   - **English:** Basic flow: User Query -> Retrieve Context -> LLM Generate.  
   - **English:** Link: [[day8_overview]]  

2. **RAG & Agent (Day 18 - 20)**  
   - **English:** Integrating RAG into an Agent as a tool (Tool Calling).  
   - **English:** The Agent can automatically decide when to search for information using RAG.  
   - **English:** Handling complex questions that require multiple lookups (Multi-hop reasoning).  

3. **Evaluating RAG (Day 24)**  
   - **English:** Using **RAGAS** to measure the quality of the RAG pipeline.  
   - **English:** 4 core RAGAS metrics:  
     - **English:** **Faithfulness**: Is the output faithful to the context? (Avoids hallucination).  
     - **English:** **Context Relevance**: Is the retrieved context relevant? (Evaluates the Retriever).  
     - **English:** **Answer Relevance**: Does the answer stay on point with the question?  
     - **English:** **Context Recall**: Did the retriever retrieve all necessary information?  
   - **English:** Link: [[day24_track3]]  

4. **System-Level RAG Optimization**  
   - **English:** RAG is not just about vector search. It needs to be combined with Keyword Search (BM25) to create Hybrid Search.  
   - **English:** Semantic Caching to save costs for repeated queries.  
   - **English:** Monitoring Vector/Embedding (Drift, Stale vectors) through Data Observability: [[day27_track2]]  

---

## When is RAG Not Enough?

**English:**  
As mentioned in the lesson on Fine-tuning ([[day21_track3]]):  
- **Fine-tuning does NOT fix knowledge gaps** – use RAG for knowledge.  
- But if the output format is complex, or the model needs to learn a specific "voice", it is necessary to combine RAG with Fine-tuning (such as LoRA/QLoRA).

*Vietnamese:*  
