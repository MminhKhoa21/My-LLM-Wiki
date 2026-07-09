---
type: summary
title: "Day 21 – Track 1: AI Evaluation (Vai trò PM)"
description: "Vai trò của AI Product Manager trong việc thiết kế và vận hành hệ thống đánh giá AI, từ giai đoạn phát triển đến sản xuất."
tags: [ai, 20k, day21, track1, evaluation, pm]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/d21-slide-v0.pdf", "raw/AI_20K_2A202600974/21/day21-lab-instruction.pdf"]
---

## Ngày 21 – Track 1: AI Evaluation – Vai trò PM


***Giảng viên**: Mai Anh Nguyen (Blue) – Generalist Product Builder*  
***Khóa**: AICB Phase 2 · Ngày 21 · Track 1*

---


## 1. Bối cảnh: Sự dịch chuyển vai trò của PM trong sản phẩm AI


Với sản phẩm truyền thống, user flow là deterministic (chắc chắn), ta quan tâm tới Usage Flows, Conversion Rate. Với sản phẩm AI, outcome là probabilistic (xác suất), có chất lượng phân bố rộng (Poor - Good - Great). Vai trò của PM chuyển từ định nghĩa luồng sang quản lý **Agent Success Rate** và **Quality Distributions**.


AI Eval được chia làm 2 lớp:

   **Model Evals**: Đánh giá năng lực cơ sở của mô hình (Reasoning, Coding, Math, Safety). Do provider (OpenAI, Anthropic, Google) phụ trách.
   **Application Evals**: Đánh giá chất lượng thực tế trong ngữ cảnh sử dụng của người dùng. Tập trung vào độ chính xác, hữu ích, an toàn, latency, cost. Đây là phần việc của Product Team.


***Các bộ chấm điểm bổ sung nhau**:*

    **Code-based grader**: Nhanh, rẻ, khách quan nhưng cứng nhắc (kiểm tra exact match, regex, định dạng).
    **Model-based grader (LLM as Judge)**: Linh hoạt, bắt được sắc thái nhưng đắt, có thể không ổn định.
    **Human grader**: Chuẩn vàng, tốn kém, dùng để hiệu chỉnh các bộ chấm khác.

---


## 2. Vòng đời AI Evals (AI Evals Lifecycle)


Quá trình Evals không phải là làm một lần trước khi release mà là một vòng lặp liên tục:



   **Mục tiêu**: Làm thủ công (Manual review) để hiểu behavior trước khi chốt PRD.
   **Thực hiện**: Generate 10-30 test inputs (gồm cả happy path và edge cases), chạy qua prototype, gắn nhãn output (Pass/Fail).
   **Kết quả**: Đầu ra tốt trở thành **Golden Outputs** (dùng cho few-shot và evals). Những case fail giúp định hình PRD. Vibe check phải làm *trước* khi viết PRD.



   **Mục tiêu**: Đánh giá tự động trên reference dataset trước khi release. Phát hiện regression.
   **Quy trình**: Trigger thay đổi (prompt/model mới) -> Chạy tập test -> So sánh với baseline -> Quyết định Deploy hoặc Fix.
   **Lưu ý**: Đặt ra **Quality Gate** (ngưỡng chất lượng tối thiểu), không pass ngưỡng thì không ship.



   **Mục tiêu**: Theo dõi sau khi launch, bắt drift, và các unknown unknowns.
   **Câu hỏi**: AI có duy trì Agent Success Rate không? User có behavior gì mới (ngôn ngữ lạ, data format mới, intent ngoài PRD)? Offline và online có bị diverge (lệch) không?

---




PRD của sản phẩm AI khác với PRD truyền thống. Nó cần bổ sung:

   **Evaluation Rubric**: Tiêu chí Pass/Fail rõ ràng.
   **Golden Outputs**: Ví dụ cụ thể (Input -> Expected Output).
   **Prompt Logic & Tools**: Xử lý API, system instruction.
   **Dataset Strategy**: Kế hoạch thu thập dữ liệu để eval.
   **Edge Case Handling**: Định nghĩa thế nào là "fail gracefully" khi mô hình gặp lỗi.
   **Unit of AI Work**: Phải thu hẹp phạm vi nhiệm vụ để có thể đánh giá (không dùng các khái niệm rộng như "AI hữu ích", mà phải là "Phân loại ticket support vào đúng queue").

---


## 4. Thiết kế Coverage & Scenario Datasets


Thay vì nhờ LLM sinh ra 50 prompts ngẫu nhiên (thường bị đồng nhất), PM cần thiết kế **User Input Grid** để đảm bảo coverage thực tế.

   **Các chiều (Dimensions)**: WHO (Persona), WHAT (User intent), HOW (Context completeness, ambiguity, complexity), CONTEXT (Language, data freshness), RISK (Hậu quả nếu fail).
   **Candidate Scenario Bank**: Tổ hợp các dimension. Bao gồm *Representative scenarios* (case phổ biến), *Challenge scenarios* (khó, ambiguity, zero-hit), và *Critical regression candidates* (tuyệt đối không được sai lặp lại).

---




Trace là toàn bộ quá trình agent vận hành và suy nghĩ (Transcript chỉ là câu chat cuối cùng mà user thấy).

   **Vì sao cần đọc Trace?**: Đôi khi câu trả lời cuối (transcript) nhìn có vẻ đúng nhưng quá trình (trace) lại sai.
   **Chuẩn hóa Trace Codes**: PM đọc trace, gom nhóm lỗi thành các trace codes chuẩn hóa (vd: `wrong_intent`, `missing_lookup`, `premature_commit`) thay vì ghi chú bằng lời tự do. Điều này giúp đo lường, phân loại và ưu tiên sửa chữa.

---


## 6. Lab 21: Thiết kế Test Inputs cho AI Evals


Bài Lab thực hành kỹ năng của PM trong việc thiết kế tập input test.

   **Pha Cá nhân**: Chọn một Unit of AI Work, đặt Quality Question, thiết kế User Input Grid (tối thiểu 3 dimensions), chọn 10 combinations đáng test. Dùng AI sinh ra >20 câu natural-language inputs và tự tay filter (loại bỏ generic/sai intent) để tạo Scenario Dataset v0.
   **Pha Nhóm**: Merge các dimension, deduplicate các inputs, check coverage matrix và chốt một **Scenario Dataset v1** (>30 rows) đủ đa dạng (representative, challenge, high-risk). Viết handoff note chuẩn bị cho việc đánh giá agent sau này.

---


## Liên kết

