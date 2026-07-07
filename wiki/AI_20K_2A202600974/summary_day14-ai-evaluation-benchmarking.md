---
type: summary
title: "Summary of day14-ai-evaluation-benchmarking"
description: "Tổng hợp kiến thức Ngày 14 về đo lường chất lượng AI một cách khoa học, các phương pháp đánh giá, metrics, RAGAS framework, LLM-as-Judge và phân tích lỗi."
tags: [ai, 20k, day14]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/14/day14-ai-evaluation-benchmarking.pdf"]
---

# Đo lường chất lượng AI một cách khoa học (AI Evaluation & Benchmarking)
# Measuring AI Quality Scientifically (AI Evaluation & Benchmarking)

Bài học nhấn mạnh việc đánh giá AI (Evaluation) là một quy trình kỹ thuật (engineering discipline) khoa học, chứ không phải dựa trên cảm tính ("cảm thấy agent trả lời tốt"). Không đo lường được = không cải thiện được.
The lesson emphasizes that AI Evaluation is a scientific engineering discipline, not based on feeling ("feeling the agent answers well"). If you can't measure it = you can't improve it.

## 1. 4 Chiều Chất Lượng Output của AI
## 1. 4 Dimensions of AI Output Quality

Một AI Agent cần được đánh giá dựa trên 4 khía cạnh chính, bởi 1 metric đơn lẻ là không đủ:
An AI Agent needs to be evaluated based on 4 main aspects, because a single metric is not enough:
- **Correctness (Tính chính xác):** Trả lời đúng sự thật không? Có bịa đặt (hallucinate) hay trích dẫn sai nguồn không?
- **Correctness:** Does it answer truthfully? Does it hallucinate or cite the wrong sources?
- **Relevance (Tính liên quan):** Trả lời đúng trọng tâm câu hỏi của user hay lạc đề?
- **Relevance:** Does it answer the core of the user's question or go off-topic?
- **Completeness (Tính đầy đủ):** Có đủ chi tiết cần thiết không? Có bỏ sót thông tin quan trọng nào không?
- **Completeness:** Does it have enough necessary details? Does it miss any important information?
- **Coherence (Tính mạch lạc):** Câu trả lời có dễ đọc, cấu trúc tốt và ngôn ngữ phù hợp không?
- **Coherence:** Is the answer easy to read, well-structured, and does it use appropriate language?

## 2. 3 Loại Đánh Giá (Evaluation Types)
## 2. 3 Types of Evaluation (Evaluation Types)

1. **Offline (Batch test trên golden dataset):** Chạy tự động mỗi khi có thay đổi code/prompt/model để tránh regression. (Dùng RAGAS, scripts).
1. **Offline (Batch test on golden dataset):** Run automatically whenever there is a code/prompt/model change to prevent regression. (Using RAGAS, scripts).
2. **Online (Monitor production traffic):** Theo dõi liên tục trên real traffic để phát hiện suy giảm chất lượng (degradation) ngay lập tức. (Dùng Langfuse, LangSmith).
2. **Online (Monitor production traffic):** Continuously monitor real traffic to detect quality degradation immediately. (Using Langfuse, LangSmith).
3. **Human Eval (Expert review):** Đánh giá bởi con người trên các sample định kỳ hoặc các tác vụ rủi ro cao (high-stakes).
3. **Human Eval (Expert review):** Evaluated by humans on periodic samples or high-stakes tasks.

> [!TIP]
> **Quy tắc chi phí:** Chi phí cho evaluation phải rẻ hơn hậu quả của bug trên production khoảng 1000 lần. Agent không pass eval offline thì không được deploy.
> **Cost rule:** The cost for evaluation must be about 1000 times cheaper than the consequence of a bug in production. If the Agent doesn't pass offline eval, it must not be deployed.

## 3. Các Nhóm Metrics Đánh Giá
## 3. Groups of Evaluation Metrics

Không phải mọi metric đều như nhau. Cần chọn metrics gắn với use case và mục tiêu kinh doanh (business outcome).
Not all metrics are equal. It is necessary to choose metrics tied to the use case and business outcome.

### 3.1. Task Completion & Answer Quality
### 3.1. Task Completion & Answer Quality
- **Task Completion:** Đánh giá nhị phân (Pass/Fail), Partial credit (theo % số subtasks hoàn thành), Weighted scoring, hoặc Trajectory eval (đánh giá cả quá trình).
- **Task Completion:** Binary evaluation (Pass/Fail), Partial credit (by % of completed subtasks), Weighted scoring, or Trajectory eval (evaluating the entire process).
- **Answer Quality (Accuracy):** 
- **Answer Quality (Accuracy):** 
  - *Exact match / F1 token:* Tốt cho câu trả lời ngắn, factual.
  - *Exact match / F1 token:* Good for short, factual answers.
  - *BERTScore / Embedding cosine:* Tốt cho so sánh ngữ nghĩa.
  - *BERTScore / Embedding cosine:* Good for semantic comparison.
  - *LLM Judge / Human:* Tốt cho nội dung phức tạp, subjective.
  - *LLM Judge / Human:* Good for complex, subjective content.

### 3.2. Business Metrics & North Star
### 3.2. Business Metrics & North Star
Cần định nghĩa một khung 3 lớp:
Need to define a 3-layer framework:
1. **North Star Metric:** Chỉ số cốt lõi về business value (vd: Tỷ lệ tự giải quyết - Resolution rate).
1. **North Star Metric:** The core metric of business value (e.g., Resolution rate).
2. **Guardrail metrics:** Các chỉ số không được phép suy giảm (vd: P95 latency $\le$ 5s, Faithfulness $\ge$ 0.8).
2. **Guardrail metrics:** Metrics that are not allowed to degrade (e.g., P95 latency $\le$ 5s, Faithfulness $\ge$ 0.8).
3. **Diagnostic metrics:** Dùng khi có sự cố để chẩn đoán (vd: Các điểm số RAGAS).
3. **Diagnostic metrics:** Used when an incident occurs for diagnosis (e.g., RAGAS scores).

## 4. RAGAS Framework
## 4. RAGAS Framework

RAGAS (Retrieval Augmented Generation Assessment) là bộ khung chuẩn để đánh giá chất lượng RAG pipeline. Gồm 4 metrics (chấm điểm từ 0-1):
RAGAS (Retrieval Augmented Generation Assessment) is the standard framework for evaluating the quality of a RAG pipeline. It consists of 4 metrics (scored from 0-1):

- **Faithfulness:** Câu trả lời có bám sát ngữ cảnh (context) lấy ra không? (Thấp = Bịa đặt/Hallucination).
- **Faithfulness:** Does the answer closely follow the retrieved context? (Low = Hallucination).
- **Context Recall:** Retriever có lấy đủ thông tin cần thiết từ ground truth không? (Thấp = Retrieve thiếu tài liệu).
- **Context Recall:** Did the Retriever fetch enough necessary information from the ground truth? (Low = Retrieved missing documents).
- **Context Precision:** Context lấy ra có chứa nhiều thông tin thực sự liên quan không? (Thấp = Retrieve nhiều nhưng bị rác/noise).
- **Context Precision:** Does the retrieved context contain a lot of genuinely relevant information? (Low = Retrieved a lot but with noise/garbage).
- **Answer Relevancy:** Câu trả lời có đúng với câu hỏi của user không? (Thấp = Lạc đề).
- **Answer Relevancy:** Is the answer relevant to the user's question? (Low = Off-topic).

**Diagnostic Flowchart khi score thấp:**
**Diagnostic Flowchart when the score is low:**
`Context Recall` (Tăng top-k, chunk nhỏ) $\rightarrow$ `Context Precision` (Thêm re-ranking) $\rightarrow$ `Faithfulness` (Ép prompt chỉ dùng context) $\rightarrow$ `Answer Relevancy` (Cải thiện template câu trả lời).
`Context Recall` (Increase top-k, smaller chunks) $\rightarrow$ `Context Precision` (Add re-ranking) $\rightarrow$ `Faithfulness` (Force prompt to only use context) $\rightarrow$ `Answer Relevancy` (Improve answer template).

## 5. Thiết Kế Benchmark (Benchmark Design)
## 5. Benchmark Design

*Garbage in, garbage out.* Đánh giá phụ thuộc rất lớn vào chất lượng Benchmark.
*Garbage in, garbage out.* Evaluation relies heavily on the quality of the Benchmark.

- **Golden Dataset:** Bộ dữ liệu chuẩn (thường 50-100 QA pairs cho production, 20 cho sanity check) kèm câu trả lời mẫu của chuyên gia (expected answers).
- **Golden Dataset:** A standard dataset (usually 50-100 QA pairs for production, 20 for sanity check) along with expert sample answers (expected answers).
- **Cách tạo:**
- **How to create:**
  1. *Expert-written:* High-stakes, chất lượng cao nhưng tốn kém.
  1. *Expert-written:* High-stakes, high quality but expensive.
  2. *From production log:* Thực tế, chi phí nhãn vừa phải.
  2. *From production log:* Realistic, moderate labeling cost.
  3. *LLM-generated:* Nhanh, scale tốt, boot-strap ban đầu (luôn cần Human review).
  3. *LLM-generated:* Fast, scales well, initial boot-strap (always requires Human review).
- **Stratified Sampling:** Lấy mẫu có phân lớp (theo category, difficulty) để đảm bảo không bị bias vào một nhóm câu hỏi phổ biến.
- **Stratified Sampling:** Taking stratified samples (by category, difficulty) to ensure there is no bias towards a common group of questions.
- **Edge Cases & Adversarial Inputs:** Cần test khoảng $\ge$ 10% các trường hợp lách luật: Prompt injection, PII extraction, Jailbreak, Typos, Mixed language.
- **Edge Cases & Adversarial Inputs:** Need to test about $\ge$ 10% of bypass cases: Prompt injection, PII extraction, Jailbreak, Typos, Mixed language.
- **Data Contamination:** Tránh việc LLM đã học qua test data bằng cách giấu kín benchmark hoặc thay đổi thường xuyên.
- **Data Contamination:** Avoid the LLM having learned the test data by keeping the benchmark secret or changing it frequently.

## 6. LLM-as-Judge
## 6. LLM-as-Judge

Sử dụng LLM để chấm điểm tự động các câu trả lời dựa trên rubric rõ ràng, giúp mở rộng quy mô đánh giá mà human eval không làm được.
Using an LLM to automatically score answers based on a clear rubric helps scale up the evaluation that human eval cannot do.

- **Rubric:** Cần tiêu chí rõ ràng (thang 1-5) kèm ví dụ. Có thể dùng *Reference-based* (có câu trả lời chuẩn để so) hoặc *Reference-free* (chấm độc lập theo độ dài, phong cách...).
- **Rubric:** Needs clear criteria (scale 1-5) with examples. Can use *Reference-based* (having a standard answer to compare against) or *Reference-free* (scoring independently by length, style...).
- **Pairwise vs Pointwise:** Pairwise (A vs B) dễ chấm và ít bias hơn, tốt cho A/B testing prompt. Pointwise (điểm tuyệt đối) tiện cho track qua thời gian.
- **Pairwise vs Pointwise:** Pairwise (A vs B) is easier to score and has less bias, good for A/B testing prompts. Pointwise (absolute score) is convenient for tracking over time.
- **Chain-of-Thought (CoT):** Yêu cầu LLM Judge phân tích từng bước trước khi cho điểm sẽ giúp tăng độ đồng thuận với chuyên gia lên 15-20%.
- **Chain-of-Thought (CoT):** Requiring the LLM Judge to analyze step-by-step before scoring will help increase agreement with experts by 15-20%.
- **7 Biases của LLM Judge:** Position bias (thiên vị vị trí), Verbosity bias (thích câu dài), Self-preference (GPT thích GPT), Sycophancy (nịnh user), Authority, Format, Recency.
- **7 Biases of LLM Judge:** Position bias, Verbosity bias (likes long sentences), Self-preference (GPT likes GPT), Sycophancy (flattering the user), Authority, Format, Recency.
- **Calibration (Hiệu chuẩn):** Luôn so sánh điểm LLM với Human trên subset $\ge$ 50 samples. Đạt Cohen's Kappa $\kappa \ge 0.6$ hoặc Spearman $\rho \ge 0.7$ mới nên dùng judge đó.
- **Calibration:** Always compare LLM scores with Human scores on a subset $\ge$ 50 samples. Achieving a Cohen's Kappa $\kappa \ge 0.6$ or Spearman $\rho \ge 0.7$ is required before using that judge.

## 7. Tính Chặt Chẽ Thống Kê (Statistical Rigor)
## 7. Statistical Rigor

LLM có tính ngẫu nhiên (nhiệt độ $>0$), do đó không thể kết luận dựa trên 1 lần chạy hay con số đơn lẻ.
LLMs have randomness (temperature $>0$), therefore conclusions cannot be made based on a single run or a single number.

- **Confidence Interval (CI - Khoảng tin cậy):** Chạy ít nhất 3 lần, báo cáo Mean $\pm$ Standard Deviation.
- **Confidence Interval (CI):** Run at least 3 times, report Mean $\pm$ Standard Deviation.
- **Significance Test:** Dùng Paired t-test để xem Agent V2 có thực sự tốt hơn V1 không (p-value $< 0.05$).
- **Significance Test:** Use Paired t-test to see if Agent V2 is truly better than V1 (p-value $< 0.05$).
- **Power Analysis:** Để phát hiện khác biệt nhỏ (vd 0.05 điểm), cần khoảng $\ge$ 30-50 cases cho benchmark. 20 cases ở môi trường Lab chỉ là sanity check.
- **Power Analysis:** To detect a small difference (e.g., 0.05 points), you need about $\ge$ 30-50 cases for the benchmark. 20 cases in a Lab environment is just a sanity check.

## 8. Đánh Giá Safety và Agentic Behavior
## 8. Evaluating Safety and Agentic Behavior

Đối với Agent có dùng Tools (Công cụ) và thực hiện nhiều bước (Multi-step):
For Agents that use Tools and perform Multi-step processes:
- **Trajectory Evaluation:** Đánh giá cả quá trình (Step correctness, Efficiency) thay vì chỉ kết quả cuối cùng. Agent có thể ra kết quả đúng nhưng đi vòng vèo, lãng phí tài nguyên.
- **Trajectory Evaluation:** Evaluating the whole process (Step correctness, Efficiency) instead of just the final result. The Agent might output the correct result but take a convoluted path, wasting resources.
- **Safety Eval:** Test Jailbreak (từ chối $\ge$ 95%), PII leakage (0% rò rỉ), Toxicity (0%), Financial/Medical advice (từ chối).
- **Safety Eval:** Test Jailbreak (refuse $\ge$ 95%), PII leakage (0% leak), Toxicity (0%), Financial/Medical advice (refuse).
- **Bias & Fairness:** Kiểm tra độ công bằng giữa các nhóm giới tính, ngôn ngữ thiểu số, độ tuổi.
- **Bias & Fairness:** Check fairness among gender groups, minority languages, ages.
- **Red Team:** Thuê chuyên gia cố tình bẻ khóa hệ thống trong thời gian giới hạn để phát hiện lỗ hổng trước major release.
- **Red Team:** Hire experts to intentionally break the system within a limited time to detect vulnerabilities before a major release.

## 9. Phân Tích Lỗi (Failure Analysis & Continuous Improvement)
## 9. Failure Analysis & Continuous Improvement

Điểm số chỉ cho biết vấn đề, Failure Analysis mới chỉ ra cách sửa.
Scores only indicate the problem; Failure Analysis actually points out how to fix it.
- **Phân loại lỗi:** Wrong answer, Hallucination, Tool failure, Refusal, Slow, Inconsistent...
- **Error classification:** Wrong answer, Hallucination, Tool failure, Refusal, Slow, Inconsistent...
- **5 Whys:** Đặt câu hỏi "Tại sao" 5 lần để tìm *Root Cause* (Nguyên nhân gốc rễ). Ví dụ: Sai $\rightarrow$ Lấy thiếu $\rightarrow$ Index chậm $\rightarrow$ Data pipeline lỗi.
- **5 Whys:** Ask "Why" 5 times to find the *Root Cause*. Example: Wrong $\rightarrow$ Retrieved missing $\rightarrow$ Slow Index $\rightarrow$ Data pipeline error.
- **Failure Clustering:** Gom nhóm các lỗi theo root cause. Sửa 1 root cause (vd: indexing) có thể giải quyết hàng loạt lỗi.
- **Failure Clustering:** Group errors by root cause. Fixing 1 root cause (e.g., indexing) can solve a series of errors.
- **Continuous Improvement Loop:** Evaluate $\rightarrow$ Analyze $\rightarrow$ Improve $\rightarrow$ Augment (thêm vào benchmark) $\rightarrow$ Evaluate.
- **Continuous Improvement Loop:** Evaluate $\rightarrow$ Analyze $\rightarrow$ Improve $\rightarrow$ Augment (add to benchmark) $\rightarrow$ Evaluate.

## 10. Tích hợp Observability
## 10. Integrating Observability
Đánh giá (Eval) và Giám sát (Observability) đi đôi với nhau:
Evaluation (Eval) and Monitoring (Observability) go hand in hand:
- **Observability (Day 13):** Cái gì đang xảy ra trên production lúc này?
- **Observability (Day 13):** What is happening in production right now?
- **Evaluation (Day 14):** Chất lượng của cái đang xảy ra là bao nhiêu?
- **Evaluation (Day 14):** What is the quality of what is happening?
- Luồng thực tế: Log (Langfuse) $\rightarrow$ Sample 1% $\rightarrow$ Chạy RAGAS tự động $\rightarrow$ Nếu điểm kém $\rightarrow$ Cảnh báo & Human review.
- Practical flow: Log (Langfuse) $\rightarrow$ Sample 1% $\rightarrow$ Run RAGAS automatically $\rightarrow$ If score is poor $\rightarrow$ Alert & Human review.
