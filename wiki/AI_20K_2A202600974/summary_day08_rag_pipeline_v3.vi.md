---
type: summary
title: "Summary: day08-rag-pipeline-v3.pdf"
description: "A comprehensive summary of the Day 8 RAG Pipeline v3 slides outlining core concepts of retrieval, prompt augmentation, generative self-correction, and rigorous evaluation using RAGAS."
tags: [ai, 20k, day8, rag, pipeline, evaluation, hybrid_search]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/day08-rag-pipeline-v3.pdf"]
---

# Tóm tắt: Đường ống RAG v3

## Tổng quan
This document summarizes the slides from "day08-rag-pipeline-v3.pdf" (by Trần Quang Thiện). The lecture traces the complete lifecycle of a Retrieval-Augmented Generation (RAG) system, extending the foundational Indexing pipeline established in Day 07 to a mature, evaluated architecture suitable for enterprise use.
Tài liệu này tóm tắt các trang trình bày từ "day08-rag-pipeline-v3.pdf" (của Trần Quang Thiện). Bài giảng theo dõi toàn bộ vòng đời của hệ thống Tạo văn bản Tăng cường Truy xuất (RAG), mở rộng từ đường ống Lập chỉ mục nền tảng được thiết lập ở Ngày 07 thành một kiến trúc hoàn thiện, được đánh giá và phù hợp cho việc sử dụng ở cấp độ doanh nghiệp.

## 1. Cơ sở nền tảng của RAG
- **"Tại sao" lại cần RAG:** Các LLM (Mô hình Ngôn ngữ Lớn) vốn dĩ thiếu dữ liệu nội bộ theo thời gian thực, có giới hạn thời gian cắt kiến thức, và có xu hướng ảo giác (bịa đặt) để che lấp các sự kiện bị thiếu. Việc tinh chỉnh (fine-tuning) các mô hình để ghi nhớ dữ liệu doanh nghiệp rất tốn kém và kém hiệu quả. RAG khắc phục điều này bằng cách truy xuất các bằng chứng có cơ sở một cách linh hoạt.
- **Các Thành phần Cốt lõi:**
  - **R (Truy xuất - Retrieval):** Lấy các đoạn văn bản (chunks) chính xác, có liên quan bằng cách sử dụng tìm kiếm ngữ nghĩa và từ vựng.
  - **A (Tăng cường - Augmentation):** Định dạng ngữ cảnh thô để tránh làm LLM bị quá tải nhận thức.
  - **G (Tạo văn bản - Generation):** Hình thành một câu trả lời thực tế, được ràng buộc với đầy đủ các trích dẫn.

## 2. Cơ chế Truy xuất Nâng cao
- **Tìm kiếm Dày đặc (Dense) vs. Tìm kiếm Thưa thớt (Sparse):**
  - *Vector Dày đặc:* Tốt cho việc đối sánh ngữ nghĩa chung (nắm bắt được các cách diễn đạt lại).
  - *Vector Thưa thớt (BM25):* Rất quan trọng đối với các đối sánh chính xác như mã sản phẩm, SKU và tên cụ thể.
- **Chiến lược Tìm kiếm Lai:** Kết hợp Dày đặc và Thưa thớt bằng cách sử dụng **Reciprocal Rank Fusion (RRF)** hoặc **Trọng số Alpha (Alpha Weighting)** để chấm điểm các tài liệu một cách tối ưu.
- **Xếp hạng lại (Reranking):** Để giải quyết vấn đề về sự liên quan chính xác, một phương pháp hai giai đoạn được sử dụng. Một tìm kiếm rộng sẽ truy xuất 100 mục đầu tiên, và một **Cross-Encoder** chậm hơn nhưng chính xác hơn sẽ xếp hạng lại chúng để đưa ra 5 mục hàng đầu.
- **MMR (Sự Liên quan Cận biên Tối đa):** Một thuật toán được sử dụng để chọn các đoạn không chỉ có liên quan mà còn đa dạng, làm giảm các đoạn ngữ cảnh dư thừa.

## 3. Các Chiến lược Tăng cường và Prompt (Câu lệnh)
- **Tiêm Ngữ cảnh & Hiệu ứng "Lạc vào Khúc giữa":**
  - LLM có xu hướng bỏ qua thông tin bị chôn vùi ở giữa một câu lệnh lớn.
  - Giải pháp: **Sắp xếp lại Tài liệu** để đặt các đoạn quan trọng nhất ở đầu và cuối của mảng câu lệnh.
- **Quản lý Ngân sách Token:** Giữ dữ liệu ngữ cảnh trong giới hạn 60% của token cho phép mô hình có đủ không gian cho các hướng dẫn và kết quả được tạo ra.
- **Tinh chỉnh Hướng dẫn:** Sử dụng các ranh giới rõ ràng (như thẻ XML `<context>...</context>`) để tách biệt các quy tắc hệ thống khỏi bằng chứng thô.

## 4. Tạo văn bản Có cơ sở
- **Cơ sở Nghiêm ngặt:** Mô hình phải được hướng dẫn rõ ràng để trả lời *chỉ* từ ngữ cảnh được cung cấp. Nếu không có dữ liệu, nó phải kích hoạt "Sự xuống cấp Khéo léo" (tức là khéo léo từ chối trả lời).
- **Bắt buộc Trích dẫn:** Các câu trả lời phải được gắn trực tiếp trở lại các `[doc_id]` để đảm bảo khả năng kiểm toán.
- **Tự sửa lỗi & CoT (Chuỗi Suy nghĩ):** Yêu cầu LLM viết ra `<thought_process>` (quá trình suy nghĩ) trước khi chốt câu trả lời sẽ làm giảm đáng kể các lỗi suy luận, đặc biệt là trên các tài liệu mâu thuẫn.

## 5. Chuyển đổi Truy vấn Tiền-RAG
- Các truy vấn thường ngắn, mơ hồ hoặc diễn đạt kém.
- **Các kỹ thuật để làm sạch truy vấn:**
  - *Lọc trước:* Sử dụng siêu dữ liệu (metadata) để thu hẹp phạm vi tìm kiếm.
  - *HyDE & Đa Truy vấn:* Mở rộng các truy vấn một cách nhân tạo hoặc tưởng tượng ra các câu trả lời lý tưởng để đóng vai trò là các mục tiêu vector tốt hơn.
  - *Phân rã & Lùi lại:* Chia nhỏ các câu hỏi nhiều bước (multi-hop) thành các truy vấn song song hoặc trừu tượng hóa các yêu cầu quá chi tiết.

## 6. Bộ ba Đánh giá RAG
- Thay thế "Kiểm tra Cảm tính" của con người bằng các đánh giá tự động, dựa trên số liệu sử dụng các khung như **RAGAS**.
- **Bộ ba:**
  1. **Độ bao phủ Ngữ cảnh (Context Recall):** Chúng ta có lấy được tất cả các sự kiện cần thiết không? (Điểm thấp -> Sửa bộ Truy xuất)
  2. **Độ trung thực (Faithfulness):** Câu trả lời có không bị ảo giác không? (Điểm thấp -> Sửa bộ Tạo văn bản/Câu lệnh)
  3. **Độ liên quan của Câu trả lời (Answer Relevance):** Câu trả lời có đúng chủ đề không?
- Triển khai đường ống "LLM làm Giám khảo" (LLM-as-a-Judge) cho phép đánh giá CI/CD liên tục, nhanh chóng hệ thống RAG đối với một Tập dữ liệu Vàng (Golden Dataset).
