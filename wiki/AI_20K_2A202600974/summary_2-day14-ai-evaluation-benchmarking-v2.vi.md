---
type: summary
title: "Summary of 2-day14-ai-evaluation-benchmarking-v2"
description: "Tổng hợp kiến thức về đo lường và đánh giá chất lượng AI một cách khoa học từ Day 14."
tags: [ai, 20k, day14]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/14/2-day14-ai-evaluation-benchmarking-v2.pdf"]
---

# Đo lường chất lượng AI một cách khoa học (AI Evaluation & Benchmarking)

## 1. Từ Monitoring sang Evaluation
- **Day 13 (Monitoring):** Tập trung vào việc hiểu hệ thống (agent) đang chạy như thế nào thông qua việc ghi nhận structured log, traces và lập dashboard theo dõi (latency, cost, errors).
- **Day 14 (Evaluation):** Tập trung đánh giá xem hệ thống làm việc **tốt đến đâu**. Trả lời các câu hỏi:
  - Agent trả lời có chính xác không?
  - Dữ liệu có bám sát ngữ cảnh (faithful) không?
  - Khi sai, sai ở đâu và tại sao sai?
  - So sánh chất lượng giữa các phiên bản (vd: tuần này với tuần trước).
> Có thể tận dụng ngay các dữ liệu log (Langfuse) từ hệ thống Monitoring ở Day 13 làm Data Source đầu vào để chạy các bộ Evaluation offline.

## 2. Các phương pháp đánh giá truyền thống và sự chuyển dịch (Paradigm Shift)
- **Chế độ Tất định (Deterministic - Truyền thống):** Dựa vào đánh giá Exact Match hoặc các thước đo N-Gram (BLEU, ROUGE, WER). Các chỉ số này **trừng phạt các câu trả lời diễn đạt theo cách khác (paraphrasing)** và không phát hiện ra mâu thuẫn về mặt logic.
- **Chế độ Xác suất (Probabilistic - AI Tạo sinh):** Sinh văn bản theo xác suất, có hàng ngàn cách diễn đạt.
- **Cosine Similarity:** Đánh giá độ tương đồng vector khá tốt trong việc nắm bắt chủ đề (Topic) nhưng thường **bỏ sót sự mâu thuẫn trái ngược** (ví dụ "yêu" và "ghét" vẫn có độ tương đồng cosine rất cao).
- **Hướng giải quyết:** Cần hệ thống có khả năng hiểu logic và ngữ nghĩa sâu $\Rightarrow$ **LLM-as-Judge**.

## 3. Nền tảng Đánh giá (Evaluation Fundamentals)
Đánh giá AI cần một phương pháp tiếp cận khoa học, tránh cảm tính: **Hypothesis -> Experiment -> Measure -> Conclude**.
- **3 Phân loại đánh giá chính:**
  1. **Batch test:** (Offline) Kiểm thử trên một tập dữ liệu "vàng" (Golden dataset) ở mỗi lần release hoặc thay đổi prompt.
  2. **Monitor quality:** (Online) Giám sát chất lượng hoạt động liên tục dựa trên traffic truy cập của người dùng thực.
  3. **Expert review:** Đánh giá chất lượng đầu ra một cách thủ công qua lấy mẫu (sampled), dùng để calibrate.
> Cần kết hợp cả 3 phương pháp. Nếu không đo lường bằng con số thì không thể cải thiện. Không thể chỉ dựa hoàn toàn vào offline hoặc chỉ dựa vào human review do khả năng scale kém.

## 4. Các Metrics dành cho AI Agent
Lựa chọn thước đo tuỳ theo use case:
- **Task Completion:** Hoàn thành bao nhiêu % nhiệm vụ, tỷ lệ hoàn thành các bước.
- **Answer Quality:** Độ chính xác (Accuracy), độ trọn vẹn (Completeness), độ mạch lạc (Coherence) và tính chính xác của trích dẫn (Citation).
- **RAG-Specific Metrics (Quan trọng):**
  - **Context Recall:** Mức độ lấy đủ thông tin cần thiết. Thấp = Retrieve thiếu.
  - **Context Precision:** Mức độ lấy đúng và trúng các tài liệu liên quan. Thấp = Retrieve thừa/sai ngữ cảnh.
  - **Faithfulness:** Mức độ trung thành của câu trả lời với context. Thấp = Bị ảo giác (Hallucinate).
  - **Answer Relevancy:** Câu trả lời có đúng với câu hỏi đặt ra không. Thấp = Trả lời lạc đề.
- **Business Metrics:** Mức độ hài lòng của khách hàng, thời gian & chi phí tiết kiệm được.

## 5. Thiết kế Benchmark
Benchmark tốt là nền tảng của evaluation ("garbage in, garbage out").
- **Golden Dataset:** Gồm Câu hỏi, Câu trả lời chuẩn (Expected answers), Context và Difficulty.
  - *Sizing:* 30-50 câu hỏi giúp test nhanh (Smoke Test) phục vụ rapid dev. 100-200 câu hỏi giúp phân tích có ý nghĩa thống kê cho production.
  - *Phân bổ (Stratified Sampling):* Cần kết hợp hài hòa các cấp độ Dễ (truy xuất fact đơn giản) - Trung bình (multi-step reasoning) - Khó (ambiguous) và adversarial (cố tình lách luật).
- Cần quan tâm đặc biệt tới **Edge cases** (Truy vấn đa ngôn ngữ, mập mờ ý nghĩa, out-of-scope).

Sử dụng AI mạnh (như GPT-4) đóng vai trò ban giám khảo chấm điểm các AI khác.
- **Rubric Design:** Cần xác định một bộ tiêu chí với các mức từ 1 đến 5 cực kỳ rõ ràng, đưa ra các ví dụ mô tả cụ thể cho từng mức.
- **Xử lý thiên kiến (Bias) cho Judge:**
  - *Vị trí:* Randomize thứ tự câu trả lời A/B.
  - *Độ dài:* Ghi rõ trong rubric "ngắn gọn là tốt" (concise is OK).
  - *Thiên vị model:* Dùng kết hợp nhiều mô hình Judge khác nhau.
> Hãy yêu cầu LLM-as-Judge xuất ra lý do (Rationale) để giải thích lựa chọn của mình trước khi in ra điểm số. Nên Calibrate các kết quả này đối chiếu với một tập nhỏ do Human đánh giá.

## 7. Các Framework Đánh giá: RAGAS, DeepEval, TruLens
| :--- | :--- | :--- | :--- |
| **Mục đích** | Đánh giá thuần các RAG Metrics | Tích hợp CI/CD, Unit Testing cho LLM | Giám sát chất lượng Production + Offline |
| **Metrics nổi bật** | 4 RAG metrics cốt lõi | Hơn 14 metrics (kể cả Toxicity, Bias...) | Dựa trên Feedback functions |
| **Đặc điểm** | Dễ dùng cho team quen Python, độ đo chuẩn mực | Viết Test như Pytest-native, tập trung CI/CD | Instrument trực tiếp vào code, Dashboard web có sẵn |
**Mẹo chọn:** Có thể kết hợp RAGAS/DeepEval cho đánh giá đầu vào tự động (Quality Gate) và TruLens cho giám sát vận hành thực tế.

## 8. Phân tích Lỗi (Failure Analysis) và Vòng lặp cải tiến
- **Failure Taxonomy (Phân loại lỗi):** Gom lỗi thành các nhóm như Wrong Answer (thường do retrieval miss), Hallucination (thiếu guardrail), Slow response (model lớn).
- **Phương pháp "5 Whys":** Trực tiếp đào sâu để tìm Root Cause (Nguyên nhân gốc rễ). Hầu hết vấn đề nằm ở Pipeline xử lý Data (Ví dụ: retriever lấy sai tài liệu) chứ không nằm ở Prompt.
- **Failure Clustering:** Hãy gom lỗi theo nhóm cùng nguyên nhân (Root cause) rồi tìm giải pháp để tối đa hóa hiệu quả "Sửa 1 chỗ xử lý được 15 lỗi" thay vì tối ưu từng lỗi một lẻ tẻ.
- **Vòng lặp phát triển (Continuous Improvement Loop):** Evaluate (Đo lường) $\rightarrow$ Analyze (Phân tích) $\rightarrow$ Improve (Khắc phục Root Cause) $\rightarrow$ Augment (Bổ sung case lỗi vào Benchmark). Cứ thế lặp lại.
