---
type: summary
title: "Day 22 – Track 1: AI Evals & Automated Evaluators"
description: "Hướng dẫn chi tiết về tự động hóa đánh giá AI (Automated Evals) và tham chiếu đánh giá AI từ góc nhìn Product Management."
tags: [ai, 20k, day22, track1, evaluation, llm-as-judge, code-evals]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/1-d22-slide.pdf", "raw/AI_20K_2A202600974/22/ai-evals-reference-guide-vi.pdf"]
---
Dưới đây là nội dung file `day22_track1.md` đã được hoàn thiện song ngữ (Anh – Việt), giữ nguyên định dạng Markdown và cấu trúc ban đầu. Những phần còn thiếu tiếng Việt (heading "Reference Dataset" và "Metrics") đã được bổ sung. Mỗi đoạn đều có cả hai ngôn ngữ, tiếng Anh trước, tiếng Việt in nghiêng bên dưới (hoặc giữ nguyên thứ tự như file gốc nếu đã có).

---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]
> **Roadmap:** [[track1_ba|Track 1: AI Product / BA]]

# Day 22 – Track 1: AI Evals & Automated Evaluators

*Ngày 22 – Track 1: Đánh giá AI & Bộ đánh giá tự động*

Đánh giá ứng dụng AI (Application Evaluation) không chỉ dừng lại ở đo usage hay funnel completion, mà là đảm bảo chất lượng, tính an toàn và khả năng suy luận của hệ thống ở quy mô lớn. 

*Evaluating AI applications goes beyond measuring usage or funnel completion; it is about ensuring quality, safety, and reasoning capability of the system at scale.*

---

## 1. Tư duy nền tảng: Tại sao cần Automated Evals?

## 1. Foundational Mindset: Why Automated Evals?

*1. Tư duy nền tảng: Tại sao cần Automated Evals?*

- **Vấn đề Scale:** Manual review không thể mở rộng. Khi lượng production traces lên tới 100k+, review thủ công sẽ chậm release và bỏ sót lỗi âm thầm (false confidence).
- **Application Eval vs Model Eval:** Model Eval (do provider thực hiện qua MMLU, HumanEval) đo năng lực nền. Application Eval đo lường *riêng cho product context* (Ví dụ: Support Triage có đúng intent và policy của doanh nghiệp không?).
- **AI Flywheel:** Quy trình cải tiến liên tục dựa trên vết tích (traces): `Traces -> Trace analysis -> Reference dataset -> Offline evals -> Release gates -> Online monitoring`.

- **The Scale Problem:** Manual review cannot scale. When production traces reach 100k+, manual review slows releases and misses silent errors (false confidence).
- **Application Eval vs Model Eval:** Model Eval (performed by providers via MMLU, HumanEval) measures foundational capability. Application Eval measures specifically for the product context (e.g., Does support triage match the business's intent and policy?).
- **AI Flywheel:** A continuous improvement process based on traces: `Traces -> Trace analysis -> Reference dataset -> Offline evals -> Release gates -> Online monitoring`.

---

## 2. Các tầng Đánh giá: Codebase, Human & LLM

## 2. Evaluation Layers: Codebase, Human & LLM

*2. Các tầng Đánh giá: Codebase, Human & LLM*

Một hệ thống eval vững chắc (Eval Suite) cần phối hợp ba nguồn đánh giá, sắp xếp theo cây quyết định ưu tiên:

*A robust eval suite must coordinate three evaluation sources, arranged in a priority decision tree:*

### Lớp 1: Code-based Evals (Luôn bật, Ưu tiên số 1)
### Layer 1: Code-based Evals (Always On, Priority #1)

*Lớp 1: Code-based Evals (Luôn bật, Ưu tiên số 1)*

- **Khi nào dùng:** Khi câu hỏi xác minh được bằng rule, DB, schema, API, regex, tính toán.
- **Ưu điểm:** Nhanh, rẻ, deterministic, dễ đưa vào CI/CD (critical path).
- **Ví dụ check:** JSON Schema đúng chuẩn (Pydantic), Assert enum category (`Technical`, `Billing`), Regex không lộ token/UUID, Tool usage đủ required fields.
- **Cấu trúc 1 Code-eval:** 
  1. Input (output string, tool calls).
  2. Logic (condition, pattern match).
  3. Result & Reason (Trả về fail rõ ràng kèm thông tin: "Missing subject line").

- **When to use:** When the question can be verified by rule, DB, schema, API, regex, computation.
- **Advantages:** Fast, cheap, deterministic, easy to integrate into CI/CD (critical path).
- **Example checks:** Valid JSON Schema (Pydantic), Assert enum category (`Technical`, `Billing`), Regex no token/UUID leakage, Tool usage has all required fields.
- **Structure of a Code-eval:** 
  1. Input (output string, tool calls).
  2. Logic (condition, pattern match).
  3. Result & Reason (Return clear failure with info: "Missing subject line").

### Lớp 2: LLM-as-Judge (Cần Calibration)
### Layer 2: LLM-as-Judge (Requires Calibration)

*Lớp 2: LLM-as-Judge (Cần Calibration)*

- **Khi nào dùng:** Khi tiêu chí phụ thuộc ngữ cảnh, sắc thái ngôn ngữ (ví dụ: giải thích hợp lý không, agent có đồng cảm với khách hàng không, intent classification).
- **Calibration (Hiệu chỉnh) là cốt lõi:** LLM judge có rủi ro dễ dãi hoặc thiên vị (bias). Cần calibrate:
  1. Human expert label trên 50-100 cases (golden labels).
  2. Chạy LLM Judge và compare kết quả (đo Precision/Recall của failure modes, không chỉ đo raw agreement).
  3. Sửa judge prompt theo pattern sai biệt và lặp lại.
- Khi LLM judge "chạm trần" (domain khó, model không đủ nền tảng), cần chuyển fallback.

- **When to use:** When criteria depend on context, language nuance (e.g., is the explanation reasonable, does the agent show empathy to the customer, intent classification).
- **Calibration is core:** LLM judge risks leniency or bias. Requires calibration:
  1. Human expert labels on 50-100 cases (golden labels).
  2. Run LLM Judge and compare results (measure Precision/Recall on failure modes, not just raw agreement).
  3. Revise judge prompt based on error patterns and repeat.
- When the LLM judge "hits a ceiling" (difficult domain, insufficient model capability), fallback to other methods.

### Lớp 3: Human Review (Fallback & Định nghĩa "Good")
### Layer 3: Human Review (Fallback & Defining "Good")

*Lớp 3: Human Review (Fallback & Định nghĩa "Good")*

- **Khi nào dùng:** Giai đoạn prototype chưa rõ rubric, high-stakes domain (y tế, tài chính), policy nuance phức tạp, hoặc làm nhãn calibration.
- **Cách review hiệu quả:** Không random hoàn toàn, phải *sample có chủ đích* (ví dụ: output được LLM judge tự tin cao nhất/thấp nhất, case disagreement).

- **When to use:** During prototype phase with unclear rubric, high-stakes domains (medical, financial), complex policy nuance, or for calibration labeling.
- **Effective review method:** Not purely random; must use *targeted sampling* (e.g., outputs where LLM judge is most/least confident, disagreement cases).

---

## 3. Kiến trúc Dataset và Metrics

## 3. Dataset Architecture and Metrics

*3. Kiến trúc Dataset và Metrics*

### Reference Dataset
### Bộ dữ liệu tham chiếu
*Reference Dataset*
*Bộ dữ liệu tham chiếu*

Không chỉ là tập prompt, một Eval Case tốt phải bao gồm:
- **Input:** Câu hỏi/Context user.
- **Expected Output:** Golden label/Rubric rõ ràng.
- **Assertions:** Các rule codebase bắt buộc.
- **Failure modes & Severity:** Phân tích nếu fail thì rủi ro ở mức độ nào (P0, P1, v.v.).

*A good Eval Case is not just a set of prompts; it must include:*
- **Input:** User question/context.
- **Expected Output:** Clear golden label/rubric.
- **Assertions:** Mandatory codebase rules.
- **Failure modes & Severity:** Analysis of risk level if failure occurs (P0, P1, etc.).

### Metrics
### Chỉ số đánh giá
*Metrics*
*Chỉ số đánh giá*

- **Agent Success Rate:** North Star Metric. Là một composite metric tổng hợp từ: Task correctness, Schema pass rate, Escalation recall, Human/LLM judge score.
- Cần phân mảng (segment) metrics theo *Intent, Persona, Prompt version, Model version* để phát hiện regression ẩn.

- **Agent Success Rate:** North Star Metric. A composite metric aggregating: Task correctness, Schema pass rate, Escalation recall, Human/LLM judge score.
- Metrics must be segmented by *Intent, Persona, Prompt version, Model version* to detect hidden regressions.

---

## 4. Eval Lifecycle (Quy trình đưa AI ra Production)
## 4. Eval Lifecycle (Process for Shipping AI to Production)

*4. Eval Lifecycle (Quy trình đưa AI ra Production)*

1. **Vibe Check (Prototype):** 10-30 cases đa dạng. Định nghĩa "good", tìm failure modes.
2. **Offline Evals (Build/Iterate):** 100-1000 cases chạy tự động trước release. Đóng vai trò là Release Gate chặn lỗi.
3. **Online Monitoring (Production):** Theo dõi drift, P95 latency, cost, user feedback. Sample các case nghi ngờ (low-confidence) đưa về làm dataset vòng tiếp.

1. **Vibe Check (Prototype):** 10-30 diverse cases. Define "good", find failure modes.
2. **Offline Evals (Build/Iterate):** 100-1000 cases run automatically before release. Acts as a Release Gate to catch errors.
3. **Online Monitoring (Production):** Monitor drift, P95 latency, cost, user feedback. Sample suspicious cases (low-confidence) to feed into the next iteration dataset.

---

## Liên kết
## Links

*Liên kết*

- [[day21_track1]] – AI Evals (Day 21)
- [[day24_track3]] – RAGAS & Guardrails (đánh giá RAG cụ thể)
- [[day22_overview]]

- [[day21_track1]] – AI Evals (Day 21)
- [[day24_track3]] – RAGAS & Guardrails (specific RAG evaluation)
- [[day22_overview]]

--- 

File đã được hoàn thiện song ngữ. Mọi thay đổi chỉ bổ sung những phần còn thiếu (heading và in nghiêng cho "Reference Dataset" và "Metrics") mà không làm thay đổi cấu trúc gốc.
