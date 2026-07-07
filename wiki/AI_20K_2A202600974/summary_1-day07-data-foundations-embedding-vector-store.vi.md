---
type: summary
title: "Summary of 1-day07-data-foundations-embedding-vector-store"
description: "Detailed summary of the Day 07 lecture slides covering Data Foundations, Agent Memory Architecture, Embedding, and Vector Stores."
tags: [day7, embedding, vector-store, rag, data-strategy, memory]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/7/1-day07-data-foundations-embedding-vector-store.pdf"]
---



## 1. Data Strategy Cho Sản Phẩm AI
Dữ liệu là cốt lõi của một sản phẩm AI chất lượng. Mô hình mạnh nhưng dữ liệu nhiễu/bẩn sẽ dẫn đến hallucination. Data quality và retrieval quality thường quyết định trải nghiệm hơn là việc đổi sang model đắt tiền hơn.

Có 3 loại Data Agent Cần:
- **Knowledge Data**: Tài liệu, policy, SOP, FAQ. Phù hợp nhất với retrieval (Vector Store).
- **Operational Data**: Database, đơn hàng, CRM logs. Phù hợp truy vấn qua API/SQL thay vì embedding.
- **Contextual Data**: Lịch sử session, user profile. Inject trực tiếp vào prompt để cá nhân hóa.

Raw (Lộn xộn, nhiễu) -> Cleaned (Bỏ nhiễu, chuẩn hóa) -> Structured (Chunk, gắn metadata) -> Enriched (Tag, quality label).

Cần mask các dữ liệu nhạy cảm (PII) như tên cá nhân, số điện thoại, email trước khi đưa vào embedding.

- **Short-term Memory**: Nằm trong context window, phù hợp cho logic ngắn, dễ đầy token.
- **Long-term Memory**: Nằm ngoài context window (Vector store, DB). Chỉ truy xuất khi cần.
- **Context Window Budget**: Cần phân bổ token hợp lý (System prompt ~15%, Retrieved context ~35%, History ~25%, Generation ~25%).

- Embedding biến ngôn ngữ thành không gian toán học nhiều chiều (vector) để máy so sánh ngữ nghĩa.
- **Cosine Similarity**: Đo độ gần về nghĩa (góc giữa 2 vector). Càng gần 1 thì càng giống nghĩa.
- Ứng dụng: Semantic search, clustering, dedup, recommendation.
- Không có model tốt nhất tuyệt đối, cần chọn theo độ cân bằng giữa tốc độ, giá và chất lượng (VD: `text-embedding-3-small` / `large`).

- Vector Store lưu 4 thứ: ID, Original Chunk, Embedding Vector, và Metadata.
- **Metadata** rất quan trọng (source, category, date) để lọc trước khi tính similarity.
- Top-k, Score Threshold và Attribute Filter giúp lọc nhiễu.

## 5. Kết Nối Agent Với Data (Retrieval Pipeline)
Pipeline chuẩn: Document -> Chunk -> Embed -> Store -> Query -> Inject
- **Chunking**: Không nên quá to (nhiễu), không quá nhỏ (mất ngữ cảnh). Thường chunk theo section/heading và giữ 10-20% chunk overlap.
- **RAG-Enhanced vs LLM Chay**: RAG giúp agent có grounded context, trích xuất nguồn, giảm hallucination.
- **Eval Retrieval**: Đo đạc độ chính xác bằng các chỉ số Precision@k, Recall@k. Hãy đánh giá quá trình retrieval trước khi đánh giá generation.

Thực hành xây dựng Retrieval pipeline tối thiểu:
- Xử lý 1 bộ tài liệu nhỏ (FAQ, policy).
- Chunking và index vào ChromaDB.
- Semantic search demo và inject context để Agent trả lời có căn cứ.
