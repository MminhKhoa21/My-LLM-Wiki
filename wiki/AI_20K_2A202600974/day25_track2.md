---
type: summary
title: "Day 25 – Track 2: GPU FinOps & Cost Optimization"
description: "Phân tích và tối ưu chi phí GPU cloud cho AI workloads: spot instances, right-sizing, inference optimization, FinOps governance."
tags: [ai, 20k, day25, track2, gpu, finops, cost-optimization]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/25/Day25 - Track 2 - Gpu-finops-cost-optimization.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]


# Day 25 – Track 2: GPU FinOps & Cost Optimization

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 2 · Ngày 25

> **Case study**: 4x A100 idle overnight (12h) = $144 wasted/day = **$52,560/year**. Hôm nay học cách cắt giảm **40–60% chi phí GPU**.

---

## Mục tiêu

1. Phân tích chi phí GPU cloud và phát hiện lãng phí
2. Áp dụng spot/preemptible instances với checkpoint strategy
3. Tối ưu inference cost bằng batching, caching, model cascading
4. Thiết kế cost allocation & FinOps review process cho team

---

## GPU Cloud Cost Anatomy

```
Tổng chi phí = Compute + Storage + Network + Support
             = (GPU hours × GPU price) + (storage GB × price) + ...
```

**Các nguồn lãng phí phổ biến**:
- GPU idle khi không có request (underutilization)
- Over-provisioning (chọn GPU lớn hơn cần)
- Dev/test chạy trên production GPU tier
- Data transfer giữa regions

---

## Spot & Preemptible Instances

| Instance type | Giá | Rủi ro | Phù hợp |
|--------------|-----|--------|---------|
| **On-demand** | 100% | Không bị interrupt | Production serving |
| **Spot/Preemptible** | 30–70% rẻ hơn | Có thể bị revoke | Training, batch jobs |
| **Reserved** | 40–60% rẻ hơn | Lock-in 1–3 năm | Stable serving |

**Checkpoint strategy với Spot**: Lưu model checkpoint mỗi N steps → khi bị interrupt, resume từ checkpoint gần nhất.

---

## Inference Cost Optimization

| Kỹ thuật | Giảm cost | Cách hoạt động |
|---------|----------|---------------|
| **Dynamic batching** | 2–5x | Gộp nhiều request cùng lúc |
| **KV-cache** | 30–50% | Cache attention keys/values |
| **Model cascading** | 40–60% | Dùng model nhỏ trước, model lớn khi cần |
| **Quantization (INT8/INT4)** | 50–75% VRAM | Giảm precision của weights |

---

## FinOps Review Process

1. **Weekly**: Review cost dashboard, flag anomalies
2. **Monthly**: Cost allocation report theo team/project
3. **Quarterly**: Rightsizing review, reserved instance strategy
4. **Annually**: Architecture review, technology refresh

---

## Sustainable AI: Carbon & Energy

- Track **PUE** (Power Usage Effectiveness) của data center
- Chọn regions có **renewable energy** cao (us-west-2, eu-north-1)
- Tắt GPU instances khi không dùng với **auto-shutdown policies**

---

## Liên kết
- [[day12_overview]] – Deployment (foundation)
- [[day25_track1]] – AI Product & Team
- [[day25_overview]]
