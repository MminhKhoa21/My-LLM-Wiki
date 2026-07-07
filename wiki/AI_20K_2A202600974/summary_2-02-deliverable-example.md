---
type: summary
title: "Summary: Day 02 Deliverable Example"
description: "A summary of the Day 02 lab deliverable example detailing problem discovery, workflow mapping, and AI decision making."
tags: [Lab Example, Workflow, Problem Statement, Delivery]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/2-02-deliverable-example.pdf"]
---

# Summary: Day 02 Deliverable Example
# Tóm tắt: Ví dụ về Sản phẩm chuyển giao Ngày 02

## Overview
## Tổng quan
This document provides a complete example of the Day 02 lab assignment. It walks through the journey of a Junior Product Manager named Minh as he performs problem scanning, designs current and future workflows, drafts a Problem Statement, and ultimately decides on implementing an AI Workflow solution for automating weekly reports.

Tài liệu này cung cấp một ví dụ hoàn chỉnh về bài tập thực hành Ngày 02. Nó đi qua hành trình của một Giám đốc Sản phẩm Tập sự (Junior Product Manager) tên là Minh khi anh thực hiện rà soát vấn đề, thiết kế quy trình làm việc hiện tại và tương lai, phác thảo Tuyên bố Vấn đề (Problem Statement) và cuối cùng quyết định triển khai giải pháp Quy trình AI (AI Workflow) để tự động hóa các báo cáo hàng tuần.

## Key Phases
## Các Giai đoạn Chính

### Phase 1: Individual Problem Scan
### Giai đoạn 1: Rà soát Vấn đề Cá nhân
- Minh lists various daily pain points using different lenses (repetitive tasks, time-consuming tasks, areas where AI could excel, and pains experienced by others).
  Minh liệt kê các điểm nghẽn (pain points) hàng ngày khác nhau bằng cách sử dụng nhiều góc nhìn khác nhau (các tác vụ lặp đi lặp lại, các tác vụ tốn thời gian, các lĩnh vực mà AI có thể xuất sắc và những khó khăn mà người khác gặp phải).
- Examples include summarizing Jira/Slack for weekly reports, reviewing PRDs, searching Slack for past decisions, and writing meeting notes.
  Các ví dụ bao gồm tóm tắt Jira/Slack cho báo cáo hàng tuần, xem xét PRD, tìm kiếm trên Slack các quyết định trong quá khứ và viết biên bản cuộc họp.
- **Top Candidates Selected:** Weekly Report, PRD Review, and Slack Search.
  **Các Ứng viên Hàng đầu Được Chọn:** Báo cáo Hàng tuần, Đánh giá PRD và Tìm kiếm trên Slack.

### Phase 2: Group Problem Statement (Convergence)
### Giai đoạn 2: Tuyên bố Vấn đề Nhóm (Sự hội tụ)
- The group aggregates individual ideas and scores them based on clarity of actor, workflow, pain evidence, measurable impact, lab feasibility, and domain understanding.
  Nhóm tổng hợp các ý tưởng cá nhân và chấm điểm chúng dựa trên tính rõ ràng của chủ thể (actor), quy trình làm việc, bằng chứng về điểm nghẽn, tác động có thể đo lường, tính khả thi trong thực hành và hiểu biết về lĩnh vực.
- **Selected Problem:** "Weekly Report" is chosen because it has a highly structured workflow, a clear baseline metric (90 minutes), and easily measurable impact.
  **Vấn đề Được Chọn:** "Báo cáo Hàng tuần" được chọn vì nó có quy trình làm việc có cấu trúc cao, một số liệu cơ sở rõ ràng (90 phút) và tác động dễ dàng đo lường.

### Phase 3: Validation and Research
### Giai đoạn 3: Xác thực và Nghiên cứu
- The group briefly validates the problem with other PMs. They find that the true pain is not just "pulling numbers" but writing the *narrative* from raw data.
  Nhóm xác thực ngắn gọn vấn đề với các PM khác. Họ nhận ra rằng khó khăn thực sự không chỉ là "rút trích các con số" mà là viết *bài tường thuật* (narrative) từ dữ liệu thô.
- They research existing tools (e.g., Jira Reports, Slack AI, Gemini in Drive) to understand current patterns. The takeaway is that AI should assist in drafting the narrative while a human retains review control.
  Họ nghiên cứu các công cụ hiện có (ví dụ: Báo cáo Jira, Slack AI, Gemini trong Drive) để hiểu các mô hình hiện tại. Bài học rút ra là AI nên hỗ trợ soạn thảo tường thuật trong khi con người vẫn giữ quyền kiểm soát việc đánh giá.

### Phase 4: Workflow Mapping
### Giai đoạn 4: Lập bản đồ Quy trình làm việc
- **Current State (90 mins):** Export Jira -> Pull Sheets -> Read Slack -> Compile -> Write Narrative (Bottleneck) -> Format -> Send.
  **Trạng thái Hiện tại (90 phút):** Xuất Jira -> Lấy bảng tính -> Đọc Slack -> Tổng hợp -> Viết Tường thuật (Nút thắt) -> Định dạng -> Gửi.
- **Future State (21 mins):** Auto-pull data (Rule) -> Structure data (Workflow/AI) -> Draft narrative (Workflow/AI) -> PM Review & Edit (Human Boundary) -> Send.
  **Trạng thái Tương lai (21 phút):** Tự động kéo dữ liệu (Theo quy tắc) -> Cấu trúc dữ liệu (Quy trình/AI) -> Soạn thảo tường thuật (Quy trình/AI) -> PM Xem xét & Chỉnh sửa (Ranh giới Con người) -> Gửi.
- **Impact:** Decreases overall time significantly while maintaining quality through manual review.
  **Tác động:** Giảm đáng kể tổng thời gian trong khi vẫn duy trì chất lượng thông qua việc đánh giá thủ công.

### Phase 5: Problem Statement and Decision
### Giai đoạn 5: Tuyên bố Vấn đề và Quyết định
- **Problem Statement:** Defines the actor (Junior PM), workflow, bottleneck (writing narrative), impact, success metric (under 30 mins total), and strict boundaries.
  **Tuyên bố Vấn đề:** Định nghĩa chủ thể (Junior PM), quy trình làm việc, nút thắt (viết tường thuật), tác động, chỉ số thành công (tổng cộng dưới 30 phút) và các ranh giới nghiêm ngặt.
- **AI Decision:** 
  **Quyết định AI:**
  - **Rule:** Insufficient because it cannot generate dynamic narratives.
    **Quy tắc (Rule):** Không đủ vì nó không thể tạo ra các tường thuật động.
  - **Workflow:** Chosen. Linear process where AI assists specifically in drafting, with PM review.
    **Quy trình (Workflow):** Được chọn. Quá trình tuyến tính trong đó AI hỗ trợ đặc biệt trong việc soạn thảo, với sự xem xét của PM.
  - **Agent:** Rejected. Too broad, unneeded autonomy, and higher risks.
    **Tác nhân (Agent):** Bị từ chối. Quá rộng, quyền tự chủ không cần thiết và rủi ro cao hơn.
- **Final Decision:** **Go** with a small pilot using historical report data to evaluate edit time and AI hallucination rates.
  **Quyết định Cuối cùng:** **Triển khai (Go)** với một dự án thí điểm nhỏ sử dụng dữ liệu báo cáo lịch sử để đánh giá thời gian chỉnh sửa và tỷ lệ ảo giác của AI.

### Phase 6: Individual Reflection
### Giai đoạn 6: Suy ngẫm Cá nhân
- Reflects on the use of AI during the lab process (e.g., generating mermaid diagrams, brainstorming ideas) and correcting AI when it suggested overly complex Agent solutions prematurely. 
  Phản ánh về việc sử dụng AI trong quá trình thực hành (ví dụ: tạo sơ đồ mermaid, lên ý tưởng) và sửa lỗi cho AI khi nó đề xuất các giải pháp Tác nhân (Agent) quá phức tạp một cách vội vàng.
- Emphasizes that the best problems have clear workflows and metrics, and that agents are not the default answer.
  Nhấn mạnh rằng những vấn đề tốt nhất có quy trình làm việc và các chỉ số đo lường rõ ràng, và các tác nhân không phải là câu trả lời mặc định.
