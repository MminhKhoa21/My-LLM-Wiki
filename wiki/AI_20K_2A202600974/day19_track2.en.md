---
type: summary
title: "Day 19 Track 2: Vector Store & Feature Store"
description: "Detailed summary of Track 2 covering vector embeddings, vector databases, RAG pipelines, hybrid search, and feature stores."
tags: [ai, data-engineering, vector-database, feature-store, rag, embeddings]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/1-Day 19 - Track 2 - Vector store and Feature store_v2.pdf"]
---
> **Roadmap:** [[track2_ai_engineer|Track 2: AI Engineer]]  

# Vector Store & Feature Store  

## 1. Vector Embeddings  

- **Essence:** Mapping unstructured data (text, image, audio) into real-number vectors (dense vectors) in high-dimensional space.  
- **Evolution:**  
  - 2013-2019: Task-specific embeddings (word2vec, FaceNet, BERT).  
    * 2013-2019: Task-specific embeddings (word2vec, FaceNet, BERT).*  
  - 2020-2026: General-purpose foundation embeddings (OpenAI ada-002, bge-m3). One model serves many use cases, supporting multi-language and multi-modality.  
- *Note:* Switching the embedding model requires re-indexing all data. The same model must be used for both Indexing and Query phases.  

## 2. Similarity Metrics  

- **Cosine Similarity:** Angle between two vectors. Default for text embeddings.  
- **Dot Product:** Scalar multiplication. Faster than Cosine as it avoids division by length. Common in ColBERT, DPR.  
- **Euclidean Distance:** Straight-line distance between two points.  
- *Note:* If vectors are unit-normalized, the ranking order of Cosine, Dot, and Euclidean is the same. Using a different metric from pretraining may reduce recall by 10-20%.  

## 3. Vector Database & RAG Pipeline  

- **Vector DBs:** Qdrant, Weaviate, Pinecone... Used to store embeddings and support Approximate Nearest Neighbor (ANN) search.  
- **ANN Techniques & Optimization:**  
  - Indexing with HNSW, IVF.  
  - Memory saving with Quantization (PQ, OPQ) can reduce storage up to 32x.  
- **Chunking Strategies:** Very important, accounts for 80% of RAG quality. The process of splitting text into chunks needs optimization of size and overlap.  
- **Hybrid Search:** Combines traditional keyword search (BM25) and semantic search (Vector Search), then merges results using RRF (Reciprocal Rank Fusion).  
- **2-Stage Retrieval:** Use Vector Search to retrieve Top-K results (fast but not optimally accurate), then use Reranking (Cross-Encoder) to reorder for higher relevance.  

## 4. Feature Store  

- **Concept:** A system that manages features used for Machine Learning models.  
- **Core Components:**  
  - *Offline Store:* Used for model training, stores massive historical data.  
  - *Online Store:* Used for low-latency inference.  
- **Point-in-time Join:** Helps join data accurately according to the actual event time, avoiding data leakage from the future.  
- **Training-Serving Skew:** Mismatch between training and deployment phases ("silent error"). Feature Store thoroughly solves this by ensuring the model uses the same feature computation logic in both phases.  


- **GraphRAG:** Mentioned as an alternative/supplement when understanding relationships (Relational QA) is needed, where pure Vector RAG struggles (Details in Track 3).  
- **Preparation for Day 20:** Understand the trade-off between Model Accuracy and Latency (e.g., 95% accuracy but 3s latency is a poor user experience). Prepare for knowledge of Model Serving & Inference Optimization (vLLM, PagedAttention).  
