---
type: summary
title: "Day 23 – Track 2: Observability & AIOps Stack"
description: "Kiến trúc quan sát hệ thống AI toàn diện: từ metrics/logs/traces truyền thống đến LLM-Native Signals, MLOps, LLMOps và AgentOps."
tags: [ai, 20k, day23, track2, observability, mlops, llmops, agentops]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/day23-monitoring-observability-stack-lecture.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]


**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 2 · Ngày 23

> **Câu hỏi trọng tâm**: Model chạy tốt hôm qua – hôm nay accuracy drop 20%. Bạn phát hiện được không, và bao lâu? Observability không phải nice-to-have – đó là **survival**.

## 1. Tại Sao AI Cần Observability Khác Biệt?
Traditional Golden Signals (latency/traffic/errors/saturation) chỉ phủ ~50% của AI failure surface. HTTP-200 OK vẫn có thể chứa hallucination, bị prompt injection, hoặc đốt $5/request cho một vòng lặp vô hạn.

- **Hallucination / Quality rate**: Đánh giá bằng LLM-as-Judge hoặc regex.
- **Output length distribution**: Histogram theo dõi tokens/response.
- **Tool-call failure rate**: Theo dõi agent failed ở các tools.

> Cardinality là số lượng unique label combinations (ví dụ: request có user, endpoint, status). Tránh dùng `user_id`, `request_id`, `prompt_hash` trong metrics (chỉ nên < 10K series / metric).

## 2. Các Trụ Cột Observability
- **Metrics**: Số đo hiệu năng theo thời gian. Sử dụng Prometheus (v3.x hỗ trợ Native histograms, OTLP receiver). Long-term storage bằng VictoriaMetrics, Grafana Mimir, hoặc Thanos.
- **Logs**: Bản ghi sự kiện chi tiết. Sử dụng Loki hoặc Elasticsearch.
- **Traces**: Theo dõi request qua nhiều service. OpenTelemetry (OTel) và Jaeger.

## 3. Phân Tầng Ops (The Ops Trinity)

Sự tiến hóa từ DevOps lên AgentOps:
- **DevOps**: CI/CD, Containerization, Infrastructure as Code, Metrics/Logs truyền thống.
- **MLOps**: Thêm Model Lifecycle, Data pipeline, Model Registry, Training pipeline, Drift Detection (Ví dụ: Evidently đo Data Drift).
- **LLMOps**: Quản lý Prompts (prompt-as-code), Eval-driven dev, RAGOps, Fine-tuning Ops (PeFT), LLM Gateway (routing & cost control).
- **AgentOps**: Quản lý Agent reliability (pass@k), Memory management, MCP/A2A ops, Frameworks (LangGraph orchestrator), Governance/Guardrails.

## 4. Tích Hợp Telemetry Toàn Diện
Day 23 là ngày tích hợp mọi artifact từ các bài trước:

## 5. Liên Kết

---

### *Câu hỏi ôn tập Ngày 23*

   Theo bài giảng, ngoài các golden signals truyền thống, LLM cần thêm những tín hiệu nào để đảm bảo observability?
   ***Đáp án:** B*

   Cardinality là “kẻ giết hóa đơn thầm lặng” vì:
     A. Nó làm tăng độ trễ của hệ thống
     B. Nó làm tăng số lượng unique label combinations, dẫn đến chi phí lưu trữ và xử lý cao
     C. Nó làm giảm số lượng metrics có thể thu thập
     D. Nó gây lỗi khi sử dụng Prometheus
   ***Đáp án:** B*

   Sự tiến hóa từ DevOps lên AgentOps được mô tả trong “The Ops Trinity” bao gồm:
   ***Đáp án:** A*

   Theo bài giảng, telemetry từ các ngày trước được tích hợp vào Day 23, ví dụ:
     A. Ngày 16: Spark UI metrics
     B. Ngày 19: GPU util (DCGM)
     C. Ngày 22: Eval-pass-rate dưới dạng Prometheus gauge
     D. Ngày 17: llama.cpp tokens/sec
   ***Đáp án:** C*
