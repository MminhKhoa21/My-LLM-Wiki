---
type: summary
title: "Day 20 Track 3: Multi-Agent Systems"
description: "Exploration of advanced multi-agent workflows, including Supervisor, Debate, and Parallel patterns, using frameworks like LangGraph."
tags: [day20, track3, multi-agent, langgraph, supervisor, debate, parallel-execution]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/20/day05-multi-agent-systems-student.pdf"]
---

# Day 20 Track 3: Hệ thống Đa tác tử


## 1. Tổng quan


Mô-đun này chuyển từ thiết lập tác tử đơn lẻ sang Hệ thống Đa tác tử. Trong khi các tác tử đơn lẻ xử lý tốt các tác vụ đơn giản, các kịch bản phức tạp đòi hỏi nhóm các tác tử chuyên biệt với vai trò riêng và trạng thái dùng chung. Tuy nhiên, việc thêm tác tử sẽ phát sinh chi phí bổ sung và thách thức về phối hợp.


## 2. Khi nào nên sử dụng Nhiều tác tử?


Bạn chỉ nên mở rộng sang kiến trúc đa tác tử nếu một tác tử đơn lẻ không thể đạt độ chính xác >80%. Ba động lực chính cho các hệ thống đa tác tử là:

  Chuyên môn hóa: Mỗi tác tử làm chủ một lĩnh vực cụ thể (ví dụ: Nhà nghiên cứu, Nhà phân tích, Người viết).

  Xử lý song song: Thực hiện các tác vụ con đồng thời để giảm độ trễ.

  Kiểm tra chéo: Sử dụng sự đồng thuận và phê bình để giảm hiện tượng ảo giác.


## 3. 5 Mẫu quy trình tác tử của Anthropic


Bắt đầu với mẫu đơn giản nhất và chỉ nâng cấp khi thực sự cần thiết về mặt đo lường.

   1. **Chuỗi Prompt:** Các thao tác tuần tự, đầu ra của bước này là đầu vào cho bước tiếp theo.

   2. **Định tuyến:** Phân loại đầu vào và chuyển hướng nó đến bộ xử lý chuyên biệt có năng lực nhất (giảm chi phí bằng cách gửi các truy vấn đơn giản đến mô hình nhỏ và các truy vấn khó đến mô hình lớn).

   3. **Song song:** Chia tác vụ thành các phần cho các tác tử song song, hoặc sử dụng bỏ phiếu giữa nhiều mô hình trên cùng một tác vụ.

   4. **Điều phối viên – Nhân viên (Giám sát):** Một LLM giám sát ủy thác các tác vụ cho các tác tử nhân viên và tổng hợp đầu ra của chúng.

   5. **Đánh giá – Tối ưu hóa:** Vòng lặp sinh-và-phê bình lặp đi lặp lại.


## 4. Mẫu Giám sát (Điều phối)

  Sử dụng **Kiến trúc Hub-Spoke** thường được triển khai qua LangGraph.

  Giám sát viên đóng vai trò như một bộ định tuyến, phân rã một tác vụ và quyết định nhân viên nào cần gọi và theo thứ tự nào.

  Trạng thái được quản lý thông qua `TypedDict` theo dõi `messages`, `next_worker`, `worker_results` và `final_answer`.

  Các chế độ lỗi: Vòng lặp định tuyến vô hạn hoặc lựa chọn nhân viên không chính xác (được giảm thiểu bằng cách đặt số lần lặp tối đa).


## 5. Tác tử Tranh luận (Cộng tác đối kháng)

  Nhiều tác tử tạo ra các câu trả lời độc lập và sau đó phê bình công việc của nhau.

  Một tác tử "Thẩm phán" tổng hợp câu trả lời cuối cùng.

  Sử dụng các mô hình không đồng nhất (ví dụ: GPT-4o, Claude, Gemini) tránh được "ảo tưởng tập thể" khi các mô hình được huấn luyện giống hệt nhau đồng thuận về thông tin sai lệch.

  Lợi ích/Đánh đổi: Giảm 15-25% hiện tượng ảo giác nhưng phải trả giá bằng độ trễ và chi phí tính toán cao gấp 2-3 lần. Tốt nhất nên dành cho các tác vụ có rủi ro cao, mơ hồ.


## 6. Thực thi Song song và Trạng thái Dùng chung

  Sử dụng thực thi Map-Reduce không đồng bộ (ví dụ: `asyncio.gather` trong Python hoặc LangGraph's Send API).

  Các tác tử phối hợp thông qua một bảng đen trung tâm (Trạng thái Dùng chung) hoặc thông qua hàng đợi truyền tin nhắn.

  Xử lý lỗi: Cần có các cơ chế timeout, thử lại, bộ ngắt mạch và hàng đợi thư chết để đảm bảo độ tin cậy trong sản xuất.


## 7. Các Framework Đa tác tử

  LangGraph: Tính linh hoạt cao, điều khiển bằng máy trạng thái, tốt nhất cho môi trường sản xuất có toàn quyền kiểm soát.

  CrewAI: Dựa trên vai trò và dễ thiết lập, tuyệt vời cho tạo mẫu nhanh.

  AutoGen: Trò chuyện nhóm và cộng tác hội thoại, mạnh về thực thi mã.




Lab tập trung vào xây dựng một hệ thống nghiên cứu 3 tác tử (Nhà nghiên cứu, Nhà phân tích, Người viết) sử dụng LangGraph. Sinh viên so sánh điểm chuẩn giữa tác tử đơn lẻ và hệ thống đa tác tử, đo lường độ chính xác, độ trễ và chi phí.

---

Câu hỏi ôn tập Ngày 20

   Khi nào bạn nên cân nhắc chuyển từ một agent duy nhất sang multi-agent system?
   - A. Khi nhiệm vụ cần tương tác với nhiều API bên ngoài.
   - B. Khi một agent đơn lẻ không đạt độ chính xác >80%.
   - C. Khi muốn giảm tổng chi phí vận hành hệ thống.
   - D. Khi cần triển khai mô hình ngôn ngữ lớn hơn.
   **Đáp án / Answer:** B

   Mô hình workflow nào trong số 5 pattern của Anthropic hoạt động bằng cách phân loại đầu vào và chuyển hướng đến handler chuyên biệt nhất?
   - A. Chuỗi Prompt
   - B. Định tuyến
   - C. Điều phối-Công nhân
   - D. Đánh giá-Tối ưu hóa
   **Đáp án / Answer:** B

   Kiến trúc nào thường được dùng để triển khai Supervisor Pattern trong multi-agent system?
   - A. Kiến trúc hình sao
   - B. Kiến trúc lưới
   - C. Kiến trúc trung tâm-nan hoa
   - D. Kiến trúc cây
   **Đáp án / Answer:** C

   Lợi ích chính của việc sử dụng Debate Agents (agents tranh luận) là gì?
   - A. Tăng tốc độ xử lý lên gấp đôi.
   - B. Giảm ảo giác (hallucination) từ 15% đến 25%.
   - C. Giảm chi phí API xuống một nửa.
   - D. Loại bỏ hoàn toàn nhu cầu dùng Judge agent.
   **Đáp án / Answer:** B

   Framework nào trong số sau đây được mô tả là “state machine driven” và phù hợp cho môi trường production cần kiểm soát chặt chẽ?
   **Đáp án / Answer:** C
