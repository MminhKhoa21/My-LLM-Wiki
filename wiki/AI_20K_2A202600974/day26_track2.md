---
type: summary
title: "Day 26 – Track 2: MCP/A2A Infrastructure & Agentic Routing"
description: "Comprehensive guide on building scalable multi-agent systems using Model Context Protocol (MCP) and Agent-to-Agent (A2A) protocols."
tags: [mcp, a2a, multi-agent, routing, orchestration, observability, infrastructure]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/26/day26-mcp-a2a-infrastructure-agentic-routing-no-k8s.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]

# Day 26 – Track 2: MCP/A2A Infrastructure & Agentic Routing

This document summarizes the theory and practical architecture for building robust multi-agent systems. It covers the Model Context Protocol (MCP) as an infrastructure layer, the Agent-to-Agent (A2A) protocol for communication, routing strategies, state management, and essential observability practices.

---

## 1. MCP: Infrastructure Layer for LLM Tools

**Model Context Protocol (MCP)** acts as the universal open protocol for LLMs to interface with tools, resources, and templates. It standardizes tool integrations so that developers only build servers once, enabling them to work across Claude, GPT, ADK, LangChain, etc.

- **Primitives:** 
  - `Tools Server` (execute functions)
  - `Resources Server` (expose data)
  - `Prompts Server` (templates)
- **Transports:** `stdio` (local subprocess), `HTTP+SSE` (remote), `WebSocket` (streaming).
- **Implementation:** Defined using Python SDK decorators (e.g., `@app.tool()`). Clear docstrings are critical because LLMs read them to decide tool usage.
- **Hosting & Registry:** Deployed locally or via remote APIs (FastAPI + uvicorn). Systems use an **Agent Registry pattern** to discover tools and capabilities (`/.well-known/agent-card.json`).

## 2. A2A Protocol: Microservices for AI Agents

The **Agent-to-Agent (A2A)** protocol treats individual AI agents as microservices. It standardizes how a primary orchestrator agent dispatches tasks and messages to specialist agents.

- **Communication:** Facilitated via Agent Cards, Tasks, and Messages.
- **Task Lifecycle:** `Submitted` -> `Working` -> `Input Required` -> `Completed` (or Failed/Canceled). Crucially, tasks can pause to ask the caller for more context rather than failing outright.
- **Orchestrator Pattern:** An orchestrator agent decomposes a user request, routes sub-tasks to specialists (e.g., Search Agent, Database Agent), and synthesizes the final response.

## 3. Agentic Routing Strategies

Routing ensures tasks are dispatched to the right specialist agent.
- **Keyword-based:** Fast but brittle (best for ≤ 5 agents).
- **Embedding-based (Semantic Routing):** Embeds requests and calculates cosine similarity with agent capabilities (robust for 5-50 agents).
- **LLM-based:** Highly flexible but slow and expensive.
- **Fallback chains:** Designing systems so tasks move from primary -> fallback -> human escalation to prevent dead-ends.

## 4. State Management

- **Stateless (Recommended initially):** Easily scales horizontally. Context is externalized to databases like Redis (short-lived context) or PostgreSQL (persistent history).
- **Stateful:** Used for long-running conversations requiring sticky sessions, but harder to scale.

## 5. Security & Governance

A "Defense in Depth" principle is required for production agentic systems:
- **Rate Limiting:** Per-agent and per-user limits.
- **Sandbox Execution:** Running agent code in isolated environments.
- **Human-in-the-Loop (HITL):** Requiring human approval for high-stakes actions (e.g., DB writes, sending emails, spending budgets).
- **Minimal Capability:** Agents are only granted the specific tools they need (Capability Matrix).
- **Audit Logging:** Every invocation must log timestamps, agent IDs, and I/O payload.

## 6. Observability for Multi-Agent Systems

- **Distributed Tracing:** Implementing W3C Trace Context across A2A calls. A single Trace ID maps the orchestrator span to all sub-agent and tool call spans.
- **Metrics:** Tracking task completion rates, average durations, tool call counts, and token costs per agent.

## 7. Lab: Multi-Agent Research System

The lab focuses on implementing a 4-agent system (1 Orchestrator + 3 Specialists) utilizing A2A, MCP, and strict governance audits without relying on Kubernetes (using a local Conda/ADK setup).
