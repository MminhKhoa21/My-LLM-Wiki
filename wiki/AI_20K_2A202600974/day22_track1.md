---
type: summary
title: "Day 22 – Track 1: AI Evals Reference Guide (Góc nhìn PM)"
description: "Tư duy nền tảng về đánh giá AI: phân biệt model eval vs application eval, cách đo chất lượng output AI trong sản phẩm thực."
tags: [ai, 20k, day22, track1, evaluation, pm]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/1-d22-slide.pdf", "raw/AI_20K_2A202600974/22/ai-evals-reference-guide-vi.pdf"]
---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]


# Day 22 – Track 1: AI Evals Reference Guide

---

## Tư duy nền tảng

### 1.1 Đánh giá AI không chỉ là đo usage

Với **sản phẩm AI**, câu hỏi chính khác biệt hoàn toàn:
- AI có hiểu đúng **intent** của người dùng không?
- AI có làm đúng **phần việc** được giao không?
- AI có ra quyết định hợp lý trong điều kiện **thiếu thông tin** không?
- AI có tuân thủ **policy, constraint, permission** và business rule không?
- Khi AI sai, lỗi đó có **chấp nhận được** không?

### 1.2 Model eval vs Application eval

| Lớp | Câu hỏi | Ai sở hữu | Ví dụ |
|-----|---------|-----------|-------|
| **Model eval** | Model reasoning, safety, coding tốt không? | Model provider / research | MMLU, HumanEval, safety benchmark |
| **Application eval** | Trong sản phẩm này, với user này, output đủ tốt không? | Product + Engineering + Domain expert | Task success rate, hallucination rate |

---

## Các loại metric trong Application Eval

| Loại | Ví dụ metric |
|------|-------------|
| **Correctness** | Factual accuracy, citation check |
| **Completeness** | Missing information rate |
| **Groundedness** | Faithfulness vs retrieved context |
| **Safety** | Harmful output rate, PII leakage |
| **Efficiency** | Latency, token cost per request |

---

## Liên kết
- [[day21_track1]] – AI Evals (Day 21)
- [[day24_track3]] – RAGAS & Guardrails (đánh giá RAG cụ thể)
- [[day22_overview]]
