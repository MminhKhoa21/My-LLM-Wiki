---
type: summary
title: "Summary: Day 02 Lecture Slides v2"
description: "A summary of the alternative version of Day 02 lecture slides on defining AI problems and workflows."
tags: [AI Problem, Double Diamond, Workflow, Problem Statement]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/5-day02-lecture-slides-v2.pdf", "raw/AI_20K_2A202600974/2/6-day02-lecture-slides-v2.pdf"]
---
# Tóm tắt: Bài giảng Ngày 02 v2  

## Tổng quan  

Tài liệu này tóm tắt các slide bài giảng Ngày 02 (phiên bản 5 và 6), phản ánh chương trình cốt lõi về việc xác định các vấn đề AI, cấu trúc Tuyên bố Vấn đề (Problem Statements) và xác định mức độ tích hợp AI phù hợp. Nó củng cố quá trình chuyển đổi từ những ý tưởng mơ hồ sang quy trình làm việc cụ thể.  

## Các Khái niệm Chính  

### Nền tảng của Sản phẩm AI  
Một sản phẩm AI được xây dựng trên ba trụ cột:  
   **Kỹ thuật AI:** Triển khai mô hình, RAG, các tác nhân (agents) và đánh giá.  
   **Tư duy Sản phẩm:** Xác định đúng vấn đề và hiểu giá trị đối với người dùng (Inspired).  
   **Tư duy Thiết kế:** Thiết kế cho các mô hình tinh thần, phản hồi và xử lý lỗi tinh tế.  

### Mô hình Kim cương Đôi (Double Diamond) & Thiết kế Lấy con người làm trung tâm (HCD)  
  **Kim cương Đôi:** Tập trung vào việc khám phá vấn đề *thực sự* trước khi thu hẹp vào một giải pháp. Một giải pháp tuyệt vời cho một vấn đề sai là vô dụng.  
  **Thiết kế Lấy con người làm trung tâm (HCD):** Nhấn mạnh vào quan sát, lên ý tưởng, tạo nguyên mẫu, thử nghiệm và lặp lại liên tục.  

### Hình thành Vấn đề  
  Xác định đúng vấn đề bao gồm việc tìm kiếm các tác vụ mang tính lặp đi lặp lại, tốn thời gian hoặc có lợi thế AI rõ ràng.  
  Tránh các phản mô hình (anti-patterns) như "Giải pháp đi trước" (xây dựng trước khi biết quy trình làm việc) và "Không có đường cơ sở" (không đo lường được chi phí hoạt động hiện tại).  
  **Phỏng vấn các bên liên quan:** Đặt câu hỏi về các quy trình làm việc hiện tại, các nút thắt, chi phí của các lỗi và các chỉ số thành công.  

### Các Thành phần của Tuyên bố Vấn đề  
Tuyên bố Vấn đề có cấu trúc yêu cầu:  
  **Chủ thể (Actor)** và **Quy trình làm việc (Workflow)**  
  **Nút thắt (Bottleneck)** và **Tác động (Impact)**  
  **Chỉ số Thành công** (Đường cơ sở, Mục tiêu, Đo lường)  
  **Ranh giới**, **Điểm can thiệp của AI**, và **Rủi ro/HITL (Con người trong vòng lặp)**  

### Khung Ra quyết định: Quy tắc, Quy trình, Tác nhân  
Chọn mức độ trừu tượng đơn giản nhất:  
  **Quy tắc (Rule):** Logic xác định. Tốt nhất cho các tác vụ cứng nhắc, tuân thủ cao.  
  **Quy trình (Workflow):** AI hoạt động trong một quy trình được xác định (ví dụ: tóm tắt, soạn thảo). Con người vẫn nắm quyền kiểm soát.  
  **Tác nhân (Agent):** Lập kế hoạch và sử dụng công cụ tự chủ. Chỉ sử dụng khi môi trường đòi hỏi khả năng thích ứng cao.  

### Các Mô hình Quy trình  
  Tuân theo các nguyên tắc của Anthropic đối với các quy trình AI: Chuỗi lời nhắc (Prompt Chaining), Định tuyến (Routing), Song song hóa (Parallelization), Điều phối viên-Người thực thi (Orchestrator-Workers) và Đánh giá viên-Trình tối ưu hóa (Evaluator-Optimizer).  
  Luôn ưu tiên các quy trình đơn giản hơn, được xác định trước so với các tác nhân hoàn toàn tự chủ trừ khi điều sau là hoàn toàn cần thiết.  

### Đánh giá và Quyết định Triển khai (Go/No-Go)  
  Chuyển đổi trực tiếp Tuyên bố Vấn đề thành một Kế hoạch Đánh giá với các trường hợp thử nghiệm và ngưỡng được xác định.  
  Đưa ra quyết định có tính toán: **Go** (vấn đề rõ ràng, chỉ số khả thi), **Not Yet** (cần chuẩn hóa dữ liệu/quy trình) hoặc **No-Go** (AI không mang lại giá trị nào hoặc rủi ro quá cao).
