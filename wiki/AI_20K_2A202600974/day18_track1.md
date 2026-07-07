---
type: summary
title: "Day 18 Track 1: Human-Centered AI Design"
description: "Summary of Human-Centered AI design principles, focusing on trust calibration, agency, and feedback loops."
tags: [UX, Human-Centered AI, Trust, Agency, Feedback, Design]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/1-d18-slide-v1-track1.pdf", "raw/AI_20K_2A202600974/18/day18-track1-lab.pdf"]
---
# Human-Centered AI Design (Day 18 - Track 1)

**Instructor:** Mai Anh Nguyen (Blue)

---

## 1. Core Principles & Expectations  
*1. Nguyên tắc cốt lõi & Kỳ vọng*

- **Expectation Setting:** Avoid letting the UI promise more than the AI can deliver. Users need to understand what the AI can do, what it cannot do, and how it might fail.  
  *Đặt kỳ vọng: Tránh để giao diện người dùng hứa hẹn nhiều hơn những gì AI có thể thực hiện. Người dùng cần hiểu AI có thể làm gì, không thể làm gì và có thể thất bại như thế nào.*

- **AI Personality:** Combining *warmth* (friendly, approachable) and *competence*. A calibrated competence helps build sustainable trust. Emitting a signal of "not too perfect" can lower initial expectations and improve long-term satisfaction.  
  *Tính cách AI: Kết hợp giữa sự ấm áp (thân thiện, dễ tiếp cận) và năng lực. Năng lực được hiệu chỉnh phù hợp giúp xây dựng lòng tin bền vững. Phát tín hiệu "không quá hoàn hảo" có thể làm giảm kỳ vọng ban đầu và cải thiện sự hài lòng lâu dài.*

- **Reference Frameworks:** Google's PAIR Guidebook (AI product framing) and Microsoft's HAX Toolkit (AI interaction design).  
  *Khung tham khảo: Sổ tay PAIR của Google (định hình sản phẩm AI) và Bộ công cụ HAX của Microsoft (thiết kế tương tác AI).*

---

## 2. Trust Calibration  
*2. Hiệu chỉnh lòng tin*

- **Overtrust:** Users trust the AI beyond its true capabilities, leading them to delegate tasks excessively without verifying.  
  *Tin tưởng thái quá: Người dùng tin tưởng AI vượt quá khả năng thực sự, dẫn đến ủy thác nhiệm vụ quá mức mà không kiểm tra lại.*

- **Distrust:** Users trust the AI less than its capabilities, leading to *underuse*.  
  *Thiếu tin tưởng: Người dùng tin tưởng AI ít hơn khả năng thực tế, dẫn đến sử dụng không đầy đủ.*

- **Formula for Trust:** `Trust Calibration = Expectation + Explainability + Control`  
  *Công thức cho lòng tin: Hiệu chỉnh lòng tin = Kỳ vọng + Khả năng giải thích + Kiểm soát*  
  - *Expectation:* Clarify AI limits.  
    *Kỳ vọng: Làm rõ giới hạn của AI.*  
  - *Explainability:* Help users understand why AI produced a specific output.  
    *Khả năng giải thích: Giúp người dùng hiểu tại sao AI đưa ra đầu ra cụ thể.*  
  - *Control:* Allow users to edit, undo, preview, or approve actions.  
    *Kiểm soát: Cho phép người dùng chỉnh sửa, hoàn tác, xem trước hoặc phê duyệt các hành động.*

---

## 3. Augmentation vs. Automation (Agency)  
*3. Tăng cường so với Tự động hóa (Quyền chủ động)*

Determine the level of AI autonomy based on the **cost of error** and user intent certainty.  
*Xác định mức độ tự chủ của AI dựa trên chi phí sai sót và mức độ chắc chắn về ý định của người dùng.*

- **Act (Automation):** High certainty, low cost of error. Easy to undo. AI performs the action automatically to save time.  
  *Hành động (Tự động hóa): Độ chắc chắn cao, chi phí sai sót thấp. Dễ hoàn tác. AI tự động thực hiện hành động để tiết kiệm thời gian.*

- **Ask (Mixed-Initiative):** Moderate certainty, significant impact. AI asks for confirmation before proceeding.  
  *Hỏi (Sáng kiến hỗn hợp): Độ chắc chắn vừa phải, tác động đáng kể. AI yêu cầu xác nhận trước khi tiến hành.*

- **Don't Act (Inaction):** High cost of error, low certainty. The system leaves the decision entirely to the user.  
  *Không hành động (Bất động): Chi phí sai sót cao, độ chắc chắn thấp. Hệ thống hoàn toàn để quyết định cho người dùng.*

---

## 4. Handling AI Failures and Uncertainty  
*4. Xử lý lỗi AI và sự không chắc chắn*

- Explain *why* the system made a decision (e.g., mapping user behavior or inputs to outputs).  
  *Giải thích lý do tại sao hệ thống đưa ra quyết định (ví dụ: ánh xạ hành vi hoặc đầu vào của người dùng thành đầu ra).*

- Display results with confidence levels.  
  *Hiển thị kết quả kèm mức độ tin cậy.*

- Offer clear escape routes (e.g., transferring to a human agent, providing fallback options).  
  *Cung cấp các lối thoát rõ ràng (ví dụ: chuyển sang nhân viên hỗ trợ, đưa ra các tùy chọn dự phòng).*

- **Undo / Rollback:** Allow users to easily revert AI actions.  
  *Hoàn tác / Quay lại: Cho phép người dùng dễ dàng khôi phục các hành động của AI.*

- Use error states as opportunities to gather feedback and educate users on correct usage.  
  *Sử dụng trạng thái lỗi như cơ hội để thu thập phản hồi và hướng dẫn người dùng cách sử dụng đúng.*

---

## 5. Feedback Loops  
*5. Vòng phản hồi*

Feedback enables the system to learn from users and users to learn from the system.  
*Phản hồi cho phép hệ thống học hỏi từ người dùng và người dùng học hỏi từ hệ thống.*

- **User Feedback (Explicit):** Thumbs up/down, rating, reporting errors.  
  *Phản hồi của người dùng (Rõ ràng): Thích/không thích, đánh giá, báo cáo lỗi.*

- **User Feedback (Implicit):** User behaviors like undoing, abandoning tasks, or accepting suggestions.  
  *Phản hồi của người dùng (Ngầm định): Các hành vi của người dùng như hoàn tác, bỏ qua tác vụ hoặc chấp nhận gợi ý.*

- **System Feedback (Explicit):** Notifications explaining limits, status, or next steps.  
  *Phản hồi của hệ thống (Rõ ràng): Thông báo giải thích giới hạn, trạng thái hoặc các bước tiếp theo.*

- **System Feedback (Implicit):** UI affordances, default states, and progressive disclosure that guide user mental models.  
  *Phản hồi của hệ thống (Ngầm định): Các gợi ý của giao diện, trạng thái mặc định và tiết lộ dần dần giúp định hướng mô hình tinh thần của người dùng.*

---

## 6. Lab Scenario Design  
*6. Thiết kế kịch bản thực hành*

The lab exercise emphasizes designing a continuous slice of the AI experience across four phases:  
*Bài tập thực hành nhấn mạnh việc thiết kế một phân đoạn liên tục của trải nghiệm AI qua bốn giai đoạn:*

1. **Onboarding:** Setting expectations without overwhelming the user.  
   *Khởi tạo: Đặt kỳ vọng mà không làm người dùng choáng ngợp.*

2. **During Action:** Displaying AI reasoning, asking for context, or proposing solutions.  
   *Trong quá trình hành động: Hiển thị suy luận của AI, yêu cầu ngữ cảnh hoặc đề xuất giải pháp.*

3. **After Action:** Reviewing results, editing, and confirming.  
   *Sau hành động: Xem xét kết quả, chỉnh sửa và xác nhận.*

4. **Failure & Recovery:** Creating feedback loops to correct errors and continue the workflow seamlessly.  
   *Sai sót & Khắc phục: Tạo vòng phản hồi để sửa lỗi và tiếp tục quy trình làm việc một cách liền mạch.*
