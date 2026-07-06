import os

base_dir = r"D:/Obsidian/My Wiki/wiki/AI_20K_2A202600974/"
os.makedirs(base_dir, exist_ok=True)

files = {}

files["day15_overview.md"] = """---
type: overview
title: "Day 15 Overview"
description: "Tổng kết 15 ngày Phase 1 và định hướng chọn Track cho Phase 2"
tags: [ai, 20k, day15]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/15/day15-trien-khai-thuc-te-dinh-huong.pdf", "raw/AI_20K_2A202600974/15/day15-slide.pdf"]
---

# Day 15 Overview

Ngày 15 đánh dấu sự kết thúc của Phase 1, nhìn lại hành trình 15 ngày xây dựng nền tảng vững chắc về AI và định hướng chuyên sâu cho Phase 2.

## Các nội dung chính
- **15 Ngày Nhìn Lại**: Từ hiểu nền tảng (LLM, bài toán, Agent, Tool Call) đến xây dựng hệ thống (RAG, Multi-agent) và đưa lên production (Deploy, Monitor, Eval).
- **Triển khai Enterprise**: Các thách thức khi đưa AI vào doanh nghiệp bao gồm Security, Compliance, Legacy systems. Sự khác biệt giữa Cloud API, On-premise và Hybrid.
- **Cost Anatomy & Optimization**: Tối ưu chi phí bằng Model Routing, Semantic Caching, Prompt Compression, và đánh giá khi nào nên tự host LLM.
- **Scaling Production**: Xử lý tải cao với Request Queue, Stateless Agent, và đảm bảo SLA/Uptime.
- **3 Tracks cho Phase 2**: Phân chia chuyên sâu theo 3 hướng:
  - Track 1: AI Business & Product
  - Track 2: AI Infrastructure & Data
  - Track 3: AI Application

## Các Track
- [[day15_track1]]
- [[day15_track2]]
- [[day15_track3]]
"""

files["day15_track1.md"] = """---
type: summary
title: "Day 15 Track 1"
description: "Tài liệu Track 1 của Ngày 15"
tags: [ai, 20k, day15]
timestamp: 2026-07-05
sources: []
---

Hiện tại chưa có tài liệu cho Track này.
"""

files["day15_track2.md"] = """---
type: summary
title: "Day 15 Track 2"
description: "Tài liệu Track 2 của Ngày 15"
tags: [ai, 20k, day15]
timestamp: 2026-07-05
sources: []
---

Hiện tại chưa có tài liệu cho Track này.
"""

files["day15_track3.md"] = """---
type: summary
title: "Day 15 Track 3"
description: "Tài liệu Track 3 của Ngày 15"
tags: [ai, 20k, day15]
timestamp: 2026-07-05
sources: []
---

Hiện tại chưa có tài liệu cho Track này.
"""

files["day16_overview.md"] = """---
type: overview
title: "Day 16 Overview"
description: "Tổng quan các track trong Ngày 16"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: []
---

# Day 16 Overview

Bắt đầu Phase 2 với 3 track chuyên sâu:

- **Track 1**: [[day16_track1]] - AI Product Strategy và JTBD
- **Track 2**: [[day16_track2]] - Cloud infrastructure for AI
- **Track 3**: [[day16_track3]] - Advanced Agent Architectures
"""

files["day16_track1.md"] = """---
type: summary
title: "Day 16 Track 1: AI Product Strategy"
description: "Chiến lược sản phẩm AI và phương pháp Job-to-be-Done (JTBD)"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/1-d16-slide-v2.pdf", "raw/AI_20K_2A202600974/16/Strategyn_JTBD_Playbook.pdf"]
---

# AI Product Strategy

Tập trung vào cách xây dựng chiến lược sản phẩm AI và áp dụng framework Job-to-be-Done (JTBD) để hiểu rõ nhu cầu của khách hàng và tối ưu sản phẩm.
"""

files["day16_track2.md"] = """---
type: summary
title: "Day 16 Track 2: Cloud Infrastructure for AI"
description: "Hạ tầng Cloud cho các hệ thống AI"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/1-Day 16_ Track 2_ Cloud infrastructure for AI.pptx"]
---

# Cloud Infrastructure for AI

Tìm hiểu về kiến trúc và hạ tầng đám mây (Cloud) để triển khai các mô hình và ứng dụng AI một cách tối ưu.
"""

files["day16_track3.md"] = """---
type: summary
title: "Day 16 Track 3: Advanced Agent Architectures"
description: "Kiến trúc Agent nâng cao: Reflexion, LATS, Voyager"
tags: [ai, 20k, day16]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/16/phase2-day01-advanced-agent-architectures-extended-fuller.pdf"]
---

# Advanced Agent Architectures

Nghiên cứu nguyên nhân Single Agent (như ReAct) thất bại trong các bài toán phức tạp và cách khắc phục:
- **Reflexion**: Thêm khả năng tự đánh giá (self-evaluation) vào reasoning loop. Agent sẽ thử, đánh giá kết quả, rút ra bài học (reflection memory) và thử lại.
- **LATS (Language Agent Tree Search)**: Kết hợp Monte Carlo Tree Search với LLM để duyệt nhiều nhánh giải pháp và quay lui (undo) khi cần.
- **Voyager**: Agent có khả năng học tập tích lũy kỹ năng (compound learning) để giải quyết các task mở.
- **Checklist an toàn**: Max attempts, structured outputs, tracing, và human review.
"""

files["day17_overview.md"] = """---
type: overview
title: "Day 17 Overview"
description: "Tổng quan các track trong Ngày 17"
tags: [ai, 20k, day17]
timestamp: 2026-07-05
sources: []
---

# Day 17 Overview

Tiếp tục chuyên sâu vào từng Track:

- **Track 1**: [[day17_track1]] - AI Product Strategy (tiếp)
- **Track 2**: [[day17_track2]] - Data Pipeline
- **Track 3**: [[day17_track3]] - Memory Systems for Agents
"""

files["day17_track1.md"] = """---
type: summary
title: "Day 17 Track 1"
description: "Chiến lược và Lab cho AI Product"
tags: [ai, 20k, day17]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/17/d17-slide-track1.pdf", "raw/AI_20K_2A202600974/17/day17-track1-lab.pdf"]
---

# AI Product Strategy (Cont.)

Tài liệu và hướng dẫn thực hành (Lab) tiếp tục nội dung quản lý và phát triển AI Product.
"""

files["day17_track2.md"] = """---
type: summary
title: "Day 17 Track 2: Data Pipeline"
description: "Xây dựng luồng dữ liệu cho hệ thống AI"
tags: [ai, 20k, day17]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/17/Day 17 - Track 2 - Data Pipeline.pdf"]
---

# Data Pipeline

Hệ thống hóa cách thiết kế và xây dựng Data Pipeline (luồng xử lý dữ liệu) để phục vụ việc huấn luyện và suy luận AI.
"""

files["day17_track3.md"] = """---
type: summary
title: "Day 17 Track 3: Memory Systems for Agents"
description: "Hệ thống bộ nhớ cho AI Agents"
tags: [ai, 20k, day17]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/17/Day17 - Track 3 - Memory-systems-for-agents.pdf"]
---

# Memory Systems for Agents

Các cơ chế bộ nhớ giúp Agent ghi nhớ context qua nhiều cuộc hội thoại, từ bộ nhớ ngắn hạn đến dài hạn và cách quản lý chúng.
"""

files["day18_overview.md"] = """---
type: overview
title: "Day 18 Overview"
description: "Tổng quan các track trong Ngày 18"
tags: [ai, 20k, day18]
timestamp: 2026-07-05
sources: []
---

# Day 18 Overview

Nội dung các Track:

- **Track 1**: [[day18_track1]] - Slide & Lab Track 1
- **Track 2**: [[day18_track2]] - Data Lakehouse Architecture
- **Track 3**: [[day18_track3]] - Production RAG
"""

files["day18_track1.md"] = """---
type: summary
title: "Day 18 Track 1"
description: "Slide và bài tập Lab cho Track 1"
tags: [ai, 20k, day18]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/1-d18-slide-v1-track1.pdf", "raw/AI_20K_2A202600974/18/day18-track1-lab.pdf"]
---

# Track 1: AI Product Management

Chiến lược và thực hành định hướng sản phẩm AI.
"""

files["day18_track2.md"] = """---
type: summary
title: "Day 18 Track 2: Data Lakehouse Architecture"
description: "Kiến trúc Data Lakehouse"
tags: [ai, 20k, day18]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-Day 18 - Track 2 - Data Lakehouse Architecture.pdf"]
---

# Data Lakehouse Architecture

Mô hình kiến trúc Data Lakehouse, kết hợp ưu điểm của Data Lake và Data Warehouse để quản lý dữ liệu hiệu quả cho AI.
"""

files["day18_track3.md"] = """---
type: summary
title: "Day 18 Track 3: Production RAG"
description: "Chẩn đoán và tối ưu RAG cho môi trường Production"
tags: [ai, 20k, day18]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-day18-production-rag.pdf"]
---

# Production RAG

Học cách đưa RAG từ Demo (60% accuracy) lên Production (85%+ accuracy):
- **Phân tích Error Tree**: Phân biệt lỗi do Ingestion (Offline) hay Retrieval (Online).
- **Offline Ingestion**: Các chiến lược Chunking (Hierarchical, Late Chunking, Semantic), Enrichment (Summarization, Hypothetical Q&A) để chuẩn bị dữ liệu chất lượng.
- **Online Retrieval**: Vượt qua giới hạn của Flat RAG bằng Two-Stage Retrieval (Bi-encoder sau đó dùng Cross-encoder Rerank) và Hybrid Search (BM25 + Dense).
- **Close the Loop**: Đánh giá bằng RAGAS metrics (Context Recall, Context Precision, Faithfulness, Answer Relevancy) để biết điểm yếu nằm ở tầng nào và tiến hành tối ưu đúng chỗ.
"""

files["day19_overview.md"] = """---
type: overview
title: "Day 19 Overview"
description: "Tổng quan các track trong Ngày 19"
tags: [ai, 20k, day19]
timestamp: 2026-07-05
sources: []
---

# Day 19 Overview

Nội dung các Track:

- **Track 1**: [[day19_track1]] - Retention, Engagement & Habit Loop
- **Track 2**: [[day19_track2]] - Vector store and Feature store
- **Track 3**: [[day19_track3]] - GraphRAG and Knowledge Graphs
"""

files["day19_track1.md"] = """---
type: summary
title: "Day 19 Track 1: Retention, Engagement & Habit Loop"
description: "Thiết kế sản phẩm AI để giữ chân người dùng"
tags: [ai, 20k, day19]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/1-d19-slide-v2.pdf", "raw/AI_20K_2A202600974/19/1-student-day20-v1.pdf"]
---

# Retention, Engagement & Habit Loop

Nghiên cứu phương pháp xây dựng sản phẩm AI có độ tương tác cao và khả năng giữ chân người dùng (Retention):
- Phân tích North Star Metric và Input Metrics.
- **Hook Model**: Tạo lập thói quen qua 4 bước (Trigger, Action, Variable Reward, Investment).
- Natural Frequency vs Nurtured Frequency trong tương tác với AI.
- Lab thực hành thiết kế User Input Grid, lựa chọn Dimension và Scenario phù hợp để testing AI eval hiệu quả.
"""

files["day19_track2.md"] = """---
type: summary
title: "Day 19 Track 2: Vector Store and Feature Store"
description: "Cơ sở dữ liệu Vector và Feature Store"
tags: [ai, 20k, day19]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/1-Day 19 - Track 2 - Vector store and Feature store_v2.pdf"]
---

# Vector Store and Feature Store

Nghiên cứu về cơ sở dữ liệu Vector (lưu trữ embeddings) và Feature Store (quản lý đặc trưng mô hình) ứng dụng cho các mô hình Machine Learning quy mô lớn.
"""

files["day19_track3.md"] = """---
type: summary
title: "Day 19 Track 3: GraphRAG and Knowledge Graphs"
description: "Tích hợp Đồ thị Tri thức vào RAG"
tags: [ai, 20k, day19]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/GraphRAG and Knowledge Graphs.pdf", "raw/AI_20K_2A202600974/19/LAB DAY 19.pdf"]
---

# GraphRAG & Knowledge Graphs

Giải quyết điểm mù của Flat RAG (khó suy luận quan hệ phức tạp, multi-hop):
- **Knowledge Graph (KG)**: Chuyển dữ liệu văn bản thô thành các Triple (Chủ thể - Mối quan hệ - Tân ngữ).
- **Quy trình GraphRAG**:
  1. Trích xuất Thực thể (NER) và Quan hệ (Relation Extraction).
  2. Xây dựng đồ thị (sử dụng Neo4j hoặc NetworkX) kèm các kỹ thuật chuẩn hóa (Deduplication).
  3. Truy vấn: Tìm kiếm Node gốc (Seed) bằng semantic search và duyệt đồ thị (Graph Traversal).
  4. Văn bản hóa subgraph và giao cho LLM sinh câu trả lời.
- Ứng dụng thực tiễn trong y tế, pháp lý, phân tích supply chain.
"""

files["day20_overview.md"] = """---
type: overview
title: "Day 20 Overview"
description: "Tổng quan các track trong Ngày 20"
tags: [ai, 20k, day20]
timestamp: 2026-07-05
sources: []
---

# Day 20 Overview

Nội dung các Track:

- **Track 1**: [[day20_track1]] - Lab: Retention & Engagement
- **Track 2**: [[day20_track2]] - Model Serving & Inference Optimization
- **Track 3**: [[day20_track3]] - Multi-Agent Systems
"""

files["day20_track1.md"] = """---
type: summary
title: "Day 20 Track 1"
description: "Lab thực hành Retention & Engagement"
tags: [ai, 20k, day20]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/20/student-day20-v1.pdf"]
---

# Day 20 Lab - Retention, Engagement & Habit Loop

Thực hành áp dụng các framework phân tích hành vi người dùng, đánh giá các kịch bản tương tác với AI và xây dựng hệ thống testing cho sản phẩm.
"""

files["day20_track2.md"] = """---
type: summary
title: "Day 20 Track 2: Model Serving & Inference Optimization"
description: "Tối ưu hóa quá trình phục vụ mô hình LLM"
tags: [ai, 20k, day20]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/20/1-day20-model-serving-inference-optimization.pdf"]
---

# Model Serving & Inference Optimization

Tổng quan về các kỹ thuật tăng tốc độ suy luận (inference) và giảm chi phí:
- **Quantization**: Giảm precision từ FP16/BF16 xuống FP8, INT8, 4-bit (AWQ, GGUF) giúp tiết kiệm VRAM đáng kể.
- **KV Cache & PagedAttention**: Quản lý bộ nhớ hiệu quả, loại bỏ fragmentation và cho phép continuous batching.
- **Inference Engines**: So sánh các engine như vLLM, SGLang, Ollama, TensorRT-LLM.
- **Distributed Inference**: Chiến lược song song hóa (Data Parallelism, Tensor Parallelism, Pipeline Parallelism, Expert Parallelism).
"""

files["day20_track3.md"] = """---
type: summary
title: "Day 20 Track 3: Multi-Agent Systems"
description: "Kiến trúc hệ thống Multi-Agent"
tags: [ai, 20k, day20]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/20/day05-multi-agent-systems-student.pdf"]
---

# Multi-Agent Systems

Khám phá cách tổ chức nhiều Agent làm việc cùng nhau khi các task trở nên quá phức tạp đối với Single Agent.
- **Supervisor Pattern (Orchestration)**: Hub-and-Spoke, một router trung tâm (Supervisor) điều phối các agent vệ tinh (Workers).
- **Debate / Adversarial**: Giảm hallucination bằng cách để các agent tranh luận với nhau trước khi tổng hợp kết quả (Judge).
- **Parallel Execution & Shared State**: Sử dụng Map-Reduce và AsyncIO để tăng tốc độ.
- **Multi-Agent Frameworks**: So sánh LangGraph, AutoGen, và CrewAI dựa trên control và linh hoạt.
"""

files["day21_overview.md"] = """---
type: overview
title: "Day 21 Overview"
description: "Tổng quan các track trong Ngày 21"
tags: [ai, 20k, day21]
timestamp: 2026-07-05
sources: []
---

# Day 21 Overview

Nội dung các Track:

- **Track 1**: [[day21_track1]] - AI Evaluation
- **Track 2**: [[day21_track2]] - CI/CD cho AI Systems
- **Track 3**: [[day21_track3]] - Fine-tuning LLMs (LoRA/QLoRA)
"""

files["day21_track1.md"] = """---
type: summary
title: "Day 21 Track 1: AI Evaluation"
description: "Đánh giá chất lượng và vòng đời kiểm thử sản phẩm AI"
tags: [ai, 20k, day21]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/d21-slide-v0.pdf", "raw/AI_20K_2A202600974/21/day21-lab-instruction.pdf"]
---

# AI Evaluation

Cách tiếp cận của Product Manager khi đánh giá mô hình AI:
- **Evals Lifecycle**: Từ Vibe Check (chạy test bằng tay để tìm failure patterns) đến Offline Evals (đánh giá trên dataset chuẩn) và Online Monitoring (theo dõi logs production).
- Sử dụng các loại grader khác nhau (Code-based, LLM-as-judge, Human grader).
- **Trace Analysis**: Đọc trace để tìm lỗi ở tầng nào của system (nhầm intent, lỗi công cụ, hay logic pipeline).
- Quá trình chuyển từ "gut feeling" sang đánh giá bằng số liệu và rubric cụ thể (áp dụng bài học từ Notion AI).
"""

files["day21_track2.md"] = """---
type: summary
title: "Day 21 Track 2: CI/CD AI Systems"
description: "Quản lý CI/CD cho các hệ thống AI"
tags: [ai, 20k, day21]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/Day 21 - Track 2 - CICD AI SYSTEMS.pptx"]
---

# CI/CD AI Systems

Tìm hiểu quy trình Continuous Integration và Continuous Deployment cho AI, tự động hóa luồng huấn luyện, đánh giá và triển khai mô hình.
"""

files["day21_track3.md"] = """---
type: summary
title: "Day 21 Track 3: Fine-tuning LLMs"
description: "Huấn luyện tinh chỉnh LLMs bằng LoRA và QLoRA"
tags: [ai, 20k, day21]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/day06-fine-tuning-llms-tu-full-fine-tune-en-loraqlora.pdf"]
---

# Fine-tuning LLMs

Khi Prompt Engineering và RAG không còn đủ khả năng cung cấp style, format, hoặc cần độ trễ thấp và tiết kiệm chi phí ở quy mô lớn (volume cao), Fine-tuning là bước tiếp theo.
- **LoRA (Low-Rank Adaptation)**: Đóng băng tham số gốc của mô hình, chỉ huấn luyện một bộ ma trận trọng số nhỏ (Adapter) chèn vào các layer. Tiết kiệm tài nguyên và giữ nguyên tri thức ban đầu.
- **QLoRA**: Kết hợp LoRA với 4-bit Quantization (sử dụng định dạng NormalFloat4) để có thể fine-tune mô hình lớn (như 7B) trên các GPU tiêu dùng (ví dụ RTX 3090).
- **Dataset Preparation**: Chất lượng dữ liệu quan trọng hơn số lượng (Quality over Quantity) - vài trăm mẫu dữ liệu sạch và chính xác sẽ hiệu quả hơn hàng ngàn mẫu nhiễu.
- Thực hành Fine-tune mô hình sử dụng các thư viện như Unsloth và TRL để tăng tốc quá trình huấn luyện và tiết kiệm VRAM.
"""

for filename, content in files.items():
    filepath = os.path.join(base_dir, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
print("Files generated successfully.")
