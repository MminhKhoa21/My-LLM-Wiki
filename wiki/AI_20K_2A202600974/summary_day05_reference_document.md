---
type: summary
title: "Summary of Day 5 Reference Document: AI Product Design for Probabilities"
description: "A detailed summary of the Day 5 reference document from VinUni A20 on designing AI products for uncertainty, including frameworks, case studies, and UX/eval best practices."
tags: [AI product, product management, uncertainty, UX, evaluation, metrics]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/5/05-reference-document.pdf"]
---

# Summary of Day 5 Reference Document: AI Product Design for Probabilities

This document serves as the main reference for Day 5 of the VinUni A20 AI in Action course. It emphasizes that AI outputs are probabilistic (probabilities with margins of error), not exact results. Designing for AI means designing for uncertainty.

## 1. Key Frameworks & Models

### Core Frameworks
- **AI = Probabilistic**: AI outputs are probabilities with margins of error. Products must be designed to handle this uncertainty gracefully.
- **Automation vs. Augmentation**: Two main deployment paths. Automation acts on behalf of the user, while augmentation suggests actions for the user to decide. Choosing incorrectly cascades to all future product decisions.
- **Agency Progression (V1 → V3)**: Start with augmentation and gradually move to automation. (e.g., V1: routing -> V2: copilot -> V3: automatic). Each step collects data for the next.
- **Three Pillars (Requirement, UX, Eval)**: AI changes these core areas. Requirements need thresholds and failure modes; UX must handle errors gracefully; Eval must measure quality distribution rather than binary pass/fail.
- **Failure Mode Library**: Instead of listing features, list how the product can fail (Trigger / Impact / Mitigation).
- **Precision vs. Recall**: Product Managers must choose between high precision (fewer false positives) or high recall (fewer false negatives) depending on the "cost of error" for their product.
- **4 Paths UX for AI**: What happens when AI is right (value moment)? When it's low-confidence (escalate)? When it's wrong (correction path)? When trust is lost (explain & opt-out)?
- **Graceful Failure + Trust**: UX design must account for AI errors. Show confidence levels, explain why, allow users to correct the output, and provide an opt-out.
- **AI Product Canvas**: A 3-column canvas (Value, Trust, Feasibility) plus a Learning Signal row, merging requirements, UX, and evaluation into one artifact.
- **Feedback Loop & Data Flywheel**: An AI product is an organism. The loop is: Ingest → Digest → Output → Repeat. Model capabilities are commoditized; proprietary data is the true moat.

### External Frameworks
- **Reforge - AI Product Management Course**: The source of many strategy frameworks like "Four Critical AI Product Strategy Mistakes," "Cost-Capability-Speed," and "AI Feature Map."
- **Zwee Dao - AI Product Design Series**: Source for UX frameworks on automation/augmentation, graceful failure, and explainability.

## 2. Case Studies

- **Google AI Overview vs. Perplexity**: Same tech but different product strategy. Google "sprinkled AI" on search, causing errors, while Perplexity built a new product around it.
- **Chegg**: Disrupted by ChatGPT. Although Chegg had data, they didn't leverage it as an AI advantage. Quizlet pivoted better.
- **GitHub Copilot**: Even with only 30% accuracy, it has 20 million users because the "cost of rejection" is practically zero (just keep typing). An example of speed-first ROI.
- **Harvey**: Legal AI where errors can lose a case. Needs high precision. High cost but clients accept it due to the value. Capability-first ROI.
- **Microsoft Tay**: Lacked a failure design and turned into a racist bot. Shows the necessity of the "when AI is wrong" UX path.
- **Descript**: Tied AI quality to pricing tiers. Quality is a spectrum, not binary.
- **Microsoft Dragon**: AI for medical scribes. Transitioned from synthetic data (30-60% acceptance) to real data (75-83% acceptance). Real data creates a powerful flywheel.
- **Customer Support Agent V1→V3**: A team tried to jump straight to V3 (automation) and failed due to errors. They had to step back and progress from augmentation to automation using collected data.

## 3. Core Principles

1. **AI is not standard software**: Requirements, UX, and Evals must be approached differently.
2. **Design for Uncertainty**: If your product uses AI, you are designing for uncertainty.
3. **Deployment Strategy**: Different deployment strategies (Copilot vs. Spam filter) yield opposite results with the same AI.
4. **The Last 20%**: Getting from 0 to 80% takes a week; 80 to 95% takes 4x the effort. A demo is not a product.
5. **Failure over Features**: List failure modes instead of features.
6. **Visibility of Errors**: If users don't see the error, prioritize precision. If they see it immediately, recall might be okay.
7. **Data Flywheel**: Models are commodities; proprietary data is the real advantage.
8. **Constant Evolution**: Today's model is the worst model you will ever use.
9. **The Loop is the Product**: The feedback loop is the core IP.
10. **The Utility Equation**: Intelligence × Context × UI = Utility. If any factor is zero, utility is zero.
11. **Qualitative > Quantitative**: An 87% accuracy metric can hide crucial flaws. Understand WHERE and WHY the AI fails.

## 4. Further Reading & Resources

The document lists additional resources for AI Product Management, Precision/Recall & Eval, UX for AI, PRD templates, Feedback Loops, ROI measurement, and Automation vs. Augmentation. Notable mentions include Lenny's Podcast interviews, Google's PAIR Guidebook, a16z reports, and Stanford HAI research.
