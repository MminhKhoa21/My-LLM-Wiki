---
type: summary
title: "Track 2: AI Infrastructure & Data (Phase 2)"
description: "Chi tiết về Track 2 - AI Infrastructure & Data, tập trung vào xây dựng và vận hành hạ tầng AI production."
tags: [ai, 20k, day15, track2, infrastructure, data]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/15/day15-activity-guide.pdf", "../raw/AI_20K_2A202600974/15/day15-trien-khai-thuc-te-dinh-huong.pdf"]
---
# Track 2: Hạ tầng AI & Dữ liệu (Giai đoạn 2)

## Tổng quan

Track 2 đào tạo các kỹ sư hạ tầng và platform AI, tập trung vào khả năng tự dựng và vận hành backend của một hệ AI ở mức độ production.

Nội dung chính bao gồm:

- Lakehouse & Feature Store. (Hồ dữ liệu & Kho tính năng)
- vLLM deployment & optimization. (Triển khai & tối ưu vLLM)
- GPU FinOps & quản lý chi phí (đặc biệt là token cost).
- Production data pipeline. (Đường ống dữ liệu sản xuất)

## Tín hiệu phù hợp

Track này phù hợp nếu bạn:

- Ở Phase 1 (Day 7, Day 10, Day 12), bạn thấy hứng thú với việc làm data pipeline, observability và deploy.
- Quen thuộc và thích làm việc với CLI / Docker / CI.
- Có tư duy về SLA / SLO / P95 / Chi phí.
- Thích xây dựng hệ thống chạy ổn định và tin cậy hơn là thêm tính năng mới.

## Năng lực sẽ xây dựng

- Serving & Scaling (triển khai các model lớn).
- CI/CD cho môi trường AI.

## Khó khăn / Thách thức

- Khối kiến thức hạ tầng rất rộng, đòi hỏi sự kiên nhẫn với các chi tiết vận hành.
- Ít thứ "đẹp" hoặc UI/UX để demo.
- Áp lực về độ tin cậy của hệ thống (on-call).
- Đường học DevOps dốc, cần nền tảng vững vàng.
- ***Điều kiện cứng:** Cần có GPU hoặc Cloud free-tier để thực hành các lab về serving và FinOps.*

## Career Path & Cơ hội

- ***Vai trò mục tiêu (CP2):** AI Data Engineer, Platform Engineer, MLOps Engineer.*
- ***Nhu cầu thị trường:** **Rất cao.** Đặc biệt khi các doanh nghiệp muốn tự chủ mô hình, tối ưu chi phí và đưa AI vào production thay vì chỉ dùng API.*

---

### *Câu hỏi ôn tập Ngày 15*

   Track 2 (AI Infrastructure & Data) trong Phase 2 tập trung đào tạo kỹ năng gì?
     A. Phát triển mô hình AI mới và tối ưu hóa kiến trúc
     B. Tự dựng và vận hành backend của hệ thống AI ở mức production
     C. Thiết kế UI/UX cho ứng dụng AI
     D. Xây dựng chiến lược kinh doanh sản phẩm AI
   ***Đáp án:** B*

   Điều kiện cứng nào được đề cập để có thể thực hành các lab về serving và FinOps trong Track 2?
     A. Có tài khoản GitHub Enterprise
     B. Cần có GPU hoặc Cloud free-tier
     C. Phải có chứng chỉ Kubernetes
     D. Cần có máy tính có RAM > 32GB
   ***Đáp án:** B*

   Vai trò mục tiêu (CP2) nào sau đây được đề cập trong bài giảng là phù hợp với Track 2?
   ***Đáp án:** C*

   Theo bài giảng, Track 2 phù hợp với những người có tư duy về các khái niệm nào dưới đây?
     A. UI/UX, trải nghiệm người dùng, A/B testing
     B. SLA, SLO, P95, Chi phí
     C. Thiết kế đồ họa, animation, storytelling
   ***Đáp án:** B*
