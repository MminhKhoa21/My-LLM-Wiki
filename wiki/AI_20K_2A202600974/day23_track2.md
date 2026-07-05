---
type: summary
title: "Day 23 – Track 2: Observability & AIOps Stack"
description: "Kiến trúc quan sát hệ thống AI toàn diện: từ metrics/logs/traces truyền thống đến LLM-Native Signals, MLOps, LLMOps và AgentOps."
tags: [ai, 20k, day23, track2, observability, mlops, llmops, agentops]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/day23-monitoring-observability-stack-lecture.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]

# Day 23 – Track 2: Observability & AIOps Stack

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 2 · Ngày 23

> **Câu hỏi trọng tâm**: Model chạy tốt hôm qua – hôm nay accuracy drop 20%. Bạn phát hiện được không, và bao lâu? Observability không phải nice-to-have – đó là **survival**.

## 1. Tại Sao AI Cần Observability Khác Biệt?
Traditional Golden Signals (latency/traffic/errors/saturation) chỉ phủ ~50% của AI failure surface. HTTP-200 OK vẫn có thể chứa hallucination, bị prompt injection, hoặc đốt $5/request cho một vòng lặp vô hạn.

**LLM-Native Signals (The New RED cho LLM Services):**
- **Token throughput**: input + output tokens/sec.
- **Hallucination / Quality rate**: Đánh giá bằng LLM-as-Judge hoặc regex.
- **Output length distribution**: Histogram theo dõi tokens/response.
- **Tool-call failure rate**: Theo dõi agent failed ở các tools.

> **Cardinality: The Silent Bill Killer** 
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
- **Day 16 (Cloud Infra)**: `node_exporter` + cAdvisor.
- **Day 17 (Data pipeline)**: Airflow DAG metrics via `statsd_exporter`.
- **Day 18 (Data Lakehouse)**: Spark UI metrics.
- **Day 19 (Vector Store)**: Qdrant `/metrics`, embedding drift.
- **Day 20 (Model Serving)**: llama.cpp tokens/sec, GPU util (DCGM).
- **Day 22 (Evals)**: Eval-pass-rate (Prometheus gauge).

## 5. Liên Kết
- [[day10_overview]] – Data Pipeline & Data Observability
- [[day13_overview]] – Monitoring & Logging 
- [[day27_track2]] – Data Observability & Lineage
- [[day23_overview]]
