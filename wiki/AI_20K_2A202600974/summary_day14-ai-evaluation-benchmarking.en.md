---
type: summary
title: "Summary of day14-ai-evaluation-benchmarking"
description: "Tổng hợp kiến thức Ngày 14 về đo lường chất lượng AI một cách khoa học, các phương pháp đánh giá, metrics, RAGAS framework, LLM-as-Judge và phân tích lỗi."
tags: [ai, 20k, day14]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/14/day14-ai-evaluation-benchmarking.pdf"]
---

# Measuring AI Quality Scientifically (AI Evaluation & Benchmarking)

The lesson emphasizes that AI Evaluation is a scientific engineering discipline, not based on feeling ("feeling the agent answers well"). If you can't measure it = you can't improve it.

## 1. 4 Dimensions of AI Output Quality

An AI Agent needs to be evaluated based on 4 main aspects, because a single metric is not enough:
- **Correctness:** Does it answer truthfully? Does it hallucinate or cite the wrong sources?
- **Relevance:** Does it answer the core of the user's question or go off-topic?
- **Completeness:** Does it have enough necessary details? Does it miss any important information?
- **Coherence:** Is the answer easy to read, well-structured, and does it use appropriate language?

## 2. 3 Types of Evaluation (Evaluation Types)

1. **Offline (Batch test on golden dataset):** Run automatically whenever there is a code/prompt/model change to prevent regression. (Using RAGAS, scripts).
2. **Online (Monitor production traffic):** Continuously monitor real traffic to detect quality degradation immediately. (Using Langfuse, LangSmith).
3. **Human Eval (Expert review):** Evaluated by humans on periodic samples or high-stakes tasks.

> [!TIP]
> **Cost rule:** The cost for evaluation must be about 1000 times cheaper than the consequence of a bug in production. If the Agent doesn't pass offline eval, it must not be deployed.

## 3. Groups of Evaluation Metrics

Not all metrics are equal. It is necessary to choose metrics tied to the use case and business outcome.

### 3.1. Task Completion & Answer Quality
### 3.1. Task Completion & Answer Quality
- **Task Completion:** Binary evaluation (Pass/Fail), Partial credit (by % of completed subtasks), Weighted scoring, or Trajectory eval (evaluating the entire process).
- **Answer Quality (Accuracy):** 
- **Answer Quality (Accuracy):** 
  - *Exact match / F1 token:* Good for short, factual answers.
  - *BERTScore / Embedding cosine:* Good for semantic comparison.
  - *LLM Judge / Human:* Good for complex, subjective content.

### 3.2. Business Metrics & North Star
### 3.2. Business Metrics & North Star
Need to define a 3-layer framework:
1. **North Star Metric:** The core metric of business value (e.g., Resolution rate).
2. **Guardrail metrics:** Metrics that are not allowed to degrade (e.g., P95 latency $\le$ 5s, Faithfulness $\ge$ 0.8).
3. **Diagnostic metrics:** Used when an incident occurs for diagnosis (e.g., RAGAS scores).

## 4. RAGAS Framework
## 4. RAGAS Framework

RAGAS (Retrieval Augmented Generation Assessment) is the standard framework for evaluating the quality of a RAG pipeline. It consists of 4 metrics (scored from 0-1):

- **Faithfulness:** Does the answer closely follow the retrieved context? (Low = Hallucination).
- **Context Recall:** Did the Retriever fetch enough necessary information from the ground truth? (Low = Retrieved missing documents).
- **Context Precision:** Does the retrieved context contain a lot of genuinely relevant information? (Low = Retrieved a lot but with noise/garbage).
- **Answer Relevancy:** Is the answer relevant to the user's question? (Low = Off-topic).

**Diagnostic Flowchart when the score is low:**
`Context Recall` (Increase top-k, smaller chunks) $\rightarrow$ `Context Precision` (Add re-ranking) $\rightarrow$ `Faithfulness` (Force prompt to only use context) $\rightarrow$ `Answer Relevancy` (Improve answer template).

## 5. Benchmark Design

*Garbage in, garbage out.* Evaluation relies heavily on the quality of the Benchmark.

- **Golden Dataset:** A standard dataset (usually 50-100 QA pairs for production, 20 for sanity check) along with expert sample answers (expected answers).
- **How to create:**
  1. *Expert-written:* High-stakes, high quality but expensive.
  2. *From production log:* Realistic, moderate labeling cost.
  3. *LLM-generated:* Fast, scales well, initial boot-strap (always requires Human review).
- **Stratified Sampling:** Taking stratified samples (by category, difficulty) to ensure there is no bias towards a common group of questions.
- **Edge Cases & Adversarial Inputs:** Need to test about $\ge$ 10% of bypass cases: Prompt injection, PII extraction, Jailbreak, Typos, Mixed language.
- **Data Contamination:** Avoid the LLM having learned the test data by keeping the benchmark secret or changing it frequently.

## 6. LLM-as-Judge
## 6. LLM-as-Judge

Using an LLM to automatically score answers based on a clear rubric helps scale up the evaluation that human eval cannot do.

- **Rubric:** Needs clear criteria (scale 1-5) with examples. Can use *Reference-based* (having a standard answer to compare against) or *Reference-free* (scoring independently by length, style...).
- **Pairwise vs Pointwise:** Pairwise (A vs B) is easier to score and has less bias, good for A/B testing prompts. Pointwise (absolute score) is convenient for tracking over time.
- **Chain-of-Thought (CoT):** Requiring the LLM Judge to analyze step-by-step before scoring will help increase agreement with experts by 15-20%.
- **7 Biases of LLM Judge:** Position bias, Verbosity bias (likes long sentences), Self-preference (GPT likes GPT), Sycophancy (flattering the user), Authority, Format, Recency.
- **Calibration:** Always compare LLM scores with Human scores on a subset $\ge$ 50 samples. Achieving a Cohen's Kappa $\kappa \ge 0.6$ or Spearman $\rho \ge 0.7$ is required before using that judge.

## 7. Statistical Rigor

LLMs have randomness (temperature $>0$), therefore conclusions cannot be made based on a single run or a single number.

- **Confidence Interval (CI):** Run at least 3 times, report Mean $\pm$ Standard Deviation.
- **Significance Test:** Use Paired t-test to see if Agent V2 is truly better than V1 (p-value $< 0.05$).
- **Power Analysis:** To detect a small difference (e.g., 0.05 points), you need about $\ge$ 30-50 cases for the benchmark. 20 cases in a Lab environment is just a sanity check.

## 8. Evaluating Safety and Agentic Behavior

For Agents that use Tools and perform Multi-step processes:
- **Trajectory Evaluation:** Evaluating the whole process (Step correctness, Efficiency) instead of just the final result. The Agent might output the correct result but take a convoluted path, wasting resources.
- **Safety Eval:** Test Jailbreak (refuse $\ge$ 95%), PII leakage (0% leak), Toxicity (0%), Financial/Medical advice (refuse).
- **Bias & Fairness:** Check fairness among gender groups, minority languages, ages.
- **Red Team:** Hire experts to intentionally break the system within a limited time to detect vulnerabilities before a major release.

## 9. Failure Analysis & Continuous Improvement

Scores only indicate the problem; Failure Analysis actually points out how to fix it.
- **Error classification:** Wrong answer, Hallucination, Tool failure, Refusal, Slow, Inconsistent...
- **5 Whys:** Ask "Why" 5 times to find the *Root Cause*. Example: Wrong $\rightarrow$ Retrieved missing $\rightarrow$ Slow Index $\rightarrow$ Data pipeline error.
- **Failure Clustering:** Group errors by root cause. Fixing 1 root cause (e.g., indexing) can solve a series of errors.
- **Continuous Improvement Loop:** Evaluate $\rightarrow$ Analyze $\rightarrow$ Improve $\rightarrow$ Augment (add to benchmark) $\rightarrow$ Evaluate.

## 10. Integrating Observability
Evaluation (Eval) and Monitoring (Observability) go hand in hand:
- **Observability (Day 13):** What is happening in production right now?
- **Evaluation (Day 14):** What is the quality of what is happening?
- Practical flow: Log (Langfuse) $\rightarrow$ Sample 1% $\rightarrow$ Run RAGAS automatically $\rightarrow$ If score is poor $\rightarrow$ Alert & Human review.
