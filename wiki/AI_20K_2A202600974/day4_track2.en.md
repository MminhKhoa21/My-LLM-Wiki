---
type: summary
title: "Day 4 Track 2 - Prompt, Context Engineering, Tool & Control"
description: "Tổng hợp kỹ thuật về Prompt, tối ưu Context, gọi Tool an toàn và cơ chế kiểm soát Agent."
tags: [ai, 20k, day4, track2, context-engineering, control, tool-calling]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/4/2-day04-lecture-slide-v3.pdf"]
---

# Day 4 Track 2: Prompt, Context Engineering, Tool & Control



## 2. Prompt Fundamentals


- **Tool Declaration**: 
- **Tool Result as Context**: 

- **Evaluation & Versioning**:

---

### Day 4 Review Questions

1. **According to the lecture, what are the four pillars a reliable Agent is built upon?**  
   - A. Prompt, Context, Tool, Control  
     *A. Prompt, Context, Tool, Control*  
   - B. Prompt, Memory, Tool, Evaluation  
     *B. Prompt, Memory, Tool, Evaluation*  
   - C. Context, RAG, Tool, Guardrail  
     *C. Context, RAG, Tool, Guardrail*  
   - D. Prompt, Context, Logging, Approval  
     *D. Prompt, Context, Logging, Approval*  
   **Answer:** A  

2. **How is the "Lost in the Middle" phenomenon in Context Engineering mitigated?**  
   - A. Cramming all information into the middle of the context  
   - B. Placing important information at the beginning and the end of the context  
   - C. Filtering out all conversation history information  
   - D. Using more examples in the prompt  
   **Answer:** B  

3. **In Tool Calling, which element acts as the instruction for the LLM to decide which tool to choose?**  
   - A. The result returned from the tool  
   - B. The tool name and its detailed description  
   - C. The JSON format of the tool  
   - D. The number of declared tools  
   **Answer:** B  

4. **When is the "Human-in-the-Loop" (HITL) mechanism applied?**  
   - A. When the tool performs data reading operations  
   - B. When the tool performs state-changing operations (e.g., payment, deleting DB)  
   - C. When the LLM returns incorrectly formatted results  
   - D. When the context is noisy (Context Rot)  
   **Answer:** B
