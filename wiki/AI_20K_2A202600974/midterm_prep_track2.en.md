---
type: concept
title: "Midterm Exam Preparation - Track 2 (Infrastructure/LLMOps)"
description: "Bộ tài liệu và câu hỏi ôn tập thi giữa kỳ Chương trình Phát triển Năng lực AI Thực Chiến dành cho Track 2 (Infrastructure/LLMOps)"
tags: [ai, 20k, exam, prep, track2]
timestamp: 2026-07-06
sources: ["wiki/AI_20K_2A202600974/day16_track2.md", "wiki/AI_20K_2A202600974/day18_track2.md", "wiki/AI_20K_2A202600974/day20_track2.md", "wiki/AI_20K_2A202600974/day21_track2.md", "wiki/AI_20K_2A202600974/day23_track2.md", "wiki/AI_20K_2A202600974/day27_track2.md"]
---
# MIDTERM EXAM PREPARATION — TRACK 2 (INFRASTRUCTURE / LLMOPS)

This document synthesizes key concepts and in-depth review questions (Multiple Choice, Multi-select, Scenario Debug, Case Study) closely aligned with the **Track 2: Infrastructure / Data Lakehouse / LLMOps** portion of the midterm exam.

---

## PART I: CORE KNOWLEDGE TRACK 2

### 1. Data Lakehouse & Ingestion Pipelines
*### 1. Data Lakehouse & Ingestion Pipelines*
* **Medallion Architecture:** 3-layer data architecture:
  * **Bronze Layer (Raw):** Stores raw, append-only data directly from sources (Kafka, APIs, files) without transformation.
  * **Silver Layer (Cleansed/Conformed):** Data is cleaned, standardized by data type, deduplicated, and initial Data Contracts are applied.
  * **Gold Layer (Business/Curated):** Data is aggregated according to business needs, directly serving BI, Analytics, and feeding into Vector Stores for RAG.
* **Storage Formats (Delta Lake / Apache Iceberg):** Supports ACID properties on Object Storage (S3, GCS), provides time travel mechanisms (retrieving old data versions), and Schema Evolution.
* **Inference Data Pipeline:** Streaming data via Kafka/Flink is aggregated and loaded into real-time Feature Stores for immediate use by Agents.

### 2. Model Serving & Inference Optimization
*### 2. Model Serving & Inference Optimization*
* **vLLM & SGLang:** High-performance Model Serving tools.
* **PagedAttention:** A GPU memory optimization solution that divides **KV Cache** memory into non-contiguous physical pages (similar to Virtual Memory in OS). It increases throughput by 2-4x and reduces GPU memory waste to near 0%.
* **Quantization:** Reduces model size by changing the floating-point precision of weights (e.g., from FP16 to INT8 or INT4).
  * **GGUF:** Suitable for CPU/Edge/Localhost execution (using llama.cpp).
  * **GPTQ / AWQ:** Suitable for commercial GPU serving on the cloud.
* **GPU FinOps:**
* ***GPU FinOps:***
  * Utilizing Spot Instances to reduce training costs by up to 70-80% (requires integration of checkpoint auto-recovery mechanisms).
  * GPU Right-sizing to prevent resource waste when the model runs at low loads.

### 3. CI/CD for AI & ML Lifecycle
*### 3. CI/CD for AI & ML Lifecycle*
* **DVC (Data Version Control):** Manages versions of large data and models with Git without storing heavy files directly in Git. DVC stores heavy files on cloud storage (S3, GCS) and generates small `.dvc` files containing hashes for Git tracking.
* **MLflow:**
* ***MLflow:***
  * **Tracking:** Logs hyperparameters, metrics (Loss, Accuracy), and artifacts of each experiment run.
  * **Model Registry:** Manages model versions and their lifecycle stages (Staging, Production, Archived).
* **GitHub Actions pipeline:** Automatically runs unit tests, linters, packages the Docker Image containing the model, and deploys to Kubernetes/EKS upon code changes.

### 4. Data Observability & Quality
*### 4. Data Observability & Quality*
* **7 dimensions of data quality measurement:**
* **Great Expectations:** A Python library that automates data testing through defined rules (Expectations), automatically generating quality reports before ingestion into AI pipelines.
* **Data Contracts & Lineage:** Agreements on data formatting between producers and consumers. Lineage diagrams help trace the data flow from raw sources to model outputs for system debugging.

---

## PRACTICAL REVIEW QUESTIONS (TRACK 2)

### Type 1: Multiple Choice & Multi-Select

#### Question 1 (Multi-select): When designing a Model Serving system using vLLM in production, which configurations help optimize performance for serving multiple concurrent users (High Throughput)? (Select all correct answers)
- [x] A. Enable PagedAttention to dynamically allocate KV Cache memory and eliminate GPU memory fragmentation.
- [ ] B. Convert the model format to GGUF for optimal execution on dedicated NVIDIA GPU server clusters.
- [x] C. Utilize the Continuous Batching mechanism to group incoming client requests into the current processing batch without waiting for the previous batch to completely finish.
- [x] D. Apply Tensor Parallelism (TP) to split the model across multiple GPUs on the same node to accelerate the generation time of a new token (Latency per token).

*Explanation: GGUF (B) is only optimized for CPUs or edge devices, and is unsuitable for dedicated GPU Server infrastructure (where GPTQ/AWQ dominates). Options A, C, and D are all core techniques for optimizing throughput and latency in vLLM.*

#### Question 2 (Single choice): In a CI/CD system for AI using Git and DVC, which file is actually committed to GitHub to manage the versioning of a 10GB dataset?
- ( ) A. The entire directory containing that 10GB raw dataset.
- (x) B. A small metadata file with a `.dvc` extension (containing the hash code and dataset size) generated by DVC.
- ( ) C. A compressed Docker Image file containing that dataset.
- ( ) D. A download link for the dataset saved in the `.gitignore` configuration.

*Explanation: DVC stores the heavy 10GB file in external Cloud Storage and generates a `.dvc` file (just a few KB) containing the hash code for Git to track data versions.*

---

### Type 2: Scenario Debug (Handling OOM Errors in Model Serving)

#### Scenario:
An enterprise Chatbot system is running on 1 NVIDIA A10G GPU (24GB VRAM) using vLLM to serve the `Llama-3-8B-Instruct` model (original FP16 size is ~16GB VRAM).
When the number of concurrent users increases to 15, the system reports a **CUDA Out of Memory (OOM)** error and the Server crashes.
Checking your current startup configuration:

```bash
python -m vllm.entrypoints.openai.api_server \
    --model meta-llama/Meta-Llama-3-8B-Instruct \
    --gpu-memory-utilization 0.90 \
    --max-model-len 8192
```

#### Debugging Questions:
1. **Why does the OOM error occur** when concurrent users hit 15, even though the original model size (~16GB) is smaller than the GPU's VRAM capacity (24GB)?
2. **Propose at least 3 specific configuration adjustments** (including quantization and hyperparameter tuning) that will help the system run this workload stably on the same A10G GPU card.

#### Proposed Solution:
1. **Cause of the error:**
   * When users interact, the model needs to save conversation context in the form of **KV Cache**.
   * With a maximum context length of `--max-model-len 8192` and 15 users, the required KV Cache size exceeds the remaining free VRAM after loading the model (24GB VRAM - 16GB model = 8GB free). Thus, when the request queue fills up, the GPU memory overflows, resulting in an OOM error.
2. **Proposing 3 configuration fixes:**
   * **Solution 1: Model Quantization**
     Switch to using a 4-bit AWQ quantized model (e.g., `Casperhansen/llama-3-8b-Instruct-awq`). The model size on VRAM will drop from ~16GB to just ~5.5GB, freeing up over 18GB for the KV Cache.
   * **Solution 2: Adjusting context length limit (`--max-model-len`)**
     If the chatbot use case does not require reading extremely long documents, reduce it to `--max-model-len 4096`. This will cut the KV Cache memory demand per user request by half.
   * **Solution 3: Limiting max KV Cache memory (`--gpu-memory-utilization`)**
     Reduce the maximum memory allocation ratio for vLLM to `--gpu-memory-utilization 0.85` to leave a safe buffer for the system to handle sudden spikes in workload.

**Optimized modified configuration:**
```bash
python -m vllm.entrypoints.openai.api_server \
    --model Casperhansen/llama-3-8b-Instruct-awq \
    --quantization awq \
    --gpu-memory-utilization 0.85 \
    --max-model-len 4096
```

---

### Type 3: Case Study - Designing a Data Observability Pipeline

#### Problem Statement:
Insurance company Z receives an average of 50,000 medical invoice images daily from its customer app to be sent to an OCR model for claims information extraction.
Many submitted images are blurry, improperly formatted, poorly cropped, or duplicated, causing errors in the AI pipeline and distorting the compensation data in the accounting system.

#### Please design a Data Observability architecture:
1. Propose specific data testing rules (Expectations) using the **Great Expectations** tool at the *Silver Layer* of the Medallion Architecture.
2. Design an automated error alerting mechanism and an error data isolation flow (Quarantine) to ensure the OCR pipeline does not crash.

#### Proposed Solution:
1. **Setting data testing rules (Expectations):**
   * *Completeness:* `expect_column_values_to_not_be_null("customer_id")` and `expect_column_values_to_not_be_null("invoice_image_path")`.
   * *Validity:* `expect_column_values_to_match_regex("invoice_date", r"^\d{4}-\d{2}-\d{2}$")`.
   * *Uniqueness:* `expect_column_values_to_be_unique("invoice_id")` based on the MD5 hash of the image to prevent duplicates.
   * *Accuracy:* `expect_column_values_to_be_between("invoice_amount", min_value=0, max_value=500000000)`.
2. **Designing the processing flow and isolation method (Quarantine):**
   * Data from Kafka flows into the **Bronze Layer** (Stored in its raw state).
   * During the transformation step to the **Silver Layer**, a Spark/Python processing flow runs Great Expectations to test the data:
     * If a data row **Passes tests**: Push it forward to the Silver table to be loaded into the OCR model system.
     * If a data row **Fails tests**: Mark its status as `status='quarantine'`, record the error reason code, and push it to a separate DB reserved for manual review (Human-in-the-loop review).
   * **Alerting:** If the error rate exceeds the Service Level Objective (SLO) quality commitment (e.g., >5% of images in 1 hour), the system automatically sends alerts (Slack/PagerDuty) to the Data/Operations team for timely intervention at the data source.
