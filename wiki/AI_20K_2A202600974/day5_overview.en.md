---
type: overview
title: "Day 5 Overview - Thiết kế sản phẩm AI"
description: "Thiết kế sản phẩm AI đối phó với sự không chắc chắn, tập trung vào UX, đánh giá và Feedback loop."
tags: [ai, 20k, day5]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/5/1-day05-lecture-slides-v2.pdf"]
---
# Day 5: Designing AI Products for Uncertainty

## 1. AI Product ≠ Traditional Software

- Traditional software runs on rules, producing fixed results. AI runs on probabilities, results vary each time, and there is inherent uncertainty.

- Designing an AI Product is not just calling an API, but designing around that uncertainty. The 3 pillars of AI product design are: **Requirement**, **User Experience (UX)**, and **Evaluation (Eval)**.

## 2. Requirement & UX for AI
*## 2. Requirement & UX cho AI*

- Distinguish between **Automation** (AI does it automatically, invisible to the user, requires extremely high accuracy) and **Augmentation** (AI suggests, user approves, accepts lower accuracy in exchange for speed/efficiency). It is best to start with Augmentation and gradually increase Automation.

- **Graceful Failure & Trust Recovery**: AI will inevitably make mistakes; the key is to handle errors gracefully (provide alternatives, allow users to correct, explain reasons) to maintain user trust.

- Avoid defaulting to a Chatbot interface. UI/UX for AI should display the reasoning process, allow editing of plans, etc.

## 3. Evaluation - Precision vs Recall

- There are no absolute "right/wrong" answers, only quality distributions.

- **Precision**: The proportion of correct predictions among all positive predictions made by AI (reduces False Positives). Prioritize when the consequences of a wrong action are severe (e.g., transferring money, deleting emails).

- **Recall**: The proportion of actual positives successfully found (reduces False Negatives). Prioritize when missing something causes severe consequences (e.g., filtering child abuse content, medical diagnostics).

- Choosing to prioritize Precision or Recall depends on the problem and the User Experience (UX).

## 4. Feedback Loop & Data Flywheel
*## 4. Feedback Loop & Data Flywheel*

- AI products must continuously learn from user interactions.

- 3 types of feedback signals:

  - **Implicit**: View time, scrolling, acceptance/ignore rate.

  - **Explicit**: Thumbs up/down, star ratings.

  - **Correction**: User directly corrects the AI's output.

- **Data Flywheel**: User data helps improve the model, a better model brings a better experience, attracting more users -> creating a continuous loop of improvement. This is the core competitive moat of an AI Product.

## 5. ROI & Costs

- AI running costs depend on each usage (Inference cost). The more users, the higher the cost. Detailed ROI calculation (under conservative, realistic, and optimistic scenarios) is needed before scaling.
