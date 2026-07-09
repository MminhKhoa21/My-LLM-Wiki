---
type: summary
title: "Day 24 Track 1: AI Ethics, AI Safety and Responsible AI"
description: "Summary of Day 24 Track 1 covering AI safety, harm mapping, system mapping, and responsible AI practices."
tags: [ai-ethics, ai-safety, responsible-ai, harm-map, track1]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/24/d24-slide-v1.pdf", "AI_20K_2A202600974/24/day24-track1-lab.pdf"]
---
# Ngày 24 Track 1: Đạo đức và An toàn AI

Trang này tóm tắt bài giảng và bài thực hành về Đạo đức và An toàn AI cho Track 1.

## Các Khái niệm Chính

### *An toàn & Đạo đức AI*

An toàn AI không chỉ đơn thuần là hệ thống có hoạt động chính xác hay không, mà còn là cách nó tác động đến người dùng thực trong bối cảnh thực tế, và liệu có đủ các rào chắn an toàn cùng cơ chế chịu trách nhiệm trước khi triển khai hay không. "AI an toàn là một hệ thống được đặt đúng bối cảnh, có đúng rào chắn, và có người chịu trách nhiệm khi mọi thứ xảy ra sai sót."

### *Các Chế độ Hỏng hóc của AI*

  - **Ảo giác:** Bịa đặt sự thật, chính sách, dữ liệu hoặc liên kết với độ tự tin cao.
  - **Thiên vị / Công bằng:** Cung cấp kết quả lệch lạc giữa các nhóm nhân khẩu học khác nhau hoặc tạo ra bất bình đẳng tinh vi.
  - **Xu nịnh:** Đồng tình với người dùng ngay cả khi người dùng sai.
  - **Phụ thuộc quá mức:** Người dùng tin tưởng đầu ra của AI như chân lý tuyệt đối và không kiểm chứng lại.
  - **Lời khuyên có hại:** Đưa ra lời khuyên nguy hiểm về y tế, pháp lý, tài chính hoặc tự gây hại.
  - **Rò rỉ quyền riêng tư:** Tiết lộ thông tin nhận dạng cá nhân (PII), prompt, tài liệu nội bộ hoặc dữ liệu của người dùng khác.
  - **Lỗi chuyển tiếp:** Không từ chối hoặc chuyển cho nhân viên con người khi cần thiết.
  - **Lạm dụng / Phá khóa:** Người dùng buộc AI vượt qua các rào chắn hoặc ràng buộc của nó.

### *Bản đồ Hệ thống để Gỡ lỗi*

Khi một hệ thống AI gặp lỗi, điều quan trọng là xác định lớp nào đã gây ra lỗi thay vì chỉ đổ lỗi cho mô hình:

   1. **Trải nghiệm người dùng (UX):** Giao diện mà người dùng tương tác. Nếu UI khiến AI trông quá chính thức mà không có dấu hiệu không chắc chắn, người dùng có thể phụ thuộc quá mức vào nó.
   2. **Thông điệp Hệ thống & Nền tảng:** Các hướng dẫn điều khiển mô hình và các nguồn mà nó dựa vào. Lỗi ở đây dẫn đến ảo giác hoặc câu trả lời ngoài phạm vi.
   3. **Hệ thống An toàn:** Các rào chắn chặn, từ chối hoặc chuyển tiếp yêu cầu. Điểm yếu ở đây cho phép các yêu cầu có hại hoặc nhạy cảm đi qua.
   4. **Mô hình:** Mô hình AI cốt lõi. Nếu nó quá yếu cho nhiệm vụ hoặc có lỗi cố hữu, nó sẽ thất bại dù có hướng dẫn tốt.

### *Khung Bản đồ Tác hại*

Để phân tích rủi ro AI một cách có hệ thống, chúng ta đánh giá chúng qua bốn khía cạnh:

  - **Mức độ nghiêm trọng:** Tác động của tác hại (Thấp: khó chịu nhỏ, Trung bình: tác hại có thể khắc phục, Cao: mất mát tài chính/pháp lý/cơ hội, Nghiêm trọng: tổn hại thể chất hoặc thiệt hại không thể khắc phục).
  - **Quy mô:** Số lượng người hoặc nhóm bị ảnh hưởng.
  - **Xác suất:** Khả năng xảy ra tác hại.
  - **Tần suất:** Mức độ thường xuyên tác hại lặp lại nếu nó xảy ra.

## Lab 24: Săn tìm Nghiên cứu Tình huống & Bản đồ Tác hại

Phần thực hành tập trung vào việc chọn một ngành (ví dụ: Nhân sự, Giáo dục, Y tế, Di động, Truyền thông, Người sáng tạo nội dung) và tìm 2-3 nghiên cứu tình huống thất bại AI thực tế trong lĩnh vực đó.

  - **Ảnh chụp nhanh Rủi ro Ngành:** Đánh giá hồ sơ rủi ro tổng thể của ngành (tiềm năng tổn hại thể chất, quyết định có rủi ro cao, dữ liệu nhạy cảm, bán kính ảnh hưởng).
  - **Bảng tính Bản đồ Tác hại:** Với mỗi nghiên cứu tình huống, sinh viên phải xác định thời điểm rủi ro cao, các bên liên quan bị ảnh hưởng, chế độ hỏng hóc, lớp phát sinh lỗi, tác hại thực tế, lăng kính tác hại (ví dụ: thông tin sai lệch, thương tích, mất quyền riêng tư), và chấm điểm dựa trên Mức độ nghiêm trọng, Quy mô, Xác suất và Tần suất.

---

### *Câu hỏi ôn tập Ngày 24*

   Theo bài giảng, định nghĩa nào dưới đây mô tả đúng nhất về “AI an toàn”?
     A. Một hệ thống AI có độ chính xác cao và không bao giờ mắc lỗi.
     B. Một hệ thống AI được đặt trong bối cảnh phù hợp, có rào chắn và có người chịu trách nhiệm khi xảy ra sự cố.
     C. Một hệ thống AI có khả năng tự học và cải thiện mà không cần con người.
     D. Một hệ thống AI tuân thủ tất cả các quy định pháp luật hiện hành.
   **Answer / Đáp án:** B

   Trạng thái “Sycophancy” trong AI đề cập đến hiện tượng gì?
     A. AI tự bịa ra thông tin sai lệch nhưng rất tự tin.
     B. AI luôn đồng ý với người dùng ngay cả khi người dùng sai.
     C. AI tiết lộ thông tin cá nhân của người dùng khác.
     D. AI từ chối trả lời mọi câu hỏi nhạy cảm.
   **Answer / Đáp án:** B

   Khi một hệ thống AI đưa ra câu trả lời sai do không có đủ nguồn tham khảo (grounding) trong system message, lỗi này thuộc lớp nào trong System Map?
     A. UX (Trải nghiệm người dùng)
     B. Safety System (Hệ thống an toàn)
     C. Model (Mô hình)
     D. System Message & Grounding (Thông báo hệ thống và nền tảng)
   **Answer / Đáp án:** D

   Trong Harm Map Framework, yếu tố “Scale” đánh giá điều gì?
     A. Mức độ nghiêm trọng của tác hại (từ thấp đến nguy kịch).
     B. Số lượng người hoặc nhóm bị ảnh hưởng.
     C. Khả năng xảy ra tác hại.
     D. Tần suất tác hại lặp lại nếu đã xảy ra.
   **Answer / Đáp án:** B
