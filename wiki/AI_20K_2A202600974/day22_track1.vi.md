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


Ngày 22 – Track 1: Đánh giá AI & Bộ đánh giá tự động

Đánh giá ứng dụng AI (Application Evaluation) không chỉ dừng lại ở đo usage hay funnel completion, mà là đảm bảo chất lượng, tính an toàn và khả năng suy luận của hệ thống ở quy mô lớn. 


---

## 1. Tư duy nền tảng: Tại sao cần Automated Evals?


1. Tư duy nền tảng: Tại sao cần Automated Evals?

- **Vấn đề Scale:** Manual review không thể mở rộng. Khi lượng production traces lên tới 100k+, review thủ công sẽ chậm release và bỏ sót lỗi âm thầm (false confidence).
- **Application Eval vs Model Eval:** Model Eval (do provider thực hiện qua MMLU, HumanEval) đo năng lực nền. Application Eval đo lường *riêng cho product context* (Ví dụ: Support Triage có đúng intent và policy của doanh nghiệp không?).
- **AI Flywheel:** Quy trình cải tiến liên tục dựa trên vết tích (traces): `Traces -> Trace analysis -> Reference dataset -> Offline evals -> Release gates -> Online monitoring`.


---

## 2. Các tầng Đánh giá: Codebase, Human & LLM


2. Các tầng Đánh giá: Codebase, Human & LLM

Một hệ thống eval vững chắc (Eval Suite) cần phối hợp ba nguồn đánh giá, sắp xếp theo cây quyết định ưu tiên:


### Lớp 1: Code-based Evals (Luôn bật, Ưu tiên số 1)

Lớp 1: Code-based Evals (Luôn bật, Ưu tiên số 1)

- **Khi nào dùng:** Khi câu hỏi xác minh được bằng rule, DB, schema, API, regex, tính toán.
- **Ưu điểm:** Nhanh, rẻ, deterministic, dễ đưa vào CI/CD (critical path).
- **Ví dụ check:** JSON Schema đúng chuẩn (Pydantic), Assert enum category (`Technical`, `Billing`), Regex không lộ token/UUID, Tool usage đủ required fields.
- **Cấu trúc 1 Code-eval:** 
  3. Result & Reason (Trả về fail rõ ràng kèm thông tin: "Missing subject line").


### Lớp 2: LLM-as-Judge (Cần Calibration)

Lớp 2: LLM-as-Judge (Cần Calibration)

- **Khi nào dùng:** Khi tiêu chí phụ thuộc ngữ cảnh, sắc thái ngôn ngữ (ví dụ: giải thích hợp lý không, agent có đồng cảm với khách hàng không, intent classification).
- **Calibration (Hiệu chỉnh) là cốt lõi:** LLM judge có rủi ro dễ dãi hoặc thiên vị (bias). Cần calibrate:
  1. Human expert label trên 50-100 cases (golden labels).
  2. Chạy LLM Judge và compare kết quả (đo Precision/Recall của failure modes, không chỉ đo raw agreement).
  3. Sửa judge prompt theo pattern sai biệt và lặp lại.
- Khi LLM judge "chạm trần" (domain khó, model không đủ nền tảng), cần chuyển fallback.


### Lớp 3: Human Review (Fallback & Định nghĩa "Good")

Lớp 3: Human Review (Fallback & Định nghĩa "Good")

- **Khi nào dùng:** Giai đoạn prototype chưa rõ rubric, high-stakes domain (y tế, tài chính), policy nuance phức tạp, hoặc làm nhãn calibration.
- **Cách review hiệu quả:** Không random hoàn toàn, phải *sample có chủ đích* (ví dụ: output được LLM judge tự tin cao nhất/thấp nhất, case disagreement).


---

## 3. Kiến trúc Dataset và Metrics


3. Kiến trúc Dataset và Metrics

### Bộ dữ liệu tham chiếu
Bộ dữ liệu tham chiếu

Không chỉ là tập prompt, một Eval Case tốt phải bao gồm:
- **Input:** Câu hỏi/Context user.
- **Expected Output:** Golden label/Rubric rõ ràng.
- **Assertions:** Các rule codebase bắt buộc.
- **Failure modes & Severity:** Phân tích nếu fail thì rủi ro ở mức độ nào (P0, P1, v.v.).


### Chỉ số đánh giá
Chỉ số đánh giá

- **Agent Success Rate:** North Star Metric. Là một composite metric tổng hợp từ: Task correctness, Schema pass rate, Escalation recall, Human/LLM judge score.
- Cần phân mảng (segment) metrics theo *Intent, Persona, Prompt version, Model version* để phát hiện regression ẩn.


---

## 4. Eval Lifecycle (Quy trình đưa AI ra Production)

4. Eval Lifecycle (Quy trình đưa AI ra Production)

1. **Vibe Check (Prototype):** 10-30 cases đa dạng. Định nghĩa "good", tìm failure modes.
2. **Offline Evals (Build/Iterate):** 100-1000 cases chạy tự động trước release. Đóng vai trò là Release Gate chặn lỗi.
3. **Online Monitoring (Production):** Theo dõi drift, P95 latency, cost, user feedback. Sample các case nghi ngờ (low-confidence) đưa về làm dataset vòng tiếp.


---

## Liên kết

Liên kết

- [[day24_track3]] – RAGAS & Guardrails (đánh giá RAG cụ thể)


--- 

File đã được hoàn thiện song ngữ. Mọi thay đổi chỉ bổ sung những phần còn thiếu (heading và in nghiêng cho "Reference Dataset" và "Metrics") mà không làm thay đổi cấu trúc gốc.

---

### *Câu hỏi ôn tập Ngày 22*

   Tại sao cần Automated Evals thay vì Manual Review?
     A. Manual review luôn chính xác hơn
     B. Automated evals không thể scale
     C. Manual review không thể mở rộng khi lượng sản phẩm (traces) lên tới 100k+
     D. Automated evals không cần calibration
   **Answer / Đáp án:** C

   Lớp đánh giá nào được ưu tiên số 1 và luôn bật trong hệ thống eval?
   **Answer / Đáp án:** B

   Khi nào nên sử dụng LLM-as-Judge thay vì Code-based Evals?
     A. Khi tiêu chí xác minh được bằng rule, regex, hoặc schema
     B. Khi cần đánh giá deterministic và nhanh
     C. Khi tiêu chí phụ thuộc vào ngữ cảnh, sắc thái ngôn ngữ
     D. Khi cần sample có chủ đích các trường hợp nghi ngờ
   **Answer / Đáp án:** C

   Trong Eval Lifecycle (quy trình đưa AI ra production), bước nào đóng vai trò Release Gate để chặn lỗi trước khi deploy?
   **Answer / Đáp án:** B

   Metric nào là North Star Metric (chỉ số tổng hợp chính) cho Agent?
     C. Agent Success Rate (tổng hợp từ task correctness, schema pass rate, v.v.)
   **Answer / Đáp án:** C
