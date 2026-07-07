---
type: concept
title: "AI Evaluation & Benchmarking"
description: "Tổng hợp các kỹ thuật, framework và mindset để đánh giá chất lượng sản phẩm AI."
tags: [ai, 20k, concept, evaluation, benchmarking]
timestamp: 2026-07-05
sources: []
---
# AI Evaluation & Benchmarking


This page compiles knowledge about AI Evaluation, covering Product, Engineering, and Data perspectives from various days.



*1. Foundational Thinking (Day 14, Day 21, Day 22)*


*Evaluating AI is not just about measuring usage:*

  *Traditional: Measure Conversion, Retention, CTR.*
  *AI Product: Measure **Agent Success Rate**, **Output Quality Distribution**.*
  *Key questions: Does the AI understand the correct intent? Does it perform the task correctly? Does it adhere to policy? Are errors acceptable?*

**Model Eval vs Application Eval**:

*Model Eval vs Application Eval:*

  *Model Eval: Does the model have good foundational capabilities? (MMLU, HumanEval) – Handled by the Research Team.*
  *Application Eval: In the context of this app and this user, is the outcome good? – Handled by the Product Team.*
  *Details: [[day22_track1]]*


*2. Evaluation Frameworks*


*2.1 RAG Evaluation (RAGAS - Day 24)*


*RAGAS is the standard framework for measuring RAG pipelines:*

  *Faithfulness: Measures hallucination. Is the answer grounded in the context?*
  *Context Relevance: Is the context relevant enough?*
  *Answer Relevance: Does the answer address the question correctly?*
  *Context Recall: Does the retriever fetch enough chunks?*
  *Details: [[day24_track3]]*

### 2.2 LLM-as-a-Judge (Day 24)

*2.2 LLM-as-a-Judge (Day 24)*


*Use a strong LLM (e.g., GPT-4) to evaluate the system's output.*

  *4 Biases to avoid: Position bias, Verbosity bias, Self-enhancement bias, Authority bias.*
  *Mitigation: Swap positions, normalize length, blind evaluation.*


*3. AI Eval Lifecycle (Day 21)*

  *Pre-release: Design Scenario Dataset (high coverage), test before deployment.*
  *Rollout: A/B Test, analyze quality distribution.*
  *Production: Learn from production traces, detect failure clusters.*
  *Details: [[day21_track1]]*


*4. Related to Data Observability*


*AI evaluation is closely tied to monitoring data quality:*

- Feature Drift, Label Drift.
  *Feature Drift, Label Drift.*
  *Boundary between Eval and Observability: Eval is typically batch/offline or sampled, Observability is real-time/online.*
  *Details: [[day23_track2]], [[day27_track2]]*
