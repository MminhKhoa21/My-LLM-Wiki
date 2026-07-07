---
type: summary
title: "Memory Systems for Agents (Track 3)"
description: "Summary of Day 17 Track 3 on designing memory systems for AI agents, including Short-term, Long-term, Episodic, and Semantic memory."
tags: [AI_20K_2A202600974, Day17, AI_Agents, Memory]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/17/Day17 - Track 3 - Memory-systems-for-agents.pdf"]
---
# Memory Systems for Agents (Day 17 - Track 3)

*# Hệ thống Bộ nhớ cho Tác nhân (Ngày 17 - Track 3)*

This track addresses a major challenge in deploying AI agents: agents are stateless by default and "forget" information between sessions. A robust memory system combines the fast access of the context window with the persistent storage of external databases.

*Track này giải quyết một thách thức lớn khi triển khai các tác nhân AI: các tác nhân mặc định là không trạng thái và "quên" thông tin giữa các phiên. Một hệ thống bộ nhớ mạnh mẽ kết hợp khả năng truy cập nhanh của cửa sổ ngữ cảnh với lưu trữ bền vững của các cơ sở dữ liệu bên ngoài.*

## 4 Types of Cognitive Memory for Agents

*## 4 Loại Bộ nhớ Nhận thức cho Tác nhân*

1. **Short-term (Working) Memory:** Managed within the LLM context window. Fast, temporary, and limited by token budget. Best managed via a sliding window strategy (system prompt + summary + last K turns) to avoid hitting token limits.

1.  ***Bộ nhớ Ngắn hạn (Làm việc):** Được quản lý trong cửa sổ ngữ cảnh của LLM. Nhanh, tạm thời và bị giới hạn bởi ngân sách token. Quản lý tốt nhất thông qua chiến lược cửa sổ trượt (lời nhắc hệ thống + tóm tắt + K lượt gần nhất) để tránh chạm giới hạn token.*

2. **Long-term (Declarative) Memory:** Persistent across sessions, storing user profiles, preferences, and facts (e.g., using Redis). Info is loaded into the system prompt when a new session begins.

2.  ***Bộ nhớ Dài hạn (Tuyên bố):** Bền vững qua các phiên, lưu trữ hồ sơ người dùng, sở thích và sự kiện (ví dụ: sử dụng Redis). Thông tin được nạp vào lời nhắc hệ thống khi một phiên mới bắt đầu.*

3. **Episodic Memory:** A sequential log of past experiences and reflections (e.g., "I tried approach X and it failed because of Y"). Useful for learning from past trajectories.

3.  ***Bộ nhớ Tình tiết:** Nhật ký tuần tự về các trải nghiệm và suy ngẫm trong quá khứ (ví dụ: "Tôi đã thử cách tiếp cận X và nó thất bại vì Y"). Hữu ích cho việc học hỏi từ các quỹ đạo trong quá khứ.*

4. **Semantic Memory:** Domain knowledge encoded into embeddings and stored in a Vector DB. Agents retrieve relevant facts via cosine similarity search.

4.  ***Bộ nhớ Ngữ nghĩa:** Kiến thức miền được mã hóa thành các embedding và lưu trữ trong Cơ sở dữ liệu Vector. Các tác nhân truy xuất các sự kiện liên quan thông qua tìm kiếm tương tự cosine.*

## Implementation & Frameworks

*## Triển khai & Khung công tác*

- **Memory Management Flow:** Buffer (Context Window) -> Summarize (LLM call) -> Extract Key Facts -> Persist (External Store like Redis or Chroma).

- ***Luồng Quản lý Bộ nhớ:** Bộ đệm (Cửa sổ Ngữ cảnh) -> Tóm tắt (gọi LLM) -> Trích xuất Sự kiện Chính -> Lưu trữ Bền vững (Kho lưu trữ Bên ngoài như Redis hoặc Chroma).*

- **LangGraph Integration:** Specialized nodes for loading memory (`retrieve_memory`) and saving memory.

- ***Tích hợp LangGraph:** Các nút chuyên biệt để nạp bộ nhớ (`retrieve_memory`) và lưu bộ nhớ.*

- **Frameworks:** Mem0 and Zep provide managed memory layers with auto-classification and smart retrieval, but custom implementations offer more control.

- ***Khung công tác:** Mem0 và Zep cung cấp các lớp bộ nhớ được quản lý với tự động phân loại và truy xuất thông minh, nhưng việc triển khai tùy chỉnh mang lại nhiều quyền kiểm soát hơn.*

- **Privacy-by-Design:** Crucial for agent memory. Includes data minimization, TTL storage limitation, and mechanisms for "Right to be Forgotten".

- ***Quyền riêng tư theo Thiết kế:** Rất quan trọng cho bộ nhớ tác nhân. Bao gồm tối thiểu hóa dữ liệu, giới hạn lưu trữ TTL và các cơ chế cho "Quyền được Lãng quên".*

## Trends in Agent Memory (2025-2026)

*## Xu hướng về Bộ nhớ Tác nhân (2025-2026)*

1. **Cross-session memory:** Shifting from thread-scoped history to user-scoped profiles and episodic stores.

1.  ***Bộ nhớ xuyên phiên:** Chuyển từ lịch sử phạm vi luồng sang hồ sơ phạm vi người dùng và kho lưu trữ tình tiết.*

2. **Compaction:** Instead of retaining full transcripts, agents compact sessions into summaries, decisions, and durable notes to preserve token budgets and improve accuracy.

2.  ***Nén:** Thay vì giữ lại toàn bộ bản ghi, các tác nhân nén các phiên thành các bản tóm tắt, quyết định và ghi chú bền vững để bảo toàn ngân sách token và cải thiện độ chính xác.*

3. **Identity Files:** Using configuration files like `AGENTS.md` and `SOUL.md` as control planes for agent identity and rules, separate from retrieval memory.

3.  ***Tệp Danh tính:** Sử dụng các tệp cấu hình như `AGENTS.md` và `SOUL.md` làm mặt phẳng điều khiển cho danh tính và quy tắc của tác nhân, tách biệt khỏi bộ nhớ truy xuất.*

4. **Heartbeat Loops:** Agents wake up periodically in the background to refresh states, clean notes, and process backlogs.

4.  ***Vòng lặp Nhịp tim:** Các tác nhân thức dậy định kỳ ở chế độ nền để làm mới trạng thái, dọn dẹp ghi chú và xử lý các công việc tồn đọng.*

5. **Compiled Knowledge Base (LLM Wiki):** Instead of raw RAG on documents, the LLM continuously curates and edits a "wiki" of concepts, entities, and timelines, solving the problem of repetitive RAG queries on the same corpus.

5.  ***Cơ sở Kiến thức Biên dịch (Wiki LLM):** Thay vì RAG thô trên các tài liệu, LLM liên tục quản lý và chỉnh sửa một "wiki" về các khái niệm, thực thể và dòng thời gian, giải quyết vấn đề các truy vấn RAG lặp đi lặp lại trên cùng một kho ngữ liệu.*
