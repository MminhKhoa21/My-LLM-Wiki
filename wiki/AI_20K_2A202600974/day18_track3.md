---
type: summary
title: "Day 18 Track 3: Production RAG"
description: "Summary of building production-grade RAG systems, spanning offline ingestion, online retrieval, and RAGAS evaluation."
tags: [RAG, Retrieval Augmented Generation, Embeddings, Chunking, Hybrid Search, RAGAS]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-day18-production-rag.pdf"]
---
# Production RAG (Day 18 - Track 3)
# Production RAG (Ngày 18 - Track 3)

**Instructor:** Tran Quang Thien  
**Giảng viên:** Tran Quang Thien

## 1. Map & Compass (RAG Architecture)
## 1. Bản đồ & La bàn (Kiến trúc RAG)

A production RAG pipeline consists of two main phases:  
Một pipeline RAG trong sản xuất bao gồm hai giai đoạn chính:

- **OFFLINE (Ingestion - 1 time):** Parse -> Chunk -> Enrich -> Embed -> Index. This phase sets the absolute ceiling for retrieval quality.  
- **OFFLINE (Tiếp nhận - 1 lần):** Phân tích cú pháp -> Chunk -> Làm giàu -> Embed -> Index. Giai đoạn này đặt ra trần tuyệt đối cho chất lượng truy xuất.

- **ONLINE (Querying - per query):** PreRAG -> Retrieve -> Rerank -> Augment -> Generate -> PostRAG.  
- **ONLINE (Truy vấn - mỗi truy vấn):** PreRAG -> Truy xuất -> Rerank -> Tăng cường -> Sinh -> PostRAG.

## 2. OFFLINE Phase: Ingestion and Enrichment
## 2. Giai đoạn OFFLINE: Tiếp nhận và Làm giàu

- **Chunking Strategies:**  
- **Chiến lược Chunking:**

  - *Fixed-size:* Baseline.  
  - *Fixed-size:* Đường cơ sở.

  - *Semantic:* Splits by topic shifts.  
  - *Semantic:* Chia theo sự chuyển chủ đề.

  - *Hierarchical:* Finds small "child" chunks (e.g., 256 tokens) but injects the larger "parent" chunk (e.g., 2048 tokens) into the LLM for full context.  
  - *Hierarchical:* Tìm các chunk "con" nhỏ (ví dụ: 256 token) nhưng chèn chunk "cha" lớn hơn (ví dụ: 2048 token) vào LLM để có ngữ cảnh đầy đủ.

  - *Late Chunking:* Embeds the entire document first to capture global context, then pools embeddings for chunks.  
  - *Late Chunking:* Nhúng toàn bộ tài liệu trước để nắm bắt ngữ cảnh toàn cục, sau đó gộp các embedding cho các chunk.

  - *RAPTOR:* A recursive tree of summaries to answer high-level synthesis questions.  
  - *RAPTOR:* Một cây tóm tắt đệ quy để trả lời các câu hỏi tổng hợp cấp cao.

- **Enrichment Techniques:**  
- **Kỹ thuật Làm giàu:**

  - *Contextual Embeddings:* Using an LLM to prepend a context sentence to each chunk before embedding.  
  - *Contextual Embeddings:* Sử dụng LLM để thêm một câu ngữ cảnh vào mỗi chunk trước khi nhúng.

  - *Hypothetical Q&A:* Using an LLM to generate questions the chunk answers, then embedding the questions alongside the chunk.  
  - *Hypothetical Q&A:* Sử dụng LLM để tạo ra các câu hỏi mà chunk trả lời, sau đó nhúng các câu hỏi cùng với chunk.

  - *Matryoshka Representation Learning (MRL):* Flexible embedding dimensions to balance cost, latency, and precision.  
  - *Matryoshka Representation Learning (MRL):* Kích thước embedding linh hoạt để cân bằng chi phí, độ trễ và độ chính xác.

## 3. ONLINE Phase: Retrieval and Reranking
## 3. Giai đoạn ONLINE: Truy xuất và Rerank

- **Retrieval:**  
- **Truy xuất:**

  - *Hybrid + RRF:* Combines exact match (BM25) and semantic match (Dense Embeddings).  
  - *Hybrid + RRF:* Kết hợp khớp chính xác (BM25) và khớp ngữ nghĩa (Dense Embeddings).

  - *Advanced Retrieval:* ColBERT (Token-level MaxSim), SPLADE (Learned sparse expansions), and ColPali (Vision-based retrieval that skips text parsing).  
  - *Truy xuất nâng cao:* ColBERT (MaxSim cấp token), SPLADE (Mở rộng thưa được học), và ColPali (Truy xuất dựa trên thị giác, bỏ qua phân tích văn bản).

- **Reranking:**  
- **Rerank:**

  - Uses Cross-Encoders to re-score the top-K chunks from retrieval. Highly cost-effective way to boost precision (e.g., top-20 to top-3) at the cost of a slight latency increase (30-50ms).  
  - Sử dụng Cross-Encoders để chấm điểm lại top-K chunk từ truy xuất. Một cách rất hiệu quả về chi phí để tăng độ chính xác (ví dụ: top-20 thành top-3) với chi phí là độ trễ tăng nhẹ (30-50ms).

- **PreRAG (Query Transformations):**  
- **PreRAG (Biến đổi truy vấn):**

  - *HyDE:* Generates a hypothetical answer to embed and search.  
  - *HyDE:* Tạo ra một câu trả lời giả định để nhúng và tìm kiếm.

  - *Multi-Query:* Breaks complex questions into simpler sub-queries.  
  - *Multi-Query:* Chia các câu hỏi phức tạp thành các truy vấn con đơn giản hơn.

  - *Corrective RAG (CRAG):* Evaluates retrieved chunks and decides whether to route to web search or rewrite the query.  
  - *Corrective RAG (CRAG):* Đánh giá các chunk đã truy xuất và quyết định chuyển hướng đến tìm kiếm web hoặc viết lại truy vấn.

- **Augmentation:** Filtering out contradictions (NLI), compressing context, and injecting citations.  
- **Tăng cường:** Lọc ra các mâu thuẫn (NLI), nén ngữ cảnh, và chèn trích dẫn.

## 4. Closing the Loop: Evaluation with RAGAS
## 4. Khép kín vòng lặp: Đánh giá với RAGAS

Measure system health using RAGAS to pinpoint exactly which layer needs fixing.  
Đo lường sức khỏe hệ thống bằng RAGAS để xác định chính xác lớp nào cần sửa.

- **Retrieval Metrics:**  
- **Chỉ số Truy xuất:**

  - *Context Recall:* Did we retrieve all necessary information? (Fix: Hybrid search, HyDE, metadata filtering)  
  - *Context Recall:* Chúng ta đã truy xuất tất cả thông tin cần thiết chưa? (Sửa: Tìm kiếm Hybrid, HyDE, lọc metadata)

  - *Context Precision:* Are relevant chunks ranked at the top? (Fix: Reranking)  
  - *Context Precision:* Các chunk liên quan có được xếp hạng cao nhất không? (Sửa: Rerank)

- **Generation Metrics:**  
- **Chỉ số Sinh:**

  - *Faithfulness:* Does the answer stick to the provided context? (Fix: Prompt tuning, lowering temperature, citations)  
  - *Faithfulness:* Câu trả lời có bám sát ngữ cảnh được cung cấp không? (Sửa: Tinh chỉnh prompt, giảm temperature, trích dẫn)

  - *Answer Relevancy:* Does it directly answer the user's question? (Fix: Better prompts)  
  - *Answer Relevancy:* Nó có trả lời trực tiếp câu hỏi của người dùng không? (Sửa: Prompt tốt hơn)

## 5. Embedding Limitations
## 5. Hạn chế của Embedding

Embeddings inherently struggle with:  
Embedding vốn dĩ gặp khó khăn với:

- **Negation Insensitivity** (e.g., "allowed" vs "not allowed")  
- **Không nhạy với phủ định** (ví dụ: "allowed" so với "not allowed")

- **Entity Swapping**  
- **Hoán đổi thực thể**

- **Temporal Blindness** (e.g., policies from 2024 vs 2026)  
- **Mù thời gian** (ví dụ: chính sách năm 2024 so với 2026)

- **Numerical Blindness**  
- **Mù số**

*Solutions:* Use metadata filtering, post-retrieval NLI verification, and precise chunk enrichment.  
*Giải pháp:* Sử dụng lọc metadata, xác minh NLI sau truy xuất, và làm giàu chunk chính xác.
