---
type: summary
title: "Summary of day11-guardrails-ai-safety.pdf"
description: "Tóm tắt bài giảng Ngày 11 về AI Safety, các rủi ro, và cách xây dựng guardrails bảo vệ Agent."
tags: [ai, 20k, day11]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/11/day11-guardrails-ai-safety.pdf"]
---

# Ngày 11: Guardrails & AI Safety - Agent mạnh rồi nhưng ai kiểm soát nó?

## 1. Tại sao cần Guardrails?
Agent mạnh mà không có guardrails giống như xe chạy nhanh mà không có phanh. Khi agent có RAG, multi-agent và UX hoàn chỉnh, nó đối mặt với nguy cơ bị thao túng. Các rủi ro phổ biến gồm có:
- **Prompt Injection:** Thao túng input để bỏ qua chỉ dẫn gốc, khiến LLM làm theo lệnh mới.
- **Jailbreaking:** Vượt qua safety filters để sinh các nội dung bị cấm, sai lệch.
- **Data Leakage:** Vô tình tiết lộ thông tin nhạy cảm như System Prompt, API keys, dữ liệu nội bộ.
- **Harmful Output:** Sinh ra nội dung vi phạm chính sách, độc hại, sai sự thật.

*OWASP Top 10 cho các ứng dụng LLM (2025)* bổ sung 2 lỗ hổng mới cho kỷ nguyên RAG/Agentic: System Prompt Leakage và Vector & Embedding Weaknesses.

## 2. Các Mối Đe Dọa (Attack Vectors) Chi Tiết
- **Direct Prompt Injection:** User gửi lệnh để trực tiếp ghi đè system prompt (ví dụ: *"Ignore all previous instructions..."*).
- **Indirect Injection:** Chỉ dẫn độc hại ẩn mình trong tài liệu ngoại vi mà agent sử dụng qua RAG hoặc từ email, web. Mức độ nguy hiểm cao hơn do không phải do user cố tình.
- **Jailbreaking:** Dùng kỹ thuật thao túng như Roleplay (ví dụ ép mô phỏng "DAN"), mã hoá lệnh (Base64, ROT13), khai thác bằng Multi-turn escalation hoặc thay đổi ngôn ngữ.
- **PII Extraction:** Hacker có thể tận dụng nhiều câu hỏi riêng lẻ, sau đó ghép nối lại để thu thập thông tin nhạy cảm. 

## 3. Hệ Thống Phòng Thủ (Defense in Depth)
An toàn không thể chỉ dựa vào một lớp mà phải là phòng thủ theo chiều sâu, từ đầu vào cho tới đầu ra.

### 3.1. Input Guardrails (Lọc trước khi xử lý)
Ngăn chặn các nội dung xấu trước khi nó đến LLM nhằm tránh chi phí token và rủi ro.
1. **Input Validation:** Kiểm tra độ dài, format, ngôn ngữ của prompt.
2. **Injection Detection:** Sử dụng Pattern Matching (Regex) và LLM classifier để phát hiện injection.
3. **Topic Filter:** Ngăn chặn các chủ đề không liên quan đến use case.
4. **Rate Limiting:** Ngăn chặn spam, abuse, kiểm soát chi phí.

*Các phòng thủ tiên tiến (2026):* Dùng Spotlighting (đánh dấu dữ liệu rõ ràng), Instruction Hierarchy (phân cấp ưu tiên mệnh lệnh) và CaMeL (DeepMind) - phân tách quyền của các LLM.

### 3.2. Output Guardrails (Kiểm tra trước khi trả lời)
1. **Content Filter:** Phát hiện từ ngữ toxicity, thông tin PII (tên, SĐT, tài khoản).
2. **Grounding Check:** Đảm bảo output có citation và được lấy từ retrieved context, chống hiện tượng Hallucination.
3. **Format Validation:** Ép định dạng trả về (ví dụ JSON schema) để đảm bảo downstream dễ dàng xử lý.
4. **Human Review:** Queue lại chờ người kiểm duyệt nếu confidence thấp hoặc chủ đề nhạy cảm.

## 4. AI Alignment, Control & Governance
- **AI Alignment:** Phải đảm bảo AI được căn chỉnh với ý muốn và giá trị của con người. Cần tránh các lỗi như *Reward Hacking* (gian lận điểm số) hoặc *Deceptive Alignment*.
- **AI Control:** Áp dụng Scope Limitation (giới hạn quyền), Kill Switch, Rate Limiting, Audit Trail.
- **AI Governance:** Tuân thủ các khung pháp lý như EU AI Act, NIST AI RMF, quy định mức độ rủi ro (Unacceptable / High / Limited).

## 5. Red Teaming & Testing
Red teaming là chủ động tấn công vào hệ thống của mình nhằm phát hiện rủi ro trước khi deploy.
- Sử dụng các **Adversarial Test Suite** (như HarmBench, AgentDojo, PyRIT) trong môi trường CI/CD mỗi khi release.
- **Responsible Disclosure:** Quản trị rủi ro qua quy trình minh bạch: Phát hiện lỗi -> Sửa chữa nhanh -> Test lại -> Thông báo (Communicate).

## 6. Human-in-the-Loop (HITL) & Trust UX
AI hoạt động hiệu quả nhất khi kết hợp phán đoán của con người ở các bước quan trọng.
- **Mô hình HITL:**
  - *Human-on-the-loop:* Agent thực hiện, người dùng review lại sau (Low-risk).
  - *Human-in-the-loop:* Agent đề xuất, người dùng chấp thuận trước (Medium-risk, irreversible action).
  - *Human-as-tiebreaker:* Người dùng quyết định, AI hỗ trợ (High-stakes).
- **Trust UX (UX xây dựng niềm tin):** Agent cần phải cung cấp cho user reasoning trace (quá trình suy nghĩ), cung cấp sources/citations, gắn tag mức độ tự tin (Confidence Badge), hiển thị preview action và luôn hỗ trợ hoàn tác (Undo/Redo). Cần có một Audit log minh bạch.

**Key Takeaways:** Guardrails không làm agent yếu đi mà giúp agent trở nên đáng tin cậy. Prompt injection khó có thể giải quyết triệt để chỉ bằng filters mà cần thiết kế kiến trúc bảo mật toàn diện.
