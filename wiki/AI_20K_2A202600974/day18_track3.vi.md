---
type: summary
title: "Day 18 Track 3: Production RAG"
description: "Summary of building production-grade RAG systems, spanning offline ingestion, online retrieval, and RAGAS evaluation."
tags: [RAG, Retrieval Augmented Generation, Embeddings, Chunking, Hybrid Search, RAGAS]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-day18-production-rag.pdf"]
---
# Production RAG (Ngày 18 - Track 3)

**Giảng viên:** Tran Quang Thien

## 1. Bản đồ & La bàn (Kiến trúc RAG)

Một pipeline RAG trong sản xuất bao gồm hai giai đoạn chính:

- **OFFLINE (Tiếp nhận - 1 lần):** Phân tích cú pháp -> Chunk -> Làm giàu -> Embed -> Index. Giai đoạn này đặt ra trần tuyệt đối cho chất lượng truy xuất.

- **ONLINE (Truy vấn - mỗi truy vấn):** PreRAG -> Truy xuất -> Rerank -> Tăng cường -> Sinh -> PostRAG.

## 2. Giai đoạn OFFLINE: Tiếp nhận và Làm giàu

- **Chiến lược Chunking:**

  - *Fixed-size:* Đường cơ sở.

  - *Semantic:* Chia theo sự chuyển chủ đề.

  - *Hierarchical:* Tìm các chunk "con" nhỏ (ví dụ: 256 token) nhưng chèn chunk "cha" lớn hơn (ví dụ: 2048 token) vào LLM để có ngữ cảnh đầy đủ.

  - *Late Chunking:* Nhúng toàn bộ tài liệu trước để nắm bắt ngữ cảnh toàn cục, sau đó gộp các embedding cho các chunk.

  - *RAPTOR:* Một cây tóm tắt đệ quy để trả lời các câu hỏi tổng hợp cấp cao.

- **Kỹ thuật Làm giàu:**

  - *Contextual Embeddings:* Sử dụng LLM để thêm một câu ngữ cảnh vào mỗi chunk trước khi nhúng.

  - *Hypothetical Q&A:* Sử dụng LLM để tạo ra các câu hỏi mà chunk trả lời, sau đó nhúng các câu hỏi cùng với chunk.

  - *Matryoshka Representation Learning (MRL):* Kích thước embedding linh hoạt để cân bằng chi phí, độ trễ và độ chính xác.

## 3. Giai đoạn ONLINE: Truy xuất và Rerank

- **Truy xuất:**

  - *Hybrid + RRF:* Kết hợp khớp chính xác (BM25) và khớp ngữ nghĩa (Dense Embeddings).

  - *Truy xuất nâng cao:* ColBERT (MaxSim cấp token), SPLADE (Mở rộng thưa được học), và ColPali (Truy xuất dựa trên thị giác, bỏ qua phân tích văn bản).


  - Sử dụng Cross-Encoders để chấm điểm lại top-K chunk từ truy xuất. Một cách rất hiệu quả về chi phí để tăng độ chính xác (ví dụ: top-20 thành top-3) với chi phí là độ trễ tăng nhẹ (30-50ms).

- **PreRAG (Biến đổi truy vấn):**

  - *HyDE:* Tạo ra một câu trả lời giả định để nhúng và tìm kiếm.

  - *Multi-Query:* Chia các câu hỏi phức tạp thành các truy vấn con đơn giản hơn.

  - *Corrective RAG (CRAG):* Đánh giá các chunk đã truy xuất và quyết định chuyển hướng đến tìm kiếm web hoặc viết lại truy vấn.

- **Tăng cường:** Lọc ra các mâu thuẫn (NLI), nén ngữ cảnh, và chèn trích dẫn.

## 4. Khép kín vòng lặp: Đánh giá với RAGAS

Đo lường sức khỏe hệ thống bằng RAGAS để xác định chính xác lớp nào cần sửa.

- **Chỉ số Truy xuất:**

  - *Context Recall:* Chúng ta đã truy xuất tất cả thông tin cần thiết chưa? (Sửa: Tìm kiếm Hybrid, HyDE, lọc metadata)

  - *Context Precision:* Các chunk liên quan có được xếp hạng cao nhất không? (Sửa: Rerank)

- **Chỉ số Sinh:**

  - *Faithfulness:* Câu trả lời có bám sát ngữ cảnh được cung cấp không? (Sửa: Tinh chỉnh prompt, giảm temperature, trích dẫn)

  - *Answer Relevancy:* Nó có trả lời trực tiếp câu hỏi của người dùng không? (Sửa: Prompt tốt hơn)

## 5. Hạn chế của Embedding

Embedding vốn dĩ gặp khó khăn với:

- **Không nhạy với phủ định** (ví dụ: "allowed" so với "not allowed")

- **Hoán đổi thực thể**

- **Mù thời gian** (ví dụ: chính sách năm 2024 so với 2026)

- **Mù số**

*Giải pháp:* Sử dụng lọc metadata, xác minh NLI sau truy xuất, và làm giàu chunk chính xác.

---

Câu hỏi ôn tập Ngày 18

   Kỹ thuật enrichment nào trong giai đoạn OFFLINE sử dụng LLM để tạo ra các câu hỏi mà một chunk có thể trả lời, sau đó nhúng các câu hỏi đó cùng với chunk?
   - A. Nhúng ngữ cảnh
   - B. Hỏi-Đáp giả định
   - C. Học biểu diễn Matryoshka
   - D. Chunk muộn
   **Đáp án / Answer:** B

   Trong giai đoạn ONLINE, thành phần nào sử dụng Cross-Encoders để sắp xếp lại các chunk đã truy xuất, giúp cải thiện độ chính xác với chi phí độ trễ nhỏ?
   - A. Tiền RAG
   - B. Truy xuất
   - C. Sắp xếp lại
   - D. Tăng cường
   **Đáp án / Answer:** C

   Theo RAGAS, metric nào đo lường mức độ trung thực của câu trả lời (có bám sát nội dung được cung cấp hay không)?
   - A. Độ thu hồi ngữ cảnh
   - B. Độ chính xác ngữ cảnh
   - C. Độ trung thực
   - D. Mức độ liên quan của câu trả lời
   **Đáp án / Answer:** C

   Hạn chế nào của embedding được nhắc đến trong bài giảng, ví dụ như không phân biệt được "allowed" và "not allowed"?
   - A. Hoán đổi thực thể
   - B. Mù thời gian
   - C. Không nhạy cảm với phủ định
   - D. Mù số học
   **Đáp án / Answer:** C

   Kỹ thuật chunking nào xây dựng một cây tóm tắt đệ quy để trả lời các câu hỏi tổng hợp ở mức cao?
   - A. Chunk ngữ nghĩa
   - B. Chunk phân cấp
   - D. Chunk muộn
   **Đáp án / Answer:** C
