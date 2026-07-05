---
type: summary
title: "Day 18 Track 3: Production RAG"
description: "Chẩn đoán và tối ưu RAG cho môi trường Production"
tags: [ai, 20k, day18]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-day18-production-rag.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# Production RAG

Học cách đưa RAG từ Demo (60% accuracy) lên Production (85%+ accuracy):
- **Phân tích Error Tree**: Phân biệt lỗi do Ingestion (Offline) hay Retrieval (Online).
- **Offline Ingestion**: Các chiến lược Chunking (Hierarchical, Late Chunking, Semantic), Enrichment (Summarization, Hypothetical Q&A) để chuẩn bị dữ liệu chất lượng.
- **Online Retrieval**: Vượt qua giới hạn của Flat RAG bằng Two-Stage Retrieval (Bi-encoder sau đó dùng Cross-encoder Rerank) và Hybrid Search (BM25 + Dense).
- **Close the Loop**: Đánh giá bằng RAGAS metrics (Context Recall, Context Precision, Faithfulness, Answer Relevancy) để biết điểm yếu nằm ở tầng nào và tiến hành tối ưu đúng chỗ.
