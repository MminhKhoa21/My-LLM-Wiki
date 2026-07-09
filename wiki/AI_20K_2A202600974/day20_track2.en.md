---
type: summary
title: "Day 20 Track 2: Model Serving & Inference Optimization"
description: "A deep dive into modern LLM serving infrastructure, quantization, KV cache optimization, and inference scaling strategies."
tags: [day20, track2, model-serving, inference, quantization, vLLM, SGLang, paged-attention]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/20/1-day20-model-serving-inference-optimization.pdf"]
---
# Day 20 Track 2: Model Serving & Inference Optimization

## 1. Overview

This module explores AI infrastructure for production, specifically focusing on how to serve Large Language Models (LLMs) with high throughput, low latency, and efficient memory utilization.

## 2. Latency Metrics and Goodput

Understanding latency is critical for user experience in LLMs.

* **TTFT (Time To First Token):** Time from request to the first generated token (depends on prefill compute and queue wait).

* **TPOT (Time Per Output Token):** Time between each generated token.

* **Throughput vs Goodput:** Throughput is total tokens/s at saturation, whereas **Goodput@SLO** is the request rate that satisfies specific TTFT and TPOT Service Level Objectives (SLOs). Goodput is the most important production metric.

## 3. Quantization

Quantization reduces the precision of model weights to save VRAM and increase throughput.

* **FP16 / BF16:** Baseline precision.

* **FP8:** <1% quality drop, halves memory (native on Hopper GPUs).

* **AWQ (4-bit):** High quality for heavily constrained environments (ideal for 8B+ models).

* **GGUF (Q4_K_M):** Recommended for CPU/Edge inference.

* **NVFP4:** Blackwell native format, extremely fast with minimal loss.

## 4. Attention Optimization & KV Cache

* **PagedAttention:** Treats KV cache like virtual memory pages to eliminate memory fragmentation, enabling continuous batching and yielding up to 24x throughput gains compared to naive Hugging Face Transformers.

* **FlashAttention (v1-v4):** IO-aware attention that optimizes HBM read/writes by tiling data in SRAM, supporting long contexts without OOM.

* **MLA (Multi-Latent Attention):** Used in architectures like DeepSeek-V3 to compress KV caches, using 10x less memory than standard Multi-Head Attention (MHA).

* **Prefix Caching:** RadixAttention (SGLang) and Automatic Prefix Caching (vLLM) cache shared system prompts across requests, massively reducing TTFT.

## 5. Inference Serving Stack 2026

Key engines for production serving:

* **vLLM:** The industry standard, featuring PagedAttention and automatic prefix caching.

* **SGLang:** Highly optimized for multi-turn and structured generation via RadixAttention.

* **TensorRT-LLM:** NVIDIA's native optimized backend.

* **llama.cpp / Ollama:** Ideal for local CPU/GPU/Apple Metal execution.

* **NVIDIA Dynamo & llm-d:** Disaggregated prefill/decode orchestrators for large-scale multi-tenant clouds.

## 6. Advanced Parallelism and Scaling

* **Disaggregated Serving:** Separating compute into Prefill Pools and Decode Pools to prevent long context prompts from blocking generation tasks.

* **Parallelism Strategies:**

  * **TP (Tensor Parallelism):** Splitting layers across GPUs within a node.

  * **PP (Pipeline Parallelism):** Splitting layers across nodes for ultra-long context.

  * **EP (Expert Parallelism):** Routing tokens to specific MoE experts.

  * **DP (Data Parallelism):** Replicating the model across instances.

* **Speculative Decoding:** Using a smaller draft model to generate tokens and a larger model to verify, speeding up generation in memory-bound setups.

## 7. Power and Sustainability

* **Tokens-per-Joule:** Energy efficiency is a primary bottleneck. Median cost is ~0.31Wh/query. Reasoning models consume significantly more energy.

## 8. Multi-modal and Embedding Serving

* **Multimodal (VLM):** TTFT becomes a function of image/video size. Encoding vision tokens is decoupled from the prefill/decode phases.

* **Semantic Caching:** Caching responses based on embedding similarity to bypass full inference.

---

### Day 20 Review Questions

1. **Which of the following metrics is considered the most important in production because it reflects the ability to meet Service Level Objectives (SLO)?**  
   - A. TTFT (Time To First Token)  
     *A. TTFT (Time To First Token)*  
   - B. TPOT (Time Per Output Token)  
     *B. TPOT (Time Per Output Token)*  
   - C. Throughput (total tokens/second)  
   - D. Goodput@SLO (the rate of requests meeting the TTFT and TPOT SLOs)  
   **Answer:** D  

2. **Which quantization technique is recommended for CPU/Edge inference environments and uses the Q4_K_M format?**  
   - A. FP8  
     *A. FP8*  
   - B. AWQ (4-bit)  
     *B. AWQ (4-bit)*  
   - C. GGUF  
     *C. GGUF*  
   - D. NVFP4  
     *D. NVFP4*  
   **Answer:** C  

3. **Which of the following statements about PagedAttention is true?**  
   - A. It only works on GPT architectures and doesn't support other models.  
   - B. It eliminates KV cache memory fragmentation and enables continuous batching, increasing throughput by up to 24x.  
   - C. It is a KV cache compression method by projecting into the latent space.  
   - D. It requires specialized hardware (NVIDIA Hopper) and cannot run on older generation GPUs.  
   **Answer:** B  

4. **Among parallelization strategies, which technique separates the prefill and decode phases into separate pools to avoid bottlenecks caused by long prompts?**  
   - A. Tensor Parallelism (TP)  
     *A. Tensor Parallelism (TP)*  
   - B. Pipeline Parallelism (PP)  
     *B. Pipeline Parallelism (PP)*  
   - C. Expert Parallelism (EP)  
     *C. Expert Parallelism (EP)*  
   - D. Disaggregated Serving  
     *D. Disaggregated Serving*  
   **Answer:** D
