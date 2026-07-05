---
type: summary
title: "Day 26 – Track 3: Model Context Protocol (MCP) – Chuẩn hóa Tool Integration"
description: "Giải quyết vấn đề N×M integration: MCP Architecture, build MCP server, security và versioning."
tags: [ai, 20k, day26, track3, mcp, tool-integration]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/26/Day26-Track3-MCP-tool-integration.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# Day 26 – Track 3: Model Context Protocol (MCP)

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 3 · Ngày 26

> **Câu hỏi trọng tâm**: MCP giải quyết vấn đề gì mà function calling thông thường không giải quyết được?

---

## Vấn đề N×M

Trước MCP, mỗi AI provider có format riêng → cần viết **N × M integration code**:

```
N models × M tools = N×M adapters
GPT-4 + Search = 1 adapter
GPT-4 + Database = 1 adapter
Claude + Search = 1 adapter
...
```

**MCP giải quyết**: Chuẩn hóa thành **N + M** (mỗi tool chỉ cần 1 MCP server, mỗi model chỉ cần 1 MCP client).

---

## MCP Architecture

```
AI Model (MCP Client)
    │
    │ JSON-RPC over stdio/HTTP
    ▼
MCP Server
    ├── tools/list       → liệt kê tools
    ├── tools/call       → gọi tool
    ├── resources/list   → liệt kê data sources
    └── prompts/list     → prompt templates
```

---

## Build MCP Server với Python SDK

```python
from mcp.server import Server
from mcp.server.models import InitializationOptions
import mcp.types as types

server = Server("my-tools-server")

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    return [
        types.Tool(
            name="search_web",
            description="Search the web for information",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "Search query"}
                },
                "required": ["query"]
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(name: str, arguments: dict) -> list[types.TextContent]:
    if name == "search_web":
        result = await do_web_search(arguments["query"])
        return [types.TextContent(type="text", text=result)]
```

---

## Security, Registry & Versioning

| Khía cạnh | Thực hành |
|-----------|----------|
| **Auth** | API key hoặc OAuth2 cho MCP server |
| **Rate limiting** | Giới hạn tool calls per minute |
| **Versioning** | Semantic versioning cho tool schema |
| **Registry** | Central catalog để discover tools |
| **Audit trail** | Log mọi tool call với user context |

---

## MCP trong thực tế 2026

- **Claude Desktop**: Built-in MCP support  
- **Cursor/Windsurf**: MCP cho coding tools  
- **GitHub Copilot**: MCP cho code search  
- **Community servers**: 500+ open-source MCP servers

---

## Liên kết
- [[day9_overview]] – Multi-Agent & MCP (nền tảng)
- [[day26_track2]] – MCP/A2A Infrastructure
- [[day26_overview]]
