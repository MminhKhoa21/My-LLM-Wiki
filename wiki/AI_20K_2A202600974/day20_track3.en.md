---
type: summary
title: "Day 20 Track 3: Multi-Agent Systems"
description: "Exploration of advanced multi-agent workflows, including Supervisor, Debate, and Parallel patterns, using frameworks like LangGraph."
tags: [day20, track3, multi-agent, langgraph, supervisor, debate, parallel-execution]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/20/day05-multi-agent-systems-student.pdf"]
---
# Day 20 Track 3: Multi-Agent Systems


## 1. Overview


This module transitions from single-agent setups to Multi-Agent Systems. While single agents handle simple tasks well, complex scenarios require teams of specialized agents with dedicated roles and shared states. However, adding agents introduces overhead and coordination challenges.


## 2. When to Use Multiple Agents?


You should only scale to multi-agent architectures if a single agent cannot achieve >80% accuracy. The three primary drivers for multi-agent systems are:


- **Specialization:** Each agent masters one specific domain (e.g., Researcher, Analyst, Writer).

- **Parallelization:** Running subtasks concurrently to reduce latency.

- **Cross-checking:** Using consensus and critique to reduce hallucinations.

## 3. Anthropic's 5 Agentic Workflow Patterns


Start with the simplest pattern and escalate only when measurably needed.


1. **Prompt Chaining:** Sequential operations where one output feeds into the next.

2. **Routing:** Classifying an input and routing it to the most capable specialized handler (reduces costs by sending easy queries to small models and hard queries to large models).

3. **Parallel:** Splitting a task into sections for parallel workers, or using voting across multiple models on the same task.

4. **Orchestrator-Workers (Supervisor):** A supervisor LLM delegates tasks to worker agents and aggregates their outputs.

5. **Evaluator-Optimizer:** An iterative generate-and-critique loop.

## 4. The Supervisor Pattern (Orchestration)


- Uses a **Hub-Spoke Architecture** implemented typically via LangGraph.

- The Supervisor acts as a router, breaking down a task and deciding which worker to call and in what order.

- State is managed through a `TypedDict` tracking `messages`, `next_worker`, `worker_results`, and `final_answer`.

- **Failure Modes:** Infinite routing loops or incorrect worker selection (mitigated by setting max iterations).

## 5. Debate Agents (Adversarial Collaboration)


- Multiple agents generate independent answers and then critique each other's work.

- A "Judge" agent synthesizes the final answer.

- Using heterogeneous models (e.g., GPT-4o, Claude, Gemini) avoids "collective delusion" where identically trained models agree on false information.

- **Benefits/Trade-offs:** Reduces hallucinations by 15-25% but at the cost of 2-3x higher latency and compute. Best reserved for high-stakes, ambiguous tasks.

## 6. Parallel Execution and Shared State


- Uses asynchronous Map-Reduce execution (e.g., `asyncio.gather` in Python or LangGraph's Send API).

- Agents coordinate either through a central blackboard (Shared State) or through Message Passing queues.

- **Failure Handling:** Timeouts, retries, circuit breakers, and dead-letter queues are necessary for production reliability.

## 7. Multi-Agent Frameworks


- **LangGraph:** High flexibility, state machine driven, best for full-control production environments.

- **CrewAI:** Role-based and easy to set up, excellent for rapid prototyping.

- **AutoGen:** Group chat and conversational collaboration, strong at code execution.

## 8. Lab 20

*## 8. Lab 20*

The lab focuses on building a 3-agent research system (Researcher, Analyst, Writer) using LangGraph. Students benchmark the single-agent baseline against the multi-agent system measuring accuracy, latency, and cost.

