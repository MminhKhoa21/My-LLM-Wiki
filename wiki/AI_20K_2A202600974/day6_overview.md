---
type: overview
title: "Day 6 Overview - AI Product Mini-Hackathon"
description: "Quy trình thực hành AI Product Mini-Hackathon từ lên Spec, vẽ Workflow, đến Prototype."
tags: [ai, 20k, day6]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/6/2-day06-lecture-slides-batch02.pdf"]
---

# Day 6: AI Product Mini-Hackathon

## 1. Quy trình Mini-Hackathon
Mini-Hackathon tập trung vào việc áp dụng kiến thức từ các bài học trước vào việc xây dựng một bản nháp sản phẩm AI thực tế. Lộ trình chung:
**SPEC -> Prototype -> Demo**

## 2. Các giai đoạn cụ thể
1. **Khám phá và Lựa chọn bài toán (Problem Scan)**:
   - Các nhóm chọn 1 track (lĩnh vực: Xe hơi, Y tế, Giáo dục, Vận tải, Tự do).
   - Liệt kê các điểm đau (pain points).
   - Lọc các bài toán bằng "Thang đo 4 câu hỏi": Có cần AI? Mức độ giải pháp? Ranh giới? Quyết định Go/No-go?

2. **Xây dựng SPEC (AI Product Canvas)**:
   - **Value**: Xác định User, Pain point, Augmentation hay Automation, và giá trị thực sự mang lại.
   - **Trust**: Chiến lược đánh giá (Precision/Recall), cách xử lý khi AI sai, cách phục hồi niềm tin (Trust recovery).
   - **Feasibility**: Rủi ro lớn nhất, dependency, ước tính cost và latency.
   - Thêm vào đó là **Learning Signal** (Cơ chế thu thập feedback để tạo Data Flywheel).

3. **Thiết kế Workflow và UX**:
   - Chỉ ra các Use Cases/Stories cụ thể (Happy path, Low-confidence path, Failure path, Correction path).
   - Vẽ luồng chạy của AI (Flowchart).

4. **Xây dựng Prototype (Build & Polish)**:
   - Dựng các mockup (vẽ tay hoặc dùng UI tool).
   - Chạy thử prompt / flow trên các tool thô (ChatGPT, Claude, hoặc mã Python đơn giản) để xác nhận khả thi.

5. **Demo và Đánh giá**:
   - Trình bày bài toán rõ ràng, mạch lạc.
   - Chứng minh được "Problem-Solution Fit".
   - Demo luồng hoạt động. Chú trọng vào việc AI dùng đúng lúc, đúng chỗ.
