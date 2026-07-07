---
type: summary
title: "Day 20 Track 2: Model Serving & Inference Optimization"
description: "A deep dive into modern LLM serving infrastructure, quantization, KV cache optimization, and inference scaling strategies."
tags: [day20, track2, model-serving, inference, quantization, vLLM, SGLang, paged-attention]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/20/1-day20-model-serving-inference-optimization.pdf"]
---
# Day 20 Track 2: Model Serving & Inference Optimization
*Ngày 20 Track 2: Phục vụ Mô hình & Tối ưu hóa Suy luận*

## 1. Overview
*1. Tổng quan*

This module explores AI infrastructure for production, specifically focusing on how to serve Large Language Models (LLMs) with high throughput, low latency, and efficient memory utilization.
*Mô-đun này khám phá cơ sở hạ tầng AI cho sản xuất, đặc biệt tập trung vào cách phục vụ các Mô hình Ngôn ngữ Lớn (LLM) với thông lượng cao, độ trễ thấp và sử dụng bộ nhớ hiệu quả.*

## 2. Latency Metrics and Goodput
*2. Các chỉ số Độ trễ và Goodput*

Understanding latency is critical for user experience in LLMs.
*Hiểu về độ trễ là rất quan trọng đối với trải nghiệm người dùng trong LLM.*

* **TTFT (Time To First Token):** Time from request to the first generated token (depends on prefill compute and queue wait).
    *TTFT (Thời gian đến Token đầu tiên): Thời gian từ yêu cầu đến token đầu tiên được sinh ra (phụ thuộc vào tính toán prefill và thời gian chờ hàng đợi).*

* **TPOT (Time Per Output Token):** Time between each generated token.
    *TPOT (Thời gian mỗi Token đầu ra): Thời gian giữa mỗi token được sinh ra.*

* **Throughput vs Goodput:** Throughput is total tokens/s at saturation, whereas **Goodput@SLO** is the request rate that satisfies specific TTFT and TPOT Service Level Objectives (SLOs). Goodput is the most important production metric.
    *Thông lượng so với Goodput: Thông lượng là tổng số token/giây ở trạng thái bão hòa, trong khi **Goodput@SLO** là tốc độ yêu cầu đáp ứng các Mục tiêu Cấp độ Dịch vụ (SLO) cụ thể về TTFT và TPOT. Goodput là chỉ số sản xuất quan trọng nhất.*

## 3. Quantization
*3. Lượng tử hóa*

Quantization reduces the precision of model weights to save VRAM and increase throughput.
*Lượng tử hóa giảm độ chính xác của trọng số mô hình để tiết kiệm VRAM và tăng thông lượng.*

* **FP16 / BF16:** Baseline precision.
    *FP16 / BF16: Độ chính xác cơ sở.*

* **FP8:** <1% quality drop, halves memory (native on Hopper GPUs).
    *FP8: Giảm chất lượng <1%, giảm một nửa bộ nhớ (hỗ trợ tự nhiên trên GPU Hopper).*

* **AWQ (4-bit):** High quality for heavily constrained environments (ideal for 8B+ models).
    *AWQ (4-bit): Chất lượng cao cho môi trường bị hạn chế nhiều (lý tưởng cho các mô hình 8B+).*

* **GGUF (Q4_K_M):** Recommended for CPU/Edge inference.
    *GGUF (Q4_K_M): Được khuyến nghị cho suy luận CPU/Edge.*

* **NVFP4:** Blackwell native format, extremely fast with minimal loss.
    *NVFP4: Định dạng gốc của Blackwell, cực kỳ nhanh với tổn thất tối thiểu.*

## 4. Attention Optimization & KV Cache
*4. Tối ưu hóa Attention & Bộ đệm KV*

* **PagedAttention:** Treats KV cache like virtual memory pages to eliminate memory fragmentation, enabling continuous batching and yielding up to 24x throughput gains compared to naive Hugging Face Transformers.
    *PagedAttention: Xử lý bộ đệm KV giống như các trang bộ nhớ ảo để loại bỏ phân mảnh bộ nhớ, cho phép xử lý theo lô liên tục và mang lại hiệu suất thông lượng lên đến 24 lần so với Hugging Face Transformers thông thường.*

* **FlashAttention (v1-v4):** IO-aware attention that optimizes HBM read/writes by tiling data in SRAM, supporting long contexts without OOM.
    *FlashAttention (v1-v4): Cơ chế attention nhận biết IO, tối ưu hóa đọc/ghi HBM bằng cách phân mảnh dữ liệu trong SRAM, hỗ trợ ngữ cảnh dài mà không bị OOM.*

* **MLA (Multi-Latent Attention):** Used in architectures like DeepSeek-V3 to compress KV caches, using 10x less memory than standard Multi-Head Attention (MHA).
    *MLA (Multi-Latent Attention): Được sử dụng trong các kiến trúc như DeepSeek-V3 để nén bộ đệm KV, sử dụng ít bộ nhớ hơn 10 lần so với Multi-Head Attention (MHA) tiêu chuẩn.*

* **Prefix Caching:** RadixAttention (SGLang) and Automatic Prefix Caching (vLLM) cache shared system prompts across requests, massively reducing TTFT.
    *Bộ đệm tiền tố (Prefix Caching): RadixAttention (SGLang) và Automatic Prefix Caching (vLLM) lưu bộ đệm các lời nhắc hệ thống dùng chung giữa các yêu cầu, giảm đáng kể TTFT.*

## 5. Inference Serving Stack 2026
*5. Ngăn xếp phục vụ suy luận 2026*

Key engines for production serving:
*Các công cụ chính cho phục vụ sản xuất:*

* **vLLM:** The industry standard, featuring PagedAttention and automatic prefix caching.
    *vLLM: Tiêu chuẩn công nghiệp, có PagedAttention và tự động lưu bộ đệm tiền tố.*

* **SGLang:** Highly optimized for multi-turn and structured generation via RadixAttention.
    *SGLang: Được tối ưu hóa cao cho sinh đa lượt và có cấu trúc thông qua RadixAttention.*

* **TensorRT-LLM:** NVIDIA's native optimized backend.
    *TensorRT-LLM: Backend tối ưu hóa gốc của NVIDIA.*

* **llama.cpp / Ollama:** Ideal for local CPU/GPU/Apple Metal execution.
    *llama.cpp / Ollama: Lý tưởng cho thực thi cục bộ trên CPU/GPU/Apple Metal.*

* **NVIDIA Dynamo & llm-d:** Disaggregated prefill/decode orchestrators for large-scale multi-tenant clouds.
    *NVIDIA Dynamo & llm-d: Các bộ điều phối prefill/decode phân tách cho các đám mây đa đối tượng quy mô lớn.*

## 6. Advanced Parallelism and Scaling
*6. Song song hóa và Mở rộng nâng cao*

* **Disaggregated Serving:** Separating compute into Prefill Pools and Decode Pools to prevent long context prompts from blocking generation tasks.
    *Phục vụ phân tách: Tách biệt tính toán thành Cụm Prefill và Cụm Decode để ngăn các lời nhắc ngữ cảnh dài làm chặn các tác vụ sinh.*

* **Parallelism Strategies:**
    *Chiến lược song song hóa:*

  * **TP (Tensor Parallelism):** Splitting layers across GPUs within a node.
      *TP (Song song Tensor): Chia các lớp trên nhiều GPU trong cùng một nút.*

  * **PP (Pipeline Parallelism):** Splitting layers across nodes for ultra-long context.
      *PP (Song song Pipeline): Chia các lớp trên nhiều nút cho ngữ cảnh siêu dài.*

  * **EP (Expert Parallelism):** Routing tokens to specific MoE experts.
      *EP (Song song Chuyên gia): Định tuyến các token đến các chuyên gia MoE cụ thể.*

  * **DP (Data Parallelism):** Replicating the model across instances.
      *DP (Song song Dữ liệu): Nhân bản mô hình trên nhiều phiên bản.*

* **Speculative Decoding:** Using a smaller draft model to generate tokens and a larger model to verify, speeding up generation in memory-bound setups.
    *Giải mã suy đoán: Sử dụng một mô hình dự thảo nhỏ hơn để sinh token và một mô hình lớn hơn để xác minh, tăng tốc quá trình sinh trong các thiết lập bị giới hạn bộ nhớ.*

## 7. Power and Sustainability
*7. Năng lượng và Tính bền vững*

* **Tokens-per-Joule:** Energy efficiency is a primary bottleneck. Median cost is ~0.31Wh/query. Reasoning models consume significantly more energy.
    *Token trên Joule: Hiệu suất năng lượng là một nút thắt chính. Chi phí trung bình khoảng 0.31Wh/truy vấn. Các mô hình suy luận tiêu thụ năng lượng nhiều hơn đáng kể.*

## 8. Multi-modal and Embedding Serving
*8. Phục vụ Đa phương thức và Embedding*

* **Multimodal (VLM):** TTFT becomes a function of image/video size. Encoding vision tokens is decoupled from the prefill/decode phases.
    *Đa phương thức (VLM): TTFT trở thành một hàm của kích thước hình ảnh/video. Mã hóa token thị giác được tách rời khỏi các giai đoạn prefill/decode.*

* **Semantic Caching:** Caching responses based on embedding similarity to bypass full inference.
    *Bộ đệm ngữ nghĩa: Lưu bộ đệm các phản hồi dựa trên độ tương đồng embedding để bỏ qua suy luận đầy đủ.*
