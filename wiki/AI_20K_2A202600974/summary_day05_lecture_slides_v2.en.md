---
type: summary
title: "Summary of Day 5 Lecture Slides v2: AI Product Design for Uncertainty"
description: "A detailed summary of the Day 5 Lecture Slides v2, exploring the transition from AI model capabilities to trustworthy user products, focusing on feedback loops, data flywheels, and ROI."
tags: [AI product, product management, uncertainty, UX, evaluation, feedback loop, data flywheel, ROI]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/5/1-day05-lecture-slides-v2.pdf"]
---

# Summary of Day 5 Lecture Slides v2: AI Product Design for Uncertainty

These slides complement the Day 5 instruction, emphasizing how to transition from a functioning AI model to a product that users trust. It heavily focuses on the iterative nature of AI products, feedback mechanisms, and the economics of AI.

## 1. The Core Misconceptions

- **Demo ≠ Product:** An agent that "works" is not necessarily a successful product. Common mistakes include adding AI just for FOMO (Google AI Overviews vs. Perplexity), stopping at an 80% accurate demo (Gamma/Tome requiring too much manual fixing), or building everything from scratch when APIs suffice.
- **AI is Probabilistic:** Unlike traditional software that follows strict rules and yields consistent results, AI outputs vary. Designing an AI product means designing for this inherent uncertainty.

## 2. Managing Uncertainty: The Three Pillars

- **Requirement:** Must define thresholds and fallback behaviors. It's not just "Input -> Output," but "Input -> Output (with 85% confidence), else ask user."
- **UX (Graceful Failure & Trust Recovery):** Design for when the AI is wrong. The user must be able to see the error, correct it easily, and regain trust in the system.
  - *4 UI Patterns:* What happens when right? When unsure? When wrong? When trust is lost?
- **Eval (Quality Distribution):** Testing is no longer pass/fail. It's about running the system 100 times and determining what percentage of failures is acceptable.

## 3. Automation vs. Augmentation & Error Types

- **Deployment Strategy:** How you deploy AI changes everything. GitHub Copilot uses augmentation (low accuracy but zero friction to reject). Spam filters use automation (high accuracy required because errors are hidden from the user).
- **Precision vs. Recall:** 
  - **Precision:** Focuses on minimizing false positives. Prioritize this when the user cannot easily see or fix the error, and the cost of acting wrongly is high (e.g., Legal RAG, Bank Chatbot).
  - **Recall:** Focuses on minimizing false negatives. Prioritize this when missing something is catastrophic, even if the user doesn't see it (e.g., Child content moderation, Fraud detection).

## 4. The Data Flywheel and Feedback Loops

- **AI is a Living Organism:** Traditional software is static once shipped. AI products begin their lifecycle once shipped.
- **The Loop IS the Product:** Data collection -> Analysis -> Model fine-tuning -> Repeat. The speed and quality of this loop define the product's success.
- **Types of Feedback Signals:**
  1. **Implicit:** System collects data without user intent (e.g., time spent reading, ignoring a Copilot suggestion).
  2. **Explicit:** User actively rates the output (e.g., Thumbs up/down, "Was this helpful?").
  3. **Correction:** User manually fixes the AI's output (e.g., editing a Grammarly suggestion). This is the highest quality signal.
- **High-Value Data Sources:** Real-time data, user-specific data, specialized domain data (e.g., Dragon medical records), human expert evaluations, RLHF (Reinforcement Learning from Human Feedback), and context data.

## 5. AI Economics and ROI

- **The Cost Triangle:** You must balance Cost, Capability, and Speed. 
  - *Copilot:* Prioritizes speed (small model, fast, high error rate acceptable).
  - *Harvey (Legal AI):* Prioritizes capability (large model, slow, high cost acceptable).
  - *Grammarly:* Prioritizes cost (rules-based first, AI only when necessary to support 30M+ free users).
- **ROI Modeling (3 Scenarios):** Because AI costs scale per use (inference costs), you must plan for three scenarios:
  1. **Conservative:** Low accuracy, low adoption, high costs.
  2. **Realistic:** Average accuracy, medium adoption, balanced costs.
  3. **Optimistic:** High accuracy, flywheel effect activated, reduced costs at scale.

## 6. Hackathon Deliverables (Thin Spec)

The slides conclude by defining the deliverables for the Day 5/6 Hackathon:
- **AI Product Canvas:** Summarizes Value, Trust, Feasibility, and Learning Signals.
- **User Stories (4 Paths):** Happy, Low-confidence, Failure, Correction.
- **Eval Metrics:** Define thresholds and red flags.
- **Failure Modes:** Trigger -> Impact -> Mitigation.
- **ROI Scenarios:** Conservative, Realistic, Optimistic.
- **Prototype:** Must demonstrate the failure path, not just a successful "happy path."
