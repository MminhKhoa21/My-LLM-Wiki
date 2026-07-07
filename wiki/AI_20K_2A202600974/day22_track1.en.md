---
type: summary
title: "Day 22 – Track 1: AI Evals & Automated Evaluators"
description: "Hướng dẫn chi tiết về tự động hóa đánh giá AI (Automated Evals) và tham chiếu đánh giá AI từ góc nhìn Product Management."
tags: [ai, 20k, day22, track1, evaluation, llm-as-judge, code-evals]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/1-d22-slide.pdf", "raw/AI_20K_2A202600974/22/ai-evals-reference-guide-vi.pdf"]
---

---

> **Roadmap:** [[track1_ba|Track 1: AI Product / BA]]

# Day 22 – Track 1: AI Evals & Automated Evaluators



*Evaluating AI applications goes beyond measuring usage or funnel completion; it is about ensuring quality, safety, and reasoning capability of the system at scale.*

---


## 1. Foundational Mindset: Why Automated Evals?



- **The Scale Problem:** Manual review cannot scale. When production traces reach 100k+, manual review slows releases and misses silent errors (false confidence).
- **Application Eval vs Model Eval:** Model Eval (performed by providers via MMLU, HumanEval) measures foundational capability. Application Eval measures specifically for the product context (e.g., Does support triage match the business's intent and policy?).
- **AI Flywheel:** A continuous improvement process based on traces: `Traces -> Trace analysis -> Reference dataset -> Offline evals -> Release gates -> Online monitoring`.

---


## 2. Evaluation Layers: Codebase, Human & LLM



*A robust eval suite must coordinate three evaluation sources, arranged in a priority decision tree:*

### Layer 1: Code-based Evals (Always On, Priority #1)


  1. Input (output string, tool calls).
  2. Logic (condition, pattern match).

- **When to use:** When the question can be verified by rule, DB, schema, API, regex, computation.
- **Advantages:** Fast, cheap, deterministic, easy to integrate into CI/CD (critical path).
- **Example checks:** Valid JSON Schema (Pydantic), Assert enum category (`Technical`, `Billing`), Regex no token/UUID leakage, Tool usage has all required fields.
- **Structure of a Code-eval:** 
  1. Input (output string, tool calls).
  2. Logic (condition, pattern match).
  3. Result & Reason (Return clear failure with info: "Missing subject line").

### Layer 2: LLM-as-Judge (Requires Calibration)



- **When to use:** When criteria depend on context, language nuance (e.g., is the explanation reasonable, does the agent show empathy to the customer, intent classification).
- **Calibration is core:** LLM judge risks leniency or bias. Requires calibration:
  1. Human expert labels on 50-100 cases (golden labels).
  2. Run LLM Judge and compare results (measure Precision/Recall on failure modes, not just raw agreement).
  3. Revise judge prompt based on error patterns and repeat.
- When the LLM judge "hits a ceiling" (difficult domain, insufficient model capability), fallback to other methods.

### Layer 3: Human Review (Fallback & Defining "Good")



- **When to use:** During prototype phase with unclear rubric, high-stakes domains (medical, financial), complex policy nuance, or for calibration labeling.
- **Effective review method:** Not purely random; must use *targeted sampling* (e.g., outputs where LLM judge is most/least confident, disagreement cases).

---


## 3. Dataset Architecture and Metrics


### Reference Dataset
*Reference Dataset*


*A good Eval Case is not just a set of prompts; it must include:*
- **Input:** User question/context.
- **Expected Output:** Clear golden label/rubric.
- **Assertions:** Mandatory codebase rules.
- **Failure modes & Severity:** Analysis of risk level if failure occurs (P0, P1, etc.).

### Metrics
*Metrics*


- **Agent Success Rate:** North Star Metric. A composite metric aggregating: Task correctness, Schema pass rate, Escalation recall, Human/LLM judge score.
- Metrics must be segmented by *Intent, Persona, Prompt version, Model version* to detect hidden regressions.

---

## 4. Eval Lifecycle (Process for Shipping AI to Production)



1. **Vibe Check (Prototype):** 10-30 diverse cases. Define "good", find failure modes.
2. **Offline Evals (Build/Iterate):** 100-1000 cases run automatically before release. Acts as a Release Gate to catch errors.
3. **Online Monitoring (Production):** Monitor drift, P95 latency, cost, user feedback. Sample suspicious cases (low-confidence) to feed into the next iteration dataset.

---

## Links


- [[day21_track1]] – AI Evals (Day 21)
- [[day22_overview]]

- [[day21_track1]] – AI Evals (Day 21)
- [[day24_track3]] – RAGAS & Guardrails (specific RAG evaluation)
- [[day22_overview]]

--- 

