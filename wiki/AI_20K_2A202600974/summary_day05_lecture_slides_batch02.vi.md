---
type: summary
title: "Summary of Day 5 Lecture Slides Batch 02: AI Product Kickoff Sprint"
description: "A comprehensive summary of the Day 5 Batch 02 lecture slides focusing on finding real problems, designing for AI failures, and scoping features for the hackathon."
tags: [AI product, hackathon, product management, uncertainty, UX, evaluation, requirements]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/5/1-day05-lecture-slides-batch02.pdf"]
---
*# Tóm tắt Slides Bài giảng Ngày 5 Batch 02: AI Product Kickoff Sprint*

*Các slide này bao gồm nội dung Kickoff Sprint Ngày 5 cho chương trình VinUni AI20K, chuẩn bị cho các đội thi Mini-Hackathon. Trọng tâm chính là việc chuyển từ một bản demo có khả năng về mặt kỹ thuật sang một sản phẩm AI đáng tin cậy và hướng đến người dùng.*

*## 1. Vấn đề Cốt lõi: Demo vs. Sản phẩm*

  *(Điểm nhấn: Chỉ vì một agent AI hoạt động được về mặt kỹ thuật (demo) không có nghĩa là sẽ có người dùng nó. Demo là khả năng kỹ thuật; sản phẩm là giá trị được mang lại trong bối cảnh thực tế.)*
  *(Ba Tầng Không chắc chắn:)*
     *(Đầu vào: Người dùng đặt câu hỏi mơ hồ hoặc không đầy đủ.)*
     *(Đầu ra: Câu trả lời của AI không cố định và có sự biến thiên.)*
     *(Quá trình: Rất khó để hiểu tại sao AI lại đưa ra một quyết định cụ thể.)*
  *(Hệ quả đối với Sản phẩm: Phần mềm tiêu chuẩn sửa lỗi để chúng biến mất. Sản phẩm AI phải quản lý phân phối của các lỗi. Sản phẩm phải được thiết kế cho những lúc AI không chắc chắn hoặc sai lệch.)*

*## 2. Quản lý Lỗi & Sự không chắc chắn*

  *(Sự trôi dạt trong Production: Ngay cả khi code không thay đổi, việc cập nhật mô hình, trôi dạt ngữ cảnh (VD: thay đổi chính sách), trôi dạt người dùng (thay đổi cách họ đặt câu hỏi) và trôi dạt prompt có thể gây ra hành vi không mong muốn.)*
  *(Định tuyến Lỗi: Một sản phẩm AI phải có luồng xử lý lỗi (Phát hiện → Định tuyến → Khôi phục → Học hỏi). Nếu một bản mẫu chỉ có "luồng hoàn hảo" (happy path), đó chưa phải là một sản phẩm AI.)*
  *(Hai Loại Lỗi (Dương tính giả vs. Âm tính giả):)*
    *(Dương tính giả (Lỗi báo cáo): AI nói "có" khi thực tế là "không" (VD: gắn cờ một giao dịch hợp lệ). Điều này làm giảm độ tin cậy.)*
    *(Âm tính giả (Lỗi bỏ sót): AI nói "không" khi thực tế là "có" (VD: bỏ sót một giao dịch gian lận). Điều này gây ra thiệt hại thực tế.)*
    *(Quyết định Sản phẩm: Bạn phải quyết định lỗi nào đắt giá hơn dựa trên trường hợp sử dụng cụ thể. Nếu dương tính giả đắt giá, hãy ưu tiên Độ chính xác (Precision). Nếu âm tính giả đắt giá, hãy ưu tiên Độ phủ (Recall).)*

*## 3. Tự động hóa (Automation) vs. Tăng cường (Augmentation)*

  *(Tự động hóa: AI hành động tự chủ. Tốt khi các tác vụ hẹp, kết quả có thể dự đoán được và lỗi sai không gây hậu quả lớn.)*
  *(Tăng cường: AI hỗ trợ con người. Thường là bước đi đầu tiên đúng đắn để thu thập dữ liệu, học hỏi và giảm rủi ro trước khi chuyển sang tự động hóa. Nó không chỉ là một phiên bản kém hơn của tự động hóa.)*
  *(Vai trò Con người: Trong mô hình "Human-in-the-loop", xác định rõ vai trò: Người đánh giá (kiểm tra đầu ra), Người quyết định (chọn từ các tùy chọn), Người huấn luyện (cung cấp tín hiệu học), hoặc Người giải cứu (can thiệp khi AI thất bại).)*
  *(Ranh giới Tác vụ: Đừng tự động hóa toàn bộ sản phẩm. Hãy chia nhỏ nó thành các tác vụ và tự động hóa các lát cắt cụ thể, có giá trị.)*

*## 4. Ba Trụ cột của Thiết kế Sản phẩm AI*

   *(Yêu cầu (Không chỉ là tính năng): Cần định nghĩa kết quả, ngưỡng tin cậy và cơ chế dự phòng. Hãy hỏi: "Mức độ thất bại nào có thể chấp nhận được?")*
   *(UX (Không chỉ là giao diện đẹp): Thiết kế cho những khi AI sai. Kết hợp "Thất bại nhẹ nhàng" và "Phục hồi niềm tin". Hãy hỏi: "Người dùng sẽ làm gì khi AI thất bại?")*
   *(Đánh giá (Không chỉ là đạt/trượt): Đo lường sự phân bố chất lượng qua nhiều lần chạy. Hãy hỏi: "Tỷ lệ lỗi nào có thể chấp nhận được?")*

*## 5. Mẫu Giao diện cho AI (4 Luồng)*

*Mọi sản phẩm AI đều phải trả lời bốn câu hỏi:*
   *(Khi đúng: Người dùng thấy gì?)*
   *(Khi không chắc chắn: Hệ thống làm gì (VD: hỏi các câu hỏi làm rõ)?)*
   *(Khi sai: Người dùng sửa chữa như thế nào?)*
   *(Khi mất niềm tin: Người dùng thoát ra hoặc phục hồi như thế nào?)*

*## 6. Chuẩn bị Hackathon (Các Lát cắt Xây dựng & Đặc tả Mỏng)*

  *(Từ Bằng chứng đến Lát cắt Xây dựng: Bắt đầu với bằng chứng người dùng thực tế (phỏng vấn, đánh giá, trải nghiệm cá nhân). Tìm insight, xác định cơ hội, và chọn một "lát cắt xây dựng" nhỏ.)*
  *(Phạm vi Lát cắt Xây dựng: Một người dùng, một tác vụ, một quyết định AI, một luồng thất bại.)*
  *(AI Product Canvas: Một trang duy nhất xác định Giá trị, Niềm tin, Tính khả thi và Các Tín hiệu Học hỏi.)*
  *(Đặc tả Mỏng cho Thất bại: Bạn phải có khả năng viết: "Nếu người dùng [hành động kích hoạt], AI có thể [thất bại], gây ra [tác động]. Bản mẫu xử lý điều này bằng cách [biện pháp giảm nhẹ].")*
  *(Vibe Coding cho Sản phẩm: Sử dụng AI để xây dựng bản mẫu, nhưng bản mẫu bắt buộc phải chứng minh được một luồng thất bại, không chỉ là một bản demo thành công.)*

*## 7. Vé đầu ra cho Ngày 5*

*Các đội phải hoàn thành Ngày 5 với:*
   *(Bằng chứng người dùng)*
   *(Một lát cắt xây dựng duy nhất)*
   *(Quyết định chọn Tự động hóa hay Tăng cường)*
   *(Một luồng thất bại đã được xác định để kiểm thử)*
   *(Phân chia vai trò làm chủ rõ ràng cho hackathon)*
