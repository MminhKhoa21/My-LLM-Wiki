---
type: overview
title: "Day 14: AI Evaluation & Benchmarking"
description: "Đo lường chất lượng AI một cách khoa học bằng các framework, golden datasets và các phương pháp LLM-as-Judge."
tags: [ai, 20k, day14, evaluation, benchmarking]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/14/day14-ai-evaluation-benchmarking_E403.pdf"]
---
# Day 14: AI Evaluation & Benchmarking



*## Main Content*


*Evaluation is a core engineering discipline that helps development teams know how good their Agent is, avoiding gut feelings or vibe checks. It acts as a set of "Unit Tests" for non-deterministic AI.*


*## Evaluation Strategy*


*AI evaluation needs to decompose layers to pinpoint where errors occur:*
- ***Retrieval Evaluation***: *Checks the system's ability to find documents, using metrics like **Hit Rate** (whether it was found), **MRR** (rank of the first correct document), **NDCG**. Poor retrieval caps the ceiling of Generation.*
- ***Generation Evaluation (RAGAS)***: *Uses metrics from the RAGAS framework such as Context Recall, Context Precision, Faithfulness (no hallucination beyond context), and Answer Relevancy.*


*## Building Golden Datasets*


*- Do not use generic tests; use data from your project’s own domain.*
*- Synthetic Data Generation (SDG) can quickly scale up your test set, but be careful to remove overly simple questions and prioritize edge cases.*
*- **Goodhart’s Law & Contamination**: Public benchmark scores are easily inflated due to model memorization. A separate held-out test set is needed to prevent cheating.*


*## LLM-as-Judge & Statistics*


*- Instead of using humans to score thousands of questions at high cost, use a strong LLM as a Judge.*
*- To reduce biases (position bias, verbosity bias) of LLM-as-Judge, you can combine **Multi-Judge Consensus** (multiple judges, majority voting).*
*- Always compare **Pairwise** (evaluate on the same test set) rather than pointwise to clearly see differences between two versions, and apply statistical methods (Confidence Intervals) to rule out luck-based results.*
*- **Regression Release Gate**: Integrate evaluation into CI/CD to block deployment if response quality degrades.*
