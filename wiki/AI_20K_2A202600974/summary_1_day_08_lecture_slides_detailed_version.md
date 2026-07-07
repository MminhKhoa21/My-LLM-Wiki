---
type: summary
title: "Summary: 1-Day 08 Lecture Slides_Detailed version.pdf"
description: "A detailed summary of the Day 8 lecture slides covering the complete Retrieval-Augmented Generation (RAG) paradigm, from indexing and retrieval to generation and evaluation."
tags: [ai, 20k, day8, rag, retrieval, generation, evaluation]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/1-Day 08 Lecture Slides_Detailed version.pdf"]
---

# Summary: Day 8 Lecture Slides - Detailed Version
# Tóm tắt: Bài giảng Ngày 8 - Phiên bản chi tiết

## Overview
## Tổng quan
This document summarizes the comprehensive lecture slides for Day 8 on the **RAG (Retrieval-Augmented Generation) Pipeline**. The lecture emphasizes that RAG is not just about adding context but is a synergistic orchestration of three main systems: Indexing, Retrieval, and Generation. It also covers evaluation frameworks, emphasizing that retrieval quality often dictates the final answer's quality.

Tài liệu này tóm tắt các slide bài giảng toàn diện cho Ngày 8 về **Quy trình RAG (Retrieval-Augmented Generation - Sinh văn bản tăng cường bằng truy xuất)**. Bài giảng nhấn mạnh rằng RAG không chỉ là việc thêm ngữ cảnh mà còn là sự phối hợp đồng bộ của ba hệ thống chính: Lập chỉ mục (Indexing), Truy xuất (Retrieval) và Sinh văn bản (Generation). Nó cũng bao gồm các khuôn khổ đánh giá, nhấn mạnh rằng chất lượng truy xuất thường quyết định chất lượng của câu trả lời cuối cùng.

## 1. The RAG Paradigm & Indexing Architecture
## 1. Mô hình RAG & Kiến trúc Lập chỉ mục
- **Why RAG?** LLMs suffer from "Knowledge Cutoff" and "Hallucination." Fine-tuning is expensive and poor at injecting factual data, whereas RAG acts like an "open-book exam," providing grounded facts, access control, and real-time updates.
  **Tại sao lại là RAG?** Các LLM gặp phải tình trạng "Giới hạn kiến thức" và "Ảo giác". Việc tinh chỉnh (Fine-tuning) rất tốn kém và kém hiệu quả trong việc đưa dữ liệu thực tế vào, trong khi RAG hoạt động như một "bài thi mở", cung cấp các dữ kiện có cơ sở, kiểm soát truy cập và cập nhật theo thời gian thực.
- **Data-Centric AI:** The true bottleneck is often the retrieval system (80% of errors) rather than the LLM (20% of errors).
  **AI lấy dữ liệu làm trung tâm:** Nút thắt thực sự thường nằm ở hệ thống truy xuất (80% lỗi) chứ không phải ở LLM (20% lỗi).
- **Indexing Pipeline:**
  **Quy trình Lập chỉ mục:**
  - **Parsing:** Real-world data is messy (PDF layouts, tables). Solutions involve specialized parsers (LlamaParse, Unstructured) or Vision LLMs (Multimodal Parsing) to extract structural elements like Markdown/HTML.
    **Phân tích cú pháp (Parsing):** Dữ liệu thực tế rất lộn xộn (bố cục PDF, bảng biểu). Các giải pháp bao gồm các trình phân tích cú pháp chuyên dụng (LlamaParse, Unstructured) hoặc Vision LLM (Phân tích đa phương thức) để trích xuất các thành phần cấu trúc như Markdown/HTML.
  - **Data Cleaning:** Normalization and Redaction (che mờ PII).
    **Làm sạch dữ liệu:** Chuẩn hóa và ẩn danh (che mờ PII).
  - **Ingestion Strategies:** Batch processing vs. Event-driven (Delta Sync) via webhooks to handle dynamic updates.
    **Chiến lược thu thập (Ingestion):** Xử lý hàng loạt (Batch processing) so với Hướng sự kiện (Event-driven / Delta Sync) thông qua webhooks để xử lý các bản cập nhật động.
- **Advanced Chunking Strategies:**
  **Chiến lược Phân mảnh (Chunking) Nâng cao:**
  - *Fixed-Size:* Cuts mechanically, risks breaking semantic meaning.
    *Kích thước cố định (Fixed-Size):* Cắt một cách máy móc, có nguy cơ phá vỡ ý nghĩa ngữ nghĩa.
  - *Recursive Chunking:* The standard approach (LangChain), respects paragraph and sentence boundaries.
    *Phân mảnh đệ quy (Recursive Chunking):* Cách tiếp cận tiêu chuẩn (LangChain), tôn trọng ranh giới đoạn văn và câu.
  - *Semantic/Structural Chunking:* Uses Markdown headings or Abstract Syntax Trees (AST) for code.
    *Phân mảnh ngữ nghĩa/Cấu trúc:* Sử dụng các tiêu đề Markdown hoặc Cây cú pháp trừu tượng (AST) cho mã.
  - *Small-to-Big Retrieval (Parent-Child):* Searches using small chunks for precision, but feeds the larger parent context to the LLM.
    *Truy xuất Từ nhỏ đến lớn (Parent-Child):* Tìm kiếm bằng cách sử dụng các đoạn nhỏ để có độ chính xác, nhưng đưa ngữ cảnh gốc lớn hơn vào LLM.
- **Embeddings & Metadata:**
  **Nhúng (Embeddings) & Siêu dữ liệu (Metadata):**
  - *Vector Search* excels at semantics and paraphrase but fails at exact keyword matches (e.g., error codes like ERR-x09).
    *Tìm kiếm Vector* xuất sắc ở ngữ nghĩa và diễn giải nhưng thất bại ở các kết quả khớp từ khóa chính xác (ví dụ: mã lỗi như ERR-x09).
  - *Metadata Filtering:* Pre-filtering vs. Post-filtering. Pre-filtering is safer and faster.
    *Lọc Siêu dữ liệu:* Lọc trước (Pre-filtering) so với Lọc sau (Post-filtering). Lọc trước an toàn hơn và nhanh hơn.

## 2. Query Processing & Advanced Retrieval
## 2. Xử lý Truy vấn & Truy xuất Nâng cao
- **Query Transformation:**
  **Chuyển đổi Truy vấn:**
  - *Query Expansion:* Adds synonyms to fix user vocabulary gaps.
    *Mở rộng Truy vấn:* Thêm các từ đồng nghĩa để khắc phục khoảng trống từ vựng của người dùng.
  - *Query Decomposition:* Splits multi-hop queries.
    *Phân tách Truy vấn:* Chia nhỏ các truy vấn đa bước.
  - *Step-Back Prompting:* Abstracts overly detailed questions.
    *Step-Back Prompting:* Trừu tượng hóa các câu hỏi quá chi tiết.
  - *HyDE (Hypothetical Document Embeddings):* Generates a fake answer and embeds it to find semantically similar real documents.
    *HyDE (Hypothetical Document Embeddings - Nhúng Tài liệu Giả định):* Tạo một câu trả lời giả và nhúng nó để tìm các tài liệu thực có ngữ nghĩa tương tự.
- **Dense vs. Sparse Retrieval:**
  **Truy xuất Dày đặc (Dense) vs. Thưa thớt (Sparse):**
  - *Sparse (BM25):* Exact match, high weights for rare words, fast but blind to synonyms.
    *Thưa thớt (BM25):* Khớp chính xác, trọng số cao cho các từ hiếm, nhanh nhưng không nhận diện được từ đồng nghĩa.
  - *Dense (Vector):* Semantic search, paraphrase-friendly, but misses exact IDs.
    *Dày đặc (Vector):* Tìm kiếm ngữ nghĩa, thân thiện với việc diễn giải lại, nhưng bỏ sót các ID chính xác.
- **Hybrid Search & Reranking:**
  **Tìm kiếm Lai & Xếp hạng lại (Reranking):**
  - Combines Dense and Sparse searches using **RRF (Reciprocal Rank Fusion)** or Alpha-tuning.
    Kết hợp các tìm kiếm Dày đặc và Thưa thớt bằng cách sử dụng **RRF (Reciprocal Rank Fusion)** hoặc Alpha-tuning.
  - **Two-stage Reranking:** Uses broad Hybrid Search for Top-100, then applies a **Cross-Encoder** to deeply score relevance for the Top-5.
    **Xếp hạng lại Hai giai đoạn:** Sử dụng Tìm kiếm Lai diện rộng cho Top-100, sau đó áp dụng **Cross-Encoder** để chấm điểm mức độ liên quan sâu sắc cho Top-5.
  - **MMR (Maximum Marginal Relevance):** Prevents redundancy in context windows by penalizing overly similar chunks.
    **MMR (Mức độ liên quan cận biên tối đa):** Ngăn ngừa sự dư thừa trong các cửa sổ ngữ cảnh bằng cách phạt các đoạn quá giống nhau.

## 3. Generation, Grounding & UX
## 3. Sinh văn bản, Nền tảng (Grounding) & Trải nghiệm Người dùng (UX)
- **Context Injection:**
  **Tiêm Ngữ cảnh:**
  - The "Lost in the Middle" effect: LLMs remember the start and end of prompts best. Solution: **Document Reordering** (placing top results at the boundaries).
    Hiệu ứng "Lạc ở giữa" (Lost in the Middle): LLM nhớ rõ nhất phần đầu và phần cuối của lời nhắc. Giải pháp: **Sắp xếp lại Tài liệu** (đặt các kết quả hàng đầu ở các ranh giới).
  - Use structured XML tags or Markdown to delineate system rules, context, and user questions. Limit context to ~60% of the token budget.
    Sử dụng các thẻ XML hoặc Markdown có cấu trúc để phân định ranh giới các quy tắc hệ thống, ngữ cảnh và câu hỏi của người dùng. Giới hạn ngữ cảnh ở khoảng 60% ngân sách token.
- **Prompt Engineering for Strict Grounding:**
  **Kỹ thuật Prompt để có Nền tảng Chặt chẽ:**
  - Enforce citations (e.g., `[doc_1]`).
    Bắt buộc trích dẫn (ví dụ: `[doc_1]`).
  - Graceful Degradation: Instruct the LLM to explicitly say "I don't know" or suggest alternatives when context is insufficient.
    Suy giảm tinh tế (Graceful Degradation): Hướng dẫn LLM nói rõ "Tôi không biết" hoặc đề xuất các lựa chọn thay thế khi ngữ cảnh không đủ.
  - **Chain-of-Thought (CoT):** Force the LLM to outline its reasoning before generating the final answer.
    **Chuỗi Suy nghĩ (Chain-of-Thought - CoT):** Buộc LLM phải vạch ra lập luận của mình trước khi tạo ra câu trả lời cuối cùng.
- **Output UX:**
  **Trải nghiệm Người dùng Đầu ra:**
  - Create scannable outputs with inline citations, source blocks, and confidence scores.
    Tạo các đầu ra dễ quét với các trích dẫn nội tuyến, khối nguồn và điểm tin cậy.
  - Use streaming states ("Đang tìm kiếm...") to improve perceived latency.
    Sử dụng các trạng thái luồng (streaming states - ví dụ: "Đang tìm kiếm...") để cải thiện độ trễ được cảm nhận.
- **Common Generation Failures:**
  **Các Lỗi Sinh văn bản Phổ biến:**
  - *Conflicting Context:* Instruct the LLM to prefer the most recent date.
    *Ngữ cảnh Mâu thuẫn:* Hướng dẫn LLM ưu tiên ngày gần nhất.
  - *Over-extrapolation:* Enforce strict grounding to prevent the LLM from guessing outside the facts.
    *Suy diễn quá mức:* Thực thi nền tảng chặt chẽ để ngăn LLM đoán mò bên ngoài các sự kiện.

## 4. Evaluation, Production & Next Steps
## 4. Đánh giá, Đưa vào Sản xuất & Các Bước Tiếp theo
- **The RAG Evaluation Triad (RAGAS):**
  **Bộ ba Đánh giá RAG (RAGAS):**
  1. **Context Recall:** Did the retriever find all necessary evidence?
     **Độ thu hồi Ngữ cảnh (Context Recall):** Trình truy xuất có tìm thấy tất cả các bằng chứng cần thiết không?
  2. **Faithfulness:** Did the generator stick strictly to the retrieved facts without hallucinating?
     **Độ trung thực (Faithfulness):** Trình tạo có bám sát chặt chẽ các sự kiện được truy xuất mà không bị ảo giác không?
  3. **Answer Relevance:** Did the answer actually address the user's question?
     **Sự liên quan của Câu trả lời (Answer Relevance):** Câu trả lời có thực sự giải quyết câu hỏi của người dùng không?
- **LLM-as-a-Judge:** Automating evaluation by having a powerful LLM grade the RAG outputs against a Golden Dataset.
  **LLM đóng vai trò Giám khảo (LLM-as-a-Judge):** Tự động hóa việc đánh giá bằng cách cho một LLM mạnh chấm điểm các đầu ra RAG dựa trên một Tập dữ liệu Vàng (Golden Dataset).
- **A/B Testing:** Evaluate ROI for advanced features (e.g., Cross-encoder adds 5% relevance but increases latency by 3s). Implement data CI/CD to block deployments if metrics drop.
  **Thử nghiệm A/B:** Đánh giá ROI (Lợi tức đầu tư) cho các tính năng nâng cao (ví dụ: Cross-encoder tăng 5% độ liên quan nhưng làm tăng độ trễ thêm 3 giây). Triển khai CI/CD dữ liệu để chặn việc triển khai nếu các chỉ số giảm sút.
- **Agentic Future:** Single-pass RAG is evolving into Multi-Agent systems (using LangGraph) where Retrieval becomes just one of many tools an LLM can invoke.
  **Tương lai của Tác nhân (Agentic Future):** RAG đơn lượt đang phát triển thành các hệ thống Đa Tác nhân (sử dụng LangGraph) nơi Truy xuất chỉ trở thành một trong nhiều công cụ mà LLM có thể gọi.
