---
type: concept
title: "Retrieval-Augmented Generation (RAG)"
description: "Tổng hợp kiến thức về RAG qua các ngày trong khóa học AI 20K."
tags: [ai, 20k, concept, rag]
timestamp: 2026-07-05
sources: []
---


*Trang này tổng hợp các kiến thức liên quan đến RAG được rải rác trong suốt khóa học.*

> 
> ***RAG (Retrieval-Augmented Generation)** là phương pháp kết hợp sức mạnh truy xuất thông tin từ cơ sở dữ liệu bên ngoài với khả năng tạo văn bản của LLM, giúp giảm hallucination và cung cấp context chính xác.*

---



*RAG được giới thiệu từ những ngày đầu và liên tục được nâng cấp:*

     *Vietnamese:* *Khái niệm cơ bản: Chunking, Embedding, Vector Database.*  
     *Vietnamese:* *Luồng cơ bản: User Query -> Retrieve Context -> LLM Generate.*  
     *Vietnamese:* *Liên kết: [[day8_overview]]*

     *Vietnamese:* *Tích hợp RAG vào Agent như một tool (Tool Calling).*  
     *Vietnamese:* *Agent có thể tự động quyết định khi nào cần tìm kiếm thông tin bằng RAG.*  
     *Vietnamese:* *Xử lý các câu hỏi phức tạp cần tra cứu nhiều bước (Multi-hop reasoning).*

     *Vietnamese:* *Sử dụng **RAGAS** để đo lường chất lượng của RAG pipeline.*  
     *Vietnamese:* *4 RAGAS metrics cốt lõi:*  
       *Vietnamese:* ***Faithfulness**: Output có trung thực với context không? (Tránh hallucination).*  
       *Vietnamese:* ***Context Relevance**: Context được retrieve có liên quan không? (Đánh giá Retriever).*  
       *Vietnamese:* ***Answer Relevance**: Trả lời có đúng trọng tâm câu hỏi không?*  
       *Vietnamese:* ***Context Recall**: Retriever có lấy đủ thông tin cần thiết không?*  
     *Vietnamese:* *Liên kết: [[day24_track3]]*

     *Vietnamese:* *RAG không chỉ là vector search. Cần kết hợp Keyword Search (BM25) để tạo Hybrid Search.*  
     *Vietnamese:* *Semantic Caching để tiết kiệm chi phí cho các query lặp lại.*  
     *Vietnamese:* *Quan sát Vector/Embedding (Drift, Stale vectors) theo Data Observability: [[day27_track2]]*

---



*Như đã đề cập trong bài học về Fine-tuning ([[day21_track3]]):*  
*- **Fine-tune KHÔNG fix knowledge gaps** – dùng RAG cho knowledge.*  
*- Nhưng nếu format đầu ra phức tạp, hoặc model cần học một "giọng văn" cụ thể, cần kết hợp RAG với Fine-tuning (như LoRA/QLoRA).*
