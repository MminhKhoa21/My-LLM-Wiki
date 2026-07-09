---
type: summary
title: "Summary: Day 02 Lecture Slides v2 (Part 2)"
description: "A summary of the alternative version of Day 02 lecture slides on defining AI problems and workflows."
tags: [AI Problem, Double Diamond, Workflow, Problem Statement]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/6-day02-lecture-slides-v2.pdf"]
---
# Tóm tắt: Bài giảng Ngày 02 Slides v2 (Phần 2)

## Tổng quan

Tài liệu này tóm tắt bài giảng Ngày 02 slides (phiên bản 6), phản ánh chương trình cốt lõi về việc xác định các bài toán AI, cấu trúc các Tuyên bố Vấn đề (Problem Statements), và xác định mức độ tích hợp AI phù hợp. Nó củng cố quá trình chuyển đổi từ những ý tưởng mơ hồ sang các quy trình làm việc (workflows) cụ thể.

## Các Khái Niệm Chính

### Nền Tảng Của Sản Phẩm AI
Một sản phẩm AI được xây dựng trên ba trụ cột:
   1. **Kỹ Thuật AI:** Triển khai mô hình, RAG, các agent (tác tử), và đánh giá.
   2. **Tư Duy Sản Phẩm:** Xác định đúng vấn đề và hiểu giá trị đối với người dùng (Inspired).
   3. **Tư Duy Thiết Kế:** Thiết kế cho các mô hình tinh thần, phản hồi, và xử lý lỗi một cách tinh tế.

### Mô Hình Kim Cương Kép & HCD (Thiết Kế Lấy Con Người Làm Trung Tâm)
  - **Kim Cương Kép:** Tập trung vào việc khám phá vấn đề thực sự trước khi thu hẹp vào một giải pháp. Một giải pháp tuyệt vời cho sai vấn đề là vô dụng.
  - **Thiết Kế Lấy Con Người Làm Trung Tâm (HCD):** Nhấn mạnh sự quan sát, lên ý tưởng, làm nguyên mẫu, thử nghiệm, và lặp lại liên tục.

### Định Hình Vấn Đề
  - Xác định đúng vấn đề liên quan đến việc tìm kiếm các tác vụ lặp đi lặp lại, tốn thời gian, hoặc có lợi thế rõ ràng khi áp dụng AI.
  - Tránh các anti-pattern như "Giải pháp trước" (xây dựng trước khi hiểu rõ quy trình làm việc) và "Không có đường cơ sở" (thất bại trong việc đo lường chi phí vận hành hiện tại).
  - **Phỏng Vấn Các Bên Liên Quan:** Đặt các câu hỏi về quy trình làm việc hiện tại, điểm nghẽn, chi phí của các lỗi sai, và các số đo thành công.

### Các Thành Phần Của Tuyên Bố Vấn Đề
Tuyên bố Vấn đề được cấu trúc yêu cầu:
  - **Chủ Thể** và **Quy Trình Làm Việc**
  - **Điểm Nghẽn** và **Tác Động**
  - **Các Số Đo Thành Công** (Đường cơ sở, Mục tiêu, Phương pháp đo lường)
  - **Phạm Vi**, **Điểm Can Thiệp AI**, và **Rủi Ro/HITL (Con Người Trong Vòng Lặp)**

### Khung Ra Quyết Định: Quy Tắc, Quy Trình, Agent
Chọn mức độ trừu tượng đơn giản nhất:
  - **Quy Tắc:** Logic tất định. Tốt nhất cho các tác vụ cứng nhắc, tuân thủ cao.
  - **Quy Trình:** AI hoạt động trong một quy trình được định nghĩa (ví dụ: tóm tắt, soạn thảo). Con người vẫn nắm quyền kiểm soát.
  - **Agent:** Tự lập kế hoạch và sử dụng công cụ. Chỉ sử dụng khi môi trường đòi hỏi sự thích ứng cao.

### Các Mẫu Quy Trình Làm Việc
  - Tuân theo các hướng dẫn của Anthropic cho các quy trình AI: Chuỗi Prompt, Định tuyến, Xử lý song song, Mô hình Điều phối - Công nhân, và Đánh giá - Tối ưu.
  - Luôn ưu tiên các quy trình đơn giản, được định nghĩa trước hơn là các agent hoàn toàn tự trị trừ khi điều sau là thực sự cần thiết.

### Đánh Giá và Quyết Định Tiếp Tục/Dừng Lại
  - Chuyển đổi Tuyên bố Vấn đề trực tiếp thành một Kế Hoạch Đánh Giá với các test case và ngưỡng được xác định.
  - Đưa ra quyết định đã được tính toán: **Go** (Tiếp tục: vấn đề rõ ràng, số đo khả thi), **Not Yet** (Chưa: cần chuẩn hóa dữ liệu/quy trình), hoặc **No-Go** (Dừng lại: AI không thêm giá trị hoặc rủi ro quá cao).
