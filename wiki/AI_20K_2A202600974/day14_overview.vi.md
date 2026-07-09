---
type: overview
title: "Day 14: AI Evaluation & Benchmarking"
description: "Đo lường chất lượng AI một cách khoa học bằng các framework, golden datasets và các phương pháp LLM-as-Judge."
tags: [ai, 20k, day14, evaluation, benchmarking]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/14/day14-ai-evaluation-benchmarking_E403.pdf"]
---

# Ngày 14: Đánh giá & Kiểm chuẩn AI

## Nội dung chính


Evaluation (đánh giá) là một kĩ năng cốt lõi (engineering discipline) giúp đội ngũ phát triển biết Agent của mình đã tốt đến đâu, tránh việc nhận định bằng cảm tính hay vibe check. Nó như một bộ "Unit Test" cho AI phi định hình.


## Chiến lược Đánh giá


Đánh giá AI cần bóc tách các tầng (Layer) để tìm ra đâu là nơi mắc lỗi:
- **Đánh giá Retrieval**: Kiểm tra khả năng tìm tài liệu của hệ thống, sử dụng các metric như **Hit Rate** (có tìm thấy không), **MRR** (xếp hạng tài liệu đúng đầu tiên), **NDCG**. Retrieval kém là giới hạn trần của Generation.
- **Đánh giá Generation (RAGAS)**: Sử dụng các metrics từ framework RAGAS như Context Recall, Context Precision, Faithfulness (không bịa ngoài context), và Answer Relevancy.


## Xây dựng Bộ Dữ liệu Chuẩn (Golden Datasets)


- Đừng dùng các bài test chung chung, hãy dùng data của riêng miền kiến thức dự án.
- Tự động sinh dữ liệu test (Synthetic Data Generation - SDG) có thể giúp tăng quy mô bộ test nhanh chóng, nhưng cần lưu ý loại bỏ các câu hỏi quá đơn giản, ưu tiên các edge cases.
- **Goodhart’s Law & Contamination**: Điểm benchmark công cộng dễ bị ảo do mô hình học thuộc (memorization). Cần tập test "held-out" (ẩn) riêng để chống gian lận.


## LLM-as-Judge & Thống kê


- Thay vì dùng con người chấm điểm hàng ngàn câu hỏi tốn kém, sử dụng một LLM mạnh làm Giám khảo (Judge).
- Để giảm thiên kiến (position bias, verbosity bias) của LLM-as-Judge, có thể kết hợp **Multi-Judge Consensus** (nhân xưng nhiều giám khảo, biểu quyết số đông).
- Luôn so sánh **Pairwise** (chấm trên cùng một tập test) thay vì pointwise để thấy rõ sự khác biệt giữa hai phiên bản, đồng thời áp dụng phương pháp thống kê (Confidence Intervals) để loại bỏ kết quả do may rủi.
- **Regression Release Gate**: Cắm Evaluation vào CI/CD để chặn (block) việc deploy nếu chất lượng sinh phản hồi giảm đi.

