---
type: summary
title: "Summary of day03-tu-chatbot-den-agentic-agent-react_manh.pdf"
description: "Tổng quan về Agentic AI, framework đánh giá Agentic Fit, kiến trúc Agent và mẫu thiết kế ReAct (Reasoning + Acting)."
tags: [ai, 20k, day03]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_manh.pdf"]
---
# Summary: From Chatbot to Agentic Agent (ReAct Design Pattern)

## 1. Spectrum: From Bot to Agent

AI systems are not confined to a single type but are divided into levels from low to high:

- **Rule-based Bot:** Bots operate based on fixed if/else rules.
- **LLM Chatbot:** Generates smooth responses, understands context but usually only operates in a single turn, lacking the ability to actively search for real-world data.
- **Reactive Agent:** Combines tool use with the ability to repeat step-by-step observations in a loop.
- **Autonomous Agent:** Pursues long-term goals with multiple consecutive decisions and has memory.

## 2. Agentic Fit Framework (When to use an Agent?)

Assess complexity through 4 criteria:

1. **Multi-step Reasoning:** Is multi-step logical reasoning required?
2. **Tool Interaction:** Do you need to call external APIs, DBs, or perform searches?
3. **Dynamic Decision:** Do actions need to change step-by-step based on returned results?
4. **Long Horizon:** Is it necessary to save states across multiple long loops?

*Note: Always benchmark with a Rule-based bot or Chatbot before using an Agent, because Agents are more costly and complex.*

## 3. Architecture of an Agent

Consists of 4 core blocks:

- **Perception:** Receives input from the user and results from tools.
- **Reasoning:** The LLM brain analyzes the state to choose the next step.
- **Action:** Calls tools like Search, APIs, or replies to the user.
- **Memory:** Includes Short-term (within the context window) and Long-term (Vector DB, traditional DB for long-term storage).

## 4. ReAct Design Pattern (Reasoning + Acting)

A pattern that combines step-by-step thinking with tool-calling actions. Instead of rushing to answer, the Agent repeats the following cycle:

- **Thought:** "What am I missing, what do I need to do?"
- **Action:** Which tool to call with what parameters?
- **Observation:** What are the results returned by the tool?

*The cycle repeats until enough data is collected to provide a "Final Answer"*

> **Advantages of ReAct:** Clear traces, easy to debug, easy to detect if the Agent chooses the wrong tool or falls into an infinite loop.

## 5. Agent Loop & Debugging
## 5. Agent Loop & Debugging

- **Safeguard:** Need to set loop limits (Max Iterations), timeouts, token costs, and fallbacks.
- **LangGraph:** For large projects, custom ReAct loops are hard to manage. LangGraph supports drawing graph flows (Nodes, Edges, State) for easier scaling.
- **Hybrid Pattern:** A pragmatic approach is to use a Chatbot for quickly handling simple tasks, switching to an Agent only when multi-step processing is needed.
