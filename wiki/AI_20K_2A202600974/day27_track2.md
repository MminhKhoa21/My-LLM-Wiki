---
type: summary
title: "Day 27 – Track 2: Data Observability & Lineage"
description: "Quan sát chính DỮ LIỆU (không chỉ hệ thống): 7 chiều observability, data contracts, OpenLineage, drift detection."
tags: [ai, 20k, day27, track2, data-observability, lineage, data-quality]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/27/day27-data-observability-lineage.pdf", "raw/AI_20K_2A202600974/27/Day27 - Track 2 - Data-observability-lineage.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]


# Day 27 – Track 2: Data Observability & Lineage

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 2 · Ngày 27

> **Reality check**: 74% đội ngũ data nói người đầu tiên phát hiện dữ liệu sai là **business stakeholder** – không phải hệ thống giám sát. Dashboard xanh ≠ dữ liệu đúng.

---

## Ranh giới với Ngày 23

| Ngày 23 | Ngày 27 |
|---------|---------|
| Quan sát **HỆ THỐNG** (service healthy?) | Quan sát **DỮ LIỆU** (data đúng/tươi/đầy đủ?) |
| Prometheus, Grafana, logs | Great Expectations, Soda, Monte Carlo |

---

## 7 Chiều của Data Observability

| Chiều | Câu hỏi | Công cụ |
|-------|---------|---------|
| **Freshness** | Dữ liệu có cập nhật kịp thời không? | dbt, Airflow |
| **Distribution** | Giá trị có phân phối bất thường không? | Great Expectations |
| **Volume** | Số records thay đổi đột ngột không? | Monte Carlo |
| **Schema** | Cấu trúc có drift không? | dbt schema tests |
| **Lineage** | Dữ liệu đến từ đâu? Đi đến đâu? | OpenLineage |
| **Uniqueness** | Có duplicate không? | Soda |
| **Completeness** | Có null value bất thường không? | Great Expectations |

---

## Drift & Anomaly Detection

| Phương pháp | Dùng khi |
|------------|---------|
| **PSI** (Population Stability Index) | Detect feature distribution shift |
| **KS test** | So sánh 2 distributions |
| **KL Divergence** | Đo "khoảng cách" giữa distributions |
| **MMD** (Maximum Mean Discrepancy) | High-dimensional data drift |

---

## Data Contracts – ODCS Standard

Data Contract là **thỏa thuận chính thức** giữa data producer và consumer:

```yaml
# data-contract.yaml (ODCS format)
apiVersion: v2.3.0
kind: DataContract
metadata:
  name: orders_daily
  owner: data-team@company.com
models:
  - name: orders
    fields:
      - name: order_id
        type: string
        required: true
        unique: true
      - name: amount
        type: number
        minimum: 0
```

---

## Lineage với OpenLineage

```python
from openlineage.client import OpenLineageClient

client = OpenLineageClient(url="http://lineage-server:5000")

# Emit lineage event khi pipeline chạy
client.emit(RunEvent(
    eventType=RunState.START,
    inputs=[Dataset(namespace="postgres", name="raw_orders")],
    outputs=[Dataset(namespace="snowflake", name="orders_daily")]
))
```

---

## AI Infrastructure Observability

| Loại | Vấn đề cần quan sát |
|------|-------------------|
| **Feature Store** | Training-serving skew |
| **Vector/Embedding** | Embedding drift, stale vectors |
| **Training data** | Label drift, data poisoning |
| **LLM data** | Prompt quality, context relevance |
| **Agent data** | Tool call patterns, state corruption |

---

## Liên kết
- [[day10_overview]] – Data Pipeline & Observability (nền tảng)
- [[day23_track2]] – System Observability
- [[day24_track2]] – Data Governance & Security
- [[day27_overview]]
