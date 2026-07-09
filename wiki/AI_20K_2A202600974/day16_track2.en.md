---
type: summary
title: "Day 16 Track 2: Cloud Infrastructure for AI"
description: "Hạ tầng Cloud cho các hệ thống AI: Lựa chọn Provider, GPU, Terraform, K8s và AI Serving"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/1-Day 16_ Track 2_ Cloud infrastructure for AI.pptx"]
---

# Cloud Infrastructure for AI  

*This content focuses on cloud infrastructure architecture for deploying AI models and applications optimized for cost and performance.*

## 1. Comparing Cloud Providers for AI  

  *AWS: Broad ecosystem (Bedrock, SageMaker), suitable for enterprise compliance needs.*  
  *GCP: Strong in PyTorch/JAX, offers TPU v5p and GKE GPU auto-provisioning.*  
  *Azure: Exclusive OpenAI services, Microsoft stack.*  
  *Vietnamese Cloud (Viettel, VNG, FPT): Compliant with Decree 13/PDPD on data residency, low cost (60-70% of global) but lack H100/H200.*  
  *Specialized GPU Clouds (Lambda, RunPod, CoreWeave, GMI Cloud): Very low cost (e.g., GMI Cloud H100 at $2.10/hr), saves 40-70% but requires operational skills (infra skills) and fewer managed services.*

## 2. Cloud Foundation cho AI  
## 2. Cloud Foundation for AI  

  *Models:*  
    *AI-aaS (OpenAI API, Vertex AI): Fast, no infrastructure needed.*  
    *PaaS (SageMaker, Azure ML): Managed scaling, less Ops.*  
    *IaaS (EC2 GPU, GCE): Full control, requires Ops.*  
  *Hybrid Strategy: Training on IaaS (to optimize cost), Serving on PaaS (to scale easily).*

## 3. GPU Selection & Cost Optimization  

  *Inference: Use T4, L40S, A10G (e.g., L40S is a "sleeper pick", $0.40-$0.86/hr, optimized for small-to-medium models).*  
  *Fine-tuning: Use A100 ($1.79-$2.70/hr).*  
  *Pre-training: Use H100, H200 Cluster (H200 has 141GB HBM3e, new standard for 2026).*  
  *Cost Optimization: Use Spot/Preemptible instances for training (save 60-70%), Reserved instances for serving. Use MIG (Multi-Instance GPU) to partition GPUs for multiple small models.*

## 4. Terraform & Kubernetes cho AI  
## 4. Terraform & Kubernetes for AI  

  *Terraform IaC: Manage infrastructure as code (GPU instances, VPC, Security Groups) with S3 backend, split workspaces (dev/staging/prod). Consider alternatives like Pulumi, OpenTofu.*  
- **Docker & K8s**:  
  *Docker & K8s:*  
    *Optimize Docker image with multi-stage build (reduce from 18GB to 6-8GB).*  
    *Use NVIDIA GPU Operator for automatic driver installation.*  
    *Karpenter (AWS) / NAP (GCP) help auto-provision GPU nodes and scale-to-zero to save costs during off-peak hours.*  
    *Kubernetes configuration: Requests = Limits for GPU (nvidia.com/gpu: 1), use Init container to load model weights from S3.*

## 5. Agent Infrastructure & AI Serving Stack  
## 5. Agent Infrastructure & AI Serving Stack  

  *8 Layers of Production AI Agent: Compute (GPU/CPU/Serverless) -> Orchestration -> Message Queue -> Cache -> Storage -> Networking -> Observability -> Secrets & Config.*  
- **AI Serving Engines (2026)**:  
  *AI Serving Engines (2026):*  
    *vLLM: PagedAttention, wide ecosystem, easy to deploy.*  
    *SGLang: RadixAttention (reuses KV cache), optimized for Agent/Multi-turn chat (20% performance boost).*  
    *LMDeploy: TurboMind engine (C++ zero overhead), 1.8x throughput of vLLM, ideal for latency-sensitive apps.*

---

### Day 16 Review Questions

1. **According to the Hybrid Cloud strategy for AI, which of the following combinations is recommended to optimize both cost and scalability?**  
   - A. Using PaaS for both Training and Serving  
   - B. Using IaaS for Training and PaaS for Serving  
   - C. Using AI-aaS for Training and IaaS for Serving  
   - D. Using PaaS for Training and IaaS for Serving  
   **Answer:** B  

2. **Which GPU is described as a "sleeper pick" for Inference tasks at $0.40-$0.86/hour?**  
   - A. A100  
     *A. A100*  
   - B. H100  
     *B. H100*  
   - C. L40S  
     *C. L40S*  
   - D. T4  
     *D. T4*  
   **Answer:** C  

3. **Which solution helps reduce AI model training costs on the cloud by 60-70%?**  
   - A. Using Reserved Instances  
   - B. Using Spot/Preemptible Instances  
   - C. Using On-Demand Instances  
   - D. Using Dedicated Hosts  
   **Answer:** B  

4. **In Kubernetes, to manage GPU resources for AI workloads, which of the following configurations is correct?**  
   - A. Setting requests smaller than limits for GPUs  
   - B. Using `nvidia.com/gpu` with requests = limits  
   - C. No need to specify resource requests for GPUs  
   - D. Using `cpu` and `memory` instead of GPU resources  
   **Answer:** B  

5. **Which serving engine uses RadixAttention to reuse KV cache, optimizing for Agents and Multi-turn chat?**  
   - A. vLLM  
     *A. vLLM*  
   - B. SGLang  
     *B. SGLang*  
   - C. LMDeploy  
     *C. LMDeploy*  
   - D. TensorRT-LLM  
     *D. TensorRT-LLM*  
   **Answer:** B
