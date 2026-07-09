---
type: summary
title: "Day 19 Track 2: Vector Store & Feature Store"
description: "Detailed summary of Track 2 covering vector embeddings, vector databases, RAG pipelines, hybrid search, and feature stores."
tags: [ai, data-engineering, vector-database, feature-store, rag, embeddings]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/1-Day 19 - Track 2 - Vector store and Feature store_v2.pdf"]
---
> * **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]*

# *Kho lưu trữ Vector & Kho đặc trưng*

## *1. Nhúng Vector*

   **Bản chất:** Ánh xạ dữ liệu phi cấu trúc (text, image, audio) thành các vector số thực (dense vectors) trong không gian nhiều chiều.
   **Sự tiến hóa:*
     2020-2026: General-purpose foundation embeddings (OpenAI ada-002, bge-m3). Một model phục vụ nhiều use cases, hỗ trợ đa ngôn ngữ và đa phương thức.
   * **Lưu ý:** Việc đổi embedding model đòi hỏi phải re-index toàn bộ dữ liệu. Cần phải sử dụng chung một model ở cả khâu Index và Query.

## *2. Độ đo tương tự*

   **Cosine Similarity:** Góc giữa hai vector. Là mặc định cho text embeddings.
   **Dot Product:** Phép nhân vô hướng. Nhanh hơn Cosine do không cần phép chia độ dài. Phổ biến trong ColBERT, DPR.
   **Euclidean Distance:** Khoảng cách thẳng giữa hai điểm.
   * **Lưu ý:** Nếu vector đã được chuẩn hóa (unit-norm) thì thứ tự xếp hạng của Cosine, Dot và Euclidean là giống nhau. Việc dùng sai metric so với lúc pretraining có thể làm giảm recall 10-20%.

## *3. Cơ sở dữ liệu Vector & Pipeline RAG*

   **Vector DBs:** Qdrant, Weaviate, Pinecone... Dùng để lưu trữ embeddings và hỗ trợ tìm kiếm lân cận gần nhất xấp xỉ (ANN - Approximate Nearest Neighbor).
   **Các kỹ thuật ANN & Tối ưu:*
     Lập chỉ mục với HNSW, IVF.
     Tiết kiệm bộ nhớ với Quantization (PQ, OPQ) có thể giảm dung lượng tới 32x.
   **Chunking Strategies:** Rất quan trọng, chiếm 80% chất lượng RAG. Quá trình chia văn bản thành các chunks cần tối ưu hóa kích thước và độ chồng lấp (overlap).
   **Hybrid Search:** Kết hợp tìm kiếm từ khóa truyền thống (BM25) và tìm kiếm ngữ nghĩa (Vector Search), sau đó trộn kết quả bằng RRF (Reciprocal Rank Fusion).
   **2-Stage Retrieval:** Sử dụng Vector Search để lấy ra Top-K kết quả (nhanh nhưng độ chính xác chưa tối ưu), sau đó dùng Reranking (Cross-Encoder) để sắp xếp lại nhằm tăng mức độ liên quan.

## *4. Kho đặc trưng*

   **Khái niệm:** Hệ thống quản lý các "features" (đặc trưng) dùng cho Machine Learning models.
   **Thành phần cốt lõi:*
     *Offline Store:* Dùng cho việc huấn luyện mô hình, lưu trữ lượng dữ liệu lịch sử khổng lồ.
     *Online Store:* Dùng cho quá trình inference với độ trễ thấp (low latency).
   **Point-in-time Join:** Giúp ghép dữ liệu chính xác theo thời gian thực tế xảy ra sự kiện, tránh rò rỉ dữ liệu (data leakage) từ tương lai.
   **Training-Serving Skew:** Sự lệch pha giữa lúc huấn luyện và lúc triển khai thực tế ("Lỗi thầm lặng"). Feature Store giúp giải quyết triệt để vấn đề này bằng cách đảm bảo mô hình sử dụng cùng một bộ xử lý tính toán feature ở cả hai khâu.

## 5. Lab & Bài tập  
## *5. Lab & Bài tập*

   **GraphRAG:** Được nhắc đến như giải pháp thay thế/bổ sung khi cần hiểu mối quan hệ (Relational QA) mà Vector RAG đơn thuần gặp khó khăn (Chi tiết ở Track 3).
   **Chuẩn bị cho Day 20:** Hiểu được sự đánh đổi giữa Model Accuracy và Latency (Ví dụ: Accuracy 95% nhưng độ trễ 3s là trải nghiệm người dùng tệ). Chuẩn bị cho kiến thức Model Serving & Inference Optimization (vLLM, PagedAttention).

---

### *Câu hỏi ôn tập Ngày 19*

   Điều gì xảy ra nếu bạn thay đổi model embedding sau khi đã index dữ liệu trong vector database?
     A. Vector database tự động cập nhật embedding cho tất cả dữ liệu cũ.
     B. Không ảnh hưởng gì vì vector database lưu trữ vector độc lập với model.
     C. Bắt buộc phải re-index toàn bộ dữ liệu vì vector từ model cũ và mới không tương thích.
     D. Chỉ cần thay đổi model ở khâu query, index vẫn giữ nguyên.
   ***Đáp án:** C*

   Khi các vector đã được chuẩn hóa (unit-norm), mệnh đề nào sau đây là đúng?
     A. Cosine Similarity và Dot Product cho thứ tự xếp hạng khác nhau.
     B. Thứ tự xếp hạng của Cosine, Dot Product và Euclidean Distance là giống nhau.
     C. Chỉ có Cosine Similarity mới cho kết quả chính xác.
     D. Euclidean Distance không thể sử dụng với vector đã chuẩn hóa.
   ***Đáp án:** B*

   Yếu tố nào được cho là chiếm tới 80% chất lượng của hệ thống RAG?
     A. Lựa chọn vector database (Qdrant, Weaviate).
     B. Kỹ thuật ANN (HNSW, IVF).
     C. Chiến lược chunking (kích thước và độ chồng lấp).
     D. Sử dụng hybrid search kết hợp BM25.
   ***Đáp án:** C*

   Vấn đề "Training-Serving Skew" trong Feature Store được giải quyết bằng cách nào?
     A. Sử dụng Point-in-time Join để ghép dữ liệu theo thời gian thực.
     B. Đảm bảo cả huấn luyện và inference dùng cùng một bộ xử lý tính toán feature.
     C. Lưu trữ tất cả features trong Online Store thay vì Offline Store.
     D. Tăng kích thước dataset để giảm sai lệch.
   ***Đáp án:** B*
