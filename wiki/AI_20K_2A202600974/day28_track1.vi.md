---
type: summary
title: "Summary of 1-ai_system_architectures_duong_trung_tin_pdf_ready"
description: "A comprehensive overview of real-world AI system architectures across ADAS, delivery robots, CCTV, humanoid robots, and satellite imaging."
tags: [ai, 20k, day28]
timestamp: 2026-07-06
sources: ["raw/AI_20K_2A202600974/28/1-ai_system_architectures_duong_trung_tin_pdf_ready.pdf"]
---
# Kiến trúc Hệ thống AI Thực tế
**Instructor:** Dương Trung Tín (AI Research Engineer · Obello)
**Giảng viên:** Dương Trung Tín (Kỹ sư Nghiên cứu AI · Obello)

## Tổng quan

Tài liệu này cung cấp một cái nhìn tổng quan về cách các hệ thống AI thực tế chuyển từ một "mô hình hoạt động được" sang một "hệ thống production". Nó bao gồm năm hệ thống AI chính:

- **ADAS / Lái xe tự động (Autonomous Driving)**
- **Robot Giao hàng Tự động (Autonomous Delivery Robot)**
- **Hệ thống AI cho Camera Giám sát (CCTV)**
- **Robot Hình người (Humanoid Robot)**
- **Ứng dụng Ảnh Vệ tinh (Satellite Image Application)**


Các tầng kiến trúc cốt lõi chung của những hệ thống này bao gồm:

1. **Dữ liệu / Cảm biến (Data / Sensor):** Camera, radar, lidar, nhật ký (log), hình ảnh vệ tinh.
2. **Nhận thức (Perception):** Phát hiện, phân vùng, theo dõi, nhúng (embeddings).
3. **Trạng thái Thế giới (World State):** BEV (Góc nhìn từ trên cao), bản đồ, đồ thị cảnh vật.
4. **Quyết định / Chính sách (Decision / Policy):** Bộ lập kế hoạch, VLA (Tầm nhìn-Ngôn ngữ-Hành động), bộ chấm điểm bất thường.
5. **Hành động / Sản phẩm (Action / Product):** Điều khiển, giao hàng, cảnh báo, bảng điều khiển.
6. **Vận hành / An toàn (Ops / Safety):** ODD (Phạm vi Thiết kế Vận hành), HITL (Human-in-the-loop), đo từ xa, kiểm toán và huấn luyện lại.

## 1. ADAS / Lái xe Tự động

- **Kiến trúc:** Chuyển đổi từ hướng tiếp cận theo mô-đun sang các hướng tiếp cận End-to-End (E2E) định hướng lập kế hoạch.
- **Khái niệm chính:**
  - **UniAD & VAD:** Kết hợp nhận thức, theo dõi, dự đoán và lập kế hoạch vào một luồng (pipeline) duy nhất.
  - **DriveLM:** Sử dụng VLM (Mô hình Tầm nhìn-Ngôn ngữ) để suy luận và VQA đồ thị (Visual Question Answering) để ra quyết định.
  - **GAIA-1 / GAIA-2:** Sử dụng World Models để mô phỏng các kịch bản hiếm gặp.
- **Bài học kinh nghiệm:** Cần phải xác định ODD trước mô hình. Một chính sách E2E vẫn cần một lớp vỏ an toàn độc lập.

## 2. Robot Giao hàng Tự động

- **Kiến trúc:** Tự hành trên vỉa hè bao gồm điều hướng tốc độ thấp, nhận thức xã hội, tính kinh tế của đội xe và hỗ trợ từ xa.
- **Khái niệm chính:**
  - **Tự hành lai (Hybrid Autonomy):** Sự tự hành kết hợp với sự hỗ trợ của con người từ xa.
  - **Điều hướng xã hội (Social Navigation):** Dự đoán hành vi của người đi bộ.
- **Bài học kinh nghiệm:** Vận hành đội xe (đỗ xe, bảo trì) là lợi thế cạnh tranh chính (moat). Trợ lý từ xa cần có khả năng quan sát cao để xử lý hiệu quả các trường hợp bị kẹt.

## 3. Hệ thống AI cho Camera Giám sát (CCTV)

- **Kiến trúc:** Chuyển đổi từ phát hiện theo lớp cố định theo thời gian thực sang các từ vựng mở (open-vocabulary) và tìm kiếm ngữ nghĩa.
- **Khái niệm chính:**
  - **Suy luận tại biên (Edge Inference):** Sử dụng YOLOv8/v10 để phát hiện nhẹ nhàng tại thiết bị biên.
  - **Từ vựng mở (Open-Vocabulary):** Sử dụng SAM / Grounded SAM để phát hiện dựa trên điều kiện văn bản.
  - **Bất thường VLM (VLM Anomaly):** Sử dụng VLM để phát hiện và giải thích các điểm bất thường trong các video dài.
- **Bài học kinh nghiệm:** Mục tiêu là giảm số lượng clip để con người xem lại, chứ không chỉ áp dụng mô hình lớn cho mọi khung hình. Tính toán tại biên là rất quan trọng để tối ưu hóa băng thông và quyền riêng tư.

## 4. Robot Hình người

- **Kiến trúc:** Thao tác giàu tiếp xúc kết hợp giữa Hệ thống 1 (vòng lặp điều khiển nhanh) và Hệ thống 2 (suy luận VLA).
- **Khái niệm chính:**
  - **Mô hình VLA:** RT-2, GR00T.
  - **Bắt chước & Học tăng cường (Imitation & RL):** Dữ liệu điều khiển từ xa (Mobile ALOHA) và học tăng cường từ mô phỏng sang thực tế (Sim-to-Real).
- **Bài học kinh nghiệm:** Dữ liệu robot đắt đỏ hơn dữ liệu web. Khoảng cách từ mô phỏng sang thực tế (Sim-to-real) đòi hỏi phải ngẫu nhiên hóa miền (domain randomization). Các thiết bị bảo vệ an toàn (dừng khẩn cấp, giới hạn mô-men xoắn) phải độc lập với chính sách.

## 5. Ứng dụng Ảnh Vệ tinh

- **Kiến trúc:** GeoAI bao gồm việc xử lý dữ liệu khổng lồ, xử lý quang học/SAR và kết hợp theo thời gian (temporal fusion).
- **Khái niệm chính:**
  - **Các mô hình Nền tảng Không gian Địa lý:** Prithvi, Clay.
  - **Đa thời gian & Đa phương thức:** Kết hợp các đường cơ sở thời gian và cảm biến khác nhau (Quang học + SAR + văn bản).
- **Bài học kinh nghiệm:** Phát hiện thay đổi đòi hỏi các đường cơ sở theo thời gian. Lập bản đồ độ không chắc chắn (Uncertainty mapping) và Vòng lặp Phân tích viên Con người là rất quan trọng cho môi trường production.

## Những điểm chính

1. **Kiến trúc quan trọng hơn Điểm chuẩn (Architecture Beats Benchmark):** Một mô hình tốt yêu cầu luồng dữ liệu chính xác, các ràng buộc về độ trễ, lớp vỏ an toàn và vòng lặp vận hành (ops loop).
2. **End-to-End Không có nghĩa là Không cần Hệ thống:** Các chính sách E2E vẫn cần xác định ODD và giám sát.
3. **Bánh đà Dữ liệu (Data Flywheel):** Các hệ thống mở rộng hiệu quả bằng cách nắm bắt các trường hợp đặc biệt (edge cases) và đưa chúng trở lại vòng lặp huấn luyện.

## Liên kết
## Liên kết (Links)
