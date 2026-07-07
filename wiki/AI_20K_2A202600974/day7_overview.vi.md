---
type: overview
title: "Day 7 Overview - Data Foundations"
description: "Nền tảng dữ liệu cho AI Product, phân biệt loại dữ liệu, cơ chế Embedding, Vector Store và Chunking."
tags: [ai, 20k, day7]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/7/Day 07 Slides C401.pdf"]
---
*Ngày 7: Nền tảng dữ liệu (Embedding & Vector Store)*

*Ba loại dữ liệu agent cần*
- ***Knowledge Data**: Tài liệu nội bộ, SOP, chính sách, FAQ... Phù hợp với *Retrieval* (RAG).*
- ***Operational Data**: Cơ sở dữ liệu giao dịch, trạng thái đơn hàng, CRM... Thường query có kiểm soát (DB query).*
- ***Contextual Data**: Hồ sơ người dùng, lịch sử chat, vị trí... Dùng để inject trực tiếp vào context.*

- *Nhằm giải quyết bài toán "khoảng cách ngữ nghĩa" (semantic distance) giữa dữ liệu đầu vào và các tài liệu lưu trữ.*
- *Embedding model là hàm biến văn bản/hình ảnh thành **Vector số** (Mảng số thực nhiều chiều).*
- *Việc tìm kiếm được thực hiện bằng cách đo khoảng cách giữa các Vector. Phổ biến nhất là **Cosine Similarity** (đo góc giữa 2 vector, bỏ qua độ dài).*
- *Embedding giúp nhận diện ý nghĩa tương đồng dù từ khóa khác nhau, hoặc ngôn ngữ khác nhau (Cross-lingual).*

- *Vector Store không chỉ lưu trữ Vector, mà lưu: **ID, Original Chunk (Text gốc), Vector, và Metadata (key-value)**.*
- *Khi truy vấn, hệ thống tìm Vector để lấy top-k kết quả, sau đó đưa Original Chunk vào Prompt cho LLM.*
- ***Metadata** đóng vai trò cực kỳ quan trọng để lọc (Filter) dữ liệu trước khi so sánh vector (ví dụ: chỉ tìm trong tài liệu nội bộ, không tìm ở file cũ).*

*Xử lý dữ liệu & Chunking*
- *Không bao giờ đưa nguyên Raw Text (như PDF scan lỗi) vào Chunking vì chất lượng retrieval sẽ giảm thảm hại. (Data Quality Pyramid: Raw -> Cleaned -> Structured -> Enriched).*
- *Định dạng tối ưu nhất cho LLM là **Markdown**, tiết kiệm 30-50% token so với HTML.*
- ***Chunking**: Cắt tài liệu thành các đoạn nhỏ hơn để giữ tập trung thông tin.*
   - *Chunk quá to: Nhiễu ngữ cảnh, vượt token limit.*
   - *Chunk quá nhỏ: Mất ngữ cảnh, câu rời rạc.*
   - *Chiến lược: Chunk theo Structure/Heading, Semantic Chunking, hoặc theo Token (cố định độ dài có overlap).*

*Quy trình Retrieval Pipeline*
*Bao gồm 2 pha tách biệt:*
- ***Ingestion (Xử lý offline)**: Document -> Chunk -> Embed -> Store (Lưu trữ Vector & Metadata).*
- ***Retrieval (Truy vấn online)**: User Question -> Embed Query -> Search trong Vector DB -> Inject Chunk vào Prompt LLM.*
