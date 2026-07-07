---
type: summary
title: "Day 22 – Track 3: DPO, ORPO & Alignment"
description: "Sự dịch chuyển từ SFT sang Preference Learning, chi tiết phương pháp DPO, ORPO, SimPO, GRPO và cách đánh giá Alignment qua LLM Benchmarks."
tags: [ai, 20k, day22, track3, dpo, orpo, alignment, rlhf, grpo]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/Day 22 - Track 3 - DPO-ORPO-Alignment.pdf", "raw/AI_20K_2A202600974/22/Day 22 - Track 3 - DPO-ORPO-Alignment_v2.pdf"]
---


**Path:** [[track3_ai_app|Track 3: AI Application]]  

# Day 22 – Track 3: DPO, ORPO & Alignment  

**Instructor:** VinUniversity  
**Course:** AICB Phase 2 · Track 3 · Day 22  

---

## 1. From SFT to Preference Learning  

SFT (Supervised Fine-Tuning) teaches the model format and style (the model learns what to say).  

However, SFT-only models often tend to be overly cautious (over-hedges), verbose, or excessively refuse.  

**Alignment** (teaching the model "how to say") is the step that helps the model learn the *margin* between a good and a bad answer (helpful, harmless, honest) based on **Preference Data** (chosen vs. rejected pairs).  

---

## 2. RLHF and the DPO Breakthrough  

### The Cost of RLHF (PPO)  

The InstructGPT pipeline: SFT → Reward Model (judge) → PPO (optimization).  

Disadvantages: requires loading three models simultaneously, high VRAM usage, PPO instability, and very sensitive hyperparameters.  

### DPO (Direct Preference Optimization)  
### *DPO (Direct Preference Optimization)*

Core idea of **DPO (2023)**: Eliminate the intermediate Reward Model entirely.  

Mathematics proves that the Optimal RL Policy has a closed-form solution.  

We can directly map preference pairs into a loss function for the model to learn:  

- **DPO Loss formula:** Optimizes cross-entropy on log-ratio probabilities of `chosen` vs `rejected`.  
- **Hyperparameter β (KL penalty):** Controls the divergence from the Reference Model.  
    - Increasing β (e.g., 0.2): Forces conservatism, stays close to the SFT base.  
    - Decreasing β (e.g., 0.05): Avoids conservatism, model is more free.  
- **Advantages:** Offline learning (more stable than PPO), fewer components. Still the strong default choice for helpfulness, tone, and safety problems.  

---

## 3. ORPO, SimPO & Alternatives (Single-Stage / No-Ref Generation)  

DPO still requires an SFT stage and a Reference model. New methods gradually remove these components.  

- **SimPO (2024):** No reference model needed. Uses *average log-prob* (length-normalized) to avoid length hacking. Very good when VRAM is limited.  
- **ORPO (2024):** Single-stage Alignment. Trains directly from Base Model to Aligned Model **without needing an SFT stage**. Integrates Odds Ratio preference into the loss.  
- **KTO:** Only needs Thumbs Up/Down labels (suitable for production logs) instead of ranking pairs. Based on Prospect Theory (loss aversion model).  

---

## 4. GRPO & RLVR: RL Returns for Reasoning  

In 2025 (DeepSeek R1 series), RL returns but in an optimized version, **without using Value Model / neural network Reward Model**:  

- **GRPO (Group Relative Policy Optimization):** Instead of using a Value Model network, it computes the average reward of a group of $G$ outputs as a baseline. Saves 50% VRAM and is very powerful for Reasoning.  
- **RLVR (RL from Verifiable Rewards):** Reward comes not from a learned judge, but from *programmatic verification* (regex, code unit tests, math format). Blocks learned-RM reward hacking, but introduces Verifier Gaming. Suitable for code/math generation.  

> **Rule of Thumb (Tulu 3 / Llama 3):** Modern alignment pipelines often stack: **SFT → Iterative DPO → GRPO/RLVR**.  

---

## 5. Evaluating Alignment (LLM Benchmarks)  

Evaluating alignment is complex because open-ended tasks have no single ground truth. It typically combines three layers:  

1. **Static Suites (Capability):** MMLU (Knowledge), GSM8K/MATH (Logical reasoning), IFEval (Format), HumanEval (Code). Monitors *Alignment Tax* (logic scores drop after alignment).  
2. **Judge-Based Suites (Response Quality):** MT-Bench, AlpacaEval 2 LC (Corrects length-bias), Arena-Hard (Harder, skill-level classification). LLM-as-Judge measures Win-rate.  
3. **RewardBench:** A benchmark that evaluates "Judges" and Reward Models (meta-evaluation).  

---

## References  

- [[day21_track3]] – LoRA/QLoRA (pre-alignment fine-tuning step)  
- [[day22_overview]]  
  *[[day22_overview]]*
