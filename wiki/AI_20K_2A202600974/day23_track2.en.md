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

---

### Day 23 Review Questions

1. **According to the lecture, besides the traditional golden signals, what additional signals do LLMs need to ensure observability?**  
   - A. Latency, traffic, errors, saturation  
     *A. Latency, traffic, errors, saturation*  
   - B. Token throughput, hallucination rate, output length distribution, tool-call failure rate  
     *B. Token throughput, hallucination rate, output length distribution, tool-call failure rate*  
   - C. CPU usage, memory usage, disk I/O  
     *C. CPU usage, memory usage, disk I/O*  
   - D. Number of users, number of requests, status codes  
     *D. Number of users, number of requests, status codes*  
   **Answer:** B  

2. **Cardinality is the “silent bill killer” because:**  
   - A. It increases system latency  
   - B. It increases the number of unique label combinations, leading to high storage and processing costs  
   - C. It reduces the number of collectable metrics  
   - D. It causes errors when using Prometheus  
   **Answer:** B  

3. **The evolution from DevOps to AgentOps described in “The Ops Trinity” includes:**  
   - A. DevOps → MLOps → LLMOps → AgentOps  
     *A. DevOps → MLOps → LLMOps → AgentOps*  
   - B. DevOps → LLMOps → MLOps → AgentOps  
     *B. DevOps → LLMOps → MLOps → AgentOps*  
   - C. DevOps → AgentOps → MLOps → LLMOps  
     *C. DevOps → AgentOps → MLOps → LLMOps*  
   - D. MLOps → DevOps → LLMOps → AgentOps  
     *D. MLOps → DevOps → LLMOps → AgentOps*  
   **Answer:** A  

4. **According to the lecture, telemetry from previous days is integrated into Day 23, for example:**  
   - A. Day 16: Spark UI metrics  
   - B. Day 19: GPU util (DCGM)  
   - C. Day 22: Eval-pass-rate as a Prometheus gauge  
   - D. Day 17: llama.cpp tokens/sec  
   **Answer:** C
