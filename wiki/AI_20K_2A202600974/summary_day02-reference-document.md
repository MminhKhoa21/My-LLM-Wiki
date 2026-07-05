---
type: summary
title: "Summary: Day 02 Reference Document"
description: "A comprehensive summary of the reference frameworks, case studies, and reading materials for Day 02."
tags: [Reference, Frameworks, Case Studies, Reading List]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/day02-reference-document.pdf"]
---

# Summary: Day 02 Reference Document

## Overview
This document compiles the comprehensive reference materials, frameworks, case studies, and core principles taught in Day 02 of the VinUni AI 20K program. It serves as a guide for framing business requirements into structured AI problems.

## 1. Frameworks and Decision Models
### In-Class Frameworks
- **Business-to-AI Translation:** Converts vague ideas into structured Problem Statements.
- **AI Possibility Spectrum:** Classifies tasks as Easy, Hard, or Impossible for current AI to set correct expectations.
- **AI Fit Matrix:** Maps Ambiguity vs. Complexity to suggest Rule, LLM Feature, or Agent.
- **Escalation Ladder:** Progression from Prompt -> Retrieval -> Workflow -> Agent. Always start simple.
- **Non-AI Baseline:** Establish a manual or rule-based baseline before attempting AI.
- **Buy / Build / Boost:** Three avenues for AI integration (Off-the-shelf, Custom, or Augmenting existing workflows).
- **AI Readiness Checklist:** 5 criteria (data, metric, failure tolerance, user readiness, resources). Under 3 YES means "Not Yet".
- **UX Patch Patterns:** UX designs to compensate for AI weaknesses (e.g., confirmation dialogs, inline suggestions, sourcing).

### External Frameworks
- **Google PAIR Guidebook:** Guidelines for responsible AI design, focusing on user needs and AI strengths.
- **Microsoft HAX Toolkit:** 18 principles for Human-AI interaction.
- **NIST AI Risk Management Framework:** Organizational risk mapping and measurement.
- **Google Rules of ML:** 43 practical rules for ML engineering, particularly around heuristics.

## 2. Case Studies
- **Google Flu Trends:** A lesson in flawed problem framing and reliance on proxy metrics.
- **Google Photos:** Decided *against* AI for photo filters because rule-based heuristics were already sufficient.
- **Stripe AI:** Uses LLMs for internal reporting summaries, heavily reliant on PM review (AI as Boost).
- **GitHub Copilot & Gmail Smart Compose:** Demonstrates the "ghost text" UX pattern (suggest-only, user decides).
- **Grammarly:** Inline AI feedback where AI highlights but doesn't autonomously change text.

## 3. Reading List
- **AI Engineering:** "Building LLM Applications for Production" by Chip Huyen.
- **System Architecture:** "Emerging Architectures for LLM Applications" by a16z; "Hidden Technical Debt in ML Systems" by Sculley et al.
- **Product Management:** "Inspired" by Marty Cagan (Problem-first thinking); "Choosing Your North Star Metric" by Lenny Rachitsky.
- **Agents:** Anthropic's "Building Effective Agents" (emphasizes composable patterns over complex frameworks) and OpenAI's Practical Guide.

## 4. Core Principles (Quick Reference)
1. "Problem-first, not AI-first."
2. The model is only 10-20% of the work; data, UX, and operations are 80-90%.
3. "Solution looking for a problem" is the most common AI failure mode.
4. Build a baseline first.
5. 85% accuracy with good UX > 95% accuracy with bad UX.
6. "Not Yet" is not a failure; it shows maturity.
7. Use UX to patch where AI falls short.
8. AI is a Boost, not a Replacement.
