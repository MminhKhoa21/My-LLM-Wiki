---
type: summary
title: "Day 24 – Track 1: AI Ethics, Safety & Responsible AI"
description: "Xây dựng AI có trách nhiệm, đạo đức và an toàn – từ catastrophic risks đến practical framework."
tags: [ai, 20k, day24, track1, ethics, safety, responsible-ai]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/24/d24-slide-v1.pdf", "raw/AI_20K_2A202600974/24/day24-track1-lab.pdf", "raw/AI_20K_2A202600974/24/lab24-student-edition.pdf"]
---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]


# Day 24 – Track 1: AI Ethics, Safety & Responsible AI

**Giảng viên**: Mai Anh Nguyen (Blue)  
**Khóa**: AICB Phase 2 · Track 1 · Ngày 24

---

## Câu hỏi khởi động

> Khi nghe "AI an toàn & có đạo đức", bạn nghĩ tới gì?  
> *(Tham khảo: "The Catastrophic Risks of AI – Yoshua Bengio | TED")*

---

## Các rủi ro của AI

| Loại rủi ro | Ví dụ |
|-------------|-------|
| **Bias & Discrimination** | Model phân biệt đối xử theo giới tính, chủng tộc |
| **Hallucination** | AI bịa thông tin y tế, pháp lý, tài chính |
| **Privacy** | Model "nhớ" và leak PII từ training data |
| **Misuse** | Deepfake, disinformation, autonomous weapons |
| **Existential risk** | AGI vượt tầm kiểm soát (long-term) |

---

## Framework Responsible AI

### Nguyên tắc cốt lõi
1. **Fairness**: Không phân biệt đối xử trong quyết định
2. **Transparency**: Giải thích được quyết định của model
3. **Accountability**: Có người chịu trách nhiệm khi AI sai
4. **Privacy**: Bảo vệ dữ liệu cá nhân
5. **Safety**: Không gây hại cho người dùng và xã hội

### Thực hành trong sản phẩm
- **Bias auditing**: Test model trên các subgroup khác nhau
- **Explainability**: LIME, SHAP cho feature importance
- **Human oversight**: Luôn có mechanism để human override
- **Incident response**: Quy trình xử lý khi AI sai

---

## Liên kết
- [[day11_overview]] – Guardrails & AI Safety (foundation)
- [[day24_track3]] – RAGAS & Guardrails (technical implementation)
- [[day24_overview]]
