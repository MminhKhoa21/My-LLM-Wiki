---
type: summary
title: "Summary of day11-guardrails-ai-safety_E402_thien.pdf"
description: "Tóm tắt bài giảng Ngày 11 (phiên bản của giảng viên Trần Quang Thiện) về AI Safety, rủi ro, và các phương pháp phòng thủ cho Agent."
tags: [ai, 20k, day11]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/11/day11-guardrails-ai-safety_E402_thien.pdf"]
---

# Ngày 11: Guardrails & AI Safety (Trần Quang Thiện)

## 1. Tại sao cần Guardrails?
Agent mạnh khi không được kiểm soát có thể gây nguy hiểm. Sự cố thực tế (như DPD Chatbot hay Car Dealer Bot) cho thấy agent cần các biện pháp kiểm soát rủi ro như:
- **Prompt Injection:** Thao túng input để bỏ qua chỉ dẫn gốc.
- **Jailbreaking:** Vượt qua safety filters để sinh nội dung cấm.
- **Data Leakage:** Vô tình tiết lộ thông tin nhạy cảm.
- **Harmful Output:** Sinh nội dung độc hại.

## 2. Các Attack Vectors Chính
- **Direct Prompt Injection:** Ghi đè chỉ dẫn trực tiếp thông qua prompt từ người dùng.
- **Indirect Injection:** Lệnh ẩn trong dữ liệu (email, web pages) mà RAG retrieve về, thao túng luồng xử lý của agent.
- **Jailbreaking:** Vượt rào bằng roleplay (VD: "Pretend you are DAN"), Encoding (Base64) hoặc đổi ngôn ngữ (Zulu, Khmer).
- **PII Extraction:** Dùng nhiều câu hỏi liên tiếp (multi-turn) để lừa agent tiết lộ thông tin cá nhân.

## 3. Defense In Depth (Phòng thủ đa lớp)
- **Input Guardrails:** Chặn đầu vào xấu bằng Validation, Injection Detection (Pattern matching + LLM classifier), Topic Filter và Rate Limiting.
- **Output Guardrails:** Kiểm soát đầu ra bằng Content Filter (phát hiện toxicity, PII), Grounding Check (đảm bảo thông tin dựa trên dữ liệu thật, chống Hallucination), Format Validation (ép JSON schema) và Human Review.
- Cần áp dụng cùng lúc nhiều lớp (Input, LLM, Output rails) vì không có lớp nào hoàn hảo 100%. Có thể sử dụng các framework như **NeMo Guardrails** (NVIDIA) hoặc **Guardrails AI**.

Là quá trình chủ động tấn công agent bằng các *adversarial prompts* để phát hiện lỗ hổng trước khi triển khai (deploy). Quá trình này nên được tích hợp thành Automated Safety Testing trong CI/CD. Cần tuân thủ Responsible Disclosure (Phát hiện lỗi -> Fix -> Test lại -> Thông báo).

AI hoạt động tốt nhất khi được con người giám sát phù hợp.
- **Mô hình HITL:** Human-on-the-loop (Low-risk), Human-in-the-loop (Medium-risk), Human-as-tiebreaker (High-stakes).
- Yêu cầu xây dựng **Trust UX** để củng cố niềm tin của người dùng:
  - Cho phép người dùng theo dõi nguồn (Show sources) và reasoning traces.
  - Báo cáo Confidence badge (Mức độ chắc chắn).
  - Preview action (Cho phép xem trước và Undo/Redo).
  - Cung cấp Audit log rõ ràng.

**Kết luận:** Guardrails giúp agent hoạt động an toàn và đáng tin cậy hơn thay vì bị hạn chế sức mạnh. Red teaming là việc cần thiết trước khi deploy lên production.
