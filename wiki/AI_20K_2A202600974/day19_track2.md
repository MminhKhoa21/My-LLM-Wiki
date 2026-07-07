---
type: summary
title: "Day 19 Track 2: Vector Store & Feature Store"
description: "Detailed summary of Track 2 covering vector embeddings, vector databases, RAG pipelines, hybrid search, and feature stores."
tags: [ai, data-engineering, vector-database, feature-store, rag, embeddings]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/1-Day 19 - Track 2 - Vector store and Feature store_v2.pdf"]
---
> **Roadmap:** [[track2_ai_engineer|Track 2: AI Engineer]]  
> * **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]*

# Vector Store & Feature Store  
# *Kho lưu trữ Vector & Kho đặc trưng*

## 1. Vector Embeddings  
## *1. Nhúng Vector*

- **Essence:** Mapping unstructured data (text, image, audio) into real-number vectors (dense vectors) in high-dimensional space.  
  * **Bản chất:** Ánh xạ dữ liệu phi cấu trúc (text, image, audio) thành các vector số thực (dense vectors) trong không gian nhiều chiều.*
- **Evolution:**  
  * **Sự tiến hóa:**  
  - 2013-2019: Task-specific embeddings (word2vec, FaceNet, BERT).  
    * 2013-2019: Task-specific embeddings (word2vec, FaceNet, BERT).*  
  - 2020-2026: General-purpose foundation embeddings (OpenAI ada-002, bge-m3). One model serves many use cases, supporting multi-language and multi-modality.  
    * 2020-2026: General-purpose foundation embeddings (OpenAI ada-002, bge-m3). Một model phục vụ nhiều use cases, hỗ trợ đa ngôn ngữ và đa phương thức.*  
- *Note:* Switching the embedding model requires re-indexing all data. The same model must be used for both Indexing and Query phases.  
  * * **Lưu ý:** Việc đổi embedding model đòi hỏi phải re-index toàn bộ dữ liệu. Cần phải sử dụng chung một model ở cả khâu Index và Query.*

## 2. Similarity Metrics  
## *2. Độ đo tương tự*

- **Cosine Similarity:** Angle between two vectors. Default for text embeddings.  
  * **Cosine Similarity:** Góc giữa hai vector. Là mặc định cho text embeddings.*  
- **Dot Product:** Scalar multiplication. Faster than Cosine as it avoids division by length. Common in ColBERT, DPR.  
  * **Dot Product:** Phép nhân vô hướng. Nhanh hơn Cosine do không cần phép chia độ dài. Phổ biến trong ColBERT, DPR.*  
- **Euclidean Distance:** Straight-line distance between two points.  
  * **Euclidean Distance:** Khoảng cách thẳng giữa hai điểm.*  
- *Note:* If vectors are unit-normalized, the ranking order of Cosine, Dot, and Euclidean is the same. Using a different metric from pretraining may reduce recall by 10-20%.  
  * * **Lưu ý:** Nếu vector đã được chuẩn hóa (unit-norm) thì thứ tự xếp hạng của Cosine, Dot và Euclidean là giống nhau. Việc dùng sai metric so với lúc pretraining có thể làm giảm recall 10-20%.*

## 3. Vector Database & RAG Pipeline  
## *3. Cơ sở dữ liệu Vector & Pipeline RAG*

- **Vector DBs:** Qdrant, Weaviate, Pinecone... Used to store embeddings and support Approximate Nearest Neighbor (ANN) search.  
  * **Vector DBs:** Qdrant, Weaviate, Pinecone... Dùng để lưu trữ embeddings và hỗ trợ tìm kiếm lân cận gần nhất xấp xỉ (ANN - Approximate Nearest Neighbor).*  
- **ANN Techniques & Optimization:**  
  * **Các kỹ thuật ANN & Tối ưu:**  
  - Indexing with HNSW, IVF.  
    * Lập chỉ mục với HNSW, IVF.*  
  - Memory saving with Quantization (PQ, OPQ) can reduce storage up to 32x.  
    * Tiết kiệm bộ nhớ với Quantization (PQ, OPQ) có thể giảm dung lượng tới 32x.*  
- **Chunking Strategies:** Very important, accounts for 80% of RAG quality. The process of splitting text into chunks needs optimization of size and overlap.  
  * **Chunking Strategies:** Rất quan trọng, chiếm 80% chất lượng RAG. Quá trình chia văn bản thành các chunks cần tối ưu hóa kích thước và độ chồng lấp (overlap).*  
- **Hybrid Search:** Combines traditional keyword search (BM25) and semantic search (Vector Search), then merges results using RRF (Reciprocal Rank Fusion).  
  * **Hybrid Search:** Kết hợp tìm kiếm từ khóa truyền thống (BM25) và tìm kiếm ngữ nghĩa (Vector Search), sau đó trộn kết quả bằng RRF (Reciprocal Rank Fusion).*  
- **2-Stage Retrieval:** Use Vector Search to retrieve Top-K results (fast but not optimally accurate), then use Reranking (Cross-Encoder) to reorder for higher relevance.  
  * **2-Stage Retrieval:** Sử dụng Vector Search để lấy ra Top-K kết quả (nhanh nhưng độ chính xác chưa tối ưu), sau đó dùng Reranking (Cross-Encoder) để sắp xếp lại nhằm tăng mức độ liên quan.*

## 4. Feature Store  
## *4. Kho đặc trưng*

- **Concept:** A system that manages features used for Machine Learning models.  
  * **Khái niệm:** Hệ thống quản lý các "features" (đặc trưng) dùng cho Machine Learning models.*  
- **Core Components:**  
  * **Thành phần cốt lõi:**  
  - *Offline Store:* Used for model training, stores massive historical data.  
    * *Offline Store:* Dùng cho việc huấn luyện mô hình, lưu trữ lượng dữ liệu lịch sử khổng lồ.*  
  - *Online Store:* Used for low-latency inference.  
    * *Online Store:* Dùng cho quá trình inference với độ trễ thấp (low latency).*  
- **Point-in-time Join:** Helps join data accurately according to the actual event time, avoiding data leakage from the future.  
  * **Point-in-time Join:** Giúp ghép dữ liệu chính xác theo thời gian thực tế xảy ra sự kiện, tránh rò rỉ dữ liệu (data leakage) từ tương lai.*  
- **Training-Serving Skew:** Mismatch between training and deployment phases ("silent error"). Feature Store thoroughly solves this by ensuring the model uses the same feature computation logic in both phases.  
  * **Training-Serving Skew:** Sự lệch pha giữa lúc huấn luyện và lúc triển khai thực tế ("Lỗi thầm lặng"). Feature Store giúp giải quyết triệt để vấn đề này bằng cách đảm bảo mô hình sử dụng cùng một bộ xử lý tính toán feature ở cả hai khâu.*

## 5. Lab & Bài tập  
## *5. Lab & Bài tập*

- **GraphRAG:** Mentioned as an alternative/supplement when understanding relationships (Relational QA) is needed, where pure Vector RAG struggles (Details in Track 3).  
  * **GraphRAG:** Được nhắc đến như giải pháp thay thế/bổ sung khi cần hiểu mối quan hệ (Relational QA) mà Vector RAG đơn thuần gặp khó khăn (Chi tiết ở Track 3).*  
- **Preparation for Day 20:** Understand the trade-off between Model Accuracy and Latency (e.g., 95% accuracy but 3s latency is a poor user experience). Prepare for knowledge of Model Serving & Inference Optimization (vLLM, PagedAttention).  
  * **Chuẩn bị cho Day 20:** Hiểu được sự đánh đổi giữa Model Accuracy và Latency (Ví dụ: Accuracy 95% nhưng độ trễ 3s là trải nghiệm người dùng tệ). Chuẩn bị cho kiến thức Model Serving & Inference Optimization (vLLM, PagedAttention).*
