---
type: summary
title: "Summary of day28-platform-engineering-documentation"
description: "An end-to-end guide on AI platform engineering, covering integration patterns, performance profiling, and production readiness."
tags: [ai, 20k, day28, platform-engineering, mlops]
timestamp: 2026-07-06
sources: ["raw/AI_20K_2A202600974/28/day28-platform-engineering-documentation.pdf"]
---
# <i>Kỹ thuật Nền tảng & Tài liệu</i>
<i>**Giảng viên:** VinUniversity (AICB-P2T2 · Phase 2 · Track 2)</i>

<i>Tổng quan</i>
<i>Tài liệu này bao gồm việc tích hợp các thành phần AI bị cô lập thành một Nền tảng AI end-to-end có đầy đủ chức năng. Trọng tâm là chuyển từ quá trình thu thập dữ liệu sang phục vụ mô hình với khả năng quan sát toàn diện và sự sẵn sàng cho môi trường production.</i>

<i>5 Lớp của Nền tảng AI</i>
1. <i>**Máy tính (Compute):** Kubernetes, các node GPU, vLLM serving, tự động mở rộng (auto-scaling).</i>
2. <i>**Dữ liệu (Data):** Lakehouse (Delta Lake), Airflow, Kafka, Vector Store.</i>
3. <i>**Học máy (ML):** Thử nghiệm MLflow, quản lý phiên bản DVC, Feature Store (Feast).</i>
4. <i>**Vận hành (Ops):** GitHub Actions CI/CD, LangSmith LLMOps, Prometheus/Grafana.</i>
5. <i>**Quản trị (Governance):** RBAC, pipeline xử lý PII, mã hóa, tự động hóa tuân thủ (compliance automation).</i>

<i>Các Mô hình Tích hợp (Patterns) và Phản mô hình (Anti-patterns)</i>
- <i>**Phản mô hình (Anti-pattern):** Các thành phần liên kết chặt chẽ (dẫn đến các lỗi dây chuyền).</i>
  - <i>**Mô hình (Pattern):** Tích hợp hướng sự kiện sử dụng các công cụ như Kafka hoặc Redis Streams để tách biệt các nhà sản xuất (producers) và người tiêu dùng (consumers).</i>
- <i>**Phản mô hình:** Cấu hình cứng (Hardcoded).</i>
  - <i>**Mô hình:** GitOps (ArgoCD, Helm) để duy trì tất cả các cấu hình trong Git.</i>
- <i>**Phản mô hình:** Chia sẻ trạng thái có thể thay đổi (Shared mutable state).</i>
  - <i>**Mô hình:** Các sự kiện bất biến và nguồn cung cấp sự kiện thông qua các log chỉ nối thêm (append-only) (Kafka).</i>
- <i>**Phản mô hình:** Các lỗi dây chuyền xuyên suốt các dịch vụ.</i>
  - <i>**Mô hình:** Mô hình vách ngăn (Bulkhead pattern) (sử dụng namespaces và hạn mức tài nguyên của K8s) để tách biệt các luồng suy luận quan trọng khỏi quá trình huấn luyện batch không quan trọng.</i>

<i>Luồng Yêu cầu End-to-End</i>
<i>Một luồng yêu cầu AI điển hình trên môi trường production bao gồm:</i>
1. <i>Yêu cầu của người dùng → API Gateway → Lớp định tuyến → Trình điều phối Agent.</i>
2. <i>Các cuộc gọi song song tới Feature Store (<5ms), Vector Search (<50ms), và Suy luận LLM (<500ms).</i>
3. <i>Các rào chắn bảo vệ cho việc kiểm tra PII (<20ms).</i>
4. <i>Phản hồi được trả về trong vòng 1 giây.</i>

<i>Tất cả các cuộc gọi phải được theo dõi (traced) bằng OpenTelemetry, Jaeger, và LangSmith.</i>

<i>Kiểm thử Tích hợp & Phân tích Hiệu suất (Profiling)</i>
- <i>**Kiểm thử:** Các bài kiểm thử tích hợp phải đảm bảo các hợp đồng API được giữ nguyên vẹn. Kiểm thử cả "golden path" (luồng thành công) và các luồng lỗi (timeouts, retries). Sử dụng Testcontainers để chạy các cơ sở dữ liệu thực trong CI.</i>
- <i>**Các Công cụ Phân tích (Profiling Tools):**</i>
  - <i>`Jaeger`: Phân tích chi tiết độ trễ end-to-end và xác định các nút thắt cổ chai trong các cuộc gọi song song so với tuần tự.</i>
  - <i>`cProfile` / `py-spy`: Xác định các điểm nóng của CPU.</i>
  - <i>`tracemalloc`: Theo dõi bộ nhớ và tìm các lỗi rò rỉ (leaks).</i>

<i>Sự Sẵn sàng cho Production: 5 Trụ cột</i>
<i>Một nền tảng phải đáp ứng các tiêu chí sau trước khi triển khai:</i>
1. <i>**Độ tin cậy:** Các bộ ngắt mạch, cơ chế thử lại (retries), tắt hệ thống an toàn (graceful shutdowns).</i>
2. <i>**Khả năng quan sát:** Các log JSON có cấu trúc, số liệu Prometheus, dấu vết OpenTelemetry, cảnh báo tự động.</i>
3. <i>**Bảo mật:** Vault/KMS cho bảo mật (secrets), RBAC, xử lý PII.</i>
4. <i>**Hiệu suất:** SLAs về độ trễ, quản lý bộ nhớ.</i>
5. <i>**Vận hành:** CI/CD tự động, kế hoạch phục hồi sau thảm họa, kiểm thử tải (load testing).</i>

<i>*Quy tắc Quan trọng:* Bảng kiểm tra Sự Sẵn sàng cho Production phải được tự động hóa trong pipeline CI, không nên dựa vào trí nhớ của con người.</i>

<i>Những Điểm Chính</i>
1. <i>**Tích hợp:** Tích hợp là nơi khái niệm "chạy được trên máy của tôi" đối mặt với thực tế. Luôn kiểm thử các điểm tích hợp thật kỹ trước khi đưa lên production.</i>
2. <i>**Tự động hóa:** Các bảng kiểm tra mức độ sẵn sàng cho production phải được tự động hóa.</i>
3. <i>**Tư duy Nền tảng:** Một nền tảng có nghĩa là các nhóm khác sẽ tiêu thụ nó. Các hợp đồng API rõ ràng, SLAs và tài liệu quan trọng hơn chất lượng mã nguồn nội bộ bị cô lập.</i>

<i>Liên kết</i>

---

### *Câu hỏi ôn tập Ngày 28*

   Theo bài giảng, đâu là **anti-pattern** trong tích hợp các thành phần AI Platform?
     A. Sử dụng event-driven integration với Kafka
     B. Duy trì cấu hình trong Git (GitOps)
     C. Gắn kết chặt chẽ (tightly coupled) giữa các thành phần
     D. Áp dụng Bulkhead pattern để tách biệt inference và training
   ***Đáp án:** C*

   Trong luồng request end-to-end, thời gian mục tiêu cho mỗi thành phần là bao nhiêu?
     D. Tất cả đều cần dưới 100ms
   ***Đáp án:** B*

   Công cụ nào được khuyến nghị để **phân tích chi tiết độ trễ (latency breakdown)** trong toàn bộ luồng?
   ***Đáp án:** C*

   Điều kiện tiên quyết để triển khai Platform ra production theo 5 Pillars là gì?
     A. Kiểm tra checklist Production Readiness bằng tay bởi kỹ sư
     B. Tự động hóa checklist trong CI pipeline
     C. Đảm bảo tất cả code đều chạy trên môi trường local
     D. Sử dụng duy nhất một framework cho toàn bộ stack
   ***Đáp án:** B*

   Mô hình nào sau đây là **integration pattern** đúng để tránh shared mutable state?
     A. Dùng cơ sở dữ liệu chung có thể ghi đồng thời
     B. Immutable events và event sourcing qua append-only log (Kafka)
     C. Lưu trạng thái trong biến toàn cục (global variable)
     D. Sử dụng file cấu hình JSON tĩnh
   ***Đáp án:** B*
