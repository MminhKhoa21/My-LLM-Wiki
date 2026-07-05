---
type: summary
title: "Summary: AI Product Mini-Hackathon Day 06"
description: "Chi tiết lộ trình, các checkpoint và tiêu chí đánh giá trong ngày AI Product Mini-Hackathon (Day 06)."
tags: [ai, 20k, day6, hackathon, product]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/6/2-day06-lecture-slides-batch02.pdf"]
---

# Summary: AI Product Mini-Hackathon Day 06

**Nguồn:** [[2-day06-lecture-slides-batch02]]

Tài liệu này tóm tắt chi tiết lịch trình, các mốc kiểm tra (checkpoint) và tiêu chí đánh giá cho sự kiện AI Product Mini-Hackathon trong khuôn khổ Day 06 của khoá học. 

Quy trình phát triển chính được nhấn mạnh: **SPEC $\rightarrow$ Prototype $\rightarrow$ Demo**.

## 1. Lộ trình Hackathon & Các Checkpoint

### 09:00 $\rightarrow$ 11:00 | BUILD (Checkpoint 1)
- **Mục tiêu:** Xây dựng Mockup / Prototype chạy được.
- **Yêu cầu:** Dựng mockup đủ luồng end-to-end bao gồm cả *happy path* và *error path*, giai đoạn này chưa cần gắn AI thực tế.
- **Phân chia công việc:** Nhóm cần chia task rõ ràng: vẽ flow, dựng mockup, thu thập data, tối ưu prompt, và code phần AI.
- **Outcome Checkpoint 1:** Chọn được 1 flow lõi để chuẩn bị gắn AI; mockup/prototype cơ bản đã sẵn sàng.

### 11:00 $\rightarrow$ 13:00 | LẮP AI VÀO FLOW (Checkpoint 2)
- **Mục tiêu:** Cắm AI thật vào luồng chính.
- **Yêu cầu:** Tích hợp AI vào ít nhất 1 flow cốt lõi đã chọn.
- **Kiểm thử:** Test bằng input thật và ghi lại những tính năng / thành phần chưa hoạt động đúng kỳ vọng.
- **Outcome Checkpoint 2:** Prototype đã có AI chạy thực tế trong ít nhất 1 flow.

### 13:00 $\rightarrow$ 14:00 | BREAK
- **Mục tiêu:** Nghỉ ngơi, nạp lại năng lượng.
- **Ghi chú:** Rời khỏi màn hình máy tính, đồng thời bắt đầu phác thảo câu chuyện (story) để trình bày demo trong đầu.

### 14:00 $\rightarrow$ 15:30 | POLISH + DEMO PREP (Checkpoint 3)
- **Mục tiêu:** Hoàn thiện sản phẩm và chuẩn bị tài liệu demo, slide thuyết trình.
- **Hoạt động:** 
  - Test luồng AI với các kịch bản khác nhau.
  - Ưu tiên sửa các lỗi nghiêm trọng ảnh hưởng đến luồng demo (demo-critical bugs).
  - Tối ưu lại UI/UX.
  - Viết nháp slide theo cấu trúc: **Vấn đề $\rightarrow$ Giải pháp $\rightarrow$ Demo**.
- **Outcome Checkpoint 3:** Slide và tài liệu demo đã hoàn thiện.

### 15:30 $\rightarrow$ 16:00 | FINAL PREP
- **Mục tiêu:** Tổng duyệt trước khi bước vào Demo Round.
- **Hoạt động:** Chạy thử demo các kịch bản, chuẩn bị screenshot dự phòng, deploy bản demo (nếu có thể - bonus) và phân vai thuyết trình trong nhóm.

---

## 2. Demo Round & Tiêu chí Đánh giá (Evaluation Criteria)

Vào lúc **16:00**, các nhóm sẽ bắt đầu **Demo Round**. Mỗi nhóm có 10 phút để thuyết trình và trả lời câu hỏi, tập trung kể chuyện và đưa ra bằng chứng thuyết phục. Mỗi cá nhân sẽ đánh giá chéo cho các nhóm khác trong cùng zone.

**Các tiêu chí đánh giá chính:**

1. **Product Canvas & Problem-Solution Fit:**
   - Ý tưởng rõ ràng, xác định đúng pain point của người dùng.
   - Giả thuyết đưa ra thuyết phục và có dẫn chứng thực tế.
2. **Demo End-to-end:**
   - Phải trình diễn được cả *happy case* lẫn *error case*.
   - Sản phẩm chạy mượt mà, không gặp lỗi trong quá trình demo.
3. **Mức độ ứng dụng AI:**
   - AI được chạy thật trong ít nhất 1 flow.
   - AI được sử dụng "đúng chỗ, đúng mức độ", giải quyết đúng vấn đề thay vì chỉ "gắn AI cho có".
   - (Bonus) Có đường link demo để mọi người cùng test.
4. **Kỹ năng thuyết trình (Presentation):**
   - Trình bày rõ ràng, mạch lạc, làm nổi bật được pain point.
5. **UI & UX:**
   - Giao diện thân thiện và trải nghiệm người dùng tốt.
