---
type: summary
title: "Memory Systems for Agents (Track 3)"
description: "Summary of Day 17 Track 3 on designing memory systems for AI agents, including Short-term, Long-term, Episodic, and Semantic memory."
tags: [AI_20K_2A202600974, Day17, AI_Agents, Memory]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/17/Day17 - Track 3 - Memory-systems-for-agents.pdf"]
---

*# Hệ thống Bộ nhớ cho Tác nhân (Ngày 17 - Track 3)*


*Track này giải quyết một thách thức lớn khi triển khai các tác nhân AI: các tác nhân mặc định là không trạng thái và "quên" thông tin giữa các phiên. Một hệ thống bộ nhớ mạnh mẽ kết hợp khả năng truy cập nhanh của cửa sổ ngữ cảnh với lưu trữ bền vững của các cơ sở dữ liệu bên ngoài.*


*## 4 Loại Bộ nhớ Nhận thức cho Tác nhân*


1.  ***Bộ nhớ Ngắn hạn (Làm việc):** Được quản lý trong cửa sổ ngữ cảnh của LLM. Nhanh, tạm thời và bị giới hạn bởi ngân sách token. Quản lý tốt nhất thông qua chiến lược cửa sổ trượt (lời nhắc hệ thống + tóm tắt + K lượt gần nhất) để tránh chạm giới hạn token.*


2.  ***Bộ nhớ Dài hạn (Tuyên bố):** Bền vững qua các phiên, lưu trữ hồ sơ người dùng, sở thích và sự kiện (ví dụ: sử dụng Redis). Thông tin được nạp vào lời nhắc hệ thống khi một phiên mới bắt đầu.*


3.  ***Bộ nhớ Tình tiết:** Nhật ký tuần tự về các trải nghiệm và suy ngẫm trong quá khứ (ví dụ: "Tôi đã thử cách tiếp cận X và nó thất bại vì Y"). Hữu ích cho việc học hỏi từ các quỹ đạo trong quá khứ.*


4.  ***Bộ nhớ Ngữ nghĩa:** Kiến thức miền được mã hóa thành các embedding và lưu trữ trong Cơ sở dữ liệu Vector. Các tác nhân truy xuất các sự kiện liên quan thông qua tìm kiếm tương tự cosine.*


*## Triển khai & Khung công tác*


- ***Luồng Quản lý Bộ nhớ:** Bộ đệm (Cửa sổ Ngữ cảnh) -> Tóm tắt (gọi LLM) -> Trích xuất Sự kiện Chính -> Lưu trữ Bền vững (Kho lưu trữ Bên ngoài như Redis hoặc Chroma).*


- ***Tích hợp LangGraph:** Các nút chuyên biệt để nạp bộ nhớ (`retrieve_memory`) và lưu bộ nhớ.*


- ***Khung công tác:** Mem0 và Zep cung cấp các lớp bộ nhớ được quản lý với tự động phân loại và truy xuất thông minh, nhưng việc triển khai tùy chỉnh mang lại nhiều quyền kiểm soát hơn.*


- ***Quyền riêng tư theo Thiết kế:** Rất quan trọng cho bộ nhớ tác nhân. Bao gồm tối thiểu hóa dữ liệu, giới hạn lưu trữ TTL và các cơ chế cho "Quyền được Lãng quên".*


*## Xu hướng về Bộ nhớ Tác nhân (2025-2026)*


1.  ***Bộ nhớ xuyên phiên:** Chuyển từ lịch sử phạm vi luồng sang hồ sơ phạm vi người dùng và kho lưu trữ tình tiết.*


2.  ***Nén:** Thay vì giữ lại toàn bộ bản ghi, các tác nhân nén các phiên thành các bản tóm tắt, quyết định và ghi chú bền vững để bảo toàn ngân sách token và cải thiện độ chính xác.*


3.  ***Tệp Danh tính:** Sử dụng các tệp cấu hình như `AGENTS.md` và `SOUL.md` làm mặt phẳng điều khiển cho danh tính và quy tắc của tác nhân, tách biệt khỏi bộ nhớ truy xuất.*


4.  ***Vòng lặp Nhịp tim:** Các tác nhân thức dậy định kỳ ở chế độ nền để làm mới trạng thái, dọn dẹp ghi chú và xử lý các công việc tồn đọng.*


5.  ***Cơ sở Kiến thức Biên dịch (Wiki LLM):** Thay vì RAG thô trên các tài liệu, LLM liên tục quản lý và chỉnh sửa một "wiki" về các khái niệm, thực thể và dòng thời gian, giải quyết vấn đề các truy vấn RAG lặp đi lặp lại trên cùng một kho ngữ liệu.*
