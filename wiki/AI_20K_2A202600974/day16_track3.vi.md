---
type: summary
title: "Day 16 Track 3: Advanced Agent Architectures"
description: "Kiến trúc Agent nâng cao: Reflexion, LATS, Voyager và cách triển khai an toàn"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/phase2-day01-advanced-agent-architectures-extended-fuller.pdf"]
---
> *Lộ trình:* [[track3_ai_app]]

*Kiến trúc Agent Nâng cao*

*Nghiên cứu nguyên nhân Single Agent (như ReAct) thất bại trong các bài toán phức tạp và cách khắc phục bằng các pattern nâng cao.*

*1. Giới hạn của Single Agent (ReAct)*

*Mô hình **ReAct (Reasoning + Acting)** rất mạnh nhưng thiếu khả năng tự đánh giá. Khi gặp lỗi, ReAct dễ rơi vào:*
*- **Lỗi lan tỏa**: Sai ở bước đầu dẫn đến sai toàn bộ chuỗi.*
*- **Infinite loop**: Tool trả về nhiễu khiến Agent lặp lại vô tận.*
*- **Không backtrack**: Đi sai đường nhưng không biết cách quay lại.*

*2. Reflexion: Dạy Agent tự phản tỉnh*

***Reflexion** khắc phục điểm yếu của ReAct bằng cách đưa **Self-evaluation** (tự đánh giá) vào reasoning loop:*
*- **Kiến trúc 4 bước**:*
  *1. **Actor**: Sinh ra hành động.*
  *2. **Evaluator**: Chấm điểm kết quả (Right/Wrong).*
  *3. **Reflector**: Rút ra bài học từ sai lầm (Reflection Memory).*
  *4. **Retry**: Thử lại với chiến lược mới.*
*- **Reflection Memory**: Là dạng *episodic memory* ngắn gọn, bao gồm `failure_reason`, `lesson`, và `next_strategy`. Agent học từ sai lầm của lần chạy trước để tránh lặp lại lỗi, giúp cải thiện đáng kể độ chính xác (ví dụ tăng từ 20-30% trên HotpotQA so với ReAct).*
*- **Lưu ý Evaluator**: Đánh giá cần dựa trên structured output (Pydantic/JSON) để đảm bảo có lý do (reason) cụ thể giúp Reflector có thể phân tích dễ dàng.*

*3. LATS và Voyager*

*- **LATS (Language Agent Tree Search)**: Kết hợp MCTS (Monte Carlo Tree Search) và LLM để thử nghiệm nhiều nhánh giải pháp và có khả năng `undo` quay lui. Có độ chính xác cực cao nhưng tốn kém compute (gấp 3-5 lần), phù hợp với high-stakes task (như code generation).*
*- **Voyager**: Agent có khả năng học tập tích lũy kỹ năng (*compound learning*) qua nhiều episode, tự động ghi nhận các skill đã verified vào thư viện để sử dụng lại cho tác vụ khác.*

*4. Triển khai an toàn cho Production*

*Khi chưa cần đến Multi-agent, hãy tối ưu Single-agent với các kỹ thuật:*
*- **Tách bạch Plan - Act - Verify**: Thay vì "nghĩ rồi làm luôn", Agent lập plan các subgoals, gọi tool, rồi verify observation để ổn định hơn.*
*- **Checklist an toàn**:*
  *1. Cấu hình `max_attempts` để chống lặp vô tận.*
  *2. Dùng structured outputs cho tool và evaluator.*
  *3. Xây dựng traces để debug từ sớm (Observability).*
  *4. Phân cấp rủi ro (Risk tiering): Read-only vs Write (cần human review/approval gate cho thao tác nhạy cảm).*
*- Đừng vội chuyển sang hệ thống **Multi-agent** trừ khi bài toán mở, thực sự cần workflow phân quyền (Planner / Worker / Judge) hoặc xử lý nhiều domain tool song song.*
