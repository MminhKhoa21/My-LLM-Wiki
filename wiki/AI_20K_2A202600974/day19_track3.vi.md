---
type: summary
title: "Day 19 Track 3: GraphRAG & Knowledge Graphs"
description: "Detailed summary of Track 3 covering the transition from Flat RAG to GraphRAG, Knowledge Graph foundations, Microsoft GraphRAG, LightRAG, and lab implementation."
tags: [ai, ai-agent, graphrag, knowledge-graph, neo4j, noderag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/GraphRAG and Knowledge Graphs.pdf", "raw/AI_20K_2A202600974/19/LAB DAY 19.pdf"]
---
Dưới đây là nội dung file `day19_track3.md` đã được chuyển đổi thành song ngữ Anh-Việt, giữ nguyên định dạng Markdown. Mỗi đoạn văn, tiêu đề, gạch đầu dòng đều có tiếng Anh trước, tiếp theo là bản dịch tiếng Việt in nghiêng.

> **Lộ trình:** [[track3_ai_app|Track 3: AI App / Agent]]  

*# GraphRAG và Đồ thị tri thức*

*## 1. Giới hạn của Vector RAG (Flat RAG)*

  * **Vấn đề:** Flat RAG hoạt động dựa trên Semantic Similarity (tìm đoạn văn bản có ý nghĩa tương tự). Nó gặp thất bại với 3 loại câu hỏi:*  
    * *Multi-hop relational:* Truy vấn cần suy luận bắc cầu qua nhiều thực thể. (Ví dụ: "AI company co-founded by ex-Google?"). Nó lấy ra các đoạn riêng lẻ nhưng thiếu mối liên kết.*  
    * *Global thematic:* Tóm tắt toàn cục toàn bộ kho dữ liệu.*  
    * *Cross-document:* So sánh chính sách rải rác ở nhiều tài liệu.*  
  * **Giải pháp:** GraphRAG hiểu được kết nối cấu trúc. Việc lấy thông tin giống như "duyệt qua một bản đồ tư duy" thay vì "tìm kiếm trên Google". Nó cải thiện 40% tính toàn diện và độ chính xác đa bước (multi-hop) gấp 2-3 lần. Tuy nhiên, với câu hỏi factoid đơn giản 1 tài liệu, Flat RAG vẫn nhanh và rẻ hơn.*

*## 2. Kiến thức cơ bản về Đồ thị tri thức (KG)*

  * **Cấu trúc:** Gồm Đỉnh (Nodes/Entities) và Cạnh (Edges/Relations).*  
  * **Triples (Bộ ba):** Đơn vị nguyên tử của KG theo cấu trúc `(Chủ thể) → [Vị ngữ / Mối quan hệ] → (Tân ngữ)`. Ví dụ: `(Sam Altman) → [CEO_OF] → (OpenAI)`.*  
  * **Loại đồ thị:** KG trong GraphRAG thường là Đồ thị có hướng và có nhãn (Directed Labeled Property Graphs).*  
  * **Công cụ:*  
    * *Neo4j:* Cơ sở dữ liệu đồ thị chuẩn công nghiệp, dùng ngôn ngữ Cypher (như SQL cho Graph).*  
    * *NetworkX:* Thư viện Python tốt cho prototyping.*

*## 3. Nút thắt trong trích xuất*

*Trích xuất Nodes và Edges từ văn bản thô là khâu khó nhất và đắt đỏ nhất. Các kỹ thuật bắt buộc:*

  * **NER & Relation Extraction:** Nhận diện thực thể và mối quan hệ bằng LLM hoặc NLP truyền thống.*  
  * **Coreference Resolution (Giải quyết đồng tham chiếu):** Xác định các đại từ như "Ông ấy" thay cho "Sam Altman". Bỏ qua bước này sẽ mất 30-40% liên kết.*  
  * **Entity Disambiguation (Khử mơ hồ) & Deduplication (Xóa trùng lặp):** Gộp các cách gọi tên khác nhau (vd: OpenAI, Open AI, OAI) thành một Node duy nhất.*

*## 4. Pipeline GraphRAG tiêu chuẩn*

*Hành trình từ câu hỏi đến câu trả lời:*

   *1. **Query Processing:** Trích xuất thực thể chính từ câu hỏi.*  
   *2. **Seed Node Matching:** Tìm các thực thể đó trong Graph DB để làm điểm xuất phát (Seed Node).*  
   *3. **Graph Traversal (Duyệt đồ thị):** Dùng thuật toán BFS (Breadth-First Search) để lấy thông tin lân cận. *Lưu ý:* Depth = 2 là tiêu chuẩn, Depth = 3+ sẽ quá nhiễu.*  
   *4. **Textualization (Văn bản hóa):** Đổi Subgraph thành văn bản dạng "Entity A liên quan Entity B".*  
   *5. **Generation:** Đưa văn bản đó vào Context Window của LLM để sinh câu trả lời.*  
  * *Hybrid Search:* Có thể kết hợp Vector DB để tìm Seed Node, sau đó dùng Graph DB để tìm Relationships.*

*## 5. Kiến trúc SOTA: Microsoft GraphRAG vs LightRAG*

    * Tạo ra khái niệm "Cộng đồng" (Community Detection) và "Tóm tắt phân cấp". Rất tốt cho Global Search (hỏi về bức tranh tổng thể).*  
    * *Nhược điểm:* Chi phí Index cực kỳ đắt đỏ, không phù hợp cho dữ liệu cập nhật liên tục.*  
    * Kiến trúc truy xuất hai cấp độ (Dual-level retrieval), tạo vector embedding cho cả Node và Edge. Truy xuất siêu nhanh và tiết kiệm chi phí index.*

*## 6. Chiến lược doanh nghiệp (ROI)*

  * **Flat RAG:** Dùng cho Support IT, quy định HR, câu hỏi có đáp án nằm trong 1 đoạn văn.*  
  * **GraphRAG:** Pháp lý (hợp đồng đa tầng), Supply Chain (nút thắt chuỗi cung ứng), bản đồ kỹ năng nhân sự. Đừng dùng cho tài liệu rác 1 lần.*

*## 7. Lab Day 19: Xây dựng hệ thống GraphRAG*

  * Xử lý bộ **Tech Company Corpus**.*  
  * Pipeline cần xây dựng: Trích xuất Triple bằng LLM -> Đưa vào NetworkX / Neo4j / **NodeRAG** framework -> Thực hiện Graph Traversal -> LLM Generation.*  
  * Đánh giá trên tập câu hỏi Multi-hop và so sánh benchmark với Flat RAG (về accuracy, latency, chi phí token).*
