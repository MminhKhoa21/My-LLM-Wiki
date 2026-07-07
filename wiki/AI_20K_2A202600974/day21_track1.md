---
type: summary
title: "Day 21 – Track 1: AI Evaluation (Vai trò PM)"
description: "Vai trò của AI Product Manager trong việc thiết kế và vận hành hệ thống đánh giá AI, từ giai đoạn phát triển đến sản xuất."
tags: [ai, 20k, day21, track1, evaluation, pm]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/d21-slide-v0.pdf", "raw/AI_20K_2A202600974/21/day21-lab-instruction.pdf"]
---
## Day 21 – Track 1: AI Evaluation – The Role of PM

*## Ngày 21 – Track 1: AI Evaluation – Vai trò PM*

**Instructor**: Mai Anh Nguyen (Blue) – Generalist Product Builder  
**Course**: AICB Phase 2 · Day 21 · Track 1

***Giảng viên**: Mai Anh Nguyen (Blue) – Generalist Product Builder*  
***Khóa**: AICB Phase 2 · Ngày 21 · Track 1*

---

## 1. Context: The Shift in the PM’s Role in AI Products

*## 1. Bối cảnh: Sự dịch chuyển vai trò của PM trong sản phẩm AI*

For traditional products, the user flow is deterministic; we care about Usage Flows and Conversion Rate. For AI products, the outcome is probabilistic, with a wide distribution of quality (Poor – Good – Great). The PM’s role shifts from defining flows to managing **Agent Success Rate** and **Quality Distributions**.

*Với sản phẩm truyền thống, user flow là deterministic (chắc chắn), ta quan tâm tới Usage Flows, Conversion Rate. Với sản phẩm AI, outcome là probabilistic (xác suất), có chất lượng phân bố rộng (Poor - Good - Great). Vai trò của PM chuyển từ định nghĩa luồng sang quản lý **Agent Success Rate** và **Quality Distributions**.*

AI Eval is divided into two layers:

*AI Eval được chia làm 2 lớp:*

- **Model Evals**: Evaluate the foundational capabilities of the model (Reasoning, Coding, Math, Safety). Handled by the provider (OpenAI, Anthropic, Google).
  * **Model Evals**: Đánh giá năng lực cơ sở của mô hình (Reasoning, Coding, Math, Safety). Do provider (OpenAI, Anthropic, Google) phụ trách.*
- **Application Evals**: Evaluate real-world quality in the user’s context. Focus on accuracy, usefulness, safety, latency, cost. This is the Product Team’s responsibility.
  * **Application Evals**: Đánh giá chất lượng thực tế trong ngữ cảnh sử dụng của người dùng. Tập trung vào độ chính xác, hữu ích, an toàn, latency, cost. Đây là phần việc của Product Team.*

**Three complementary grading methods:**

***Các bộ chấm điểm bổ sung nhau**:*

1. **Code-based grader**: Fast, cheap, objective but rigid (checks exact match, regex, formatting).
   * **Code-based grader**: Nhanh, rẻ, khách quan nhưng cứng nhắc (kiểm tra exact match, regex, định dạng).*
2. **Model-based grader (LLM as Judge)**: Flexible, captures nuance but expensive, potentially unstable.
   * **Model-based grader (LLM as Judge)**: Linh hoạt, bắt được sắc thái nhưng đắt, có thể không ổn định.*
3. **Human grader**: Gold standard, costly, used to calibrate other graders.
   * **Human grader**: Chuẩn vàng, tốn kém, dùng để hiệu chỉnh các bộ chấm khác.*

---

## 2. AI Evals Lifecycle

*## 2. Vòng đời AI Evals (AI Evals Lifecycle)*

The evaluation process is not a one-time task before release but a continuous loop:

*Quá trình Evals không phải là làm một lần trước khi release mà là một vòng lặp liên tục:*

### Stage 01: Vibe Check (Prototype phase)

*### Stage 01: Vibe Check (Prototype phase)*

- **Goal**: Manual review to understand behavior before finalizing the PRD.
  * **Mục tiêu**: Làm thủ công (Manual review) để hiểu behavior trước khi chốt PRD.*
- **Execution**: Generate 10–30 test inputs (including happy path and edge cases), run through the prototype, label outputs (Pass/Fail).
  * **Thực hiện**: Generate 10-30 test inputs (gồm cả happy path và edge cases), chạy qua prototype, gắn nhãn output (Pass/Fail).*
- **Result**: Good outputs become **Golden Outputs** (used for few-shot and evals). Failed cases help shape the PRD. Vibe check must be done *before* writing the PRD.
  * **Kết quả**: Đầu ra tốt trở thành **Golden Outputs** (dùng cho few-shot và evals). Những case fail giúp định hình PRD. Vibe check phải làm *trước* khi viết PRD.*

### Stage 02: Offline Evals (Build phase)

*### Stage 02: Offline Evals (Build phase)*

- **Goal**: Automated evaluation on a reference dataset before release. Detect regression.
  * **Mục tiêu**: Đánh giá tự động trên reference dataset trước khi release. Phát hiện regression.*
- **Process**: Trigger a change (new prompt/model) → Run the test set → Compare with baseline → Decide to Deploy or Fix.
  * **Quy trình**: Trigger thay đổi (prompt/model mới) -> Chạy tập test -> So sánh với baseline -> Quyết định Deploy hoặc Fix.*
- **Note**: Set a **Quality Gate** (minimum quality threshold); if not passed, do not ship.
  * **Lưu ý**: Đặt ra **Quality Gate** (ngưỡng chất lượng tối thiểu), không pass ngưỡng thì không ship.*

### Stage 03: Online Monitoring (Production phase)

*### Stage 03: Online Monitoring (Production phase)*

- **Goal**: Monitor after launch, detect drift, and uncover unknown unknowns.
  * **Mục tiêu**: Theo dõi sau khi launch, bắt drift, và các unknown unknowns.*
- **Questions**: Does the AI maintain the Agent Success Rate? Are there new user behaviors (unusual language, new data formats, intents outside the PRD)? Is there divergence between offline and online metrics?
  * **Câu hỏi**: AI có duy trì Agent Success Rate không? User có behavior gì mới (ngôn ngữ lạ, data format mới, intent ngoài PRD)? Offline và online có bị diverge (lệch) không?*

---

## 3. AI-native PRDs

*## 3. AI-native PRDs*

PRDs for AI products differ from traditional PRDs. They need to include:

*PRD của sản phẩm AI khác với PRD truyền thống. Nó cần bổ sung:*

- **Evaluation Rubric**: Clear Pass/Fail criteria.
  * **Evaluation Rubric**: Tiêu chí Pass/Fail rõ ràng.*
- **Golden Outputs**: Concrete examples (Input → Expected Output).
  * **Golden Outputs**: Ví dụ cụ thể (Input -> Expected Output).*
- **Prompt Logic & Tools**: API handling, system instructions.
  * **Prompt Logic & Tools**: Xử lý API, system instruction.*
- **Dataset Strategy**: Plan for collecting evaluation data.
  * **Dataset Strategy**: Kế hoạch thu thập dữ liệu để eval.*
- **Edge Case Handling**: Define what “fail gracefully” means when the model encounters errors.
  * **Edge Case Handling**: Định nghĩa thế nào là "fail gracefully" khi mô hình gặp lỗi.*
- **Unit of AI Work**: Narrow the scope of tasks so they can be evaluated (avoid broad concepts like “AI helpfulness”; use concrete ones like “Classify a support ticket into the correct queue”).
  * **Unit of AI Work**: Phải thu hẹp phạm vi nhiệm vụ để có thể đánh giá (không dùng các khái niệm rộng như "AI hữu ích", mà phải là "Phân loại ticket support vào đúng queue").*

---

## 4. Designing Coverage & Scenario Datasets

*## 4. Thiết kế Coverage & Scenario Datasets*

Instead of asking the LLM to generate 50 random prompts (which often turn out homogeneous), the PM needs to design a **User Input Grid** to ensure real-world coverage.

*Thay vì nhờ LLM sinh ra 50 prompts ngẫu nhiên (thường bị đồng nhất), PM cần thiết kế **User Input Grid** để đảm bảo coverage thực tế.*

- **Dimensions**: WHO (Persona), WHAT (User intent), HOW (Context completeness, ambiguity, complexity), CONTEXT (Language, data freshness), RISK (Consequences if it fails).
  * **Các chiều (Dimensions)**: WHO (Persona), WHAT (User intent), HOW (Context completeness, ambiguity, complexity), CONTEXT (Language, data freshness), RISK (Hậu quả nếu fail).*
- **Candidate Scenario Bank**: Combinations of dimensions. Includes **Representative scenarios** (common cases), **Challenge scenarios** (difficult, ambiguous, zero‑hit), and **Critical regression candidates** (cases that must never fail again).
  * **Candidate Scenario Bank**: Tổ hợp các dimension. Bao gồm *Representative scenarios* (case phổ biến), *Challenge scenarios* (khó, ambiguity, zero-hit), và *Critical regression candidates* (tuyệt đối không được sai lặp lại).*

---

## 5. Trace Analysis

*## 5. Trace Analysis*

A trace is the entire process of the agent’s operation and reasoning (a transcript is just the final chat message the user sees).

*Trace là toàn bộ quá trình agent vận hành và suy nghĩ (Transcript chỉ là câu chat cuối cùng mà user thấy).*

- **Why read the trace?** Sometimes the final answer (transcript) looks correct, but the process (trace) is wrong.
  * **Vì sao cần đọc Trace?**: Đôi khi câu trả lời cuối (transcript) nhìn có vẻ đúng nhưng quá trình (trace) lại sai.*
- **Standardizing Trace Codes**: The PM reads traces, groups errors into standardized trace codes (e.g., `wrong_intent`, `missing_lookup`, `premature_commit`) instead of writing free‑form notes. This enables measurement, classification, and prioritization of fixes.
  * **Chuẩn hóa Trace Codes**: PM đọc trace, gom nhóm lỗi thành các trace codes chuẩn hóa (vd: `wrong_intent`, `missing_lookup`, `premature_commit`) thay vì ghi chú bằng lời tự do. Điều này giúp đo lường, phân loại và ưu tiên sửa chữa.*

---

## 6. Lab 21: Designing Test Inputs for AI Evals

*## 6. Lab 21: Thiết kế Test Inputs cho AI Evals*

This lab exercise trains the PM’s skill in designing test input sets.

*Bài Lab thực hành kỹ năng của PM trong việc thiết kế tập input test.*

- **Individual Phase**: Choose one Unit of AI Work, define a Quality Question, design a User Input Grid (minimum 3 dimensions), select 10 promising combinations. Use AI to generate >20 natural‑language inputs, then manually filter (remove generic/wrong‑intent items) to create a Scenario Dataset v0.
  * **Pha Cá nhân**: Chọn một Unit of AI Work, đặt Quality Question, thiết kế User Input Grid (tối thiểu 3 dimensions), chọn 10 combinations đáng test. Dùng AI sinh ra >20 câu natural-language inputs và tự tay filter (loại bỏ generic/sai intent) để tạo Scenario Dataset v0.*
- **Group Phase**: Merge dimensions, deduplicate inputs, check the coverage matrix, and finalize a **Scenario Dataset v1** (>30 rows) that is sufficiently diverse (representative, challenge, high‑risk). Write a handoff note for later agent evaluation.
  * **Pha Nhóm**: Merge các dimension, deduplicate các inputs, check coverage matrix và chốt một **Scenario Dataset v1** (>30 rows) đủ đa dạng (representative, challenge, high-risk). Viết handoff note chuẩn bị cho việc đánh giá agent sau này.*

---

## Links

*## Liên kết*

- [[day21_track2]] – CI/CD AI Systems
- [[day21_track3]] – Fine-tuning LLMs
- [[day21_overview]]
