---
type: overview
title: "Day 15 – Retrospective & Track Decision"
description: "Ngày cuối Phase 1: nhìn lại 14 ngày, tổng hợp bài học thực tế, và chọn hướng chuyên sâu (Track) cho Phase 2."
tags: [ai, 20k, day15, retrospective]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/15/day15-slide.pdf", "raw/AI_20K_2A202600974/15/day15-trien-khai-thuc-te-dinh-huong.pdf", "raw/AI_20K_2A202600974/15/day15-activity-guide.pdf"]
---

# Day 15 – Retrospective & Track Decision

> **Ngày 15 là ngày đặc biệt**: Không có nội dung kỹ thuật mới. Đây là ngày nhìn lại toàn bộ hành trình Phase 1 và đưa ra quyết định chọn Track cho Phase 2.

---

## Lịch cả ngày

| Giờ | Khối | Nội dung |
|-----|------|---------|
| 09:00–09:30 | A0 | Mở đầu + nguyên tắc làm việc |
| 09:30–10:00 | A1 | Nhìn lại cá nhân (Solo) |
| 10:00–11:30 | A2 | Nhìn lại theo nhóm (Group Retro) |
| 11:40–12:20 | A3 | Chia sẻ trước lớp |
| Chiều | A4–A5 | Track Landscape + Track Decision |

---

## Buổi sáng: Retrospective Phase 1

**Big idea**: 15 ngày của Phase 1 hợp thành **một hệ thống AI hoàn chỉnh**, không phải 15 chủ đề rời.

Hành trình 14 ngày nhìn lại:
- Nền tảng: LLM hoạt động thế nào, bài toán, Agent, Tool Call
- Xây dựng hệ thống: RAG Pipeline, Multi-Agent, MCP/A2A
- Đưa vào production: Deploy, Monitoring, Guardrails, AI Evals

---

## Triển khai Enterprise (Bài giảng cuối Phase 1)

**Thách thức khi đưa AI vào doanh nghiệp**:

| Thách thức | Giải pháp |
|-----------|----------|
| Security & Compliance | Zero-trust, audit trail, RBAC |
| Legacy systems | API gateway, phased migration |
| Cost management | Model routing, caching, prompt compression |
| Scaling | Stateless agent, request queue, SLA/Uptime |

**Cloud strategy**:
- **Cloud API** (OpenAI, Anthropic): Nhanh, dễ, nhưng data ở cloud provider
- **On-premise**: Kiểm soát hoàn toàn, nhưng tốn hạ tầng
- **Hybrid**: Dữ liệu nhạy cảm on-prem, general workload trên cloud

---

## Buổi chiều: Track Decision

Học viên đọc bản đồ các hướng đi trong AI, đối chiếu với hành trình học của mình, và chọn Track Phase 2.

### 3 Tracks Phase 2:

| Track | Tên | Phù hợp với |
|-------|-----|-------------|
| **Track 1** | AI Business & Product | PM, Business Analyst, Founder |
| **Track 2** | AI Infrastructure & Data | Data Engineer, MLOps, DevOps |
| **Track 3** | AI Application & Engineering | AI Engineer, Software Engineer |

> **Kết quả**: Mỗi học viên hoàn thành một **Track Decision Memo** ghi rõ lý do chọn track.

---

## Tài liệu bổ sung trong thư mục

- `2026_Work_Trend_Index_Annual_Report`: Báo cáo xu hướng công việc Microsoft 2026 – tham khảo thị trường
- `ITviec_Salary_Report_2025_2026_VN`: Báo cáo lương IT Việt Nam – định hướng career path

---

## Liên kết
- **Ngược lại**: [[day14_overview]] – AI Evaluation & Benchmarking (ngày cuối nội dung kỹ thuật Phase 1)
- **Tiếp theo**: [[day16_overview]] – Ngày đầu Phase 2 (3 tracks chính thức tách biệt)
