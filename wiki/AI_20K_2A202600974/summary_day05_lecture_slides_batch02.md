---
type: summary
title: "Summary of Day 5 Lecture Slides Batch 02: AI Product Kickoff Sprint"
description: "A comprehensive summary of the Day 5 Batch 02 lecture slides focusing on finding real problems, designing for AI failures, and scoping features for the hackathon."
tags: [AI product, hackathon, product management, uncertainty, UX, evaluation, requirements]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/5/1-day05-lecture-slides-batch02.pdf"]
---

# Summary of Day 5 Lecture Slides Batch 02: AI Product Kickoff Sprint

These slides cover the Day 5 Kickoff Sprint for the VinUni AI20K program, preparing teams for a Mini-Hackathon. The central narrative is moving from a technically capable demo to a trustworthy, user-focused AI product.

## 1. The Core Problem: Demo vs. Product

- **The Hook:** Just because an AI agent works technically (demo) doesn't mean anyone will use it. Demos are technical capabilities; products are value delivered in a real context.
- **Three Layers of Uncertainty:**
  1. **Input:** Users ask ambiguous or incomplete questions.
  2. **Output:** AI answers are not fixed and have variance.
  3. **Process:** It's hard to see why an AI made a specific decision.
- **Product Implication:** Standard software fixes bugs so they disappear. AI products must *manage the distribution of errors*. The product must be designed for times when the AI is uncertain or wrong.

## 2. Managing Errors & Uncertainty

- **Production Drift:** Even if the code doesn't change, model updates, context drift (e.g., policy changes), user drift (changing how they ask), and prompt drift can cause unexpected behavior.
- **Error Routing:** An AI product must have a path for errors (Detect → Route → Recover → Learn). If a prototype only has a "happy path," it is not an AI product.
- **Two Types of Errors (False Positive vs. False Negative):**
  - **False Positive (Reporting error):** AI says "yes" when it's "no." (e.g., flagging a valid transaction). This reduces trust.
  - **False Negative (Missing error):** AI says "no" when it's "yes." (e.g., missing a fraudulent transaction). This causes actual harm.
  - **Product Decision:** You must decide which error is more expensive based on your specific use case. If false positives are expensive, prioritize **Precision**. If false negatives are expensive, prioritize **Recall**.

## 3. Automation vs. Augmentation

- **Automation:** AI acts autonomously. Good when tasks are narrow, outcomes are predictable, and errors are cheap.
- **Augmentation:** AI assists a human. Often the right first step to gather data, learn, and lower risk before moving to automation. It is *not* just a lesser version of automation.
- **Human Roles:** In "Human-in-the-loop," define the role clearly: Reviewer (checks output), Decider (chooses from options), Trainer (provides learning signal), or Rescuer (intervenes when AI fails).
- **Task Boundary:** Don't automate an entire product. Break it down into tasks and automate specific, valuable slices.

## 4. The Three Pillars of AI Product Design

1. **Requirement (Not just features):** Needs to define the outcome, the confidence threshold, and the fallback mechanism. Ask: "What level of failure is acceptable?"
2. **UX (Not just pretty screens):** Design for when the AI is wrong. Incorporate "Graceful Failure" and "Trust Recovery." Ask: "What does the user do when the AI fails?"
3. **Eval (Not just pass/fail):** Measure the distribution of quality over many runs. Ask: "What percentage of errors is acceptable?"

## 5. UI Patterns for AI (The 4 Paths)

Every AI product must answer four questions:
1. **When it's right:** What does the user see?
2. **When it's unsure:** What does the system do (e.g., ask clarifying questions)?
3. **When it's wrong:** How does the user correct it?
4. **When trust is lost:** How does the user opt-out or recover?

## 6. Hackathon Preparation (Build Slices & Thin Spec)

- **Evidence-to-Build Slice:** Start with real user evidence (interviews, reviews, own experience). Find the insight, define the opportunity, and choose a small "build slice."
- **Build Slice Scope:** One user, one task, one AI decision, one failure path.
- **AI Product Canvas:** A single page defining Value, Trust, Feasibility, and Learning Signals.
- **Thin Spec Failure:** You must be able to write: "If user [trigger], AI might [fail], causing [impact]. The prototype handles this by [mitigation]."
- **Vibe Coding for Product:** Use AI to build the prototype, but the prototype *must* demonstrate a failure path, not just a successful demo.

## 7. Exit Ticket for Day 5

Teams must leave Day 5 with:
1. User evidence
2. A single build slice
3. A decision on Auto vs. Augment
4. A defined failure path to test
5. Clear ownership roles for the hackathon
