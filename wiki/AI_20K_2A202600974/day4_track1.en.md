---
type: summary
title: "Day 4 Track 1 - Prompt Engineering, Tool Calling & LangGraph"
description: "Tổng hợp kiến thức về Prompt Engineering nâng cao, System Prompts, Tool Calling và ứng dụng LangGraph cho Agent."
tags: [ai, 20k, day4, track1, prompt-engineering, tool-calling, langgraph]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/4/1-day04-prompt-engineering-tool-calling-v2.pdf", "raw/AI_20K_2A202600974/4/1-day04-prompt-engineering-tool-calling.pdf", "raw/AI_20K_2A202600974/4/day04-prompt-engineering-tool-calling.pdf"]
---

# Day 4 Track 1: Prompt Engineering, Tool Calling & LangGraph


## 1. Prompt Engineering Fundamentals

## 2. Advanced Prompting Techniques
- **Zero-shot, Few-shot, CoT**:

## 3. System Prompt Engineering
  - Persona & Tone.

## 4. Function/Tool Calling
  1. Trigger (User input).
- **Tool Schema**:

## 5. Orchestration with LangGraph
- **Core Concepts**:

---

### Day 4 Review Questions  

1. According to the RTCF model, which component is considered the top priority in a good prompt?  
   - A. Role  
   - B. Task  
   - C. Context  
   - D. Format  

2. Which technique is recommended to force the LLM to output a stable format, typically using 2-5 examples focusing on edge-cases?  
   - A. Zero‑shot  
     *A. Zero‑shot*  
   - B. Chain‑of‑Thought (CoT)  
     *B. Chain‑of‑Thought (CoT)*  
   - C. Few‑shot  
     *C. Few‑shot*  
   - D. Dynamic Prompting  
     *D. Dynamic Prompting*  

3. In the Tool Calling architecture, what data does the LLM return in the second step (after receiving user input) so the app can execute the tool?  
   - A. Raw text response  
     *A. Raw text response*  
   - B. JSON `tool_calls`  
     *B. JSON `tool_calls`*  
   - C. An SQL command  
   - D. A dictionary containing `tool_outputs`  

4. When encountering an error during tool execution, what is the recommended error handling strategy?  
   - A. Stop the entire agent and notify the user of the error  
   - B. Send the raw error message back to the LLM so it can fix the error itself  
   - C. Ignore the error and continue executing another tool  
   - D. Recall the tool with default parameters  

5. In LangGraph, which mechanism is used to store and update `messages` throughout the graph?  
   - A. Global variable  
   - B. Append‑only Reducer  
     *B. Append‑only Reducer*  
   - C. Conditional Edge  
     *C. Conditional Edge*  
   - D. Router Node  
     *D. Router Node*
