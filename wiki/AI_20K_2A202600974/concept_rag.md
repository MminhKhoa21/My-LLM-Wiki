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
*Trang này tổng hợp các kiến thức liên quan đến RAG được rải rác trong suốt khóa học.*

> **English:**  
> **RAG (Retrieval-Augmented Generation)** is a method that combines the power of retrieving information from external databases with the text generation capabilities of LLMs, helping to reduce hallucination and provide accurate context.  
> 
> *Vietnamese:*  
> ***RAG (Retrieval-Augmented Generation)** là phương pháp kết hợp sức mạnh truy xuất thông tin từ cơ sở dữ liệu bên ngoài với khả năng tạo văn bản của LLM, giúp giảm hallucination và cung cấp context chính xác.*

---

## The Evolution of RAG in the Course

**English:**  
RAG was introduced from the early days and has been continuously upgraded:

*Vietnamese:*  
*RAG được giới thiệu từ những ngày đầu và liên tục được nâng cấp:*

1. **Basic RAG (Day 8)**  
   - **English:** Basic concepts: Chunking, Embedding, Vector Database.  
     *Vietnamese:* *Khái niệm cơ bản: Chunking, Embedding, Vector Database.*  
   - **English:** Basic flow: User Query -> Retrieve Context -> LLM Generate.  
     *Vietnamese:* *Luồng cơ bản: User Query -> Retrieve Context -> LLM Generate.*  
   - **English:** Link: [[day8_overview]]  
     *Vietnamese:* *Liên kết: [[day8_overview]]*

2. **RAG & Agent (Day 18 - 20)**  
   - **English:** Integrating RAG into an Agent as a tool (Tool Calling).  
     *Vietnamese:* *Tích hợp RAG vào Agent như một tool (Tool Calling).*  
   - **English:** The Agent can automatically decide when to search for information using RAG.  
     *Vietnamese:* *Agent có thể tự động quyết định khi nào cần tìm kiếm thông tin bằng RAG.*  
   - **English:** Handling complex questions that require multiple lookups (Multi-hop reasoning).  
     *Vietnamese:* *Xử lý các câu hỏi phức tạp cần tra cứu nhiều bước (Multi-hop reasoning).*

3. **Evaluating RAG (Day 24)**  
   - **English:** Using **RAGAS** to measure the quality of the RAG pipeline.  
     *Vietnamese:* *Sử dụng **RAGAS** để đo lường chất lượng của RAG pipeline.*  
   - **English:** 4 core RAGAS metrics:  
     *Vietnamese:* *4 RAGAS metrics cốt lõi:*  
     - **English:** **Faithfulness**: Is the output faithful to the context? (Avoids hallucination).  
       *Vietnamese:* ***Faithfulness**: Output có trung thực với context không? (Tránh hallucination).*  
     - **English:** **Context Relevance**: Is the retrieved context relevant? (Evaluates the Retriever).  
       *Vietnamese:* ***Context Relevance**: Context được retrieve có liên quan không? (Đánh giá Retriever).*  
     - **English:** **Answer Relevance**: Does the answer stay on point with the question?  
       *Vietnamese:* ***Answer Relevance**: Trả lời có đúng trọng tâm câu hỏi không?*  
     - **English:** **Context Recall**: Did the retriever retrieve all necessary information?  
       *Vietnamese:* ***Context Recall**: Retriever có lấy đủ thông tin cần thiết không?*  
   - **English:** Link: [[day24_track3]]  
     *Vietnamese:* *Liên kết: [[day24_track3]]*

4. **System-Level RAG Optimization**  
   - **English:** RAG is not just about vector search. It needs to be combined with Keyword Search (BM25) to create Hybrid Search.  
     *Vietnamese:* *RAG không chỉ là vector search. Cần kết hợp Keyword Search (BM25) để tạo Hybrid Search.*  
   - **English:** Semantic Caching to save costs for repeated queries.  
     *Vietnamese:* *Semantic Caching để tiết kiệm chi phí cho các query lặp lại.*  
   - **English:** Monitoring Vector/Embedding (Drift, Stale vectors) through Data Observability: [[day27_track2]]  
     *Vietnamese:* *Quan sát Vector/Embedding (Drift, Stale vectors) theo Data Observability: [[day27_track2]]*

---

## When is RAG Not Enough?

**English:**  
As mentioned in the lesson on Fine-tuning ([[day21_track3]]):  
- **Fine-tuning does NOT fix knowledge gaps** – use RAG for knowledge.  
- But if the output format is complex, or the model needs to learn a specific "voice", it is necessary to combine RAG with Fine-tuning (such as LoRA/QLoRA).

*Vietnamese:*  
*Như đã đề cập trong bài học về Fine-tuning ([[day21_track3]]):*  
*- **Fine-tune KHÔNG fix knowledge gaps** – dùng RAG cho knowledge.*  
*- Nhưng nếu format đầu ra phức tạp, hoặc model cần học một "giọng văn" cụ thể, cần kết hợp RAG với Fine-tuning (như LoRA/QLoRA).*
