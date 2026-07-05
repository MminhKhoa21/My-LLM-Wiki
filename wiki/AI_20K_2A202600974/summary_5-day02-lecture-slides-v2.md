---
type: summary
title: "Summary: Day 02 Lecture Slides v2"
description: "A summary of the alternative version of Day 02 lecture slides on defining AI problems and workflows."
tags: [AI Problem, Double Diamond, Workflow, Problem Statement]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/5-day02-lecture-slides-v2.pdf", "raw/AI_20K_2A202600974/2/6-day02-lecture-slides-v2.pdf"]
---

# Summary: Day 02 Lecture Slides v2

## Overview
This document summarizes the Day 02 lecture slides (versions 5 and 6), which mirror the core curriculum of identifying AI problems, structuring Problem Statements, and determining the appropriate level of AI integration. It reinforces the transition from vague ideas to concrete workflows.

## Key Concepts

### Foundation of AI Products
An AI product is built on three pillars:
1. **AI Engineering:** Model deployment, RAG, agents, and evaluation.
2. **Product Thinking:** Identifying the right problem and understanding user value (Inspired).
3. **Design Thinking:** Designing for mental models, feedback, and graceful handling of errors.

### The Double Diamond & HCD
- **Double Diamond:** Focuses on discovering the *real* problem before narrowing down a solution. A great solution to the wrong problem is useless.
- **Human-Centered Design (HCD):** Emphasizes observation, ideation, prototyping, testing, and continuous iteration.

### Problem Formulation
- Identifying the right problem involves looking for tasks that are repetitive, time-consuming, or have a clear AI advantage.
- Avoid anti-patterns like "Solution-first" (building before knowing the workflow) and "No baseline" (failing to measure current operational costs).
- **Stakeholder Interviews:** Ask questions about current workflows, bottlenecks, costs of errors, and success metrics.

### Problem Statement Components
The structured Problem Statement requires:
- **Actor** and **Workflow**
- **Bottleneck** and **Impact**
- **Success Metrics** (Baseline, Target, Measurement)
- **Boundary**, **AI Intervention Point**, and **Risk/HITL**

### Decision Framework: Rule, Workflow, Agent
Choose the simplest level of abstraction:
- **Rule:** Deterministic logic. Best for rigid, high-compliance tasks.
- **Workflow:** AI acts within a defined process (e.g., summarizing, drafting). Human remains in control.
- **Agent:** Autonomous planning and tool usage. Use only when the environment demands high adaptability.

### Workflow Patterns
- Follow Anthropic's guidelines for AI workflows: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, and Evaluator-Optimizer.
- Always prefer simpler, pre-defined workflows over fully autonomous agents unless the latter is absolutely necessary.

### Evaluation and Go/No-Go Decision
- Translate the Problem Statement directly into an Evaluation Plan with defined test cases and thresholds.
- Make a calculated decision: **Go** (clear problem, feasible metric), **Not Yet** (needs data/process standardization), or **No-Go** (AI adds no value or risk is too high).
