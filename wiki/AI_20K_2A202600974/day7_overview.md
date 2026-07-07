---
type: overview
title: "Day 7 Overview - Data Foundations"
description: "Nền tảng dữ liệu cho AI Product, phân biệt loại dữ liệu, cơ chế Embedding, Vector Store và Chunking."
tags: [ai, 20k, day7]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/7/Day 07 Slides C401.pdf"]
---

# Day 7: Data Foundations (Embedding & Vector Store)
# Day 7: Data Foundations (Embedding & Vector Store)

## 1. Ba Loại Dữ Liệu Agent Cần
## 1. Three Types of Data Agents Need
- **Knowledge Data**: Tài liệu nội bộ, SOP, chính sách, FAQ... Phù hợp với *Retrieval* (RAG).
- ***Knowledge Data**: Internal documents, SOPs, policies, FAQs... Suitable for *Retrieval* (RAG).*
- **Operational Data**: Cơ sở dữ liệu giao dịch, trạng thái đơn hàng, CRM... Thường query có kiểm soát (DB query).
- ***Operational Data**: Transactional databases, order statuses, CRM... Typically accessed via controlled queries (DB query).*
- **Contextual Data**: Hồ sơ người dùng, lịch sử chat, vị trí... Dùng để inject trực tiếp vào context.
- ***Contextual Data**: User profiles, chat history, location... Used for direct injection into the context.*

## 2. Embedding
## 2. Embedding
- Nhằm giải quyết bài toán "khoảng cách ngữ nghĩa" (semantic distance) giữa dữ liệu đầu vào và các tài liệu lưu trữ.
- *Aims to solve the "semantic distance" problem between input data and stored documents.*
- Embedding model là hàm biến văn bản/hình ảnh thành **Vector số** (Mảng số thực nhiều chiều).
- *An Embedding model is a function that converts text/images into **Numerical Vectors** (Multi-dimensional arrays of real numbers).*
- Việc tìm kiếm được thực hiện bằng cách đo khoảng cách giữa các Vector. Phổ biến nhất là **Cosine Similarity** (đo góc giữa 2 vector, bỏ qua độ dài). 
- *Searching is performed by measuring the distance between Vectors. The most common is **Cosine Similarity** (measuring the angle between 2 vectors, ignoring magnitude).*
- Embedding giúp nhận diện ý nghĩa tương đồng dù từ khóa khác nhau, hoặc ngôn ngữ khác nhau (Cross-lingual).
- *Embedding helps recognize similar meanings even with different keywords, or across different languages (Cross-lingual).*

## 3. Vector Store
## 3. Vector Store
- Vector Store không chỉ lưu trữ Vector, mà lưu: **ID, Original Chunk (Text gốc), Vector, và Metadata (key-value)**.
- *Vector Store does not just store Vectors, but stores: **ID, Original Chunk (source text), Vector, and Metadata (key-value)**.*
- Khi truy vấn, hệ thống tìm Vector để lấy top-k kết quả, sau đó đưa Original Chunk vào Prompt cho LLM.
- *Upon querying, the system searches Vectors to retrieve the top-k results, then injects the Original Chunk into the Prompt for the LLM.*
- **Metadata** đóng vai trò cực kỳ quan trọng để lọc (Filter) dữ liệu trước khi so sánh vector (ví dụ: chỉ tìm trong tài liệu nội bộ, không tìm ở file cũ).
- ***Metadata** plays a crucial role in filtering data before vector comparison (e.g., searching only within internal documents, excluding old files).*

## 4. Xử Lý Dữ Liệu & Chunking
## 4. Data Processing & Chunking
- Không bao giờ đưa nguyên Raw Text (như PDF scan lỗi) vào Chunking vì chất lượng retrieval sẽ giảm thảm hại. (Data Quality Pyramid: Raw -> Cleaned -> Structured -> Enriched).
- *Never feed raw text (like error-prone scanned PDFs) directly into Chunking because retrieval quality will degrade drastically. (Data Quality Pyramid: Raw -> Cleaned -> Structured -> Enriched).*
- Định dạng tối ưu nhất cho LLM là **Markdown**, tiết kiệm 30-50% token so với HTML.
- *The most optimal format for LLMs is **Markdown**, saving 30-50% in tokens compared to HTML.*
- **Chunking**: Cắt tài liệu thành các đoạn nhỏ hơn để giữ tập trung thông tin.
- ***Chunking**: Breaking documents into smaller segments to maintain information focus.*
   - Chunk quá to: Nhiễu ngữ cảnh, vượt token limit.
   - *Chunks too large: Context noise, exceeding token limits.*
   - Chunk quá nhỏ: Mất ngữ cảnh, câu rời rạc.
   - *Chunks too small: Loss of context, disjointed sentences.*
   - Chiến lược: Chunk theo Structure/Heading, Semantic Chunking, hoặc theo Token (cố định độ dài có overlap).
   - *Strategies: Chunk by Structure/Heading, Semantic Chunking, or by Token (fixed length with overlap).*

## 5. Quy trình Retrieval Pipeline
## 5. Retrieval Pipeline Process
Bao gồm 2 pha tách biệt:
*Includes 2 distinct phases:*
- **Ingestion (Xử lý offline)**: Document -> Chunk -> Embed -> Store (Lưu trữ Vector & Metadata).
- ***Ingestion (Offline processing)**: Document -> Chunk -> Embed -> Store (Saving Vectors & Metadata).*
- **Retrieval (Truy vấn online)**: User Question -> Embed Query -> Search trong Vector DB -> Inject Chunk vào Prompt LLM.
- ***Retrieval (Online querying)**: User Question -> Embed Query -> Search in Vector DB -> Inject Chunk into LLM Prompt.*
