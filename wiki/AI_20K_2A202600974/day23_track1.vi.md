---
type: summary
title: "Day 23 – Track 1: RAGAS, LLM-as-Judge & Guardrails"
description: "Đo lường và bảo vệ AI Agent thông qua framework RAGAS, LLM-as-Judge và kiến trúc Guardrails đa lớp."
tags: [ai, 20k, day23, track1, ragas, evaluation, guardrails, llm-as-judge]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/1-day24-ragas-guardrails.pdf"]
---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]


**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 3 / 1

> **Câu hỏi trọng tâm**: Làm sao đảm bảo chatbot không bịa đặt chính sách (như Air Canada), chửi lại công ty (như DPD), hay bị lộ mã nguồn (như Samsung)? Giải pháp nằm ở Evaluation và Guardrails.

## 1. Nền Tảng Đánh Giá (Foundations of Evaluation)
- Vibe-check không scale: Cần automated evals (L1 Heuristic -> L2 Component/RAGAS -> L3 LLM-as-Judge -> L4 Human Eval).
- **Reference-based**: Cần ground truth (vd: exact match, BLEU, Context Recall).
- **Reference-free**: Dùng được ở production (vd: Faithfulness, Answer Relevancy).

RAGAS là chuẩn de-facto cho đánh giá pipeline RAG:
1. **Faithfulness** (Câu trả lời ↔ Context): Đo hallucination. Answer sinh ra có được support từ context không.
2. **Answer Relevancy** (Câu trả lời ↔ Câu hỏi): Đo sự đi đúng trọng tâm (on-topic). Tạo câu hỏi ngược từ answer và đo cosine similarity với câu hỏi gốc.
3. **Context Precision** (Ranking của retrieved chunks): NDCG score, xem thông tin cần thiết có ở top kết quả không.
4. **Context Recall** (Bao phủ Ground Truth): Có lấy đủ chunk chứa thông tin trả lời ground truth không.

## 3. LLM-as-Judge và 4 Biases
Sử dụng LLM thay thế con người cho scale lớn với chi phí rẻ hơn (cần đo Cohen’s Kappa so với con người):
1. **Position Bias**: Có xu hướng chọn câu đầu hoặc câu cuối (Khắc phục: swap-and-average).
2. **Length Bias**: Ưu tiên output dài "có vẻ thông minh" (Khắc phục: length penalty).
3. **Self-Enhancement Bias**: Ưu tiên văn phong của chính nó (Khắc phục: Cross-judge protocol, VD: GPT-4 đánh giá Claude, Claude đánh giá GPT-4).
4. **Style Bias**: Ưu tiên format markdown đẹp hơn là ý nghĩa (Khắc phục: strip text trước khi đánh giá).

- **SelfCheckGPT**: Kiểm tra tính nhất quán (Consistency). Cùng một context mà sinh ra nhiều answers mâu thuẫn nhau -> dễ là hallucination.
- **NLI (Natural Language Inference)**: Phân loại mâu thuẫn/đồng thuận giữa answer và context.

## 5. Guardrails - Kiến Trúc 4 Lớp
- **L1 - Input Layer**: Chặn PII bằng Regex/Presidio, lọc chủ đề (ValidTopic).
- **L2 - LLM Layer**: Chặn bằng System Prompt Rules.
- **L3 - Output Layer**: Phân loại an toàn (Llama Guard 3), NLI checks.
- **L4 - Audit Layer**: Log và sample để phân tích.

Bảo vệ khỏi các cuộc tấn công như **Prompt Injection** (DAN) hay **Session Poisoning** (nhúng mã độc vào lịch sử hội thoại).

## 6. Liên Kết
- [[concept_rag]] – Các thành phần RAG cơ bản
- [[concept_evaluation]] – Tổng quan đánh giá Agent
