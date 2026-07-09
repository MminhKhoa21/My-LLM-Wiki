---
type: summary
title: "Day 26 – Track 3: Model Context Protocol (MCP) Tool Integration"
description: "Detailed dive into building MCP servers with FastMCP and integrating them natively with LLMs."
tags: [mcp, fastmcp, tool-integration, llm-tools, architecture]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/26/Day26-Track3-MCP-tool-integration.pdf"]
---
Dưới đây là nội dung file `day26_track3.md` đã được hoàn thiện đầy đủ song ngữ Anh - Việt, giữ nguyên định dạng Markdown và cấu trúc gốc. Mỗi đoạn văn, dòng tiêu đề, danh sách đều có cả hai ngôn ngữ, đảm bảo rõ ràng và dễ theo dõi.

```markdown
> **Lộ trình:** [[track3_ai_app|Track 3: AI App]]
> **Roadmap:** [[track3_ai_app|Track 3: AI App]]

# Day 26 – Track 3: Model Context Protocol (MCP) Tool Integration
# Ngày 26 – Track 3: Tích hợp công cụ Model Context Protocol (MCP)

This document covers the Model Context Protocol (MCP), focusing on the problems it solves, its architecture, and practical implementation details using the FastMCP Python SDK.
Tài liệu này đề cập đến Model Context Protocol (MCP), tập trung vào các vấn đề mà nó giải quyết, kiến trúc của nó và các chi tiết triển khai thực tế bằng cách sử dụng FastMCP Python SDK.

---

## 1. The N×M Problem and Why MCP is Needed
## 1. Vấn đề N×M và Tại sao cần MCP

Before MCP, integrating tools with different LLM providers (OpenAI, Anthropic, Google) required custom adapters for each combination. Connecting 3 providers to 3 tools meant writing 9 separate adapters (N×M).
Trước MCP, việc tích hợp công cụ với các nhà cung cấp LLM khác nhau (OpenAI, Anthropic, Google) yêu cầu các bộ chuyển đổi (adapter) tùy chỉnh cho từng kết hợp. Việc kết nối 3 nhà cung cấp với 3 công cụ đồng nghĩa với việc viết 9 bộ chuyển đổi riêng biệt (N×M).

MCP introduces a universal, provider-agnostic standard (similar to USB-C for devices). By implementing MCP, the integration complexity drops to N+M (6 adapters). Developers "write once, run anywhere."
MCP giới thiệu một tiêu chuẩn chung, không phụ thuộc vào nhà cung cấp (tương tự như USB-C cho các thiết bị). Bằng cách triển khai MCP, độ phức tạp tích hợp giảm xuống còn N+M (6 bộ chuyển đổi). Các nhà phát triển "viết một lần, chạy mọi nơi."

## 2. MCP Architecture
## 2. Kiến trúc MCP

The MCP ecosystem relies on a standardized connection between Host, Client, and Server:
Hệ sinh thái MCP dựa trên kết nối tiêu chuẩn hóa giữa Host (Máy chủ), Client (Máy khách) và Server (Máy phục vụ):
- **Host:** The environment running the LLM (e.g., Claude Desktop, Cursor).
- **Host (Máy chủ):** Môi trường chạy LLM (ví dụ: Claude Desktop, Cursor).
- **Client:** The interface communicating with the MCP Server.
- **Client (Máy khách):** Giao diện giao tiếp với MCP Server.
- **Server:** Exposes specific capabilities (e.g., PostgreSQL, GitHub tools).
- **Server (Máy phục vụ):** Cung cấp các khả năng cụ thể (ví dụ: PostgreSQL, các công cụ GitHub).
- **Transport:** Can be local `stdio` (same machine, low latency) or `SSE/HTTP` (remote, production).
- **Transport (Giao thức truyền tải):** Có thể là `stdio` cục bộ (cùng một máy, độ trễ thấp) hoặc `SSE/HTTP` (từ xa, môi trường production).

### 6 Core Primitives of MCP
### 6 Nguyên thủy cốt lõi của MCP
1. **Tools:** Callable functions the LLM decides to use (e.g., `query_db()`).
1. **Tools (Công cụ):** Các hàm có thể gọi mà LLM quyết định sử dụng (ví dụ: `query_db()`).
2. **Resources:** Read-only data (URIs) provided as context (e.g., `file://docs/guide.md`).
2. **Resources (Tài nguyên):** Dữ liệu chỉ đọc (URIs) được cung cấp dưới dạng ngữ cảnh (ví dụ: `file://docs/guide.md`).
3. **Prompts:** Reusable interaction templates.
3. **Prompts (Dấu nhắc):** Các mẫu tương tác có thể tái sử dụng.
4. **Roots:** Secure workspace access provided by the client.
4. **Roots (Gốc):** Quyền truy cập không gian làm việc an toàn do client cung cấp.
5. **Sampling:** Server requesting the LLM to perform further reasoning.
5. **Sampling (Lấy mẫu):** Server yêu cầu LLM thực hiện suy luận thêm.
6. **Elicitation:** Server asking the user for structured input via the host UI.
6. **Elicitation (Khơi gợi):** Server yêu cầu người dùng nhập thông tin có cấu trúc thông qua giao diện người dùng (UI) của host.

Takeaway: MCP is a protocol for **context exchange**, not just "function calling". Resources and Prompts are highly underutilized but powerful.
Bài học: MCP là một giao thức để **trao đổi ngữ cảnh**, không chỉ là "gọi hàm". Tài nguyên và Dấu nhắc thường ít được sử dụng nhưng rất mạnh mẽ.

## 3. Building an MCP Server with Python SDK (FastMCP)
## 3. Xây dựng một MCP Server với Python SDK (FastMCP)

The `FastMCP` framework allows for building production-ready servers cleanly using decorators:
Framework `FastMCP` cho phép xây dựng các server sẵn sàng cho production một cách gọn gàng bằng cách sử dụng các decorators:
- `@mcp.tool()`: Exposes a function for the LLM to call.
- `@mcp.tool()`: Cung cấp một hàm để LLM gọi.
- `@mcp.resource()`: Exposes read-only data.
- `@mcp.resource()`: Cung cấp dữ liệu chỉ đọc.
- `@mcp.prompt()`: Defines reusable prompts.
- `@mcp.prompt()`: Định nghĩa các prompt có thể tái sử dụng.

**Crucial Note:** The tool description (docstring) is the most critical element. LLMs rely 100% on the `name` + `description` to decide which tool to call. Vague descriptions lead to hallucinated tool usage or failures.
**Lưu ý quan trọng:** Mô tả công cụ (docstring) là yếu tố quan trọng nhất. Các LLM dựa 100% vào `name` + `description` để quyết định gọi công cụ nào. Các mô tả mơ hồ sẽ dẫn đến việc sử dụng công cụ bị ảo giác hoặc thất bại.

## 4. Security, Registry, and Versioning
## 4. Bảo mật, Đăng ký (Registry) và Phiên bản (Versioning)

Production-grade MCP servers demand robust security:
Các MCP server cấp production đòi hỏi bảo mật mạnh mẽ:
- **Transport Security:** `stdio` is secure locally, but remote HTTP/SSE must use OAuth 2.0 and TLS.
- **Bảo mật truyền tải:** `stdio` an toàn cục bộ, nhưng HTTP/SSE từ xa phải sử dụng OAuth 2.0 và TLS.
- **Input Validation:** Must happen server-side.
- **Xác thực đầu vào:** Phải diễn ra ở phía server.
- **Permissions:** Apply the principle of least privilege.
- **Quyền hạn:** Áp dụng nguyên tắc đặc quyền tối thiểu.
- **Audit Logs:** Log every tool call and result.
- **Nhật ký kiểm toán (Audit Logs):** Ghi chép lại mọi lần gọi công cụ và kết quả.

**Tool Registries** allow agents to discover tools at runtime based on task requirements, utilizing Semantic Versioning (Semver) to manage breaking changes.
**Tool Registries (Hệ thống đăng ký công cụ)** cho phép các tác tử khám phá các công cụ tại thời điểm chạy dựa trên yêu cầu nhiệm vụ, sử dụng Semantic Versioning (Semver - Phiên bản theo ngữ nghĩa) để quản lý các thay đổi đột phá.

## 5. Best Practices & Workflows
## 5. Thực hành tốt nhất & Quy trình làm việc

### Claude Code + Codex Practices
### Thực hành với Claude Code + Codex
- **Design for Search/Read First:** Implement read paths (docs/search/fetch) before write paths (mutations). Let the agent read the exact context before acting.
- **Thiết kế Ưu tiên Tìm kiếm/Đọc:** Triển khai các đường dẫn đọc (tài liệu/tìm kiếm/lấy dữ liệu) trước các đường dẫn ghi (đột biến). Hãy để tác tử đọc ngữ cảnh chính xác trước khi hành động.
- **Limit Context Bloat:** Return summaries + IDs instead of dumping massive JSON payloads into the context window.
- **Hạn chế phình to ngữ cảnh:** Trả về các bản tóm tắt + ID thay vì đổ các khối dữ liệu JSON khổng lồ vào cửa sổ ngữ cảnh.
- **Use the MCP Inspector:** Always test schemas, output formats, and error handling locally in the Inspector before integrating with Claude Desktop.
- **Sử dụng MCP Inspector:** Luôn kiểm tra các schema (lược đồ), định dạng đầu ra và xử lý lỗi cục bộ trong Inspector trước khi tích hợp với Claude Desktop.

### High ROI Workflows
### Quy trình làm việc mang lại ROI (Tỷ suất hoàn vốn) cao
- **Ticket -> Code -> PR:** GitHub MCP + Docs MCP. Agent reads the issue, fixes the code, and creates a PR.
- **Ticket -> Code -> PR:** GitHub MCP + Docs MCP. Tác tử đọc issue, sửa mã và tạo PR.
- **Prod Error -> Root Cause:** Sentry MCP + GitHub MCP. Agent analyzes the stack trace, maps it to a commit, and drafts a fix.
- **Lỗi Prod -> Nguyên nhân gốc rễ:** Sentry MCP + GitHub MCP. Tác tử phân tích stack trace, ánh xạ nó với một commit và phác thảo bản sửa lỗi.
- **Library Upgrade -> Migration:** Docs MCP + Playwright MCP. Agent reads new framework docs, refactors code, and verifies UI flow.
- **Nâng cấp Thư viện -> Di chuyển:** Docs MCP + Playwright MCP. Tác tử đọc tài liệu framework mới, cấu trúc lại mã và xác minh luồng UI.
```

Nếu bạn cần thêm bất kỳ điều chỉnh nào về phong cách (ví dụ: in nghiêng hoàn toàn cho phần tiếng Việt), tôi sẵn sàng hỗ trợ.

---

Câu hỏi ôn tập Ngày 26

   Vấn đề N×M trong tích hợp công cụ LLM được giải quyết như thế nào bởi MCP?
   - A. Bằng cách yêu cầu mỗi nhà cung cấp LLM viết adapter riêng.
   - B. Bằng cách giới thiệu một giao thức chuẩn, giảm độ phức tạp từ N×M xuống N+M.
   - C. Bằng cách loại bỏ hoàn toàn nhu cầu sử dụng công cụ bên ngoài.
   - D. Bằng cách chỉ hỗ trợ một nhà cung cấp LLM duy nhất.
   **Đáp án / Answer:** B

   Trong kiến trúc MCP, thành phần nào chịu trách nhiệm cung cấp các hàm có thể gọi được (callable functions) cho LLM quyết định sử dụng?
   - A. Tài nguyên
   - B. Lời nhắc
   - C. Công cụ
   - D. Gốc
   **Đáp án / Answer:** C

   Khi xây dựng MCP Server bằng FastMCP, yếu tố nào được nhấn mạnh là quan trọng nhất để LLM quyết định gọi tool chính xác?
   - A. Tên hàm và kiểu dữ liệu đầu vào.
   - B. Mô tả tool (docstring) rõ ràng.
   - C. Số lượng tham số của hàm.
   - D. Tốc độ xử lý của server.
   **Đáp án / Answer:** B

   Để bảo mật MCP Server từ xa (remote), giao thức nào bắt buộc phải được sử dụng?
   - A. HTTP không mã hóa.
   - B. SSH với private key.
   - C. OAuth 2.0 và TLS.
   - D. Chỉ cần xác thực qua API key.
   **Đáp án / Answer:** C

   Theo best practices của Claude Code, nên ưu tiên thiết kế luồng nào trước khi thực hiện các thay đổi (mutations)?
   - A. Luồng ghi (write) để tác động nhanh.
   - B. Luồng đọc/tìm kiếm (search/read) để lấy ngữ cảnh chính xác.
   - C. Luồng xóa (delete) để dọn dẹp dữ liệu.
   - D. Luồng cập nhật (update) để đồng bộ ngay lập tức.
   **Đáp án / Answer:** B
