---
type: summary
title: "Day 19 Track 1: Retention, Engagement & Habit Loop"
description: "Detailed summary of Track 1 covering product retention, metrics, the Hook model, and the lab on designing user engagement."
tags: [ai, product-management, retention, engagement, habit-loop, metrics]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/1-d19-slide-v2.pdf", "raw/AI_20K_2A202600974/19/1-student-day20-v1.pdf"]
---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]

# Retention, Engagement & Habit Loop

## 1. Tổng quan các Metrics cốt lõi
- **Active User:** Người dùng được tính là "đang hoạt động" theo định nghĩa của team. Có các chỉ số phổ biến: DAU (Daily), WAU (Weekly), MAU (Monthly).
- **Activation & Retention:**
  - *Activation:* Thời điểm user lần đầu nhận được giá trị.
  - *Time to Value (TTV):* Thời gian từ lúc vào sản phẩm đến lúc nhận giá trị đầu tiên.
  - *Retention:* Tỷ lệ user quay lại sử dụng theo thời gian (ví dụ: D1 / D7 / D30 Retention).
  - *Churn:* User rời bỏ, không quay lại.
- **Engagement & Stickiness:** Mức độ gắn bó. Stickiness thường đo bằng DAU/MAU.
- **Business Metrics:** CAC (Chi phí thu hút), LTV (Giá trị vòng đời), Payback Period (Thời gian thu hồi vốn).
- **North Star Metric:** Chỉ số cốt lõi phản ánh giá trị chính mà sản phẩm tạo ra.

## 2. Vì sao Retention quan trọng?
Tăng trưởng bề mặt (Acquisition thông qua PR, ads) có thể che đậy retention kém. Retention trả lời câu hỏi: sau một thời gian nhất định, còn bao nhiêu user quay lại? Nếu retention kém từ đầu (ví dụ D1 ~10%), vấn đề thường ở **Core Value** chưa giải quyết đúng nhu cầu. Những tối ưu nhỏ trên bề mặt (đổi màu nút, popup) không giải quyết được mà cần một "cú pivot lớn" về cốt lõi.

## 3. Natural vs Nurture
- **Nature (Tự nhiên):** Tần suất tự nhiên mà user gặp vấn đề (hàng ngày, hàng tuần, hàng tháng...). Đây là nền tảng của Retention.
- **Nurture (Nuôi dưỡng):** Các tác động từ sản phẩm (notification, email reminder, onboarding) để khuếch đại nhịp tự nhiên đó. *Nurture không thể tạo ra nhu cầu từ số 0.*
- Cần thiết kế metrics phù hợp với *Natural Frequency*. Ví dụ, app mua nhà thì không thể chọn DAU làm metric.

## 4. Habit Loop: Mô hình Hook (Hook Model)
Để sản phẩm trở thành thói quen, cần dẫn dắt user qua một vòng lặp (Habit Loop) liên tục:
1. **Trigger (Kích hoạt):** 
   - *Internal Trigger:* Nhu cầu/cảm xúc nội tại (muốn tiến bộ, thấy chán).
   - *External Trigger:* Thông báo, nhắc nhở từ bên ngoài.
2. **Action (Hành động):** Hành động đơn giản nhất user cần thực hiện để nhận thưởng. (Cần tăng Ability và Motivation).
3. **Variable Reward (Phần thưởng biến đổi):**
   - *The Tribe:* Kết nối xã hội, sự công nhận.
   - *The Hunt:* Tìm kiếm tài nguyên, thông tin.
   - *The Self:* Sự thành thạo, cảm giác tiến bộ.
4. **Investment (Đầu tư):** User bỏ công sức (data, content, skill) vào sản phẩm, tạo ra giá trị cho lần sau và "load" trigger tiếp theo.

## 5. Lab Day 20: Thực hành Retention & Habit Loop
Áp dụng kiến thức Ngày 19 vào prototype AI (như AI Travel Planner, AI Personal Assistant):
- **Customer Retention Canvas:** Xác định đúng Persona, Problem, Alternative (giải pháp thay thế hiện tại) và Natural Frequency.
- **Core Action & Active User:** Định nghĩa chính xác hành động tạo ra giá trị (không chỉ là "mở app") và chọn Retention Metric tương ứng với tần suất tự nhiên.
- **Onboarding Audit:** Rà soát và tối ưu Onboarding flow (Keep, Remove, Delay, Simplify) để giảm *Time to First Core Action* và *Time to Value*.
- **Measurement Ladder & North Star:** Thiết lập bậc thang đo lường từ Input metrics đến North Star Metric và kết quả kinh doanh dài hạn.
- **Hook Review:** Thiết kế vòng lặp thói quen với Trigger, Action, Reward, Investment, đảm bảo phù hợp với *Nature* của sản phẩm.
- **Metric Tracking Requirement:** Lên danh sách các sự kiện cần tracking, điều kiện ghi nhận để đo lường chính xác các metrics đã chọn.
