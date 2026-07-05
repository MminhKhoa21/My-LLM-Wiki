---
type: summary
title: "Day 20 Track 2: Model Serving & Inference Optimization"
description: "Tối ưu hóa quá trình phục vụ mô hình LLM"
tags: [ai, 20k, day20]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/20/1-day20-model-serving-inference-optimization.pdf"]
---

> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]


# Model Serving & Inference Optimization

Tổng quan về các kỹ thuật tăng tốc độ suy luận (inference) và giảm chi phí:
- **Quantization**: Giảm precision từ FP16/BF16 xuống FP8, INT8, 4-bit (AWQ, GGUF) giúp tiết kiệm VRAM đáng kể.
- **KV Cache & PagedAttention**: Quản lý bộ nhớ hiệu quả, loại bỏ fragmentation và cho phép continuous batching.
- **Inference Engines**: So sánh các engine như vLLM, SGLang, Ollama, TensorRT-LLM.
- **Distributed Inference**: Chiến lược song song hóa (Data Parallelism, Tensor Parallelism, Pipeline Parallelism, Expert Parallelism).
