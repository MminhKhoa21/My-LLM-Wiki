---
type: summary
title: "Summary of day07-lecture-slides"
description: "Detailed summary of the generic Day 07 lecture slides on Data Strategy, Agent Memory, Embedding, Vector Store, and Chunking."
tags: [day7, embedding, vector-store, rag, data-strategy, memory]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/7/day07-lecture-slides.pdf"]
---

# Summary: Day 07 Lecture Slides (Data Foundations)

This document provides a summary of the Day 07 lecture slides covering core data foundations for AI applications.

## 1. Data Strategy & Data Types
Dữ liệu là thành phần quan trọng quyết định độ chính xác và chất lượng phản hồi của Agent. Các mô hình mạnh nhất vẫn trả lời sai (hallucinate) nếu dữ liệu đưa vào thiếu chất lượng hoặc cũ. Cần tập trung vào làm sạch dữ liệu (Data Quality Pyramid) trước khi tính đến chuyện thay đổi model.
Ba loại Data chính:
- **Knowledge Data**: Văn bản, SOP, FAQ nội bộ -> Dùng tốt với Vector Store.
- **Operational Data**: Dữ liệu thay đổi liên tục, Database nội bộ -> Dùng tốt qua API / Function Calling.
- **Contextual Data**: Dữ liệu phiên người dùng -> Dùng trực tiếp trong Context Window.

## 2. Agent Memory Architecture
Kiến trúc lưu trữ của Agent cần được thiết kế bài bản:
- Không được gom tất cả dữ liệu vào "System Prompt". Context window của model bị giới hạn và dễ sinh ảo giác nếu quá dài. Phân bổ token ngân sách rõ ràng.
- Vector store đóng vai trò là "Long-term Memory" giúp truy xuất tài liệu lớn theo ngữ nghĩa. "Short-term Memory" là cửa sổ context ở hiện tại.

## 3. Data Processing & Chunking
- Định dạng lý tưởng nhất để đưa dữ liệu vào LLM là Markdown, tiết kiệm một lượng token khổng lồ nhưng vẫn bảo tồn được cấu trúc của trang.
- Quá trình **Chunking**: Cắt nhỏ tài liệu trước khi embed. Phải cẩn thận, chunk quá to sẽ nhiễu ngữ nghĩa (nhiều chủ đề vào 1 chunk), chunk quá nhỏ mất ngữ cảnh. Tối ưu nhất là chia khối theo Section/Heading, kèm 10-20% chồng lấn (overlap).

## 4. Embeddings & Vector Store
- **Embedding**: Quá trình ánh xạ ngôn ngữ/tài liệu sang vector n chiều (không gian toán học). **Cosine Similarity** được dùng làm phương pháp chuẩn để đo độ tương đồng về phương hướng giữa hai vector để nhận ra các cụm từ khác mặt chữ nhưng cùng ngữ nghĩa.
- **Vector Store**: Nơi lưu giữ Vector, ID, Original Chunk, và Metadata.
- Vector Store đặc biệt quan trọng ở khâu Filtering qua **Metadata**. Filtering thu hẹp phạm vi tìm kiếm trước khi áp dụng Cosine Similarity để đạt độ chính xác tối đa.

## 5. Retrieval Pipeline Basics
Tích hợp Agent với dữ liệu qua 2 bước lớn:
1. **Pha Ingestion**: Cắt đoạn (Chunk) -> Embed (biến thành vector) -> Index (Lưu vào Vector DB).
2. **Pha Retrieval**: Nhận truy vấn (Query) -> Biến câu truy vấn thành Vector -> Tìm khoảng cách Cosine nhỏ nhất -> Trả về k chunks tốt nhất (Top-k) -> Truyền các chunk nguyên gốc vào Prompt cho LLM.

## Lab 7 & Deliverables
Phần thực hành tập trung vào việc áp dụng Vector Store (như ChromaDB) cùng với Chunking Scripts, nhằm xây dựng quy trình RAG Pattern đơn giản. Mục tiêu là dùng LLM giải đáp dựa vào các file được truy xuất chuẩn xác.
