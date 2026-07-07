---
type: overview
title: "Day 14: AI Evaluation & Benchmarking"
description: "Đo lường chất lượng AI một cách khoa học bằng các framework, golden datasets và các phương pháp LLM-as-Judge."
tags: [ai, 20k, day14, evaluation, benchmarking]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/14/day14-ai-evaluation-benchmarking_E403.pdf"]
---
# Day 14: AI Evaluation & Benchmarking

*# Ngày 14: Đánh giá & Kiểm chuẩn AI*

## Nội dung chính

*## Main Content*

Evaluation (đánh giá) là một kĩ năng cốt lõi (engineering discipline) giúp đội ngũ phát triển biết Agent của mình đã tốt đến đâu, tránh việc nhận định bằng cảm tính hay vibe check. Nó như một bộ "Unit Test" cho AI phi định hình.

*Evaluation is a core engineering discipline that helps development teams know how good their Agent is, avoiding gut feelings or vibe checks. It acts as a set of "Unit Tests" for non-deterministic AI.*

## Chiến lược Đánh giá

*## Evaluation Strategy*

Đánh giá AI cần bóc tách các tầng (Layer) để tìm ra đâu là nơi mắc lỗi:
- **Đánh giá Retrieval**: Kiểm tra khả năng tìm tài liệu của hệ thống, sử dụng các metric như **Hit Rate** (có tìm thấy không), **MRR** (xếp hạng tài liệu đúng đầu tiên), **NDCG**. Retrieval kém là giới hạn trần của Generation.
- **Đánh giá Generation (RAGAS)**: Sử dụng các metrics từ framework RAGAS như Context Recall, Context Precision, Faithfulness (không bịa ngoài context), và Answer Relevancy.

*AI evaluation needs to decompose layers to pinpoint where errors occur:*
- ***Retrieval Evaluation***: *Checks the system's ability to find documents, using metrics like **Hit Rate** (whether it was found), **MRR** (rank of the first correct document), **NDCG**. Poor retrieval caps the ceiling of Generation.*
- ***Generation Evaluation (RAGAS)***: *Uses metrics from the RAGAS framework such as Context Recall, Context Precision, Faithfulness (no hallucination beyond context), and Answer Relevancy.*

## Xây dựng Bộ Dữ liệu Chuẩn (Golden Datasets)

*## Building Golden Datasets*

- Đừng dùng các bài test chung chung, hãy dùng data của riêng miền kiến thức dự án.
- Tự động sinh dữ liệu test (Synthetic Data Generation - SDG) có thể giúp tăng quy mô bộ test nhanh chóng, nhưng cần lưu ý loại bỏ các câu hỏi quá đơn giản, ưu tiên các edge cases.
- **Goodhart’s Law & Contamination**: Điểm benchmark công cộng dễ bị ảo do mô hình học thuộc (memorization). Cần tập test "held-out" (ẩn) riêng để chống gian lận.

*- Do not use generic tests; use data from your project’s own domain.*
*- Synthetic Data Generation (SDG) can quickly scale up your test set, but be careful to remove overly simple questions and prioritize edge cases.*
*- **Goodhart’s Law & Contamination**: Public benchmark scores are easily inflated due to model memorization. A separate held-out test set is needed to prevent cheating.*

## LLM-as-Judge & Thống kê

*## LLM-as-Judge & Statistics*

- Thay vì dùng con người chấm điểm hàng ngàn câu hỏi tốn kém, sử dụng một LLM mạnh làm Giám khảo (Judge).
- Để giảm thiên kiến (position bias, verbosity bias) của LLM-as-Judge, có thể kết hợp **Multi-Judge Consensus** (nhân xưng nhiều giám khảo, biểu quyết số đông).
- Luôn so sánh **Pairwise** (chấm trên cùng một tập test) thay vì pointwise để thấy rõ sự khác biệt giữa hai phiên bản, đồng thời áp dụng phương pháp thống kê (Confidence Intervals) để loại bỏ kết quả do may rủi.
- **Regression Release Gate**: Cắm Evaluation vào CI/CD để chặn (block) việc deploy nếu chất lượng sinh phản hồi giảm đi.

*- Instead of using humans to score thousands of questions at high cost, use a strong LLM as a Judge.*
*- To reduce biases (position bias, verbosity bias) of LLM-as-Judge, you can combine **Multi-Judge Consensus** (multiple judges, majority voting).*
*- Always compare **Pairwise** (evaluate on the same test set) rather than pointwise to clearly see differences between two versions, and apply statistical methods (Confidence Intervals) to rule out luck-based results.*
*- **Regression Release Gate**: Integrate evaluation into CI/CD to block deployment if response quality degrades.*
