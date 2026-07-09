---
type: summary
title: "Day 24 Track 1: AI Ethics, AI Safety and Responsible AI"
description: "Summary of Day 24 Track 1 covering AI safety, harm mapping, system mapping, and responsible AI practices."
tags: [ai-ethics, ai-safety, responsible-ai, harm-map, track1]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/24/d24-slide-v1.pdf", "AI_20K_2A202600974/24/day24-track1-lab.pdf"]
---
# Day 24 Track 1: AI Ethics & Safety

This page summarizes the lecture and lab on AI Ethics and Safety for Track 1.

## Key Concepts

### AI Safety & Ethics

AI safety is not just about whether a system functions correctly, but how it impacts real users in real-world contexts, and whether there are sufficient guardrails and accountability mechanisms in place before deployment. "Safe AI is a system placed in the right context, with the right guardrails, and someone taking responsibility when things go wrong."

### Failure Modes of AI

- **Hallucination:** Fabricating facts, policies, data, or links with high confidence.
- **Bias / Fairness:** Providing skewed results across different demographics or creating subtle inequalities.
- **Sycophancy:** Agreeing with the user even when the user is wrong.
- **Over-reliance:** Users trusting the AI's output as the absolute truth and failing to verify it.
- **Harmful Advice:** Giving dangerous medical, legal, financial, or self-harm advice.
- **Privacy Leak:** Exposing PII, prompts, internal documents, or other users' data.
- **Escalation Failure:** Failing to refuse or hand off to a human agent when necessary.
- **Misuse / Jailbreak:** Users forcing the AI to bypass its guardrails or constraints.

### System Map for Debugging

When an AI system fails, it's crucial to identify which layer originated the error rather than just blaming the model:

1. **User Experience (UX):** The interface users interact with. If the UI makes the AI look too official without uncertainty cues, users might over-rely on it.
2. **System Message & Grounding:** Instructions guiding the model and the sources it relies on. Errors here lead to hallucinations or out-of-scope answers.
3. **Safety System:** Guardrails that block, refuse, or escalate requests. Weaknesses here allow harmful or sensitive requests to pass through.
4. **Model:** The core AI model. If it's too weak for the task or inherently flawed, it will fail despite good instructions.

### Harm Map Framework

To systematically analyze AI risks, we evaluate them across four dimensions:

- **Severity:** The impact of the harm (Low: minor annoyance, Medium: reversible harm, High: financial/legal/opportunity loss, Critical: physical harm or irreversible damage).
- **Scale:** The number of people or groups affected.
- **Probability:** The likelihood of the harm occurring.
- **Frequency:** How often the harm repeats if it occurs.

## Lab 24: Case Study Hunt & Harm Map

The lab focuses on selecting an industry (e.g., HR, Education, Healthcare, Mobility, Media, Content Creator) and finding 2-3 real-world AI failure case studies within that domain.

- **Industry Risk Snapshot:** Evaluate the industry's overall risk profile (physical harm potential, high-stakes decisions, sensitive data, blast radius).
- **Harm Map Worksheet:** For each case study, students must identify the high-risk moment, affected stakeholders, failure mode, the layer where the error originated, the actual harm, the harm lens (e.g., misinformation, injury, privacy loss), and score it based on Severity, Scale, Probability, and Frequency.

---

### Day 24 Review Questions  

1. According to the lecture, which of the following definitions best describes "Safe AI"?  
   - A. An AI system with high accuracy that never makes mistakes.  
   - B. An AI system placed in an appropriate context, with guardrails and human accountability when incidents occur.  
   - C. An AI system capable of self-learning and improvement without humans.  
   - D. An AI system that complies with all current legal regulations.  

2. What phenomenon does the state of “Sycophancy” in AI refer to?  
   - A. AI makes up false information but is very confident.  
   - B. AI always agrees with the user even when the user is wrong.  
   - C. AI discloses other users' personal information.  
   - D. AI refuses to answer all sensitive questions.  

3. When an AI system gives a wrong answer due to insufficient grounding in the system message, which layer in the System Map does this error belong to?  
   - A. UX (User Experience)  
   - B. Safety System  
   - C. Model  
   - D. System Message & Grounding  

4. In the Harm Map Framework, what does the “Scale” factor assess?  
   - A. The severity of the harm (from low to critical).  
   - B. The number of people or groups affected.  
   - C. The probability of harm occurring.  
   - D. The frequency of the harm repeating once it has occurred.
