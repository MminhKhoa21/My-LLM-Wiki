---
type: summary
title: "Day 21 – Track 3: Fine-tuning LLMs (LoRA/QLoRA)"
description: "Khi nào cần fine-tune LLM, cơ chế LoRA và QLoRA, kiến trúc FlashAttention, pipeline huấn luyện và thực hành."
tags: [ai, 20k, day21, track3, fine-tuning, lora, qlora, flashattention]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/day06-fine-tuning-llms-tu-full-fine-tune-en-loraqlora.pdf"]
---
Dưới đây là nội dung file `day21_track3.md` đã được hoàn thiện theo yêu cầu song ngữ Anh - Việt, với mỗi đoạn/câu/bullet được trình bày liền kề (tiếng Anh trước, tiếng Việt sau) và giữ nguyên định dạng Markdown.

---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]  
> **Track:** [[track3_ai_app|Track 3: AI Application]]

**Track:** [[track3_ai_app|Track 3: AI Application]]  
**Lộ trình:** [[track3_ai_app|Track 3: AI Application]]

# Day 21 – Track 3: Fine-tuning LLMs – From Full Fine-tune to LoRA/QLoRA  
# Ngày 21 – Track 3: Fine-tuning LLMs – Từ Full Fine-tune đến LoRA/QLoRA

**Giảng viên**: Nguyễn Khánh Linh (VinUniversity)  
**Instructor**: Nguyễn Khánh Linh (VinUniversity)  

**Khóa**: AICB Phase 2 · Track 3 · Ngày 21  
**Course**: AICB Phase 2 · Track 3 · Day 21  

---

## 1. When to Fine-tune?  
## 1. Khi nào cần Fine-tune?

With Frontier Models (GPT-4o, Claude 3.5, Gemini 2) in 2025-2026, over 80% of tasks can already be solved well.  
*Với các Frontier Models (GPT-4o, Claude 3.5, Gemini 2) năm 2025-2026, hơn 80% tasks đã có thể được giải quyết tốt.*

- **Standard workflow:** Prompt Engineering → RAG → Fine-tune.  
  **Quy trình chuẩn:** Prompt Engineering → RAG → Fine-tune.  
- **When to fine-tune?:** When prompt and RAG are exhausted but the model still lacks a custom format, domain jargon, or when you need to reduce latency/cost at large scale (volume > 50k req/day).  
  **Khi nào fine-tune?:** Khi prompt và RAG đã hết sức nhưng mô hình vẫn thiếu format riêng, domain jargon (từ ngữ chuyên ngành), hoặc cần giảm latency / cost ở scale lớn (volume > 50k req/day).  
- **Critical note:** Fine-tuning is **NOT** for adding new knowledge (knowledge gaps). Use RAG to supply knowledge. Fine-tuning is mainly for adjusting **style and format**.  
  **Lưu ý cực quan trọng:** Fine-tune **KHÔNG** dùng để thêm kiến thức mới (knowledge gaps). Hãy dùng RAG để cấp kiến thức. Fine-tune chủ yếu để chỉnh **style và format**.

---

## 2. LoRA (Low-Rank Adaptation)  
## 2. LoRA (Low-Rank Adaptation)

Instead of updating all parameters (Full Fine-tune) which is very VRAM‑expensive, LoRA freezes the base weights and only trains the delta $\Delta W$ via two low‑rank matrices $A$ and $B$.  
*Thay vì cập nhật toàn bộ tham số (Full Fine-tune) tốn kém rất nhiều VRAM, LoRA đóng băng (freeze) base weights và chỉ huấn luyện thêm phần chênh lệch $\Delta W$ thông qua hai ma trận nhỏ (low-rank) $A$ và $B$.*

- Formula: $h = W_0 x + B \cdot A \cdot x$  
  *Công thức:* $h = W_0 x + B \cdot A \cdot x$  
- $A$ and $B$ have rank $r \ll d$ (typically $r \in \{8, 16, 32, 64\}$). Only about 1% of parameters need training compared to Full FT.  
  *$A$ và $B$ có kích thước rank $r \ll d$ (thường $r \in \{8, 16, 32, 64\}$). Chỉ mất khoảng 1% tham số cần train so với Full FT.*  
- **Inference:** When deployed, matrices A and B are merged directly into $W_0$, so inference speed remains unchanged (zero added latency).  
  *Inference: Khi deploy, ma trận A và B được gộp (merge) thẳng vào $W_0$, giúp tốc độ inference không thay đổi (zero added latency).*

---

## 3. QLoRA – Fine-tune on Small GPUs  
## 3. QLoRA – Fine-tune trên GPU nhỏ

Combines 4‑bit quantization (NF4) of the base model with bf16 LoRA adapters.  
*Kết hợp quantization 4-bit (NF4) của base model và bộ điều chỉnh bf16 LoRA adapters.*

- Allows training large models (e.g., 7B) on a single consumer GPU (e.g., RTX 3090 24GB).  
  *Cho phép huấn luyện mô hình lớn (vd: 7B) trên một GPU consumer thông thường (như RTX 3090 24GB).*  
- Uses **PagedAdamW** to offload optimizer states to CPU RAM when VRAM is insufficient.  
  *Sử dụng **PagedAdamW** để offload optimizer states sang CPU RAM khi thiếu VRAM.*  
- **Multi-tenant:** You can host one base model and attach multiple different LoRA adapters simultaneously for different clients or tasks.  
  *Multi-tenant: Có thể host 1 base model và gắn nhiều LoRA adapters khác nhau cùng lúc cho từng khách hàng hoặc từng task riêng biệt.*

---

## 4. FlashAttention & Memory Optimization  
## 4. FlashAttention & Tối ưu bộ nhớ

- **FlashAttention 2:** An IO‑Aware Exact Attention technique. Vanilla attention reads/writes through HBM (very slow); FlashAttention uses tiling to compute in SRAM (10x faster). It accelerates training by 2‑4x and drastically reduces activation memory. Should be enabled during training.  
  *FlashAttention 2: Kỹ thuật IO-Aware Exact Attention. Vanila attention ghi và đọc qua bộ nhớ HBM (rất chậm), FlashAttention thực hiện chia khối tính toán ("tiling"), đưa vào SRAM (nhanh hơn 10x). Giúp tăng tốc 2-4x và giảm mạnh bộ nhớ activations. Bắt buộc nên bật khi huấn luyện.*  
- **Gradient Checkpointing:** Recomputes activations during backward pass instead of storing them, saving up to 60% VRAM (at the cost of ~20% extra training time).  
  *Gradient Checkpointing: Tính toán lại (recompute) activations trong quá trình backward thay vì lưu trữ sẵn trên bộ nhớ, giúp tiết kiệm đến 60% VRAM (chỉ đổi lại tốn thêm ~20% thời gian train).*  
- **Sequence Packing:** Packs multiple small samples into one long sequence to double throughput (set `packing=True` in the library).  
  *Sequence Packing: Gộp nhiều mẫu nhỏ thành 1 chuỗi dài để tăng throughput lên x2 (cấu hình `packing=True` trong thư viện).*

---

## 5. Dataset & Training Pipeline  
## 5. Dataset & Training Pipeline

- **Dataset:** Quality matters more than quantity. 500 perfect samples are better than 10k noisy ones.  
  *Dataset: Chất lượng quan trọng hơn số lượng. 500 mẫu hoàn hảo tốt hơn 10k mẫu nhiễu.*  
- Avoid "Data contamination": Absolutely ensure the test set is not in the training data.  
  *Chống "Data contamination": Tuyệt đối đảm bảo tập test không nằm trong training data.*  
- **Pipeline:**  
  1. Prepare Dataset (normalize to formats like Alpaca/ChatML).  
     *Chuẩn bị Dataset (chuẩn hóa về format như Alpaca/ChatML).*  
  2. Setup Config (use Unsloth + TRL, set parameters $r=16, \alpha=32$).  
     *Cấu hình (dùng Unsloth + TRL, đặt các tham số $r=16, \alpha=32$).*  
  3. Train with `SFTTrainer` (use cosine schedule, monitor loss).  
     *Huấn luyện với `SFTTrainer` (sử dụng cosine schedule, theo dõi loss).*  
  4. Evaluate (monitor eval loss to detect overfitting).  
     *Đánh giá (monitor eval loss để phát hiện overfitting).*  
  5. Merge & Deploy (merge adapters and convert to GGUF format for running on vLLM or llama.cpp).  
     *Merge & Deploy (gộp adapters và convert sang định dạng GGUF chạy trên vLLM hoặc llama.cpp).*

---

## 6. Lab 21: Fine-tuning Practice  
## 6. Lab 21: Thực hành Fine-tune

- **Objective:** Fine‑tune the Qwen2.5‑7B model with LoRA/QLoRA on a custom Vietnamese dataset (using the `Unsloth` + `TRL` libraries).  
  *Mục tiêu: Fine-tune mô hình Qwen2.5-7B với LoRA/QLoRA trên tập dữ liệu tiếng Việt tùy chỉnh (sử dụng thư viện `Unsloth` + `TRL`).*  
- **Task:** Run rank experiments with $r=8$ and $r=64$. Extract an evaluation report (perplexity table, qualitative examples) to compare the trade‑off between training cost and final quality. Choose the rank that gives the best ROI.  
  *Nhiệm vụ: Chạy rank experiment với $r=8$ và $r=64$. Trích xuất evaluation report (bảng perplexity, qualitive examples) để so sánh trade-off giữa training cost và chất lượng cuối cùng. Chọn rank cho ROI tốt nhất.*

---

## Links  
## Liên kết

- [[day21_track1]] – AI Evaluation  
  [[day21_track1]] – Đánh giá AI  
- [[day21_track2]] – CI/CD AI Systems  
  [[day21_track2]] – Hệ thống CI/CD AI  
- [[day22_track3]] – DPO/ORPO Alignment  
  [[day22_track3]] – Căn chỉnh DPO/ORPO  
- [[day21_overview]] – Overview  
  [[day21_overview]] – Tổng quan
