---
type: summary
title: "Summary: day08-rag-pipeline-v3.pdf"
description: "A comprehensive summary of the Day 8 RAG Pipeline v3 slides outlining core concepts of retrieval, prompt augmentation, generative self-correction, and rigorous evaluation using RAGAS."
tags: [ai, 20k, day8, rag, pipeline, evaluation, hybrid_search]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/day08-rag-pipeline-v3.pdf"]
---

# Summary: RAG Pipeline v3
# Tóm tắt: Đường ống RAG v3

## Overview
## Tổng quan
This document summarizes the slides from "day08-rag-pipeline-v3.pdf" (by Trần Quang Thiện). The lecture traces the complete lifecycle of a Retrieval-Augmented Generation (RAG) system, extending the foundational Indexing pipeline established in Day 07 to a mature, evaluated architecture suitable for enterprise use.
Tài liệu này tóm tắt các trang trình bày từ "day08-rag-pipeline-v3.pdf" (của Trần Quang Thiện). Bài giảng theo dõi toàn bộ vòng đời của hệ thống Tạo văn bản Tăng cường Truy xuất (RAG), mở rộng từ đường ống Lập chỉ mục nền tảng được thiết lập ở Ngày 07 thành một kiến trúc hoàn thiện, được đánh giá và phù hợp cho việc sử dụng ở cấp độ doanh nghiệp.

## 1. Fundamentals of RAG
## 1. Cơ sở nền tảng của RAG
- **The "Why" of RAG:** LLMs inherently lack real-time internal data, have knowledge cutoffs, and tend to hallucinate to cover up missing facts. Fine-tuning models to memorize enterprise data is costly and inefficient. RAG circumvents this by fetching grounded evidence dynamically.
- **"Tại sao" lại cần RAG:** Các LLM (Mô hình Ngôn ngữ Lớn) vốn dĩ thiếu dữ liệu nội bộ theo thời gian thực, có giới hạn thời gian cắt kiến thức, và có xu hướng ảo giác (bịa đặt) để che lấp các sự kiện bị thiếu. Việc tinh chỉnh (fine-tuning) các mô hình để ghi nhớ dữ liệu doanh nghiệp rất tốn kém và kém hiệu quả. RAG khắc phục điều này bằng cách truy xuất các bằng chứng có cơ sở một cách linh hoạt.
- **Core Components:**
- **Các Thành phần Cốt lõi:**
  - **R (Retrieval):** Fetching accurate, relevant chunks using semantic and lexical search.
  - **R (Truy xuất - Retrieval):** Lấy các đoạn văn bản (chunks) chính xác, có liên quan bằng cách sử dụng tìm kiếm ngữ nghĩa và từ vựng.
  - **A (Augmentation):** Formatting the raw context to prevent cognitive overload for the LLM.
  - **A (Tăng cường - Augmentation):** Định dạng ngữ cảnh thô để tránh làm LLM bị quá tải nhận thức.
  - **G (Generation):** Formulating a constrained, factual response complete with citations.
  - **G (Tạo văn bản - Generation):** Hình thành một câu trả lời thực tế, được ràng buộc với đầy đủ các trích dẫn.

## 2. Advanced Retrieval Mechanics
## 2. Cơ chế Truy xuất Nâng cao
- **Dense vs. Sparse Search:**
- **Tìm kiếm Dày đặc (Dense) vs. Tìm kiếm Thưa thớt (Sparse):**
  - *Dense Vectors:* Good for general semantic matching (captures paraphrasing).
  - *Vector Dày đặc:* Tốt cho việc đối sánh ngữ nghĩa chung (nắm bắt được các cách diễn đạt lại).
  - *Sparse Vectors (BM25):* Critical for exact matches like product codes, SKUs, and specific names.
  - *Vector Thưa thớt (BM25):* Rất quan trọng đối với các đối sánh chính xác như mã sản phẩm, SKU và tên cụ thể.
- **Hybrid Search Strategy:** Unifies Dense and Sparse using **Reciprocal Rank Fusion (RRF)** or **Alpha Weighting** to score documents optimally.
- **Chiến lược Tìm kiếm Lai:** Kết hợp Dày đặc và Thưa thớt bằng cách sử dụng **Reciprocal Rank Fusion (RRF)** hoặc **Trọng số Alpha (Alpha Weighting)** để chấm điểm các tài liệu một cách tối ưu.
- **Reranking:** To solve the problem of precise relevance, a two-stage approach is used. A broad search retrieves Top-100 items, and a slower, more accurate **Cross-Encoder** reranks them to present the Top-5.
- **Xếp hạng lại (Reranking):** Để giải quyết vấn đề về sự liên quan chính xác, một phương pháp hai giai đoạn được sử dụng. Một tìm kiếm rộng sẽ truy xuất 100 mục đầu tiên, và một **Cross-Encoder** chậm hơn nhưng chính xác hơn sẽ xếp hạng lại chúng để đưa ra 5 mục hàng đầu.
- **MMR (Maximum Marginal Relevance):** An algorithm used to select chunks that are not only relevant but also diverse, reducing redundant context chunks.
- **MMR (Sự Liên quan Cận biên Tối đa):** Một thuật toán được sử dụng để chọn các đoạn không chỉ có liên quan mà còn đa dạng, làm giảm các đoạn ngữ cảnh dư thừa.

## 3. Augmentation and Prompt Strategies
## 3. Các Chiến lược Tăng cường và Prompt (Câu lệnh)
- **Context Injection & The "Lost in the Middle" Effect:**
- **Tiêm Ngữ cảnh & Hiệu ứng "Lạc vào Khúc giữa":**
  - LLMs tend to ignore information buried in the middle of a large prompt.
  - LLM có xu hướng bỏ qua thông tin bị chôn vùi ở giữa một câu lệnh lớn.
  - Solution: **Document Reordering** to place the most critical chunks at the top and bottom of the prompt array.
  - Giải pháp: **Sắp xếp lại Tài liệu** để đặt các đoạn quan trọng nhất ở đầu và cuối của mảng câu lệnh.
- **Token Budget Management:** Keeping context data within 60% of the token limit allows the model sufficient headroom for instructions and generated output.
- **Quản lý Ngân sách Token:** Giữ dữ liệu ngữ cảnh trong giới hạn 60% của token cho phép mô hình có đủ không gian cho các hướng dẫn và kết quả được tạo ra.
- **Instruction Tuning:** Use clear delimitations (like XML tags `<context>...</context>`) to separate system rules from raw evidence.
- **Tinh chỉnh Hướng dẫn:** Sử dụng các ranh giới rõ ràng (như thẻ XML `<context>...</context>`) để tách biệt các quy tắc hệ thống khỏi bằng chứng thô.

## 4. Grounded Generation
## 4. Tạo văn bản Có cơ sở
- **Strict Grounding:** The model must be explicitly instructed to answer *only* from the provided context. If the data is absent, it must trigger a "Graceful Degradation" (i.e., gracefully declining to answer).
- **Cơ sở Nghiêm ngặt:** Mô hình phải được hướng dẫn rõ ràng để trả lời *chỉ* từ ngữ cảnh được cung cấp. Nếu không có dữ liệu, nó phải kích hoạt "Sự xuống cấp Khéo léo" (tức là khéo léo từ chối trả lời).
- **Forcing Citations:** Responses must be tied directly back to `[doc_id]`s to ensure auditability.
- **Bắt buộc Trích dẫn:** Các câu trả lời phải được gắn trực tiếp trở lại các `[doc_id]` để đảm bảo khả năng kiểm toán.
- **Self-Correction & CoT:** Prompting the LLM to write out a `<thought_process>` before finalizing its answer drastically reduces reasoning errors, especially on conflicting documents.
- **Tự sửa lỗi & CoT (Chuỗi Suy nghĩ):** Yêu cầu LLM viết ra `<thought_process>` (quá trình suy nghĩ) trước khi chốt câu trả lời sẽ làm giảm đáng kể các lỗi suy luận, đặc biệt là trên các tài liệu mâu thuẫn.

## 5. Pre-RAG Query Transformations
## 5. Chuyển đổi Truy vấn Tiền-RAG
- Queries are often short, ambiguous, or poorly phrased.
- Các truy vấn thường ngắn, mơ hồ hoặc diễn đạt kém.
- **Techniques to clean queries:**
- **Các kỹ thuật để làm sạch truy vấn:**
  - *Pre-Filtering:* Utilizing metadata to narrow the search scope.
  - *Lọc trước:* Sử dụng siêu dữ liệu (metadata) để thu hẹp phạm vi tìm kiếm.
  - *HyDE & Multi-Query:* Expanding queries artificially or hallucinating ideal answers to act as better vector targets.
  - *HyDE & Đa Truy vấn:* Mở rộng các truy vấn một cách nhân tạo hoặc tưởng tượng ra các câu trả lời lý tưởng để đóng vai trò là các mục tiêu vector tốt hơn.
  - *Decomposition & Step-Back:* Breaking down multi-hop questions into parallel queries or abstracting overly detailed requests.
  - *Phân rã & Lùi lại:* Chia nhỏ các câu hỏi nhiều bước (multi-hop) thành các truy vấn song song hoặc trừu tượng hóa các yêu cầu quá chi tiết.

## 6. The RAG Evaluation Triad
## 6. Bộ ba Đánh giá RAG
- Replacing human "Vibe Checks" with automated, metrics-driven evaluations using frameworks like **RAGAS**.
- Thay thế "Kiểm tra Cảm tính" của con người bằng các đánh giá tự động, dựa trên số liệu sử dụng các khung như **RAGAS**.
- **The Triad:**
- **Bộ ba:**
  1. **Context Recall:** Did we fetch all the necessary facts? (Low score -> Fix Retriever)
  1. **Độ bao phủ Ngữ cảnh (Context Recall):** Chúng ta có lấy được tất cả các sự kiện cần thiết không? (Điểm thấp -> Sửa bộ Truy xuất)
  2. **Faithfulness:** Is the answer hallucination-free? (Low score -> Fix Generation/Prompt)
  2. **Độ trung thực (Faithfulness):** Câu trả lời có không bị ảo giác không? (Điểm thấp -> Sửa bộ Tạo văn bản/Câu lệnh)
  3. **Answer Relevance:** Is the answer on-topic?
  3. **Độ liên quan của Câu trả lời (Answer Relevance):** Câu trả lời có đúng chủ đề không?
- Implementing an "LLM-as-a-Judge" pipeline allows for rapid, continuous CI/CD evaluation of the RAG system against a Golden Dataset.
- Triển khai đường ống "LLM làm Giám khảo" (LLM-as-a-Judge) cho phép đánh giá CI/CD liên tục, nhanh chóng hệ thống RAG đối với một Tập dữ liệu Vàng (Golden Dataset).
