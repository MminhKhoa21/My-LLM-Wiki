---
type: summary
title: "Day 16 Track 3: Advanced Agent Architectures"
description: "Kiến trúc Agent nâng cao: Reflexion, LATS, Voyager và cách triển khai an toàn"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/phase2-day01-advanced-agent-architectures-extended-fuller.pdf"]
---
> **Roadmap:** [[track3_ai_app]]

# Advanced Agent Architectures

Research the reasons why Single Agent (like ReAct) fails in complex problems and how to overcome them with advanced patterns.

## 1. Limitations of Single Agent (ReAct)

The **ReAct (Reasoning + Acting)** model is very powerful but lacks self-evaluation capability. When encountering errors, ReAct easily falls into:
- **Error propagation**: An error in the first step leads to the entire chain being wrong.
- **Infinite loop**: The tool returns noise causing the agent to repeat endlessly.
- **No backtracking**: Goes down the wrong path but doesn't know how to return.

## 2. Reflexion: Teach Agent Self-Reflection

**Reflexion** overcomes ReAct's weaknesses by incorporating **Self-evaluation** into the reasoning loop:
- **4-step Architecture**:
  1. **Actor**: Generates actions.
  2. **Evaluator**: Scores the result (Right/Wrong).
  3. **Reflector**: Extracts lessons from mistakes (Reflection Memory).
  4. **Retry**: Tries again with a new strategy.
- **Reflection Memory**: A concise form of *episodic memory* that includes `failure_reason`, `lesson`, and `next_strategy`. The agent learns from previous run mistakes to avoid repeating errors, significantly improving accuracy (e.g., increasing 20-30% on HotpotQA compared to ReAct).
- **Evaluator Note**: Evaluation should be based on structured output (Pydantic/JSON) to ensure specific reasons (reason) that help the Reflector analyze easily.

## 3. LATS and Voyager

- **LATS (Language Agent Tree Search)**: Combines MCTS (Monte Carlo Tree Search) and LLM to explore multiple solution branches and support `undo` backtracking. Extremely accurate but compute-intensive (3-5 times more), suitable for high-stakes tasks (e.g., code generation).
- **Voyager**: An agent with compound learning ability across multiple episodes, automatically recording verified skills into a library for reuse in other tasks.

## 4. Safe Deployment for Production

When Multi-agent is not yet needed, optimize Single-agent with these techniques:
- **Separate Plan - Act - Verify**: Instead of "think and act immediately", the agent creates a plan of subgoals, calls tools, then verifies observations for better stability.
- **Safety Checklist**:
  1. Configure `max_attempts` to prevent infinite loops.
  2. Use structured outputs for tools and evaluators.
  3. Build traces for early debugging (Observability).
  4. Risk tiering: Read-only vs Write (require human review/approval gate for sensitive operations).
- Do not rush to move to a **Multi-agent** system unless the problem is open-ended, truly needs a delegation workflow (Planner / Worker / Judge), or handles multiple domain tools in parallel.

---

### Day 16 Review Questions

1. What main weakness of Single Agent (ReAct) does Reflexion address?
   - A. Cannot use multiple tools simultaneously.
   - B. Lacks the ability to self-evaluate and backtrack when encountering errors.
   - C. Computation cost is too high for each step.
   - D. Does not support structured output.

2. In the Reflexion architecture, which component is responsible for drawing lessons from mistakes and saving them to memory?
   - A. Actor
   - B. Evaluator
   - C. Reflector
   - D. Retry

3. What is the prominent feature of LATS (Language Agent Tree Search) compared to Reflexion?
   - A. Uses Reflection Memory to store errors.
   - B. Combines MCTS to try multiple solution branches and has the ability to undo.
   - C. Automatically records new skills into the library.
   - D. Only suitable for data reading tasks.

4. Which safety measure is recommended when deploying Single-agent in production?
   - A. Always use Multi-agent from the beginning.
   - B. No need to configure max_attempts because the agent knows when to stop.
   - C. Risk tiering, setting up human approval gates for sensitive operations.
   - D. Only use unstructured output for flexibility.
