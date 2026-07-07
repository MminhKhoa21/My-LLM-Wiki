---
type: summary
title: "Day 21 – Track 1: AI Evaluation (Vai trò PM)"
description: "Vai trò của AI Product Manager trong việc thiết kế và vận hành hệ thống đánh giá AI, từ giai đoạn phát triển đến sản xuất."
tags: [ai, 20k, day21, track1, evaluation, pm]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/d21-slide-v0.pdf", "raw/AI_20K_2A202600974/21/day21-lab-instruction.pdf"]
---
## Day 21 – Track 1: AI Evaluation – The Role of PM


**Instructor**: Mai Anh Nguyen (Blue) – Generalist Product Builder  
**Course**: AICB Phase 2 · Day 21 · Track 1


---

## 1. Context: The Shift in the PM’s Role in AI Products


For traditional products, the user flow is deterministic; we care about Usage Flows and Conversion Rate. For AI products, the outcome is probabilistic, with a wide distribution of quality (Poor – Good – Great). The PM’s role shifts from defining flows to managing **Agent Success Rate** and **Quality Distributions**.


AI Eval is divided into two layers:


- **Model Evals**: Evaluate the foundational capabilities of the model (Reasoning, Coding, Math, Safety). Handled by the provider (OpenAI, Anthropic, Google).
- **Application Evals**: Evaluate real-world quality in the user’s context. Focus on accuracy, usefulness, safety, latency, cost. This is the Product Team’s responsibility.

**Three complementary grading methods:**


1. **Code-based grader**: Fast, cheap, objective but rigid (checks exact match, regex, formatting).
2. **Model-based grader (LLM as Judge)**: Flexible, captures nuance but expensive, potentially unstable.
3. **Human grader**: Gold standard, costly, used to calibrate other graders.

---

## 2. AI Evals Lifecycle


The evaluation process is not a one-time task before release but a continuous loop:


### Stage 01: Vibe Check (Prototype phase)

*### Stage 01: Vibe Check (Prototype phase)*

- **Goal**: Manual review to understand behavior before finalizing the PRD.
- **Execution**: Generate 10–30 test inputs (including happy path and edge cases), run through the prototype, label outputs (Pass/Fail).
- **Result**: Good outputs become **Golden Outputs** (used for few-shot and evals). Failed cases help shape the PRD. Vibe check must be done *before* writing the PRD.

### Stage 02: Offline Evals (Build phase)

*### Stage 02: Offline Evals (Build phase)*

- **Goal**: Automated evaluation on a reference dataset before release. Detect regression.
- **Process**: Trigger a change (new prompt/model) → Run the test set → Compare with baseline → Decide to Deploy or Fix.
- **Note**: Set a **Quality Gate** (minimum quality threshold); if not passed, do not ship.

### Stage 03: Online Monitoring (Production phase)

*### Stage 03: Online Monitoring (Production phase)*

- **Goal**: Monitor after launch, detect drift, and uncover unknown unknowns.
- **Questions**: Does the AI maintain the Agent Success Rate? Are there new user behaviors (unusual language, new data formats, intents outside the PRD)? Is there divergence between offline and online metrics?

---

## 3. AI-native PRDs

*## 3. AI-native PRDs*

PRDs for AI products differ from traditional PRDs. They need to include:


- **Evaluation Rubric**: Clear Pass/Fail criteria.
- **Golden Outputs**: Concrete examples (Input → Expected Output).
- **Prompt Logic & Tools**: API handling, system instructions.
- **Dataset Strategy**: Plan for collecting evaluation data.
- **Edge Case Handling**: Define what “fail gracefully” means when the model encounters errors.
- **Unit of AI Work**: Narrow the scope of tasks so they can be evaluated (avoid broad concepts like “AI helpfulness”; use concrete ones like “Classify a support ticket into the correct queue”).

---

## 4. Designing Coverage & Scenario Datasets


Instead of asking the LLM to generate 50 random prompts (which often turn out homogeneous), the PM needs to design a **User Input Grid** to ensure real-world coverage.


- **Dimensions**: WHO (Persona), WHAT (User intent), HOW (Context completeness, ambiguity, complexity), CONTEXT (Language, data freshness), RISK (Consequences if it fails).
- **Candidate Scenario Bank**: Combinations of dimensions. Includes **Representative scenarios** (common cases), **Challenge scenarios** (difficult, ambiguous, zero‑hit), and **Critical regression candidates** (cases that must never fail again).

---

## 5. Trace Analysis

*## 5. Trace Analysis*

A trace is the entire process of the agent’s operation and reasoning (a transcript is just the final chat message the user sees).


- **Why read the trace?** Sometimes the final answer (transcript) looks correct, but the process (trace) is wrong.
- **Standardizing Trace Codes**: The PM reads traces, groups errors into standardized trace codes (e.g., `wrong_intent`, `missing_lookup`, `premature_commit`) instead of writing free‑form notes. This enables measurement, classification, and prioritization of fixes.

---

## 6. Lab 21: Designing Test Inputs for AI Evals


This lab exercise trains the PM’s skill in designing test input sets.


- **Individual Phase**: Choose one Unit of AI Work, define a Quality Question, design a User Input Grid (minimum 3 dimensions), select 10 promising combinations. Use AI to generate >20 natural‑language inputs, then manually filter (remove generic/wrong‑intent items) to create a Scenario Dataset v0.
- **Group Phase**: Merge dimensions, deduplicate inputs, check the coverage matrix, and finalize a **Scenario Dataset v1** (>30 rows) that is sufficiently diverse (representative, challenge, high‑risk). Write a handoff note for later agent evaluation.

---

## Links


- [[day21_track2]] – CI/CD AI Systems
- [[day21_track3]] – Fine-tuning LLMs
- [[day21_overview]]
