---
type: summary
title: "Day 20 Track 2: Model Serving & Inference Optimization"
description: "A deep dive into modern LLM serving infrastructure, quantization, KV cache optimization, and inference scaling strategies."
tags: [day20, track2, model-serving, inference, quantization, vLLM, SGLang, paged-attention]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/20/1-day20-model-serving-inference-optimization.pdf"]
---
Ngày 20 Track 2: Phục vụ Mô hình & Tối ưu hóa Suy luận

1. Tổng quan

Mô-đun này khám phá cơ sở hạ tầng AI cho sản xuất, đặc biệt tập trung vào cách phục vụ các Mô hình Ngôn ngữ Lớn (LLM) với thông lượng cao, độ trễ thấp và sử dụng bộ nhớ hiệu quả.

2. Các chỉ số Độ trễ và Goodput

Hiểu về độ trễ là rất quan trọng đối với trải nghiệm người dùng trong LLM.

    TTFT (Thời gian đến Token đầu tiên): Thời gian từ yêu cầu đến token đầu tiên được sinh ra (phụ thuộc vào tính toán prefill và thời gian chờ hàng đợi).

    TPOT (Thời gian mỗi Token đầu ra): Thời gian giữa mỗi token được sinh ra.

    Thông lượng so với Goodput: Thông lượng là tổng số token/giây ở trạng thái bão hòa, trong khi **Goodput@SLO** là tốc độ yêu cầu đáp ứng các Mục tiêu Cấp độ Dịch vụ (SLO) cụ thể về TTFT và TPOT. Goodput là chỉ số sản xuất quan trọng nhất.

3. Lượng tử hóa

Lượng tử hóa giảm độ chính xác của trọng số mô hình để tiết kiệm VRAM và tăng thông lượng.

    FP16 / BF16: Độ chính xác cơ sở.

    FP8: Giảm chất lượng <1%, giảm một nửa bộ nhớ (hỗ trợ tự nhiên trên GPU Hopper).

    AWQ (4-bit): Chất lượng cao cho môi trường bị hạn chế nhiều (lý tưởng cho các mô hình 8B+).

    GGUF (Q4_K_M): Được khuyến nghị cho suy luận CPU/Edge.

    NVFP4: Định dạng gốc của Blackwell, cực kỳ nhanh với tổn thất tối thiểu.

4. Tối ưu hóa Attention & Bộ đệm KV

    PagedAttention: Xử lý bộ đệm KV giống như các trang bộ nhớ ảo để loại bỏ phân mảnh bộ nhớ, cho phép xử lý theo lô liên tục và mang lại hiệu suất thông lượng lên đến 24 lần so với Hugging Face Transformers thông thường.

    FlashAttention (v1-v4): Cơ chế attention nhận biết IO, tối ưu hóa đọc/ghi HBM bằng cách phân mảnh dữ liệu trong SRAM, hỗ trợ ngữ cảnh dài mà không bị OOM.

    MLA (Multi-Latent Attention): Được sử dụng trong các kiến trúc như DeepSeek-V3 để nén bộ đệm KV, sử dụng ít bộ nhớ hơn 10 lần so với Multi-Head Attention (MHA) tiêu chuẩn.

    Bộ đệm tiền tố (Prefix Caching): RadixAttention (SGLang) và Automatic Prefix Caching (vLLM) lưu bộ đệm các lời nhắc hệ thống dùng chung giữa các yêu cầu, giảm đáng kể TTFT.

5. Ngăn xếp phục vụ suy luận 2026

Các công cụ chính cho phục vụ sản xuất:

    vLLM: Tiêu chuẩn công nghiệp, có PagedAttention và tự động lưu bộ đệm tiền tố.

    SGLang: Được tối ưu hóa cao cho sinh đa lượt và có cấu trúc thông qua RadixAttention.

    TensorRT-LLM: Backend tối ưu hóa gốc của NVIDIA.

    llama.cpp / Ollama: Lý tưởng cho thực thi cục bộ trên CPU/GPU/Apple Metal.

    NVIDIA Dynamo & llm-d: Các bộ điều phối prefill/decode phân tách cho các đám mây đa đối tượng quy mô lớn.

6. Song song hóa và Mở rộng nâng cao

    Phục vụ phân tách: Tách biệt tính toán thành Cụm Prefill và Cụm Decode để ngăn các lời nhắc ngữ cảnh dài làm chặn các tác vụ sinh.

    Chiến lược song song hóa:

      TP (Song song Tensor): Chia các lớp trên nhiều GPU trong cùng một nút.

      PP (Song song Pipeline): Chia các lớp trên nhiều nút cho ngữ cảnh siêu dài.

      EP (Song song Chuyên gia): Định tuyến các token đến các chuyên gia MoE cụ thể.

      DP (Song song Dữ liệu): Nhân bản mô hình trên nhiều phiên bản.

    Giải mã suy đoán: Sử dụng một mô hình dự thảo nhỏ hơn để sinh token và một mô hình lớn hơn để xác minh, tăng tốc quá trình sinh trong các thiết lập bị giới hạn bộ nhớ.

7. Năng lượng và Tính bền vững

    Token trên Joule: Hiệu suất năng lượng là một nút thắt chính. Chi phí trung bình khoảng 0.31Wh/truy vấn. Các mô hình suy luận tiêu thụ năng lượng nhiều hơn đáng kể.

8. Phục vụ Đa phương thức và Embedding

    Đa phương thức (VLM): TTFT trở thành một hàm của kích thước hình ảnh/video. Mã hóa token thị giác được tách rời khỏi các giai đoạn prefill/decode.

    Bộ đệm ngữ nghĩa: Lưu bộ đệm các phản hồi dựa trên độ tương đồng embedding để bỏ qua suy luận đầy đủ.
