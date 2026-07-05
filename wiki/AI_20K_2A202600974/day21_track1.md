---
type: summary
title: "Day 21 – Track 1: AI Evaluation (Vai trò PM)"
description: "Vai trò của AI Product Manager trong việc thiết kế và vận hành hệ thống đánh giá AI, từ giai đoạn phát triển đến sản xuất."
tags: [ai, 20k, day21, track1, evaluation, pm]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/d21-slide-v0.pdf", "raw/AI_20K_2A202600974/21/day21-lab-instruction.pdf"]
---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]


# Day 21 – Track 1: AI Evaluation – Vai trò PM

**Giảng viên**: Mai Anh Nguyen (Blue) – Generalist Product Builder  
**Khóa**: AICB Phase 2 · Ngày 21 · Track 1

---

## Bối cảnh: Khi feature AI scale lên production

AI Product khác với phần mềm truyền thống ở chỗ:  
- **Traditional Product**: Deterministic user flows → đo Conversion Rate, Retention, CTR.  
- **AI Product**: Wide outcome distributions → đo **Agent Success Rate**, **Output Quality Distribution**.

Khi số lượng user tăng, quality phân tán – PM không thể chỉ xem log mà phải thiết kế hệ thống **Eval** bài bản.

---

## Phân biệt 2 lớp Evaluation

| Lớp | Câu hỏi chính | Ai sở hữu | Ví dụ |
|-----|--------------|-----------|-------|
| **Model eval** | Model có reasoning, instruction-following, safety tốt không? | Model provider, research team | MMLU, coding benchmark |
| **Application eval** | Trong sản phẩm này, với user này, trong context này, output có đủ tốt không? | Product + Engineering + Domain expert | Task completion rate, hallucination rate |

---

## Vòng đời AI Eval qua từng giai đoạn

1. **Pre-release**: Thiết kế Scenario Dataset, kiểm tra coverage trước khi deploy.
2. **Rollout**: A/B test, phân tích quality distribution cho nhóm user thử nghiệm.
3. **Production**: Học từ production trace, phát hiện failure cluster, liên tục cải thiện.

---

## Lab 21: Thiết kế Test Inputs

**Logic bài lab**:  
`Use case (Day 18/19)` → `Quality Question` → `User Input Grid` → `Meaningful Combinations` → `AI-assisted Input Generation` → `Human Filtering` → `Scenario Dataset v0` → `Group Coverage Review` → `Scenario Dataset v1`

**Điểm cốt lõi**: Human quyết định coverage. AI chỉ giúp viết nhiều cách diễn đạt tự nhiên hơn.

---

## Liên kết
- [[day21_track2]] – CI/CD AI Systems
- [[day21_track3]] – Fine-tuning LLMs
- [[day21_overview]]
