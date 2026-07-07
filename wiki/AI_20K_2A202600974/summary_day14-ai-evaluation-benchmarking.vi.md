---
type: summary
title: "Summary of day14-ai-evaluation-benchmarking"
description: "Tổng hợp kiến thức Ngày 14 về đo lường chất lượng AI một cách khoa học, các phương pháp đánh giá, metrics, RAGAS framework, LLM-as-Judge và phân tích lỗi."
tags: [ai, 20k, day14]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/14/day14-ai-evaluation-benchmarking.pdf"]
---

# Đo lường chất lượng AI một cách khoa học (AI Evaluation & Benchmarking)

Bài học nhấn mạnh việc đánh giá AI (Evaluation) là một quy trình kỹ thuật (engineering discipline) khoa học, chứ không phải dựa trên cảm tính ("cảm thấy agent trả lời tốt"). Không đo lường được = không cải thiện được.

## 1. 4 Chiều Chất Lượng Output của AI

Một AI Agent cần được đánh giá dựa trên 4 khía cạnh chính, bởi 1 metric đơn lẻ là không đủ:
- **Correctness (Tính chính xác):** Trả lời đúng sự thật không? Có bịa đặt (hallucinate) hay trích dẫn sai nguồn không?
- **Relevance (Tính liên quan):** Trả lời đúng trọng tâm câu hỏi của user hay lạc đề?
- **Completeness (Tính đầy đủ):** Có đủ chi tiết cần thiết không? Có bỏ sót thông tin quan trọng nào không?
- **Coherence (Tính mạch lạc):** Câu trả lời có dễ đọc, cấu trúc tốt và ngôn ngữ phù hợp không?

## 2. 3 Loại Đánh Giá (Evaluation Types)

1. **Offline (Batch test trên golden dataset):** Chạy tự động mỗi khi có thay đổi code/prompt/model để tránh regression. (Dùng RAGAS, scripts).
2. **Online (Monitor production traffic):** Theo dõi liên tục trên real traffic để phát hiện suy giảm chất lượng (degradation) ngay lập tức. (Dùng Langfuse, LangSmith).
3. **Human Eval (Expert review):** Đánh giá bởi con người trên các sample định kỳ hoặc các tác vụ rủi ro cao (high-stakes).

> **Quy tắc chi phí:** Chi phí cho evaluation phải rẻ hơn hậu quả của bug trên production khoảng 1000 lần. Agent không pass eval offline thì không được deploy.

## 3. Các Nhóm Metrics Đánh Giá

Không phải mọi metric đều như nhau. Cần chọn metrics gắn với use case và mục tiêu kinh doanh (business outcome).

- **Task Completion:** Đánh giá nhị phân (Pass/Fail), Partial credit (theo % số subtasks hoàn thành), Weighted scoring, hoặc Trajectory eval (đánh giá cả quá trình).
  - *Exact match / F1 token:* Tốt cho câu trả lời ngắn, factual.
  - *BERTScore / Embedding cosine:* Tốt cho so sánh ngữ nghĩa.
  - *LLM Judge / Human:* Tốt cho nội dung phức tạp, subjective.

Cần định nghĩa một khung 3 lớp:
1. **North Star Metric:** Chỉ số cốt lõi về business value (vd: Tỷ lệ tự giải quyết - Resolution rate).
2. **Guardrail metrics:** Các chỉ số không được phép suy giảm (vd: P95 latency $\le$ 5s, Faithfulness $\ge$ 0.8).
3. **Diagnostic metrics:** Dùng khi có sự cố để chẩn đoán (vd: Các điểm số RAGAS).


RAGAS (Retrieval Augmented Generation Assessment) là bộ khung chuẩn để đánh giá chất lượng RAG pipeline. Gồm 4 metrics (chấm điểm từ 0-1):

- **Faithfulness:** Câu trả lời có bám sát ngữ cảnh (context) lấy ra không? (Thấp = Bịa đặt/Hallucination).
- **Context Recall:** Retriever có lấy đủ thông tin cần thiết từ ground truth không? (Thấp = Retrieve thiếu tài liệu).
- **Context Precision:** Context lấy ra có chứa nhiều thông tin thực sự liên quan không? (Thấp = Retrieve nhiều nhưng bị rác/noise).
- **Answer Relevancy:** Câu trả lời có đúng với câu hỏi của user không? (Thấp = Lạc đề).

**Diagnostic Flowchart khi score thấp:**
`Context Recall` (Tăng top-k, chunk nhỏ) $\rightarrow$ `Context Precision` (Thêm re-ranking) $\rightarrow$ `Faithfulness` (Ép prompt chỉ dùng context) $\rightarrow$ `Answer Relevancy` (Cải thiện template câu trả lời).

## 5. Thiết Kế Benchmark (Benchmark Design)

*Garbage in, garbage out.* Đánh giá phụ thuộc rất lớn vào chất lượng Benchmark.

- **Golden Dataset:** Bộ dữ liệu chuẩn (thường 50-100 QA pairs cho production, 20 cho sanity check) kèm câu trả lời mẫu của chuyên gia (expected answers).
- **Cách tạo:**
  1. *Expert-written:* High-stakes, chất lượng cao nhưng tốn kém.
  2. *From production log:* Thực tế, chi phí nhãn vừa phải.
  3. *LLM-generated:* Nhanh, scale tốt, boot-strap ban đầu (luôn cần Human review).
- **Stratified Sampling:** Lấy mẫu có phân lớp (theo category, difficulty) để đảm bảo không bị bias vào một nhóm câu hỏi phổ biến.
- **Edge Cases & Adversarial Inputs:** Cần test khoảng $\ge$ 10% các trường hợp lách luật: Prompt injection, PII extraction, Jailbreak, Typos, Mixed language.
- **Data Contamination:** Tránh việc LLM đã học qua test data bằng cách giấu kín benchmark hoặc thay đổi thường xuyên.


Sử dụng LLM để chấm điểm tự động các câu trả lời dựa trên rubric rõ ràng, giúp mở rộng quy mô đánh giá mà human eval không làm được.

- **Rubric:** Cần tiêu chí rõ ràng (thang 1-5) kèm ví dụ. Có thể dùng *Reference-based* (có câu trả lời chuẩn để so) hoặc *Reference-free* (chấm độc lập theo độ dài, phong cách...).
- **Pairwise vs Pointwise:** Pairwise (A vs B) dễ chấm và ít bias hơn, tốt cho A/B testing prompt. Pointwise (điểm tuyệt đối) tiện cho track qua thời gian.
- **Chain-of-Thought (CoT):** Yêu cầu LLM Judge phân tích từng bước trước khi cho điểm sẽ giúp tăng độ đồng thuận với chuyên gia lên 15-20%.
- **7 Biases của LLM Judge:** Position bias (thiên vị vị trí), Verbosity bias (thích câu dài), Self-preference (GPT thích GPT), Sycophancy (nịnh user), Authority, Format, Recency.
- **Calibration (Hiệu chuẩn):** Luôn so sánh điểm LLM với Human trên subset $\ge$ 50 samples. Đạt Cohen's Kappa $\kappa \ge 0.6$ hoặc Spearman $\rho \ge 0.7$ mới nên dùng judge đó.

## 7. Tính Chặt Chẽ Thống Kê (Statistical Rigor)

LLM có tính ngẫu nhiên (nhiệt độ $>0$), do đó không thể kết luận dựa trên 1 lần chạy hay con số đơn lẻ.

- **Confidence Interval (CI - Khoảng tin cậy):** Chạy ít nhất 3 lần, báo cáo Mean $\pm$ Standard Deviation.
- **Significance Test:** Dùng Paired t-test để xem Agent V2 có thực sự tốt hơn V1 không (p-value $< 0.05$).
- **Power Analysis:** Để phát hiện khác biệt nhỏ (vd 0.05 điểm), cần khoảng $\ge$ 30-50 cases cho benchmark. 20 cases ở môi trường Lab chỉ là sanity check.

## 8. Đánh Giá Safety và Agentic Behavior

Đối với Agent có dùng Tools (Công cụ) và thực hiện nhiều bước (Multi-step):
- **Trajectory Evaluation:** Đánh giá cả quá trình (Step correctness, Efficiency) thay vì chỉ kết quả cuối cùng. Agent có thể ra kết quả đúng nhưng đi vòng vèo, lãng phí tài nguyên.
- **Safety Eval:** Test Jailbreak (từ chối $\ge$ 95%), PII leakage (0% rò rỉ), Toxicity (0%), Financial/Medical advice (từ chối).
- **Bias & Fairness:** Kiểm tra độ công bằng giữa các nhóm giới tính, ngôn ngữ thiểu số, độ tuổi.
- **Red Team:** Thuê chuyên gia cố tình bẻ khóa hệ thống trong thời gian giới hạn để phát hiện lỗ hổng trước major release.

## 9. Phân Tích Lỗi (Failure Analysis & Continuous Improvement)

Điểm số chỉ cho biết vấn đề, Failure Analysis mới chỉ ra cách sửa.
- **Phân loại lỗi:** Wrong answer, Hallucination, Tool failure, Refusal, Slow, Inconsistent...
- **5 Whys:** Đặt câu hỏi "Tại sao" 5 lần để tìm *Root Cause* (Nguyên nhân gốc rễ). Ví dụ: Sai $\rightarrow$ Lấy thiếu $\rightarrow$ Index chậm $\rightarrow$ Data pipeline lỗi.
- **Failure Clustering:** Gom nhóm các lỗi theo root cause. Sửa 1 root cause (vd: indexing) có thể giải quyết hàng loạt lỗi.
- **Continuous Improvement Loop:** Evaluate $\rightarrow$ Analyze $\rightarrow$ Improve $\rightarrow$ Augment (thêm vào benchmark) $\rightarrow$ Evaluate.

## 10. Tích hợp Observability
Đánh giá (Eval) và Giám sát (Observability) đi đôi với nhau:
- **Observability (Day 13):** Cái gì đang xảy ra trên production lúc này?
- **Evaluation (Day 14):** Chất lượng của cái đang xảy ra là bao nhiêu?
- Luồng thực tế: Log (Langfuse) $\rightarrow$ Sample 1% $\rightarrow$ Chạy RAGAS tự động $\rightarrow$ Nếu điểm kém $\rightarrow$ Cảnh báo & Human review.
