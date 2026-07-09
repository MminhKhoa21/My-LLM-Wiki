---
type: summary
title: "Day 16 Track 2: Cloud Infrastructure for AI"
description: "Hạ tầng Cloud cho các hệ thống AI: Lựa chọn Provider, GPU, Terraform, K8s và AI Serving"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/1-Day 16_ Track 2_ Cloud infrastructure for AI.pptx"]
---
> **Lộ trình:** [[track2_ai_engineer]]

# Hạ tầng Đám mây cho AI  

Nội dung tập trung vào kiến trúc hạ tầng đám mây (Cloud) để triển khai các mô hình và ứng dụng AI tối ưu về chi phí và hiệu suất.  

## 1. So sánh Cloud Providers cho AI  

- **AWS**: Hệ sinh thái rộng (Bedrock, SageMaker), phù hợp nhu cầu Enterprise compliance.  
- **GCP**: Mạnh về PyTorch/JAX, có TPU v5p và GKE GPU auto-provisioning.  
- **Azure**: Độc quyền dịch vụ OpenAI, Microsoft stack.  
- **Vietnamese Cloud (Viettel, VNG, FPT)**: Đáp ứng NĐ13/PDPD về data residency, giá rẻ (60-70% global) nhưng thiếu H100/H200.  
- **Specialized GPU Clouds (Lambda, RunPod, CoreWeave, GMI Cloud)**: Giá rất rẻ (ví dụ GMI Cloud H100 chỉ $2.10/hr), tiết kiệm 40-70% nhưng cần kỹ năng vận hành (infra skills) và ít managed services.  


- **Mô hình**:  
  - **AI-aaS** (OpenAI API, Vertex AI): Nhanh, không cần hạ tầng.  
  - **PaaS** (SageMaker, Azure ML): Managed scaling, ít Ops.  
  - **IaaS** (EC2 GPU, GCE): Full control, cần Ops.  
- **Chiến lược Hybrid**: Training bằng IaaS (để tối ưu chi phí), Serving bằng PaaS (để scale dễ dàng).  

## 3. Lựa chọn GPU & Tối ưu chi phí  

- **Inference**: Dùng T4, L40S, A10G (ví dụ: L40S là "sleeper pick", giá $0.40-$0.86/hr, tối ưu cho model vừa và nhỏ).  
- **Fine-tuning**: Dùng A100 ($1.79-$2.70/hr).  
- **Pre-training**: Dùng H100, H200 Cluster (H200 có 141GB HBM3e, chuẩn mực mới của 2026).  
- **Tối ưu chi phí**: Dùng Spot/Preemptible instances cho training (giảm 60-70%), Reserved instances cho serving. Sử dụng MIG (Multi-Instance GPU) để chia nhỏ GPU phục vụ nhiều model nhỏ.  


- **Terraform IaC**: Quản lý infrastructure as code (GPU instances, VPC, Security Groups) với S3 backend, chia workspaces (dev/staging/prod). Cân nhắc các phương án như Pulumi, OpenTofu.  
  - Tối ưu Docker image với multi-stage build (giảm từ 18GB xuống 6-8GB).  
  - Sử dụng NVIDIA GPU Operator để tự cài đặt driver.  
  - Karpenter (AWS) / NAP (GCP) giúp auto-provision GPU node và scale-to-zero để tiết kiệm chi phí ngoài giờ cao điểm.  
  - Cấu hình Kubernetes: Requests = Limits cho GPU (nvidia.com/gpu: 1), dùng Init container để tải model weights từ S3.  


- **8 Layers của Production AI Agent**: Compute (GPU/CPU/Serverless) -> Orchestration -> Message Queue -> Cache -> Storage -> Networking -> Observability -> Secrets & Config.  
  - **vLLM**: PagedAttention, hệ sinh thái rộng, dễ deploy.  
  - **SGLang**: RadixAttention (tái sử dụng KV cache), tối ưu cho Agent/Multi-turn chat (tăng 20% hiệu năng).  
  - **LMDeploy**: TurboMind engine (C++ zero overhead), throughput gấp 1.8x vLLM, lý tưởng cho latency-sensitive apps.

---

### *Câu hỏi ôn tập Ngày 16*

   Theo chiến lược Hybrid Cloud cho AI, cách kết hợp nào sau đây được khuyến nghị để tối ưu cả chi phí và khả năng mở rộng?
     A. Training và Serving đều dùng PaaS
     B. Training dùng IaaS, Serving dùng PaaS
     C. Training dùng AI-aaS, Serving dùng IaaS
     D. Training dùng PaaS, Serving dùng IaaS
   ***Đáp án:** B*

   GPU nào được mô tả là "sleeper pick" cho tác vụ Inference với mức giá $0.40-$0.86/giờ?
   ***Đáp án:** C*

   Giải pháp nào giúp giảm 60-70% chi phí khi training model AI trên cloud?
     A. Sử dụng Reserved Instances
     B. Sử dụng Spot/Preemptible Instances
     C. Sử dụng On-Demand Instances
     D. Sử dụng Dedicated Hosts
   ***Đáp án:** B*

   Trong Kubernetes, để quản lý tài nguyên GPU cho AI workload, cấu hình nào sau đây là đúng?
     A. Đặt requests nhỏ hơn limits cho GPU
     B. Dùng `nvidia.com/gpu` với requests = limits
     C. Không cần chỉ định resource requests cho GPU
     D. Dùng `cpu` và `memory` thay vì GPU resource
   ***Đáp án:** B*

   Serving engine nào sử dụng RadixAttention để tái sử dụng KV cache, tối ưu cho Agent và Multi-turn chat?
   ***Đáp án:** B*
