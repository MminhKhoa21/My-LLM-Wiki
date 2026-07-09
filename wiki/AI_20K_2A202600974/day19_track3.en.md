---
type: summary
title: "Day 19 Track 3: GraphRAG & Knowledge Graphs"
description: "Detailed summary of Track 3 covering the transition from Flat RAG to GraphRAG, Knowledge Graph foundations, Microsoft GraphRAG, LightRAG, and lab implementation."
tags: [ai, ai-agent, graphrag, knowledge-graph, neo4j, noderag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/19/GraphRAG and Knowledge Graphs.pdf", "raw/AI_20K_2A202600974/19/LAB DAY 19.pdf"]
---

> **Roadmap:** [[track3_ai_app|Track 3: AI App / Agent]]

# GraphRAG & Knowledge Graphs  

## 1. Limitations of Vector RAG (Flat RAG)  

- **Problem:** Flat RAG works based on Semantic Similarity (finding text passages with similar meaning). It fails with 3 types of questions:  
  - *Multi-hop relational:* Queries requiring transitive reasoning across multiple entities. (Example: "AI company co-founded by ex-Google?"). It retrieves individual passages but lacks relationships.  
  - *Global thematic:* Summarizing the entire corpus globally.  
  - *Cross-document:* Comparing policies scattered across many documents.  
- **Solution:** GraphRAG understands structural connections. Information retrieval is like "browsing a mind map" rather than "searching Google". It improves comprehensiveness by 40% and multi-hop accuracy by 2-3 times. However, for simple factoid questions within a single document, Flat RAG is still faster and cheaper.  

## 2. Knowledge Graph (KG) Fundamentals  

- **Structure:** Consists of Vertices (Nodes/Entities) and Edges (Edges/Relations).  
- **Triples:** Atomic unit of KG in the form `(Subject) → [Predicate/Relation] → (Object)`. Example: `(Sam Altman) → [CEO_OF] → (OpenAI)`.  
- **Graph type:** KG in GraphRAG is typically a Directed Labeled Property Graph.  
- **Tools:**  
  - *Neo4j:* Industry-standard graph database, using Cypher language (like SQL for Graphs).  
  - *NetworkX:* Good Python library for prototyping.  

## 3. The Extraction Bottleneck  

Extracting Nodes and Edges from raw text is the hardest and most expensive step. Required techniques:  

- **NER & Relation Extraction:** Identifying entities and relations using LLM or traditional NLP.  
- **Coreference Resolution:** Resolving pronouns like "He" referring to "Sam Altman". Skipping this step loses 30-40% of links.  
- **Entity Disambiguation & Deduplication:** Merging different name variations (e.g., OpenAI, Open AI, OAI) into a single Node.  

## 4. Standard GraphRAG Pipeline  

The journey from question to answer:  

1. **Query Processing:** Extract main entities from the question.  
2. **Seed Node Matching:** Find those entities in the Graph DB as starting points (Seed Nodes).  
3. **Graph Traversal:** Use BFS (Breadth-First Search) algorithm to retrieve neighboring information. *Note:* Depth = 2 is standard, Depth = 3+ introduces too much noise.  
4. **Textualization:** Convert the subgraph into text like "Entity A is related to Entity B".  
5. **Generation:** Feed that text into the LLM's context window to generate the answer.  
- *Hybrid Search:* Can combine Vector DB to find Seed Nodes, then use Graph DB to find Relationships.  

## 5. SOTA Architectures: Microsoft GraphRAG vs LightRAG  

- **Microsoft GraphRAG (2024):**  
  * **Microsoft GraphRAG (2024):*  
  - Introduces "Community Detection" and "Hierarchical Summarization". Excellent for Global Search (asking about the big picture).  
  - *Drawback:* Extremely expensive indexing, not suitable for continuously updated data.  
- **LightRAG:**  
  * **LightRAG:*  
  - Dual-level retrieval architecture, creating vector embeddings for both Nodes and Edges. Ultra-fast retrieval and cost-effective indexing.  

## 6. Enterprise Strategy (ROI)  

- **Flat RAG:** Use for IT support, HR policies, questions whose answer lies in a single paragraph.  
- **GraphRAG:** Legal (multi-layer contracts), Supply Chain (bottlenecks), HR skill mapping. Do not use for one-off garbage documents.  

## 7. Lab Day 19: Building a GraphRAG System  

- Process the **Tech Company Corpus**.  
- Pipeline to build: Triple Extraction using LLM → Load into NetworkX / Neo4j / **NodeRAG** framework → Perform Graph Traversal → LLM Generation.  
- Evaluate on a set of Multi-hop questions and benchmark against Flat RAG (accuracy, latency, token cost).

---

### Day 19 Review Questions

1. Flat RAG (Vector RAG) typically fails with which of the following types of questions?
   - A. Simple factoid questions located within a single document.
   - B. Questions requiring reasoning across multiple entities (multi-hop).
   - C. Questions about basic concept definitions.
   - D. Questions extracting information from a short paragraph.

2. What is the atomic unit of a Knowledge Graph?
   - A. Individual Nodes and Edges.
   - B. A Triple consisting of Subject - Predicate - Object.
   - C. Any Subgraph.
   - D. A complete sentence in the original text.

3. In the standard GraphRAG pipeline, which step converts the subgraph into text format to be fed into the LLM?
   - A. Seed Node Matching.
   - B. Graph Traversal.
   - C. Textualization.
   - D. Generation.
   - *D. Sinh.*

4. Through what architecture does LightRAG improve speed and cost compared to Microsoft GraphRAG?
   - A. Using Community Detection and Hierarchical Summarization.
   - B. Dual-level retrieval with embeddings for both Nodes and Edges.
   - C. Graph traversal with a maximum depth of 3.
   - D. Combining Vector DB and Graph DB via Hybrid Search mechanism.
