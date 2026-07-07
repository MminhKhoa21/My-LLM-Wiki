---
type: concept
title: "AI Evaluation & Benchmarking"
description: "Tổng hợp các kỹ thuật, framework và mindset để đánh giá chất lượng sản phẩm AI."
tags: [ai, 20k, concept, evaluation, benchmarking]
timestamp: 2026-07-05
sources: []
---
# AI Evaluation & Benchmarking

*Đánh giá AI & Thiết lập điểm chuẩn*

This page compiles knowledge about AI Evaluation, covering Product, Engineering, and Data perspectives from various days.

*Trang này tổng hợp các kiến thức về AI Evaluation, bao gồm cả góc nhìn Product, Engineering và Data từ nhiều ngày khác nhau.*

## 1. Tư duy nền tảng (Day 14, Day 21, Day 22)

*1. Foundational Thinking (Day 14, Day 21, Day 22)*

**Đánh giá AI không chỉ là đo usage**:

*Evaluating AI is not just about measuring usage:*

- Truyền thống: Đo Conversion, Retention, CTR.
  *Traditional: Measure Conversion, Retention, CTR.*
- AI Product: Đo **Agent Success Rate**, **Output Quality Distribution**.
  *AI Product: Measure **Agent Success Rate**, **Output Quality Distribution**.*
- Câu hỏi chính: AI có hiểu đúng intent? Làm đúng task? Có tuân thủ policy? Lỗi có chấp nhận được không?
  *Key questions: Does the AI understand the correct intent? Does it perform the task correctly? Does it adhere to policy? Are errors acceptable?*

**Model Eval vs Application Eval**:

*Model Eval vs Application Eval:*

- **Model Eval**: Model có năng lực nền tảng tốt không? (MMLU, HumanEval) - Research Team lo.
  *Model Eval: Does the model have good foundational capabilities? (MMLU, HumanEval) – Handled by the Research Team.*
- **Application Eval**: Trong context của app này, user này, kết quả có tốt không? - Product Team lo.
  *Application Eval: In the context of this app and this user, is the outcome good? – Handled by the Product Team.*
- Chi tiết: [[day22_track1]]
  *Details: [[day22_track1]]*

## 2. Các Framework Đánh Giá

*2. Evaluation Frameworks*

### 2.1 Đánh giá RAG (RAGAS - Day 24)

*2.1 RAG Evaluation (RAGAS - Day 24)*

RAGAS là framework chuẩn để đo lường RAG pipeline:

*RAGAS is the standard framework for measuring RAG pipelines:*

- **Faithfulness**: Đo lường Hallucination. Trả lời có dựa trên context?
  *Faithfulness: Measures hallucination. Is the answer grounded in the context?*
- **Context Relevance**: Context có relevancy tốt không?
  *Context Relevance: Is the context relevant enough?*
- **Answer Relevance**: Câu trả lời có đúng ý câu hỏi?
  *Answer Relevance: Does the answer address the question correctly?*
- **Context Recall**: Retriever lấy đủ chunk không?
  *Context Recall: Does the retriever fetch enough chunks?*
- Chi tiết: [[day24_track3]]
  *Details: [[day24_track3]]*

### 2.2 LLM-as-a-Judge (Day 24)

*2.2 LLM-as-a-Judge (Day 24)*

Dùng một LLM mạnh (như GPT-4) để đánh giá output của hệ thống.

*Use a strong LLM (e.g., GPT-4) to evaluate the system's output.*

- **4 Biases cần tránh**: Position bias, Verbosity bias, Self-enhancement bias, Authority bias.
  *4 Biases to avoid: Position bias, Verbosity bias, Self-enhancement bias, Authority bias.*
- Cách khắc phục: Swap positions, normalize length, blind evaluation.
  *Mitigation: Swap positions, normalize length, blind evaluation.*

## 3. Vòng đời AI Eval (Day 21)

*3. AI Eval Lifecycle (Day 21)*

- **Pre-release**: Thiết kế Scenario Dataset (Coverage cao), kiểm tra trước khi deploy.
  *Pre-release: Design Scenario Dataset (high coverage), test before deployment.*
- **Rollout**: A/B Test, phân tích quality distribution.
  *Rollout: A/B Test, analyze quality distribution.*
- **Production**: Học từ production traces, phát hiện failure clusters.
  *Production: Learn from production traces, detect failure clusters.*
- Chi tiết: [[day21_track1]]
  *Details: [[day21_track1]]*

## 4. Liên quan đến Data Observability

*4. Related to Data Observability*

Đánh giá AI liên quan chặt chẽ đến việc quan sát chất lượng dữ liệu:

*AI evaluation is closely tied to monitoring data quality:*

- Feature Drift, Label Drift.
  *Feature Drift, Label Drift.*
- Ranh giới giữa Eval và Observability: Eval thường là batch/offline hoặc sample, Observability là real-time/online.
  *Boundary between Eval and Observability: Eval is typically batch/offline or sampled, Observability is real-time/online.*
- Chi tiết: [[day23_track2]], [[day27_track2]]
  *Details: [[day23_track2]], [[day27_track2]]*
