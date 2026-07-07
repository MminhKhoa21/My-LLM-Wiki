---
type: overview
title: "Day 1 Overview - AI & LLM Foundation"
description: "Tổng quan về bức tranh AI 2026, nền tảng LLM, kiến trúc Transformer và cách tính chi phí API."
tags: [ai, 20k, day1]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/1/1-AICB_Ngày_1.pdf"]
---
# Day 1: AI & LLM Foundation
*# Ngày 1: Nền tảng AI & LLM*

## 1. The AI Landscape in 2026
*## 1. Bức tranh AI 2026*

The shift from Machine Learning and Generative AI to **Agentic AI**. AI is no longer just about "answering well" but also about **acting, connecting to tools, and generating ROI**. Agents are becoming more versatile, deeply personalized, and self-operating across multiple systems.
*Sự dịch chuyển từ Machine Learning và Generative AI sang **Agentic AI**. AI không chỉ "trả lời hay" mà còn biết **hành động, kết nối công cụ và tạo ra ROI**. Các agent ngày càng trở nên đa năng, cá nhân hóa sâu và tự vận hành trong nhiều hệ thống.*

## 2. LLM — The Heart of Modern AI
*## 2. LLM — Trái tim của AI hiện đại*

- **Large Language Model (LLM)** is based on the **Transformer** architecture.
  *- **Large Language Model (LLM)** dựa trên kiến trúc **Transformer**.*

- **Transformer**: Uses the Self-Attention mechanism so that the model "pays attention" to the most relevant tokens in the context when generating the next word.
  *- **Transformer**: Sử dụng cơ chế Self-Attention để mô hình "chú ý" đến các token liên quan nhất trong ngữ cảnh khi sinh từ tiếp theo.*

- Instead of sequential processing, the Transformer processes in parallel and understands context better through components such as Input Embedding, Positional Encoding, and Multi-Head Attention.
  *- Thay vì xử lý tuần tự, Transformer xử lý song song và hiểu ngữ cảnh tốt hơn qua các thành phần như Input Embedding, Positional Encoding, và Multi-Head Attention.*

- Current LLMs operate mainly based on the **Next-token prediction** mechanism.
  *- LLM hiện tại hoạt động chủ yếu dựa trên cơ chế **Next-token prediction** (Dự đoán từ tiếp theo).*

## 3. Token Economy
*## 3. Token Economy*

- **Token** is the smallest unit that an LLM processes (1 token ~ 0.75 English words, ~ 0.5 Vietnamese words).
  *- **Token** là đơn vị nhỏ nhất mà LLM xử lý (1 token ~ 0.75 từ tiếng Anh, ~ 0.5 từ tiếng Việt).*

- The cost of LLM APIs depends on the number of input tokens and output tokens, where output tokens are usually more expensive than input tokens.
  *- Chi phí của API LLM phụ thuộc vào số lượng token đầu vào (Input) và token đầu ra (Output), trong đó Output tokens thường đắt hơn Input tokens.*

- Languages like Vietnamese often consume more tokens due to Unicode encoding, leading to higher costs for the same content.
  *- Các ngôn ngữ như tiếng Việt thường tốn nhiều token hơn do cách mã hóa Unicode, dẫn đến chi phí cao hơn cho cùng một nội dung.*

- The trade-off between **Latency** and **Cost**: The more tokens, the slower and more expensive the system becomes. Therefore, optimizing the Prompt and Context is essential.
  *- Sự cân bằng (Trade-off) giữa **Latency** và **Cost**: Càng nhiều tokens thì hệ thống chạy càng chậm và càng đắt. Do đó, cần tối ưu Prompt và Context.*

## 4. Vibe Coding
*## 4. Vibe Coding*

Programming by collaborating with AI: Describe ideas and requirements in natural language so that the AI automatically generates code.
*Lập trình bằng cách phối hợp với AI: Mô tả ý tưởng và yêu cầu bằng ngôn ngữ tự nhiên để AI tự động sinh code.*

- The skill lies not in remembering syntax but in the ability to express logic and break down problems.
  *- Kỹ năng không nằm ở việc nhớ cú pháp (syntax) mà là khả năng diễn đạt logic và chia nhỏ bài toán.*

- Using APIs (OpenAI) to integrate LLMs into real-world applications.
  *- Việc sử dụng API (OpenAI) để tích hợp LLM vào ứng dụng thực tế.*

- An API call involves three things to control: **quality, latency, cost**.
  *- API call gồm 3 thứ cần kiểm soát: **quality, latency, cost**.*

## 5. Common Models
*## 5. Các mô hình phổ biến*

- Categorize when to use expensive/high-capability models (e.g., GPT-4o, Claude Opus) vs. cheap/fast models (e.g., Claude Haiku, Gemini Flash).
  *- Phân loại khi nào nên dùng mô hình đắt tiền/năng lực cao (như GPT-4o, Claude Opus) vs mô hình rẻ/nhanh (như Claude Haiku, Gemini Flash).*

- Rule of thumb: Start with a model that is **good enough and cheap enough**. Only upgrade when quality blocks the use case.
  *- Rule of thumb: Bắt đầu từ model **đủ tốt và đủ rẻ**. Chỉ nâng cấp khi chất lượng chặn đứng use case.*
