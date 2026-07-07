---
type: summary
title: "Day 16 Track 3: Advanced Agent Architectures"
description: "Kiến trúc Agent nâng cao: Reflexion, LATS, Voyager và cách triển khai an toàn"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/phase2-day01-advanced-agent-architectures-extended-fuller.pdf"]
---
> **Roadmap:** [[track3_ai_app]]
> *Lộ trình:* [[track3_ai_app]]

# Advanced Agent Architectures
*Kiến trúc Agent Nâng cao*

Research the reasons why Single Agent (like ReAct) fails in complex problems and how to overcome them with advanced patterns.
*Nghiên cứu nguyên nhân Single Agent (như ReAct) thất bại trong các bài toán phức tạp và cách khắc phục bằng các pattern nâng cao.*

## 1. Limitations of Single Agent (ReAct)
*1. Giới hạn của Single Agent (ReAct)*

The **ReAct (Reasoning + Acting)** model is very powerful but lacks self-evaluation capability. When encountering errors, ReAct easily falls into:
- **Error propagation**: An error in the first step leads to the entire chain being wrong.
- **Infinite loop**: The tool returns noise causing the agent to repeat endlessly.
- **No backtracking**: Goes down the wrong path but doesn't know how to return.
*Mô hình **ReAct (Reasoning + Acting)** rất mạnh nhưng thiếu khả năng tự đánh giá. Khi gặp lỗi, ReAct dễ rơi vào:*
*- **Lỗi lan tỏa**: Sai ở bước đầu dẫn đến sai toàn bộ chuỗi.*
*- **Infinite loop**: Tool trả về nhiễu khiến Agent lặp lại vô tận.*
*- **Không backtrack**: Đi sai đường nhưng không biết cách quay lại.*

## 2. Reflexion: Teach Agent Self-Reflection
*2. Reflexion: Dạy Agent tự phản tỉnh*

**Reflexion** overcomes ReAct's weaknesses by incorporating **Self-evaluation** into the reasoning loop:
- **4-step Architecture**:
  1. **Actor**: Generates actions.
  2. **Evaluator**: Scores the result (Right/Wrong).
  3. **Reflector**: Extracts lessons from mistakes (Reflection Memory).
  4. **Retry**: Tries again with a new strategy.
- **Reflection Memory**: A concise form of *episodic memory* that includes `failure_reason`, `lesson`, and `next_strategy`. The agent learns from previous run mistakes to avoid repeating errors, significantly improving accuracy (e.g., increasing 20-30% on HotpotQA compared to ReAct).
- **Evaluator Note**: Evaluation should be based on structured output (Pydantic/JSON) to ensure specific reasons (reason) that help the Reflector analyze easily.
***Reflexion** khắc phục điểm yếu của ReAct bằng cách đưa **Self-evaluation** (tự đánh giá) vào reasoning loop:*
*- **Kiến trúc 4 bước**:*
  *1. **Actor**: Sinh ra hành động.*
  *2. **Evaluator**: Chấm điểm kết quả (Right/Wrong).*
  *3. **Reflector**: Rút ra bài học từ sai lầm (Reflection Memory).*
  *4. **Retry**: Thử lại với chiến lược mới.*
*- **Reflection Memory**: Là dạng *episodic memory* ngắn gọn, bao gồm `failure_reason`, `lesson`, và `next_strategy`. Agent học từ sai lầm của lần chạy trước để tránh lặp lại lỗi, giúp cải thiện đáng kể độ chính xác (ví dụ tăng từ 20-30% trên HotpotQA so với ReAct).*
*- **Lưu ý Evaluator**: Đánh giá cần dựa trên structured output (Pydantic/JSON) để đảm bảo có lý do (reason) cụ thể giúp Reflector có thể phân tích dễ dàng.*

## 3. LATS and Voyager
*3. LATS và Voyager*

- **LATS (Language Agent Tree Search)**: Combines MCTS (Monte Carlo Tree Search) and LLM to explore multiple solution branches and support `undo` backtracking. Extremely accurate but compute-intensive (3-5 times more), suitable for high-stakes tasks (e.g., code generation).
- **Voyager**: An agent with compound learning ability across multiple episodes, automatically recording verified skills into a library for reuse in other tasks.
*- **LATS (Language Agent Tree Search)**: Kết hợp MCTS (Monte Carlo Tree Search) và LLM để thử nghiệm nhiều nhánh giải pháp và có khả năng `undo` quay lui. Có độ chính xác cực cao nhưng tốn kém compute (gấp 3-5 lần), phù hợp với high-stakes task (như code generation).*
*- **Voyager**: Agent có khả năng học tập tích lũy kỹ năng (*compound learning*) qua nhiều episode, tự động ghi nhận các skill đã verified vào thư viện để sử dụng lại cho tác vụ khác.*

## 4. Safe Deployment for Production
*4. Triển khai an toàn cho Production*

When Multi-agent is not yet needed, optimize Single-agent with these techniques:
- **Separate Plan - Act - Verify**: Instead of "think and act immediately", the agent creates a plan of subgoals, calls tools, then verifies observations for better stability.
- **Safety Checklist**:
  1. Configure `max_attempts` to prevent infinite loops.
  2. Use structured outputs for tools and evaluators.
  3. Build traces for early debugging (Observability).
  4. Risk tiering: Read-only vs Write (require human review/approval gate for sensitive operations).
- Do not rush to move to a **Multi-agent** system unless the problem is open-ended, truly needs a delegation workflow (Planner / Worker / Judge), or handles multiple domain tools in parallel.
*Khi chưa cần đến Multi-agent, hãy tối ưu Single-agent với các kỹ thuật:*
*- **Tách bạch Plan - Act - Verify**: Thay vì "nghĩ rồi làm luôn", Agent lập plan các subgoals, gọi tool, rồi verify observation để ổn định hơn.*
*- **Checklist an toàn**:*
  *1. Cấu hình `max_attempts` để chống lặp vô tận.*
  *2. Dùng structured outputs cho tool và evaluator.*
  *3. Xây dựng traces để debug từ sớm (Observability).*
  *4. Phân cấp rủi ro (Risk tiering): Read-only vs Write (cần human review/approval gate cho thao tác nhạy cảm).*
*- Đừng vội chuyển sang hệ thống **Multi-agent** trừ khi bài toán mở, thực sự cần workflow phân quyền (Planner / Worker / Judge) hoặc xử lý nhiều domain tool song song.*
