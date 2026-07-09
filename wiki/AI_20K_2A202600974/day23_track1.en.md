---
type: summary
title: "Day 23 – Track 1: RAGAS, LLM-as-Judge & Guardrails"
description: "Đo lường và bảo vệ AI Agent thông qua framework RAGAS, LLM-as-Judge và kiến trúc Guardrails đa lớp."
tags: [ai, 20k, day23, track1, ragas, evaluation, guardrails, llm-as-judge]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/23/1-day24-ragas-guardrails.pdf"]
---


# Day 23 – Track 1: RAGAS, LLM-as-Judge & Guardrails




## 2. RAGAS Framework (4 Core Metrics)


## 4. Hallucination Detection



- [[day23_overview]]

---

### Day 23 Review Questions  

1. In the RAGAS framework, which metric measures "hallucination" by checking whether the answer is supported by the context?  
   - A. Context Precision  
     *A. Context Precision*  
   - B. Answer Relevancy  
     *B. Answer Relevancy*  
   - C. Faithfulness  
     *C. Faithfulness*  
   - D. Context Recall  
     *D. Context Recall*  

2. When using an LLM as a judge (LLM-as-Judge), which bias occurs when the LLM tends to choose the first or last option in a list?  
   - A. Length Bias  
     *A. Length Bias*  
   - B. Self-Enhancement Bias  
     *B. Self-Enhancement Bias*  
   - C. Style Bias  
     *C. Style Bias*  
   - D. Position Bias  
     *D. Position Bias*  

3. In the 4-layer Guardrails architecture, which layer is responsible for blocking PII (Personally Identifiable Information) using Regex or Presidio?  
   - A. L2 – LLM Layer  
     *A. L2 – LLM Layer*  
   - B. L4 – Audit Layer  
     *B. L4 – Audit Layer*  
   - C. L1 – Input Layer  
     *C. L1 – Input Layer*  
   - D. L3 – Output Layer  
     *D. L3 – Output Layer*  

4. Which method uses a Natural Language Inference (NLI) model to detect contradictions between the answer and context, thereby identifying hallucinations?  
   - A. SelfCheckGPT  
     *A. SelfCheckGPT*  
   - B. Semantic Similarity  
     *B. Semantic Similarity*  
   - C. NLI-based Detection  
     *C. NLI-based Detection*  
   - D. RAGAS Answer Relevancy  
     *D. RAGAS Answer Relevancy*  

5. Which metric in RAGAS is reference-free (no ground truth needed) and can be used directly in a production environment?  
   - A. Context Recall  
     *A. Context Recall*  
   - B. Exact Match  
     *B. Exact Match*  
   - C. Faithfulness  
     *C. Faithfulness*  
   - D. BLEU  
     *D. BLEU*
