---
type: summary
title: "Day 16 Track 2: Cloud Infrastructure for AI"
description: "Hạ tầng Cloud cho các hệ thống AI: Lựa chọn Provider, GPU, Terraform, K8s và AI Serving"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/1-Day 16_ Track 2_ Cloud infrastructure for AI.pptx"]
---
> **Lộ trình:** [[track2_ai_engineer]]

# Cloud Infrastructure for AI  
# Hạ tầng Đám mây cho AI  

Nội dung tập trung vào kiến trúc hạ tầng đám mây (Cloud) để triển khai các mô hình và ứng dụng AI tối ưu về chi phí và hiệu suất.  
*This content focuses on cloud infrastructure architecture for deploying AI models and applications optimized for cost and performance.*

## 1. So sánh Cloud Providers cho AI  
## 1. Comparing Cloud Providers for AI  

- **AWS**: Hệ sinh thái rộng (Bedrock, SageMaker), phù hợp nhu cầu Enterprise compliance.  
  *AWS: Broad ecosystem (Bedrock, SageMaker), suitable for enterprise compliance needs.*  
- **GCP**: Mạnh về PyTorch/JAX, có TPU v5p và GKE GPU auto-provisioning.  
  *GCP: Strong in PyTorch/JAX, offers TPU v5p and GKE GPU auto-provisioning.*  
- **Azure**: Độc quyền dịch vụ OpenAI, Microsoft stack.  
  *Azure: Exclusive OpenAI services, Microsoft stack.*  
- **Vietnamese Cloud (Viettel, VNG, FPT)**: Đáp ứng NĐ13/PDPD về data residency, giá rẻ (60-70% global) nhưng thiếu H100/H200.  
  *Vietnamese Cloud (Viettel, VNG, FPT): Compliant with Decree 13/PDPD on data residency, low cost (60-70% of global) but lack H100/H200.*  
- **Specialized GPU Clouds (Lambda, RunPod, CoreWeave, GMI Cloud)**: Giá rất rẻ (ví dụ GMI Cloud H100 chỉ $2.10/hr), tiết kiệm 40-70% nhưng cần kỹ năng vận hành (infra skills) và ít managed services.  
  *Specialized GPU Clouds (Lambda, RunPod, CoreWeave, GMI Cloud): Very low cost (e.g., GMI Cloud H100 at $2.10/hr), saves 40-70% but requires operational skills (infra skills) and fewer managed services.*

## 2. Cloud Foundation cho AI  
## 2. Cloud Foundation for AI  

- **Mô hình**:  
  *Models:*  
  - **AI-aaS** (OpenAI API, Vertex AI): Nhanh, không cần hạ tầng.  
    *AI-aaS (OpenAI API, Vertex AI): Fast, no infrastructure needed.*  
  - **PaaS** (SageMaker, Azure ML): Managed scaling, ít Ops.  
    *PaaS (SageMaker, Azure ML): Managed scaling, less Ops.*  
  - **IaaS** (EC2 GPU, GCE): Full control, cần Ops.  
    *IaaS (EC2 GPU, GCE): Full control, requires Ops.*  
- **Chiến lược Hybrid**: Training bằng IaaS (để tối ưu chi phí), Serving bằng PaaS (để scale dễ dàng).  
  *Hybrid Strategy: Training on IaaS (to optimize cost), Serving on PaaS (to scale easily).*

## 3. Lựa chọn GPU & Tối ưu chi phí  
## 3. GPU Selection & Cost Optimization  

- **Inference**: Dùng T4, L40S, A10G (ví dụ: L40S là "sleeper pick", giá $0.40-$0.86/hr, tối ưu cho model vừa và nhỏ).  
  *Inference: Use T4, L40S, A10G (e.g., L40S is a "sleeper pick", $0.40-$0.86/hr, optimized for small-to-medium models).*  
- **Fine-tuning**: Dùng A100 ($1.79-$2.70/hr).  
  *Fine-tuning: Use A100 ($1.79-$2.70/hr).*  
- **Pre-training**: Dùng H100, H200 Cluster (H200 có 141GB HBM3e, chuẩn mực mới của 2026).  
  *Pre-training: Use H100, H200 Cluster (H200 has 141GB HBM3e, new standard for 2026).*  
- **Tối ưu chi phí**: Dùng Spot/Preemptible instances cho training (giảm 60-70%), Reserved instances cho serving. Sử dụng MIG (Multi-Instance GPU) để chia nhỏ GPU phục vụ nhiều model nhỏ.  
  *Cost Optimization: Use Spot/Preemptible instances for training (save 60-70%), Reserved instances for serving. Use MIG (Multi-Instance GPU) to partition GPUs for multiple small models.*

## 4. Terraform & Kubernetes cho AI  
## 4. Terraform & Kubernetes for AI  

- **Terraform IaC**: Quản lý infrastructure as code (GPU instances, VPC, Security Groups) với S3 backend, chia workspaces (dev/staging/prod). Cân nhắc các phương án như Pulumi, OpenTofu.  
  *Terraform IaC: Manage infrastructure as code (GPU instances, VPC, Security Groups) with S3 backend, split workspaces (dev/staging/prod). Consider alternatives like Pulumi, OpenTofu.*  
- **Docker & K8s**:  
  *Docker & K8s:*  
  - Tối ưu Docker image với multi-stage build (giảm từ 18GB xuống 6-8GB).  
    *Optimize Docker image with multi-stage build (reduce from 18GB to 6-8GB).*  
  - Sử dụng NVIDIA GPU Operator để tự cài đặt driver.  
    *Use NVIDIA GPU Operator for automatic driver installation.*  
  - Karpenter (AWS) / NAP (GCP) giúp auto-provision GPU node và scale-to-zero để tiết kiệm chi phí ngoài giờ cao điểm.  
    *Karpenter (AWS) / NAP (GCP) help auto-provision GPU nodes and scale-to-zero to save costs during off-peak hours.*  
  - Cấu hình Kubernetes: Requests = Limits cho GPU (nvidia.com/gpu: 1), dùng Init container để tải model weights từ S3.  
    *Kubernetes configuration: Requests = Limits for GPU (nvidia.com/gpu: 1), use Init container to load model weights from S3.*

## 5. Agent Infrastructure & AI Serving Stack  
## 5. Agent Infrastructure & AI Serving Stack  

- **8 Layers của Production AI Agent**: Compute (GPU/CPU/Serverless) -> Orchestration -> Message Queue -> Cache -> Storage -> Networking -> Observability -> Secrets & Config.  
  *8 Layers of Production AI Agent: Compute (GPU/CPU/Serverless) -> Orchestration -> Message Queue -> Cache -> Storage -> Networking -> Observability -> Secrets & Config.*  
- **AI Serving Engines (2026)**:  
  *AI Serving Engines (2026):*  
  - **vLLM**: PagedAttention, hệ sinh thái rộng, dễ deploy.  
    *vLLM: PagedAttention, wide ecosystem, easy to deploy.*  
  - **SGLang**: RadixAttention (tái sử dụng KV cache), tối ưu cho Agent/Multi-turn chat (tăng 20% hiệu năng).  
    *SGLang: RadixAttention (reuses KV cache), optimized for Agent/Multi-turn chat (20% performance boost).*  
  - **LMDeploy**: TurboMind engine (C++ zero overhead), throughput gấp 1.8x vLLM, lý tưởng cho latency-sensitive apps.  
    *LMDeploy: TurboMind engine (C++ zero overhead), 1.8x throughput of vLLM, ideal for latency-sensitive apps.*
