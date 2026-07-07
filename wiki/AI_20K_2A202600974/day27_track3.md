---
type: summary
title: "Summary: Day 27 Track 3 - Human-in-the-Loop UX"
description: "A summary on designing Human-in-the-Loop (HITL) interactions, bounded autonomy, and approval workflows for AI agents."
tags: [human-in-the-loop, ai-agents, ux, langgraph, governance]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/27/Day12 - Track 3 - Human-in-the-loop-ux-khi-nao-agent-can-xin-phep.pdf"]
---
# Day 27 Track 3 - Human-in-the-Loop UX
# Ngày 27 Track 3 - Trải nghiệm người dùng Human-in-the-Loop (HITL)

This document summarizes the Day 27 Track 3 lecture on the User Experience (UX) of Human-in-the-Loop (HITL) systems, focusing on when and how AI agents should ask for human permission.

Tài liệu này tóm tắt bài giảng Ngày 27 Track 3 về Trải nghiệm người dùng (UX) của các hệ thống Human-in-the-Loop (HITL), tập trung vào thời điểm và cách thức các AI agent nên xin phép con người.

## 1. The Danger of Full Autonomy
## 1. Sự nguy hiểm của tính tự chủ hoàn toàn

Allowing an AI agent full autonomy can lead to catastrophic consequences if the agent makes a high-confidence but incorrect decision (e.g., deleting a database without approval). 
The 2026 industry standard shifts from "full autonomy" to **Bounded Autonomy**: agents can act automatically within defined safe boundaries (e.g., read/search), but must ask for permission when crossing risk boundaries (e.g., side-effects, sending emails, prod deployments).

Việc cho phép một AI agent tự chủ hoàn toàn có thể dẫn đến những hậu quả thảm khốc nếu agent đưa ra quyết định có độ tự tin cao nhưng không chính xác (ví dụ: xóa cơ sở dữ liệu mà không cần phê duyệt). 
Tiêu chuẩn ngành năm 2026 chuyển từ "tự chủ hoàn toàn" sang **Tự chủ có giới hạn (Bounded Autonomy)**: các agent có thể hoạt động tự động trong các ranh giới an toàn đã được xác định (ví dụ: đọc/tìm kiếm), nhưng phải xin phép khi vượt qua các ranh giới rủi ro (ví dụ: gây ra tác động phụ, gửi email, triển khai môi trường production).

## 2. HITL Taxonomy - 6 Interaction Patterns
## 2. Phân loại HITL - 6 Mô hình Tương tác

There is a spectrum from Full Manual to Full Auto. The "sweet spot" depends on risk and trust. The 6 key interaction patterns are:

Có một phổ trải dài từ Hoàn toàn Thủ công (Full Manual) đến Hoàn toàn Tự động (Full Auto). "Điểm cân bằng" phụ thuộc vào rủi ro và độ tin cậy. 6 mô hình tương tác chính là:

1. **Approval:** For side effects (e.g., Deploy, delete data).
1. **Phê duyệt (Approval):** Dành cho các hành động có tác động phụ (ví dụ: Triển khai, xóa dữ liệu).
2. **Clarification:** For ambiguous inputs (e.g., "Report Q1 or Q2?").
2. **Làm rõ (Clarification):** Dành cho các đầu vào mơ hồ (ví dụ: "Báo cáo Q1 hay Q2?").
3. **Structured Elicitation:** For missing mandatory fields (e.g., form to select environment).
3. **Thu thập có cấu trúc (Structured Elicitation):** Dành cho các trường thông tin bắt buộc bị thiếu (ví dụ: biểu mẫu chọn môi trường).
4. **Review Checkpoint:** For inspecting draft outputs (e.g., Code PRs, draft emails).
4. **Điểm kiểm tra đánh giá (Review Checkpoint):** Dành cho việc kiểm tra các kết quả dự thảo (ví dụ: Pull Request mã nguồn, email nháp).
5. **Edit / Correction:** Allowing humans to edit arguments before execution.
5. **Chỉnh sửa / Sửa chữa (Edit / Correction):** Cho phép con người chỉnh sửa các tham số trước khi thực thi.
6. **Escalation:** Bumping decisions to higher authorities for legal/security risks.
6. **Leo thang (Escalation):** Chuyển quyết định lên các cấp thẩm quyền cao hơn đối với các rủi ro về pháp lý/bảo mật.

## 3. Confidence Routing: When to Interrupt?
## 3. Định tuyến theo độ tự tin: Khi nào nên ngắt quãng?

Agents shouldn't interrupt solely based on a single confidence score. Interruptions should occur based on heuristic action classes:

Các agent không nên ngắt quãng chỉ dựa trên một điểm số tự tin duy nhất. Việc ngắt quãng nên xảy ra dựa trên các phân lớp hành động mang tính kinh nghiệm (heuristic):

- **Reversible?** If yes, prefer auto-execution.
- **Có thể đảo ngược (Reversible)?** Nếu có, ưu tiên tự động thực thi.
- **External Side-effects?** If yes, require review/approval.
- **Có tác động phụ ra bên ngoài (External Side-effects)?** Nếu có, yêu cầu đánh giá/phê duyệt.
- **Missing Information?** If yes, ask using structured forms.
- **Thiếu thông tin (Missing Information)?** Nếu có, hãy hỏi thông qua các biểu mẫu có cấu trúc.

*Note:* Policy-aware gating is crucial. Even a highly confident model must stop if it touches sensitive data or strict policy boundaries.

*Lưu ý:* Việc kiểm soát dựa trên nhận thức về chính sách là rất quan trọng. Ngay cả một mô hình có độ tự tin cao cũng phải dừng lại nếu nó chạm tới dữ liệu nhạy cảm hoặc các ranh giới chính sách nghiêm ngặt.

## 4. Approval Workflows & Implementation
## 4. Luồng công việc Phê duyệt & Triển khai

Using tools like **LangGraph**, HITL can be programmed systematically:

Sử dụng các công cụ như **LangGraph**, HITL có thể được lập trình một cách có hệ thống:

- **Interrupt / Resume:** Pause at policy nodes, allowing humans to approve, edit, or reject. Resuming must happen on the same thread/checkpoint.
- **Ngắt / Tiếp tục (Interrupt / Resume):** Tạm dừng tại các node chính sách, cho phép con người phê duyệt, chỉnh sửa hoặc từ chối. Việc tiếp tục phải diễn ra trên cùng một luồng/điểm kiểm tra (thread/checkpoint).
- **Granular Decisions:** Define per-tool policies (e.g., `send_email` allows `approve/edit/reject`, while `ask_user` allows `respond`).
- **Quyết định chi tiết (Granular Decisions):** Xác định chính sách cho từng công cụ (ví dụ: `send_email` cho phép `approve/edit/reject`, trong khi `ask_user` cho phép `respond`).
- **Review Cards & Structured Forms:** Instead of simple Yes/No modals, present users with Review Cards containing What/Why/Risk/Rollback info, alongside editable fields.
- **Thẻ Đánh giá & Biểu mẫu Có cấu trúc (Review Cards & Structured Forms):** Thay vì các hộp thoại Yes/No đơn giản, hãy cung cấp cho người dùng các Thẻ Đánh giá chứa thông tin về Cái gì/Tại sao/Rủi ro/Cách khôi phục (What/Why/Risk/Rollback), cùng với các trường có thể chỉnh sửa.

## 5. 2026 Product Landscape
## 5. Bức tranh Sản phẩm năm 2026

Big tech companies are converging on bounded autonomy:

Các công ty công nghệ lớn đang hội tụ về hướng tự chủ có giới hạn:

- **OpenAI Codex:** Separates permission boundaries from reasoning. Supports `requestUserInput` and async remote approvals.
- **OpenAI Codex:** Tách biệt ranh giới cấp phép khỏi quá trình suy luận. Hỗ trợ `requestUserInput` và phê duyệt từ xa bất đồng bộ.
- **Anthropic Claude Code:** Exposes permission modes (default, acceptEdits, plan, auto) directly to the user, with programmable hooks.
- **Anthropic Claude Code:** Cung cấp các chế độ cấp phép (default, acceptEdits, plan, auto) trực tiếp cho người dùng, với các hook có thể lập trình được.
- **Google Gemini (Computer Use):** Pauses right before the final irreversible step (e.g., clicking "Confirm Purchase").
- **Google Gemini (Sử dụng Máy tính):** Tạm dừng ngay trước bước cuối cùng không thể đảo ngược (ví dụ: nhấp vào "Xác nhận Mua").
- **Cursor:** Reduces approval fatigue with Plan Mode and Auto-review (using classifier subagents).
- **Cursor:** Giảm thiểu sự mệt mỏi khi phê duyệt bằng Chế độ Kế hoạch (Plan Mode) và Tự động đánh giá (Auto-review) (sử dụng các subagent phân loại).

## 6. Feedback Loops, Analytics & Audit Trails
## 6. Vòng lặp phản hồi, Phân tích & Chuỗi kiểm toán

To safely scale autonomy, robust tracking is required:

Để mở rộng tính tự chủ một cách an toàn, cần có hệ thống theo dõi mạnh mẽ:

- **Audit Trails:** Log *who* (agent & reviewer), *what* (action), *when*, and *why* for compliance (SOC2/GDPR).
- **Chuỗi kiểm toán (Audit Trails):** Ghi chép lại *ai* (agent & người đánh giá), *cái gì* (hành động), *khi nào*, và *tại sao* để phục vụ cho việc tuân thủ (SOC2/GDPR).
- **Decision Analytics:** Track Approval Rate, Review Latency, and Regret Rate. Only increase autonomy when approval rates are high and regret rates are low.
- **Phân tích Quyết định (Decision Analytics):** Theo dõi Tỷ lệ Phê duyệt, Độ trễ Đánh giá, và Tỷ lệ Hối tiếc (Regret Rate). Chỉ tăng cường tính tự chủ khi tỷ lệ phê duyệt cao và tỷ lệ hối tiếc thấp.

## 7. HITL UX Best Practices
## 7. Thực hành tốt nhất cho HITL UX

Avoid simple Yes/No prompts for complex actions. Ask early for missing data, ask late for irreversible actions. Reduce cognitive load with dropdowns and scoped approvals (e.g., "approve for this session"). Interruptions should feel like small, structured interactions, not roadblocks.

Tránh các lời nhắc Yes/No đơn giản cho các hành động phức tạp. Hỏi thông tin sớm nếu thiếu dữ liệu, hỏi muộn đối với các hành động không thể đảo ngược. Giảm tải nhận thức bằng các danh sách thả xuống (dropdown) và các phê duyệt có phạm vi giới hạn (ví dụ: "phê duyệt cho phiên này"). Việc ngắt quãng nên mang lại cảm giác như các tương tác nhỏ, có cấu trúc chứ không phải là rào cản.
