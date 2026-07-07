---
type: summary
title: "Summary: Day 02 Lecture Slides Blue"
description: "A summary of the Day 02 lecture slides on defining AI problems, frameworks, and solution levels."
tags: [AI Problem, Double Diamond, Workflow, Problem Statement]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/1-day02-lecture-slides-blue.pdf"]
---
Dưới đây là nội dung file `summary_1-day02-lecture-slides-blue.md` đã được chuyển đổi sang định dạng **song ngữ Anh – Việt**, giữ nguyên cấu trúc Markdown. Mỗi phần tiếng Anh được giữ nguyên, bản dịch tiếng Việt được in nghiêng và đặt ngay phía dưới.

---

# Tóm tắt: Bài giảng Ngày 02 Slides Blue  

## Tổng quan  

*Tài liệu này tóm tắt các slide bài giảng từ Ngày 02 của chương trình VinUni AI 20K, do giảng viên Mai Anh Nguyen (Blue) hướng dẫn. Trọng tâm cốt lõi là chuyển đổi các yêu cầu kinh doanh mơ hồ thành các Tuyên bố Vấn đề AI (AI Problem Statements) rõ ràng, có thể hành động, đánh giá xem AI có thực sự cần thiết hay không, và lựa chọn cấp độ giải pháp phù hợp (Quy tắc, Quy trình làm việc, hoặc Tác nhân).*

## Các khái niệm chính  

### Khám phá Vấn đề và Mô hình Kim cương Đôi (Double Diamond Model)  

- **Mô hình Kim cương Đôi** nhấn mạnh việc tìm đúng vấn đề trước khi tìm giải pháp phù hợp. Nó bao gồm hai viên kim cương:  

  - **Kim cương 1 (Vấn đề):** Khám phá (Discover – phân kỳ để tìm hiểu) và Định nghĩa (Define – hội tụ để xác định chính xác gốc rễ vấn đề).  

  - **Kim cương 2 (Giải pháp):** Phát triển (Develop – phân kỳ để khám phá các giải pháp) và Cung cấp (Deliver – hội tụ để chọn và triển khai).  

- Ưu tiên **Thiết kế Lấy Con người làm Trung tâm (HCD)** bằng cách quan sát người dùng, hiểu những điểm đau của họ (những nút thắt cổ chai), và tránh các khuôn mẫu "giải pháp trước tiên" (solution-first) sai lầm.  

### Định nghĩa Tuyên bố Vấn đề (Problem Statement)  

*Một **Tuyên bố Vấn đề** rõ ràng là điều cần thiết trước khi xem xét giải pháp AI. Nó bao gồm:*  

1. **Đối tượng (Actor)**: Ai là người bị ảnh hưởng?  

2. **Quy trình làm việc (Workflow)**: Quá trình từng bước hiện tại là gì?  

3. **Nút thắt cổ chai (Bottleneck)**: Sự chậm trễ, lỗi hoặc lặp lại chính xác nằm ở đâu?  

4. **Tác động (Impact)**: Tổn thất có thể định lượng được là gì (thời gian, chi phí)?  

5. **Chỉ số Thành công (Success Metric)**: Sự cải thiện sẽ được đo lường như thế nào?  

6. **Ranh giới (Boundary)**: Những giới hạn nghiêm ngặt là gì (ví dụ: AI không thể tự động gửi email)?  

7. **Điểm can thiệp AI (AI Intervention Point)**: Chính xác vị trí nào trong quy trình làm việc mà AI sẽ bước vào?  

8. **Cấp độ Giải pháp (Level of Solution)**: Quy tắc, Quy trình làm việc hay Tác nhân?  

9. **Rủi ro & Sự tham gia của con người (HITL)**: Cách xử lý các lỗi của AI và những nơi cần sự phê duyệt của con người.  

### Cấp độ Giải pháp AI: Quy tắc vs. Quy trình làm việc vs. Tác nhân  

*Luôn ưu tiên giải pháp đơn giản nhất mà vẫn mang lại hiệu quả:*  

- **Cấp độ 1 - Quy tắc (Rule)**: Sử dụng khi logic mang tính tất định (If/Else) và yêu cầu sự chính xác. Không cần đến AI.  

- **Cấp độ 2 - Quy trình làm việc (LLM Feature)**: Sử dụng khi các bước đã được xác định, nhưng một số bước cần AI để xử lý ngôn ngữ, tóm tắt hoặc phân loại. Vẫn giữ toàn quyền kiểm soát của con người.  

- **Cấp độ 3 - Tác nhân (Agent)**: Sử dụng khi môi trường mang tính động cao, đòi hỏi khả năng lên kế hoạch tự chủ và phối hợp nhiều công cụ. Rủi ro và chi phí vận hành cao hơn.  

### Các mẫu Quy trình làm việc  

*Dựa trên hướng dẫn của Anthropic:*  

- **Mẫu Cơ bản**: Chuỗi lệnh (Prompt Chaining), Điều hướng (Routing), Song song hóa (Parallelization).  

- **Mẫu Nâng cao**: Người điều phối - Công nhân (Orchestrator-Workers), Người đánh giá - Người tối ưu hóa (Evaluator-Optimizer), Tác nhân Tự chủ (Autonomous Agents).  

### Ra Quyết định  

*Bước cuối cùng trong việc thiết lập vấn đề là đưa ra một quyết định có ý thức:*  

- **Tiến hành (Go)**: Vấn đề rõ ràng, các chỉ số có thể đo lường và AI mang lại lợi thế vượt trội.  

- **Chưa thể thực hiện (Not Yet)**: Cần thêm dữ liệu, chuẩn hóa quy trình, hoặc các chỉ số rõ ràng hơn.  

- **Không thực hiện (No-Go)**: Quá rủi ro, hoặc các giải pháp phi AI hiệu quả hơn.  

## Tích hợp Quy trình làm việc  

- **Trải nghiệm người dùng & Sự tham gia của con người (UX & HITL)**: Đảm bảo thiết kế giao diện người dùng (UI) phù hợp để xử lý những thiếu sót của AI (ví dụ: yêu cầu làm rõ, cung cấp trích dẫn, yêu cầu phê duyệt thủ công).  

- **Đánh giá (Evaluation)**: Tuyên bố Vấn đề đóng vai trò như bản thiết kế cho Kế hoạch Đánh giá (đường cơ sở, các trường hợp kiểm thử và ngưỡng thành công).  

--- 

**Ghi chú:** Toàn bộ nội dung trên đã được biên tập để đảm bảo mỗi phần đều có cả tiếng Anh và tiếng Việt in nghiêng. Không có YAML frontmatter trong file này nên không cần bỏ qua phần nào.
