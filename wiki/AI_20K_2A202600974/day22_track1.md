---
type: summary
title: "Day 22 – Track 1: AI Evals & Automated Evaluators"
description: "Hướng dẫn chi tiết về tự động hóa đánh giá AI (Automated Evals) và tham chiếu đánh giá AI từ góc nhìn Product Management."
tags: [ai, 20k, day22, track1, evaluation, llm-as-judge, code-evals]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/1-d22-slide.pdf", "raw/AI_20K_2A202600974/22/ai-evals-reference-guide-vi.pdf"]
---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]

# Day 22 – Track 1: AI Evals & Automated Evaluators

Đánh giá ứng dụng AI (Application Evaluation) không chỉ dừng lại ở đo usage hay funnel completion, mà là đảm bảo chất lượng, tính an toàn và khả năng suy luận của hệ thống ở quy mô lớn. 

---

## 1. Tư duy nền tảng: Tại sao cần Automated Evals?

- **Vấn đề Scale:** Manual review không thể mở rộng. Khi lượng production traces lên tới 100k+, review thủ công sẽ chậm release và bỏ sót lỗi âm thầm (false confidence).
- **Application Eval vs Model Eval:** Model Eval (do provider thực hiện qua MMLU, HumanEval) đo năng lực nền. Application Eval đo lường *riêng cho product context* (Ví dụ: Support Triage có đúng intent và policy của doanh nghiệp không?).
- **AI Flywheel:** Quy trình cải tiến liên tục dựa trên vết tích (traces): `Traces -> Trace analysis -> Reference dataset -> Offline evals -> Release gates -> Online monitoring`.

---

## 2. Các tầng Đánh giá: Codebase, Human & LLM

Một hệ thống eval vững chắc (Eval Suite) cần phối hợp ba nguồn đánh giá, sắp xếp theo cây quyết định ưu tiên:

### Lớp 1: Code-based Evals (Luôn bật, Ưu tiên số 1)
- **Khi nào dùng:** Khi câu hỏi xác minh được bằng rule, DB, schema, API, regex, tính toán.
- **Ưu điểm:** Nhanh, rẻ, deterministic, dễ đưa vào CI/CD (critical path).
- **Ví dụ check:** JSON Schema đúng chuẩn (Pydantic), Assert enum category (`Technical`, `Billing`), Regex không lộ token/UUID, Tool usage đủ required fields.
- **Cấu trúc 1 Code-eval:** 
  1. Input (output string, tool calls).
  2. Logic (condition, pattern match).
  3. Result & Reason (Trả về fail rõ ràng kèm thông tin: "Missing subject line").

### Lớp 2: LLM-as-Judge (Cần Calibration)
- **Khi nào dùng:** Khi tiêu chí phụ thuộc ngữ cảnh, sắc thái ngôn ngữ (ví dụ: giải thích hợp lý không, agent có đồng cảm với khách hàng không, intent classification).
- **Calibration (Hiệu chỉnh) là cốt lõi:** LLM judge có rủi ro dễ dãi hoặc thiên vị (bias). Cần calibrate:
  1. Human expert label trên 50-100 cases (golden labels).
  2. Chạy LLM Judge và compare kết quả (đo Precision/Recall của failure modes, không chỉ đo raw agreement).
  3. Sửa judge prompt theo pattern sai biệt và lặp lại.
- Khi LLM judge "chạm trần" (domain khó, model không đủ nền tảng), cần chuyển fallback.

### Lớp 3: Human Review (Fallback & Định nghĩa "Good")
- **Khi nào dùng:** Giai đoạn prototype chưa rõ rubric, high-stakes domain (y tế, tài chính), policy nuance phức tạp, hoặc làm nhãn calibration.
- **Cách review hiệu quả:** Không random hoàn toàn, phải *sample có chủ đích* (ví dụ: output được LLM judge tự tin cao nhất/thấp nhất, case disagreement).

---

## 3. Kiến trúc Dataset và Metrics

### Reference Dataset
Không chỉ là tập prompt, một Eval Case tốt phải bao gồm:
- **Input:** Câu hỏi/Context user.
- **Expected Output:** Golden label/Rubric rõ ràng.
- **Assertions:** Các rule codebase bắt buộc.
- **Failure modes & Severity:** Phân tích nếu fail thì rủi ro ở mức độ nào (P0, P1, v.v.).

### Metrics
- **Agent Success Rate:** North Star Metric. Là một composite metric tổng hợp từ: Task correctness, Schema pass rate, Escalation recall, Human/LLM judge score.
- Cần phân mảng (segment) metrics theo *Intent, Persona, Prompt version, Model version* để phát hiện regression ẩn.

---

## 4. Eval Lifecycle (Quy trình đưa AI ra Production)
1. **Vibe Check (Prototype):** 10-30 cases đa dạng. Định nghĩa "good", tìm failure modes.
2. **Offline Evals (Build/Iterate):** 100-1000 cases chạy tự động trước release. Đóng vai trò là Release Gate chặn lỗi.
3. **Online Monitoring (Production):** Theo dõi drift, P95 latency, cost, user feedback. Sample các case nghi ngờ (low-confidence) đưa về làm dataset vòng tiếp.

---

## Liên kết
- [[day21_track1]] – AI Evals (Day 21)
- [[day24_track3]] – RAGAS & Guardrails (đánh giá RAG cụ thể)
- [[day22_overview]]
