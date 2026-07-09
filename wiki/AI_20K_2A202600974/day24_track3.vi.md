---
type: summary
title: "Day 24 Track 3: RAGAS, LLM-as-Judge & Guardrails"
description: "Summary of Day 24 Track 3 focusing on automated evaluation using RAGAS, LLM-as-Judge pipelines, hallucination detection, and robust guardrails."
tags: [ragas, llm-as-judge, guardrails, evaluation, hallucination, track3]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/24/2-day24-ragas-guardrails.pdf", "AI_20K_2A202600974/24/lab24-student-edition.pdf"]
---
# Ngày 24 Track 3: RAGAS, LLM-as-Judge & Guardrails  

Trang này tóm tắt bài giảng và phòng thí nghiệm về Đánh giá RAG và Hệ thống Guardrail cho Track 3.

## Nền tảng đánh giá  

   **Quy tắc 80/5:** Các nhóm trước đây dành 80% thời gian để xây dựng và 5% để đánh giá. Tiêu chuẩn năm 2026 chuyển thành 50% xây dựng, 30% đánh giá và 20% guardrail. Việc kiểm tra cảm tính thủ công không thể mở rộng quy mô.
   **Đánh giá ngoại tuyến so với trực tuyến:** Đánh giá ngoại tuyến hoạt động như cổng CI trước khi triển khai bằng cách sử dụng bộ dữ liệu tĩnh. Đánh giá trực tuyến lấy mẫu lưu lượng sản xuất để phát hiện độ lệch và giám sát.
   **Đánh giá thành phần so với đầu cuối:** RAGAS cung cấp đánh giá cấp thành phần (truy xuất so với sinh), trong khi LLM-as-Judge cung cấp điểm tổng thể đầu cuối.

### RAGAS: 4 chỉ số cốt lõi  

    **Độ trung thực:** Ngữ cảnh có hỗ trợ câu trả lời không? Kiểm tra ảo giác nội tại. (Mục tiêu $\ge 0.85$)
    **Mức độ liên quan của câu trả lời:** Câu trả lời có giải quyết câu hỏi không? Sử dụng sinh câu hỏi ngược để phạt các câu trả lời lạc đề. (Mục tiêu $\ge 0.80$)
    **Độ chính xác ngữ cảnh:** Các đoạn truy xuất có liên quan có được xếp hạng cao nhất không? Đánh giá bằng NDCG. (Mục tiêu $\ge 0.70$)
    **Độ thu hồi ngữ cảnh:** Ngữ cảnh truy xuất có bao phủ sự thật cơ bản không? Yêu cầu câu trả lời tham chiếu. (Mục tiêu $\ge 0.75$)


Được sử dụng để mở rộng quy mô đánh giá từ hàng trăm lên hàng trăm nghìn truy vấn, nhưng cần giảm thiểu bốn thiên kiến chính:

    **Thiên kiến vị trí:** Các mô hình ưa thích tùy chọn đầu tiên hoặc cuối cùng. Được giảm thiểu thông qua *hoán đổi và lấy trung bình*.
    **Thiên kiến độ dài:** Các mô hình ưa thích câu trả lời dài dòng. Được giảm thiểu bằng đánh giá kiểm soát độ dài hoặc tiêu chí chặt chẽ.
    **Thiên kiến tự nâng cao:** Các mô hình thích đầu ra do chính chúng tạo ra. Được giảm thiểu thông qua *giao thức đánh giá chéo*.
    **Thiên kiến phong cách:** Các mô hình thích đầu ra được định dạng (ví dụ: markdown) hơn văn bản thuần. Được giảm thiểu bằng cách loại bỏ định dạng trước khi đánh giá.
   **Hiệu chỉnh con người:** Cần thiết phải đo lường sự phù hợp của người đánh giá với người đánh giá con người bằng **Cohen's Kappa**. Điểm số $\ge 0.60$ được yêu cầu cho sản xuất.

### Phát hiện ảo giác  

   **SelfCheckGPT:** Lấy mẫu nhiều câu trả lời với nhiệt độ > 0 và đo lường tính nhất quán. Phương sai cao cho thấy ảo giác.
   **NLI (Suy luận ngôn ngữ tự nhiên):** Sử dụng các mô hình như DeBERTa để xác minh xem ngữ cảnh truy xuất có hàm ý câu trả lời hay không.
   **Entropy ngữ nghĩa:** Phân cụm các câu trả lời theo tương đương ngữ nghĩa để đo lường độ không chắc chắn và xác suất ảo giác.


Guardrails cung cấp kiến trúc phòng thủ theo chiều sâu trên bốn chiều: Chủ đề, An toàn, Bảo mật và Tuân thủ.

   **Lớp đầu vào L1 (<30ms):** Xác thực đầu vào bằng cách sử dụng che dữ liệu PII (Presidio), phát hiện tiêm prompt (Prompt Guard) và trình xác thực phạm vi chủ đề (Guardrails AI).
   **Lớp LLM L2 (0ms):** Được xử lý thông qua các prompt có cấu trúc.
   **Lớp đầu ra L3 (<50ms):** Phân loại an toàn (Llama Guard 3) và phát hiện ảo giác (NLI).
   **Lớp kiểm toán L4:** Ghi nhật ký bất đồng bộ tất cả các truy vấn và hành động.

### Các mẫu tấn công  

   **Tiêm trực tiếp:** Ví dụ: DAN (Làm bất cứ điều gì ngay lập tức), Tách tải trọng, Vượt qua mã hóa.
   **Tiêm gián tiếp:** Các tải trọng độc hại được cấy vào các tài liệu truy xuất.
   **Đầu độc phiên:** Kẻ tấn công tiêm ý định độc hại vào lịch sử hội thoại, sau đó sử dụng một truy vấn lành tính để kích hoạt khai thác, vượt qua các bộ chặn đầu ra đơn giản. Được phòng thủ bằng cách thay thế các đầu vào độc hại trong chính lịch sử.

## Phòng thí nghiệm 24: Hệ thống đánh giá và Guardrail đầy đủ  

Phòng thí nghiệm có bốn giai đoạn:

   **Giai đoạn A (RAGAS):** Tạo bộ kiểm tra tổng hợp, chạy 4 chỉ số RAGAS, phân tích các cụm lỗi và thiết lập cổng GitHub Action CI/CD.
   **Giai đoạn B (LLM-as-Judge):** Xây dựng các pipeline chấm điểm theo cặp và tuyệt đối, đo lường Cohen's Kappa so với nhãn của con người và phân tích thiên kiến người đánh giá.
   **Giai đoạn C (Guardrails):** Triển khai hệ thống guardrail đầy đủ với Presidio, trình xác thực chủ đề, kiểm thử đối kháng và Llama Guard 3, được đo điểm chuẩn cho độ trễ P50/P95.
   **Giai đoạn D (Bản thiết kế):** Tài liệu hóa kiến trúc hệ thống, Mục tiêu cấp độ dịch vụ (SLO), sổ tay cảnh báo và phân tích chi phí.
