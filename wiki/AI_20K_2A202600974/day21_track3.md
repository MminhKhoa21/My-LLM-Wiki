---
type: summary
title: "Day 21 – Track 3: Fine-tuning LLMs (LoRA/QLoRA)"
description: "Khi nào cần fine-tune LLM, cơ chế LoRA và QLoRA, pipeline huấn luyện và thực hành."
tags: [ai, 20k, day21, track3, fine-tuning, lora, qlora]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/day06-fine-tuning-llms-tu-full-fine-tune-en-loraqlora.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# Day 21 – Track 3: Fine-tuning LLMs – Từ Full Fine-tune đến LoRA/QLoRA

**Giảng viên**: Nguyễn Khánh Linh (VinUniversity)  
**Khóa**: AICB Phase 2 · Track 3 · Ngày 21

---

## Khi nào cần Fine-tune?

Trong bối cảnh 2025–2026, frontier models (GPT-4o, Claude 3.5, Gemini 2) đã đủ tốt cho 80%+ tasks. Quy trình quyết định:

```
Prompt Engineering → (không đủ?) → RAG → (vẫn thiếu?) → Fine-tune
```

**Fine-tune CHỈ khi thực sự cần**: format riêng, domain jargon, giảm cost at scale.  
⚠️ Fine-tune **KHÔNG fix knowledge gaps** – dùng RAG cho knowledge. Fine-tune fix **style và format**.

---

## LoRA – Low-Rank Adaptation

Thay vì update toàn bộ weights (rất tốn VRAM), LoRA thêm 2 ma trận nhỏ **A** và **B** (rank thấp) vào mỗi lớp attention:

$$W' = W + \Delta W = W + A \cdot B$$

- **A**: shape `(d, r)`, **B**: shape `(r, d)`, với r ≪ d  
- Chỉ train A và B → giảm số params cần train từ hàng tỷ xuống hàng triệu  
- Model gốc đóng băng → tránh catastrophic forgetting

---

## QLoRA – Quantized LoRA

QLoRA kết hợp LoRA với **quantization 4-bit (NF4)**, cho phép fine-tune model 7-13B trên GPU consumer (RTX 3090, 4090):

- Quantize base model xuống 4-bit → giảm VRAM 75%  
- Dequantize khi compute, gradient chảy qua LoRA adapters  
- Dùng **bitsandbytes** + **peft** library

---

## Dataset & Training Pipeline

1. Thu thập instruction dataset (format: system / user / assistant)  
2. Tokenize & pack sequences  
3. Cấu hình LoRA (r, alpha, target modules)  
4. Train với `SFTTrainer` (TRL library)  
5. Merge adapter vào base model  
6. Evaluate bằng benchmark

---

## Liên kết
- [[day21_track1]] – AI Evaluation
- [[day22_track3]] – DPO/ORPO Alignment (tiếp nối Fine-tuning)
- [[day21_overview]]
