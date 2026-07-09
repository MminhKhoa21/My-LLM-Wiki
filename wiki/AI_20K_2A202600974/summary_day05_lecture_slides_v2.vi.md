---
type: summary
title: "Summary of Day 5 Lecture Slides v2: AI Product Design for Uncertainty"
description: "A detailed summary of the Day 5 Lecture Slides v2, exploring the transition from AI model capabilities to trustworthy user products, focusing on feedback loops, data flywheels, and ROI."
tags: [AI product, product management, uncertainty, UX, evaluation, feedback loop, data flywheel, ROI]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/5/1-day05-lecture-slides-v2.pdf"]
---

# Tóm tắt Slides Bài giảng Ngày 5 v2: Thiết kế Sản phẩm AI cho Sự không chắc chắn

Các slide này bổ sung cho bài giảng Ngày 5, nhấn mạnh cách chuyển đổi từ một mô hình AI đang hoạt động thành một sản phẩm mà người dùng tin tưởng. Bài giảng tập trung nhiều vào tính chất lặp lại của các sản phẩm AI, cơ chế phản hồi và tính kinh tế của AI.

## 1. Những Nhận thức sai lầm Cốt lõi

  (Demo ≠ Sản phẩm: Một agent "hoạt động được" không nhất thiết là một sản phẩm thành công. Những sai lầm phổ biến bao gồm thêm AI chỉ vì FOMO (Google AI Overviews so với Perplexity), dừng lại ở bản demo chính xác 80% (Gamma/Tome đòi hỏi quá nhiều chỉnh sửa thủ công), hoặc xây dựng mọi thứ từ đầu khi mà các APIs đã đủ đáp ứng.)
  (AI mang tính Xác suất: Khác với phần mềm truyền thống tuân theo các quy tắc nghiêm ngặt và mang lại kết quả nhất quán, đầu ra của AI biến thiên. Thiết kế một sản phẩm AI nghĩa là thiết kế cho sự không chắc chắn cố hữu này.)

## 2. Quản lý Sự không chắc chắn: Ba Trụ cột

  (Yêu cầu: Phải xác định các ngưỡng và hành vi dự phòng. Không chỉ là "Đầu vào -> Đầu ra," mà là "Đầu vào -> Đầu ra (với 85% độ tin cậy), nếu không thì hỏi người dùng.")
  (UX (Thất bại nhẹ nhàng & Phục hồi niềm tin): Thiết kế cho những lúc AI sai. Người dùng phải có khả năng nhìn thấy lỗi, sửa nó dễ dàng và lấy lại niềm tin vào hệ thống.)
    (4 Mẫu Giao diện: Chuyện gì xảy ra khi đúng? Khi không chắc? Khi sai? Khi mất niềm tin?)
  (Đánh giá (Phân bố Chất lượng): Kiểm thử không còn là đạt/trượt nữa. Nó là việc chạy hệ thống 100 lần và xác định tỷ lệ thất bại nào có thể chấp nhận được.)

## 3. Tự động hóa vs. Tăng cường & Các loại Lỗi

  (Chiến lược Triển khai: Cách bạn triển khai AI thay đổi mọi thứ. GitHub Copilot sử dụng tăng cường (độ chính xác thấp nhưng không có rào cản khi từ chối). Bộ lọc thư rác sử dụng tự động hóa (yêu cầu độ chính xác cao vì lỗi bị ẩn khỏi người dùng).)
  (Độ chính xác (Precision) vs. Độ phủ (Recall):)
    (Độ chính xác (Precision): Tập trung giảm thiểu dương tính giả. Ưu tiên điều này khi người dùng không dễ dàng nhìn thấy hoặc sửa lỗi, và chi phí khi hành động sai là cao (VD: Legal RAG, Chatbot Ngân hàng).)
    (Độ phủ (Recall): Tập trung giảm thiểu âm tính giả. Ưu tiên điều này khi bỏ sót điều gì đó là thảm họa, ngay cả khi người dùng không nhìn thấy (VD: Kiểm duyệt nội dung trẻ em, Phát hiện gian lận).)

## 4. Vòng xoay Dữ liệu (Data Flywheel) và Các Vòng Phản hồi

  (AI là một Sinh vật sống: Phần mềm truyền thống là tĩnh khi được phát hành. Sản phẩm AI mới thực sự bắt đầu vòng đời khi được tung ra.)
  (Vòng lặp LÀ Sản phẩm: Thu thập dữ liệu -> Phân tích -> Tinh chỉnh mô hình -> Lặp lại. Tốc độ và chất lượng của vòng lặp này quyết định sự thành công của sản phẩm.)
  (Các Loại Tín hiệu Phản hồi:)
     (Ngầm định: Hệ thống thu thập dữ liệu mà người dùng không chủ ý (VD: thời gian dành để đọc, bỏ qua gợi ý của Copilot).)
     (Rõ ràng: Người dùng chủ động đánh giá đầu ra (VD: Thích/Không thích, "Điều này có hữu ích không?").)
     (Sửa chữa: Người dùng sửa lỗi đầu ra của AI bằng tay (VD: chỉnh sửa gợi ý của Grammarly). Đây là tín hiệu có chất lượng cao nhất.)
  (Nguồn Dữ liệu Giá trị Cao: Dữ liệu thời gian thực, dữ liệu dành riêng cho người dùng, dữ liệu lĩnh vực chuyên biệt (VD: hồ sơ y tế Dragon), đánh giá của chuyên gia con người, RLHF (Học tăng cường từ Phản hồi của Con người), và dữ liệu ngữ cảnh.)

## 5. Tính Kinh tế của AI và ROI (Tỷ suất Hoàn vốn)

  (Tam giác Chi phí: Bạn phải cân bằng giữa Chi phí, Năng lực và Tốc độ.)
    (Copilot: Ưu tiên tốc độ (mô hình nhỏ, nhanh, tỷ lệ lỗi cao có thể chấp nhận được).)
    (Harvey (AI Pháp lý): Ưu tiên năng lực (mô hình lớn, chậm, chi phí cao có thể chấp nhận được).)
    (Grammarly: Ưu tiên chi phí (dựa trên quy tắc trước, chỉ dùng AI khi cần thiết để hỗ trợ 30 triệu+ người dùng miễn phí).)
  (Mô hình hóa ROI (3 Kịch bản): Vì chi phí AI tăng theo số lần sử dụng (chi phí suy luận), bạn phải lập kế hoạch cho ba kịch bản:)
     (Bảo thủ: Độ chính xác thấp, tỷ lệ áp dụng thấp, chi phí cao.)
     (Thực tế: Độ chính xác trung bình, tỷ lệ áp dụng trung bình, chi phí cân bằng.)
     (Lạc quan: Độ chính xác cao, hiệu ứng vòng xoay được kích hoạt, giảm chi phí ở quy mô lớn.)

## 6. Yêu cầu Bàn giao Hackathon (Đặc tả Mỏng)

Các slide kết thúc bằng việc xác định các sản phẩm bàn giao cho Hackathon Ngày 5/6:
  (AI Product Canvas: Tóm tắt Giá trị, Niềm tin, Tính khả thi và Các Tín hiệu Học hỏi.)
  (User Stories (4 Luồng): Hoàn hảo, Tự tự tin thấp, Thất bại, Sửa chữa.)
  (Chỉ số Đánh giá: Xác định các ngưỡng và cảnh báo đỏ.)
  (Các Chế độ Thất bại: Kích hoạt -> Tác động -> Giảm nhẹ.)
  (Các Kịch bản ROI: Bảo thủ, Thực tế, Lạc quan.)
  (Bản mẫu: Phải chứng minh được luồng thất bại, không chỉ là một "luồng hoàn hảo" thành công.)
