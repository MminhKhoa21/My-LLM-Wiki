---
type: summary
title: "Day 22 Track 2: LLMOps & Prompt Versioning"
description: "Sử dụng LangSmith, Prompt Hub và Guardrails để quản lý vòng đời LLM, theo dõi prompt và giám sát hệ thống."
tags: [ai, 20k, day22, track2, llmops, langsmith, prompt-versioning, evaluation, guardrails]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/Day 22 - Track 2 - LLMOPS-prompt-versioning.pptx"]
---
Dưới đây là nội dung file `day22_track2.md` đã được chuyển đổi sang song ngữ Anh – Việt, giữ nguyên định dạng Markdown và cấu trúc. Mỗi đoạn văn, câu hỏi hoặc gạch đầu dòng được trình bày tiếng Anh trước, tiếp theo là bản dịch tiếng Việt in nghiêng.

> * **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]*

# *LLMOps & Prompt Versioning (Ngày 22 - Track 2)*

 **Giảng viên:** VinUniversity
 **Khóa:** AICB Phase 2 · Track 2

> * **Câu hỏi trọng tâm:** "Prompt thay đổi = behavior thay đổi." Một thay đổi nhỏ trong system prompt có thể làm tăng latency 3x và token cost 200%. Làm thế nào để trace, version và eval mọi thay đổi?*

## *1. LLMOps vs MLOps Truyền Thống*

- Khác biệt cốt lõi: Trong LLMOps, việc quản lý phiên bản của **Prompt** quan trọng không kém việc quản lý code hay data.
- ***Mục đích:** Khả năng truy vết (trace), lưu trữ phiên bản (version control) và đánh giá (evaluation) liên tục giúp đảm bảo độ ổn định và chi phí của ứng dụng LLM.*

## *2. Công Cụ & Kỹ Thuật Trọng Tâm*

  - Instrument (đo lường) các ứng dụng LLM.
  - Trace từng API call để debug nút thắt cổ chai (bottlenecks).
  - Lọc (filter) traces theo latency, cost, và error rate.
  - Giống như "GitHub dành riêng cho prompt".
  - Cho phép lưu trữ, versioning và pin (ghim) các prompt để kiểm soát phiên bản độc lập với code.
  - Đánh giá vượt ra ngoài độ chính xác (accuracy) thông thường.
  - Sử dụng RAGAS để chấm điểm mức độ tin cậy (faithfulness), sự liên quan (relevance), và nhận diện ảo giác (hallucination) một cách có hệ thống.
  - Validate cả đầu vào (inputs) và đầu ra (outputs) của LLM.
  - Ngăn chặn lộ thông tin cá nhân (PII), phát hiện Prompt Injection.
  - Tự động re-ask (hỏi lại) khi LLM trả về format sai (non-JSON).

## *3. Deliverables của Lab*

-  **LangSmith Project:** Ghi lại >100 traces từ RAG pipeline. Phân tích chi tiết latency, cost và error rate.
-  **Prompt Hub:** Tạo 2 version prompt với commit message rõ ràng. Thực hiện A/B routing 50/50.
-  **RAGAS Evaluation Report:** Chạy đánh giá trên 50 QA pairs. Mục tiêu: Faithfulness score > 0.8. So sánh kết quả giữa 2 prompt versions.
-  **Guardrails AI Validator:** Tích hợp bộ chặn PII (chặn email, số điện thoại), tự động reformat JSON và log toàn bộ sự cố (incidents).

## *4. Liên Kết*

---

### *Câu hỏi ôn tập Ngày 22*

   Điểm khác biệt cốt lõi giữa LLMOps và MLOps truyền thống là gì?
     A. LLMOps tập trung vào quản lý dữ liệu hơn là code
     B. LLMOps coi việc quản lý phiên bản Prompt quan trọng như quản lý code và data
     C. MLOps không cần đến evaluation
     D. LLMOps chỉ dùng cho các mô hình ngôn ngữ nhỏ
   ***Đáp án:** B*

   Công cụ nào được mô tả như "GitHub dành riêng cho prompt" trong bài giảng?
   ***Đáp án:** C*

   Theo bài giảng, RAGAS được sử dụng để đánh giá những khía cạnh nào của LLM?
     A. Chỉ độ chính xác (accuracy)
     B. Tốc độ inference và chi phí
     C. Faithfulness, relevance và hallucination
     D. Khả năng phát hiện Prompt Injection
   ***Đáp án:** C*

   Một trong những mục tiêu của Guardrails & Safety Monitoring là gì?
     A. Tăng tốc độ sinh token
     B. Chặn lộ thông tin cá nhân (PII) và phát hiện Prompt Injection
     C. Tự động tạo prompt mới từ dữ liệu
     D. Tối ưu hóa chi phí API
   ***Đáp án:** B*
