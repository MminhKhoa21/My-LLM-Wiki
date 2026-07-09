---
type: summary
title: "Day 18 Track 1: Human-Centered AI Design"
description: "Summary of Human-Centered AI design principles, focusing on trust calibration, agency, and feedback loops."
tags: [UX, Human-Centered AI, Trust, Agency, Feedback, Design]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/1-d18-slide-v1-track1.pdf", "raw/AI_20K_2A202600974/18/day18-track1-lab.pdf"]
---
# Human-Centered AI Design (Day 18 - Track 1)

**Instructor:** Mai Anh Nguyen (Blue)

---

## 1. Core Principles & Expectations  

- **Expectation Setting:** Avoid letting the UI promise more than the AI can deliver. Users need to understand what the AI can do, what it cannot do, and how it might fail.  

- **AI Personality:** Combining *warmth* (friendly, approachable) and *competence*. A calibrated competence helps build sustainable trust. Emitting a signal of "not too perfect" can lower initial expectations and improve long-term satisfaction.  

- **Reference Frameworks:** Google's PAIR Guidebook (AI product framing) and Microsoft's HAX Toolkit (AI interaction design).  

---

## 2. Trust Calibration  

- **Overtrust:** Users trust the AI beyond its true capabilities, leading them to delegate tasks excessively without verifying.  

- **Distrust:** Users trust the AI less than its capabilities, leading to *underuse*.  

- **Formula for Trust:** `Trust Calibration = Expectation + Explainability + Control`  
  - *Expectation:* Clarify AI limits.  
  - *Explainability:* Help users understand why AI produced a specific output.  
  - *Control:* Allow users to edit, undo, preview, or approve actions.  

---

## 3. Augmentation vs. Automation (Agency)  

Determine the level of AI autonomy based on the **cost of error** and user intent certainty.  

- **Act (Automation):** High certainty, low cost of error. Easy to undo. AI performs the action automatically to save time.  

- **Ask (Mixed-Initiative):** Moderate certainty, significant impact. AI asks for confirmation before proceeding.  

- **Don't Act (Inaction):** High cost of error, low certainty. The system leaves the decision entirely to the user.  

---

## 4. Handling AI Failures and Uncertainty  

- Explain *why* the system made a decision (e.g., mapping user behavior or inputs to outputs).  

- Display results with confidence levels.  

- Offer clear escape routes (e.g., transferring to a human agent, providing fallback options).  

- **Undo / Rollback:** Allow users to easily revert AI actions.  

- Use error states as opportunities to gather feedback and educate users on correct usage.  

---

## 5. Feedback Loops  

Feedback enables the system to learn from users and users to learn from the system.  

- **User Feedback (Explicit):** Thumbs up/down, rating, reporting errors.  

- **User Feedback (Implicit):** User behaviors like undoing, abandoning tasks, or accepting suggestions.  

- **System Feedback (Explicit):** Notifications explaining limits, status, or next steps.  

- **System Feedback (Implicit):** UI affordances, default states, and progressive disclosure that guide user mental models.  

---

## 6. Lab Scenario Design  

The lab exercise emphasizes designing a continuous slice of the AI experience across four phases:  

1. **Onboarding:** Setting expectations without overwhelming the user.  

2. **During Action:** Displaying AI reasoning, asking for context, or proposing solutions.  

3. **After Action:** Reviewing results, editing, and confirming.  

4. **Failure & Recovery:** Creating feedback loops to correct errors and continue the workflow seamlessly.

---

### Day 18 Review Questions  

1. The **Trust Calibration** formula includes Expectation, Explainability, and Control. Which element helps users understand why the AI produced a specific result?  
   - A. Expectation  
   - B. Explainability  
   - C. Control  
   - D. Automation  

2. In the **Augmentation vs Automation** decision, when should AI act automatically?  
   - A. Low certainty, high cost of mistakes  
   - B. High certainty, low cost of mistakes  
   - C. Medium certainty, significant impact  
   - D. Always automate to save time  

3. When the AI encounters an error or is uncertain, which of the following handling methods is recommended?  
   - A. Hide results to avoid confusion  
   - B. Display results with confidence levels and provide an escape hatch  
   - C. Force users to accept the results  
   - D. Do not collect feedback from errors  

4. "Users clicking the **like/dislike** button or rating the product" belongs to which type of feedback?  
   - A. User Feedback (Implicit)  
   - B. User Feedback (Explicit)  
   - C. System Feedback (Explicit)  
   - D. System Feedback (Implicit)
