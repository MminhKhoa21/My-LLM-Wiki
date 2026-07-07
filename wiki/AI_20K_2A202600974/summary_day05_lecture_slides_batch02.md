---
type: summary
title: "Summary of Day 5 Lecture Slides Batch 02: AI Product Kickoff Sprint"
description: "A comprehensive summary of the Day 5 Batch 02 lecture slides focusing on finding real problems, designing for AI failures, and scoping features for the hackathon."
tags: [AI product, hackathon, product management, uncertainty, UX, evaluation, requirements]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/5/1-day05-lecture-slides-batch02.pdf"]
---

# Summary of Day 5 Lecture Slides Batch 02: AI Product Kickoff Sprint
# Tóm tắt Slides Bài giảng Ngày 5 Batch 02: AI Product Kickoff Sprint

These slides cover the Day 5 Kickoff Sprint for the VinUni AI20K program, preparing teams for a Mini-Hackathon. The central narrative is moving from a technically capable demo to a trustworthy, user-focused AI product.
*Các slide này bao gồm nội dung Kickoff Sprint Ngày 5 cho chương trình VinUni AI20K, chuẩn bị cho các đội thi Mini-Hackathon. Trọng tâm chính là việc chuyển từ một bản demo có khả năng về mặt kỹ thuật sang một sản phẩm AI đáng tin cậy và hướng đến người dùng.*

## 1. The Core Problem: Demo vs. Product
## 1. Vấn đề Cốt lõi: Demo vs. Sản phẩm

- **The Hook:** Just because an AI agent works technically (demo) doesn't mean anyone will use it. Demos are technical capabilities; products are value delivered in a real context.
  *(Điểm nhấn: Chỉ vì một agent AI hoạt động được về mặt kỹ thuật (demo) không có nghĩa là sẽ có người dùng nó. Demo là khả năng kỹ thuật; sản phẩm là giá trị được mang lại trong bối cảnh thực tế.)*
- **Three Layers of Uncertainty:**
  *(Ba Tầng Không chắc chắn:)*
  1. **Input:** Users ask ambiguous or incomplete questions.
     *(Đầu vào: Người dùng đặt câu hỏi mơ hồ hoặc không đầy đủ.)*
  2. **Output:** AI answers are not fixed and have variance.
     *(Đầu ra: Câu trả lời của AI không cố định và có sự biến thiên.)*
  3. **Process:** It's hard to see why an AI made a specific decision.
     *(Quá trình: Rất khó để hiểu tại sao AI lại đưa ra một quyết định cụ thể.)*
- **Product Implication:** Standard software fixes bugs so they disappear. AI products must *manage the distribution of errors*. The product must be designed for times when the AI is uncertain or wrong.
  *(Hệ quả đối với Sản phẩm: Phần mềm tiêu chuẩn sửa lỗi để chúng biến mất. Sản phẩm AI phải quản lý phân phối của các lỗi. Sản phẩm phải được thiết kế cho những lúc AI không chắc chắn hoặc sai lệch.)*

## 2. Managing Errors & Uncertainty
## 2. Quản lý Lỗi & Sự không chắc chắn

- **Production Drift:** Even if the code doesn't change, model updates, context drift (e.g., policy changes), user drift (changing how they ask), and prompt drift can cause unexpected behavior.
  *(Sự trôi dạt trong Production: Ngay cả khi code không thay đổi, việc cập nhật mô hình, trôi dạt ngữ cảnh (VD: thay đổi chính sách), trôi dạt người dùng (thay đổi cách họ đặt câu hỏi) và trôi dạt prompt có thể gây ra hành vi không mong muốn.)*
- **Error Routing:** An AI product must have a path for errors (Detect → Route → Recover → Learn). If a prototype only has a "happy path," it is not an AI product.
  *(Định tuyến Lỗi: Một sản phẩm AI phải có luồng xử lý lỗi (Phát hiện → Định tuyến → Khôi phục → Học hỏi). Nếu một bản mẫu chỉ có "luồng hoàn hảo" (happy path), đó chưa phải là một sản phẩm AI.)*
- **Two Types of Errors (False Positive vs. False Negative):**
  *(Hai Loại Lỗi (Dương tính giả vs. Âm tính giả):)*
  - **False Positive (Reporting error):** AI says "yes" when it's "no." (e.g., flagging a valid transaction). This reduces trust.
    *(Dương tính giả (Lỗi báo cáo): AI nói "có" khi thực tế là "không" (VD: gắn cờ một giao dịch hợp lệ). Điều này làm giảm độ tin cậy.)*
  - **False Negative (Missing error):** AI says "no" when it's "yes." (e.g., missing a fraudulent transaction). This causes actual harm.
    *(Âm tính giả (Lỗi bỏ sót): AI nói "không" khi thực tế là "có" (VD: bỏ sót một giao dịch gian lận). Điều này gây ra thiệt hại thực tế.)*
  - **Product Decision:** You must decide which error is more expensive based on your specific use case. If false positives are expensive, prioritize **Precision**. If false negatives are expensive, prioritize **Recall**.
    *(Quyết định Sản phẩm: Bạn phải quyết định lỗi nào đắt giá hơn dựa trên trường hợp sử dụng cụ thể. Nếu dương tính giả đắt giá, hãy ưu tiên Độ chính xác (Precision). Nếu âm tính giả đắt giá, hãy ưu tiên Độ phủ (Recall).)*

## 3. Automation vs. Augmentation
## 3. Tự động hóa (Automation) vs. Tăng cường (Augmentation)

- **Automation:** AI acts autonomously. Good when tasks are narrow, outcomes are predictable, and errors are cheap.
  *(Tự động hóa: AI hành động tự chủ. Tốt khi các tác vụ hẹp, kết quả có thể dự đoán được và lỗi sai không gây hậu quả lớn.)*
- **Augmentation:** AI assists a human. Often the right first step to gather data, learn, and lower risk before moving to automation. It is *not* just a lesser version of automation.
  *(Tăng cường: AI hỗ trợ con người. Thường là bước đi đầu tiên đúng đắn để thu thập dữ liệu, học hỏi và giảm rủi ro trước khi chuyển sang tự động hóa. Nó không chỉ là một phiên bản kém hơn của tự động hóa.)*
- **Human Roles:** In "Human-in-the-loop," define the role clearly: Reviewer (checks output), Decider (chooses from options), Trainer (provides learning signal), or Rescuer (intervenes when AI fails).
  *(Vai trò Con người: Trong mô hình "Human-in-the-loop", xác định rõ vai trò: Người đánh giá (kiểm tra đầu ra), Người quyết định (chọn từ các tùy chọn), Người huấn luyện (cung cấp tín hiệu học), hoặc Người giải cứu (can thiệp khi AI thất bại).)*
- **Task Boundary:** Don't automate an entire product. Break it down into tasks and automate specific, valuable slices.
  *(Ranh giới Tác vụ: Đừng tự động hóa toàn bộ sản phẩm. Hãy chia nhỏ nó thành các tác vụ và tự động hóa các lát cắt cụ thể, có giá trị.)*

## 4. The Three Pillars of AI Product Design
## 4. Ba Trụ cột của Thiết kế Sản phẩm AI

1. **Requirement (Not just features):** Needs to define the outcome, the confidence threshold, and the fallback mechanism. Ask: "What level of failure is acceptable?"
   *(Yêu cầu (Không chỉ là tính năng): Cần định nghĩa kết quả, ngưỡng tin cậy và cơ chế dự phòng. Hãy hỏi: "Mức độ thất bại nào có thể chấp nhận được?")*
2. **UX (Not just pretty screens):** Design for when the AI is wrong. Incorporate "Graceful Failure" and "Trust Recovery." Ask: "What does the user do when the AI fails?"
   *(UX (Không chỉ là giao diện đẹp): Thiết kế cho những khi AI sai. Kết hợp "Thất bại nhẹ nhàng" và "Phục hồi niềm tin". Hãy hỏi: "Người dùng sẽ làm gì khi AI thất bại?")*
3. **Eval (Not just pass/fail):** Measure the distribution of quality over many runs. Ask: "What percentage of errors is acceptable?"
   *(Đánh giá (Không chỉ là đạt/trượt): Đo lường sự phân bố chất lượng qua nhiều lần chạy. Hãy hỏi: "Tỷ lệ lỗi nào có thể chấp nhận được?")*

## 5. UI Patterns for AI (The 4 Paths)
## 5. Mẫu Giao diện cho AI (4 Luồng)

Every AI product must answer four questions:
*Mọi sản phẩm AI đều phải trả lời bốn câu hỏi:*
1. **When it's right:** What does the user see?
   *(Khi đúng: Người dùng thấy gì?)*
2. **When it's unsure:** What does the system do (e.g., ask clarifying questions)?
   *(Khi không chắc chắn: Hệ thống làm gì (VD: hỏi các câu hỏi làm rõ)?)*
3. **When it's wrong:** How does the user correct it?
   *(Khi sai: Người dùng sửa chữa như thế nào?)*
4. **When trust is lost:** How does the user opt-out or recover?
   *(Khi mất niềm tin: Người dùng thoát ra hoặc phục hồi như thế nào?)*

## 6. Hackathon Preparation (Build Slices & Thin Spec)
## 6. Chuẩn bị Hackathon (Các Lát cắt Xây dựng & Đặc tả Mỏng)

- **Evidence-to-Build Slice:** Start with real user evidence (interviews, reviews, own experience). Find the insight, define the opportunity, and choose a small "build slice."
  *(Từ Bằng chứng đến Lát cắt Xây dựng: Bắt đầu với bằng chứng người dùng thực tế (phỏng vấn, đánh giá, trải nghiệm cá nhân). Tìm insight, xác định cơ hội, và chọn một "lát cắt xây dựng" nhỏ.)*
- **Build Slice Scope:** One user, one task, one AI decision, one failure path.
  *(Phạm vi Lát cắt Xây dựng: Một người dùng, một tác vụ, một quyết định AI, một luồng thất bại.)*
- **AI Product Canvas:** A single page defining Value, Trust, Feasibility, and Learning Signals.
  *(AI Product Canvas: Một trang duy nhất xác định Giá trị, Niềm tin, Tính khả thi và Các Tín hiệu Học hỏi.)*
- **Thin Spec Failure:** You must be able to write: "If user [trigger], AI might [fail], causing [impact]. The prototype handles this by [mitigation]."
  *(Đặc tả Mỏng cho Thất bại: Bạn phải có khả năng viết: "Nếu người dùng [hành động kích hoạt], AI có thể [thất bại], gây ra [tác động]. Bản mẫu xử lý điều này bằng cách [biện pháp giảm nhẹ].")*
- **Vibe Coding for Product:** Use AI to build the prototype, but the prototype *must* demonstrate a failure path, not just a successful demo.
  *(Vibe Coding cho Sản phẩm: Sử dụng AI để xây dựng bản mẫu, nhưng bản mẫu bắt buộc phải chứng minh được một luồng thất bại, không chỉ là một bản demo thành công.)*

## 7. Exit Ticket for Day 5
## 7. Vé đầu ra cho Ngày 5

Teams must leave Day 5 with:
*Các đội phải hoàn thành Ngày 5 với:*
1. User evidence
   *(Bằng chứng người dùng)*
2. A single build slice
   *(Một lát cắt xây dựng duy nhất)*
3. A decision on Auto vs. Augment
   *(Quyết định chọn Tự động hóa hay Tăng cường)*
4. A defined failure path to test
   *(Một luồng thất bại đã được xác định để kiểm thử)*
5. Clear ownership roles for the hackathon
   *(Phân chia vai trò làm chủ rõ ràng cho hackathon)*
