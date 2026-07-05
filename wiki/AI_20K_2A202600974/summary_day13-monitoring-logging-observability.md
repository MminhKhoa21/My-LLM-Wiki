---
type: summary
title: "Summary of day13-monitoring-logging-observability"
description: "Tổng hợp kiến thức về Monitoring, Logging, Observability đặc thù cho AI Agent (Day 13)."
tags: [ai, 20k, day13]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/13/day13-monitoring-logging-observability.pdf"]
---

# 🚀 Monitoring, Logging & Observability cho AI Agent

Tài liệu này tóm tắt bài giảng **Day 13: Biết agent đang hoạt động thế nào**, tập trung vào cách thiết lập hệ thống quan trắc (observability) từ mức độ cơ bản đến chi tiết trong hệ thống ứng dụng AI (LLM-based Agents).

> [!NOTE]
> Khác biệt cốt lõi: 
> - **Monitoring (Giám sát):** Trả lời các câu hỏi đã biết trước (known-unknowns).
> - **Observability (Quan trắc):** Cho phép hệ thống phát ra đủ dữ liệu để trả lời các câu hỏi mới phát sinh (unknown-unknowns), vốn rất phổ biến trong AI Agent (ví dụ: model drift, prompt mới).

---

## 1. 🏗️ Foundations of Observability (Nền tảng hệ thống quan trắc)

### 3 Pillars of Observability (3 Trụ cột)
1. **Metrics (Đo lường - Rẻ, dùng để cảnh báo):** Số liệu tổng hợp như Latency, QPS, Error Rate.
2. **Logs (Ghi chép - Đắt, dùng để debug root cause):** Sự kiện chi tiết với Input/Output.
3. **Traces (Theo dõi - Mức vừa phải, tìm bottleneck):** Hành trình end-to-end của request.
*(Profile là trụ cột thứ 4 nhưng ít dùng cho AI do độ trễ thường nằm ở LLM API chứ không phải ở local)*.

### Ngôn ngữ của Độ tin cậy (Reliability)
- **SLI (Service Level Indicator):** Chỉ số đo lường (VD: P95 latency).
- **SLO (Service Level Objective):** Mục tiêu nội bộ cho SLI (VD: P95 ≤ 3s trong 99.5% thời gian).
- **SLA (Service Level Agreement):** Cam kết với khách hàng (VD: 99% uptime).
- **Error Budget (Dung sai):** Khoảng sai lệch cho phép (100% - SLO). Hết dung sai -> Dừng tính năng mới, chỉ fix bug.

### Cardinality
- Là số lượng tổ hợp độc nhất của nhãn (label).
- **Không dùng:** `user_id`, `request_id` làm nhãn của metrics vì sẽ gây phình data (High Cardinality).
- **Nên dùng:** `model`, `env`, `tier`. Data high cardinality nên chuyển vào logs/traces.

---

## 2. 📊 AI Metrics Deep Dive (Các chỉ số đặc thù cho AI)

### Bổ sung vào "4 Golden Signals"
Ngoài 4 tín hiệu truyền thống (Latency, Traffic, Errors, Saturation), AI cần thêm:
1. **Cost (Chi phí):** $/request, usage token.
2. **Quality (Chất lượng):** Tỷ lệ ảo giác (hallucination), CSAT.

### Metrics Hiệu Suất & Chất Lượng
- **TTFT (Time To First Token) & TPOT (Time Per Output Token):** Quyết định trải nghiệm streaming của user thay vì chỉ đo tổng latency.
- **Percentile (P95, P99):** Ưu tiên đo đạc theo phân vị (P99) thay vì trung bình (Average) để khắc phục độ trễ cho nhóm người dùng bị "long tail".
- **Kim Tự Tháp Chất Lượng (4 tầng):** Automated Heuristic (L1) -> LLM-as-Judge (L2) -> User Signal (L3) -> Outcome (L4).
- **User-centric metrics:** *Regenerate rate* (Tỷ lệ ấn thử lại) là dấu hiệu tốt nhất để dự đoán người dùng sẽ bỏ ứng dụng (churn).

### Cost Engineering (Tối ưu chi phí)
Cost = (Input Tokens * Giá) + (Output Tokens * Giá) + (Cache Read/Write * Giá).
- **Yêu cầu:** Phải luôn gán tag `user_id`, `feature`, và `model` trong log để truy xuất được chi phí do ai/vào việc gì gây ra.
- **4 Patterns Tối Ưu:** Prompt Caching (Rẻ hơn 10x), Model Routing (Cascade), Semantic Cache (Similarity query), Batch API.

---

## 3. 📝 Structured Logging (Ghi log có cấu trúc)

Nên chuyển từ text thường sang **JSON** để dễ dàng filter và aggregate trên hệ thống.

- **Schema 3 Tier:**
  1. *Required:* `ts`, `level`, `correlation_id`, `service`, `event`.
  2. *Context:* `user_id`, `feature`, `model`, `env`.
  3. *Payload:* `latency`, `tokens`, `cost`, `error_type`.
- **Thực hành:** Dùng `structlog` (Python). Sử dụng `contextvars` để truyền **Correlation ID** (ID Request xuyên suốt các services).
- **PII Sanitization:** **TUYỆT ĐỐI KHÔNG** log thông tin cá nhân (PII như CCCD, thẻ tín dụng). Sử dụng Regex hoặc `Presidio` để ẩn danh trước khi ghi log.

---

## 4. 🔍 Distributed Tracing (Truy vết phân tán)

Traces là cách kết nối nhiều Spans (bước con) để tạo thành một "cây" luồng đi của request, giúp nhìn rõ điểm nghẽn (bottleneck).

- **OpenTelemetry (OTel):** Tiêu chuẩn chuẩn quốc tế, độc lập với nhà cung cấp. Cho phép `Auto-instrumentation` tự động trace các request API, DB mà không cần sửa code.
- **4 Mẫu Điểm Nghẽn Thường Gặp:**
  1. *Sequential dependency:* Gọi hàm tuần tự thay vì song song.
  2. *N+1 queries:* Gọi lặp API/DB nhiều lần.
  3. *Waiting:* Span chờ lâu (như gọi LLM) không tốn CPU -> cần cache, timeout.
  4. *Retry storm:* Span retry liên tục -> cần backoff hợp lý.
- **Tool Đề Xuất:** **Langfuse** (mã nguồn mở, phù hợp LLM, hỗ trợ giá model) hoặc Helicone, LangSmith.

---

## 5. 🚨 SLO-based Alerting & Dashboard (Cảnh báo & Bảng điều khiển)

### Cảnh báo Dựa Trên Triệu Chứng (Symptom-based)
- Đừng cảnh báo nguyên nhân (Ví dụ: CPU > 80%).
- Hãy cảnh báo triệu chứng tác động tới user (Ví dụ: P95 > SLO, Error > 1%).
- **Lưu ý:** Alert BẮT BUỘC phải kèm theo `runbook` (hướng dẫn xử lý). Nếu không, kỹ sư trực không biết cách sửa.

### Dashboard Design - 3 Layers
Không dồn tất cả biểu đồ vào một bảng, chia làm 3 tầng:
1. **Overview (Tổng quan):** Dành cho Leadership (Status, Cost).
2. **Detail (Chi tiết):** 4 Golden Signals + Cost/Quality (Tối đa 6 panels).
3. **Drill-down (Tìm nguồn gốc lỗi):** Các traces cá nhân, logs tìm lỗi cho kỹ sư debug.

---

## 6. ❌ Anti-patterns Cần Tránh (Kinh nghiệm thực tế)

1. **"We'll add monitoring later":** Đừng trì hoãn, hãy thiết lập từ ngày đầu (MVP).
2. **Log full prompts/responses:** Rủi ro lộ dữ liệu PII và tốn chi phí lưu trữ log (nên sanitize và sample).
3. **Quá nhiều alerts:** Gây "alert fatigue" (nhờn cảnh báo).
4. **Không có runbook:** Khi alert kêu lúc 3h sáng không ai biết xử lý.
5. **Môi trường Dev khác Prod:** Không reproduce được lỗi.
6. **Chỉ đo performance, quên cost:** Hậu quả là cháy túi cuối tháng.
7. **Tin tưởng vendor mặc định:** Mặc định của vài framework có thể log toàn bộ dữ liệu nhạy cảm.

---
> [!TIP]
> Việc sở hữu hệ thống Monitoring tốt cho AI Agent cho phép team nhận ra và giải quyết các lỗi đứt gãy, giảm engagement, vượt chi phí trước cả khi khách hàng bắt đầu phàn nàn.
