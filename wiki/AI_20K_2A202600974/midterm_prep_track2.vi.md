---
type: concept
title: "Midterm Exam Preparation - Track 2 (Infrastructure/LLMOps)"
description: "Bộ tài liệu và câu hỏi ôn tập thi giữa kỳ Chương trình Phát triển Năng lực AI Thực Chiến dành cho Track 2 (Infrastructure/LLMOps)"
tags: [ai, 20k, exam, prep, track2]
timestamp: 2026-07-06
sources: ["wiki/AI_20K_2A202600974/day16_track2.md", "wiki/AI_20K_2A202600974/day18_track2.md", "wiki/AI_20K_2A202600974/day20_track2.md", "wiki/AI_20K_2A202600974/day21_track2.md", "wiki/AI_20K_2A202600974/day23_track2.md", "wiki/AI_20K_2A202600974/day27_track2.md"]
---
# BỘ ÔN TẬP THI GIỮA KỲ — TRACK 2 (INFRASTRUCTURE / LLMOPS)

Tài liệu này tổng hợp kiến thức trọng tâm và các dạng câu hỏi ôn tập chuyên sâu (Trắc nghiệm, Multi-select, Scenario Debug, Case Study) bám sát phần thi của **Track 2: Infrastructure / Data Lakehouse / LLMOps** trong kỳ thi giữa kỳ.

---

## PHẦN I: KIẾN THỨC TRỌNG TÂM TRACK 2

 ***Medallion Architecture:** Kiến trúc dữ liệu 3 lớp:
   **Bronze Layer (Raw):** *Lưu trữ dữ liệu thô dạng append-only trực tiếp từ nguồn (Kafka, APIs, files) mà không qua biến đổi.
   **Silver Layer (Cleansed/Conformed):** *Dữ liệu được làm sạch, chuẩn hóa kiểu dữ liệu, khử trùng lặp và áp dụng Data Contracts sơ bộ.
   **Gold Layer (Business/Curated):** *Dữ liệu được tổng hợp theo nhu cầu nghiệp vụ, phục vụ trực tiếp cho BI, Analytics và đưa vào Vector Stores cho RAG.
 ***Storage Formats (Delta Lake / Apache Iceberg):** Hỗ trợ các thuộc tính ACID trên Object Storage (S3, GCS), cung cấp cơ chế du hành thời gian (Time travel - truy xuất lại phiên bản dữ liệu cũ) và Schema Evolution.
 ***Inference Data Pipeline:** Dữ liệu streaming thông qua Kafka/Flink được gom nhóm và đổ về Feature Stores thời gian thực để Agent sử dụng tức thì.

 ***vLLM & SGLang:** Các công cụ phục vụ mô hình (Model Serving) hiệu năng cao.
 ***PagedAttention:** Giải pháp tối ưu hóa bộ nhớ GPU bằng cách phân chia bộ nhớ **KV Cache** thành các trang vật lý không liên tục (tương tự Virtual Memory trong OS). Giúp tăng thông lượng (Throughput) lên 2-4 lần và giảm lãng phí bộ nhớ GPU xuống gần 0%.
 ***Quantization (Lượng tử hóa):** Giảm dung lượng mô hình bằng cách đổi kiểu số thực của trọng số (ví dụ từ FP16 sang INT8 hoặc INT4).
   ***GGUF:** Phù hợp chạy CPU/Edge/Localhost (sử dụng llama.cpp).
   ***GPTQ / AWQ:** Phù hợp chạy GPU phục vụ thương mại trên cloud.
   *Sử dụng Spot Instances để giảm chi phí huấn luyện tới 70-80% (cần tích hợp cơ chế tự phục hồi checkpoint).
   *Tối ưu hóa kích thước GPU (Right-sizing) tránh lãng phí khi mô hình chạy ở mức tải thấp.

 ***DVC (Data Version Control):** Quản lý phiên bản dữ liệu và mô hình lớn bằng Git mà không lưu trực tiếp file nặng vào Git. DVC lưu trữ file nặng trên cloud storage (S3, GCS) và tạo ra các file `.dvc` nhỏ chứa hash để Git theo dõi.
   ***Tracking:** Ghi lại các tham số (Hyperparameters), metrics (Loss, Accuracy) và artifacts của mỗi lượt thí nghiệm.
   ***Model Registry:** Quản lý các phiên bản mô hình và trạng thái của chúng (Staging, Production, Archived).
 ***GitHub Actions pipeline:** Tự động chạy unit test, linter, đóng gói Docker Image chứa mô hình và deploy lên Kubernetes/EKS khi code thay đổi.

 ***7 chiều đo lường chất lượng dữ liệu:**
  1. *Completeness (Độ đầy đủ)*
  2. *Accuracy (Độ chính xác)*
  3. *Consistency (Độ nhất quán)*
  4. *Validity (Độ hợp lệ về định dạng)*
  5. *Timeliness (Tính kịp thời)*
  6. *Uniqueness (Tính duy nhất - không trùng lặp)*
  7. *Integrity (Tính toàn vẹn liên kết)*
 ***Great Expectations:** Thư viện Python tự động hóa việc kiểm thử dữ liệu thông qua định nghĩa các quy tắc kiểm tra (Expectations), xuất báo cáo chất lượng tự động trước khi nạp vào pipeline AI.
 ***Data Contracts & Lineage:** Thỏa thuận về định dạng dữ liệu giữa bên sản xuất và bên tiêu thụ. Sơ đồ Lineage giúp truy vết dòng chảy dữ liệu từ nguồn thô đến đầu ra mô hình để phục vụ debug lỗi hệ thống.

---

## CÂU HỎI ÔN TẬP THỰC CHIẾN (TRACK 2)

### Dạng 1: Trắc nghiệm & Multi-Select

#### Câu 1 (Multi-select): Khi thiết kế một hệ thống Model Serving sử dụng vLLM trên production, cấu hình nào giúp bạn tối ưu hóa hiệu suất phục vụ nhiều người dùng đồng thời (High Throughput)? (Chọn tất cả các đáp án đúng)
- [x] *A. Kích hoạt PagedAttention để phân bổ động bộ nhớ KV Cache và triệt tiêu phân mảnh bộ nhớ GPU.*
- [ ] *B. Chuyển định dạng mô hình sang GGUF để chạy tối ưu trên các cụm máy chủ GPU NVIDIA chuyên dụng.*
- [x] *C. Tận dụng cơ chế Continuous Batching để gộp các yêu cầu của khách hàng đến sau vào lượt xử lý hiện tại của mô hình mà không cần đợi lượt trước kết thúc hoàn toàn.*
- [x] *D. Áp dụng Tensor Parallelism (TP) chia mô hình trên nhiều GPU cùng node để tăng tốc thời gian sinh một token mới (Latency per token).*

Giải thích: GGUF (B) chỉ tối ưu cho CPU hoặc thiết bị ngoại vi, không phù hợp cho hạ tầng GPU Server chuyên dụng (nơi GPTQ/AWQ chiếm ưu thế). Các đáp án A, C, D đều là các kỹ thuật tối ưu hóa thông lượng và độ trễ cốt lõi của vLLM.

#### Câu 2 (Single choice): Trong hệ thống CI/CD cho AI sử dụng Git và DVC, file nào thực tế sẽ được commit lên GitHub để quản lý phiên bản của một dataset nặng 10GB?
- ( ) *A. Toàn bộ thư mục chứa dataset thô 10GB đó.*
- (x) *B. File metadata nhỏ dạng `.dvc` (chứa mã băm hash và kích thước của dataset) được sinh ra bởi DVC.*
- ( ) *C. Một tệp Docker Image nén chứa dataset đó.*
- ( ) *D. Đường link tải dataset lưu trong cấu hình `.gitignore`.*

Giải thích: DVC lưu file nặng 10GB ở Cloud Storage bên ngoài và sinh ra file `.dvc` (chỉ vài KB) chứa mã hash để Git theo dõi phiên bản dữ liệu.

---

### Dạng 2: Scenario Debug (Xử lý lỗi OOM trong Model Serving)

#### Tình huống:
Một hệ thống Chatbot doanh nghiệp chạy trên 1 GPU NVIDIA A10G (24GB VRAM) sử dụng vLLM để phục vụ mô hình `Llama-3-8B-Instruct` (kích thước gốc FP16 là ~16GB VRAM).
Khi số lượng người dùng đồng thời tăng lên 15 người cùng lúc, hệ thống báo lỗi **CUDA Out of Memory (OOM)** và sập Server.
Kiểm tra cấu hình khởi chạy hiện tại của bạn:

```bash
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Meta-Llama-3-8B-Instruct \
    --gpu-memory-utilization 0.90 \
    --max-model-len 8192
```

#### Câu hỏi Debug:
1. **Tại sao lỗi OOM lại xảy ra** khi lượng người dùng đồng thời tăng lên 15 người, mặc dù kích thước mô hình gốc (~16GB) nhỏ hơn dung lượng VRAM của GPU (24GB)?
2. **Đề xuất ít nhất 3 cấu hình chỉnh sửa** cụ thể (bao gồm lượng tử hóa và điều chỉnh siêu tham số) giúp hệ thống chạy ổn định tải này trên cùng 1 card GPU A10G.

#### Lời giải đề xuất:
1. **Nguyên nhân lỗi:**
    *Khi người dùng tương tác, mô hình cần lưu lại ngữ cảnh hội thoại dưới dạng **KV Cache**.
    *Với độ dài ngữ cảnh tối đa `--max-model-len 8192` và 15 người dùng, dung lượng KV Cache cần thiết vượt quá khoảng VRAM trống còn lại sau khi load mô hình (24GB VRAM - 16GB mô hình = 8GB trống). Do đó, khi hàng đợi yêu cầu đầy, GPU bị tràn bộ nhớ và xảy ra lỗi OOM.
2. **Đề xuất 3 cấu hình khắc phục:**
    **Giải pháp 1: Lượng tử hóa mô hình (Quantization)*
     Chuyển sang sử dụng mô hình được lượng tử hóa AWQ 4-bit (ví dụ: `Casperhansen/llama-3-8b-Instruct-awq`). Dung lượng mô hình trên VRAM sẽ giảm từ ~16GB xuống chỉ còn ~5.5GB, giải phóng hơn 18GB trống cho KV Cache.
    **Giải pháp 2: Điều chỉnh giới hạn độ dài ngữ cảnh (`--max-model-len`)*
     Nếu nghiệp vụ chatbot không đòi hỏi đọc tài liệu quá dài, hãy giảm xuống `--max-model-len 4096`. Điều này sẽ cắt giảm một nửa nhu cầu bộ nhớ KV Cache trên mỗi request của người dùng.
    **Giải pháp 3: Giới hạn bộ nhớ KV Cache tối đa (`--gpu-memory-utilization`)*
     Giảm tỷ lệ bộ nhớ phân bổ tối đa cho vLLM xuống `--gpu-memory-utilization 0.85` để dành khoảng trống an toàn cho hệ thống xử lý các tác vụ đột biến.

**Cấu hình sửa đổi tối ưu:**
```bash
python -m vllm.entrypoints.openai.api_server \
    --model Casperhansen/llama-3-8b-Instruct-awq \
    --quantization awq \
    --gpu-memory-utilization 0.85 \
    --max-model-len 4096
```

---

### Dạng 3: Case Study Thiết kế Pipeline Data Observability

#### Đề bài:
Doanh nghiệp bảo hiểm Z tiếp nhận trung bình 50,000 ảnh chụp hóa đơn y tế mỗi ngày từ ứng dụng của khách hàng để gửi cho mô hình OCR trích xuất thông tin bồi thường.
Rất nhiều ảnh gửi lên bị mờ, sai định dạng, chụp thiếu góc hoặc bị trùng lặp, gây ra lỗi cho pipeline AI và làm sai lệch dữ liệu bồi thường của hệ thống kế toán.

#### Bạn hãy thiết kế kiến trúc giám sát chất lượng dữ liệu (Data Observability):
1. *Đề xuất các quy tắc kiểm thử dữ liệu (Expectations) cụ thể bằng công cụ **Great Expectations** ở lớp *Silver Layer* của Medallion Architecture.*
2. *Thiết kế cơ chế cảnh báo lỗi tự động và luồng cô lập dữ liệu lỗi (Quarantine) để đảm bảo không làm sập pipeline OCR.*

#### Lời giải đề xuất:
1. **Thiết lập quy tắc kiểm thử dữ liệu (Expectations):**
   * *Độ đầy đủ (Completeness):* `expect_column_values_to_not_be_null("customer_id")` và `expect_column_values_to_not_be_null("invoice_image_path")`.
   * *Định dạng hợp lệ (Validity):* `expect_column_values_to_match_regex("invoice_date", r"^\d{4}-\d{2}-\d{2}$")`.
   * *Tính duy nhất (Uniqueness):* `expect_column_values_to_be_unique("invoice_id")` dựa trên mã hóa hash MD5 của ảnh để chống trùng lặp.
   * *Độ chính xác (Accuracy):* `expect_column_values_to_be_between("invoice_amount", min_value=0, max_value=500000000)`.
2. **Thiết kế luồng xử lý và cách cô lập (Quarantine):**
    *Dữ liệu từ Kafka đổ về **Bronze Layer** (Lưu nguyên trạng thái thô).
    *Tại bước chuyển đổi sang **Silver Layer**, luồng xử lý Spark/Python chạy Great Expectations kiểm tra dữ liệu:
      *Nếu dòng dữ liệu nào **Đạt kiểm thử**: Đẩy tiếp sang bảng Silver để nạp vào hệ thống mô hình OCR.
      *Nếu dòng dữ liệu nào **Không đạt**: Đánh dấu trạng thái `status='quarantine'`, ghi nhận mã lỗi lý do và đẩy vào một DB riêng biệt dành cho việc kiểm tra tay (Human-in-the-loop review).
   * **Cảnh báo (Alerting):** Nếu tỷ lệ lỗi vượt quá mức cam kết chất lượng SLO (ví dụ >5% lượng ảnh trong 1 giờ), hệ thống tự động gửi cảnh báo (Slack/PagerDuty) cho đội ngũ Data/Operations để kịp thời can thiệp xử lý nguồn gửi dữ liệu.
