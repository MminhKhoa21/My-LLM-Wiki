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
> **Roadmap:** [[track3_ai_app|Track 3: AI App / Agent]]

# GraphRAG & Knowledge Graphs  
*# GraphRAG và Đồ thị tri thức*

## 1. Limitations of Vector RAG (Flat RAG)  
*## 1. Giới hạn của Vector RAG (Flat RAG)*

- **Problem:** Flat RAG works based on Semantic Similarity (finding text passages with similar meaning). It fails with 3 types of questions:  
  * **Vấn đề:** Flat RAG hoạt động dựa trên Semantic Similarity (tìm đoạn văn bản có ý nghĩa tương tự). Nó gặp thất bại với 3 loại câu hỏi:*  
  - *Multi-hop relational:* Queries requiring transitive reasoning across multiple entities. (Example: "AI company co-founded by ex-Google?"). It retrieves individual passages but lacks relationships.  
    * *Multi-hop relational:* Truy vấn cần suy luận bắc cầu qua nhiều thực thể. (Ví dụ: "AI company co-founded by ex-Google?"). Nó lấy ra các đoạn riêng lẻ nhưng thiếu mối liên kết.*  
  - *Global thematic:* Summarizing the entire corpus globally.  
    * *Global thematic:* Tóm tắt toàn cục toàn bộ kho dữ liệu.*  
  - *Cross-document:* Comparing policies scattered across many documents.  
    * *Cross-document:* So sánh chính sách rải rác ở nhiều tài liệu.*  
- **Solution:** GraphRAG understands structural connections. Information retrieval is like "browsing a mind map" rather than "searching Google". It improves comprehensiveness by 40% and multi-hop accuracy by 2-3 times. However, for simple factoid questions within a single document, Flat RAG is still faster and cheaper.  
  * **Giải pháp:** GraphRAG hiểu được kết nối cấu trúc. Việc lấy thông tin giống như "duyệt qua một bản đồ tư duy" thay vì "tìm kiếm trên Google". Nó cải thiện 40% tính toàn diện và độ chính xác đa bước (multi-hop) gấp 2-3 lần. Tuy nhiên, với câu hỏi factoid đơn giản 1 tài liệu, Flat RAG vẫn nhanh và rẻ hơn.*

## 2. Knowledge Graph (KG) Fundamentals  
*## 2. Kiến thức cơ bản về Đồ thị tri thức (KG)*

- **Structure:** Consists of Vertices (Nodes/Entities) and Edges (Edges/Relations).  
  * **Cấu trúc:** Gồm Đỉnh (Nodes/Entities) và Cạnh (Edges/Relations).*  
- **Triples:** Atomic unit of KG in the form `(Subject) → [Predicate/Relation] → (Object)`. Example: `(Sam Altman) → [CEO_OF] → (OpenAI)`.  
  * **Triples (Bộ ba):** Đơn vị nguyên tử của KG theo cấu trúc `(Chủ thể) → [Vị ngữ / Mối quan hệ] → (Tân ngữ)`. Ví dụ: `(Sam Altman) → [CEO_OF] → (OpenAI)`.*  
- **Graph type:** KG in GraphRAG is typically a Directed Labeled Property Graph.  
  * **Loại đồ thị:** KG trong GraphRAG thường là Đồ thị có hướng và có nhãn (Directed Labeled Property Graphs).*  
- **Tools:**  
  * **Công cụ:*  
  - *Neo4j:* Industry-standard graph database, using Cypher language (like SQL for Graphs).  
    * *Neo4j:* Cơ sở dữ liệu đồ thị chuẩn công nghiệp, dùng ngôn ngữ Cypher (như SQL cho Graph).*  
  - *NetworkX:* Good Python library for prototyping.  
    * *NetworkX:* Thư viện Python tốt cho prototyping.*

## 3. The Extraction Bottleneck  
*## 3. Nút thắt trong trích xuất*

Extracting Nodes and Edges from raw text is the hardest and most expensive step. Required techniques:  
*Trích xuất Nodes và Edges từ văn bản thô là khâu khó nhất và đắt đỏ nhất. Các kỹ thuật bắt buộc:*

- **NER & Relation Extraction:** Identifying entities and relations using LLM or traditional NLP.  
  * **NER & Relation Extraction:** Nhận diện thực thể và mối quan hệ bằng LLM hoặc NLP truyền thống.*  
- **Coreference Resolution:** Resolving pronouns like "He" referring to "Sam Altman". Skipping this step loses 30-40% of links.  
  * **Coreference Resolution (Giải quyết đồng tham chiếu):** Xác định các đại từ như "Ông ấy" thay cho "Sam Altman". Bỏ qua bước này sẽ mất 30-40% liên kết.*  
- **Entity Disambiguation & Deduplication:** Merging different name variations (e.g., OpenAI, Open AI, OAI) into a single Node.  
  * **Entity Disambiguation (Khử mơ hồ) & Deduplication (Xóa trùng lặp):** Gộp các cách gọi tên khác nhau (vd: OpenAI, Open AI, OAI) thành một Node duy nhất.*

## 4. Standard GraphRAG Pipeline  
*## 4. Pipeline GraphRAG tiêu chuẩn*

The journey from question to answer:  
*Hành trình từ câu hỏi đến câu trả lời:*

1. **Query Processing:** Extract main entities from the question.  
   *1. **Query Processing:** Trích xuất thực thể chính từ câu hỏi.*  
2. **Seed Node Matching:** Find those entities in the Graph DB as starting points (Seed Nodes).  
   *2. **Seed Node Matching:** Tìm các thực thể đó trong Graph DB để làm điểm xuất phát (Seed Node).*  
3. **Graph Traversal:** Use BFS (Breadth-First Search) algorithm to retrieve neighboring information. *Note:* Depth = 2 is standard, Depth = 3+ introduces too much noise.  
   *3. **Graph Traversal (Duyệt đồ thị):** Dùng thuật toán BFS (Breadth-First Search) để lấy thông tin lân cận. *Lưu ý:* Depth = 2 là tiêu chuẩn, Depth = 3+ sẽ quá nhiễu.*  
4. **Textualization:** Convert the subgraph into text like "Entity A is related to Entity B".  
   *4. **Textualization (Văn bản hóa):** Đổi Subgraph thành văn bản dạng "Entity A liên quan Entity B".*  
5. **Generation:** Feed that text into the LLM's context window to generate the answer.  
   *5. **Generation:** Đưa văn bản đó vào Context Window của LLM để sinh câu trả lời.*  
- *Hybrid Search:* Can combine Vector DB to find Seed Nodes, then use Graph DB to find Relationships.  
  * *Hybrid Search:* Có thể kết hợp Vector DB để tìm Seed Node, sau đó dùng Graph DB để tìm Relationships.*

## 5. SOTA Architectures: Microsoft GraphRAG vs LightRAG  
*## 5. Kiến trúc SOTA: Microsoft GraphRAG vs LightRAG*

- **Microsoft GraphRAG (2024):**  
  * **Microsoft GraphRAG (2024):*  
  - Introduces "Community Detection" and "Hierarchical Summarization". Excellent for Global Search (asking about the big picture).  
    * Tạo ra khái niệm "Cộng đồng" (Community Detection) và "Tóm tắt phân cấp". Rất tốt cho Global Search (hỏi về bức tranh tổng thể).*  
  - *Drawback:* Extremely expensive indexing, not suitable for continuously updated data.  
    * *Nhược điểm:* Chi phí Index cực kỳ đắt đỏ, không phù hợp cho dữ liệu cập nhật liên tục.*  
- **LightRAG:**  
  * **LightRAG:*  
  - Dual-level retrieval architecture, creating vector embeddings for both Nodes and Edges. Ultra-fast retrieval and cost-effective indexing.  
    * Kiến trúc truy xuất hai cấp độ (Dual-level retrieval), tạo vector embedding cho cả Node và Edge. Truy xuất siêu nhanh và tiết kiệm chi phí index.*

## 6. Enterprise Strategy (ROI)  
*## 6. Chiến lược doanh nghiệp (ROI)*

- **Flat RAG:** Use for IT support, HR policies, questions whose answer lies in a single paragraph.  
  * **Flat RAG:** Dùng cho Support IT, quy định HR, câu hỏi có đáp án nằm trong 1 đoạn văn.*  
- **GraphRAG:** Legal (multi-layer contracts), Supply Chain (bottlenecks), HR skill mapping. Do not use for one-off garbage documents.  
  * **GraphRAG:** Pháp lý (hợp đồng đa tầng), Supply Chain (nút thắt chuỗi cung ứng), bản đồ kỹ năng nhân sự. Đừng dùng cho tài liệu rác 1 lần.*

## 7. Lab Day 19: Building a GraphRAG System  
*## 7. Lab Day 19: Xây dựng hệ thống GraphRAG*

- Process the **Tech Company Corpus**.  
  * Xử lý bộ **Tech Company Corpus**.*  
- Pipeline to build: Triple Extraction using LLM → Load into NetworkX / Neo4j / **NodeRAG** framework → Perform Graph Traversal → LLM Generation.  
  * Pipeline cần xây dựng: Trích xuất Triple bằng LLM -> Đưa vào NetworkX / Neo4j / **NodeRAG** framework -> Thực hiện Graph Traversal -> LLM Generation.*  
- Evaluate on a set of Multi-hop questions and benchmark against Flat RAG (accuracy, latency, token cost).  
  * Đánh giá trên tập câu hỏi Multi-hop và so sánh benchmark với Flat RAG (về accuracy, latency, chi phí token).*
