---
type: summary
title: "Summary: Day 02 Reference Document"
description: "A comprehensive summary of the reference frameworks, case studies, and reading materials for Day 02."
tags: [Reference, Frameworks, Case Studies, Reading List]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/day02-reference-document.pdf"]
---
*# Tóm tắt: Tài liệu Tham khảo Ngày 02*

*## Tổng quan*
*Tài liệu này tổng hợp các tài liệu tham khảo toàn diện, các bộ khung (frameworks), các nghiên cứu tình huống (case studies), và các nguyên tắc cốt lõi được giảng dạy trong Ngày 02 của chương trình VinUni AI 20K. Nó đóng vai trò như một hướng dẫn để định hình các yêu cầu kinh doanh thành các bài toán AI có cấu trúc.*

*## 1. Các Bộ Khung và Mô Hình Ra Quyết Định*
*### Các Bộ Khung Trong Lớp Học*
  * **Dịch từ Kinh doanh sang AI:** Chuyển đổi các ý tưởng mơ hồ thành các Tuyên bố Vấn đề có cấu trúc.*
  * **Phổ Khả Năng Của AI:** Phân loại các tác vụ thành Dễ, Khó, hoặc Không Thể đối với AI hiện tại để thiết lập kỳ vọng đúng đắn.*
  * **Ma Trận Phù Hợp Của AI:** Ánh xạ Độ Mơ Hồ so với Độ Phức Tạp để đề xuất sử dụng Quy Tắc, Tính năng LLM, hoặc Agent.*
  * **Thang Nâng Cấp:** Tiến trình từ Prompt -> Truy xuất (Retrieval) -> Quy trình (Workflow) -> Agent. Luôn bắt đầu đơn giản.*
  * **Đường Cơ Sở Không AI:** Thiết lập một đường cơ sở thủ công hoặc dựa trên quy tắc trước khi thử nghiệm AI.*
  * **Mua / Xây dựng / Thúc đẩy:** Ba con đường để tích hợp AI (Sẵn có, Tùy chỉnh, hoặc Tăng cường các quy trình hiện tại).*
  * **Danh Sách Kiểm Tra Mức Độ Sẵn Sàng Của AI:** 5 tiêu chí (dữ liệu, số đo, dung sai thất bại, độ sẵn sàng của người dùng, tài nguyên). Dưới 3 CÓ nghĩa là "Chưa".*
  * **Các Mẫu Vá Lỗi UX:** Các thiết kế UX để bù đắp cho những điểm yếu của AI (ví dụ: hộp thoại xác nhận, đề xuất nội tuyến, trích xuất nguồn).*

*### Các Bộ Khung Bên Ngoài*
  * **Sổ Tay Google PAIR:** Hướng dẫn cho thiết kế AI có trách nhiệm, tập trung vào nhu cầu người dùng và điểm mạnh của AI.*
  * **Bộ Công Cụ Microsoft HAX:** 18 nguyên tắc cho tương tác Con Người - AI.*
  * **Khung Quản Lý Rủi Ro AI Của NIST:** Lập bản đồ và đo lường rủi ro của tổ chức.*
  * **Các Quy Tắc Của Google Về Học Máy:** 43 quy tắc thực tế cho kỹ thuật Học Máy, đặc biệt là xoay quanh heuristics (các quy tắc suy nghiệm).*

*## 2. Các Nghiên Cứu Tình Huống (Case Studies)*
  * **Google Flu Trends:** Bài học về việc định hình vấn đề có thiếu sót và phụ thuộc vào các số đo đại diện (proxy metrics).*
  * **Google Photos:** Quyết định *không* dùng AI cho các bộ lọc ảnh vì các heuristics dựa trên quy tắc đã đủ tốt.*
  * **Stripe AI:** Sử dụng LLMs cho việc tóm tắt báo cáo nội bộ, phụ thuộc nhiều vào việc review của Giám Đốc Sản Phẩm (AI đóng vai trò như Boost/Thúc đẩy).*
  * **GitHub Copilot & Gmail Smart Compose:** Minh chứng cho mẫu UX "ghost text" (chỉ đề xuất, người dùng quyết định).*
  * **Grammarly:** Phản hồi AI nội tuyến, trong đó AI làm nổi bật nhưng không tự động thay đổi văn bản.*

*## 3. Danh Sách Đọc*
  * **Kỹ Thuật AI:** "Xây Dựng Các Ứng Dụng LLM Để Đưa Lên Production" bởi Chip Huyen.*
  * **Kiến Trúc Hệ Thống:** "Các Kiến Trúc Mới Nổi Cho Các Ứng Dụng LLM" bởi a16z; "Nợ Kỹ Thuật Ẩn Trong Các Hệ Thống Học Máy" bởi Sculley và cộng sự.*
  * **Quản Lý Sản Phẩm:** "Inspired" bởi Marty Cagan (Tư duy ưu tiên vấn đề); "Chọn Số Đo Sao Bắc Đẩu Của Bạn" bởi Lenny Rachitsky.*
  * **Agents:** "Xây Dựng Các Agent Hiệu Quả" của Anthropic (nhấn mạnh các mẫu có khả năng lắp ráp (composable patterns) hơn là các framework phức tạp) và Hướng Dẫn Thực Hành Của OpenAI.*

*## 4. Các Nguyên Tắc Cốt Lõi (Tham Khảo Nhanh)*
   *"Ưu tiên vấn đề, không phải ưu tiên AI."*
   *Mô hình chỉ chiếm 10-20% công việc; dữ liệu, UX, và vận hành chiếm 80-90%.*
   *"Giải pháp đi tìm vấn đề" là kiểu thất bại AI phổ biến nhất.*
   *Xây dựng một đường cơ sở trước.*
   *Độ chính xác 85% với UX tốt > độ chính xác 95% với UX tệ.*
   *"Chưa" không phải là một sự thất bại; nó thể hiện sự trưởng thành.*
   *Sử dụng UX để vá lỗi ở những nơi AI thiếu sót.*
   *AI là một sự Thúc đẩy, không phải là sự Thay thế.*
