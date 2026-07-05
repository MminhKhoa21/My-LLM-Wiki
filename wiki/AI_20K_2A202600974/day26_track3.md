---
type: summary
title: "Day 26 – Track 3: Model Context Protocol (MCP) Tool Integration"
description: "Detailed dive into building MCP servers with FastMCP and integrating them natively with LLMs."
tags: [mcp, fastmcp, tool-integration, llm-tools, architecture]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/26/Day26-Track3-MCP-tool-integration.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI App]]

# Day 26 – Track 3: Model Context Protocol (MCP) Tool Integration

This document covers the Model Context Protocol (MCP), focusing on the problems it solves, its architecture, and practical implementation details using the FastMCP Python SDK.

---

## 1. The N×M Problem and Why MCP is Needed

Before MCP, integrating tools with different LLM providers (OpenAI, Anthropic, Google) required custom adapters for each combination. Connecting 3 providers to 3 tools meant writing 9 separate adapters (N×M).
MCP introduces a universal, provider-agnostic standard (similar to USB-C for devices). By implementing MCP, the integration complexity drops to N+M (6 adapters). Developers "write once, run anywhere."

## 2. MCP Architecture

The MCP ecosystem relies on a standardized connection between Host, Client, and Server:
- **Host:** The environment running the LLM (e.g., Claude Desktop, Cursor).
- **Client:** The interface communicating with the MCP Server.
- **Server:** Exposes specific capabilities (e.g., PostgreSQL, GitHub tools).
- **Transport:** Can be local `stdio` (same machine, low latency) or `SSE/HTTP` (remote, production).

### 6 Core Primitives of MCP
1. **Tools:** Callable functions the LLM decides to use (e.g., `query_db()`).
2. **Resources:** Read-only data (URIs) provided as context (e.g., `file://docs/guide.md`).
3. **Prompts:** Reusable interaction templates.
4. **Roots:** Secure workspace access provided by the client.
5. **Sampling:** Server requesting the LLM to perform further reasoning.
6. **Elicitation:** Server asking the user for structured input via the host UI.

*Takeaway: MCP is a protocol for **context exchange**, not just "function calling". Resources and Prompts are highly underutilized but powerful.*

## 3. Building an MCP Server with Python SDK (FastMCP)

The `FastMCP` framework allows for building production-ready servers cleanly using decorators:
- `@mcp.tool()`: Exposes a function for the LLM to call.
- `@mcp.resource()`: Exposes read-only data.
- `@mcp.prompt()`: Defines reusable prompts.

**Crucial Note:** The tool description (docstring) is the most critical element. LLMs rely 100% on the `name` + `description` to decide which tool to call. Vague descriptions lead to hallucinated tool usage or failures.

## 4. Security, Registry, and Versioning

Production-grade MCP servers demand robust security:
- **Transport Security:** `stdio` is secure locally, but remote HTTP/SSE must use OAuth 2.0 and TLS.
- **Input Validation:** Must happen server-side.
- **Permissions:** Apply the principle of least privilege.
- **Audit Logs:** Log every tool call and result.

**Tool Registries** allow agents to discover tools at runtime based on task requirements, utilizing Semantic Versioning (Semver) to manage breaking changes.

## 5. Best Practices & Workflows

### Claude Code + Codex Practices
- **Design for Search/Read First:** Implement read paths (docs/search/fetch) before write paths (mutations). Let the agent read the exact context before acting.
- **Limit Context Bloat:** Return summaries + IDs instead of dumping massive JSON payloads into the context window.
- **Use the MCP Inspector:** Always test schemas, output formats, and error handling locally in the Inspector before integrating with Claude Desktop.

### High ROI Workflows
- **Ticket -> Code -> PR:** GitHub MCP + Docs MCP. Agent reads the issue, fixes the code, and creates a PR.
- **Prod Error -> Root Cause:** Sentry MCP + GitHub MCP. Agent analyzes the stack trace, maps it to a commit, and drafts a fix.
- **Library Upgrade -> Migration:** Docs MCP + Playwright MCP. Agent reads new framework docs, refactors code, and verifies UI flow.
