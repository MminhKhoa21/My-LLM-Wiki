---
type: overview
title: "Day 8: RAG Pipeline Overview"
description: "Tổng quan về Retrieval-Augmented Generation (RAG), từ kỹ thuật truy xuất (Retrieval), tăng cường ngữ cảnh (Augmentation) đến sinh ngôn ngữ (Generation)."
tags: [ai, 20k, day8, rag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/day08-rag-pipeline-v3.pdf"]
---

# Day 8: RAG Pipeline Overview

## Nội dung chính
Bài học đi sâu vào kiến trúc và các thành phần của một hệ thống **RAG (Retrieval-Augmented Generation)**:
- **R (Retrieval)**: Các kỹ thuật tìm kiếm như Dense Search (dựa trên semantic, vector), Sparse Search (BM25, dựa trên exact keyword), và sự kết hợp của cả hai là **Hybrid Search**. Tối ưu hóa Retrieval bao gồm các kỹ thuật như Reranking (Cross-encoder) và MMR (Maximum Marginal Relevance) để đa dạng hóa kết quả, chống trùng lặp.
- **A (Augmentation)**: Kỹ thuật nhúng context vào prompt cho LLM. Bao gồm giải quyết vấn đề "Lost in the Middle" thông qua việc reordering (sắp xếp lại tài liệu), strict constraints (ép LLM chỉ trả lời dựa trên context), và token budget management (giới hạn context để dành chỗ cho instructions và output).
- **G (Generation)**: Quá trình LLM sinh câu trả lời. Bao gồm các kỹ thuật hạn chế ảo giác (hallucination) qua việc buộc LLM trích dẫn (forcing citations), xử lý khi không có đủ context (graceful degradation), và các phương pháp kỹ thuật như Chain-of-Thought (CoT) trong generation.

## Các kỹ thuật nổi bật
- **Hybrid Search**: Gộp kết quả của Dense và Sparse search bằng các thuật toán như RRF (Reciprocal Rank Fusion) hoặc Alpha Weighting (Score Fusion).
- **Retrieve-and-Rerank**: Tìm kiếm diện rộng (nhanh, rẻ) sau đó dùng Cross-encoder để chấm điểm lại chi tiết top kết quả.
- **Pre-Filtering**: Thu hẹp không gian tìm kiếm thông qua metadata trước khi vector search.
- **Query Transformation**: Xử lý, biến đổi hoặc phân rã câu hỏi của user trước khi đưa vào pipeline để cải thiện độ chính xác (ví dụ: HyDE, Multi-Query, Query Decomposition).

## Ứng dụng thực tế
- RAG giúp LLM trả lời dựa trên dữ liệu nội bộ liên tục thay đổi của doanh nghiệp mà không cần fine-tuning tốn kém.
- Thiết kế Agentic RAG: Thêm khả năng reasoning loops như Self-Query, C-RAG, Adaptive RAG, hoặc gọi công cụ ngoài qua API thay vì chỉ đọc vector DB thụ động.
