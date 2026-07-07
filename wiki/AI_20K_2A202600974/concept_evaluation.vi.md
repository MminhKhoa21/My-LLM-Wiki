---
type: concept
title: "AI Evaluation & Benchmarking"
description: "Tổng hợp các kỹ thuật, framework và mindset để đánh giá chất lượng sản phẩm AI."
tags: [ai, 20k, concept, evaluation, benchmarking]
timestamp: 2026-07-05
sources: []
---

*Đánh giá AI & Thiết lập điểm chuẩn*


*Trang này tổng hợp các kiến thức về AI Evaluation, bao gồm cả góc nhìn Product, Engineering và Data từ nhiều ngày khác nhau.*

## 1. Tư duy nền tảng (Day 14, Day 21, Day 22)


**Đánh giá AI không chỉ là đo usage**:


- Truyền thống: Đo Conversion, Retention, CTR.
- AI Product: Đo **Agent Success Rate**, **Output Quality Distribution**.
- Câu hỏi chính: AI có hiểu đúng intent? Làm đúng task? Có tuân thủ policy? Lỗi có chấp nhận được không?



- **Model Eval**: Model có năng lực nền tảng tốt không? (MMLU, HumanEval) - Research Team lo.
- **Application Eval**: Trong context của app này, user này, kết quả có tốt không? - Product Team lo.
- Chi tiết: [[day22_track1]]

## 2. Các Framework Đánh Giá


### 2.1 Đánh giá RAG (RAGAS - Day 24)


RAGAS là framework chuẩn để đo lường RAG pipeline:


- **Faithfulness**: Đo lường Hallucination. Trả lời có dựa trên context?
- **Context Relevance**: Context có relevancy tốt không?
- **Answer Relevance**: Câu trả lời có đúng ý câu hỏi?
- **Context Recall**: Retriever lấy đủ chunk không?
- Chi tiết: [[day24_track3]]



Dùng một LLM mạnh (như GPT-4) để đánh giá output của hệ thống.


- **4 Biases cần tránh**: Position bias, Verbosity bias, Self-enhancement bias, Authority bias.
- Cách khắc phục: Swap positions, normalize length, blind evaluation.

## 3. Vòng đời AI Eval (Day 21)


- **Pre-release**: Thiết kế Scenario Dataset (Coverage cao), kiểm tra trước khi deploy.
- **Rollout**: A/B Test, phân tích quality distribution.
- **Production**: Học từ production traces, phát hiện failure clusters.
- Chi tiết: [[day21_track1]]

## 4. Liên quan đến Data Observability


Đánh giá AI liên quan chặt chẽ đến việc quan sát chất lượng dữ liệu:


- Ranh giới giữa Eval và Observability: Eval thường là batch/offline hoặc sample, Observability là real-time/online.
- Chi tiết: [[day23_track2]], [[day27_track2]]
