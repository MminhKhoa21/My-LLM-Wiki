---
type: summary
title: "Day 3 Track 3: Từ Chatbot Đến Agentic Agent (Hieu)"
description: "Slide bài giảng Ngày 3 do giảng viên Hiếu trình bày về sự tiến hóa từ chatbot sang agent và cơ chế ReAct."
tags: [ai, 20k, day3, track3, agent, react, chatbot]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react_hieu_e403.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---
# Day 3 Track 3: From Chatbot To Agentic Agent  

This document summarizes the Day 3 lecture slides (instructor Hieu's version) combined with practical exercises. The content delves into developing Agents through the ReAct pattern, applying Native Tool Calling, and failure analysis methods.  

## 1. Intelligence Level of AI Systems  

- **Rule-based Bot**: Based on fixed rules (if/else), cheap cost, highly limited.  
- **LLM Chatbot**: Answers flexibly but often only reacts well to single-turn conversations. Risk of hallucinating information.  
- **Agent**: Goal-driven. Uses LLM's capability to decide on calling tools, reads the results, then loops to reach the destination.  

## 2. Agentic Fit Framework  
*## 2. Agentic Fit Framework*

Guide to evaluating when a problem truly needs an Agent using 4 core criteria:  

1. **Multi-step Reasoning**  
   *1. **Multi-step Reasoning***  
2. **Tool Interaction**  
   *2. **Tool Interaction***  
3. **Dynamic Decision**  
   *3. **Dynamic Decision***  
4. **Long Horizon**  
   *4. **Long Horizon***

## 3. Agent Architecture  

- **Perception**: Receives queries from users and feedback from tools.  
- **Reasoning**: Core reasoning processing (LLM), makes decisions for the next step.  
- **Action**: Executes actions using Native Tool Calling.  
- **Memory**:  
  *- **Memory**:*  
  - *Short-term*: Short-term in Session/Context.  
  - *Long-term*: Resides in DB/Vector Store, maintains facts over time.  

## 4. ReAct Pattern & Text-based vs Native  
*## 4. ReAct Pattern & Text-based vs Native*

- **ReAct (Reasoning + Acting)**: Combines reasoning (Thought) with tool-calling actions (Action) and tracking results (Observation). The main advantage is exposing the AI's reasoning to help humans control it.  
- **Text-ReAct (Classic)**: Forces the model to generate formatted text (e.g., `Action: get_weather()`), prone to breaking during parsing (especially with small local models).  
- **Native Tool Calling (Modern)**: LLM generates output using standard JSON schema from API providers (like OpenAI), significantly increasing stability.  

## 5. Failure Modes (5 Types of Agent Errors)  

During coding and debugging, students will frequently encounter 5 errors:  

1. **Parse Error**: The model prints in the wrong format.  
2. **Hallucinated Tool**: Spontaneously calls a non-existent tool.  
3. **Hallucinated Args**: Passes wrong data or invents non-existent parameters.  
4. **Empty Observation**: The tool returns no data but the Agent doesn't know how to branch next.  
5. **Timeout/Loop**: The Agent gets stuck, continuously calling a tool without an end.  

## 6. Evaluation & Telemetry  
*## 6. Evaluation & Telemetry*

Evaluating an Agent's quality cannot just look at the final result. It requires **Eval-by-Trace**:  

- Measure *Tokens* and *Latency*.  
- Count the number of loops (*Loop count*).  
- Log (Telemetry) at each step to pinpoint exactly whether the Agent failed at "Reasoning" or due to "Tool Result".  

## 7. Lab 3 Practice & Material  

- **Lab 3**: Build a Chatbot baseline and upgrade to a ReAct Agent for e-commerce (check_stock, get_discount, calc_shipping).  
- **Failure Analysis**: Students are required to read JSON logs to find errors (parse error, hallucinated tool) and improve Tool Descriptions.  
- Evaluate the Agent's capability through group discussions (Discord activity) on optimal use cases.  
