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

**Lộ trình:** [[track3_ai_app|Track 3: AI Application]]

# Ngày 21 – Track 3: Fine-tuning LLMs – Từ Full Fine-tune đến LoRA/QLoRA

**Giảng viên**: Nguyễn Khánh Linh (VinUniversity)  
**Instructor**: Nguyễn Khánh Linh (VinUniversity)  

**Khóa**: AICB Phase 2 · Track 3 · Ngày 21  

---

## 1. Khi nào cần Fine-tune?

*Với các Frontier Models (GPT-4o, Claude 3.5, Gemini 2) năm 2025-2026, hơn 80% tasks đã có thể được giải quyết tốt.*

  **Quy trình chuẩn:** Prompt Engineering → RAG → Fine-tune.  
  **Khi nào fine-tune?:** Khi prompt và RAG đã hết sức nhưng mô hình vẫn thiếu format riêng, domain jargon (từ ngữ chuyên ngành), hoặc cần giảm latency / cost ở scale lớn (volume > 50k req/day).  
  **Lưu ý cực quan trọng:** Fine-tune **KHÔNG** dùng để thêm kiến thức mới (knowledge gaps). Hãy dùng RAG để cấp kiến thức. Fine-tune chủ yếu để chỉnh **style và format**.

---


*Thay vì cập nhật toàn bộ tham số (Full Fine-tune) tốn kém rất nhiều VRAM, LoRA đóng băng (freeze) base weights và chỉ huấn luyện thêm phần chênh lệch $\Delta W$ thông qua hai ma trận nhỏ (low-rank) $A$ và $B$.*

  *Công thức:* $h = W_0 x + B \cdot A \cdot x$  
  *$A$ và $B$ có kích thước rank $r \ll d$ (thường $r \in \{8, 16, 32, 64\}$). Chỉ mất khoảng 1% tham số cần train so với Full FT.*  
  *Inference: Khi deploy, ma trận A và B được gộp (merge) thẳng vào $W_0$, giúp tốc độ inference không thay đổi (zero added latency).*

---

## 3. QLoRA – Fine-tune trên GPU nhỏ

*Kết hợp quantization 4-bit (NF4) của base model và bộ điều chỉnh bf16 LoRA adapters.*

  *Cho phép huấn luyện mô hình lớn (vd: 7B) trên một GPU consumer thông thường (như RTX 3090 24GB).*  
  *Sử dụng **PagedAdamW** để offload optimizer states sang CPU RAM khi thiếu VRAM.*  
  *Multi-tenant: Có thể host 1 base model và gắn nhiều LoRA adapters khác nhau cùng lúc cho từng khách hàng hoặc từng task riêng biệt.*

---

## 4. FlashAttention & Tối ưu bộ nhớ

  *FlashAttention 2: Kỹ thuật IO-Aware Exact Attention. Vanila attention ghi và đọc qua bộ nhớ HBM (rất chậm), FlashAttention thực hiện chia khối tính toán ("tiling"), đưa vào SRAM (nhanh hơn 10x). Giúp tăng tốc 2-4x và giảm mạnh bộ nhớ activations. Bắt buộc nên bật khi huấn luyện.*  
  *Gradient Checkpointing: Tính toán lại (recompute) activations trong quá trình backward thay vì lưu trữ sẵn trên bộ nhớ, giúp tiết kiệm đến 60% VRAM (chỉ đổi lại tốn thêm ~20% thời gian train).*  
  *Sequence Packing: Gộp nhiều mẫu nhỏ thành 1 chuỗi dài để tăng throughput lên x2 (cấu hình `packing=True` trong thư viện).*

---


  *Dataset: Chất lượng quan trọng hơn số lượng. 500 mẫu hoàn hảo tốt hơn 10k mẫu nhiễu.*  
  *Chống "Data contamination": Tuyệt đối đảm bảo tập test không nằm trong training data.*  
     *Chuẩn bị Dataset (chuẩn hóa về format như Alpaca/ChatML).*  
     *Cấu hình (dùng Unsloth + TRL, đặt các tham số $r=16, \alpha=32$).*  
     *Huấn luyện với `SFTTrainer` (sử dụng cosine schedule, theo dõi loss).*  
     *Đánh giá (monitor eval loss để phát hiện overfitting).*  
     *Merge & Deploy (gộp adapters và convert sang định dạng GGUF chạy trên vLLM hoặc llama.cpp).*

---

## 6. Lab 21: Thực hành Fine-tune

  *Mục tiêu: Fine-tune mô hình Qwen2.5-7B với LoRA/QLoRA trên tập dữ liệu tiếng Việt tùy chỉnh (sử dụng thư viện `Unsloth` + `TRL`).*  
  *Nhiệm vụ: Chạy rank experiment với $r=8$ và $r=64$. Trích xuất evaluation report (bảng perplexity, qualitive examples) để so sánh trade-off giữa training cost và chất lượng cuối cùng. Chọn rank cho ROI tốt nhất.*

---

## Liên kết

  [[day21_track1]] – Đánh giá AI  
  [[day21_track2]] – Hệ thống CI/CD AI  
  [[day22_track3]] – Căn chỉnh DPO/ORPO  
  [[day21_overview]] – Tổng quan
