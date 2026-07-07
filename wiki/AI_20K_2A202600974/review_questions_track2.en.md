---
type: summary
title: "Câu hỏi ôn tập - Track2"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track2"
tags: [review, track2]
timestamp: 2026-07-06
sources: []
---
# Track2 Review Questions

### Day 3 Review Questions

1. **According to the lecture, what is the main difference between an Agent and an LLM Chatbot?**  
   - A. An Agent does not use a large language model (LLM).  
   - B. An Agent has a long-horizon goal loop and uses tools to observe step-by-step.  
   - C. An LLM Chatbot is capable of making more consecutive decisions than an Agent.  
   - D. An Agent only operates based on fixed rules (rule-based).  
   **Answer:** B  

2. **Which of the following criteria does NOT belong to the four criteria of the Agentic Fit Framework?**  
   - A. Multi-step Reasoning  
     *A. Multi-step Reasoning*  
   - B. Tool Interaction  
     *B. Tool Interaction*  
   - C. High Latency Requirement  
     *C. High Latency Requirement*  
   - D. Long Horizon  
     *D. Long Horizon*  
   **Answer:** C  

3. **In the ReAct Pattern, what is the correct order of a basic loop?**  
   - A. Action → Observation → Thought  
     *A. Action → Observation → Thought*  
   - B. Observation → Thought → Action  
     *B. Observation → Thought → Action*  
   - C. Thought → Action → Observation  
     *C. Thought → Action → Observation*  
   - D. Thought → Observation → Action  
     *D. Thought → Observation → Action*  
   **Answer:** C  

4. **When debugging an Agent loop, what is the first step to check?**  
   - A. Check if the tool description is detailed enough.  
   - B. Review if the Agent's "Thought" aligns with the goal.  
   - C. Set up a fallback retry immediately.  
   - D. Increase the maximum number of tools.  
   **Answer:** B  

---

### Day 4 Review Questions

1. **According to the lecture, what are the four pillars a reliable Agent is built upon?**  
   - A. Prompt, Context, Tool, Control  
     *A. Prompt, Context, Tool, Control*  
   - B. Prompt, Memory, Tool, Evaluation  
     *B. Prompt, Memory, Tool, Evaluation*  
   - C. Context, RAG, Tool, Guardrail  
     *C. Context, RAG, Tool, Guardrail*  
   - D. Prompt, Context, Logging, Approval  
     *D. Prompt, Context, Logging, Approval*  
   **Answer:** A  

2. **How is the "Lost in the Middle" phenomenon in Context Engineering mitigated?**  
   - A. Cramming all information into the middle of the context  
   - B. Placing important information at the beginning and the end of the context  
   - C. Filtering out all conversation history information  
   - D. Using more examples in the prompt  
   **Answer:** B  

3. **In Tool Calling, which element acts as the instruction for the LLM to decide which tool to choose?**  
   - A. The result returned from the tool  
   - B. The tool name and its detailed description  
   - C. The JSON format of the tool  
   - D. The number of declared tools  
   **Answer:** B  

4. **When is the "Human-in-the-Loop" (HITL) mechanism applied?**  
   - A. When the tool performs data reading operations  
   - B. When the tool performs state-changing operations (e.g., payment, deleting DB)  
   - C. When the LLM returns incorrectly formatted results  
   - D. When the context is noisy (Context Rot)  
   **Answer:** B  

---

### Day 15 Review Questions

1. **What skills does Track 2 (AI Infrastructure & Data) in Phase 2 focus on training?**  
   - A. Developing new AI models and optimizing architecture  
   - B. Self-hosting and operating the backend of AI systems at the production level  
   - C. Designing UI/UX for AI applications  
   - D. Building business strategies for AI products  
   **Answer:** B  

2. **What is the hard requirement mentioned to be able to practice the serving and FinOps labs in Track 2?**  
   - A. Having a GitHub Enterprise account  
   - B. Needing a GPU or a Cloud free-tier  
   - C. Having a Kubernetes certification  
   - D. Needing a computer with RAM > 32GB  
   **Answer:** B  

3. **Which of the following target roles (CP2) mentioned in the lecture is suitable for Track 2?**  
   - A. AI Researcher, Data Scientist  
     *A. AI Researcher, Data Scientist*  
   - B. Full-stack Developer, UX Designer  
     *B. Full-stack Developer, UX Designer*  
   - C. AI Data Engineer, Platform Engineer, MLOps Engineer  
     *C. AI Data Engineer, Platform Engineer, MLOps Engineer*  
   - D. Product Manager, AI Ethics Officer  
     *D. Product Manager, AI Ethics Officer*  
   **Answer:** C  

4. **According to the lecture, Track 2 is suitable for people who have a mindset about which of the following concepts?**  
   - A. UI/UX, user experience, A/B testing  
   - B. SLA, SLO, P95, Cost  
   - C. Graphic design, animation, storytelling  
   - D. Marketing, sales, customer acquisition  
     *D. Marketing, sales, customer acquisition*  
   **Answer:** B  

---

### Day 16 Review Questions

1. **According to the Hybrid Cloud strategy for AI, which of the following combinations is recommended to optimize both cost and scalability?**  
   - A. Using PaaS for both Training and Serving  
   - B. Using IaaS for Training and PaaS for Serving  
   - C. Using AI-aaS for Training and IaaS for Serving  
   - D. Using PaaS for Training and IaaS for Serving  
   **Answer:** B  

2. **Which GPU is described as a "sleeper pick" for Inference tasks at $0.40-$0.86/hour?**  
   - A. A100  
     *A. A100*  
   - B. H100  
     *B. H100*  
   - C. L40S  
     *C. L40S*  
   - D. T4  
     *D. T4*  
   **Answer:** C  

3. **Which solution helps reduce AI model training costs on the cloud by 60-70%?**  
   - A. Using Reserved Instances  
   - B. Using Spot/Preemptible Instances  
   - C. Using On-Demand Instances  
   - D. Using Dedicated Hosts  
   **Answer:** B  

4. **In Kubernetes, to manage GPU resources for AI workloads, which of the following configurations is correct?**  
   - A. Setting requests smaller than limits for GPUs  
   - B. Using `nvidia.com/gpu` with requests = limits  
   - C. No need to specify resource requests for GPUs  
   - D. Using `cpu` and `memory` instead of GPU resources  
   **Answer:** B  

5. **Which serving engine uses RadixAttention to reuse KV cache, optimizing for Agents and Multi-turn chat?**  
   - A. vLLM  
     *A. vLLM*  
   - B. SGLang  
     *B. SGLang*  
   - C. LMDeploy  
     *C. LMDeploy*  
   - D. TensorRT-LLM  
     *D. TensorRT-LLM*  
   **Answer:** B  

---

### Day 17 Review Questions

1. **In the Medallion Architecture, which layer contains data that has been cleaned, deduplicated, and schema-applied?**  
   - A. Bronze  
     *A. Bronze*  
   - B. Silver  
     *B. Silver*  
   - C. Gold  
     *C. Gold*  
   - D. Raw  
     *D. Raw*  
   **Answer:** B  

2. **Which technique is used to detect erroneous records in a pipeline without breaking the entire processing flow?**  
   - A. Logging errors to a temporary file  
   - B. Moving erroneous records to a Dead-Letter Queue (DLQ)  
   - C. Stopping the pipeline immediately  
   - D. Overwriting erroneous data with null values  
   **Answer:** B  

3. **Which method helps minimize training-serving skew by generating features in real-time?**  
   - A. Daily batch processing  
   - B. Streaming with Kafka and Flink  
   - C. Using a File Store instead of a Feature Store  
   - D. Using CDC from the database only  
   **Answer:** B  

4. **In the ingestion process for LLMs, which step occurs after parsing unstructured data?**  
   - A. Embedding into a Vector Store  
   - B. Chunking (e.g., 512 tokens)  
   - C. Storing in raw format  
   - D. Schema checking  
   **Answer:** B  

5. **What kind of data does the "Data Flywheel" in an AI pipeline use as the source for the Bronze layer?**  
   - A. Financial transaction data  
   - B. Agent traces (prompts, tool calls, user feedback)  
   - C. IoT sensor data  
   - D. Pure system logs  
   **Answer:** B  

---

### Day 18 Review Questions

1. **Which technology is highlighted for its **Hidden Partitioning** feature that automatically abstracts partitioning logic away from the user?**  
   - A. Delta Lake  
     *A. Delta Lake*  
   - B. Apache Iceberg  
     *B. Apache Iceberg*  
   - C. Apache Hudi  
     *C. Apache Hudi*  
   - D. Apache Parquet  
     *D. Apache Parquet*  
   **Answer:** B  

2. **Which of the following anti-patterns typically leads to the **small files problem** in a Data Lakehouse?**  
   - A. Partitioning by a high-cardinality column  
   - B. Skipping the `OPTIMIZE` command  
   - C. Setting `VACUUM 0 HOURS`  
   - D. Using Spark for small queries  
   **Answer:** B  

3. **In the Medallion Architecture, which layer contains **immutable and append-only** data?**  
   - A. Bronze  
     *A. Bronze*  
   - B. Silver  
     *B. Silver*  
   - C. Gold  
     *C. Gold*  
   - D. Platinum  
     *D. Platinum*  
   **Answer:** A  

4. **To ensure model reproducibility, **Delta versions** should be integrated with which of the following?**  
   - A. Git source code  
   - B. MLflow run ID  
   - C. System timestamp  
   - D. Parquet file name  
   **Answer:** B  

5. **Which storage format is recommended for good columnar read performance and compression in a Lakehouse?**  
   - A. JSON  
     *A. JSON*  
   - B. CSV  
     *B. CSV*  
   - C. Parquet  
     *C. Parquet*  
   - D. Avro  
     *D. Avro*  
   **Answer:** C  

---

### Day 19 Review Questions

1. **What happens if you change the embedding model after indexing data in a vector database?**  
   - A. The vector database automatically updates embeddings for all old data.  
   - B. No impact because the vector database stores vectors independently of the model.  
   - C. A full re-index is required because vectors from the old and new models are incompatible.  
   - D. Only the query model needs to be changed; the index remains the same.  
   **Answer:** C  

2. **When vectors are unit-normalized, which of the following statements is true?**  
   - A. Cosine Similarity and Dot Product give different rankings.  
   - B. The ranking order of Cosine, Dot Product, and Euclidean Distance is the same.  
   - C. Only Cosine Similarity gives accurate results.  
   - D. Euclidean Distance cannot be used with normalized vectors.  
   **Answer:** B  

3. **Which factor is considered to account for up to 80% of the quality in a RAG system?**  
   - A. The choice of vector database (Qdrant, Weaviate).  
   - B. The ANN technique (HNSW, IVF).  
   - C. The chunking strategy (size and overlap).  
   - D. Using hybrid search combined with BM25.  
   **Answer:** C  

4. **How is the "Training-Serving Skew" problem resolved in a Feature Store?**  
   - A. Using Point-in-time Join to stitch data in real-time.  
   - B. Ensuring both training and inference use the same feature computation processor.  
   - C. Storing all features in the Online Store instead of the Offline Store.  
   - D. Increasing the dataset size to reduce skew.  
   **Answer:** B  

---

### Day 20 Review Questions

1. **Which of the following metrics is considered the most important in production because it reflects the ability to meet Service Level Objectives (SLO)?**  
   - A. TTFT (Time To First Token)  
     *A. TTFT (Time To First Token)*  
   - B. TPOT (Time Per Output Token)  
     *B. TPOT (Time Per Output Token)*  
   - C. Throughput (total tokens/second)  
   - D. Goodput@SLO (the rate of requests meeting the TTFT and TPOT SLOs)  
   **Answer:** D  

2. **Which quantization technique is recommended for CPU/Edge inference environments and uses the Q4_K_M format?**  
   - A. FP8  
     *A. FP8*  
   - B. AWQ (4-bit)  
     *B. AWQ (4-bit)*  
   - C. GGUF  
     *C. GGUF*  
   - D. NVFP4  
     *D. NVFP4*  
   **Answer:** C  

3. **Which of the following statements about PagedAttention is true?**  
   - A. It only works on GPT architectures and doesn't support other models.  
   - B. It eliminates KV cache memory fragmentation and enables continuous batching, increasing throughput by up to 24x.  
   - C. It is a KV cache compression method by projecting into the latent space.  
   - D. It requires specialized hardware (NVIDIA Hopper) and cannot run on older generation GPUs.  
   **Answer:** B  

4. **Among parallelization strategies, which technique separates the prefill and decode phases into separate pools to avoid bottlenecks caused by long prompts?**  
   - A. Tensor Parallelism (TP)  
     *A. Tensor Parallelism (TP)*  
   - B. Pipeline Parallelism (PP)  
     *B. Pipeline Parallelism (PP)*  
   - C. Expert Parallelism (EP)  
     *C. Expert Parallelism (EP)*  
   - D. Disaggregated Serving  
     *D. Disaggregated Serving*  
   **Answer:** D  

---

### Day 21 Review Questions

1. **What is the core difference when applying CI/CD to AI systems compared to traditional software?**  
   - A. UI testing needs to be automated.  
   - B. Data versions must be managed and experiments tracked to prevent model regression.  
   - C. Testing is unnecessary because the model always works well.  
   - D. Only one single tool is used for the entire pipeline.  
   **Answer:** B  

2. **In MLflow, what is the Model Registry primarily used for?**  
   - A. Storing training data as artifacts.  
   - B. Comparing runs on the UI.  
   - C. Managing the model lifecycle, including staging, production, and versioning.  
   - D. Automatically deploying the model to production without testing.  
   **Answer:** C  

3. **When using DVC, which command is used to rerun the entire pipeline reproducibly?**  
   - A. `dvc run`  
     *A. `dvc run`*  
   - B. `dvc push`  
     *B. `dvc push`*  
   - C. `dvc repro`  
     *C. `dvc repro`*  
   - D. `dvc commit`  
     *D. `dvc commit`*  
   **Answer:** C  

4. **Which deployment strategy allows running a new model in parallel with the old one without affecting users, strictly for logging and comparison?**  
   - A. Canary deployment  
     *A. Canary deployment*  
   - B. Blue/Green deployment  
     *B. Blue/Green deployment*  
   - C. Shadow deployment  
     *C. Shadow deployment*  
   - D. Rolling deployment  
     *D. Rolling deployment*  
   **Answer:** C  

---

### Day 22 Review Questions

1. **What is the core difference between LLMOps and traditional MLOps?**  
   - A. LLMOps focuses more on data management than code.  
   - B. LLMOps treats Prompt version management as critically as code and data management.  
   - C. MLOps does not require evaluation.  
   - D. LLMOps is only used for small language models.  
   **Answer:** B  

2. **Which tool is described as "GitHub specifically for prompts" in the lecture?**  
   - A. LangSmith  
     *A. LangSmith*  
   - B. W&B Weave  
     *B. W&B Weave*  
   - C. Prompt Hub  
     *C. Prompt Hub*  
   - D. RAGAS  
     *D. RAGAS*  
   **Answer:** C  

3. **According to the lecture, what aspects of LLMs is RAGAS used to evaluate?**  
   - A. Only accuracy  
   - B. Inference speed and cost  
   - C. Faithfulness, relevance, and hallucination  
   - D. The ability to detect Prompt Injection  
   **Answer:** C  

4. **What is one of the goals of Guardrails & Safety Monitoring?**  
   - A. Increasing token generation speed  
   - B. Blocking PII leakage and detecting Prompt Injection  
   - C. Automatically generating new prompts from data  
   - D. Optimizing API costs  
   **Answer:** B  

---

### Day 23 Review Questions

1. **According to the lecture, besides the traditional golden signals, what additional signals do LLMs need to ensure observability?**  
   - A. Latency, traffic, errors, saturation  
     *A. Latency, traffic, errors, saturation*  
   - B. Token throughput, hallucination rate, output length distribution, tool-call failure rate  
     *B. Token throughput, hallucination rate, output length distribution, tool-call failure rate*  
   - C. CPU usage, memory usage, disk I/O  
     *C. CPU usage, memory usage, disk I/O*  
   - D. Number of users, number of requests, status codes  
     *D. Number of users, number of requests, status codes*  
   **Answer:** B  

2. **Cardinality is the “silent bill killer” because:**  
   - A. It increases system latency  
   - B. It increases the number of unique label combinations, leading to high storage and processing costs  
   - C. It reduces the number of collectable metrics  
   - D. It causes errors when using Prometheus  
   **Answer:** B  

3. **The evolution from DevOps to AgentOps described in “The Ops Trinity” includes:**  
   - A. DevOps → MLOps → LLMOps → AgentOps  
     *A. DevOps → MLOps → LLMOps → AgentOps*  
   - B. DevOps → LLMOps → MLOps → AgentOps  
     *B. DevOps → LLMOps → MLOps → AgentOps*  
   - C. DevOps → AgentOps → MLOps → LLMOps  
     *C. DevOps → AgentOps → MLOps → LLMOps*  
   - D. MLOps → DevOps → LLMOps → AgentOps  
     *D. MLOps → DevOps → LLMOps → AgentOps*  
   **Answer:** A  

4. **According to the lecture, telemetry from previous days is integrated into Day 23, for example:**  
   - A. Day 16: Spark UI metrics  
   - B. Day 19: GPU util (DCGM)  
   - C. Day 22: Eval-pass-rate as a Prometheus gauge  
   - D. Day 17: llama.cpp tokens/sec  
   **Answer:** C  

---

### Day 24 Review Questions

1. **According to the Least Privilege principle, which of the following roles has permission to delete production data?**  
   - A. ML Engineer  
     *A. ML Engineer*  
   - B. Data Analyst  
     *B. Data Analyst*  
   - C. Admin  
     *C. Admin*  
   - D. Service Account  
     *D. Service Account*  
   **Answer:** C  

2. **In the envelope encryption model, how is the Data Encryption Key (DEK) protected?**  
   - A. Stored as plaintext in code  
   - B. Encrypted by a Key Encryption Key (KEK)  
   - C. Rotated annually instead of monthly  
   - D. Embedded directly into the model  
   **Answer:** B  

3. **Which PII processing technique is reversible and commonly used for internal analysis?**  
   - A. Anonymization  
     *A. Anonymization*  
   - B. Masking  
     *B. Masking*  
   - C. Hashing  
     *C. Hashing*  
   - D. De-identification  
     *D. De-identification*  
   **Answer:** D  

4. **In the Security Testing Pyramid, which tool is used to detect exposed secrets in a source code repository?**  
   - A. Bandit (SAST)  
     *A. Bandit (SAST)*  
   - B. pip-audit (Dependency Scanning)  
     *B. pip-audit (Dependency Scanning)*  
   - C. truffleHog (Secret Scanning)  
     *C. truffleHog (Secret Scanning)*  
   - D. Garak (Prompt Injection Testing)  
     *D. Garak (Prompt Injection Testing)*  
   **Answer:** C  

---

### Day 25 Review Questions

1. **According to the lecture, which sign indicates that immediate GPU right-sizing is needed?**  
   - A. GPU utilization < 50%  
     *A. GPU utilization < 50%*  
   - B. GPU utilization < 30%  
     *B. GPU utilization < 30%*  
   - C. MFU < 50%  
     *C. MFU < 50%*  
   - D. MBU < 30%  
     *D. MBU < 30%*  
   **Answer:** B  

2. **Which strategy helps leverage spot instances for a 60-70% cost reduction while still ensuring reliability?**  
   - A. Using 100% spot instances only  
   - B. Mixed Fleet Strategy: 20% on-demand + 80% spot, combined with frequent checkpointing  
   - C. Using on-demand for training and spot for inference  
   - D. Using reserved instances instead of spot  
   **Answer:** B  

3. **To monitor GPU performance, which metric is particularly important for compute-bound tasks (e.g., training, prefill)?**  
   - A. GPU Utilization  
     *A. GPU Utilization*  
   - B. MBU (Memory Bandwidth Utilization)  
     *B. MBU (Memory Bandwidth Utilization)*  
   - C. MFU (Model FLOPs Utilization)  
     *C. MFU (Model FLOPs Utilization)*  
   - D. Cache hit rate  
     *D. Cache hit rate*  
   **Answer:** C  

4. **Which inference optimization technique helps reduce per-token cost by using smaller models for most simple queries?**  
   - A. Request Batching  
     *A. Request Batching*  
   - B. Caching  
     *B. Caching*  
   - C. Model Cascading  
     *C. Model Cascading*  
   - D. Disaggregated Serving  
     *D. Disaggregated Serving*  
   **Answer:** C  

5. **To allocate GPU costs to teams (chargeback), which strategy does the lecture recommend?**  
   - A. Calculating an average cost for all teams  
   - B. Setting up tagging (team, project, env) and using Kubecost for analysis  
   - C. Using a single undivided cloud account  
   - D. Only tracking total monthly costs  
   **Answer:** B  

---

### Day 26 Review Questions

1. **What primitives does the MCP (Model Context Protocol) provide for LLMs to interact with tools and data?**  
   - A. Tools, Resources, Prompts  
     *A. Tools, Resources, Prompts*  
   - B. Agents, Tasks, Messages  
     *B. Agents, Tasks, Messages*  
   - C. Orchestrator, Specialist, Router  
     *C. Orchestrator, Specialist, Router*  
   - D. Redis, PostgreSQL, FastAPI  
     *D. Redis, PostgreSQL, FastAPI*  
   **Answer:** A  

2. **In the A2A protocol, what state can a task transition to in order to request more information from the caller instead of failing immediately?**  
   - A. Submitted  
     *A. Submitted*  
   - B. Working  
     *B. Working*  
   - C. Input Required  
     *C. Input Required*  
   - D. Canceled  
     *D. Canceled*  
   **Answer:** C  

3. **Which routing strategy is described as the most flexible but slow and expensive?**  
   - A. Keyword-based  
     *A. Keyword-based*  
   - B. Embedding-based (Semantic Routing)  
     *B. Embedding-based (Semantic Routing)*  
   - C. LLM-based  
     *C. LLM-based*  
   - D. Fallback chains  
     *D. Fallback chains*  
   **Answer:** C  

4. **According to the lecture, which state management method is initially recommended because it scales horizontally easily?**  
   - A. Stateful with sticky sessions  
   - B. Stateless with context stored in Redis or PostgreSQL  
   - C. Stateful with local storage  
   - D. Stateless not storing context  
   **Answer:** B  

5. **Which security principle requires human approval for high-risk actions like writing to a database?**  
   - A. Rate Limiting  
     *A. Rate Limiting*  
   - B. Sandbox Execution  
     *B. Sandbox Execution*  
   - C. Human-in-the-Loop (HITL)  
     *C. Human-in-the-Loop (HITL)*  
   - D. Minimal Capability  
     *D. Minimal Capability*  
   **Answer:** C  

---

### Day 27 Review Questions

1. **What is the core difference between **Pipeline Monitoring** and **Data Observability**?**  
   - A. Pipeline Monitoring only checks runtime, while Data Observability checks data correctness.  
   - B. Pipeline Monitoring is used for batch, Data Observability is used for streaming.  
   - C. Pipeline Monitoring focuses on logs, Data Observability focuses on schema.  
   - D. There is no difference, both are the same.  
   **Answer:** A  

2. **Among the 5 pillars of Data Observability, which pillar detects changes in column names or data types?**  
   - A. Freshness  
     *A. Freshness*  
   - B. Volume  
     *B. Volume*  
   - C. Schema  
     *C. Schema*  
   - D. Lineage  
     *D. Lineage*  
   **Answer:** C  

3. **In Great Expectations, what is the role of a **Checkpoint**?**  
   - A. Storing data validation rules (Expectation Suite).  
   - B. Integrating the Expectation Suite into the production pipeline and triggering actions (alert, block) upon failure.  
   - C. Automatically generating sample data for testing.  
   - D. Completely replacing dbt tests.  
   **Answer:** B  

4. **In SLO Engineering, what is the **Error Budget** used for?**  
   - A. Measuring data freshness.  
   - B. Balancing stability and new features: if the error budget is depleted, prioritize bug fixes over feature releases.  
   - C. Determining the alert threshold for anomaly detection.  
   - D. Classifying incident severity (P0-P3).  
   **Answer:** B  

---

### Day 28 Review Questions

1. **According to the lecture, what is an **anti-pattern** in integrating AI Platform components?**  
   - A. Using event-driven integration with Kafka  
   - B. Maintaining configuration in Git (GitOps)  
   - C. Tightly coupling between components  
   - D. Applying the Bulkhead pattern to separate inference and training  
   **Answer:** C  

2. **In the end-to-end request flow, what is the target time for each component?**  
   - A. Vector Search < 5ms, Feature Store < 50ms, LLM Inference < 500ms  
     *A. Vector Search < 5ms, Feature Store < 50ms, LLM Inference < 500ms*  
   - B. Feature Store < 5ms, Vector Search < 50ms, LLM Inference < 500ms  
     *B. Feature Store < 5ms, Vector Search < 50ms, LLM Inference < 500ms*  
   - C. Feature Store < 50ms, Vector Search < 500ms, LLM Inference < 5ms  
     *C. Feature Store < 50ms, Vector Search < 500ms, LLM Inference < 5ms*  
   - D. All need to be under 100ms  
   **Answer:** B  

3. **Which tool is recommended for **detailed latency breakdown analysis** across the entire flow?**  
   - A. Py-spy  
     *A. Py-spy*  
   - B. Tracemalloc  
     *B. Tracemalloc*  
   - C. Jaeger  
     *C. Jaeger*  
   - D. cProfile  
     *D. cProfile*  
   **Answer:** C  

4. **What is the prerequisite for deploying the Platform to production according to the 5 Pillars?**  
   - A. Manual checking of the Production Readiness checklist by an engineer  
   - B. Automating the checklist in the CI pipeline  
   - C. Ensuring all code runs in the local environment  
   - D. Using a single framework for the entire stack  
   **Answer:** B  

5. **Which of the following models is the correct **integration pattern** to avoid shared mutable state?**  
   - A. Using a shared database with concurrent writes  
   - B. Immutable events and event sourcing via append-only log (Kafka)  
   - C. Storing state in a global variable  
   - D. Using a static JSON configuration file  
   **Answer:** B  
