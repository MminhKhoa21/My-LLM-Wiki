---
type: overview
title: "Day 13: Monitoring, Logging & Observability"
description: "Đo lường, ghi log, và theo dõi chất lượng hệ thống AI trên production để phát hiện lỗi và đánh giá hiệu năng thực tế."
tags: [ai, 20k, day13, monitoring, observability]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/13/day13-monitoring-logging-observability_v2.pdf"]
---


## Nội dung chính
Để duy trì chất lượng hệ thống AI sau khi deploy, không thể chờ user phàn nàn mới tìm cách sửa lỗi. Cần xây dựng kiến trúc **Observability** dựa trên 4 trụ cột chính.

1. **Metrics (Đo lường)**: Cho biết hệ thống chạy nhanh/chậm, tốn kém bao nhiêu. Các nhóm metric chính: Performance (Latency, TTFT), Cost (Tokens/request), Reliability (Error rate), và Quality.
2. **Logs (Ghi chép)**: Ghi lại chi tiết từng sự kiện. Nên dùng **Structured Logging (JSON)** để dễ dàng lọc và tìm kiếm thay vì text thô. Cần lưu ý bảo mật (redact PII) trước khi lưu log.
3. **Traces (Theo dõi đường đi)**: Đóng vai trò cực kỳ quan trọng trong AI Agent nhiều bước. Trace phân tích chi tiết "cây thực thi" (span tree), giúp biết LLM call hay Tool call nào đang làm chậm hoặc hỏng toàn bộ quy trình.
4. **Online Evaluation (Pillar 4)**: Đánh giá chất lượng sinh ra trên production (ví dụ: HTTP 200 chưa chắc câu trả lời đã đúng). Sử dụng feedback của user hoặc chấm điểm bằng LLM (LLM-as-Judge) để cảnh báo.

## Metrics quan trọng
- Tập trung vào chỉ số **P95 / P99 Latency** thay vì trung bình (average) để phản ánh trải nghiệm thực tế của user.
- Cost là "First-class metric": cần theo dõi chặt chẽ vì Output đắt hơn Input, Agent lỗi vòng lặp có thể ngốn sạch budget nhanh chóng.
- **SLI / SLO**: Đặt ngưỡng mục tiêu (SLO) cho các chỉ số quan trọng, thiết lập các cảnh báo dựa trên triệu chứng (Symptom-based Alerting) để không rơi vào tình trạng "Báo động giả" (Alert fatigue).

## Công cụ
- **OpenTelemetry (OTel)** là chuẩn chung giúp gửi metrics/logs/traces đến các backend khác nhau mà không bị khóa hệ sinh thái (vendor lock-in).
- Ngăn xếp phổ biến: Prometheus (lưu metric) + Grafana (vẽ dashboard) kết hợp với các bộ LLM-observability tools chuyên dụng như Langfuse, LangSmith.
