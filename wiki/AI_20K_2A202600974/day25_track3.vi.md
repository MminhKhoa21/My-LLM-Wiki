---
type: summary
title: "Circuit Breakers, Caching & Reliability for Production Agents"
description: "Summary of Day 10 on reliability primitives including failure modes, circuit breakers, caching, observability, and chaos testing for production LLM agents."
tags: [reliability, circuit breaker, caching, observability, slo, chaos testing, llm agents]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/25/day10_reliability_student.pdf"]
---
*# Bộ ngắt mạch, Bộ nhớ đệm và Độ tin cậy cho các tác nhân sản xuất*

*Tài liệu này tóm tắt nội dung từ phiên AICB-P2T3 Ngày 10 về các khái niệm sẵn sàng sản xuất cho tác nhân, tập trung vào các nguyên tắc cơ bản về độ tin cậy.*

*## 1. Các dạng lỗi*

*Độ tin cậy bắt đầu bằng việc đặt tên chính xác các lỗi. 6 dạng lỗi phổ biến cần theo dõi trong các tác nhân LLM sản xuất là:*

    *Dịch: **Lỗi tạm thời của nhà cung cấp**: Các lỗi như 429 (Giới hạn tốc độ), 500 (Lỗi máy chủ nội bộ) hoặc hết thời gian chờ.*
    *Dịch: **Độ trễ suy giảm**: Sự gia tăng đột ngột của độ trễ P95.*
    *Dịch: **Ngừng hoạt động hoàn toàn**: Nhà cung cấp ngừng phản hồi hoàn toàn.*
    *Dịch: **Vòng lặp điều phối**: Các lỗi liên quan đến trạng thái hoặc thử lại không chính xác.*
    *Dịch: **Lỗi công cụ/bộ nhớ đệm**: Các vấn đề như bộ nhớ đệm lỗi thời, lược đồ không chính xác hoặc lỗi xác thực.*
    *Dịch: **Hành động kinh doanh sai**: Các hành động kinh doanh không chính xác với các tác dụng phụ không thể hoàn tác.*

*### Suy giảm thầm lặng*

*Một hệ thống có thể suy giảm mà không có lỗi rõ ràng (ví dụ: tỷ lệ lỗi = 0%). Điều này xảy ra khi:*

  *Nhà cung cấp cập nhật mô hình một cách thầm lặng.*
  *Prompt/lược đồ thay đổi nhưng việc đánh giá thì không.*
  *Cơ sở tri thức trở nên lỗi thời hoặc khả năng truy xuất suy yếu.*
  *Bộ nhớ đệm trả về câu trả lời trước đây đúng nhưng hiện tại sai.*

*## 2. Bộ ngắt mạch & Dự phòng*

*Một **Bộ ngắt mạch** dừng các cuộc gọi đến nhà cung cấp đang gặp lỗi, trong khi một chuỗi **Dự phòng** duy trì trải nghiệm người dùng ở mức chấp nhận được.*

*### 3 Trạng thái của Bộ ngắt mạch*

  *Dịch: **ĐÓNG**: Các cuộc gọi bình thường được tiến hành.*
  *Dịch: **MỞ**: Thất bại nhanh. Chuyển từ ĐÓNG khi ngưỡng lỗi đạt đến.*
  *Dịch: **NỬA-MỞ**: Cuộc gọi thăm dò để kiểm tra xem nhà cung cấp đã phục hồi chưa. Chuyển từ MỞ sau thời gian chờ đặt lại. Chuyển lại thành ĐÓNG nếu thành công, hoặc MỞ nếu thất bại.*

*### Thang dự phòng (Suy giảm có kiểm soát)*

*Một chính sách dự phòng điển hình:*

    *Dịch: **Mô hình tốt nhất** (Chất lượng cao nhất)*
    *Dịch: **Nhà cung cấp dự phòng** (Cùng bộ tính năng)*
    *Dịch: **Mô hình rẻ hơn/nhỏ hơn** (Chất lượng hạn chế)*
    *Dịch: **Phản hồi được lưu trong bộ nhớ đệm***
    *Dịch: **Tin nhắn dự phòng tĩnh***

*Lưu ý: Tính tương thích của tính năng (chế độ JSON, gọi công cụ, độ dài ngữ cảnh, độ trễ/chi phí, hành vi chính sách) phải được kiểm tra khi chuyển sang mô hình yếu hơn.*

*## 3. Bộ nhớ đệm & Ngân sách chi phí*

*Bộ nhớ đệm thích hợp giảm độ trễ và chi phí; bộ nhớ đệm không phù hợp gây ra câu trả lời lỗi thời và ảo giác ổn định.*

*### 3 Lớp bộ nhớ đệm cho các ứng dụng LLM*

    *Dịch: **Bộ nhớ đệm prompt/tiền tố của nhà cung cấp**: Giảm chi phí khi các tiền tố dài được tái sử dụng.*
    *Dịch: **Bộ nhớ đệm phản hồi ngữ nghĩa của ứng dụng**: Tái sử dụng các phản hồi cho các truy vấn tương tự về mặt ngữ nghĩa.*
    *Dịch: **Bộ nhớ đệm công cụ/kết quả**: Lưu trữ các kết quả API/DB đắt tiền nhưng xác định.*

*### Luồng bộ nhớ đệm ngữ nghĩa*

  *Dịch: **TRÚNG**: `độ tương tự > ngưỡng` -> Trả về bộ nhớ đệm.*
  *Dịch: **TRƯỢT**: `độ tương tự < ngưỡng` -> Gọi LLM -> Lưu trữ kết quả.*
*Cảnh báo: Nhiễm độc bộ nhớ đệm xảy ra khi hai truy vấn rất gần nhau về độ tương tự cosine nhưng có ý định khác nhau. Theo dõi tỷ lệ trúng và tỷ lệ trúng giả.*

*### Ngân sách chi phí*

*Kiểm soát chi phí ở 3 lớp:*

    *Dịch: Giới hạn mỗi yêu cầu (tối đa token, tối đa công cụ, thời gian chờ).*
    *Dịch: Giới hạn tốc độ mỗi người dùng/ứng dụng (bucket token).*
    *Dịch: Ngân sách hàng tháng (cảnh báo ở 80%, dừng cứng/chuyển hướng đến mô hình rẻ hơn ở 100%).*

*## 4. Khả năng quan sát & SLO*

*Nếu không có giám sát, không thể biết liệu hệ thống có tốt, chậm, đắt đỏ hay đang trả về câu trả lời không chính xác hay không.*

  *Dịch: **SLI (Chỉ báo mức dịch vụ)**: Số liệu được đo (ví dụ: tính khả dụng, độ trễ P95, tỷ lệ trúng bộ nhớ đệm).*
  *Dịch: **SLO (Mục tiêu mức dịch vụ)**: Mục tiêu nội bộ (ví dụ: khả dụng >= 99%, P95 < 2.5s, thành công dự phòng >= 95%).*
  *Dịch: **SLA (Thỏa thuận mức dịch vụ)**: Cam kết bên ngoài (ví dụ: thời gian hoạt động 99.5%/tháng cho các API hướng tới khách hàng).*
  *Dịch: **Ngân sách lỗi**: Tỷ lệ lỗi được phép trước khi hành động được thực hiện (ví dụ: đóng băng các tính năng để ưu tiên độ tin cậy).*

*Lưu ý: Các tác nhân LLM yêu cầu SLO chất lượng ngoài SLO thời gian hoạt động (ví dụ: tính trung thực, tỷ lệ vượt qua an toàn, tính chính xác của việc leo thang).*

*## 5. Phòng thí nghiệm: Kỹ thuật độ tin cậy*

*Phòng thí nghiệm liên quan đến việc xây dựng một cổng độ tin cậy thực hiện:*

  *Bộ ngắt mạch + bộ nhớ đệm ngữ nghĩa/công cụ*
  *Công cụ đo lường số liệu (JSON/CSV)*
  *Kiểm tra hỗn loạn và báo cáo*

***Các kịch bản kiểm tra hỗn loạn:** *

  *Nhà cung cấp chính hết thời gian chờ 100%.*
  *Nhà cung cấp chính gián đoạn 50%.*
  *Bộ nhớ đệm trả về ứng viên lỗi thời.*
  *Giới hạn chi phí gần như đạt đến.*

*Bằng chứng dự kiến bao gồm các số liệu cho thấy bộ ngắt mạch chuyển đổi (ĐÓNG -> MỞ), cổng chuyển hướng đến dự phòng mà không có bão thử lại, và thời gian phục hồi được ghi lại.*
