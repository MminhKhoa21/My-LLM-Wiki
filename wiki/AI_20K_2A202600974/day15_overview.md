---
type: overview
title: "Day 15 – Retrospective & Track Decision"
description: "Ngày cuối Phase 1: nhìn lại 14 ngày, tổng hợp bài học thực tế, và chọn hướng chuyên sâu (Track) cho Phase 2."
tags: [ai, 20k, day15, retrospective]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/15/day15-slide.pdf", "raw/AI_20K_2A202600974/15/day15-trien-khai-thuc-te-dinh-huong.pdf", "raw/AI_20K_2A202600974/15/day15-activity-guide.pdf"]
---
# Day 15 – Retrospective & Track Decision

> **Day 15 is a special day**: No new technical content. It is a day to look back at the entire Phase 1 journey and make a Track decision for Phase 2.
>  
> *Ngày 15 là ngày đặc biệt: Không có nội dung kỹ thuật mới. Đây là ngày nhìn lại toàn bộ hành trình Phase 1 và đưa ra quyết định chọn Track cho Phase 2.*

---

## Full-day Schedule

| Time<br>*Giờ* | Block<br>*Khối* | Content<br>*Nội dung* |
|-----|------|---------|
| 09:00–09:30 | A0 | Opening + working principles<br>*Mở đầu + nguyên tắc làm việc* |
| 09:30–10:00 | A1 | Personal retrospective (Solo)<br>*Nhìn lại cá nhân (Solo)* |
| 10:00–11:30 | A2 | Group retrospective<br>*Nhìn lại theo nhóm (Group Retro)* |
| 11:40–12:20 | A3 | Sharing with the class<br>*Chia sẻ trước lớp* |
| Afternoon<br>*Chiều* | A4–A5 | Track Landscape + Track Decision<br>*Bản đồ các Track + Quyết định chọn Track* |

---

## Morning: Phase 1 Retrospective

**Big idea**: The 15 days of Phase 1 form **one complete AI system**, not 15 separate topics.

*Big idea: 15 ngày của Phase 1 hợp thành **một hệ thống AI hoàn chỉnh**, không phải 15 chủ đề rời.*

A look back at the 14-day journey:

*Hành trình 14 ngày nhìn lại:*

- Foundation: How LLMs work, problems, Agents, Tool Calls
  *Nền tảng: LLM hoạt động thế nào, bài toán, Agent, Tool Call*
- System building: RAG Pipeline, Multi-Agent, MCP/A2A
  *Xây dựng hệ thống: RAG Pipeline, Multi-Agent, MCP/A2A*
- Going to production: Deploy, Monitoring, Guardrails, AI Evals
  *Đưa vào production: Deploy, Monitoring, Guardrails, AI Evals*

---

## Enterprise Deployment (Final Lecture of Phase 1)

**Challenges when bringing AI into enterprises**:

*Thách thức khi đưa AI vào doanh nghiệp:*

| Challenge<br>*Thách thức* | Solution<br>*Giải pháp* |
|-----------|----------|
| Security & Compliance<br>*Bảo mật & Tuân thủ* | Zero-trust, audit trail, RBAC |
| Legacy systems<br>*Hệ thống cũ* | API gateway, phased migration<br>*API gateway, di chuyển theo giai đoạn* |
| Cost management<br>*Quản lý chi phí* | Model routing, caching, prompt compression<br>*Định tuyến mô hình, bộ nhớ đệm, nén prompt* |
| Scaling<br>*Mở rộng* | Stateless agent, request queue, SLA/Uptime<br>*Agent không trạng thái, hàng đợi yêu cầu, SLA/Uptime* |

**Cloud strategy**:

- **Cloud API** (OpenAI, Anthropic): Fast, easy, but data stays with the cloud provider
  *Nhanh, dễ, nhưng dữ liệu ở nhà cung cấp đám mây*
- **On-premise**: Full control, but high infrastructure cost
  *Kiểm soát hoàn toàn, nhưng tốn hạ tầng*
- **Hybrid**: Sensitive data on-prem, general workload on cloud
  *Dữ liệu nhạy cảm on-prem, khối lượng công việc chung trên cloud*

---

## Afternoon: Track Decision

Students read the landscape of AI directions, compare with their own learning journey, and choose a Phase 2 Track.

*Học viên đọc bản đồ các hướng đi trong AI, đối chiếu với hành trình học của mình, và chọn Track Phase 2.*

### Phase 2 Tracks (3 Tracks):

| Track | Name<br>*Tên* | Suitable for<br>*Phù hợp với* |
|-------|-----|-------------|
| **Track 1** | AI Business & Product | PM, Business Analyst, Founder |
| **Track 2** | AI Infrastructure & Data | Data Engineer, MLOps, DevOps |
| **Track 3** | AI Application & Engineering | AI Engineer, Software Engineer |

> **Outcome**: Each student completes a **Track Decision Memo** clearly stating the reasons for their track choice.
>  
> *Kết quả: Mỗi học viên hoàn thành một **Track Decision Memo** ghi rõ lý do chọn track.*

---

## Additional Materials in the Folder

- `2026_Work_Trend_Index_Annual_Report`: Microsoft 2026 Work Trends Report – market reference
  *Báo cáo xu hướng công việc Microsoft 2026 – tham khảo thị trường*
- `ITviec_Salary_Report_2025_2026_VN`: IT Vietnam Salary Report – career path guidance
  *Báo cáo lương IT Việt Nam – định hướng career path*

---

## Links
- **Previous**: [[day14_overview]] – AI Evaluation & Benchmarking (last technical day of Phase 1)
  *Ngược lại: [[day14_overview]] – AI Evaluation & Benchmarking (ngày cuối nội dung kỹ thuật Phase 1)*
- **Next**: [[day16_overview]] – First day of Phase 2 (3 official tracks split)
  *Tiếp theo: [[day16_overview]] – Ngày đầu Phase 2 (3 tracks chính thức tách biệt)*
