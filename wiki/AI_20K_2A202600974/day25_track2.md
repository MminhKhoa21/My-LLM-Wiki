---
type: summary
title: "Day 25 Track 2: GPU FinOps & Cost Optimization"
description: "A comprehensive guide to optimizing GPU cloud costs, utilizing spot instances, right-sizing workloads, and inference cost reduction techniques."
tags: [FinOps, GPU, cost-optimization, inference, LLMOps]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/25/Day25 - Track 2 - Gpu-finops-cost-optimization.pdf"]
---
Nội dung bạn cung cấp đã là song ngữ (Anh - Việt) hoàn chỉnh, với tiếng Anh ở dòng chính và bản dịch tiếng Việt in nghiêng ngay bên dưới. Dưới đây là nội dung được giữ nguyên định dạng Markdown và đã có đầy đủ cả hai ngôn ngữ:

# Day 25 Track 2: GPU FinOps & Cost Optimization  
*Ngày 25 Track 2: Quản lý tài chính và tối ưu chi phí GPU*

This document summarizes the strategies for managing and optimizing GPU costs (FinOps) in production AI environments, covering everything from instance selection to advanced inference optimization.  
*Tài liệu này tóm tắt các chiến lược quản lý và tối ưu chi phí GPU (FinOps) trong các môi trường AI sản xuất, bao gồm mọi thứ từ lựa chọn instance đến tối ưu suy luận nâng cao.*

## 1. GPU Cloud Cost Anatomy  
*1. Cấu trúc chi phí GPU đám mây*

Cost is not just the hourly rate of the GPU.  
*Chi phí không chỉ là giá theo giờ của GPU.*

- **Hidden Costs**: Data transfer (egress), NAT gateway, secrets management.  
  ***Chi phí ẩn**: Truyền dữ liệu (egress), NAT gateway, quản lý bí mật.*
- **Wasted Spend**: Idle GPUs overnight, over-provisioned instances, unused reserved capacity, and development environments left running 24/7.  
  ***Chi tiêu lãng phí**: GPU nhàn rỗi qua đêm, instance cấp phát quá mức, dung lượng dự trữ không dùng, và môi trường phát triển chạy 24/7.*

*Rule of Thumb: A GPU utilization < 30% indicates an immediate need for right-sizing.*  
*Nguyên tắc chung: Mức sử dụng GPU < 30% cho thấy cần điều chỉnh kích thước ngay.*

## 2. Spot & Preemptible Instances  
*2. Instance Spot và Preemptible*

Spot instances can provide 60-70% discounts but require graceful handling of interruptions.  
*Instance Spot có thể giảm 60-70% chi phí nhưng yêu cầu xử lý gián đoạn một cách linh hoạt.*

- **Mixed Fleet Strategy**: 20% on-demand (baseline) and 80% spot instances (burst) to balance cost and reliability.  
  ***Chiến lược hỗn hợp đội tàu**: 20% on-demand (cơ sở) và 80% spot (bùng nổ) để cân bằng chi phí và độ tin cậy.*
- **Checkpoint Strategy**: Save model state frequently (e.g., every epoch or 30 mins) to S3/GCS. If a spot instance is terminated, a new instance can resume from the checkpoint seamlessly.  
  ***Chiến lược Checkpoint**: Lưu trạng thái mô hình thường xuyên (ví dụ: mỗi epoch hoặc 30 phút) vào S3/GCS. Nếu một spot instance bị chấm dứt, instance mới có thể tiếp tục từ checkpoint một cách liền mạch.*

## 3. Right-Sizing & Utilization  
*3. Điều chỉnh kích thước và mức sử dụng*

Optimizing utilization requires tracking the right metrics:  
*Tối ưu hóa mức sử dụng yêu cầu theo dõi các chỉ số phù hợp:*

- **GPU Utilization**: Checks if the GPU is idle.  
  ***Sử dụng GPU**: Kiểm tra xem GPU có nhàn rỗi không.*
- **MFU (Model FLOPs Utilization)**: Tracks compute-bound tasks (e.g., training, prefill).  
  ***MFU (Sử dụng FLOPs của mô hình)**: Theo dõi các tác vụ bị giới hạn tính toán (vd: huấn luyện, prefill).*
- **MBU (Memory Bandwidth Utilization)**: Tracks memory-bound tasks (e.g., decoding, serving).  
  ***MBU (Sử dụng băng thông bộ nhớ)**: Theo dõi các tác vụ bị giới hạn bộ nhớ (vd: giải mã, phục vụ).*

### Multi-Model Serving & MIG (Multi-Instance GPU)  
*Phục vụ đa mô hình và MIG (GPU đa instance)*

To improve low utilization on large GPUs (e.g., A100), use MIG to isolate instances or implement multi-model serving to swap models dynamically based on requests.  
*Để cải thiện mức sử dụng thấp trên GPU lớn (vd: A100), sử dụng MIG để cô lập các instance hoặc triển khai phục vụ đa mô hình để hoán đổi mô hình động dựa trên yêu cầu.*

## 4. Inference Cost Optimization  
*4. Tối ưu chi phí suy luận*

Advanced levers to reduce cost per token:  
*Các đòn bẩy nâng cao để giảm chi phí mỗi token:*

- **Request Batching**: Grouping requests significantly increases throughput and drops cost.  
  ***Gộp yêu cầu (Request Batching)**: Nhóm các yêu cầu giúp tăng đáng kể thông lượng và giảm chi phí.*
- **Caching**: Use Redis or Semantic caching to reuse previous prompt responses (30-40% hit rate).  
  ***Bộ nhớ đệm**: Sử dụng Redis hoặc bộ nhớ đệm ngữ nghĩa để tái sử dụng phản hồi prompt trước đó (tỷ lệ trúng 30-40%).*
- **Model Cascading**: Use a smaller, cheaper model (e.g., Llama-3-8B) for 80% of queries and route only complex queries to larger models.  
  ***Phân tầng mô hình**: Sử dụng mô hình nhỏ hơn, rẻ hơn (vd: Llama-3-8B) cho 80% truy vấn và chỉ chuyển các truy vấn phức tạp đến mô hình lớn hơn.*
- **Quantization**: Formats like AWQ 4-bit can reduce cost per token drastically.  
  ***Lượng tử hóa**: Các định dạng như AWQ 4-bit có thể giảm chi phí mỗi token đáng kể.*
- **Disaggregated Serving**: Separate prefill (compute-heavy) and decode (memory-heavy) onto separate GPU clusters to prevent bottlenecks.  
  ***Phục vụ phân tách**: Tách prefill (nặng tính toán) và decode (nặng bộ nhớ) lên các cụm GPU riêng biệt để tránh tắc nghẽn.*
- **Chunked Prefilling & Speculative Decoding**: Balance TTFT (Time To First Token) and ITL (Inter-Token Latency).  
  ***Prefill theo khối và Giải mã suy luận**: Cân bằng TTFT (Thời gian đến token đầu tiên) và ITL (Độ trễ giữa các token).*
- **KV Cache & Prefix Caching**: Reuse KV memory for shared prefixes to speed up TTFT for identical system prompts.  
  ***Bộ nhớ đệm KV và tiền tố (Prefix Caching)**: Tái sử dụng bộ nhớ KV cho các tiền tố chung để tăng tốc TTFT cho các prompt hệ thống giống nhau.*

## 5. Cost Allocation & Chargeback  
*5. Phân bổ chi phí và tính phí lại*

Establish clear tagging strategies (`team`, `project`, `env`) enforced by SCP/OPA policies. Utilize tools like Kubecost to breakdown per-pod costs, ensuring each team has a designated budget and transparent dashboard.  
*Thiết lập chiến lược gắn thẻ rõ ràng (`team`, `project`, `env`) được thực thi bởi các chính sách SCP/OPA. Sử dụng các công cụ như Kubecost để phân tích chi phí theo pod, đảm bảo mỗi nhóm có ngân sách được chỉ định và bảng điều khiển minh bạch.*

## 6. Sustainable AI: Carbon & Energy  
*6. AI bền vững: Carbon và năng lượng*

Optimization also reduces carbon footprint. Pick green cloud regions (e.g., hydro-powered data centers) and use distilled, smaller models when feasible. Track carbon emissions alongside performance metrics (e.g., `CodeCarbon`).  
*Tối ưu hóa cũng giảm dấu chân carbon. Chọn các khu vực đám mây xanh (vd: trung tâm dữ liệu thủy điện) và sử dụng các mô hình chưng cất, nhỏ hơn khi khả thi. Theo dõi lượng phát thải carbon cùng với các chỉ số hiệu suất (vd: `CodeCarbon`).*

Nếu bạn cần bất kỳ điều chỉnh nào về ngôn ngữ hoặc định dạng, hãy cho tôi biết.
