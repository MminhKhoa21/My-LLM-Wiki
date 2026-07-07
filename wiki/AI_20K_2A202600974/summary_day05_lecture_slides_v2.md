---
type: summary
title: "Summary of Day 5 Lecture Slides v2: AI Product Design for Uncertainty"
description: "A detailed summary of the Day 5 Lecture Slides v2, exploring the transition from AI model capabilities to trustworthy user products, focusing on feedback loops, data flywheels, and ROI."
tags: [AI product, product management, uncertainty, UX, evaluation, feedback loop, data flywheel, ROI]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/5/1-day05-lecture-slides-v2.pdf"]
---
# Summary of Day 5 Lecture Slides v2: AI Product Design for Uncertainty
# Tóm tắt Slides Bài giảng Ngày 5 v2: Thiết kế Sản phẩm AI cho Sự không chắc chắn

These slides complement the Day 5 instruction, emphasizing how to transition from a functioning AI model to a product that users trust. It heavily focuses on the iterative nature of AI products, feedback mechanisms, and the economics of AI.
*Các slide này bổ sung cho bài giảng Ngày 5, nhấn mạnh cách chuyển đổi từ một mô hình AI đang hoạt động thành một sản phẩm mà người dùng tin tưởng. Bài giảng tập trung nhiều vào tính chất lặp lại của các sản phẩm AI, cơ chế phản hồi và tính kinh tế của AI.*

## 1. The Core Misconceptions
## 1. Những Nhận thức sai lầm Cốt lõi

- **Demo ≠ Product:** An agent that "works" is not necessarily a successful product. Common mistakes include adding AI just for FOMO (Google AI Overviews vs. Perplexity), stopping at an 80% accurate demo (Gamma/Tome requiring too much manual fixing), or building everything from scratch when APIs suffice.
  *Demo ≠ Sản phẩm: Một agent "hoạt động được" không nhất thiết là một sản phẩm thành công. Những sai lầm phổ biến bao gồm thêm AI chỉ vì FOMO (Google AI Overviews so với Perplexity), dừng lại ở bản demo chính xác 80% (Gamma/Tome đòi hỏi quá nhiều chỉnh sửa thủ công), hoặc xây dựng mọi thứ từ đầu khi mà các APIs đã đủ đáp ứng.*

- **AI is Probabilistic:** Unlike traditional software that follows strict rules and yields consistent results, AI outputs vary. Designing an AI product means designing for this inherent uncertainty.
  *AI mang tính Xác suất: Khác với phần mềm truyền thống tuân theo các quy tắc nghiêm ngặt và mang lại kết quả nhất quán, đầu ra của AI biến thiên. Thiết kế một sản phẩm AI nghĩa là thiết kế cho sự không chắc chắn cố hữu này.*

## 2. Managing Uncertainty: The Three Pillars
## 2. Quản lý Sự không chắc chắn: Ba Trụ cột

- **Requirement:** Must define thresholds and fallback behaviors. It's not just "Input -> Output," but "Input -> Output (with 85% confidence), else ask user."
  *Yêu cầu: Phải xác định các ngưỡng và hành vi dự phòng. Không chỉ là "Đầu vào -> Đầu ra," mà là "Đầu vào -> Đầu ra (với 85% độ tin cậy), nếu không thì hỏi người dùng."*

- **UX (Graceful Failure & Trust Recovery):** Design for when the AI is wrong. The user must be able to see the error, correct it easily, and regain trust in the system.
  *UX (Thất bại nhẹ nhàng & Phục hồi niềm tin): Thiết kế cho những lúc AI sai. Người dùng phải có khả năng nhìn thấy lỗi, sửa nó dễ dàng và lấy lại niềm tin vào hệ thống.*

  - *4 UI Patterns:* What happens when right? When unsure? When wrong? When trust is lost?
    *4 Mẫu Giao diện: Chuyện gì xảy ra khi đúng? Khi không chắc? Khi sai? Khi mất niềm tin?*

- **Eval (Quality Distribution):** Testing is no longer pass/fail. It's about running the system 100 times and determining what percentage of failures is acceptable.
  *Đánh giá (Phân bố Chất lượng): Kiểm thử không còn là đạt/trượt nữa. Nó là việc chạy hệ thống 100 lần và xác định tỷ lệ thất bại nào có thể chấp nhận được.*

## 3. Automation vs. Augmentation & Error Types
## 3. Tự động hóa vs. Tăng cường & Các loại Lỗi

- **Deployment Strategy:** How you deploy AI changes everything. GitHub Copilot uses augmentation (low accuracy but zero friction to reject). Spam filters use automation (high accuracy required because errors are hidden from the user).
  *Chiến lược Triển khai: Cách bạn triển khai AI thay đổi mọi thứ. GitHub Copilot sử dụng tăng cường (độ chính xác thấp nhưng không có rào cản khi từ chối). Bộ lọc thư rác sử dụng tự động hóa (yêu cầu độ chính xác cao vì lỗi bị ẩn khỏi người dùng).*

- **Precision vs. Recall:**
  *Độ chính xác (Precision) vs. Độ phủ (Recall):*

  - **Precision:** Focuses on minimizing false positives. Prioritize this when the user cannot easily see or fix the error, and the cost of acting wrongly is high (e.g., Legal RAG, Bank Chatbot).
    *Độ chính xác (Precision): Tập trung giảm thiểu dương tính giả. Ưu tiên điều này khi người dùng không dễ dàng nhìn thấy hoặc sửa lỗi, và chi phí khi hành động sai là cao (VD: Legal RAG, Chatbot Ngân hàng).*

  - **Recall:** Focuses on minimizing false negatives. Prioritize this when missing something is catastrophic, even if the user doesn't see it (e.g., Child content moderation, Fraud detection).
    *Độ phủ (Recall): Tập trung giảm thiểu âm tính giả. Ưu tiên điều này khi bỏ sót điều gì đó là thảm họa, ngay cả khi người dùng không nhìn thấy (VD: Kiểm duyệt nội dung trẻ em, Phát hiện gian lận).*

## 4. The Data Flywheel and Feedback Loops
## 4. Vòng xoay Dữ liệu (Data Flywheel) và Các Vòng Phản hồi

- **AI is a Living Organism:** Traditional software is static once shipped. AI products begin their lifecycle once shipped.
  *AI là một Sinh vật sống: Phần mềm truyền thống là tĩnh khi được phát hành. Sản phẩm AI mới thực sự bắt đầu vòng đời khi được tung ra.*

- **The Loop IS the Product:** Data collection -> Analysis -> Model fine-tuning -> Repeat. The speed and quality of this loop define the product's success.
  *Vòng lặp LÀ Sản phẩm: Thu thập dữ liệu -> Phân tích -> Tinh chỉnh mô hình -> Lặp lại. Tốc độ và chất lượng của vòng lặp này quyết định sự thành công của sản phẩm.*

- **Types of Feedback Signals:**
  *Các Loại Tín hiệu Phản hồi:*

  1. **Implicit:** System collects data without user intent (e.g., time spent reading, ignoring a Copilot suggestion).
     *Ngầm định: Hệ thống thu thập dữ liệu mà người dùng không chủ ý (VD: thời gian dành để đọc, bỏ qua gợi ý của Copilot).*

  2. **Explicit:** User actively rates the output (e.g., Thumbs up/down, "Was this helpful?").
     *Rõ ràng: Người dùng chủ động đánh giá đầu ra (VD: Thích/Không thích, "Điều này có hữu ích không?").*

  3. **Correction:** User manually fixes the AI's output (e.g., editing a Grammarly suggestion). This is the highest quality signal.
     *Sửa chữa: Người dùng sửa lỗi đầu ra của AI bằng tay (VD: chỉnh sửa gợi ý của Grammarly). Đây là tín hiệu có chất lượng cao nhất.*

- **High-Value Data Sources:** Real-time data, user-specific data, specialized domain data (e.g., Dragon medical records), human expert evaluations, RLHF (Reinforcement Learning from Human Feedback), and context data.
  *Nguồn Dữ liệu Giá trị Cao: Dữ liệu thời gian thực, dữ liệu dành riêng cho người dùng, dữ liệu lĩnh vực chuyên biệt (VD: hồ sơ y tế Dragon), đánh giá của chuyên gia con người, RLHF (Học tăng cường từ Phản hồi của Con người), và dữ liệu ngữ cảnh.*

## 5. AI Economics and ROI
## 5. Tính Kinh tế của AI và ROI (Tỷ suất Hoàn vốn)

- **The Cost Triangle:** You must balance Cost, Capability, and Speed.
  *Tam giác Chi phí: Bạn phải cân bằng giữa Chi phí, Năng lực và Tốc độ.*

  - *Copilot:* Prioritizes speed (small model, fast, high error rate acceptable).
    *Copilot: Ưu tiên tốc độ (mô hình nhỏ, nhanh, tỷ lệ lỗi cao có thể chấp nhận được).*

  - *Harvey (Legal AI):* Prioritizes capability (large model, slow, high cost acceptable).
    *Harvey (AI Pháp lý): Ưu tiên năng lực (mô hình lớn, chậm, chi phí cao có thể chấp nhận được).*

  - *Grammarly:* Prioritizes cost (rules-based first, AI only when necessary to support 30M+ free users).
    *Grammarly: Ưu tiên chi phí (dựa trên quy tắc trước, chỉ dùng AI khi cần thiết để hỗ trợ 30 triệu+ người dùng miễn phí).*

- **ROI Modeling (3 Scenarios):** Because AI costs scale per use (inference costs), you must plan for three scenarios:
  *Mô hình hóa ROI (3 Kịch bản): Vì chi phí AI tăng theo số lần sử dụng (chi phí suy luận), bạn phải lập kế hoạch cho ba kịch bản:*

  1. **Conservative:** Low accuracy, low adoption, high costs.
     *Bảo thủ: Độ chính xác thấp, tỷ lệ áp dụng thấp, chi phí cao.*

  2. **Realistic:** Average accuracy, medium adoption, balanced costs.
     *Thực tế: Độ chính xác trung bình, tỷ lệ áp dụng trung bình, chi phí cân bằng.*

  3. **Optimistic:** High accuracy, flywheel effect activated, reduced costs at scale.
     *Lạc quan: Độ chính xác cao, hiệu ứng vòng xoay được kích hoạt, giảm chi phí ở quy mô lớn.*

## 6. Hackathon Deliverables (Thin Spec)
## 6. Yêu cầu Bàn giao Hackathon (Đặc tả Mỏng)

The slides conclude by defining the deliverables for the Day 5/6 Hackathon:
*Các slide kết thúc bằng việc xác định các sản phẩm bàn giao cho Hackathon Ngày 5/6:*

- **AI Product Canvas:** Summarizes Value, Trust, Feasibility, and Learning Signals.
  *AI Product Canvas: Tóm tắt Giá trị, Niềm tin, Tính khả thi và Các Tín hiệu Học hỏi.*

- **User Stories (4 Paths):** Happy, Low-confidence, Failure, Correction.
  *User Stories (4 Luồng): Hoàn hảo, Tự tin thấp, Thất bại, Sửa chữa.*

- **Eval Metrics:** Define thresholds and red flags.
  *Chỉ số Đánh giá: Xác định các ngưỡng và cảnh báo đỏ.*

- **Failure Modes:** Trigger -> Impact -> Mitigation.
  *Các Chế độ Thất bại: Kích hoạt -> Tác động -> Giảm nhẹ.*

- **ROI Scenarios:** Conservative, Realistic, Optimistic.
  *Các Kịch bản ROI: Bảo thủ, Thực tế, Lạc quan.*

- **Prototype:** Must demonstrate the failure path, not just a successful "happy path."
  *Bản mẫu: Phải chứng minh được luồng thất bại, không chỉ là một "luồng hoàn hảo" thành công.*
