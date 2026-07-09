---
type: summary
title: "Summary: Day 27 Track 1 - Stakeholder Management & AI Team Performance"
description: "A summary of stakeholder management, communication, RACI matrix, AI team structure, and high-performance operations for AI projects."
tags: [stakeholder-management, ai-team, raci, agentic-sdlc, product-management]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/27/Day25_track1_aithucchien_cohort2.pdf"]
---
# Ngày 27 Track 1 - Quản lý các Bên liên quan & Hiệu suất Nhóm AI  

Tài liệu này tóm tắt bài giảng Ngày 27 Track 1 về các yếu tố con người trong các dự án AI, bao gồm quản lý các bên liên quan, giao tiếp hiệu quả, cấu trúc nhóm và các hoạt động hiệu suất.

## 1. Quản lý các Bên liên quan  

A good AI product can fail if the human element is not managed properly (e.g., IBM Watson Health at MD Anderson failed due to overpromising sales and neglecting doctors, the core blockers). Stakeholders must be mapped early using a 4-quadrant diagram based on **Influence** (Ảnh hưởng) and **Interest** (Quan tâm):  
Một sản phẩm AI tốt có thể thất bại nếu yếu tố con người không được quản lý hợp lý (ví dụ: IBM Watson Health tại MD Anderson thất bại do bán hàng hứa hẹn quá mức và bỏ qua các bác sĩ, những người cản trở cốt lõi). Các bên liên quan phải được lập bản đồ sớm bằng cách sử dụng sơ đồ 4 góc phần tư dựa trên **Influence** (Ảnh hưởng) và **Interest** (Quan tâm):

- ***Blockers (Kẻ cản trở - Ảnh hưởng cao, Quan tâm thấp):** ví dụ: Nhà đầu tư, đối tác lớn. Chiến lược: Thuyết phục, giảm thiểu rủi ro sớm, giải quyết các mối quan tâm trước khi họ hỏi.*  
- ***Champions (Nhà vô địch - Ảnh hưởng cao, Quan tâm cao):** ví dụ: Giảng viên, nhà đầu tư cam kết. Chiến lược: Duy trì sự gắn kết, tận dụng các nguồn lực và mạng lưới của họ.*  
- ***Bystanders (Người ngoài cuộc - Ảnh hưởng thấp, Quan tâm thấp):** ví dụ: Các thành viên trong nhóm không liên quan. Chiến lược: Theo dõi và thông báo định kỳ.*  
- ***Supporters (Người ủng hộ - Ảnh hưởng thấp, Quan tâm cao):** ví dụ: Khách hàng dùng thử. Chiến lược: Trao quyền cho họ, thu thập phản hồi, biến họ thành những người ủng hộ.*  

## 2. Giao tiếp và Ma trận RACI  

### Nguyên tắc "Kết luận trước"  

Các bên liên quan khác nhau lắng nghe những điều khác nhau (Nhà đầu tư: Tỷ suất hoàn vốn; Giảng viên: tính khả thi/rủi ro; Khách hàng: lợi ích). Luôn bắt đầu bằng kết luận, sau đó là lý do và dữ liệu. **Nghiên cứu điển hình:** Klarna đã hứa hẹn quá mức về khả năng của AI, dẫn đến sự không hài lòng của khách hàng khi chất lượng giảm sút.

### Xử lý Phản đối  

- ***"Quá rủi ro"**: Đề xuất các dự án thí điểm nhỏ, thiết kế có sự tham gia của con người (human-in-the-loop).*  
- ***"Không đáng chi phí"**: Chỉ ra chi phí cơ hội của việc không thực hiện nó.*  
- ***"Tôi không tin tưởng AI"**: Cung cấp các bản demo thực tế và các nghiên cứu điển hình.*  
- ***"Để tôi suy nghĩ đã"**: Đề xuất một hành động nhỏ, cụ thể (yêu cầu nhỏ).*  

### Ma trận RACI  

Một công cụ quan trọng để phân công công việc trong dự án AI:

- ***R (Responsible - Trách nhiệm):** Người thực hiện công việc.*  
- ***A (Accountable - Giải trình):** Người ra quyết định cuối cùng (Chỉ được phép có ĐÚNG MỘT người cho mỗi nhiệm vụ).*  
- ***C (Consulted - Tham vấn):** Cung cấp thông tin *trước khi* quyết định.*  
- ***I (Informed - Thông báo):** Được thông báo *sau khi* quyết định.*  

## 3. Cấu trúc Nhóm AI & Vai trò  

### Các Vai trò đang Tiến hóa  

Vai trò của **Kỹ sư Triển khai Tiền tuyến (Forward Deployed Engineer - FDE)** là rất quan trọng—những kỹ sư gắn kết với khách hàng để tích hợp AI vào các quy trình làm việc hiện có (ví dụ: Anthropic, Palantir). Một **Giám đốc Sản phẩm AI (AI Product Manager)** khác với PM truyền thống ở chỗ họ quản lý sự không chắc chắn, đánh giá mô hình (độ chính xác/độ phủ, ảo giác) và các quy trình làm việc có sự tham gia của con người.

### Kiến trúc Nhóm  

- ***Tập trung (Centralized):** Một nhóm AI cốt lõi phục vụ toàn bộ công ty (dễ chia sẻ kiến thức, nhưng có thể bị tắc nghẽn).*  
- ***Nhúng (Embedded):** Kỹ sư AI tham gia vào các nhóm sản phẩm (nhanh chóng, thực tế, nhưng khó duy trì tính nhất quán).*  
- ***Lai (Hub-and-Spoke - Trục và Nan hoa):** Trục trung tâm cho các công cụ, nan hoa nhúng cho việc thực thi sản phẩm.*  
- ***Mô hình Đội ngũ (Kiểu Spotify):** Các nhóm tự trị, liên chức năng sở hữu toàn bộ vòng đời sản phẩm AI.*  

## 4. Các Hoạt động của Nhóm AI Hiệu suất cao  

### Vòng đời Phát triển Phần mềm (SDLC) Tác tử  

Các tác tử AI hiện tham gia vào toàn bộ Vòng đời Phát triển Phần mềm (SDLC):

- ***Lập kế hoạch (Planning):** Con người thiết lập ý định; tác tử lập kế hoạch. Lập kế hoạch đúng lúc (Just-in-time) thay thế cho lộ trình 6 tháng.*  
- ***Lập trình & Kiểm thử (Coding & Testing):** Tác tử viết mã và tự kiểm thử; con người đóng vai trò là người đánh giá.*  
- ***Đánh giá (Review):** "Tin tưởng nhưng phải xác minh". Con người tập trung vào bảo mật, pháp lý và UX (Trải nghiệm người dùng).*  

### Khung Năng lực  

- ***L1 (Hiểu biết AI):** Sử dụng các công cụ AI để tăng tốc công việc cá nhân.*  
- ***L2 (Người thực hành AI):** Xây dựng các tính năng AI đơn giản (RAG, tích hợp API).*  
- ***L3 (Người xây dựng AI):** Thiết kế các hệ thống đa tác tử phức tạp và các khuôn khổ quản trị.*  

### An toàn Tâm lý  

Yếu tố quan trọng nhất đối với một nhóm AI là an toàn tâm lý (Dự án Aristotle). Các nhóm phải cảm thấy an toàn để thử nghiệm, thất bại và lên tiếng, vì các mô hình AI vốn dĩ có tính không chắc chắn.

---

### *Câu hỏi ôn tập Ngày 27*

   Trong mô hình 4 góc phần tư quản lý stakeholders, nhóm nào có **Chiến lược: Thuyết phục, giảm thiểu rủi ro từ sớm, giải quyết mối quan tâm trước khi họ hỏi**?
     A. Người ủng hộ
     B. Người cản trở
     C. Người hỗ trợ
     D. Người đứng ngoài
   **Answer / Đáp án:** B

   Trong ma trận RACI, thành viên nào phải là **duy nhất một người cho mỗi nhiệm vụ** và chịu trách nhiệm quyết định cuối cùng?
     A. Người thực hiện
     B. Người chịu trách nhiệm
     C. Người được tham vấn
     D. Người được thông báo
   **Answer / Đáp án:** B

   Nguyên tắc **"Kết luận trước"** khi giao tiếp với stakeholders yêu cầu điều gì?
     A. Đưa ra tất cả dữ liệu trước, sau đó mới kết luận
     B. Bắt đầu bằng kết luận, sau đó đưa ra lý do và dữ liệu
     C. Chỉ trình bày kết luận khi được hỏi
     D. Tập trung vào chi tiết kỹ thuật trước
   **Answer / Đáp án:** B

   Yếu tố nào được Project Aristotle xác định là **quan trọng nhất** cho một nhóm AI hiệu quả?
     A. Cấu trúc nhóm Hybrid (Hub-and-Spoke)
     B. Năng lực L3 (AI Builder)
     C. An toàn tâm lý (Psychological Safety)
     D. Áp dụng Agentic SDLC
   **Answer / Đáp án:** C
