---
type: summary
title: "Day 22 – Track 2"
description: "Tóm tắt tài liệu Track 2 ngày 22 về LLMOPS và prompt versioning."
tags: [ai, 20k, day22, track2]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/Day 22 - Track 2 - LLMOPS-prompt-versioning.pptx"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]


# Day 22 – Track 2

> **Nội dung chính**: Giới thiệu cách quản lý prompt versioning cho các mô hình LLM, bao gồm quy trình tạo, lưu trữ, và kiểm thử các phiên bản prompt. Tài liệu nhấn mạnh tầm quan trọng của việc ghi nhận thay đổi để tránh regressions và hỗ trợ reproducibility.

* Các bước chính:
  1. Định nghĩa phiên bản prompt (semantic versioning).
  2. Lưu trữ trong repos (Git) với chú thích chi tiết.
  3. Kiểm thử A/B để so sánh hiệu năng của các phiên bản.
  4. Tích hợp với pipeline CI/CD.
* Các công cụ đề xuất: PromptFlow, LangChain PromptStore.
