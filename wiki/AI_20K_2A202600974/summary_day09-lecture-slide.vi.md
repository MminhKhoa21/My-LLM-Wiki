---
type: summary
title: "Summary: day09-lecture-slide"
description: "A detailed summary of the day09-lecture-slide.pdf document."
tags: [day09, multi-agent, lecture-slides]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/9/day09-lecture-slide.pdf"]
---

# Tóm tắt: AI in Action - Ngày 09 (Đa tác nhân & Tích hợp Hệ thống)

Tài liệu này tóm tắt các trang trình bày bài giảng Ngày 09 của khóa học "AI in Action", tập trung vào việc chuyển đổi từ một tác nhân đơn lẻ bị quá tải sang một hệ thống đa tác nhân mạnh mẽ với các vai trò rõ ràng, tận dụng các công cụ như LangGraph, MCP, và giao tiếp A2A.

## 1. Bối cảnh & Trường hợp Sử dụng
- **Trường hợp Sử dụng:** Trợ lý nội bộ cho CS (Thành công của Khách hàng - Customer Success) và bộ phận Hỗ trợ CNTT. Các tác vụ bao gồm xử lý các chính sách hoàn tiền (ví dụ: chính sách hoàn tiền trong 7 ngày), P1 SLA (Thỏa thuận Mức Dịch vụ cho sự cố ưu tiên cao), và các quy trình phê duyệt quyền truy cập.
- **Mục tiêu của Ngày 09:** Thêm một lớp điều phối (Người giám sát + Công nhân) vào đường ống RAG đã xây dựng ở Ngày 08. Nhấn mạnh các vai trò rõ ràng, khả năng truy xuất nguồn gốc và khả năng mở rộng.

## 2. Giới hạn của Các Tác nhân Đơn lẻ
Một tác nhân nguyên khối đơn lẻ có thể trở thành nút thắt cổ chai khi nó bị buộc phải lập kế hoạch, truy xuất, gọi công cụ, tổng hợp, giám sát và thử lại tất cả cùng một lúc. Các giới hạn cốt lõi là:
- **Nút thắt ngữ cảnh:** Kích thước câu lệnh phình to.
- **Đánh đổi sự chuyên môn hóa:** Khó để thực hiện tốt nhiều tác vụ khác nhau chỉ với một câu lệnh đơn lẻ.
- **Giới hạn tính song song:** Các tác vụ độc lập bị buộc phải chạy tuần tự.
- **Độ tin cậy:** Một lỗi định tuyến ngay từ đầu sẽ phá hỏng toàn bộ quy trình làm việc.
*Nguyên tắc chung:* Hệ thống đa tác nhân nên được sử dụng không chỉ để nghe cho ấn tượng, mà là để tách biệt logic và cải thiện khả năng quan sát hệ thống.

## 3. Các Mô hình Đa tác nhân
Bốn mô hình phổ biến đã được giới thiệu:
1. **Người giám sát - Công nhân (Supervisor-Worker):** Định tuyến rõ ràng, dễ truy xuất. (Trọng tâm của Ngày 09).
2. **Đường ống (Pipeline):** Luồng tuyến tính, tốt cho các SOP (Quy trình Vận hành Tiêu chuẩn) cố định.
3. **Tranh luận (Debate):** Nhiều góc nhìn để giảm thiểu điểm mù.
4. **Phân cấp (Hierarchical):** Khả năng mở rộng tuyệt vời cho các miền tách biệt.

### Đi sâu vào Mô hình Người giám sát - Công nhân
- **Người giám sát:** Chịu trách nhiệm đưa ra các quyết định định tuyến và theo dõi trạng thái. Nó *không* cần phải là tác nhân thông minh nhất; nó chỉ cần phân quyền một cách rõ ràng.
- **Công nhân:** Các tác nhân chuyên trách (ví dụ: Công nhân Truy xuất, Công nhân Công cụ/Chính sách, Công nhân Tổng hợp) với các kỹ năng hẹp, được xác định rõ.
- **Hợp đồng (Contracts):** Giao tiếp dựa trên các hợp đồng JSON rõ ràng (các tác vụ, các ràng buộc, đầu ra mong đợi, lỗi) giúp cho các công nhân có thể kiểm thử và thay thế được.

## 4. MCP (Giao thức Ngữ cảnh Mô hình) vs. A2A (Tác nhân-với-Tác nhân)
- **MCP (Kiến trúc Máy khách - Máy chủ):** Một giao diện tiêu chuẩn để kết nối các tác nhân với các khả năng bên ngoài (Công cụ, Tài nguyên, Câu lệnh) mà không cần lập trình tích hợp cứng (hard-coding).
  - *Công cụ:* Các hành động có tác dụng phụ (ví dụ: API của Zendesk, Jira).
  - *Tài nguyên:* Dữ liệu tĩnh (ví dụ: lược đồ, tài liệu).
  - *Câu lệnh:* Các hướng dẫn/mẫu được định nghĩa trước.
- **A2A:** Các tác nhân ủy thác tác vụ hoặc hợp tác với các tác nhân khác (ví dụ: Chuyển giao, Tìm kiếm Hợp tác, Tranh luận Đồng thời, Tự Sửa lỗi, Quyết định Chung).
- *Nguyên tắc chung:* Sử dụng MCP để lấy một khả năng hoặc thực thi một công cụ. Sử dụng A2A để giao một nhiệm vụ cho một vai trò thông minh khác.

## 5. LangGraph & Triển khai Điều phối
- **Các Thành phần Cốt lõi:** Nodes (ai hành động), Edges (đi đâu tiếp theo), State (hệ thống biết gì), Checkpointer (bộ nhớ/du hành thời gian), và Routing (logic quyết định).
- **HITL (Con người trong Vòng lặp):** Cực kỳ cần thiết cho các hành động có rủi ro cao (hoàn tiền, thay đổi quyền truy cập) hoặc các tình huống có độ tin cậy thấp. LangGraph hỗ trợ thêm các điểm dừng (breakpoints) để con người đánh giá.
- **Đồ thị con (Sub-graphs):** Chia nhỏ các luồng khổng lồ thành các đồ thị dạng mô-đun, có thể tái sử dụng dựa trên nhóm (ví dụ: `IT_Graph`, `Sales_Graph`).
- **Trạng thái (State) vs. Truyền Tin nhắn:** Sử dụng *trạng thái chia sẻ* để điều phối toàn bộ luồng và *hợp đồng tin nhắn* để giao nhiệm vụ xuyên qua ranh giới của các công nhân.

## 6. Tổng quan Bài thực hành
Học viên được kỳ vọng sẽ tái cấu trúc (refactor) RAG tác nhân đơn lẻ từ Ngày 08 thành một thiết lập điều phối đa tác nhân bao gồm:
1. **Tái cấu trúc đồ thị:** Thiết lập một luồng Người giám sát cơ bản.
2. **Xây dựng công nhân:** Các công nhân Truy xuất, Công cụ/Chính sách, và Tổng hợp.
3. **Thêm MCP:** Kết nối ít nhất một khả năng bên ngoài thực tế hoặc được mô phỏng.
4. **Theo dõi (Trace) & Tài liệu:** Cung cấp một bản theo dõi thực thi dễ đọc cho thấy logic định tuyến, đầu vào/đầu ra của node, và so sánh hiệu suất giữa tác nhân đơn lẻ và đa tác nhân.

## Điểm chính Rút ra
Đa tác nhân không chỉ đơn giản là có nhiều tác nhân hơn; mà là việc tách biệt các mối quan tâm để con đường suy luận của hệ thống có thể quan sát được, kiểm thử được và đáng tin cậy. Việc theo dõi (tracing) đúng cách là nền tảng cho trọng tâm của Ngày 10 về khả năng quan sát và các đường ống dữ liệu.
