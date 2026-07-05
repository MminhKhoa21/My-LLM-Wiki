---
type: summary
title: "Summary of Day 07 Slides C401"
description: "Detailed summary of the Day 07 lecture slides (Class C401 version by Trần Quang Thiện) covering Data Foundations, Embedding, Vector Stores, and RAG Integration."
tags: [day7, embedding, vector-store, rag, data-strategy, memory, c401]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/7/Day 07 Slides C401.pdf"]
---

# Summary: Day 07 Slides C401

This document summarizes the key concepts from the Day 7 lecture on Data Foundations, specifically customized for class C401 by instructor Trần Quang Thiện.

## 1. Data Strategy Cho Sản Phẩm AI
Chất lượng dữ liệu quyết định phần lớn sức mạnh của AI trong sản phẩm thực tế, quan trọng hơn việc thay đổi model.
- **Knowledge Data**: Tài liệu, policy, SOP, FAQ nội bộ. Được nhắm tới cho mô hình RAG.
- **Operational Data**: Dữ liệu vận hành như CRM, trạng thái đơn hàng. Nên dùng function calling / API.
- **Contextual Data**: Ngữ cảnh phiên người dùng. Có thể inject trực tiếp để agent cá nhân hóa câu trả lời.

**Data Quality Pyramid**: Raw (nhiễu) -> Cleaned -> Structured -> Enriched (chất lượng cao nhất). Quá trình làm sạch trước khi Index là bắt buộc.

## 2. Agent Memory Architecture
Phân chia bộ nhớ của AI Agent:
- **Short-term Memory**: Nằm trong context window, chịu trách nhiệm cho các logic hội thoại tức thời.
- **Long-term Memory**: Bộ nhớ lưu trữ bên ngoài (Vector DB, RDBMS). Chỉ nên truy xuất khi thật sự cần thiết nhằm bảo toàn Context Window Budget.

## 3. Data Processing & Format
Format tối ưu nhất cho LLM là Markdown, giúp bảo toàn được cấu trúc heading/table nhưng lại tiết kiệm token đáng kể so với HTML hay Plain text. Quá trình xử lý văn bản (Ingestion pipeline) cần Clean & Structure trước khi cắt nhỏ.

## 4. Embeddings
Đưa ngôn ngữ và các dữ liệu đa phương tiện (multi-modal) vào một không gian toán học:
- **Cosine Similarity**: Công thức chủ đạo để tính khoảng cách vector cho text embedding. Nó đo góc giữa 2 vector, bỏ qua độ dài.
- Tốc độ, độ lớn mô hình và giá tiền là một sự đánh đổi (Trade-off). Các mô hình như `text-embedding-3-small` / `large` thường được sử dụng dựa trên từng Use case.
- Ứng dụng phổ biến: Semantic search, clustering, dedup, recommendation.

## 5. Vector Store & Retrieval Pipeline
- **Vector Store** lưu giữ 4 giá trị cốt lõi: Vector ID, Text Chunk Gốc, Embedding Vector, và **Metadata**.
- **Metadata Filtering** đi đôi với Semantic Similarity để loại bỏ nhiễu và lọc theo điều kiện rõ ràng (category, source).
- **Chunking Strategy**: Chunking quá lớn làm nhiễu LLM, chunking quá nhỏ gây mất ngữ cảnh. Tối ưu thường cắt theo Section/Heading và có Overlap hợp lý.
- Có 2 pha tách biệt: Pha Ingestion (offline) và Pha Retrieval (online).

## Lab 7 (C401 Specifics)
Giao phẩm cuối ngày của học viên (C401) bao gồm việc xây dựng một pipeline hoàn chỉnh:
1. `chunking.py` — Implement 3 chunking strategies và đo khoảng cách Cosine.
2. `store.py` — Khởi tạo Embedding Store cùng các hàm thao tác thêm/xóa/tìm kiếm/lọc.
3. `agent.py` — Triển khai KnowledgeBaseAgent dựa trên cấu trúc RAG Pattern.
4. Test và so sánh kết quả truy vấn (5 benchmark queries).
