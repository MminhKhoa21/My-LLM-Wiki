---
type: overview
title: "Day 5 Overview - Thiết kế sản phẩm AI"
description: "Thiết kế sản phẩm AI đối phó với sự không chắc chắn, tập trung vào UX, đánh giá và Feedback loop."
tags: [ai, 20k, day5]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/5/1-day05-lecture-slides-v2.pdf"]
---

# Day 5: Thiết kế sản phẩm AI cho sự không chắc chắn
# Day 5: Designing AI Products for Uncertainty

## 1. AI Product ≠ Phần mềm truyền thống
## 1. AI Product ≠ Traditional Software
- Phần mềm truyền thống chạy theo luật, đưa ra kết quả cố định. AI chạy theo xác suất, kết quả mỗi lần một khác và tồn tại sự không chắc chắn (uncertainty).
- *Traditional software runs on rules, producing fixed results. AI runs on probabilities, results vary each time, and there is inherent uncertainty.*
- Thiết kế AI Product không chỉ là gọi API, mà là thiết kế xoay quanh sự không chắc chắn đó. 3 trụ cột thiết kế AI product: **Yêu cầu (Requirement)**, **Trải nghiệm (UX)**, và **Đánh giá (Eval)**.
- *Designing an AI Product is not just calling an API, but designing around that uncertainty. The 3 pillars of AI product design are: **Requirement**, **User Experience (UX)**, and **Evaluation (Eval)**.*

## 2. Requirement & UX cho AI
## 2. Requirement & UX for AI
- Phân biệt giữa **Automation** (AI tự động làm thay, user không thấy, yêu cầu độ chính xác cực cao) và **Augmentation** (AI gợi ý, user duyệt, chấp nhận độ chính xác thấp hơn để đổi lấy tốc độ/hiệu suất). Tốt nhất nên bắt đầu bằng Augmentation và tăng dần Automation.
- *Distinguish between **Automation** (AI does it automatically, invisible to the user, requires extremely high accuracy) and **Augmentation** (AI suggests, user approves, accepts lower accuracy in exchange for speed/efficiency). It is best to start with Augmentation and gradually increase Automation.*
- **Graceful Failure & Trust Recovery**: AI chắc chắn sẽ sai, vấn đề là xử lý lỗi một cách nhẹ nhàng (đưa ra các lựa chọn thay thế, cho phép user sửa, giải thích lý do) để giữ được niềm tin của người dùng.
- ***Graceful Failure & Trust Recovery**: AI will inevitably make mistakes; the key is to handle errors gracefully (provide alternatives, allow users to correct, explain reasons) to maintain user trust.*
- Tránh việc lấy giao diện Chatbot làm mặc định. UI/UX cho AI nên hiển thị quá trình suy luận, cho phép chỉnh sửa kế hoạch, v.v.
- *Avoid defaulting to a Chatbot interface. UI/UX for AI should display the reasoning process, allow editing of plans, etc.*

## 3. Đánh giá (Evaluation) - Precision vs Recall
## 3. Evaluation - Precision vs Recall
- Không có câu trả lời "đúng/sai" tuyệt đối mà chỉ có phân phối chất lượng.
- *There are no absolute "right/wrong" answers, only quality distributions.*
- **Precision**: Tỷ lệ đúng trong những gì AI dự đoán là đúng (giảm báo nhầm / False Positive). Ưu tiên khi hậu quả của hành động sai là rất lớn (ví dụ: chuyển tiền, xoá email).
- ***Precision**: The proportion of correct predictions among all positive predictions made by AI (reduces False Positives). Prioritize when the consequences of a wrong action are severe (e.g., transferring money, deleting emails).*
- **Recall**: Tỷ lệ tìm được trong tất cả những thứ cần tìm (giảm bỏ sót / False Negative). Ưu tiên khi bỏ sót gây hậu quả nghiêm trọng hơn (ví dụ: lọc nội dung trẻ em, y tế).
- ***Recall**: The proportion of actual positives successfully found (reduces False Negatives). Prioritize when missing something causes severe consequences (e.g., filtering child abuse content, medical diagnostics).*
- Chọn ưu tiên Precision hay Recall phụ thuộc vào bài toán và trải nghiệm người dùng (UX).
- *Choosing to prioritize Precision or Recall depends on the problem and the User Experience (UX).*

## 4. Feedback Loop & Data Flywheel
## 4. Feedback Loop & Data Flywheel
- Sản phẩm AI phải liên tục học hỏi từ tương tác của người dùng.
- *AI products must continuously learn from user interactions.*
- 3 loại feedback signal:
- *3 types of feedback signals:*
  - **Implicit (Ngầm)**: Thời gian xem, cuộn trang, tỷ lệ chấp nhận/bỏ qua.
  - ***Implicit**: View time, scrolling, acceptance/ignore rate.*
  - **Explicit (Trực tiếp)**: Thích/Không thích (Thumbs up/down), đánh giá sao.
  - ***Explicit**: Thumbs up/down, star ratings.*
  - **Correction (Sửa lỗi)**: User trực tiếp sửa kết quả của AI.
  - ***Correction**: User directly corrects the AI's output.*
- **Data Flywheel**: Dữ liệu từ người dùng giúp cải thiện mô hình, mô hình tốt hơn mang lại trải nghiệm tốt hơn, thu hút nhiều người dùng hơn -> tạo vòng lặp liên tục cải tiến. Đây mới là rào cản cạnh tranh cốt lõi của AI Product.
- ***Data Flywheel**: User data helps improve the model, a better model brings a better experience, attracting more users -> creating a continuous loop of improvement. This is the core competitive moat of an AI Product.*

## 5. ROI & Chi phí
## 5. ROI & Costs
- Chi phí chạy AI phụ thuộc vào mỗi lượt sử dụng (Inference cost). Càng nhiều người dùng càng tốn tiền. Cần tính toán ROI chi tiết (theo kịch bản thận trọng, thực tế, lạc quan) trước khi scale.
- *AI running costs depend on each usage (Inference cost). The more users, the higher the cost. Detailed ROI calculation (under conservative, realistic, and optimistic scenarios) is needed before scaling.*
