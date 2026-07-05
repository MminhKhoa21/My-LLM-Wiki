---
type: overview
title: "Day 11: Guardrails & AI Safety"
description: "Các nguyên tắc an toàn, quản lý rủi ro và xây dựng hệ thống Guardrails bảo vệ AI trước các lỗ hổng và rủi ro độc hại."
tags: [ai, 20k, day11, guardrails, safety]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/11/day11-guardrails-ai-safety_E403_v2_linh.pdf"]
---

# Day 11: Guardrails & AI Safety

## Nội dung chính
Khi Agent có khả năng hoạt động độc lập và gắn trực tiếp với thế giới thực (thông qua API/Tools), rủi ro liên quan đến bảo mật và ảo giác tăng vọt. Agent không có hệ thống **Guardrails** giống như chiếc xe không có phanh.

## Các rủi ro phổ biến (Attack Vectors)
- **Prompt Injection (Direct & Indirect)**: Người dùng cố tình (hoặc vô tình qua tài liệu truy xuất) ghi đè system prompt để ép AI làm những việc không được phép.
- **Jailbreaking**: Kỹ thuật bypass các bộ lọc an toàn của LLM (ví dụ: yêu cầu đóng vai, mã hóa text).
- **Data Leakage & PII**: AI vô tình tiết lộ thông tin cá nhân, bí mật nội bộ, hoặc system prompt thông qua các truy vấn tinh vi.
- **Hallucination & Harmful Output**: Agent tạo ra câu trả lời vi phạm chính sách hoặc sai sự thật nhưng rất thuyết phục.

## Xây dựng Guardrails (Defense in Depth)
Bảo vệ AI không dựa vào một hàng rào duy nhất mà là sự kết hợp nhiều lớp (Defense in Depth):
1. **Input Rails**: Chặn đứng thông tin đầu vào độc hại trước khi chạm đến LLM (giới hạn độ dài, check ngôn ngữ, pattern matching để bắt prompt injection).
2. **LLM Rails**: Làm cứng system prompt, thêm safety instructions.
3. **Output Rails**: Kiểm tra tính trung thực của kết quả (Grounding Check), Format validation, và chặn các nội dung độc hại (Toxicity, PII) trước khi trả về cho người dùng.

## Human-in-the-Loop (HITL)
Áp dụng sự can thiệp của con người vào những quyết định quan trọng (high-stakes) hoặc không thể hoàn tác:
- **Human-on-the-loop**: Agent hành động, con người giám sát sau đó.
- **Human-in-the-loop**: Agent đề xuất, cần sự đồng ý trước khi thực hiện.
- **Human-as-tiebreaker**: Agent chỉ hỗ trợ, con người quyết định hoàn toàn.

## Red Teaming
Thực hiện các bài kiểm thử giả định đóng vai tin tặc (Red Team) tấn công vào Agent để phát hiện trước các lỗ hổng. Quá trình này cần thực hiện liên tục và kết hợp với việc xây dựng Adversarial Prompt Library.
