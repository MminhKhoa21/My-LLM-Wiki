---
type: summary
title: "Day 3 Track 1: Từ Chatbot Đến Agentic Agent (v7 & Material)"
description: "Slide bài giảng chi tiết Ngày 3 về việc nâng cấp từ Chatbot lên Agentic Agent sử dụng ReAct pattern và Tool Calling."
tags: [ai, 20k, day3, track1, agent, react, chatbot, tool-calling]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/3/day03-tu-chatbot-den-agentic-agent-react-v7.pdf", "raw/AI_20K_2A202600974/3/day3-material.pdf"]
---
# Day 3 Track 1: From Chatbot To Agentic Agent

This document summarizes the knowledge from the Day 3 lecture slides (v7) and practical exercises (material). The content focuses on shaping AI systems, Agent architecture, the ReAct pattern, and safe design principles.

## 1. 3 Types of AI Systems  
- **Rule-based Bot**: Based on rigid if/else logic, predictable, low cost, poor flexibility (e.g., IVR switchboard).  
- **LLM Chatbot**: Good text generation capability according to context, focused on 1-turn conversation (reactive). Higher risk of Hallucination.  
- **Agent**: Proactively goal-driven. Loops through `Plan -> Act -> Observe -> Adapt`. Integrates the ability to use Tools, solving complex multi-step problems (Booking, Coding assistant).

## 2. Agentic Fit Framework  
## 2. Agentic Fit Framework  
4 criteria to decide whether to use an Agent:  
1. **Multi-step Reasoning**: Requires reasoning through multiple interdependent steps.  
2. **Tool Interaction**: Interacts with the external environment (API, DB, Web search).  
3. **Dynamic Decision**: The next step depends on the results observed from the previous step.  
4. **Long Horizon**: Needs to maintain long-term goals.

> [!TIP]  
>   
> Always benchmark with a Rule-based system or Chatbot before applying an Agent to avoid overkill. If the problem only requires 1 step and no tools, a Chatbot (or RAG) is sufficient.

## 3. Agent Architecture  
An Agent consists of 4 main blocks:  
- **Perception**: Gateway to receive input from the user and environment (tools).  
- **Reasoning**: Core processing block (LLM Core).  
- **Action**: Makes decisions and calls tools (API) or returns results.  
- **Memory**:   
- **Memory**:   
  - *Short-term*: In the context window, serves the current task.  
  - *Long-term*: In Store/Vector DB, stores long-term information (facts, preferences).

## 4. ReAct Pattern (Reasoning + Acting)  
## 4. ReAct Pattern (Reasoning + Acting)  
ReAct helps the Agent reason step-by-step:  
- **Thought**: Thinking about what to do next.  
- **Action**: Which tool to call and with what parameters.  
- **Observation**: Observing the results from the tool.  
- The biggest strength of ReAct is its **Debuggable** nature: The reasoning steps are clearly displayed, allowing users to intervene and evaluate the process instead of just looking at the final result.

## 5. ReAct vs Function Calling  
## 5. ReAct vs Function Calling  
- **Text-based ReAct (2022)**: LLM generates formatted text. Prone to breaking (parse error).  
- **Native Function Calling (2023)**: LLM returns structured JSON.  
- **Hybrid (2024+)**: Combines Function Calling (for stability) and Reasoning Trace (for easy debugging). This is the optimal architecture for Production environments.

## 6. Agent Loop & Safeguards  
## 6. Agent Loop & Safeguards  
- The Agent loop needs to be controlled by:  
  - **Max Iterations**: Prevents infinite loops.  
  - **Timeout/Error Handling**: Handles Graceful Degradation when tools fail.  
- **Cost & Security**:   
- **Cost & Security**:   
  - Trade-off between autonomy and cost (Agents are more expensive and slower than Chatbots).  
  - Risk of Prompt Injection from tool output. Need to apply 3 Guard layers: Input Guard, Tool Guard, and Output Guard.

## 7. Lab 3 Practice & Activities (Material)  
- Join group activities: Score use cases according to Agentic Fit.  
- Identify factors that increase/decrease the Agent's ability to use tools correctly (quality of tool description, number of tools).  
- **Lab Practice**: Build a Chatbot baseline and upgrade to a ReAct Agent for e-commerce (check_stock, get_discount, calc_shipping).  
- **Evaluation**: Evaluate based on Trace (Token, Latency, Loop Count, Reasoning Quality) instead of just the Final Answer.

---

### Day 3 Review Questions  

1. What is the main difference between an Agent and an LLM Chatbot?  
   - A. Agents only operate based on rigid if/else rules.  
   - B. Agents are proactively goal-oriented and can use tools.  
   - C. Chatbots have more complex multi-step reasoning capabilities than Agents.  
   - D. Agents do not have long-term memory capabilities.  

2. In the Agentic Fit Framework, which criterion indicates that the problem requires interaction with the external environment?  
   - A. Multi-step Reasoning  
   - B. Tool Interaction  
   - C. Dynamic Decision  
   - D. Long Horizon  

3. Which component in the Agent architecture is responsible for deciding to call a tool and processing its output?  
   - A. Perception  
   - B. Reasoning  
   - C. Action  
   - D. Memory  

4. What is the biggest benefit of the ReAct pattern compared to other methods?  
   - A. Reduces operational costs.  
   - B. Increases response speed.  
   - C. Ability to debug and intervene in the reasoning process.  
   - D. Completely eliminates parse errors.
