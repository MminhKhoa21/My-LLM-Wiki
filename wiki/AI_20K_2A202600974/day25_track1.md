---
type: summary
title: "Day 25 Track 1: Roadmap & Execution"
description: "Frameworks for AI startup execution: RICE prioritization, Now/Next/Later roadmaps, OKRs, and Dependency mapping."
tags: [startup, roadmap, product-management, OKRs, FinOps]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/25/day25-track1-ai-product-slide-deck.pdf"]
---

# Day 25 Track 1: Roadmap & Execution

This document summarizes the slide deck on "Roadmap & Execution" (Kế hoạch sinh tồn của AI startup) which provides a 4-step framework for founders post-fundraising to prioritize tasks and measure outcomes.

## 1. Prioritization Framework: RICE & 2x2 Matrix
Founders often struggle with "Idea Overload". To avoid making decisions based on "gut feeling" or the loudest voice, the **RICE Framework** uses mathematics to score ideas:
- **Reach (R)**: Number of users impacted per quarter.
- **Impact (I)**: Scale from 0.25 (tiny) to 3 (massive).
- **Confidence (C)**: Confidence level (50%, 80%, 100%). Must be tested; 50% max if untested.
- **Effort (E)**: Person-months required.

*RICE Score = (Reach × Impact × Confidence) / Effort*

### Value-Effort 2x2 Matrix
- **Quick Wins**: High value, low effort. Build momentum.
- **Strategic Bets**: High value, high effort. Build long-term moat.
- **Fill-ins**: Low value, low effort. Do when free.
- **Non-starters**: Low value, high effort. Discard.

## 2. Roadmap Mapping: Now / Next / Later
A traditional Gantt Chart is dangerous because it forces arbitrary deadlines that are often missed. Instead, use a **Now/Next/Later** format focusing on problems rather than fixed features:
- **NOW**: What is currently being built (1-3 months). High detail, low risk. E.g., Quick Wins.
- **NEXT**: What to build next (3-6 months). Medium detail, medium risk. E.g., Strategic Bets.
- **LATER**: Long-term vision (6-18 months). Low detail, high risk. Can change based on market.

## 3. Setting Milestones: OKRs
Tracking "Output" (e.g., lines of code, number of features) leads to wasted effort. Instead, track **Outcome** using **OKRs** (Objectives and Key Results).
- **Objective (O)**: Qualitative, inspiring goal.
- **Key Results (KR)**: Quantitative, measurable outcomes.
  - *Leading*: User behavior metrics (predictive).
  - *Lagging*: Business/Revenue metrics (confirming).
  - *Quality*: NPS, retention, churn (safeguard).

## 4. Parasitic Traps: Dependency Mapping
AI startups often rely on external services (e.g., [[OpenAI]] API, cloud providers, App Stores) making them vulnerable to unexpected changes like rate limits or policy updates.
- **Dependency Mapping**: Identify external dependencies that could kill the project.
- **Plan B**: Every Tier 1 dependency requires a fallback plan deployable within 24 hours.
- **Critical Path**: Identify the longest sequence of tasks that dictates the launch date. Typically, data pipeline and legal compliance form the critical path for AI startups. Delay here delays the entire project.

## Milestone 1: Investor-Ready Package
Combine the outputs of Day 16-20 into a single package for Seed Round fundraising:
1. Market Analysis + PRD
2. Financial Model + Unit Economics
3. Investor Pitch Deck
4. Roadmap Now/Next/Later + OKRs
5. Dependency Map + Critical Path
