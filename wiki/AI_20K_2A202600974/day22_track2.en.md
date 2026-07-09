---
type: summary
title: "Day 22 Track 2: LLMOps & Prompt Versioning"
description: "Sử dụng LangSmith, Prompt Hub và Guardrails để quản lý vòng đời LLM, theo dõi prompt và giám sát hệ thống."
tags: [ai, 20k, day22, track2, llmops, langsmith, prompt-versioning, evaluation, guardrails]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/Day 22 - Track 2 - LLMOPS-prompt-versioning.pptx"]
---

> **Roadmap:** [[track2_ai_engineer|Track 2: AI Engineer]]  

# LLMOps & Prompt Versioning (Day 22 - Track 2)  

**Lecturer:** VinUniversity  
**Course:** AICB Phase 2 · Track 2  

> **Key Question:** "Prompt change = behavior change." A small change in the system prompt can increase latency by 3x and token cost by 200%. How to trace, version, and evaluate every change?  

## 1. LLMOps vs Traditional MLOps  

- Core difference: In LLMOps, versioning the **Prompt** is as important as versioning code or data.  
- **Purpose:** Traceability, version control, and continuous evaluation ensure the stability and cost-effectiveness of LLM applications.  

## 2. Key Tools & Techniques  

- **LangSmith (Trace, Debug & Monitor):**  
  - Instrument (measure) LLM applications.  
  - Trace each API call to debug bottlenecks.  
  - Filter traces by latency, cost, and error rate.  
- **Prompt Hub (Version Control):**  
  - Like "GitHub for prompts".  
  - Allows storing, versioning, and pinning prompts to control versions independently of code.  
- **LLM Evaluation (W&B Weave / RAGAS):**  
  - Evaluate beyond standard accuracy.  
  - Use RAGAS to systematically score faithfulness, relevance, and hallucination.  
- **Guardrails & Safety Monitoring:**  
  - Validate both LLM inputs and outputs.  
  - Prevent PII leakage, detect Prompt Injection.  
  - Auto re-ask when LLM returns wrong format (non‑JSON).  

## 3. Lab Deliverables  

- **LangSmith Project:** Record >100 traces from the RAG pipeline. Perform detailed analysis of latency, cost, and error rate.  
- **Prompt Hub:** Create 2 prompt versions with clear commit messages. Implement A/B routing with 50/50 split.  
- **RAGAS Evaluation Report:** Run evaluation on 50 QA pairs. Target: Faithfulness score > 0.8. Compare results between the 2 prompt versions.  
- **Guardrails AI Validator:** Integrate a PII blocker (block emails, phone numbers), auto-reformat JSON, and log all incidents.  

## 4. Links  

- [[day22_overview]]  
- *[[day22_overview]]*

---

### Day 22 Review Questions

1. **What is the core difference between LLMOps and traditional MLOps?**  
   - A. LLMOps focuses more on data management than code.  
   - B. LLMOps treats Prompt version management as critically as code and data management.  
   - C. MLOps does not require evaluation.  
   - D. LLMOps is only used for small language models.  
   **Answer:** B  

2. **Which tool is described as "GitHub specifically for prompts" in the lecture?**  
   - A. LangSmith  
     *A. LangSmith*  
   - B. W&B Weave  
     *B. W&B Weave*  
   - C. Prompt Hub  
     *C. Prompt Hub*  
   - D. RAGAS  
     *D. RAGAS*  
   **Answer:** C  

3. **According to the lecture, what aspects of LLMs is RAGAS used to evaluate?**  
   - A. Only accuracy  
   - B. Inference speed and cost  
   - C. Faithfulness, relevance, and hallucination  
   - D. The ability to detect Prompt Injection  
   **Answer:** C  

4. **What is one of the goals of Guardrails & Safety Monitoring?**  
   - A. Increasing token generation speed  
   - B. Blocking PII leakage and detecting Prompt Injection  
   - C. Automatically generating new prompts from data  
   - D. Optimizing API costs  
   **Answer:** B
