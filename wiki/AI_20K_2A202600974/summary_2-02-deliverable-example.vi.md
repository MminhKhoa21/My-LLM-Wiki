---
type: summary
title: "Summary: Day 02 Deliverable Example"
description: "A summary of the Day 02 lab deliverable example detailing problem discovery, workflow mapping, and AI decision making."
tags: [Lab Example, Workflow, Problem Statement, Delivery]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/2-02-deliverable-example.pdf"]
---
Dưới đây là nội dung file đã được chuyển đổi sang song ngữ Anh - Việt, giữ nguyên định dạng Markdown. Tiếng Anh được đặt trước, tiếp theo là bản dịch tiếng Việt in nghiêng.

---

# *Tóm tắt: Ví dụ về Sản phẩm chuyển giao Ngày 02*

## *Tổng quan*


Tài liệu này cung cấp một ví dụ hoàn chỉnh về bài tập thực hành Ngày 02. Nó đi qua hành trình của một Giám đốc Sản phẩm Tập sự (Junior Product Manager) tên là Minh khi anh thực hiện rà soát vấn đề, thiết kế quy trình làm việc hiện tại và tương lai, phác thảo Tuyên bố Vấn đề (Problem Statement) và cuối cùng quyết định triển khai giải pháp Quy trình AI (AI Workflow) để tự động hóa các báo cáo hàng tuần.

## *Các Giai đoạn Chính*

### *Giai đoạn 1: Rà soát Vấn đề Cá nhân*

  
  Minh liệt kê các điểm nghẽn (pain points) hàng ngày khác nhau bằng cách sử dụng nhiều góc nhìn khác nhau (các tác vụ lặp đi lặp lại, các tác vụ tốn thời gian, các lĩnh vực mà AI có thể xuất sắc và những khó khăn mà người khác gặp phải).
  
  
  Các ví dụ bao gồm tóm tắt Jira/Slack cho báo cáo hàng tuần, xem xét PRD, tìm kiếm trên Slack các quyết định trong quá khứ và viết biên bản cuộc họp.
  
  
  ***Các Ứng viên Hàng đầu Được Chọn:** Báo cáo Hàng tuần, Đánh giá PRD và Tìm kiếm trên Slack.*

### *Giai đoạn 2: Tuyên bố Vấn đề Nhóm (Sự hội tụ)*

  
  Nhóm tổng hợp các ý tưởng cá nhân và chấm điểm chúng dựa trên tính rõ ràng của chủ thể (actor), quy trình làm việc, bằng chứng về điểm nghẽn, tác động có thể đo lường, tính khả thi trong thực hành và hiểu biết về lĩnh vực.
  
  
  ***Vấn đề Được Chọn:** "Báo cáo Hàng tuần" được chọn vì nó có quy trình làm việc có cấu trúc cao, một số liệu cơ sở rõ ràng (90 phút) và tác động dễ dàng đo lường.*

### *Giai đoạn 3: Xác thực và Nghiên cứu*

  
  Nhóm xác thực ngắn gọn vấn đề với các PM khác. Họ nhận ra rằng khó khăn thực sự không chỉ là "rút trích các con số" mà là viết *bài tường thuật* (narrative) từ dữ liệu thô.
  
  
  Họ nghiên cứu các công cụ hiện có (ví dụ: Báo cáo Jira, Slack AI, Gemini trong Drive) để hiểu các mô hình hiện tại. Bài học rút ra là AI nên hỗ trợ soạn thảo tường thuật trong khi con người vẫn giữ quyền kiểm soát việc đánh giá.

### *Giai đoạn 4: Lập bản đồ Quy trình làm việc*

  
  ***Trạng thái Hiện tại (90 phút):** Xuất Jira -> Lấy bảng tính -> Đọc Slack -> Tổng hợp -> Viết Tường thuật (Nút thắt) -> Định dạng -> Gửi.*
  
  
  ***Trạng thái Tương lai (21 phút):** Tự động kéo dữ liệu (Theo quy tắc) -> Cấu trúc dữ liệu (Quy trình/AI) -> Soạn thảo tường thuật (Quy trình/AI) -> PM Xem xét & Chỉnh sửa (Ranh giới Con người) -> Gửi.*
  
  
  ***Tác động:** Giảm đáng kể tổng thời gian trong khi vẫn duy trì chất lượng thông qua việc đánh giá thủ công.*

### *Giai đoạn 5: Tuyên bố Vấn đề và Quyết định*

  
  ***Tuyên bố Vấn đề:** Định nghĩa chủ thể (Junior PM), quy trình làm việc, nút thắt (viết tường thuật), tác động, chỉ số thành công (tổng cộng dưới 30 phút) và các ranh giới nghiêm ngặt.*
  
  
  ***Quyết định AI:***
  
    
    ***Quy tắc (Rule):** Không đủ vì nó không thể tạo ra các tường thuật động.*
    
    
    ***Quy trình (Workflow):** Được chọn. Quá trình tuyến tính trong đó AI hỗ trợ đặc biệt trong việc soạn thảo, với sự xem xét của PM.*
    
    
    ***Tác nhân (Agent):** Bị từ chối. Quá rộng, quyền tự chủ không cần thiết và rủi ro cao hơn.*
    
  
  ***Quyết định Cuối cùng:** **Triển khai (Go)** với một dự án thí điểm nhỏ sử dụng dữ liệu báo cáo lịch sử để đánh giá thời gian chỉnh sửa và tỷ lệ ảo giác của AI.*

### *Giai đoạn 6: Suy ngẫm Cá nhân*

  
  Phản ánh về việc sử dụng AI trong quá trình thực hành (ví dụ: tạo sơ đồ mermaid, lên ý tưởng) và sửa lỗi cho AI khi nó đề xuất các giải pháp Tác nhân (Agent) quá phức tạp một cách vội vàng.
  
  
  Nhấn mạnh rằng những vấn đề tốt nhất có quy trình làm việc và các chỉ số đo lường rõ ràng, và các tác nhân không phải là câu trả lời mặc định.
