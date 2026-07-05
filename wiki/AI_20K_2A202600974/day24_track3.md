---
type: summary
title: "Day 24 – Track 3: RAGAS, LLM-as-Judge & Guardrails"
description: "Đo lường và bảo vệ Agent: 4 RAGAS metrics, LLM-as-Judge biases, Hallucination Detection, Guardrails production patterns."
tags: [ai, 20k, day24, track3, ragas, guardrails, llm-judge, evaluation]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/24/2-day24-ragas-guardrails.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# Day 24 – Track 3: RAGAS, LLM-as-Judge & Guardrails

**Khóa**: AICB Phase 2 · Track 3 · Ngày 24

> **3 câu chuyện thật**: Air Canada thua kiện vì chatbot bịa chính sách. Samsung ban ChatGPT toàn công ty. DPD chatbot chửi chính công ty, viral 800k retweets. **Tất cả vì thiếu evaluation và guardrails.**

---

## RAGAS – 4 Core Metrics

| Metric | Đo lường | Câu hỏi |
|--------|---------|---------|
| **Faithfulness** | Output có trung thực với context không? | AI có bịa thêm thông tin không có trong tài liệu? |
| **Context Relevance** | Context được retrieve có liên quan không? | Retriever có lấy đúng chunk không? |
| **Answer Relevance** | Câu trả lời có trả lời đúng câu hỏi không? | AI có trả lời "lạc đề" không? |
| **Context Recall** | Context có đủ để trả lời không? | Retriever có bỏ sót chunk quan trọng không? |

```python
from ragas import evaluate
from ragas.metrics import faithfulness, context_relevancy, answer_relevancy

result = evaluate(
    dataset=eval_dataset,
    metrics=[faithfulness, context_relevancy, answer_relevancy]
)
```

---

## LLM-as-Judge – 4 Biases cần tránh

| Bias | Mô tả | Cách giảm thiểu |
|------|-------|----------------|
| **Position bias** | Ưu tiên câu trả lời ở vị trí đầu/cuối | Swap positions, average scores |
| **Verbosity bias** | Ưu tiên câu trả lời dài hơn | Normalize length |
| **Self-enhancement bias** | Ưu tiên output của chính mình | Dùng model khác làm judge |
| **Authority bias** | Ưu tiên câu trả lời có "vẻ" authority | Blind evaluation |

---

## Guardrails – 4 Trục bảo vệ

| Trục | Kỹ thuật | Công cụ |
|------|---------|---------|
| **Input rails** | Prompt injection detection, length limit | Llama Guard 3 |
| **Output rails** | Hallucination check, toxicity filter | RAGAS Faithfulness |
| **PII protection** | Redaction trước khi gửi LLM | Presidio |
| **Session protection** | Phát hiện session poisoning | NeMo Guardrails |

---

## CI/CD Integration

```yaml
# GitHub Actions: chạy RAGAS eval sau mỗi PR
- name: Run RAGAS evaluation
  run: |
    python eval/run_ragas.py --threshold 0.8
    if [ $? -ne 0 ]; then
      echo "RAGAS score below threshold, blocking merge"
      exit 1
    fi
```

---

## Liên kết
- [[day11_overview]] – Guardrails & AI Safety (nền tảng)
- [[day22_track1]] – AI Evals Reference Guide
- [[day24_overview]]
