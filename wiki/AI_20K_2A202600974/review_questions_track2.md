---
type: summary
title: "Câu hỏi ôn tập - Track2"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track2"
tags: [review, track2]
timestamp: 2026-07-06
sources: []
---

# Bộ câu hỏi ôn tập Track2
# Track2 Review Questions

### Câu hỏi ôn tập Ngày 3
### Day 3 Review Questions

1. **Theo bài giảng, điểm khác biệt chính giữa Agent và LLM Chatbot là gì?**  
   **According to the lecture, what is the main difference between an Agent and an LLM Chatbot?**  
   - A. Agent không sử dụng mô hình ngôn ngữ lớn (LLM).  
     A. An Agent does not use a large language model (LLM).  
   - B. Agent có vòng lặp tư duy dài hạn (long-horizon goal) và sử dụng tools để quan sát từng bước.  
     B. An Agent has a long-horizon goal loop and uses tools to observe step-by-step.  
   - C. LLM Chatbot có khả năng thực hiện nhiều quyết định liên tiếp hơn Agent.  
     C. An LLM Chatbot is capable of making more consecutive decisions than an Agent.  
   - D. Agent chỉ hoạt động dựa trên quy tắc cố định (rule-based).  
     D. An Agent only operates based on fixed rules (rule-based).  
   **Đáp án:** B  
   **Answer:** B

2. **Tiêu chí nào sau đây KHÔNG thuộc bộ bốn tiêu chí của Agentic Fit Framework?**  
   **Which of the following criteria does NOT belong to the four criteria of the Agentic Fit Framework?**  
   - A. Multi-step Reasoning  
     A. Multi-step Reasoning  
   - B. Tool Interaction  
     B. Tool Interaction  
   - C. High Latency Requirement  
     C. High Latency Requirement  
   - D. Long Horizon  
     D. Long Horizon  
   **Đáp án:** C  
   **Answer:** C

3. **Trong ReAct Pattern, thứ tự đúng của một vòng lặp cơ bản là:**  
   **In the ReAct Pattern, what is the correct order of a basic loop?**  
   - A. Action → Observation → Thought  
     A. Action → Observation → Thought  
   - B. Observation → Thought → Action  
     B. Observation → Thought → Action  
   - C. Thought → Action → Observation  
     C. Thought → Action → Observation  
   - D. Thought → Observation → Action  
     D. Thought → Observation → Action  
   **Đáp án:** C  
   **Answer:** C

4. **Khi gỡ lỗi (debug) Agent loop, bước đầu tiên nên kiểm tra là gì?**  
   **When debugging an Agent loop, what is the first step to check?**  
   - A. Kiểm tra tool description có đủ chi tiết không.  
     A. Check if the tool description is detailed enough.  
   - B. Xem xét "Thought" của Agent có đúng mục tiêu không.  
     B. Review if the Agent's "Thought" aligns with the goal.  
   - C. Cài đặt fallback retry ngay lập tức.  
     C. Set up a fallback retry immediately.  
   - D. Tăng số lượng tools tối đa.  
     D. Increase the maximum number of tools.  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 4
### Day 4 Review Questions

1. Theo bài giảng, một Agent đáng tin cậy được xây dựng dựa trên bốn trụ cột nào?  
   **According to the lecture, what are the four pillars a reliable Agent is built upon?**  
   - A. Prompt, Context, Tool, Control  
     A. Prompt, Context, Tool, Control  
   - B. Prompt, Memory, Tool, Evaluation  
     B. Prompt, Memory, Tool, Evaluation  
   - C. Context, RAG, Tool, Guardrail  
     C. Context, RAG, Tool, Guardrail  
   - D. Prompt, Context, Logging, Approval  
     D. Prompt, Context, Logging, Approval  
   **Đáp án:** A  
   **Answer:** A

2. Hiện tượng "Lost in the Middle" trong Context Engineering được khắc phục bằng cách nào?  
   **How is the "Lost in the Middle" phenomenon in Context Engineering mitigated?**  
   - A. Nhồi nhét tất cả thông tin vào giữa context  
     A. Cramming all information into the middle of the context  
   - B. Sắp xếp thông tin quan trọng ở đầu và cuối context  
     B. Placing important information at the beginning and the end of the context  
   - C. Lọc bỏ toàn bộ thông tin lịch sử hội thoại  
     C. Filtering out all conversation history information  
   - D. Sử dụng nhiều ví dụ hơn trong prompt  
     D. Using more examples in the prompt  
   **Đáp án:** B  
   **Answer:** B

3. Trong Tool Calling, yếu tố nào đóng vai trò như instruction để LLM quyết định chọn tool?  
   **In Tool Calling, which element acts as the instruction for the LLM to decide which tool to choose?**  
   - A. Kết quả trả về từ tool  
     A. The result returned from the tool  
   - B. Tên tool và mô tả chi tiết  
     B. The tool name and its detailed description  
   - C. Định dạng JSON của tool  
     C. The JSON format of the tool  
   - D. Số lượng tool được khai báo  
     D. The number of declared tools  
   **Đáp án:** B  
   **Answer:** B

4. Cơ chế "Human-in-the-Loop" (HITL) được áp dụng khi nào?  
   **When is the "Human-in-the-Loop" (HITL) mechanism applied?**  
   - A. Khi tool thực hiện thao tác đọc dữ liệu  
     A. When the tool performs data reading operations  
   - B. Khi tool thực hiện thao tác thay đổi trạng thái (ví dụ: thanh toán, xóa DB)  
     B. When the tool performs state-changing operations (e.g., payment, deleting DB)  
   - C. Khi LLM trả về kết quả không đúng format  
     C. When the LLM returns incorrectly formatted results  
   - D. Khi context bị nhiễu (Context Rot)  
     D. When the context is noisy (Context Rot)  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 15
### Day 15 Review Questions

1. Track 2 (AI Infrastructure & Data) trong Phase 2 tập trung đào tạo kỹ năng gì?  
   **What skills does Track 2 (AI Infrastructure & Data) in Phase 2 focus on training?**  
   - A. Phát triển mô hình AI mới và tối ưu hóa kiến trúc  
     A. Developing new AI models and optimizing architecture  
   - B. Tự dựng và vận hành backend của hệ thống AI ở mức production  
     B. Self-hosting and operating the backend of AI systems at the production level  
   - C. Thiết kế UI/UX cho ứng dụng AI  
     C. Designing UI/UX for AI applications  
   - D. Xây dựng chiến lược kinh doanh sản phẩm AI  
     D. Building business strategies for AI products  
   **Đáp án:** B  
   **Answer:** B

2. Điều kiện cứng nào được đề cập để có thể thực hành các lab về serving và FinOps trong Track 2?  
   **What is the hard requirement mentioned to be able to practice the serving and FinOps labs in Track 2?**  
   - A. Có tài khoản GitHub Enterprise  
     A. Having a GitHub Enterprise account  
   - B. Cần có GPU hoặc Cloud free-tier  
     B. Needing a GPU or a Cloud free-tier  
   - C. Phải có chứng chỉ Kubernetes  
     C. Having a Kubernetes certification  
   - D. Cần có máy tính có RAM > 32GB  
     D. Needing a computer with RAM > 32GB  
   **Đáp án:** B  
   **Answer:** B

3. Vai trò mục tiêu (CP2) nào sau đây được đề cập trong bài giảng là phù hợp với Track 2?  
   **Which of the following target roles (CP2) mentioned in the lecture is suitable for Track 2?**  
   - A. AI Researcher, Data Scientist  
     A. AI Researcher, Data Scientist  
   - B. Full-stack Developer, UX Designer  
     B. Full-stack Developer, UX Designer  
   - C. AI Data Engineer, Platform Engineer, MLOps Engineer  
     C. AI Data Engineer, Platform Engineer, MLOps Engineer  
   - D. Product Manager, AI Ethics Officer  
     D. Product Manager, AI Ethics Officer  
   **Đáp án:** C  
   **Answer:** C

4. Theo bài giảng, Track 2 phù hợp với những người có tư duy về các khái niệm nào dưới đây?  
   **According to the lecture, Track 2 is suitable for people who have a mindset about which of the following concepts?**  
   - A. UI/UX, trải nghiệm người dùng, A/B testing  
     A. UI/UX, user experience, A/B testing  
   - B. SLA, SLO, P95, Chi phí  
     B. SLA, SLO, P95, Cost  
   - C. Thiết kế đồ họa, animation, storytelling  
     C. Graphic design, animation, storytelling  
   - D. Marketing, sales, customer acquisition  
     D. Marketing, sales, customer acquisition  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 16
### Day 16 Review Questions

1. Theo chiến lược Hybrid Cloud cho AI, cách kết hợp nào sau đây được khuyến nghị để tối ưu cả chi phí và khả năng mở rộng?  
   **According to the Hybrid Cloud strategy for AI, which of the following combinations is recommended to optimize both cost and scalability?**  
   - A. Training và Serving đều dùng PaaS  
     A. Using PaaS for both Training and Serving  
   - B. Training dùng IaaS, Serving dùng PaaS  
     B. Using IaaS for Training and PaaS for Serving  
   - C. Training dùng AI-aaS, Serving dùng IaaS  
     C. Using AI-aaS for Training and IaaS for Serving  
   - D. Training dùng PaaS, Serving dùng IaaS  
     D. Using PaaS for Training and IaaS for Serving  
   **Đáp án:** B  
   **Answer:** B

2. GPU nào được mô tả là "sleeper pick" cho tác vụ Inference với mức giá $0.40-$0.86/giờ?  
   **Which GPU is described as a "sleeper pick" for Inference tasks at $0.40-$0.86/hour?**  
   - A. A100  
     A. A100  
   - B. H100  
     B. H100  
   - C. L40S  
     C. L40S  
   - D. T4  
     D. T4  
   **Đáp án:** C  
   **Answer:** C

3. Giải pháp nào giúp giảm 60-70% chi phí khi training model AI trên cloud?  
   **Which solution helps reduce AI model training costs on the cloud by 60-70%?**  
   - A. Sử dụng Reserved Instances  
     A. Using Reserved Instances  
   - B. Sử dụng Spot/Preemptible Instances  
     B. Using Spot/Preemptible Instances  
   - C. Sử dụng On-Demand Instances  
     C. Using On-Demand Instances  
   - D. Sử dụng Dedicated Hosts  
     D. Using Dedicated Hosts  
   **Đáp án:** B  
   **Answer:** B

4. Trong Kubernetes, để quản lý tài nguyên GPU cho AI workload, cấu hình nào sau đây là đúng?  
   **In Kubernetes, to manage GPU resources for AI workloads, which of the following configurations is correct?**  
   - A. Đặt requests nhỏ hơn limits cho GPU  
     A. Setting requests smaller than limits for GPUs  
   - B. Dùng `nvidia.com/gpu` với requests = limits  
     B. Using `nvidia.com/gpu` with requests = limits  
   - C. Không cần chỉ định resource requests cho GPU  
     C. No need to specify resource requests for GPUs  
   - D. Dùng `cpu` và `memory` thay vì GPU resource  
     D. Using `cpu` and `memory` instead of GPU resources  
   **Đáp án:** B  
   **Answer:** B

5. Serving engine nào sử dụng RadixAttention để tái sử dụng KV cache, tối ưu cho Agent và Multi-turn chat?  
   **Which serving engine uses RadixAttention to reuse KV cache, optimizing for Agents and Multi-turn chat?**  
   - A. vLLM  
     A. vLLM  
   - B. SGLang  
     B. SGLang  
   - C. LMDeploy  
     C. LMDeploy  
   - D. TensorRT-LLM  
     D. TensorRT-LLM  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 17
### Day 17 Review Questions

1. Trong Medallion Architecture, lớp nào chứa dữ liệu đã được làm sạch, khử trùng lặp và áp dụng schema?  
   **In the Medallion Architecture, which layer contains data that has been cleaned, deduplicated, and schema-applied?**  
   - A. Bronze  
     A. Bronze  
   - B. Silver  
     B. Silver  
   - C. Gold  
     C. Gold  
   - D. Raw  
     D. Raw  
   **Đáp án:** B  
   **Answer:** B

2. Kỹ thuật nào được sử dụng để phát hiện các bản ghi lỗi trong pipeline mà không làm hỏng toàn bộ luồng xử lý?  
   **Which technique is used to detect erroneous records in a pipeline without breaking the entire processing flow?**  
   - A. Ghi log lỗi vào file tạm  
     A. Logging errors to a temporary file  
   - B. Chuyển bản ghi lỗi vào Dead-Letter Queue (DLQ)  
     B. Moving erroneous records to a Dead-Letter Queue (DLQ)  
   - C. Dừng pipeline ngay lập tức  
     C. Stopping the pipeline immediately  
   - D. Ghi đè dữ liệu lỗi bằng giá trị null  
     D. Overwriting erroneous data with null values  
   **Đáp án:** B  
   **Answer:** B

3. Phương pháp nào giúp giảm thiểu training-serving skew bằng cách tạo features theo thời gian thực?  
   **Which method helps minimize training-serving skew by generating features in real-time?**  
   - A. Batch processing hàng ngày  
     A. Daily batch processing  
   - B. Streaming với Kafka và Flink  
     B. Streaming with Kafka and Flink  
   - C. Sử dụng File Store thay vì Feature Store  
     C. Using a File Store instead of a Feature Store  
   - D. Chỉ dùng CDC từ database  
     D. Using CDC from the database only  
   **Đáp án:** B  
   **Answer:** B

4. Trong quy trình ingestion cho LLM, bước nào diễn ra sau khi parsing dữ liệu phi cấu trúc?  
   **In the ingestion process for LLMs, which step occurs after parsing unstructured data?**  
   - A. Embedding vào Vector Store  
     A. Embedding into a Vector Store  
   - B. Chunking (ví dụ: 512 token)  
     B. Chunking (e.g., 512 tokens)  
   - C. Lưu trữ dạng raw  
     C. Storing in raw format  
   - D. Kiểm tra schema  
     D. Schema checking  
   **Đáp án:** B  
   **Answer:** B

5. "Data Flywheel" trong AI pipeline sử dụng loại dữ liệu nào làm nguồn cho lớp Bronze?  
   **What kind of data does the "Data Flywheel" in an AI pipeline use as the source for the Bronze layer?**  
   - A. Dữ liệu giao dịch tài chính  
     A. Financial transaction data  
   - B. Agent traces (prompt, tool calls, phản hồi người dùng)  
     B. Agent traces (prompts, tool calls, user feedback)  
   - C. Dữ liệu cảm biến IoT  
     C. IoT sensor data  
   - D. Log hệ thống thuần túy  
     D. Pure system logs  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 18
### Day 18 Review Questions

1. Công nghệ nào nổi bật với tính năng **Hidden Partitioning** giúp tự động trừu tượng hóa logic phân vùng khỏi người dùng?  
   **Which technology is highlighted for its **Hidden Partitioning** feature that automatically abstracts partitioning logic away from the user?**  
   - A. Delta Lake  
     A. Delta Lake  
   - B. Apache Iceberg  
     B. Apache Iceberg  
   - C. Apache Hudi  
     C. Apache Hudi  
   - D. Apache Parquet  
     D. Apache Parquet  
   **Đáp án:** B  
   **Answer:** B

2. Anti-pattern nào sau đây thường dẫn đến **vấn đề file nhỏ** trong Data Lakehouse?  
   **Which of the following anti-patterns typically leads to the **small files problem** in a Data Lakehouse?**  
   - A. Phân vùng theo cột có nhiều giá trị (cardinality cao)  
     A. Partitioning by a high-cardinality column  
   - B. Bỏ qua lệnh `OPTIMIZE`  
     B. Skipping the `OPTIMIZE` command  
   - C. Đặt `VACUUM 0 HOURS`  
     C. Setting `VACUUM 0 HOURS`  
   - D. Sử dụng Spark cho các truy vấn nhỏ  
     D. Using Spark for small queries  
   **Đáp án:** B  
   **Answer:** B

3. Trong kiến trúc Medallion, lớp nào chứa dữ liệu **bất biến (immutable) và chỉ nối thêm (append-only)**?  
   **In the Medallion Architecture, which layer contains **immutable and append-only** data?**  
   - A. Bronze  
     A. Bronze  
   - B. Silver  
     B. Silver  
   - C. Gold  
     C. Gold  
   - D. Platinum  
     D. Platinum  
   **Đáp án:** A  
   **Answer:** A

4. Để đảm bảo tính tái lập mô hình (model reproducibility), nên tích hợp **phiên bản Delta** với yếu tố nào?  
   **To ensure model reproducibility, **Delta versions** should be integrated with which of the following?**  
   - A. Mã nguồn Git  
     A. Git source code  
   - B. ID chạy MLflow (run ID)  
     B. MLflow run ID  
   - C. Dấu thời gian hệ thống  
     C. System timestamp  
   - D. Tên file Parquet  
     D. Parquet file name  
   **Đáp án:** B  
   **Answer:** B

5. Định dạng lưu trữ nào được khuyến nghị cho hiệu suất đọc cột và nén tốt trong Lakehouse?  
   **Which storage format is recommended for good columnar read performance and compression in a Lakehouse?**  
   - A. JSON  
     A. JSON  
   - B. CSV  
     B. CSV  
   - C. Parquet  
     C. Parquet  
   - D. Avro  
     D. Avro  
   **Đáp án:** C  
   **Answer:** C

---

### Câu hỏi ôn tập Ngày 19
### Day 19 Review Questions

1. **Điều gì xảy ra nếu bạn thay đổi model embedding sau khi đã index dữ liệu trong vector database?**  
   **What happens if you change the embedding model after indexing data in a vector database?**  
   - A. Vector database tự động cập nhật embedding cho tất cả dữ liệu cũ.  
     A. The vector database automatically updates embeddings for all old data.  
   - B. Không ảnh hưởng gì vì vector database lưu trữ vector độc lập với model.  
     B. No impact because the vector database stores vectors independently of the model.  
   - C. Bắt buộc phải re-index toàn bộ dữ liệu vì vector từ model cũ và mới không tương thích.  
     C. A full re-index is required because vectors from the old and new models are incompatible.  
   - D. Chỉ cần thay đổi model ở khâu query, index vẫn giữ nguyên.  
     D. Only the query model needs to be changed; the index remains the same.  
   **Đáp án:** C  
   **Answer:** C

2. **Khi các vector đã được chuẩn hóa (unit-norm), mệnh đề nào sau đây là đúng?**  
   **When vectors are unit-normalized, which of the following statements is true?**  
   - A. Cosine Similarity và Dot Product cho thứ tự xếp hạng khác nhau.  
     A. Cosine Similarity and Dot Product give different rankings.  
   - B. Thứ tự xếp hạng của Cosine, Dot Product và Euclidean Distance là giống nhau.  
     B. The ranking order of Cosine, Dot Product, and Euclidean Distance is the same.  
   - C. Chỉ có Cosine Similarity mới cho kết quả chính xác.  
     C. Only Cosine Similarity gives accurate results.  
   - D. Euclidean Distance không thể sử dụng với vector đã chuẩn hóa.  
     D. Euclidean Distance cannot be used with normalized vectors.  
   **Đáp án:** B  
   **Answer:** B

3. **Yếu tố nào được cho là chiếm tới 80% chất lượng của hệ thống RAG?**  
   **Which factor is considered to account for up to 80% of the quality in a RAG system?**  
   - A. Lựa chọn vector database (Qdrant, Weaviate).  
     A. The choice of vector database (Qdrant, Weaviate).  
   - B. Kỹ thuật ANN (HNSW, IVF).  
     B. The ANN technique (HNSW, IVF).  
   - C. Chiến lược chunking (kích thước và độ chồng lấp).  
     C. The chunking strategy (size and overlap).  
   - D. Sử dụng hybrid search kết hợp BM25.  
     D. Using hybrid search combined with BM25.  
   **Đáp án:** C  
   **Answer:** C

4. **Vấn đề "Training-Serving Skew" trong Feature Store được giải quyết bằng cách nào?**  
   **How is the "Training-Serving Skew" problem resolved in a Feature Store?**  
   - A. Sử dụng Point-in-time Join để ghép dữ liệu theo thời gian thực.  
     A. Using Point-in-time Join to stitch data in real-time.  
   - B. Đảm bảo cả huấn luyện và inference dùng cùng một bộ xử lý tính toán feature.  
     B. Ensuring both training and inference use the same feature computation processor.  
   - C. Lưu trữ tất cả features trong Online Store thay vì Offline Store.  
     C. Storing all features in the Online Store instead of the Offline Store.  
   - D. Tăng kích thước dataset để giảm sai lệch.  
     D. Increasing the dataset size to reduce skew.  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 20
### Day 20 Review Questions

1. **Chỉ số nào dưới đây được coi là thước đo quan trọng nhất trong sản xuất (production) vì nó phản ánh khả năng đáp ứng các mục tiêu về chất lượng dịch vụ (SLO)?**  
   **Which of the following metrics is considered the most important in production because it reflects the ability to meet Service Level Objectives (SLO)?**  
   - A. TTFT (Time To First Token)  
     A. TTFT (Time To First Token)  
   - B. TPOT (Time Per Output Token)  
     B. TPOT (Time Per Output Token)  
   - C. Throughput (tổng số token/giây)  
     C. Throughput (total tokens/second)  
   - D. Goodput@SLO (tốc độ yêu cầu thỏa mãn SLO của TTFT và TPOT)  
     D. Goodput@SLO (the rate of requests meeting the TTFT and TPOT SLOs)  
   **Đáp án:** D  
   **Answer:** D

2. **Kỹ thuật lượng tử hóa nào được khuyên dùng cho môi trường CPU/Edge inference và sử dụng định dạng Q4_K_M?**  
   **Which quantization technique is recommended for CPU/Edge inference environments and uses the Q4_K_M format?**  
   - A. FP8  
     A. FP8  
   - B. AWQ (4-bit)  
     B. AWQ (4-bit)  
   - C. GGUF  
     C. GGUF  
   - D. NVFP4  
     D. NVFP4  
   **Đáp án:** C  
   **Answer:** C

3. **Phát biểu nào sau đây đúng về PagedAttention?**  
   **Which of the following statements about PagedAttention is true?**  
   - A. Chỉ hoạt động trên kiến trúc GPT, không hỗ trợ các mô hình khác.  
     A. It only works on GPT architectures and doesn't support other models.  
   - B. Loại bỏ phân mảnh bộ nhớ KV cache và cho phép continuous batching, tăng throughput lên đến 24x.  
     B. It eliminates KV cache memory fragmentation and enables continuous batching, increasing throughput by up to 24x.  
   - C. Là phương pháp nén KV cache bằng cách chiếu xuống không gian tiềm ẩn (latent space).  
     C. It is a KV cache compression method by projecting into the latent space.  
   - D. Yêu cầu phần cứng chuyên dụng (NVIDIA Hopper) và không thể chạy trên GPU thế hệ cũ.  
     D. It requires specialized hardware (NVIDIA Hopper) and cannot run on older generation GPUs.  
   **Đáp án:** B  
   **Answer:** B

4. **Trong các chiến lược song song hóa, kỹ thuật nào tách biệt pha prefill và decode thành các cụm (pool) riêng để tránh tắc nghẽn do các prompt dài?**  
   **Among parallelization strategies, which technique separates the prefill and decode phases into separate pools to avoid bottlenecks caused by long prompts?**  
   - A. Tensor Parallelism (TP)  
     A. Tensor Parallelism (TP)  
   - B. Pipeline Parallelism (PP)  
     B. Pipeline Parallelism (PP)  
   - C. Expert Parallelism (EP)  
     C. Expert Parallelism (EP)  
   - D. Disaggregated Serving  
     D. Disaggregated Serving  
   **Đáp án:** D  
   **Answer:** D

---

### Câu hỏi ôn tập Ngày 21
### Day 21 Review Questions

1. Điểm khác biệt cốt lõi nhất khi áp dụng CI/CD cho hệ thống AI so với phần mềm thông thường là gì?  
   **What is the core difference when applying CI/CD to AI systems compared to traditional software?**  
   - A. Cần tự động hóa việc kiểm thử giao diện người dùng.  
     A. UI testing needs to be automated.  
   - B. Phải quản lý phiên bản dữ liệu và theo dõi thí nghiệm để ngăn model regression.  
     B. Data versions must be managed and experiments tracked to prevent model regression.  
   - C. Không cần kiểm thử vì model luôn hoạt động tốt.  
     C. Testing is unnecessary because the model always works well.  
   - D. Chỉ sử dụng một công cụ duy nhất cho toàn bộ pipeline.  
     D. Only one single tool is used for the entire pipeline.  
   **Đáp án:** B  
   **Answer:** B

2. Trong MLflow, chức năng Model Registry được sử dụng chủ yếu để làm gì?  
   **In MLflow, what is the Model Registry primarily used for?**  
   - A. Lưu trữ dữ liệu huấn luyện dưới dạng artifact.  
     A. Storing training data as artifacts.  
   - B. So sánh các runs trên giao diện UI.  
     B. Comparing runs on the UI.  
   - C. Quản lý vòng đời mô hình, bao gồm staging, production và versioning.  
     C. Managing the model lifecycle, including staging, production, and versioning.  
   - D. Tự động deploy model lên production không cần kiểm tra.  
     D. Automatically deploying the model to production without testing.  
   **Đáp án:** C  
   **Answer:** C

3. Khi sử dụng DVC, lệnh nào được dùng để chạy lại toàn bộ pipeline một cách tái lập (reproducible)?  
   **When using DVC, which command is used to rerun the entire pipeline reproducibly?**  
   - A. `dvc run`  
     A. `dvc run`  
   - B. `dvc push`  
     B. `dvc push`  
   - C. `dvc repro`  
     C. `dvc repro`  
   - D. `dvc commit`  
     D. `dvc commit`  
   **Đáp án:** C  
   **Answer:** C

4. Chiến lược triển khai nào cho phép chạy model mới song song với model cũ mà không ảnh hưởng đến người dùng, chỉ để thu thập log và so sánh?  
   **Which deployment strategy allows running a new model in parallel with the old one without affecting users, strictly for logging and comparison?**  
   - A. Canary deployment  
     A. Canary deployment  
   - B. Blue/Green deployment  
     B. Blue/Green deployment  
   - C. Shadow deployment  
     C. Shadow deployment  
   - D. Rolling deployment  
     D. Rolling deployment  
   **Đáp án:** C  
   **Answer:** C

---

### Câu hỏi ôn tập Ngày 22
### Day 22 Review Questions

1. Điểm khác biệt cốt lõi giữa LLMOps và MLOps truyền thống là gì?  
   **What is the core difference between LLMOps and traditional MLOps?**  
   - A. LLMOps tập trung vào quản lý dữ liệu hơn là code  
     A. LLMOps focuses more on data management than code.  
   - B. LLMOps coi việc quản lý phiên bản Prompt quan trọng như quản lý code và data  
     B. LLMOps treats Prompt version management as critically as code and data management.  
   - C. MLOps không cần đến evaluation  
     C. MLOps does not require evaluation.  
   - D. LLMOps chỉ dùng cho các mô hình ngôn ngữ nhỏ  
     D. LLMOps is only used for small language models.  
   **Đáp án:** B  
   **Answer:** B

2. Công cụ nào được mô tả như "GitHub dành riêng cho prompt" trong bài giảng?  
   **Which tool is described as "GitHub specifically for prompts" in the lecture?**  
   - A. LangSmith  
     A. LangSmith  
   - B. W&B Weave  
     B. W&B Weave  
   - C. Prompt Hub  
     C. Prompt Hub  
   - D. RAGAS  
     D. RAGAS  
   **Đáp án:** C  
   **Answer:** C

3. Theo bài giảng, RAGAS được sử dụng để đánh giá những khía cạnh nào của LLM?  
   **According to the lecture, what aspects of LLMs is RAGAS used to evaluate?**  
   - A. Chỉ độ chính xác (accuracy)  
     A. Only accuracy  
   - B. Tốc độ inference và chi phí  
     B. Inference speed and cost  
   - C. Faithfulness, relevance và hallucination  
     C. Faithfulness, relevance, and hallucination  
   - D. Khả năng phát hiện Prompt Injection  
     D. The ability to detect Prompt Injection  
   **Đáp án:** C  
   **Answer:** C

4. Một trong những mục tiêu của Guardrails & Safety Monitoring là gì?  
   **What is one of the goals of Guardrails & Safety Monitoring?**  
   - A. Tăng tốc độ sinh token  
     A. Increasing token generation speed  
   - B. Chặn lộ thông tin cá nhân (PII) và phát hiện Prompt Injection  
     B. Blocking PII leakage and detecting Prompt Injection  
   - C. Tự động tạo prompt mới từ dữ liệu  
     C. Automatically generating new prompts from data  
   - D. Tối ưu hóa chi phí API  
     D. Optimizing API costs  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 23
### Day 23 Review Questions

1. Theo bài giảng, ngoài các golden signals truyền thống, LLM cần thêm những tín hiệu nào để đảm bảo observability?  
   **According to the lecture, besides the traditional golden signals, what additional signals do LLMs need to ensure observability?**  
   - A. Latency, traffic, errors, saturation  
     A. Latency, traffic, errors, saturation  
   - B. Token throughput, hallucination rate, output length distribution, tool-call failure rate  
     B. Token throughput, hallucination rate, output length distribution, tool-call failure rate  
   - C. CPU usage, memory usage, disk I/O  
     C. CPU usage, memory usage, disk I/O  
   - D. Number of users, number of requests, status codes  
     D. Number of users, number of requests, status codes  
   **Đáp án:** B  
   **Answer:** B

2. Cardinality là “kẻ giết hóa đơn thầm lặng” vì:  
   **Cardinality is the “silent bill killer” because:**  
   - A. Nó làm tăng độ trễ của hệ thống  
     A. It increases system latency  
   - B. Nó làm tăng số lượng unique label combinations, dẫn đến chi phí lưu trữ và xử lý cao  
     B. It increases the number of unique label combinations, leading to high storage and processing costs  
   - C. Nó làm giảm số lượng metrics có thể thu thập  
     C. It reduces the number of collectable metrics  
   - D. Nó gây lỗi khi sử dụng Prometheus  
     D. It causes errors when using Prometheus  
   **Đáp án:** B  
   **Answer:** B

3. Sự tiến hóa từ DevOps lên AgentOps được mô tả trong “The Ops Trinity” bao gồm:  
   **The evolution from DevOps to AgentOps described in “The Ops Trinity” includes:**  
   - A. DevOps → MLOps → LLMOps → AgentOps  
     A. DevOps → MLOps → LLMOps → AgentOps  
   - B. DevOps → LLMOps → MLOps → AgentOps  
     B. DevOps → LLMOps → MLOps → AgentOps  
   - C. DevOps → AgentOps → MLOps → LLMOps  
     C. DevOps → AgentOps → MLOps → LLMOps  
   - D. MLOps → DevOps → LLMOps → AgentOps  
     D. MLOps → DevOps → LLMOps → AgentOps  
   **Đáp án:** A  
   **Answer:** A

4. Theo bài giảng, telemetry từ các ngày trước được tích hợp vào Day 23, ví dụ:  
   **According to the lecture, telemetry from previous days is integrated into Day 23, for example:**  
   - A. Ngày 16: Spark UI metrics  
     A. Day 16: Spark UI metrics  
   - B. Ngày 19: GPU util (DCGM)  
     B. Day 19: GPU util (DCGM)  
   - C. Ngày 22: Eval-pass-rate dưới dạng Prometheus gauge  
     C. Day 22: Eval-pass-rate as a Prometheus gauge  
   - D. Ngày 17: llama.cpp tokens/sec  
     D. Day 17: llama.cpp tokens/sec  
   **Đáp án:** C  
   **Answer:** C

---

### Câu hỏi ôn tập Ngày 24
### Day 24 Review Questions

1. Theo nguyên tắc Least Privilege, role nào sau đây có quyền xóa dữ liệu production?  
   **According to the Least Privilege principle, which of the following roles has permission to delete production data?**  
   - A. ML Engineer  
     A. ML Engineer  
   - B. Data Analyst  
     B. Data Analyst  
   - C. Admin  
     C. Admin  
   - D. Service Account  
     D. Service Account  
   **Đáp án:** C  
   **Answer:** C

2. Trong mô hình envelope encryption, Data Encryption Key (DEK) được bảo vệ như thế nào?  
   **In the envelope encryption model, how is the Data Encryption Key (DEK) protected?**  
   - A. Lưu trữ dưới dạng plaintext trong code  
     A. Stored as plaintext in code  
   - B. Được mã hóa bởi Key Encryption Key (KEK)  
     B. Encrypted by a Key Encryption Key (KEK)  
   - C. Xoay vòng hàng năm thay vì hàng tháng  
     C. Rotated annually instead of monthly  
   - D. Được nhúng trực tiếp vào mô hình  
     D. Embedded directly into the model  
   **Đáp án:** B  
   **Answer:** B

3. Kỹ thuật xử lý PII nào có thể đảo ngược và thường được dùng cho phân tích nội bộ?  
   **Which PII processing technique is reversible and commonly used for internal analysis?**  
   - A. Anonymization  
     A. Anonymization  
   - B. Masking  
     B. Masking  
   - C. Hashing  
     C. Hashing  
   - D. De-identification  
     D. De-identification  
   **Đáp án:** D  
   **Answer:** D

4. Trong Security Testing Pyramid, công cụ nào được sử dụng để phát hiện secret bị lộ trong kho lưu trữ mã nguồn?  
   **In the Security Testing Pyramid, which tool is used to detect exposed secrets in a source code repository?**  
   - A. Bandit (SAST)  
     A. Bandit (SAST)  
   - B. pip-audit (Dependency Scanning)  
     B. pip-audit (Dependency Scanning)  
   - C. truffleHog (Secret Scanning)  
     C. truffleHog (Secret Scanning)  
   - D. Garak (Prompt Injection Testing)  
     D. Garak (Prompt Injection Testing)  
   **Đáp án:** C  
   **Answer:** C

---

### Câu hỏi ôn tập Ngày 25
### Day 25 Review Questions

1. Theo bài giảng, dấu hiệu nào cho thấy cần phải right-sizing GPU ngay lập tức?  
   **According to the lecture, which sign indicates that immediate GPU right-sizing is needed?**  
   - A. GPU utilization < 50%  
     A. GPU utilization < 50%  
   - B. GPU utilization < 30%  
     B. GPU utilization < 30%  
   - C. MFU < 50%  
     C. MFU < 50%  
   - D. MBU < 30%  
     D. MBU < 30%  
   **Đáp án:** B  
   **Answer:** B

2. Chiến lược nào giúp tận dụng spot instances với mức giảm 60-70% chi phí mà vẫn đảm bảo độ tin cậy?  
   **Which strategy helps leverage spot instances for a 60-70% cost reduction while still ensuring reliability?**  
   - A. Chỉ sử dụng 100% spot instances  
     A. Using 100% spot instances only  
   - B. Mixed Fleet Strategy: 20% on-demand + 80% spot, kết hợp checkpoint thường xuyên  
     B. Mixed Fleet Strategy: 20% on-demand + 80% spot, combined with frequent checkpointing  
   - C. Sử dụng on-demand cho training và spot cho inference  
     C. Using on-demand for training and spot for inference  
   - D. Dùng reserved instances thay cho spot  
     D. Using reserved instances instead of spot  
   **Đáp án:** B  
   **Answer:** B

3. Để theo dõi hiệu suất GPU, chỉ số nào đặc biệt quan trọng đối với tác vụ compute-bound (ví dụ: training, prefill)?  
   **To monitor GPU performance, which metric is particularly important for compute-bound tasks (e.g., training, prefill)?**  
   - A. GPU Utilization  
     A. GPU Utilization  
   - B. MBU (Memory Bandwidth Utilization)  
     B. MBU (Memory Bandwidth Utilization)  
   - C. MFU (Model FLOPs Utilization)  
     C. MFU (Model FLOPs Utilization)  
   - D. Cache hit rate  
     D. Cache hit rate  
   **Đáp án:** C  
   **Answer:** C

4. Kỹ thuật nào trong inference optimization giúp giảm chi phí per token bằng cách sử dụng mô hình nhỏ hơn cho hầu hết các truy vấn đơn giản?  
   **Which inference optimization technique helps reduce per-token cost by using smaller models for most simple queries?**  
   - A. Request Batching  
     A. Request Batching  
   - B. Caching  
     B. Caching  
   - C. Model Cascading  
     C. Model Cascading  
   - D. Disaggregated Serving  
     D. Disaggregated Serving  
   **Đáp án:** C  
   **Answer:** C

5. Để phân bổ chi phí GPU cho các nhóm (chargeback), bài giảng khuyến nghị sử dụng chiến lược nào?  
   **To allocate GPU costs to teams (chargeback), which strategy does the lecture recommend?**  
   - A. Tính chi phí trung bình cho tất cả nhóm  
     A. Calculating an average cost for all teams  
   - B. Thiết lập tagging (team, project, env) và dùng Kubecost để phân tích  
     B. Setting up tagging (team, project, env) and using Kubecost for analysis  
   - C. Dùng một tài khoản cloud duy nhất không phân chia  
     C. Using a single undivided cloud account  
   - D. Chỉ theo dõi tổng chi phí hàng tháng  
     D. Only tracking total monthly costs  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 26
### Day 26 Review Questions

1. **MCP (Model Context Protocol) cung cấp những primitives nào để LLM tương tác với công cụ và dữ liệu?**  
   **What primitives does the MCP (Model Context Protocol) provide for LLMs to interact with tools and data?**  
   - A. Tools, Resources, Prompts  
     A. Tools, Resources, Prompts  
   - B. Agents, Tasks, Messages  
     B. Agents, Tasks, Messages  
   - C. Orchestrator, Specialist, Router  
     C. Orchestrator, Specialist, Router  
   - D. Redis, PostgreSQL, FastAPI  
     D. Redis, PostgreSQL, FastAPI  
   **Đáp án:** A  
   **Answer:** A

2. **Trong giao thức A2A, một task có thể chuyển sang trạng thái nào để yêu cầu thêm thông tin từ caller thay vì thất bại ngay lập tức?**  
   **In the A2A protocol, what state can a task transition to in order to request more information from the caller instead of failing immediately?**  
   - A. Submitted  
     A. Submitted  
   - B. Working  
     B. Working  
   - C. Input Required  
     C. Input Required  
   - D. Canceled  
     D. Canceled  
   **Đáp án:** C  
   **Answer:** C

3. **Chiến lược routing nào được mô tả là linh hoạt nhất nhưng chậm và tốn kém?**  
   **Which routing strategy is described as the most flexible but slow and expensive?**  
   - A. Keyword-based  
     A. Keyword-based  
   - B. Embedding-based (Semantic Routing)  
     B. Embedding-based (Semantic Routing)  
   - C. LLM-based  
     C. LLM-based  
   - D. Fallback chains  
     D. Fallback chains  
   **Đáp án:** C  
   **Answer:** C

4. **Theo bài giảng, phương pháp quản lý trạng thái nào được khuyến nghị ban đầu vì dễ mở rộng theo chiều ngang?**  
   **According to the lecture, which state management method is initially recommended because it scales horizontally easily?**  
   - A. Stateful với sticky sessions  
     A. Stateful with sticky sessions  
   - B. Stateless với context lưu trong Redis hoặc PostgreSQL  
     B. Stateless with context stored in Redis or PostgreSQL  
   - C. Stateful với lưu trữ cục bộ  
     C. Stateful with local storage  
   - D. Stateless không lưu context  
     D. Stateless not storing context  
   **Đáp án:** B  
   **Answer:** B

5. **Nguyên tắc bảo mật nào yêu cầu con người phải phê duyệt các hành động rủi ro cao như ghi cơ sở dữ liệu?**  
   **Which security principle requires human approval for high-risk actions like writing to a database?**  
   - A. Rate Limiting  
     A. Rate Limiting  
   - B. Sandbox Execution  
     B. Sandbox Execution  
   - C. Human-in-the-Loop (HITL)  
     C. Human-in-the-Loop (HITL)  
   - D. Minimal Capability  
     D. Minimal Capability  
   **Đáp án:** C  
   **Answer:** C

---

### Câu hỏi ôn tập Ngày 27
### Day 27 Review Questions

1. Điểm khác biệt cốt lõi giữa **Pipeline Monitoring** và **Data Observability** là gì?  
   **What is the core difference between **Pipeline Monitoring** and **Data Observability**?**  
   - A. Pipeline Monitoring chỉ kiểm tra thời gian chạy, còn Data Observability kiểm tra tính đúng đắn của dữ liệu.  
     A. Pipeline Monitoring only checks runtime, while Data Observability checks data correctness.  
   - B. Pipeline Monitoring dùng cho batch, Data Observability dùng cho streaming.  
     B. Pipeline Monitoring is used for batch, Data Observability is used for streaming.  
   - C. Pipeline Monitoring tập trung vào logs, Data Observability tập trung vào schema.  
     C. Pipeline Monitoring focuses on logs, Data Observability focuses on schema.  
   - D. Không có sự khác biệt, cả hai đều giống nhau.  
     D. There is no difference, both are the same.  
   **Đáp án:** A  
   **Answer:** A

2. Trong 5 trụ cột của Data Observability, trụ cột nào phát hiện sự thay đổi về tên cột hoặc kiểu dữ liệu?  
   **Among the 5 pillars of Data Observability, which pillar detects changes in column names or data types?**  
   - A. Freshness  
     A. Freshness  
   - B. Volume  
     B. Volume  
   - C. Schema  
     C. Schema  
   - D. Lineage  
     D. Lineage  
   **Đáp án:** C  
   **Answer:** C

3. Trong Great Expectations, **Checkpoint** có vai trò gì?  
   **In Great Expectations, what is the role of a **Checkpoint**?**  
   - A. Lưu trữ các rule kiểm tra dữ liệu (Expectation Suite).  
     A. Storing data validation rules (Expectation Suite).  
   - B. Tích hợp Expectation Suite vào pipeline sản xuất và kích hoạt hành động (alert, block) khi thất bại.  
     B. Integrating the Expectation Suite into the production pipeline and triggering actions (alert, block) upon failure.  
   - C. Tự động sinh dữ liệu mẫu để kiểm tra.  
     C. Automatically generating sample data for testing.  
   - D. Thay thế hoàn toàn cho dbt tests.  
     D. Completely replacing dbt tests.  
   **Đáp án:** B  
   **Answer:** B

4. Trong SLO Engineering, **Error Budget** được sử dụng để làm gì?  
   **In SLO Engineering, what is the **Error Budget** used for?**  
   - A. Đo lường mức độ tươi mới của dữ liệu.  
     A. Measuring data freshness.  
   - B. Cân bằng giữa tính ổn định và tính năng mới: nếu ngân sách lỗi cạn kiệt, ưu tiên sửa lỗi thay vì phát hành tính năng.  
     B. Balancing stability and new features: if the error budget is depleted, prioritize bug fixes over feature releases.  
   - C. Xác định ngưỡng cảnh báo cho anomaly detection.  
     C. Determining the alert threshold for anomaly detection.  
   - D. Phân loại mức độ nghiêm trọng của sự cố (P0-P3).  
     D. Classifying incident severity (P0-P3).  
   **Đáp án:** B  
   **Answer:** B

---

### Câu hỏi ôn tập Ngày 28
### Day 28 Review Questions

1. Theo bài giảng, đâu là **anti-pattern** trong tích hợp các thành phần AI Platform?  
   **According to the lecture, what is an **anti-pattern** in integrating AI Platform components?**  
   - A. Sử dụng event-driven integration với Kafka  
     A. Using event-driven integration with Kafka  
   - B. Duy trì cấu hình trong Git (GitOps)  
     B. Maintaining configuration in Git (GitOps)  
   - C. Gắn kết chặt chẽ (tightly coupled) giữa các thành phần  
     C. Tightly coupling between components  
   - D. Áp dụng Bulkhead pattern để tách biệt inference và training  
     D. Applying the Bulkhead pattern to separate inference and training  
   **Đáp án:** C  
   **Answer:** C

2. Trong luồng request end-to-end, thời gian mục tiêu cho mỗi thành phần là bao nhiêu?  
   **In the end-to-end request flow, what is the target time for each component?**  
   - A. Vector Search < 5ms, Feature Store < 50ms, LLM Inference < 500ms  
     A. Vector Search < 5ms, Feature Store < 50ms, LLM Inference < 500ms  
   - B. Feature Store < 5ms, Vector Search < 50ms, LLM Inference < 500ms  
     B. Feature Store < 5ms, Vector Search < 50ms, LLM Inference < 500ms  
   - C. Feature Store < 50ms, Vector Search < 500ms, LLM Inference < 5ms  
     C. Feature Store < 50ms, Vector Search < 500ms, LLM Inference < 5ms  
   - D. Tất cả đều cần dưới 100ms  
     D. All need to be under 100ms  
   **Đáp án:** B  
   **Answer:** B

3. Công cụ nào được khuyến nghị để **phân tích chi tiết độ trễ (latency breakdown)** trong toàn bộ luồng?  
   **Which tool is recommended for **detailed latency breakdown analysis** across the entire flow?**  
   - A. Py-spy  
     A. Py-spy  
   - B. Tracemalloc  
     B. Tracemalloc  
   - C. Jaeger  
     C. Jaeger  
   - D. cProfile  
     D. cProfile  
   **Đáp án:** C  
   **Answer:** C

4. Điều kiện tiên quyết để triển khai Platform ra production theo 5 Pillars là gì?  
   **What is the prerequisite for deploying the Platform to production according to the 5 Pillars?**  
   - A. Kiểm tra checklist Production Readiness bằng tay bởi kỹ sư  
     A. Manual checking of the Production Readiness checklist by an engineer  
   - B. Tự động hóa checklist trong CI pipeline  
     B. Automating the checklist in the CI pipeline  
   - C. Đảm bảo tất cả code đều chạy trên môi trường local  
     C. Ensuring all code runs in the local environment  
   - D. Sử dụng duy nhất một framework cho toàn bộ stack  
     D. Using a single framework for the entire stack  
   **Đáp án:** B  
   **Answer:** B

5. Mô hình nào sau đây là **integration pattern** đúng để tránh shared mutable state?  
   **Which of the following models is the correct **integration pattern** to avoid shared mutable state?**  
   - A. Dùng cơ sở dữ liệu chung có thể ghi đồng thời  
     A. Using a shared database with concurrent writes  
   - B. Immutable events và event sourcing qua append-only log (Kafka)  
     B. Immutable events and event sourcing via append-only log (Kafka)  
   - C. Lưu trạng thái trong biến toàn cục (global variable)  
     C. Storing state in a global variable  
   - D. Sử dụng file cấu hình JSON tĩnh  
     D. Using a static JSON configuration file  
   **Đáp án:** B  
   **Answer:** B
