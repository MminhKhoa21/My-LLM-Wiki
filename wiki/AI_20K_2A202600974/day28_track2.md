---
type: summary
title: "Summary of day28-platform-engineering-documentation"
description: "An end-to-end guide on AI platform engineering, covering integration patterns, performance profiling, and production readiness."
tags: [ai, 20k, day28, platform-engineering, mlops]
timestamp: 2026-07-06
sources: ["raw/AI_20K_2A202600974/28/day28-platform-engineering-documentation.pdf"]
---

# Platform Engineering & Documentation
# Kỹ thuật Nền tảng & Tài liệu
**Instructor:** VinUniversity (AICB-P2T2 · Phase 2 · Track 2)
**Giảng viên:** VinUniversity (AICB-P2T2 · Phase 2 · Track 2)

## Overview
## Tổng quan
This document covers the integration of isolated AI components into a fully functional end-to-end AI Platform. The focus is on moving from data ingestion to model serving with comprehensive observability and production readiness.

Tài liệu này bao gồm việc tích hợp các thành phần AI bị cô lập thành một Nền tảng AI end-to-end có đầy đủ chức năng. Trọng tâm là chuyển từ quá trình thu thập dữ liệu sang phục vụ mô hình với khả năng quan sát toàn diện và sự sẵn sàng cho môi trường production.

## 5 Layers of the AI Platform
## 5 Lớp của Nền tảng AI
1. **Compute:** Kubernetes, GPU nodes, vLLM serving, auto-scaling.
1. **Máy tính (Compute):** Kubernetes, các node GPU, vLLM serving, tự động mở rộng (auto-scaling).
2. **Data:** Lakehouse (Delta Lake), Airflow, Kafka, Vector Store.
2. **Dữ liệu (Data):** Lakehouse (Delta Lake), Airflow, Kafka, Vector Store.
3. **ML:** MLflow experiments, DVC versioning, Feature Store (Feast).
3. **Học máy (ML):** Thử nghiệm MLflow, quản lý phiên bản DVC, Feature Store (Feast).
4. **Ops:** GitHub Actions CI/CD, LangSmith LLMOps, Prometheus/Grafana.
4. **Vận hành (Ops):** GitHub Actions CI/CD, LangSmith LLMOps, Prometheus/Grafana.
5. **Governance:** RBAC, PII pipelines, encryption, compliance automation.
5. **Quản trị (Governance):** RBAC, pipeline xử lý PII, mã hóa, tự động hóa tuân thủ (compliance automation).

## Integration Patterns vs. Anti-patterns
## Các Mô hình Tích hợp (Patterns) và Phản mô hình (Anti-patterns)
- **Anti-pattern:** Tightly coupled components (leads to cascading failures).
- **Phản mô hình (Anti-pattern):** Các thành phần liên kết chặt chẽ (dẫn đến các lỗi dây chuyền).
  - **Pattern:** Event-driven integration using tools like Kafka or Redis Streams to decouple producers and consumers.
  - **Mô hình (Pattern):** Tích hợp hướng sự kiện sử dụng các công cụ như Kafka hoặc Redis Streams để tách biệt các nhà sản xuất (producers) và người tiêu dùng (consumers).
- **Anti-pattern:** Hardcoded configurations.
- **Phản mô hình:** Cấu hình cứng (Hardcoded).
  - **Pattern:** GitOps (ArgoCD, Helm) to maintain all configurations in Git.
  - **Mô hình:** GitOps (ArgoCD, Helm) để duy trì tất cả các cấu hình trong Git.
- **Anti-pattern:** Shared mutable state.
- **Phản mô hình:** Chia sẻ trạng thái có thể thay đổi (Shared mutable state).
  - **Pattern:** Immutable events and event sourcing via append-only logs (Kafka).
  - **Mô hình:** Các sự kiện bất biến và nguồn cung cấp sự kiện thông qua các log chỉ nối thêm (append-only) (Kafka).
- **Anti-pattern:** Cascading failures across services.
- **Phản mô hình:** Các lỗi dây chuyền xuyên suốt các dịch vụ.
  - **Pattern:** Bulkhead pattern (using K8s namespaces and resource quotas) to separate critical inference paths from non-critical batch training.
  - **Mô hình:** Mô hình vách ngăn (Bulkhead pattern) (sử dụng namespaces và hạn mức tài nguyên của K8s) để tách biệt các luồng suy luận quan trọng khỏi quá trình huấn luyện batch không quan trọng.

## End-to-End Request Flow
## Luồng Yêu cầu End-to-End
A typical production AI request flow involves:

Một luồng yêu cầu AI điển hình trên môi trường production bao gồm:
1. User Request → API Gateway → Routing Layer → Agent Orchestrator.
1. Yêu cầu của người dùng → API Gateway → Lớp định tuyến → Trình điều phối Agent.
2. Parallel calls to Feature Store (<5ms), Vector Search (<50ms), and LLM Inference (<500ms).
2. Các cuộc gọi song song tới Feature Store (<5ms), Vector Search (<50ms), và Suy luận LLM (<500ms).
3. Guardrails for PII checks (<20ms).
3. Các rào chắn bảo vệ cho việc kiểm tra PII (<20ms).
4. Response delivered within 1 second.
4. Phản hồi được trả về trong vòng 1 giây.

All calls must be traced using OpenTelemetry, Jaeger, and LangSmith.

Tất cả các cuộc gọi phải được theo dõi (traced) bằng OpenTelemetry, Jaeger, và LangSmith.

## Integration Testing & Profiling
## Kiểm thử Tích hợp & Phân tích Hiệu suất (Profiling)
- **Testing:** Integration tests must ensure API contracts remain intact. Test against both the "golden path" (happy flow) and failure paths (timeouts, retries). Use Testcontainers for spinning up real databases in CI.
- **Kiểm thử:** Các bài kiểm thử tích hợp phải đảm bảo các hợp đồng API được giữ nguyên vẹn. Kiểm thử cả "golden path" (luồng thành công) và các luồng lỗi (timeouts, retries). Sử dụng Testcontainers để chạy các cơ sở dữ liệu thực trong CI.
- **Profiling Tools:**
- **Các Công cụ Phân tích (Profiling Tools):**
  - `Jaeger`: End-to-end latency breakdown and identifying bottlenecks in parallel vs. sequential calls.
  - `Jaeger`: Phân tích chi tiết độ trễ end-to-end và xác định các nút thắt cổ chai trong các cuộc gọi song song so với tuần tự.
  - `cProfile` / `py-spy`: Identifying CPU hotspots.
  - `cProfile` / `py-spy`: Xác định các điểm nóng của CPU.
  - `tracemalloc`: Memory tracking and finding leaks.
  - `tracemalloc`: Theo dõi bộ nhớ và tìm các lỗi rò rỉ (leaks).

## Production Readiness: 5 Pillars
## Sự Sẵn sàng cho Production: 5 Trụ cột
A platform must meet these criteria before deployment:

Một nền tảng phải đáp ứng các tiêu chí sau trước khi triển khai:
1. **Reliability:** Circuit breakers, retries, graceful shutdowns.
1. **Độ tin cậy:** Các bộ ngắt mạch, cơ chế thử lại (retries), tắt hệ thống an toàn (graceful shutdowns).
2. **Observability:** Structured JSON logs, Prometheus metrics, OpenTelemetry traces, automated alerts.
2. **Khả năng quan sát:** Các log JSON có cấu trúc, số liệu Prometheus, dấu vết OpenTelemetry, cảnh báo tự động.
3. **Security:** Vault/KMS for secrets, RBAC, PII handling.
3. **Bảo mật:** Vault/KMS cho bảo mật (secrets), RBAC, xử lý PII.
4. **Performance:** Latency SLAs, memory management.
4. **Hiệu suất:** SLAs về độ trễ, quản lý bộ nhớ.
5. **Operations:** Automated CI/CD, disaster recovery plans, load testing.
5. **Vận hành:** CI/CD tự động, kế hoạch phục hồi sau thảm họa, kiểm thử tải (load testing).

*Crucial Rule:* The Production Readiness checklist must be automated in the CI pipeline, not reliant on human memory.
*Quy tắc Quan trọng:* Bảng kiểm tra Sự Sẵn sàng cho Production phải được tự động hóa trong pipeline CI, không nên dựa vào trí nhớ của con người.

## Key Takeaways
## Những Điểm Chính
1. **Integration:** Integration is where "works on my machine" meets reality. Always test integration points heavily before production.
1. **Tích hợp:** Tích hợp là nơi khái niệm "chạy được trên máy của tôi" đối mặt với thực tế. Luôn kiểm thử các điểm tích hợp thật kỹ trước khi đưa lên production.
2. **Automation:** Checklists for production readiness must be automated.
2. **Tự động hóa:** Các bảng kiểm tra mức độ sẵn sàng cho production phải được tự động hóa.
3. **Platform Mindset:** A platform implies other teams consume it. Clear API contracts, SLAs, and documentation are more important than isolated internal code quality.
3. **Tư duy Nền tảng:** Một nền tảng có nghĩa là các nhóm khác sẽ tiêu thụ nó. Các hợp đồng API rõ ràng, SLAs và tài liệu quan trọng hơn chất lượng mã nguồn nội bộ bị cô lập.


## Liên kết
## Links
- [[day28_overview]]
