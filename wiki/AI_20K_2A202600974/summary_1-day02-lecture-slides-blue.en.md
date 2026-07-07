---
type: summary
title: "Summary: Day 02 Lecture Slides Blue"
description: "A summary of the Day 02 lecture slides on defining AI problems, frameworks, and solution levels."
tags: [AI Problem, Double Diamond, Workflow, Problem Statement]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/1-day02-lecture-slides-blue.pdf"]
---

---

# Summary: Day 02 Lecture Slides Blue  

## Overview  

This document summarizes the lecture slides from Day 02 of the VinUni AI 20K program, instructed by Mai Anh Nguyen (Blue). The core focus is on transforming vague business requirements into clear, actionable AI Problem Statements, evaluating whether AI is genuinely needed, and choosing the right level of solution (Rule, Workflow, or Agent).  

## Key Concepts  

### Problem Discovery and the Double Diamond Model  

- The **Double Diamond Model** emphasizes finding the right problem before finding the right solution. It consists of two diamonds:  

  - **Diamond 1 (Problem):** Discover (diverge to explore) and Define (converge to pinpoint the root problem).  

  - **Diamond 2 (Solution):** Develop (diverge to explore solutions) and Deliver (converge to select and implement).  

- Prioritize **Human-Centered Design (HCD)** by observing users, understanding their pain points (bottlenecks), and avoiding "solution-first" anti-patterns.  

### Defining the Problem Statement  

A clear **Problem Statement** is essential before considering an AI solution. It comprises:  

1. **Actor**: Who is impacted?  

2. **Workflow**: What is the current step-by-step process?  

3. **Bottleneck**: Where is the exact delay, error, or repetition?  

4. **Impact**: What is the quantifiable loss (time, cost)?  

5. **Success Metric**: How will improvement be measured?  

6. **Boundary**: What are the strict limitations (e.g., AI cannot auto-send emails)?  

7. **AI Intervention Point**: Exactly where in the workflow does AI step in?  

8. **Level of Solution**: Rule, Workflow, or Agent?  

9. **Risk & Human-in-the-Loop (HITL)**: How to handle AI errors and where human approval is required.  

### AI Solution Levels: Rule vs. Workflow vs. Agent  

Always opt for the simplest solution that works:  

- **Level 1 - Rule**: Use when logic is deterministic (If/Else) and exactness is required. No AI needed.  

- **Level 2 - Workflow (LLM Feature)**: Use when steps are defined, but some steps need AI for language processing, summarization, or classification. Retains full human control.  

- **Level 3 - Agent**: Use when the environment is highly dynamic, requiring autonomous planning and multi-tool coordination. Higher risk and operational cost.  

### Workflow Patterns  

Based on Anthropic's guidelines:  

- **Basic Patterns**: Prompt Chaining, Routing, Parallelization.  

- **Advanced Patterns**: Orchestrator-Workers, Evaluator-Optimizer, Autonomous Agents.  

### Decision Making  

The final step in problem framing is making a conscious decision:  

- **Go**: Problem is clear, metrics are measurable, and AI provides a distinct advantage.  

- **Not Yet**: Needs more data, process standardization, or clearer metrics.  

- **No-Go**: Too risky, or non-AI solutions are more effective.  

## Workflow Integration  

- **UX & HITL**: Ensure proper UI design to manage AI shortcomings (e.g., asking for clarification, providing citations, requiring manual approval).  

- **Evaluation**: The Problem Statement serves as the blueprint for the Evaluation Plan (baseline, test cases, and success thresholds).  

--- 

