---
type: concept
title: "Midterm Exam Preparation - Track 2 (Infrastructure/LLMOps)"
description: "Bộ tài liệu và câu hỏi ôn tập thi giữa kỳ Chương trình Phát triển Năng lực AI Thực Chiến dành cho Track 2 (Infrastructure/LLMOps)"
tags: [ai, 20k, exam, prep, track2]
timestamp: 2026-07-06
sources: ["wiki/AI_20K_2A202600974/day16_track2.md", "wiki/AI_20K_2A202600974/day18_track2.md", "wiki/AI_20K_2A202600974/day20_track2.md", "wiki/AI_20K_2A202600974/day21_track2.md", "wiki/AI_20K_2A202600974/day23_track2.md", "wiki/AI_20K_2A202600974/day27_track2.md"]
---

# BỘ ÔN TẬP THI GIỮA KỲ — TRACK 2 (INFRASTRUCTURE / LLMOPS)
# MIDTERM EXAM PREPARATION — TRACK 2 (INFRASTRUCTURE / LLMOPS)

Tài liệu này tổng hợp kiến thức trọng tâm và các dạng câu hỏi ôn tập chuyên sâu (Trắc nghiệm, Multi-select, Scenario Debug, Case Study) bám sát phần thi của **Track 2: Infrastructure / Data Lakehouse / LLMOps** trong kỳ thi giữa kỳ.
*This document synthesizes key concepts and in-depth review questions (Multiple Choice, Multi-select, Scenario Debug, Case Study) closely aligned with the **Track 2: Infrastructure / Data Lakehouse / LLMOps** portion of the midterm exam.*

---

## PHẦN I: KIẾN THỨC TRỌNG TÂM TRACK 2
## PART I: CORE KNOWLEDGE TRACK 2

### 1. Data Lakehouse & Ingestion Pipelines
### 1. Data Lakehouse & Ingestion Pipelines
* **Medallion Architecture:** Kiến trúc dữ liệu 3 lớp:
* ***Medallion Architecture:** 3-layer data architecture:*
  * *Bronze Layer (Raw):* Lưu trữ dữ liệu thô dạng append-only trực tiếp từ nguồn (Kafka, APIs, files) mà không qua biến đổi.
  * *Bronze Layer (Raw): Stores raw, append-only data directly from sources (Kafka, APIs, files) without transformation.*
  * *Silver Layer (Cleansed/Conformed):* Dữ liệu được làm sạch, chuẩn hóa kiểu dữ liệu, khử trùng lặp và áp dụng Data Contracts sơ bộ.
  * *Silver Layer (Cleansed/Conformed): Data is cleaned, standardized by data type, deduplicated, and initial Data Contracts are applied.*
  * *Gold Layer (Business/Curated):* Dữ liệu được tổng hợp theo nhu cầu nghiệp vụ, phục vụ trực tiếp cho BI, Analytics và đưa vào Vector Stores cho RAG.
  * *Gold Layer (Business/Curated): Data is aggregated according to business needs, directly serving BI, Analytics, and feeding into Vector Stores for RAG.*
* **Storage Formats (Delta Lake / Apache Iceberg):** Hỗ trợ các thuộc tính ACID trên Object Storage (S3, GCS), cung cấp cơ chế du hành thời gian (Time travel - truy xuất lại phiên bản dữ liệu cũ) và Schema Evolution.
* ***Storage Formats (Delta Lake / Apache Iceberg):** Supports ACID properties on Object Storage (S3, GCS), provides time travel mechanisms (retrieving old data versions), and Schema Evolution.*
* **Inference Data Pipeline:** Dữ liệu streaming thông qua Kafka/Flink được gom nhóm và đổ về Feature Stores thời gian thực để Agent sử dụng tức thì.
* ***Inference Data Pipeline:** Streaming data via Kafka/Flink is aggregated and loaded into real-time Feature Stores for immediate use by Agents.*

### 2. Model Serving & Inference Optimization
### 2. Model Serving & Inference Optimization
* **vLLM & SGLang:** Các công cụ phục vụ mô hình (Model Serving) hiệu năng cao.
* ***vLLM & SGLang:** High-performance Model Serving tools.*
* **PagedAttention:** Giải pháp tối ưu hóa bộ nhớ GPU bằng cách phân chia bộ nhớ **KV Cache** thành các trang vật lý không liên tục (tương tự Virtual Memory trong OS). Giúp tăng thông lượng (Throughput) lên 2-4 lần và giảm lãng phí bộ nhớ GPU xuống gần 0%.
* ***PagedAttention:** A GPU memory optimization solution that divides **KV Cache** memory into non-contiguous physical pages (similar to Virtual Memory in OS). It increases throughput by 2-4x and reduces GPU memory waste to near 0%.*
* **Quantization (Lượng tử hóa):** Giảm dung lượng mô hình bằng cách đổi kiểu số thực của trọng số (ví dụ từ FP16 sang INT8 hoặc INT4).
* ***Quantization:** Reduces model size by changing the floating-point precision of weights (e.g., from FP16 to INT8 or INT4).*
  * *GGUF:* Phù hợp chạy CPU/Edge/Localhost (sử dụng llama.cpp).
  * *GGUF: Suitable for CPU/Edge/Localhost execution (using llama.cpp).*
  * *GPTQ / AWQ:* Phù hợp chạy GPU phục vụ thương mại trên cloud.
  * *GPTQ / AWQ: Suitable for commercial GPU serving on the cloud.*
* **GPU FinOps:**
* ***GPU FinOps:**
  * Sử dụng *Spot Instances* để giảm chi phí huấn luyện tới 70-80% (cần tích hợp cơ chế tự phục hồi checkpoint).
  * *Utilizing Spot Instances to reduce training costs by up to 70-80% (requires integration of checkpoint auto-recovery mechanisms).*
  * Tối ưu hóa kích thước GPU (Right-sizing) tránh lãng phí khi mô hình chạy ở mức tải thấp.
  * *GPU Right-sizing to prevent resource waste when the model runs at low loads.*

### 3. CI/CD for AI & ML Lifecycle
### 3. CI/CD for AI & ML Lifecycle
* **DVC (Data Version Control):** Quản lý phiên bản dữ liệu và mô hình lớn bằng Git mà không lưu trực tiếp file nặng vào Git. DVC lưu trữ file nặng trên cloud storage (S3, GCS) và tạo ra các file `.dvc` nhỏ chứa hash để Git theo dõi.
* ***DVC (Data Version Control):** Manages versions of large data and models with Git without storing heavy files directly in Git. DVC stores heavy files on cloud storage (S3, GCS) and generates small `.dvc` files containing hashes for Git tracking.*
* **MLflow:** 
* ***MLflow:** 
  * *Tracking:* Ghi lại các tham số (Hyperparameters), metrics (Loss, Accuracy) và artifacts của mỗi lượt thí nghiệm.
  * *Tracking: Logs hyperparameters, metrics (Loss, Accuracy), and artifacts of each experiment run.*
  * *Model Registry:* Quản lý các phiên bản mô hình và trạng thái của chúng (Staging, Production, Archived).
  * *Model Registry: Manages model versions and their lifecycle stages (Staging, Production, Archived).*
* **GitHub Actions pipeline:** Tự động chạy unit test, linter, đóng gói Docker Image chứa mô hình và deploy lên Kubernetes/EKS khi code thay đổi.
* ***GitHub Actions pipeline:** Automatically runs unit tests, linters, packages the Docker Image containing the model, and deploys to Kubernetes/EKS upon code changes.*

### 4. Data Observability & Quality
### 4. Data Observability & Quality
* **7 chiều đo lường chất lượng dữ liệu:**
* ***7 dimensions of data quality measurement:**
  1. *Completeness (Độ đầy đủ)*
  1. *Completeness*
  2. *Accuracy (Độ chính xác)*
  2. *Accuracy*
  3. *Consistency (Độ nhất quán)*
  3. *Consistency*
  4. *Validity (Độ hợp lệ về định dạng)*
  4. *Validity (Format correctness)*
  5. *Timeliness (Tính kịp thời)*
  5. *Timeliness*
  6. *Uniqueness (Tính duy nhất - không trùng lặp)*
  6. *Uniqueness (No duplication)*
  7. *Integrity (Tính toàn vẹn liên kết)*
  7. *Integrity (Relational integrity)*
* **Great Expectations:** Thư viện Python tự động hóa việc kiểm thử dữ liệu thông qua định nghĩa các quy tắc kiểm tra (Expectations), xuất báo cáo chất lượng tự động trước khi nạp vào pipeline AI.
* ***Great Expectations:** A Python library that automates data testing through defined rules (Expectations), automatically generating quality reports before ingestion into AI pipelines.*
* **Data Contracts & Lineage:** Thỏa thuận về định dạng dữ liệu giữa bên sản xuất và bên tiêu thụ. Sơ đồ Lineage giúp truy vết dòng chảy dữ liệu từ nguồn thô đến đầu ra mô hình để phục vụ debug lỗi hệ thống.
* ***Data Contracts & Lineage:** Agreements on data formatting between producers and consumers. Lineage diagrams help trace the data flow from raw sources to model outputs for system debugging.*

---

## CÂU HỎI ÔN TẬP THỰC CHIẾN (TRACK 2)
## PRACTICAL REVIEW QUESTIONS (TRACK 2)

### Dạng 1: Trắc nghiệm & Multi-Select
### Type 1: Multiple Choice & Multi-Select

#### Câu 1 (Multi-select): Khi thiết kế một hệ thống Model Serving sử dụng vLLM trên production, cấu hình nào giúp bạn tối ưu hóa hiệu suất phục vụ nhiều người dùng đồng thời (High Throughput)? (Chọn tất cả các đáp án đúng)
#### Question 1 (Multi-select): When designing a Model Serving system using vLLM in production, which configurations help optimize performance for serving multiple concurrent users (High Throughput)? (Select all correct answers)
- [x] A. Kích hoạt PagedAttention để phân bổ động bộ nhớ KV Cache và triệt tiêu phân mảnh bộ nhớ GPU.
- [x] A. Enable PagedAttention to dynamically allocate KV Cache memory and eliminate GPU memory fragmentation.
- [ ] B. Chuyển định dạng mô hình sang GGUF để chạy tối ưu trên các cụm máy chủ GPU NVIDIA chuyên dụng.
- [ ] B. Convert the model format to GGUF for optimal execution on dedicated NVIDIA GPU server clusters.
- [x] C. Tận dụng cơ chế Continuous Batching để gộp các yêu cầu của khách hàng đến sau vào lượt xử lý hiện tại của mô hình mà không cần đợi lượt trước kết thúc hoàn toàn.
- [x] C. Utilize the Continuous Batching mechanism to group incoming client requests into the current processing batch without waiting for the previous batch to completely finish.
- [x] D. Áp dụng Tensor Parallelism (TP) chia mô hình trên nhiều GPU cùng node để tăng tốc thời gian sinh một token mới (Latency per token).
- [x] D. Apply Tensor Parallelism (TP) to split the model across multiple GPUs on the same node to accelerate the generation time of a new token (Latency per token).

*Giải thích:* GGUF (B) chỉ tối ưu cho CPU hoặc thiết bị ngoại vi, không phù hợp cho hạ tầng GPU Server chuyên dụng (nơi GPTQ/AWQ chiếm ưu thế). Các đáp án A, C, D đều là các kỹ thuật tối ưu hóa thông lượng và độ trễ cốt lõi của vLLM.
*Explanation: GGUF (B) is only optimized for CPUs or edge devices, and is unsuitable for dedicated GPU Server infrastructure (where GPTQ/AWQ dominates). Options A, C, and D are all core techniques for optimizing throughput and latency in vLLM.*

#### Câu 2 (Single choice): Trong hệ thống CI/CD cho AI sử dụng Git và DVC, file nào thực tế sẽ được commit lên GitHub để quản lý phiên bản của một dataset nặng 10GB?
#### Question 2 (Single choice): In a CI/CD system for AI using Git and DVC, which file is actually committed to GitHub to manage the versioning of a 10GB dataset?
- ( ) A. Toàn bộ thư mục chứa dataset thô 10GB đó.
- ( ) A. The entire directory containing that 10GB raw dataset.
- (x) B. File metadata nhỏ dạng `.dvc` (chứa mã băm hash và kích thước của dataset) được sinh ra bởi DVC.
- (x) B. A small metadata file with a `.dvc` extension (containing the hash code and dataset size) generated by DVC.
- ( ) C. Một tệp Docker Image nén chứa dataset đó.
- ( ) C. A compressed Docker Image file containing that dataset.
- ( ) D. Đường link tải dataset lưu trong cấu hình `.gitignore`.
- ( ) D. A download link for the dataset saved in the `.gitignore` configuration.

*Giải thích:* DVC lưu file nặng 10GB ở Cloud Storage bên ngoài và sinh ra file `.dvc` (chỉ vài KB) chứa mã hash để Git theo dõi phiên bản dữ liệu.
*Explanation: DVC stores the heavy 10GB file in external Cloud Storage and generates a `.dvc` file (just a few KB) containing the hash code for Git to track data versions.*

---

### Dạng 2: Scenario Debug (Xử lý lỗi OOM trong Model Serving)
### Type 2: Scenario Debug (Handling OOM Errors in Model Serving)

#### Tình huống:
#### Scenario:
Một hệ thống Chatbot doanh nghiệp chạy trên 1 GPU NVIDIA A10G (24GB VRAM) sử dụng vLLM để phục vụ mô hình `Llama-3-8B-Instruct` (kích thước gốc FP16 là ~16GB VRAM). 
*An enterprise Chatbot system is running on 1 NVIDIA A10G GPU (24GB VRAM) using vLLM to serve the `Llama-3-8B-Instruct` model (original FP16 size is ~16GB VRAM).*
Khi số lượng người dùng đồng thời tăng lên 15 người cùng lúc, hệ thống báo lỗi **CUDA Out of Memory (OOM)** và sập Server.
*When the number of concurrent users increases to 15, the system reports a **CUDA Out of Memory (OOM)** error and the Server crashes.*
Kiểm tra cấu hình khởi chạy hiện tại của bạn:
*Checking your current startup configuration:*

```bash
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Meta-Llama-3-8B-Instruct \
    --gpu-memory-utilization 0.90 \
    --max-model-len 8192
```

#### Câu hỏi Debug:
#### Debugging Questions:
1. **Tại sao lỗi OOM lại xảy ra** khi lượng người dùng đồng thời tăng lên 15 người, mặc dù kích thước mô hình gốc (~16GB) nhỏ hơn dung lượng VRAM của GPU (24GB)?
1. **Why does the OOM error occur** when concurrent users hit 15, even though the original model size (~16GB) is smaller than the GPU's VRAM capacity (24GB)?
2. **Đề xuất ít nhất 3 cấu hình chỉnh sửa** cụ thể (bao gồm lượng tử hóa và điều chỉnh siêu tham số) giúp hệ thống chạy ổn định tải này trên cùng 1 card GPU A10G.
2. **Propose at least 3 specific configuration adjustments** (including quantization and hyperparameter tuning) that will help the system run this workload stably on the same A10G GPU card.

#### Lời giải đề xuất:
#### Proposed Solution:
1. **Nguyên nhân lỗi:**
1. **Cause of the error:**
   * Khi người dùng tương tác, mô hình cần lưu lại ngữ cảnh hội thoại dưới dạng **KV Cache**.
   * *When users interact, the model needs to save conversation context in the form of **KV Cache**.*
   * Với độ dài ngữ cảnh tối đa `--max-model-len 8192` và 15 người dùng, dung lượng KV Cache cần thiết vượt quá khoảng VRAM trống còn lại sau khi load mô hình (24GB VRAM - 16GB mô hình = 8GB trống). Do đó, khi hàng đợi yêu cầu đầy, GPU bị tràn bộ nhớ và xảy ra lỗi OOM.
   * *With a maximum context length of `--max-model-len 8192` and 15 users, the required KV Cache size exceeds the remaining free VRAM after loading the model (24GB VRAM - 16GB model = 8GB free). Thus, when the request queue fills up, the GPU memory overflows, resulting in an OOM error.*
2. **Đề xuất 3 cấu hình khắc phục:**
2. **Proposing 3 configuration fixes:**
   * **Giải pháp 1: Lượng tử hóa mô hình (Quantization)**
   * **Solution 1: Model Quantization**
     Chuyển sang sử dụng mô hình được lượng tử hóa AWQ 4-bit (ví dụ: `Casperhansen/llama-3-8b-Instruct-awq`). Dung lượng mô hình trên VRAM sẽ giảm từ ~16GB xuống chỉ còn ~5.5GB, giải phóng hơn 18GB trống cho KV Cache.
     *Switch to using a 4-bit AWQ quantized model (e.g., `Casperhansen/llama-3-8b-Instruct-awq`). The model size on VRAM will drop from ~16GB to just ~5.5GB, freeing up over 18GB for the KV Cache.*
   * **Giải pháp 2: Điều chỉnh giới hạn độ dài ngữ cảnh (`--max-model-len`)**
   * **Solution 2: Adjusting context length limit (`--max-model-len`)**
     Nếu nghiệp vụ chatbot không đòi hỏi đọc tài liệu quá dài, hãy giảm xuống `--max-model-len 4096`. Điều này sẽ cắt giảm một nửa nhu cầu bộ nhớ KV Cache trên mỗi request của người dùng.
     *If the chatbot use case does not require reading extremely long documents, reduce it to `--max-model-len 4096`. This will cut the KV Cache memory demand per user request by half.*
   * **Giải pháp 3: Giới hạn bộ nhớ KV Cache tối đa (`--gpu-memory-utilization`)**
   * **Solution 3: Limiting max KV Cache memory (`--gpu-memory-utilization`)**
     Giảm tỷ lệ bộ nhớ phân bổ tối đa cho vLLM xuống `--gpu-memory-utilization 0.85` để dành khoảng trống an toàn cho hệ thống xử lý các tác vụ đột biến.
     *Reduce the maximum memory allocation ratio for vLLM to `--gpu-memory-utilization 0.85` to leave a safe buffer for the system to handle sudden spikes in workload.*

**Cấu hình sửa đổi tối ưu:**
**Optimized modified configuration:**
```bash
python -m vllm.entrypoints.openai.api_server \
    --model Casperhansen/llama-3-8b-Instruct-awq \
    --quantization awq \
    --gpu-memory-utilization 0.85 \
    --max-model-len 4096
```

---

### Dạng 3: Case Study Thiết kế Pipeline Data Observability
### Type 3: Case Study - Designing a Data Observability Pipeline

#### Đề bài:
#### Problem Statement:
Doanh nghiệp bảo hiểm Z tiếp nhận trung bình 50,000 ảnh chụp hóa đơn y tế mỗi ngày từ ứng dụng của khách hàng để gửi cho mô hình OCR trích xuất thông tin bồi thường. 
*Insurance company Z receives an average of 50,000 medical invoice images daily from its customer app to be sent to an OCR model for claims information extraction.*
Rất nhiều ảnh gửi lên bị mờ, sai định dạng, chụp thiếu góc hoặc bị trùng lặp, gây ra lỗi cho pipeline AI và làm sai lệch dữ liệu bồi thường của hệ thống kế toán.
*Many submitted images are blurry, improperly formatted, poorly cropped, or duplicated, causing errors in the AI pipeline and distorting the compensation data in the accounting system.*

#### Bạn hãy thiết kế kiến trúc giám sát chất lượng dữ liệu (Data Observability):
#### Please design a Data Observability architecture:
1. Đề xuất các quy tắc kiểm thử dữ liệu (Expectations) cụ thể bằng công cụ **Great Expectations** ở lớp *Silver Layer* của Medallion Architecture.
1. Propose specific data testing rules (Expectations) using the **Great Expectations** tool at the *Silver Layer* of the Medallion Architecture.
2. Thiết kế cơ chế cảnh báo lỗi tự động và luồng cô lập dữ liệu lỗi (Quarantine) để đảm bảo không làm sập pipeline OCR.
2. Design an automated error alerting mechanism and an error data isolation flow (Quarantine) to ensure the OCR pipeline does not crash.

#### Lời giải đề xuất:
#### Proposed Solution:
1. **Thiết lập quy tắc kiểm thử dữ liệu (Expectations):**
1. **Setting data testing rules (Expectations):**
   * *Độ đầy đủ (Completeness):* `expect_column_values_to_not_be_null("customer_id")` và `expect_column_values_to_not_be_null("invoice_image_path")`.
   * *Completeness:* `expect_column_values_to_not_be_null("customer_id")` and `expect_column_values_to_not_be_null("invoice_image_path")`.
   * *Định dạng hợp lệ (Validity):* `expect_column_values_to_match_regex("invoice_date", r"^\d{4}-\d{2}-\d{2}$")`.
   * *Validity:* `expect_column_values_to_match_regex("invoice_date", r"^\d{4}-\d{2}-\d{2}$")`.
   * *Tính duy nhất (Uniqueness):* `expect_column_values_to_be_unique("invoice_id")` dựa trên mã hóa hash MD5 của ảnh để chống trùng lặp.
   * *Uniqueness:* `expect_column_values_to_be_unique("invoice_id")` based on the MD5 hash of the image to prevent duplicates.
   * *Độ chính xác (Accuracy):* `expect_column_values_to_be_between("invoice_amount", min_value=0, max_value=500000000)`.
   * *Accuracy:* `expect_column_values_to_be_between("invoice_amount", min_value=0, max_value=500000000)`.
2. **Thiết kế luồng xử lý và cách cô lập (Quarantine):**
2. **Designing the processing flow and isolation method (Quarantine):**
   * Dữ liệu từ Kafka đổ về **Bronze Layer** (Lưu nguyên trạng thái thô).
   * *Data from Kafka flows into the **Bronze Layer** (Stored in its raw state).*
   * Tại bước chuyển đổi sang **Silver Layer**, luồng xử lý Spark/Python chạy Great Expectations kiểm tra dữ liệu:
   * *During the transformation step to the **Silver Layer**, a Spark/Python processing flow runs Great Expectations to test the data:*
     * Nếu dòng dữ liệu nào **Đạt kiểm thử**: Đẩy tiếp sang bảng Silver để nạp vào hệ thống mô hình OCR.
     * *If a data row **Passes tests**: Push it forward to the Silver table to be loaded into the OCR model system.*
     * Nếu dòng dữ liệu nào **Không đạt**: Đánh dấu trạng thái `status='quarantine'`, ghi nhận mã lỗi lý do và đẩy vào một DB riêng biệt dành cho việc kiểm tra tay (Human-in-the-loop review).
     * *If a data row **Fails tests**: Mark its status as `status='quarantine'`, record the error reason code, and push it to a separate DB reserved for manual review (Human-in-the-loop review).*
   * **Cảnh báo (Alerting):** Nếu tỷ lệ lỗi vượt quá mức cam kết chất lượng SLO (ví dụ >5% lượng ảnh trong 1 giờ), hệ thống tự động gửi cảnh báo (Slack/PagerDuty) cho đội ngũ Data/Operations để kịp thời can thiệp xử lý nguồn gửi dữ liệu.
   * **Alerting:** If the error rate exceeds the Service Level Objective (SLO) quality commitment (e.g., >5% of images in 1 hour), the system automatically sends alerts (Slack/PagerDuty) to the Data/Operations team for timely intervention at the data source.*
