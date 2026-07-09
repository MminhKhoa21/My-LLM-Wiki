---
type: summary
title: "Day 21 – Track 3: Fine-tuning LLMs (LoRA/QLoRA)"
description: "Khi nào cần fine-tune LLM, cơ chế LoRA và QLoRA, kiến trúc FlashAttention, pipeline huấn luyện và thực hành."
tags: [ai, 20k, day21, track3, fine-tuning, lora, qlora, flashattention]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/day06-fine-tuning-llms-tu-full-fine-tune-en-loraqlora.pdf"]
---

---

> **Track:** [[track3_ai_app|Track 3: AI Application]]

**Track:** [[track3_ai_app|Track 3: AI Application]]  

# Day 21 – Track 3: Fine-tuning LLMs – From Full Fine-tune to LoRA/QLoRA  


**Course**: AICB Phase 2 · Track 3 · Day 21  

---

## 1. When to Fine-tune?  

With Frontier Models (GPT-4o, Claude 3.5, Gemini 2) in 2025-2026, over 80% of tasks can already be solved well.  

- **Standard workflow:** Prompt Engineering → RAG → Fine-tune.  
- **When to fine-tune?:** When prompt and RAG are exhausted but the model still lacks a custom format, domain jargon, or when you need to reduce latency/cost at large scale (volume > 50k req/day).  
- **Critical note:** Fine-tuning is **NOT** for adding new knowledge (knowledge gaps). Use RAG to supply knowledge. Fine-tuning is mainly for adjusting **style and format**.  

---

## 2. LoRA (Low-Rank Adaptation)  
## 2. LoRA (Low-Rank Adaptation)

Instead of updating all parameters (Full Fine-tune) which is very VRAM‑expensive, LoRA freezes the base weights and only trains the delta $\Delta W$ via two low‑rank matrices $A$ and $B$.  

- Formula: $h = W_0 x + B \cdot A \cdot x$  
- $A$ and $B$ have rank $r \ll d$ (typically $r \in \{8, 16, 32, 64\}$). Only about 1% of parameters need training compared to Full FT.  
- **Inference:** When deployed, matrices A and B are merged directly into $W_0$, so inference speed remains unchanged (zero added latency).  

---

## 3. QLoRA – Fine-tune on Small GPUs  

Combines 4‑bit quantization (NF4) of the base model with bf16 LoRA adapters.  

- Allows training large models (e.g., 7B) on a single consumer GPU (e.g., RTX 3090 24GB).  
- Uses **PagedAdamW** to offload optimizer states to CPU RAM when VRAM is insufficient.  
- **Multi-tenant:** You can host one base model and attach multiple different LoRA adapters simultaneously for different clients or tasks.  

---

## 4. FlashAttention & Memory Optimization  

- **FlashAttention 2:** An IO‑Aware Exact Attention technique. Vanilla attention reads/writes through HBM (very slow); FlashAttention uses tiling to compute in SRAM (10x faster). It accelerates training by 2‑4x and drastically reduces activation memory. Should be enabled during training.  
- **Gradient Checkpointing:** Recomputes activations during backward pass instead of storing them, saving up to 60% VRAM (at the cost of ~20% extra training time).  
- **Sequence Packing:** Packs multiple small samples into one long sequence to double throughput (set `packing=True` in the library).  

---

## 5. Dataset & Training Pipeline  
## 5. Dataset & Training Pipeline

- **Dataset:** Quality matters more than quantity. 500 perfect samples are better than 10k noisy ones.  
- Avoid "Data contamination": Absolutely ensure the test set is not in the training data.  
- **Pipeline:**  
  1. Prepare Dataset (normalize to formats like Alpaca/ChatML).  
  2. Setup Config (use Unsloth + TRL, set parameters $r=16, \alpha=32$).  
  3. Train with `SFTTrainer` (use cosine schedule, monitor loss).  
  4. Evaluate (monitor eval loss to detect overfitting).  
  5. Merge & Deploy (merge adapters and convert to GGUF format for running on vLLM or llama.cpp).  

---

## 6. Lab 21: Fine-tuning Practice  

- **Objective:** Fine‑tune the Qwen2.5‑7B model with LoRA/QLoRA on a custom Vietnamese dataset (using the `Unsloth` + `TRL` libraries).  
- **Task:** Run rank experiments with $r=8$ and $r=64$. Extract an evaluation report (perplexity table, qualitative examples) to compare the trade‑off between training cost and final quality. Choose the rank that gives the best ROI.  

---

## Links  

- [[day21_track1]] – AI Evaluation  
- [[day21_track2]] – CI/CD AI Systems  
- [[day22_track3]] – DPO/ORPO Alignment  
- [[day21_overview]] – Overview

---

### Day 21 Review Questions

1. According to the lecture, in standard procedures, when should one switch to Fine-tuning instead of continuing with Prompt Engineering and RAG?
   - A. When new knowledge needs to be added to the model.
   - B. When Prompt Engineering and RAG have maxed out but the model still lacks specialized formatting or needs reduced latency/cost at scale.
   - C. When the number of requests is under 50k per day.
   - D. When the dataset has over 10k samples.

2. How does LoRA differ from Full Fine-tuning?
   - A. LoRA updates all parameters of the original model.
   - B. LoRA freezes the original weights and only trains two small matrices A and B (low-rank).
   - C. LoRA increases inference latency due to computing additional matrices.
   - D. LoRA requires more VRAM than Full Fine-tuning.

3. What technique combination allows QLoRA to fine-tune a 7B model on a 24GB GPU?
   - A. Only using Gradient Checkpointing and FlashAttention.
   - B. Quantizing the original model down to 4-bit (NF4) and using bf16 LoRA adapters, combined with PagedAdamW.
   - C. Reducing LoRA rank to r=1.
   - D. Compressing the entire model down to 2-bit.

4. According to the lecture, which of the following is true regarding Datasets when fine-tuning?
   - A. Sample quantity is more important than quality; 10k noisy samples are better than 500 clean ones.
   - B. Ensure the test set is not in the training set to avoid "Data contamination".
   - C. Just 100 samples are enough for any task.
   - D. The original model's test set can be reused without checking for duplicates.
