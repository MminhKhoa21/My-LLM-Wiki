---
type: summary
title: "Day 23 – Track 2: Observability & AIOps Stack"
description: "Kiến trúc quan sát hệ thống AI toàn diện: từ metrics/logs/traces truyền thống đến LLM-Native Signals, MLOps, LLMOps và AgentOps."
tags: [ai, 20k, day23, track2, observability, mlops, llmops, agentops]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/day23-monitoring-observability-stack-lecture.pdf"]
---


# Day 23 – Track 2: Observability & AIOps Stack




**LLM-Native Signals (The New RED cho LLM Services):**
- **Token throughput**: input + output tokens/sec.

> **Cardinality: The Silent Bill Killer** 




- **Day 16 (Cloud Infra)**: `node_exporter` + cAdvisor.
- **Day 17 (Data pipeline)**: Airflow DAG metrics via `statsd_exporter`.
- **Day 18 (Data Lakehouse)**: Spark UI metrics.
- **Day 19 (Vector Store)**: Qdrant `/metrics`, embedding drift.
- **Day 20 (Model Serving)**: llama.cpp tokens/sec, GPU util (DCGM).
- **Day 22 (Evals)**: Eval-pass-rate (Prometheus gauge).

- [[day10_overview]] – Data Pipeline & Data Observability
- [[day13_overview]] – Monitoring & Logging 
- [[day27_track2]] – Data Observability & Lineage
- [[day23_overview]]
