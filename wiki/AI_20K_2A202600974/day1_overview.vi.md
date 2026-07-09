---
type: overview
title: "Day 1 Overview - AI & LLM Foundation"
description: "Tổng quan về bức tranh AI 2026, nền tảng LLM, kiến trúc Transformer và cách tính chi phí API."
tags: [ai, 20k, day1]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/1/1-AICB_Ngày_1.pdf"]
---
# Ngày 1: Nền tảng AI & LLM

## 1. Bức tranh AI 2026

Sự dịch chuyển từ Machine Learning và Generative AI sang **Agentic AI**. AI không chỉ "trả lời hay" mà còn biết **hành động, kết nối công cụ và tạo ra ROI**. Các agent ngày càng trở nên đa năng, cá nhân hóa sâu và tự vận hành trong nhiều hệ thống.

## 2. LLM — Trái tim của AI hiện đại

  - **Large Language Model (LLM)** dựa trên kiến trúc **Transformer**.

  - **Transformer**: Sử dụng cơ chế Self-Attention để mô hình "chú ý" đến các token liên quan nhất trong ngữ cảnh khi sinh từ tiếp theo.

  - Thay vì xử lý tuần tự, Transformer xử lý song song và hiểu ngữ cảnh tốt hơn qua các thành phần như Input Embedding, Positional Encoding, và Multi-Head Attention.

  - LLM hiện tại hoạt động chủ yếu dựa trên cơ chế **Next-token prediction** (Dự đoán từ tiếp theo).


  - **Token** là đơn vị nhỏ nhất mà LLM xử lý (1 token ~ 0.75 từ tiếng Anh, ~ 0.5 từ tiếng Việt).

  - Chi phí của API LLM phụ thuộc vào số lượng token đầu vào (Input) và token đầu ra (Output), trong đó Output tokens thường đắt hơn Input tokens.

  - Các ngôn ngữ như tiếng Việt thường tốn nhiều token hơn do cách mã hóa Unicode, dẫn đến chi phí cao hơn cho cùng một nội dung.

  - Sự cân bằng (Trade-off) giữa **Latency** và **Cost**: Càng nhiều tokens thì hệ thống chạy càng chậm và càng đắt. Do đó, cần tối ưu Prompt và Context.


Lập trình bằng cách phối hợp với AI: Mô tả ý tưởng và yêu cầu bằng ngôn ngữ tự nhiên để AI tự động sinh code.

  - Kỹ năng không nằm ở việc nhớ cú pháp (syntax) mà là khả năng diễn đạt logic và chia nhỏ bài toán.

  - Việc sử dụng API (OpenAI) để tích hợp LLM vào ứng dụng thực tế.

  - API call gồm 3 thứ cần kiểm soát: **quality, latency, cost**.

## 5. Các mô hình phổ biến

  - Phân loại khi nào nên dùng mô hình đắt tiền/năng lực cao (như GPT-4o, Claude Opus) vs mô hình rẻ/nhanh (như Claude Haiku, Gemini Flash).

  - Rule of thumb: Bắt đầu từ model **đủ tốt và đủ rẻ**. Chỉ nâng cấp khi chất lượng chặn đứng use case.
