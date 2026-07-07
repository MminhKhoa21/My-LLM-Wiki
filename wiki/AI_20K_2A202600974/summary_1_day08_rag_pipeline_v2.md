---
type: summary
title: "Summary: 1-day08-rag-pipeline-v2.pdf"
description: "A detailed summary of the Day 8 RAG Pipeline v2 slides focusing on bridging retrieval, augmentation, and generation, alongside pre-RAG query transformations and evaluation techniques."
tags: [ai, 20k, day8, rag, pipeline, augmentation]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/1-day08-rag-pipeline-v2.pdf"]
---

# Summary: RAG Pipeline v2
# Tóm tắt: Pipeline RAG v2

## Overview
## Tổng quan
This document summarizes the slides from "1-day08-rag-pipeline-v2.pdf" (by M.Sc Trần Minh Tú). It details the evolution from a simple Indexing pipeline (Day 07) to a fully orchestrated **Retrieval-Augmented Generation (RAG)** pipeline. The lecture highlights how RAG solves the LLM illusion of knowledge, making it a compulsory architecture for enterprise AI applications.
Tài liệu này tóm tắt các slide từ "1-day08-rag-pipeline-v2.pdf" (của ThS. Trần Minh Tú). Nó nêu chi tiết quá trình phát triển từ một pipeline Lập chỉ mục đơn giản (Ngày 07) sang một pipeline **Retrieval-Augmented Generation (RAG - Tạo sinh tăng cường truy xuất)** được điều phối hoàn chỉnh. Bài giảng nhấn mạnh cách RAG giải quyết ảo giác kiến thức của LLM, khiến nó trở thành một kiến trúc bắt buộc cho các ứng dụng AI của doanh nghiệp.

## 1. Moving from Retrieval to RAG
## 1. Chuyển từ Truy xuất (Retrieval) sang RAG
- **Why RAG?** LLMs have knowledge cutoffs and are probabilistic by nature, leading to hallucinations. RAG solves this by providing dynamic, grounded context (like an open-book exam) instead of relying on expensive and static fine-tuning.
- **Tại sao lại dùng RAG?** LLMs có giới hạn kiến thức tại một thời điểm nhất định và có bản chất xác suất, dẫn đến hiện tượng ảo giác (hallucinations). RAG giải quyết vấn đề này bằng cách cung cấp ngữ cảnh động, có cơ sở (giống như bài thi tự luận được mở tài liệu) thay vì phụ thuộc vào việc tinh chỉnh (fine-tuning) tốn kém và tĩnh.
- **The R-A-G Triad:**
- **Bộ ba R-A-G:**
  - **Retrieval (R):** Finding the right evidence (Dense, Sparse, Hybrid search).
  - **Retrieval (R - Truy xuất):** Tìm kiếm bằng chứng phù hợp (Tìm kiếm dày đặc, thưa thớt, kết hợp).
  - **Augmentation (A):** Structuring the context to mitigate "lost in the middle" effects and noise.
  - **Augmentation (A - Tăng cường):** Cấu trúc lại ngữ cảnh để giảm thiểu hiệu ứng "mất thông tin ở giữa" (lost in the middle) và nhiễu.
  - **Generation (G):** Producing a grounded answer with strict citations and self-checks.
  - **Generation (G - Tạo sinh):** Đưa ra câu trả lời có cơ sở với các trích dẫn nghiêm ngặt và tự kiểm tra.

## 2. Retrieval Deep Dive
## 2. Đi sâu vào Truy xuất (Retrieval)
- **Semantic vs. Lexical Search:**
- **Tìm kiếm Ngữ nghĩa (Semantic) vs. Tìm kiếm Từ vựng (Lexical):**
  - *Dense Vector (Semantic):* Captures meaning, paraphrases, but struggles with exact keywords like IDs or codes.
  - *Dense Vector (Ngữ nghĩa):* Nắm bắt ý nghĩa, diễn giải lại, nhưng gặp khó khăn với các từ khóa chính xác như ID hoặc mã.
  - *Sparse Vector (BM25):* Matches exact keywords fast but ignores context and synonyms.
  - *Sparse Vector (BM25):* Khớp từ khóa chính xác một cách nhanh chóng nhưng bỏ qua ngữ cảnh và các từ đồng nghĩa.
- **Hybrid Search & Fusion:**
- **Tìm kiếm Kết hợp (Hybrid) & Dung hợp (Fusion):**
  - Combines both methods using **RRF (Reciprocal Rank Fusion)** or Alpha-weighting.
  - Kết hợp cả hai phương pháp bằng cách sử dụng **RRF (Reciprocal Rank Fusion)** hoặc Trọng số Alpha (Alpha-weighting).
- **Reranking & MMR:**
- **Xếp hạng lại (Reranking) & MMR:**
  - After a broad top-K search, use a **Cross-Encoder** for precise relevance scoring.
  - Sau khi tìm kiếm top-K rộng rãi, sử dụng **Cross-Encoder** để chấm điểm mức độ liên quan chính xác.
  - Apply **MMR (Maximum Marginal Relevance)** to reduce redundant chunks and retain diverse context.
  - Áp dụng **MMR (Maximum Marginal Relevance - Mức độ liên quan cận biên tối đa)** để giảm bớt các đoạn dư thừa và giữ lại ngữ cảnh đa dạng.

## 3. Augmentation Strategies
## 3. Các Chiến lược Tăng cường (Augmentation)
- **Context Injection:**
- **Tiêm Ngữ cảnh (Context Injection):**
  - **Document Reordering:** Since LLMs recall the beginning and end of prompts better, place the most relevant documents at the boundaries `[1, 3, 5, 4, 2]`.
  - **Sắp xếp lại tài liệu:** Vì LLMs ghi nhớ phần đầu và phần cuối của câu lệnh tốt hơn, hãy đặt các tài liệu phù hợp nhất ở hai đầu `[1, 3, 5, 4, 2]`.
- **Grounding and Verification:**
- **Đảm bảo Tính có cơ sở (Grounding) và Xác thực:**
  - Isolate System Rules, Context, and User Questions via XML tags.
  - Cô lập các Quy tắc Hệ thống, Ngữ cảnh và Câu hỏi Người dùng qua các thẻ XML.
  - Implement **Metadata Integration** and **Citation Formatting** to ensure accountability.
  - Tích hợp **Siêu dữ liệu (Metadata)** và **Định dạng Trích dẫn** để đảm bảo trách nhiệm giải trình.
- **Token Budget Management:** Keep context under 60% of the token limit to avoid diluting the instruction. Use Context Compression if necessary.
- **Quản lý Ngân sách Token:** Giữ ngữ cảnh dưới 60% giới hạn token để tránh làm loãng câu lệnh. Sử dụng Nén Ngữ cảnh nếu cần thiết.

## 4. Generation & Output Control
## 4. Kiểm soát Tạo sinh (Generation) & Đầu ra
- **Model Selection & Formatting:** Choose models based on task complexity (e.g., local small models vs. large enterprise APIs). Standardize output via Markdown or JSON.
- **Lựa chọn Mô hình & Định dạng:** Chọn các mô hình dựa trên độ phức tạp của tác vụ (ví dụ: các mô hình cục bộ nhỏ so với API lớn của doanh nghiệp). Chuẩn hóa đầu ra thông qua Markdown hoặc JSON.
- **Safety and Alignment:** Filter PII and apply abstention rules ("Graceful Degradation" - admitting "I don't know" when context is missing).
- **An toàn và Căn chỉnh:** Lọc thông tin nhận dạng cá nhân (PII) và áp dụng các quy tắc từ chối ("Graceful Degradation" - thừa nhận "Tôi không biết" khi thiếu ngữ cảnh).
- **Self-Correction & CoT:**
- **Tự Sửa lỗi & Chuỗi Suy luận (CoT):**
  - Use **Chain-of-Thought (CoT)** (`<thought_process>`) to force step-by-step reasoning before answering.
  - Sử dụng **Chuỗi Suy luận (Chain-of-Thought - CoT)** (`<thought_process>`) để ép buộc việc suy luận từng bước trước khi trả lời.
  - Implement self-checks against the context before presenting the final answer.
  - Thực hiện tự kiểm tra với ngữ cảnh trước khi đưa ra câu trả lời cuối cùng.
- **User Experience (UX):** Output format matters. Scannable text, inline citations, source popups, and streaming generation build user trust.
- **Trải nghiệm Người dùng (UX):** Định dạng đầu ra rất quan trọng. Văn bản dễ nhìn, trích dẫn nội dòng, cửa sổ bật lên (popups) về nguồn, và tạo sinh luồng (streaming) sẽ tạo niềm tin cho người dùng.

## 5. Pre-RAG & Agentic RAG
## 5. Tiền RAG (Pre-RAG) & RAG Tác nhân (Agentic RAG)
- **Query Transformation:**
- **Chuyển đổi Câu truy vấn:**
  - Use LLMs to pre-process queries before vector searches: *Multi-Query* (variations), *HyDE* (hallucinated answers), *Query Expansion* (synonyms), *Decomposition* (splitting multi-hop queries), and *Step-Back Prompting* (abstraction).
  - Sử dụng LLMs để tiền xử lý các câu truy vấn trước khi tìm kiếm vector: *Multi-Query* (các biến thể), *HyDE* (các câu trả lời tạo từ ảo giác), *Mở rộng Truy vấn* (từ đồng nghĩa), *Phân tách* (chia nhỏ các truy vấn đa bước), và *Step-Back Prompting* (trừu tượng hóa).
  - Pre-filtering via metadata massively speeds up and focuses the search.
  - Tiền lọc qua siêu dữ liệu (metadata) sẽ tăng tốc mạnh mẽ và tập trung vào mục tiêu tìm kiếm.
- **Agentic RAG:** Elevates the system to self-query, self-correct (C-RAG), and adapt. Retrieval becomes just one of many "tools" in a multi-agent system.
- **RAG Tác nhân (Agentic RAG):** Nâng cấp hệ thống để tự truy vấn, tự sửa lỗi (C-RAG) và thích ứng. Truy xuất chỉ trở thành một trong nhiều "công cụ" trong một hệ thống đa tác nhân.

## 6. RAG Evaluation (RAGAS)
## 6. Đánh giá RAG (RAGAS)
A "vibe check" is inadequate. A rigorous, automated evaluation framework involves three axes:
Việc "kiểm tra theo cảm tính" (vibe check) là không đủ. Một khuôn khổ đánh giá nghiêm ngặt, tự động bao gồm ba trục chính:
1. **Context Recall:** Did the retriever fetch the necessary documents?
1. **Độ hồi tưởng Ngữ cảnh (Context Recall):** Trình truy xuất có thu thập các tài liệu cần thiết không?
2. **Faithfulness:** Is the LLM's answer loyal to the retrieved context?
2. **Độ trung thực (Faithfulness):** Câu trả lời của LLM có bám sát vào ngữ cảnh được truy xuất không?
3. **Answer Relevance:** Did the answer satisfy the user's prompt without wandering?
3. **Độ liên quan của Câu trả lời (Answer Relevance):** Câu trả lời có thỏa mãn yêu cầu của người dùng mà không bị lan man không?
- Implementing CI/CD pipelines for AI involves testing the "behavior" of the AI against a Golden Dataset.
- Việc triển khai các đường ống CI/CD cho AI bao gồm việc kiểm thử "hành vi" của AI so với Tập dữ liệu Chuẩn (Golden Dataset).
