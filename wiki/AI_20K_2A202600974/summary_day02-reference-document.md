---
type: summary
title: "Summary: Day 02 Reference Document"
description: "A comprehensive summary of the reference frameworks, case studies, and reading materials for Day 02."
tags: [Reference, Frameworks, Case Studies, Reading List]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/day02-reference-document.pdf"]
---

# Summary: Day 02 Reference Document
# Tóm tắt: Tài liệu Tham khảo Ngày 02

## Overview
## Tổng quan
This document compiles the comprehensive reference materials, frameworks, case studies, and core principles taught in Day 02 of the VinUni AI 20K program. It serves as a guide for framing business requirements into structured AI problems.

Tài liệu này tổng hợp các tài liệu tham khảo toàn diện, các bộ khung (frameworks), các nghiên cứu tình huống (case studies), và các nguyên tắc cốt lõi được giảng dạy trong Ngày 02 của chương trình VinUni AI 20K. Nó đóng vai trò như một hướng dẫn để định hình các yêu cầu kinh doanh thành các bài toán AI có cấu trúc.

## 1. Frameworks and Decision Models
## 1. Các Bộ Khung và Mô Hình Ra Quyết Định
### In-Class Frameworks
### Các Bộ Khung Trong Lớp Học
- **Business-to-AI Translation:** Converts vague ideas into structured Problem Statements.
  **Dịch từ Kinh doanh sang AI:** Chuyển đổi các ý tưởng mơ hồ thành các Tuyên bố Vấn đề có cấu trúc.
- **AI Possibility Spectrum:** Classifies tasks as Easy, Hard, or Impossible for current AI to set correct expectations.
  **Phổ Khả Năng Của AI:** Phân loại các tác vụ thành Dễ, Khó, hoặc Không Thể đối với AI hiện tại để thiết lập kỳ vọng đúng đắn.
- **AI Fit Matrix:** Maps Ambiguity vs. Complexity to suggest Rule, LLM Feature, or Agent.
  **Ma Trận Phù Hợp Của AI:** Ánh xạ Độ Mơ Hồ so với Độ Phức Tạp để đề xuất sử dụng Quy Tắc, Tính năng LLM, hoặc Agent.
- **Escalation Ladder:** Progression from Prompt -> Retrieval -> Workflow -> Agent. Always start simple.
  **Thang Nâng Cấp:** Tiến trình từ Prompt -> Truy xuất (Retrieval) -> Quy trình (Workflow) -> Agent. Luôn bắt đầu đơn giản.
- **Non-AI Baseline:** Establish a manual or rule-based baseline before attempting AI.
  **Đường Cơ Sở Không AI:** Thiết lập một đường cơ sở thủ công hoặc dựa trên quy tắc trước khi thử nghiệm AI.
- **Buy / Build / Boost:** Three avenues for AI integration (Off-the-shelf, Custom, or Augmenting existing workflows).
  **Mua / Xây dựng / Thúc đẩy:** Ba con đường để tích hợp AI (Sẵn có, Tùy chỉnh, hoặc Tăng cường các quy trình hiện tại).
- **AI Readiness Checklist:** 5 criteria (data, metric, failure tolerance, user readiness, resources). Under 3 YES means "Not Yet".
  **Danh Sách Kiểm Tra Mức Độ Sẵn Sàng Của AI:** 5 tiêu chí (dữ liệu, số đo, dung sai thất bại, độ sẵn sàng của người dùng, tài nguyên). Dưới 3 CÓ nghĩa là "Chưa".
- **UX Patch Patterns:** UX designs to compensate for AI weaknesses (e.g., confirmation dialogs, inline suggestions, sourcing).
  **Các Mẫu Vá Lỗi UX:** Các thiết kế UX để bù đắp cho những điểm yếu của AI (ví dụ: hộp thoại xác nhận, đề xuất nội tuyến, trích xuất nguồn).

### External Frameworks
### Các Bộ Khung Bên Ngoài
- **Google PAIR Guidebook:** Guidelines for responsible AI design, focusing on user needs and AI strengths.
  **Sổ Tay Google PAIR:** Hướng dẫn cho thiết kế AI có trách nhiệm, tập trung vào nhu cầu người dùng và điểm mạnh của AI.
- **Microsoft HAX Toolkit:** 18 principles for Human-AI interaction.
  **Bộ Công Cụ Microsoft HAX:** 18 nguyên tắc cho tương tác Con Người - AI.
- **NIST AI Risk Management Framework:** Organizational risk mapping and measurement.
  **Khung Quản Lý Rủi Ro AI Của NIST:** Lập bản đồ và đo lường rủi ro của tổ chức.
- **Google Rules of ML:** 43 practical rules for ML engineering, particularly around heuristics.
  **Các Quy Tắc Của Google Về Học Máy:** 43 quy tắc thực tế cho kỹ thuật Học Máy, đặc biệt là xoay quanh heuristics (các quy tắc suy nghiệm).

## 2. Case Studies
## 2. Các Nghiên Cứu Tình Huống (Case Studies)
- **Google Flu Trends:** A lesson in flawed problem framing and reliance on proxy metrics.
  **Google Flu Trends:** Bài học về việc định hình vấn đề có thiếu sót và phụ thuộc vào các số đo đại diện (proxy metrics).
- **Google Photos:** Decided *against* AI for photo filters because rule-based heuristics were already sufficient.
  **Google Photos:** Quyết định *không* dùng AI cho các bộ lọc ảnh vì các heuristics dựa trên quy tắc đã đủ tốt.
- **Stripe AI:** Uses LLMs for internal reporting summaries, heavily reliant on PM review (AI as Boost).
  **Stripe AI:** Sử dụng LLMs cho việc tóm tắt báo cáo nội bộ, phụ thuộc nhiều vào việc review của Giám Đốc Sản Phẩm (AI đóng vai trò như Boost/Thúc đẩy).
- **GitHub Copilot & Gmail Smart Compose:** Demonstrates the "ghost text" UX pattern (suggest-only, user decides).
  **GitHub Copilot & Gmail Smart Compose:** Minh chứng cho mẫu UX "ghost text" (chỉ đề xuất, người dùng quyết định).
- **Grammarly:** Inline AI feedback where AI highlights but doesn't autonomously change text.
  **Grammarly:** Phản hồi AI nội tuyến, trong đó AI làm nổi bật nhưng không tự động thay đổi văn bản.

## 3. Reading List
## 3. Danh Sách Đọc
- **AI Engineering:** "Building LLM Applications for Production" by Chip Huyen.
  **Kỹ Thuật AI:** "Xây Dựng Các Ứng Dụng LLM Để Đưa Lên Production" bởi Chip Huyen.
- **System Architecture:** "Emerging Architectures for LLM Applications" by a16z; "Hidden Technical Debt in ML Systems" by Sculley et al.
  **Kiến Trúc Hệ Thống:** "Các Kiến Trúc Mới Nổi Cho Các Ứng Dụng LLM" bởi a16z; "Nợ Kỹ Thuật Ẩn Trong Các Hệ Thống Học Máy" bởi Sculley và cộng sự.
- **Product Management:** "Inspired" by Marty Cagan (Problem-first thinking); "Choosing Your North Star Metric" by Lenny Rachitsky.
  **Quản Lý Sản Phẩm:** "Inspired" bởi Marty Cagan (Tư duy ưu tiên vấn đề); "Chọn Số Đo Sao Bắc Đẩu Của Bạn" bởi Lenny Rachitsky.
- **Agents:** Anthropic's "Building Effective Agents" (emphasizes composable patterns over complex frameworks) and OpenAI's Practical Guide.
  **Agents:** "Xây Dựng Các Agent Hiệu Quả" của Anthropic (nhấn mạnh các mẫu có khả năng lắp ráp (composable patterns) hơn là các framework phức tạp) và Hướng Dẫn Thực Hành Của OpenAI.

## 4. Core Principles (Quick Reference)
## 4. Các Nguyên Tắc Cốt Lõi (Tham Khảo Nhanh)
1. "Problem-first, not AI-first."
   "Ưu tiên vấn đề, không phải ưu tiên AI."
2. The model is only 10-20% of the work; data, UX, and operations are 80-90%.
   Mô hình chỉ chiếm 10-20% công việc; dữ liệu, UX, và vận hành chiếm 80-90%.
3. "Solution looking for a problem" is the most common AI failure mode.
   "Giải pháp đi tìm vấn đề" là kiểu thất bại AI phổ biến nhất.
4. Build a baseline first.
   Xây dựng một đường cơ sở trước.
5. 85% accuracy with good UX > 95% accuracy with bad UX.
   Độ chính xác 85% với UX tốt > độ chính xác 95% với UX tệ.
6. "Not Yet" is not a failure; it shows maturity.
   "Chưa" không phải là một sự thất bại; nó thể hiện sự trưởng thành.
7. Use UX to patch where AI falls short.
   Sử dụng UX để vá lỗi ở những nơi AI thiếu sót.
8. AI is a Boost, not a Replacement.
   AI là một sự Thúc đẩy, không phải là sự Thay thế.
