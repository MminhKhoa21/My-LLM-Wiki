---
type: overview
title: "Day 3 Overview - Từ Chatbot đến Agentic Agent"
description: "Kiến trúc của Agent, ReAct Pattern, Function Calling và quy trình xây dựng Agent thực tế."
tags: [ai, 20k, day3]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react-v7.pdf"]
---

# Day 3: From Chatbot to Agentic Agent  

## 1. 3 Types of AI Systems  

- **Rule-based Bot**: Static logic (if/else), no LLM calls, easy to control but lacks flexibility.  

- **LLM Chatbot**: Uses LLM to generate fluent responses, but typically handles only single-turn tasks, prone to Hallucination.  

- **Agent**: LLM operates in a `Plan -> Act -> Observe -> Adapt` loop. Ability to use Tools to fetch real data and make flexible multi-step decisions.  

## 2. Agentic Fit Framework  
*## 2. Agentic Fit Framework*  

The framework consists of 4 criteria to evaluate when to use an Agent:  

1. **Multi-step Reasoning**: The problem is divided into multiple interdependent steps.  

2. **Tool Interaction**: The system needs to use APIs, DBs, Web Search, etc.  

3. **Dynamic Decision**: Each subsequent step depends on the result of the previous step.  

4. **Long Horizon**: Maintains the objective across multiple iterations.  

## 3. Agent Architecture (Perception, Reasoning, Action, Memory)  

- **Perception**: The agent receives input (from users, tools, feedback).  

- **Reasoning**: The LLM Core analyzes and selects the next action.  

- **Action**: Calls tools and outputs the response.  

- **Memory**: Consists of *Short-term* (Context window, containing recent conversation history) and *Long-term* (Databases, Vector Stores, containing knowledge and user profiles).  

## 4. ReAct Pattern (Reasoning + Acting)  
*## 4. ReAct Pattern (Reasoning + Acting)*  

The ReAct loop helps the LLM reason step-by-step:  

- **Thought**: Thinking about what to do next.  

- **Action**: Deciding which tool to call and with what parameters.  

- **Observation**: Observing the results returned by the tool.  

- The loop stops when enough information is gathered to provide the Final Answer. Its strength is making debugging easier because the agent's reasoning process is exposed.  

## 5. ReAct vs Native Function Calling  
*## 5. ReAct vs Native Function Calling*  

- **ReAct text-based**: Requires the LLM to return formatted text (usually parsed by regex), which is fragile.  

- **Native Function Calling**: The LLM outputs structured JSON to call functions, which is more stable. Currently, in production environments, a *Hybrid* approach (Function Calling + Reasoning trace) should be used.  

## 6. Agent Loop & Debugging  
*## 6. Agent Loop & Debugging*  

- The Agent loop needs safety mechanisms (Guardrails) such as: Limiting the number of loops (Max Iterations), Timeouts, Error Handling (Graceful Degradation), and Fallbacks when tools fail.  

- Evaluation for Agents is more complex than for Chatbots: It not only evaluates the final answer but also evaluates the reasoning quality, tool selection, parameters, and stopping conditions.  
