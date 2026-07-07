---
type: summary
title: "Day 20 Track 3: Multi-Agent Systems"
description: "Exploration of advanced multi-agent workflows, including Supervisor, Debate, and Parallel patterns, using frameworks like LangGraph."
tags: [day20, track3, multi-agent, langgraph, supervisor, debate, parallel-execution]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/20/day05-multi-agent-systems-student.pdf"]
---
# Day 20 Track 3: Multi-Agent Systems

*# Day 20 Track 3: Hệ thống Đa tác tử*

## 1. Overview

*## 1. Tổng quan*

This module transitions from single-agent setups to Multi-Agent Systems. While single agents handle simple tasks well, complex scenarios require teams of specialized agents with dedicated roles and shared states. However, adding agents introduces overhead and coordination challenges.

*Mô-đun này chuyển từ thiết lập tác tử đơn lẻ sang Hệ thống Đa tác tử. Trong khi các tác tử đơn lẻ xử lý tốt các tác vụ đơn giản, các kịch bản phức tạp đòi hỏi nhóm các tác tử chuyên biệt với vai trò riêng và trạng thái dùng chung. Tuy nhiên, việc thêm tác tử sẽ phát sinh chi phí bổ sung và thách thức về phối hợp.*

## 2. When to Use Multiple Agents?

*## 2. Khi nào nên sử dụng Nhiều tác tử?*

You should only scale to multi-agent architectures if a single agent cannot achieve >80% accuracy. The three primary drivers for multi-agent systems are:

*Bạn chỉ nên mở rộng sang kiến trúc đa tác tử nếu một tác tử đơn lẻ không thể đạt độ chính xác >80%. Ba động lực chính cho các hệ thống đa tác tử là:*

- **Specialization:** Each agent masters one specific domain (e.g., Researcher, Analyst, Writer).
  *Chuyên môn hóa: Mỗi tác tử làm chủ một lĩnh vực cụ thể (ví dụ: Nhà nghiên cứu, Nhà phân tích, Người viết).*

- **Parallelization:** Running subtasks concurrently to reduce latency.
  *Xử lý song song: Thực hiện các tác vụ con đồng thời để giảm độ trễ.*

- **Cross-checking:** Using consensus and critique to reduce hallucinations.
  *Kiểm tra chéo: Sử dụng sự đồng thuận và phê bình để giảm hiện tượng ảo giác.*

## 3. Anthropic's 5 Agentic Workflow Patterns

*## 3. 5 Mẫu quy trình tác tử của Anthropic*

Start with the simplest pattern and escalate only when measurably needed.

*Bắt đầu với mẫu đơn giản nhất và chỉ nâng cấp khi thực sự cần thiết về mặt đo lường.*

1. **Prompt Chaining:** Sequential operations where one output feeds into the next.
   *1. **Chuỗi Prompt:** Các thao tác tuần tự, đầu ra của bước này là đầu vào cho bước tiếp theo.*

2. **Routing:** Classifying an input and routing it to the most capable specialized handler (reduces costs by sending easy queries to small models and hard queries to large models).
   *2. **Định tuyến:** Phân loại đầu vào và chuyển hướng nó đến bộ xử lý chuyên biệt có năng lực nhất (giảm chi phí bằng cách gửi các truy vấn đơn giản đến mô hình nhỏ và các truy vấn khó đến mô hình lớn).*

3. **Parallel:** Splitting a task into sections for parallel workers, or using voting across multiple models on the same task.
   *3. **Song song:** Chia tác vụ thành các phần cho các tác tử song song, hoặc sử dụng bỏ phiếu giữa nhiều mô hình trên cùng một tác vụ.*

4. **Orchestrator-Workers (Supervisor):** A supervisor LLM delegates tasks to worker agents and aggregates their outputs.
   *4. **Điều phối viên – Nhân viên (Giám sát):** Một LLM giám sát ủy thác các tác vụ cho các tác tử nhân viên và tổng hợp đầu ra của chúng.*

5. **Evaluator-Optimizer:** An iterative generate-and-critique loop.
   *5. **Đánh giá – Tối ưu hóa:** Vòng lặp sinh-và-phê bình lặp đi lặp lại.*

## 4. The Supervisor Pattern (Orchestration)

*## 4. Mẫu Giám sát (Điều phối)*

- Uses a **Hub-Spoke Architecture** implemented typically via LangGraph.
  *Sử dụng **Kiến trúc Hub-Spoke** thường được triển khai qua LangGraph.*

- The Supervisor acts as a router, breaking down a task and deciding which worker to call and in what order.
  *Giám sát viên đóng vai trò như một bộ định tuyến, phân rã một tác vụ và quyết định nhân viên nào cần gọi và theo thứ tự nào.*

- State is managed through a `TypedDict` tracking `messages`, `next_worker`, `worker_results`, and `final_answer`.
  *Trạng thái được quản lý thông qua `TypedDict` theo dõi `messages`, `next_worker`, `worker_results` và `final_answer`.*

- **Failure Modes:** Infinite routing loops or incorrect worker selection (mitigated by setting max iterations).
  *Các chế độ lỗi: Vòng lặp định tuyến vô hạn hoặc lựa chọn nhân viên không chính xác (được giảm thiểu bằng cách đặt số lần lặp tối đa).*

## 5. Debate Agents (Adversarial Collaboration)

*## 5. Tác tử Tranh luận (Cộng tác đối kháng)*

- Multiple agents generate independent answers and then critique each other's work.
  *Nhiều tác tử tạo ra các câu trả lời độc lập và sau đó phê bình công việc của nhau.*

- A "Judge" agent synthesizes the final answer.
  *Một tác tử "Thẩm phán" tổng hợp câu trả lời cuối cùng.*

- Using heterogeneous models (e.g., GPT-4o, Claude, Gemini) avoids "collective delusion" where identically trained models agree on false information.
  *Sử dụng các mô hình không đồng nhất (ví dụ: GPT-4o, Claude, Gemini) tránh được "ảo tưởng tập thể" khi các mô hình được huấn luyện giống hệt nhau đồng thuận về thông tin sai lệch.*

- **Benefits/Trade-offs:** Reduces hallucinations by 15-25% but at the cost of 2-3x higher latency and compute. Best reserved for high-stakes, ambiguous tasks.
  *Lợi ích/Đánh đổi: Giảm 15-25% hiện tượng ảo giác nhưng phải trả giá bằng độ trễ và chi phí tính toán cao gấp 2-3 lần. Tốt nhất nên dành cho các tác vụ có rủi ro cao, mơ hồ.*

## 6. Parallel Execution and Shared State

*## 6. Thực thi Song song và Trạng thái Dùng chung*

- Uses asynchronous Map-Reduce execution (e.g., `asyncio.gather` in Python or LangGraph's Send API).
  *Sử dụng thực thi Map-Reduce không đồng bộ (ví dụ: `asyncio.gather` trong Python hoặc LangGraph's Send API).*

- Agents coordinate either through a central blackboard (Shared State) or through Message Passing queues.
  *Các tác tử phối hợp thông qua một bảng đen trung tâm (Trạng thái Dùng chung) hoặc thông qua hàng đợi truyền tin nhắn.*

- **Failure Handling:** Timeouts, retries, circuit breakers, and dead-letter queues are necessary for production reliability.
  *Xử lý lỗi: Cần có các cơ chế timeout, thử lại, bộ ngắt mạch và hàng đợi thư chết để đảm bảo độ tin cậy trong sản xuất.*

## 7. Multi-Agent Frameworks

*## 7. Các Framework Đa tác tử*

- **LangGraph:** High flexibility, state machine driven, best for full-control production environments.
  *LangGraph: Tính linh hoạt cao, điều khiển bằng máy trạng thái, tốt nhất cho môi trường sản xuất có toàn quyền kiểm soát.*

- **CrewAI:** Role-based and easy to set up, excellent for rapid prototyping.
  *CrewAI: Dựa trên vai trò và dễ thiết lập, tuyệt vời cho tạo mẫu nhanh.*

- **AutoGen:** Group chat and conversational collaboration, strong at code execution.
  *AutoGen: Trò chuyện nhóm và cộng tác hội thoại, mạnh về thực thi mã.*

## 8. Lab 20

*## 8. Lab 20*

The lab focuses on building a 3-agent research system (Researcher, Analyst, Writer) using LangGraph. Students benchmark the single-agent baseline against the multi-agent system measuring accuracy, latency, and cost.

*Lab tập trung vào xây dựng một hệ thống nghiên cứu 3 tác tử (Nhà nghiên cứu, Nhà phân tích, Người viết) sử dụng LangGraph. Sinh viên so sánh điểm chuẩn giữa tác tử đơn lẻ và hệ thống đa tác tử, đo lường độ chính xác, độ trễ và chi phí.*
