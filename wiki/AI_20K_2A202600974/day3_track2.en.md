---
type: summary
title: "Day 3 Track 2: Từ Chatbot Đến Agentic Agent (Manh)"
description: "Slide bài giảng Ngày 3 do giảng viên Phạm Mạnh trình bày về quá trình nâng cấp hệ thống AI từ Rule-based đến Agentic Agent."
tags: [ai, 20k, day3, track2, agent, react, chatbot]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_manh_v2.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---
# Day 3 Track 2: From Chatbot To Agentic Agent  

This document summarizes the Day 3 lecture based on instructor Pham Manh's slides and classroom activities. The lecture guides how to determine when to use an Agent and the basic architecture to build an effective Agent system.  

## 1. 3 Types of AI Systems  

AI systems are classified into 3 levels:  

- **Rule-based Bot**: Operates based on fixed rules (If/else), does not call LLM, low flexibility.  

- **LLM Chatbot**: Answers intelligently based on context but is reactive in nature, lacking a long-term reasoning loop.  

- **Agent**: Operates in a loop using tools and observing step-by-step. Can solve long-horizon goals through multiple consecutive decisions.  

## 2. When is an Agent Needed? (Agentic Fit)  

Use the Agentic Fit Framework to evaluate with 4 criteria:  

1. **Multi-step Reasoning**  

2. **Tool Interaction**  

3. **Dynamic Decision**  

4. **Long Horizon**  

> [!WARNING]  
> Do not use an Agent if the problem is a simple 1-step task, requires absolute determinism, has no tools to interact with, or requires extremely short response latency.  

## 3. Agent Architecture  

- **Perception**: Input from user and tool results.  

- **Reasoning**: The core of the model (LLM Core) for making decisions.  

- **Action**: Executes the task (API, Exploration tool).  

- **Memory**: Short-term (Context window) and long-term (Store/DB). Memory is only effective with a clear read/write strategy.  

## 4. ReAct Pattern (Reasoning + Acting)  
## *4. ReAct Pattern (Reasoning + Acting)*

- Loop: `Thought` (Think next step) -> `Action` (Call tool) -> `Observation` (Result returned).  

- **Benefits**: Increases debugging capability thanks to a transparent action trace.  

- **LangGraph Integration**: The lecture points from the traditional ReAct loop (manual code) towards developing a graph approach using LangGraph in later lessons to better manage state and routing.  

## 5. Agent Loop & Troubleshooting  
## *5. Agent Loop & Troubleshooting*

- **Code Anatomy**: Set up strict system prompts, clearly register tools (Tool Registry) with detailed descriptions, and configure Max Iterations.  

- **Debug Checklist**:  
  *- **Debug Checklist**:*

  - Check if Thought aligns with the goal.  

  - Check if the Agent selected the wrong tool or passed wrong parameters.  

  - Fix by improving Tool description or configuring fallback retry.  

## 6. Group Exercises & Lab 3  

- Score a chosen use case using Agentic Fit (post to Discord).  

- Practice analyzing factors that increase/decrease the Agent's tool selection capability (e.g., clear tool description).  

- Upgrade the baseline Chatbot to a ReAct agent with at least 1-2 tools for the use case.  

- Run 5 comparison test cases and draw a flowchart illustrating the Agent's advantages in complex contexts.  
