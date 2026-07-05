---
type: summary
title: "Day 23 – Track 2: Observability & AIOps Stack"
description: "Kiến trúc quan sát hệ thống AI toàn diện: từ metrics/logs/traces đến LLMOps, AgentOps và AIOps."
tags: [ai, 20k, day23, track2, observability, mlops, llmops, agentops]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/day23-monitoring-observability-stack-lecture.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]


# Day 23 – Track 2: Observability & AIOps Stack

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 2 · Ngày 23

> **Câu hỏi trọng tâm**: Model chạy tốt hôm qua – hôm nay accuracy drop 20%. Bạn phát hiện được không, và bao lâu? Reality check: Phần lớn team AI chỉ biết model fail khi user phàn nàn – trung bình mất **3–5 ngày**. Observability không phải nice-to-have – đó là **survival**.

---

## Lộ trình nội dung

| Phần | Chủ đề |
|------|--------|
| §1–2 | Evolution of Observability · RED/USE Pillars |
| §3–4 | Prometheus · TSDB/Storage |
| §5–6 | Grafana/Loki · SLO/Burn-rate |
| §7 | Distributed Tracing & OpenTelemetry |
| §8–9 | GPU-Serving · eBPF/Profiling |
| §10–11 | Drift/Eval · Cost/FinOps |
| §12 | Postmortems |
| §13–14 | Agent Observability / Harness |
| §16–19 | Ops Trinity: DevOps → MLOps → LLMOps → AgentOps |
| §20 | AIOps – AI cho IT Ops |

---

## 3 Trụ cột Observability

| Trụ cột | Mô tả | Công cụ |
|---------|-------|---------|
| **Metrics** | Số đo hiệu năng theo thời gian | Prometheus, Grafana |
| **Logs** | Bản ghi sự kiện chi tiết | Loki, Elasticsearch |
| **Traces** | Theo dõi luồng request qua nhiều service | Jaeger, OpenTelemetry |

---

## Phân tầng Ops

```
DevOps → MLOps → LLMOps → AgentOps
          ↑ thêm model lifecycle
                   ↑ thêm prompt, eval, hallucination
                            ↑ thêm tool calls, loop tracing
```

---

## Liên kết
- [[day10_overview]] – Data Pipeline & Data Observability (nền tảng)
- [[day13_overview]] – Monitoring & Logging (nền tảng)
- [[day27_track2]] – Data Observability & Lineage (nâng cao)
- [[day23_overview]]
