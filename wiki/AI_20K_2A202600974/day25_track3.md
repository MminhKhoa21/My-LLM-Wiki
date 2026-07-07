---
type: summary
title: "Circuit Breakers, Caching & Reliability for Production Agents"
description: "Summary of Day 10 on reliability primitives including failure modes, circuit breakers, caching, observability, and chaos testing for production LLM agents."
tags: [reliability, circuit breaker, caching, observability, slo, chaos testing, llm agents]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/25/day10_reliability_student.pdf"]
---
# Circuit Breakers, Caching & Reliability for Production Agents
*# Bộ ngắt mạch, Bộ nhớ đệm và Độ tin cậy cho các tác nhân sản xuất*

This document summarizes the content from the AICB-P2T3 Day 10 session on Agent Production-Ready concepts, focusing on reliability primitives.
*Tài liệu này tóm tắt nội dung từ phiên AICB-P2T3 Ngày 10 về các khái niệm sẵn sàng sản xuất cho tác nhân, tập trung vào các nguyên tắc cơ bản về độ tin cậy.*

## 1. Failure Modes
*## 1. Các dạng lỗi*

Reliability starts with correctly naming the errors. The 6 common failure modes to monitor in production LLM agents are:
*Độ tin cậy bắt đầu bằng việc đặt tên chính xác các lỗi. 6 dạng lỗi phổ biến cần theo dõi trong các tác nhân LLM sản xuất là:*

1.  **Provider transient**: Errors like 429 (Rate Limit), 500 (Internal Server Error), or timeouts.
    *Dịch: **Lỗi tạm thời của nhà cung cấp**: Các lỗi như 429 (Giới hạn tốc độ), 500 (Lỗi máy chủ nội bộ) hoặc hết thời gian chờ.*
2.  **Degraded latency**: A sharp increase in P95 latency.
    *Dịch: **Độ trễ suy giảm**: Sự gia tăng đột ngột của độ trễ P95.*
3.  **Full outage**: The provider stops responding completely.
    *Dịch: **Ngừng hoạt động hoàn toàn**: Nhà cung cấp ngừng phản hồi hoàn toàn.*
4.  **Orchestration loop**: Errors related to state or incorrect retries.
    *Dịch: **Vòng lặp điều phối**: Các lỗi liên quan đến trạng thái hoặc thử lại không chính xác.*
5.  **Tool/cache failure**: Issues like stale cache, incorrect schema, or authentication failures.
    *Dịch: **Lỗi công cụ/bộ nhớ đệm**: Các vấn đề như bộ nhớ đệm lỗi thời, lược đồ không chính xác hoặc lỗi xác thực.*
6.  **Business action sai**: Incorrect business actions with side effects that cannot be rolled back.
    *Dịch: **Hành động kinh doanh sai**: Các hành động kinh doanh không chính xác với các tác dụng phụ không thể hoàn tác.*

### Silent Degradation
*### Suy giảm thầm lặng*

A system can degrade without explicit errors (e.g., error rate = 0%). This happens when:
*Một hệ thống có thể suy giảm mà không có lỗi rõ ràng (ví dụ: tỷ lệ lỗi = 0%). Điều này xảy ra khi:*

- The provider updates the model silently.
  *Nhà cung cấp cập nhật mô hình một cách thầm lặng.*
- Prompt/schema changes but evaluation does not.
  *Prompt/lược đồ thay đổi nhưng việc đánh giá thì không.*
- Knowledge base becomes stale or retrieval weakens.
  *Cơ sở tri thức trở nên lỗi thời hoặc khả năng truy xuất suy yếu.*
- Cache returns a previously correct but currently incorrect answer.
  *Bộ nhớ đệm trả về câu trả lời trước đây đúng nhưng hiện tại sai.*

## 2. Circuit Breaker & Fallback
*## 2. Bộ ngắt mạch & Dự phòng*

A **Circuit Breaker** stops calls to a failing provider, while a **Fallback** chain maintains user experience at an acceptable level.
*Một **Bộ ngắt mạch** dừng các cuộc gọi đến nhà cung cấp đang gặp lỗi, trong khi một chuỗi **Dự phòng** duy trì trải nghiệm người dùng ở mức chấp nhận được.*

### 3 States of a Circuit Breaker
*### 3 Trạng thái của Bộ ngắt mạch*

- **CLOSED**: Normal calls proceed.
  *Dịch: **ĐÓNG**: Các cuộc gọi bình thường được tiến hành.*
- **OPEN**: Fail fast. Transitions from CLOSED when the failure threshold is reached.
  *Dịch: **MỞ**: Thất bại nhanh. Chuyển từ ĐÓNG khi ngưỡng lỗi đạt đến.*
- **HALF-OPEN**: Probe call to test if the provider has recovered. Transitions from OPEN after a reset timeout. Transitions back to CLOSED on success, or OPEN on failure.
  *Dịch: **NỬA-MỞ**: Cuộc gọi thăm dò để kiểm tra xem nhà cung cấp đã phục hồi chưa. Chuyển từ MỞ sau thời gian chờ đặt lại. Chuyển lại thành ĐÓNG nếu thành công, hoặc MỞ nếu thất bại.*

### Fallback Ladder (Graceful Degradation)
*### Thang dự phòng (Suy giảm có kiểm soát)*

A typical fallback policy:
*Một chính sách dự phòng điển hình:*

1.  **Best model** (Highest quality)
    *Dịch: **Mô hình tốt nhất** (Chất lượng cao nhất)*
2.  **Backup provider** (Same feature set)
    *Dịch: **Nhà cung cấp dự phòng** (Cùng bộ tính năng)*
3.  **Cheaper/smaller model** (Limited quality)
    *Dịch: **Mô hình rẻ hơn/nhỏ hơn** (Chất lượng hạn chế)*
4.  **Cached response**
    *Dịch: **Phản hồi được lưu trong bộ nhớ đệm***
5.  **Static fallback message**
    *Dịch: **Tin nhắn dự phòng tĩnh***

*Note: Feature compatibility (JSON mode, tool calling, context length, latency/cost, policy behavior) must be checked when falling back to a weaker model.*
*Lưu ý: Tính tương thích của tính năng (chế độ JSON, gọi công cụ, độ dài ngữ cảnh, độ trễ/chi phí, hành vi chính sách) phải được kiểm tra khi chuyển sang mô hình yếu hơn.*

## 3. Caching & Cost Budgeting
*## 3. Bộ nhớ đệm & Ngân sách chi phí*

Proper caching reduces latency and cost; improper caching causes stale answers and stable hallucinations.
*Bộ nhớ đệm thích hợp giảm độ trễ và chi phí; bộ nhớ đệm không phù hợp gây ra câu trả lời lỗi thời và ảo giác ổn định.*

### 3 Caching Layers for LLM Applications
*### 3 Lớp bộ nhớ đệm cho các ứng dụng LLM*

1.  **Provider prompt/prefix cache**: Reduces cost when long prefixes are reused.
    *Dịch: **Bộ nhớ đệm prompt/tiền tố của nhà cung cấp**: Giảm chi phí khi các tiền tố dài được tái sử dụng.*
2.  **App semantic response cache**: Reuses responses for semantically similar queries.
    *Dịch: **Bộ nhớ đệm phản hồi ngữ nghĩa của ứng dụng**: Tái sử dụng các phản hồi cho các truy vấn tương tự về mặt ngữ nghĩa.*
3.  **Tool/result cache**: Caches expensive but deterministic API/DB results.
    *Dịch: **Bộ nhớ đệm công cụ/kết quả**: Lưu trữ các kết quả API/DB đắt tiền nhưng xác định.*

### Semantic Cache Flow
*### Luồng bộ nhớ đệm ngữ nghĩa*

- **HIT**: `similarity > threshold` -> Return cache.
  *Dịch: **TRÚNG**: `độ tương tự > ngưỡng` -> Trả về bộ nhớ đệm.*
- **MISS**: `similarity < threshold` -> Call LLM -> Store result.
  *Dịch: **TRƯỢT**: `độ tương tự < ngưỡng` -> Gọi LLM -> Lưu trữ kết quả.*
*Caution: Cache poisoning occurs when two queries are very close in cosine similarity but have different intents. Monitor hit rate and false-hit rate.*
*Cảnh báo: Nhiễm độc bộ nhớ đệm xảy ra khi hai truy vấn rất gần nhau về độ tương tự cosine nhưng có ý định khác nhau. Theo dõi tỷ lệ trúng và tỷ lệ trúng giả.*

### Cost Budgeting
*### Ngân sách chi phí*

Control costs at 3 layers:
*Kiểm soát chi phí ở 3 lớp:*

1.  Per-request cap (max tokens, max tools, timeout).
    *Dịch: Giới hạn mỗi yêu cầu (tối đa token, tối đa công cụ, thời gian chờ).*
2.  Per-user/app rate limit (token bucket).
    *Dịch: Giới hạn tốc độ mỗi người dùng/ứng dụng (bucket token).*
3.  Monthly budget (warn at 80%, hard stop/route to cheaper model at 100%).
    *Dịch: Ngân sách hàng tháng (cảnh báo ở 80%, dừng cứng/chuyển hướng đến mô hình rẻ hơn ở 100%).*

## 4. Observability & SLO
*## 4. Khả năng quan sát & SLO*

Without monitoring, it is impossible to know if the system is good, slow, expensive, or returning incorrect answers.
*Nếu không có giám sát, không thể biết liệu hệ thống có tốt, chậm, đắt đỏ hay đang trả về câu trả lời không chính xác hay không.*

- **SLI (Service Level Indicator)**: The measured metric (e.g., availability, P95 latency, cache hit rate).
  *Dịch: **SLI (Chỉ báo mức dịch vụ)**: Số liệu được đo (ví dụ: tính khả dụng, độ trễ P95, tỷ lệ trúng bộ nhớ đệm).*
- **SLO (Service Level Objective)**: Internal target (e.g., availability >= 99%, P95 < 2.5s, fallback success >= 95%).
  *Dịch: **SLO (Mục tiêu mức dịch vụ)**: Mục tiêu nội bộ (ví dụ: khả dụng >= 99%, P95 < 2.5s, thành công dự phòng >= 95%).*
- **SLA (Service Level Agreement)**: External commitment (e.g., 99.5% uptime/month for customer-facing APIs).
  *Dịch: **SLA (Thỏa thuận mức dịch vụ)**: Cam kết bên ngoài (ví dụ: thời gian hoạt động 99.5%/tháng cho các API hướng tới khách hàng).*
- **Error budget**: The allowed failure rate before action is taken (e.g., freezing features to prioritize reliability).
  *Dịch: **Ngân sách lỗi**: Tỷ lệ lỗi được phép trước khi hành động được thực hiện (ví dụ: đóng băng các tính năng để ưu tiên độ tin cậy).*

*Note: LLM agents require quality SLOs in addition to uptime SLOs (e.g., faithfulness, safety pass rate, escalation correctness).*
*Lưu ý: Các tác nhân LLM yêu cầu SLO chất lượng ngoài SLO thời gian hoạt động (ví dụ: tính trung thực, tỷ lệ vượt qua an toàn, tính chính xác của việc leo thang).*

## 5. Lab: Reliability Engineering
*## 5. Phòng thí nghiệm: Kỹ thuật độ tin cậy*

The lab involves building a reliability gateway that implements:
*Phòng thí nghiệm liên quan đến việc xây dựng một cổng độ tin cậy thực hiện:*

- Circuit breaker + semantic/tool cache
  *Bộ ngắt mạch + bộ nhớ đệm ngữ nghĩa/công cụ*
- Metrics instrumentation (JSON/CSV)
  *Công cụ đo lường số liệu (JSON/CSV)*
- Chaos testing and reporting
  *Kiểm tra hỗn loạn và báo cáo*

**Chaos Testing Scenarios:**
***Các kịch bản kiểm tra hỗn loạn:** *

- Primary provider timeout 100%.
  *Nhà cung cấp chính hết thời gian chờ 100%.*
- Primary provider intermittent 50%.
  *Nhà cung cấp chính gián đoạn 50%.*
- Cache returns stale candidate.
  *Bộ nhớ đệm trả về ứng viên lỗi thời.*
- Cost cap almost reached.
  *Giới hạn chi phí gần như đạt đến.*

Expected evidence includes metrics showing the circuit breaker transitioning (CLOSED -> OPEN), gateway routing to fallback without a retry storm, and logged recovery time.
*Bằng chứng dự kiến bao gồm các số liệu cho thấy bộ ngắt mạch chuyển đổi (ĐÓNG -> MỞ), cổng chuyển hướng đến dự phòng mà không có bão thử lại, và thời gian phục hồi được ghi lại.*
