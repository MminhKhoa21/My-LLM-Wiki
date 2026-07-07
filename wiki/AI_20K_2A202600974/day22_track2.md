---
type: summary
title: "Day 22 Track 2: LLMOps & Prompt Versioning"
description: "Sử dụng LangSmith, Prompt Hub và Guardrails để quản lý vòng đời LLM, theo dõi prompt và giám sát hệ thống."
tags: [ai, 20k, day22, track2, llmops, langsmith, prompt-versioning, evaluation, guardrails]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/Day 22 - Track 2 - LLMOPS-prompt-versioning.pptx"]
---
Dưới đây là nội dung file `day22_track2.md` đã được chuyển đổi sang song ngữ Anh – Việt, giữ nguyên định dạng Markdown và cấu trúc. Mỗi đoạn văn, câu hỏi hoặc gạch đầu dòng được trình bày tiếng Anh trước, tiếp theo là bản dịch tiếng Việt in nghiêng.

> **Roadmap:** [[track2_ai_engineer|Track 2: AI Engineer]]  
> * **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]*

# LLMOps & Prompt Versioning (Day 22 - Track 2)  
# *LLMOps & Prompt Versioning (Ngày 22 - Track 2)*

**Lecturer:** VinUniversity  
* **Giảng viên:** VinUniversity*  
**Course:** AICB Phase 2 · Track 2  
* **Khóa:** AICB Phase 2 · Track 2*

> **Key Question:** "Prompt change = behavior change." A small change in the system prompt can increase latency by 3x and token cost by 200%. How to trace, version, and evaluate every change?  
> * **Câu hỏi trọng tâm:** "Prompt thay đổi = behavior thay đổi." Một thay đổi nhỏ trong system prompt có thể làm tăng latency 3x và token cost 200%. Làm thế nào để trace, version và eval mọi thay đổi?*

## 1. LLMOps vs Traditional MLOps  
## *1. LLMOps vs MLOps Truyền Thống*

- Core difference: In LLMOps, versioning the **Prompt** is as important as versioning code or data.  
- *Khác biệt cốt lõi: Trong LLMOps, việc quản lý phiên bản của **Prompt** quan trọng không kém việc quản lý code hay data.*  
- **Purpose:** Traceability, version control, and continuous evaluation ensure the stability and cost-effectiveness of LLM applications.  
- ***Mục đích:** Khả năng truy vết (trace), lưu trữ phiên bản (version control) và đánh giá (evaluation) liên tục giúp đảm bảo độ ổn định và chi phí của ứng dụng LLM.*

## 2. Key Tools & Techniques  
## *2. Công Cụ & Kỹ Thuật Trọng Tâm*

- **LangSmith (Trace, Debug & Monitor):**  
  - Instrument (measure) LLM applications.  
  - *Instrument (đo lường) các ứng dụng LLM.*  
  - Trace each API call to debug bottlenecks.  
  - *Trace từng API call để debug nút thắt cổ chai (bottlenecks).*  
  - Filter traces by latency, cost, and error rate.  
  - *Lọc (filter) traces theo latency, cost, và error rate.*  
- **Prompt Hub (Version Control):**  
  - Like "GitHub for prompts".  
  - *Giống như "GitHub dành riêng cho prompt".*  
  - Allows storing, versioning, and pinning prompts to control versions independently of code.  
  - *Cho phép lưu trữ, versioning và pin (ghim) các prompt để kiểm soát phiên bản độc lập với code.*  
- **LLM Evaluation (W&B Weave / RAGAS):**  
  - Evaluate beyond standard accuracy.  
  - *Đánh giá vượt ra ngoài độ chính xác (accuracy) thông thường.*  
  - Use RAGAS to systematically score faithfulness, relevance, and hallucination.  
  - *Sử dụng RAGAS để chấm điểm mức độ tin cậy (faithfulness), sự liên quan (relevance), và nhận diện ảo giác (hallucination) một cách có hệ thống.*  
- **Guardrails & Safety Monitoring:**  
  - Validate both LLM inputs and outputs.  
  - *Validate cả đầu vào (inputs) và đầu ra (outputs) của LLM.*  
  - Prevent PII leakage, detect Prompt Injection.  
  - *Ngăn chặn lộ thông tin cá nhân (PII), phát hiện Prompt Injection.*  
  - Auto re-ask when LLM returns wrong format (non‑JSON).  
  - *Tự động re-ask (hỏi lại) khi LLM trả về format sai (non-JSON).*

## 3. Lab Deliverables  
## *3. Deliverables của Lab*

- **LangSmith Project:** Record >100 traces from the RAG pipeline. Perform detailed analysis of latency, cost, and error rate.  
- * **LangSmith Project:** Ghi lại >100 traces từ RAG pipeline. Phân tích chi tiết latency, cost và error rate.*  
- **Prompt Hub:** Create 2 prompt versions with clear commit messages. Implement A/B routing with 50/50 split.  
- * **Prompt Hub:** Tạo 2 version prompt với commit message rõ ràng. Thực hiện A/B routing 50/50.*  
- **RAGAS Evaluation Report:** Run evaluation on 50 QA pairs. Target: Faithfulness score > 0.8. Compare results between the 2 prompt versions.  
- * **RAGAS Evaluation Report:** Chạy đánh giá trên 50 QA pairs. Mục tiêu: Faithfulness score > 0.8. So sánh kết quả giữa 2 prompt versions.*  
- **Guardrails AI Validator:** Integrate a PII blocker (block emails, phone numbers), auto-reformat JSON, and log all incidents.  
- * **Guardrails AI Validator:** Tích hợp bộ chặn PII (chặn email, số điện thoại), tự động reformat JSON và log toàn bộ sự cố (incidents).*

## 4. Links  
## *4. Liên Kết*

- [[day22_overview]]  
- *[[day22_overview]]*
