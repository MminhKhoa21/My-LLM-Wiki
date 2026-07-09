---
type: summary
title: "Day 25 Track 2: GPU FinOps & Cost Optimization"
description: "A comprehensive guide to optimizing GPU cloud costs, utilizing spot instances, right-sizing workloads, and inference cost reduction techniques."
tags: [FinOps, GPU, cost-optimization, inference, LLMOps]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/25/Day25 - Track 2 - Gpu-finops-cost-optimization.pdf"]
---

# Day 25 Track 2: GPU FinOps & Cost Optimization  

This document summarizes the strategies for managing and optimizing GPU costs (FinOps) in production AI environments, covering everything from instance selection to advanced inference optimization.  

## 1. GPU Cloud Cost Anatomy  

Cost is not just the hourly rate of the GPU.  

- **Hidden Costs**: Data transfer (egress), NAT gateway, secrets management.  
- **Wasted Spend**: Idle GPUs overnight, over-provisioned instances, unused reserved capacity, and development environments left running 24/7.  

*Rule of Thumb: A GPU utilization < 30% indicates an immediate need for right-sizing.*  

## 2. Spot & Preemptible Instances  

Spot instances can provide 60-70% discounts but require graceful handling of interruptions.  

- **Mixed Fleet Strategy**: 20% on-demand (baseline) and 80% spot instances (burst) to balance cost and reliability.  
- **Checkpoint Strategy**: Save model state frequently (e.g., every epoch or 30 mins) to S3/GCS. If a spot instance is terminated, a new instance can resume from the checkpoint seamlessly.  

## 3. Right-Sizing & Utilization  

Optimizing utilization requires tracking the right metrics:  

- **GPU Utilization**: Checks if the GPU is idle.  
- **MFU (Model FLOPs Utilization)**: Tracks compute-bound tasks (e.g., training, prefill).  
- **MBU (Memory Bandwidth Utilization)**: Tracks memory-bound tasks (e.g., decoding, serving).  

### Multi-Model Serving & MIG (Multi-Instance GPU)  

To improve low utilization on large GPUs (e.g., A100), use MIG to isolate instances or implement multi-model serving to swap models dynamically based on requests.  

## 4. Inference Cost Optimization  

Advanced levers to reduce cost per token:  

- **Request Batching**: Grouping requests significantly increases throughput and drops cost.  
- **Caching**: Use Redis or Semantic caching to reuse previous prompt responses (30-40% hit rate).  
- **Model Cascading**: Use a smaller, cheaper model (e.g., Llama-3-8B) for 80% of queries and route only complex queries to larger models.  
- **Quantization**: Formats like AWQ 4-bit can reduce cost per token drastically.  
- **Disaggregated Serving**: Separate prefill (compute-heavy) and decode (memory-heavy) onto separate GPU clusters to prevent bottlenecks.  
- **Chunked Prefilling & Speculative Decoding**: Balance TTFT (Time To First Token) and ITL (Inter-Token Latency).  
- **KV Cache & Prefix Caching**: Reuse KV memory for shared prefixes to speed up TTFT for identical system prompts.  

## 5. Cost Allocation & Chargeback  

Establish clear tagging strategies (`team`, `project`, `env`) enforced by SCP/OPA policies. Utilize tools like Kubecost to breakdown per-pod costs, ensuring each team has a designated budget and transparent dashboard.  

## 6. Sustainable AI: Carbon & Energy  

Optimization also reduces carbon footprint. Pick green cloud regions (e.g., hydro-powered data centers) and use distilled, smaller models when feasible. Track carbon emissions alongside performance metrics (e.g., `CodeCarbon`).

---

### Day 25 Review Questions

1. **According to the lecture, which sign indicates that immediate GPU right-sizing is needed?**  
   - A. GPU utilization < 50%  
     *A. GPU utilization < 50%*  
   - B. GPU utilization < 30%  
     *B. GPU utilization < 30%*  
   - C. MFU < 50%  
     *C. MFU < 50%*  
   - D. MBU < 30%  
     *D. MBU < 30%*  
   **Answer:** B  

2. **Which strategy helps leverage spot instances for a 60-70% cost reduction while still ensuring reliability?**  
   - A. Using 100% spot instances only  
   - B. Mixed Fleet Strategy: 20% on-demand + 80% spot, combined with frequent checkpointing  
   - C. Using on-demand for training and spot for inference  
   - D. Using reserved instances instead of spot  
   **Answer:** B  

3. **To monitor GPU performance, which metric is particularly important for compute-bound tasks (e.g., training, prefill)?**  
   - A. GPU Utilization  
     *A. GPU Utilization*  
   - B. MBU (Memory Bandwidth Utilization)  
     *B. MBU (Memory Bandwidth Utilization)*  
   - C. MFU (Model FLOPs Utilization)  
     *C. MFU (Model FLOPs Utilization)*  
   - D. Cache hit rate  
     *D. Cache hit rate*  
   **Answer:** C  

4. **Which inference optimization technique helps reduce per-token cost by using smaller models for most simple queries?**  
   - A. Request Batching  
     *A. Request Batching*  
   - B. Caching  
     *B. Caching*  
   - C. Model Cascading  
     *C. Model Cascading*  
   - D. Disaggregated Serving  
     *D. Disaggregated Serving*  
   **Answer:** C  

5. **To allocate GPU costs to teams (chargeback), which strategy does the lecture recommend?**  
   - A. Calculating an average cost for all teams  
   - B. Setting up tagging (team, project, env) and using Kubecost for analysis  
   - C. Using a single undivided cloud account  
   - D. Only tracking total monthly costs  
   **Answer:** B
