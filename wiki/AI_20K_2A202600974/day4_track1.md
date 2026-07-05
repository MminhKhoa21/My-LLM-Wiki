---
type: summary
title: "Day 4 Track 1 - Prompt Engineering, Tool Calling & LangGraph"
description: "Tổng hợp kiến thức về Prompt Engineering nâng cao, System Prompts, Tool Calling và ứng dụng LangGraph cho Agent."
tags: [ai, 20k, day4, track1, prompt-engineering, tool-calling, langgraph]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/4/1-day04-prompt-engineering-tool-calling-v2.pdf", "raw/AI_20K_2A202600974/4/1-day04-prompt-engineering-tool-calling.pdf", "raw/AI_20K_2A202600974/4/day04-prompt-engineering-tool-calling.pdf"]
---

# Day 4 Track 1: Prompt Engineering, Tool Calling & LangGraph

Tài liệu này tóm tắt các kiến thức cốt lõi về cách thiết kế Prompt từ cơ bản đến nâng cao, vòng lặp Tool Calling và sử dụng LangGraph để điều phối Agent.

## 1. Prompt Engineering Fundamentals
- **Prompt là Interface**: Là cầu nối giữa ý định của con người và khả năng của model. Một prompt tốt cần cụ thể, tạo ra hành vi ổn định.
- **4 Thành Phần Của Prompt Tốt (RTCF)**:
  - **Role** (Vai trò): Định nghĩa persona, expertise level.
  - **Task** (Nhiệm vụ): Rõ ràng, cụ thể (ưu tiên hàng đầu).
  - **Context** (Bối cảnh): Thông tin nền tảng, điều kiện bổ sung.
  - **Format** (Định dạng): Chuẩn đầu ra (JSON, Markdown, Bullet list...).
- **Các loại Prompt**:
  - **Instruction prompt**: Lệnh trực tiếp.
  - **Conversation prompt**: Giữ ngữ cảnh nhiều lượt.
  - **System prompt**: Đặt policy, rules, output contract cho Agent.

## 2. Advanced Prompting Techniques
- **Zero-shot, Few-shot, CoT**:
  - *Zero-shot*: Không ví dụ, nên thử trước.
  - *Few-shot*: Dùng 2-5 ví dụ (tập trung vào edge-cases, "show, don't just tell", định dạng chuẩn). Giúp ép output format ổn định.
  - *Chain-of-Thought (CoT)*: Dùng cho bài toán cần reasoning, tách phần `<thinking>` và `<result>`.
- **Cấu trúc hóa bằng XML Tags / Delimiters**:
  - Tránh Context Bleed (lẫn lộn lệnh và dữ liệu, dẫn đến prompt injection).
  - Sử dụng các thẻ: `<system_role>`, `<instructions>`, `<examples>`, `<context>`, `<user_input>`.
- **Lost in the Middle**: LLM dễ quên thông tin ở giữa. Tối ưu bằng *Recency Bias*: đặt yêu cầu/câu hỏi cuối cùng, context dài ở giữa.

## 3. System Prompt Engineering
- System Prompt là "Bộ Não" của Agent, một hợp đồng (Contract) giữa developer và LLM.
- **Thành phần Production-grade**:
  - Persona & Tone.
  - Core Directives (LUÔN LUÔN, KHÔNG BAO GIỜ).
  - Capabilities (Công cụ được phép dùng).
  - Output Contract (JSON schema hoặc format bắt buộc).
- **Edge Cases & Graceful Fallback**: Xử lý tình huống hỏi ngoài lề (Out-of-Scope), thiết lập ranh giới hành vi, và quyền được nói "Tôi không biết" để giảm ảo giác.
- **Dynamic System Prompts**: Nhúng biến (thời gian, user info, system status) vào prompt bằng Jinja2 hoặc f-strings trước khi gọi API.

## 4. Function/Tool Calling
- **Kiến trúc 4 bước**:
  1. Trigger (User input).
  2. LLM trả về JSON `tool_calls`.
  3. App thực thi tool cục bộ.
  4. Gửi `tool_outputs` lại cho LLM (Second Call).
- **Tool Schema**:
  - Tên hàm: Verb + Noun rõ ràng.
  - Mô tả: CHÍNH LÀ prompt cho AI, cần định nghĩa ranh giới khi nào dùng/không dùng.
  - Tham số (Parameters): Chặt chẽ, dùng `enum` để khóa chặt lựa chọn, define rõ `required`. Không nhồi nhét quá 5-7 tham số.
- **Execution Strategies**: Tuần tự (Sequential - khi có phụ thuộc) vs Song song (Parallel - khi độc lập).
- **Error Handling**: Bọc try-except, nếu lỗi gửi raw error message lại cho LLM để nó tự sửa lỗi (Self-Correction).

## 5. Orchestration with LangGraph
- Chuyển từ `while True` sang Máy Trạng Thái (State Machine) bằng Đồ thị định hướng (Cyclic Graphs).
- **Core Concepts**:
  - **State**: Bộ nhớ chung (TypedDict) lưu `messages` xuyên suốt với cơ chế Append-only (Reducer).
  - **Nodes**: Nút xử lý (Agent Node gọi model, Tool Node gọi hàm).
  - **Edges**: Điều hướng (Normal Edge chạy cố định, Conditional Edge/Router rẽ nhánh theo logic).
- Cung cấp kiến trúc an toàn, có khả năng Human-in-the-loop (HITL) và gỡ lỗi tốt hơn.
