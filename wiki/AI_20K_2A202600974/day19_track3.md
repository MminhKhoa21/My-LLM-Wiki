---
type: summary
title: "Day 19 Track 3: GraphRAG and Knowledge Graphs"
description: "Tích hợp Đồ thị Tri thức vào RAG"
tags: [ai, 20k, day19]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/GraphRAG and Knowledge Graphs.pdf", "raw/AI_20K_2A202600974/19/LAB DAY 19.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# GraphRAG & Knowledge Graphs

Giải quyết điểm mù của Flat RAG (khó suy luận quan hệ phức tạp, multi-hop):
- **Knowledge Graph (KG)**: Chuyển dữ liệu văn bản thô thành các Triple (Chủ thể - Mối quan hệ - Tân ngữ).
- **Quy trình GraphRAG**:
  1. Trích xuất Thực thể (NER) và Quan hệ (Relation Extraction).
  2. Xây dựng đồ thị (sử dụng Neo4j hoặc NetworkX) kèm các kỹ thuật chuẩn hóa (Deduplication).
  3. Truy vấn: Tìm kiếm Node gốc (Seed) bằng semantic search và duyệt đồ thị (Graph Traversal).
  4. Văn bản hóa subgraph và giao cho LLM sinh câu trả lời.
- Ứng dụng thực tiễn trong y tế, pháp lý, phân tích supply chain.
