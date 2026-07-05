---
type: summary
title: "Day 16 Track 3: Advanced Agent Architectures"
description: "Kiến trúc Agent nâng cao: Reflexion, LATS, Voyager"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/phase2-day01-advanced-agent-architectures-extended-fuller.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# Advanced Agent Architectures

Nghiên cứu nguyên nhân Single Agent (như ReAct) thất bại trong các bài toán phức tạp và cách khắc phục:
- **Reflexion**: Thêm khả năng tự đánh giá (self-evaluation) vào reasoning loop. Agent sẽ thử, đánh giá kết quả, rút ra bài học (reflection memory) và thử lại.
- **LATS (Language Agent Tree Search)**: Kết hợp Monte Carlo Tree Search với LLM để duyệt nhiều nhánh giải pháp và quay lui (undo) khi cần.
- **Voyager**: Agent có khả năng học tập tích lũy kỹ năng (compound learning) để giải quyết các task mở.
- **Checklist an toàn**: Max attempts, structured outputs, tracing, và human review.
