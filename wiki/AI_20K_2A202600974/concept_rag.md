---
type: concept
title: "Retrieval-Augmented Generation (RAG)"
description: "Tổng hợp kiến thức về RAG qua các ngày trong khóa học AI 20K."
tags: [ai, 20k, concept, rag]
timestamp: 2026-07-05
sources: []
---

# Retrieval-Augmented Generation (RAG)

Trang này tổng hợp các kiến thức liên quan đến RAG được rải rác trong suốt khóa học. 

> **RAG (Retrieval-Augmented Generation)** là phương pháp kết hợp sức mạnh truy xuất thông tin từ cơ sở dữ liệu bên ngoài với khả năng tạo văn bản của LLM, giúp giảm hallucination và cung cấp context chính xác.

## Sự tiến hóa của RAG trong khóa học

RAG được giới thiệu từ những ngày đầu và liên tục được nâng cấp:

1. **RAG Cơ bản (Day 8)**
   - Khái niệm cơ bản: Chunking, Embedding, Vector Database.
   - Luồng cơ bản: User Query -> Retrieve Context -> LLM Generate.
   - Liên kết: [[day8_overview]]

2. **RAG & Agent (Day 18 - 20)**
   - Tích hợp RAG vào Agent như một tool (Tool Calling).
   - Agent có thể tự động quyết định khi nào cần tìm kiếm thông tin bằng RAG.
   - Xử lý các câu hỏi phức tạp cần tra cứu nhiều bước (Multi-hop reasoning).

3. **Đánh giá RAG (Day 24)**
   - Sử dụng **RAGAS** để đo lường chất lượng của RAG pipeline.
   - 4 RAGAS metrics cốt lõi:
     - **Faithfulness**: Output có trung thực với context không? (Tránh hallucination).
     - **Context Relevance**: Context được retrieve có liên quan không? (Đánh giá Retriever).
     - **Answer Relevance**: Trả lời có đúng trọng tâm câu hỏi không?
     - **Context Recall**: Retriever có lấy đủ thông tin cần thiết không?
   - Liên kết: [[day24_track3]]

4. **Tối ưu hóa RAG ở cấp độ hệ thống**
   - RAG không chỉ là vector search. Cần kết hợp Keyword Search (BM25) để tạo Hybrid Search.
   - Semantic Caching để tiết kiệm chi phí cho các query lặp lại.
   - Quan sát Vector/Embedding (Drift, Stale vectors) theo Data Observability: [[day27_track2]]

---

## Khi nào RAG không đủ?

Như đã đề cập trong bài học về Fine-tuning ([[day21_track3]]):
- **Fine-tune KHÔNG fix knowledge gaps** – dùng RAG cho knowledge. 
- Nhưng nếu format đầu ra phức tạp, hoặc model cần học một "giọng văn" cụ thể, cần kết hợp RAG với Fine-tuning (như LoRA/QLoRA).
