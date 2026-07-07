---
type: overview
title: "Day 7 Overview - Data Foundations"
description: "Nền tảng dữ liệu cho AI Product, phân biệt loại dữ liệu, cơ chế Embedding, Vector Store và Chunking."
tags: [ai, 20k, day7]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/7/Day 07 Slides C401.pdf"]
---
# Day 7: Data Foundations (Embedding & Vector Store)

## 1. Three Types of Data Agents Need
- **Knowledge Data**: Internal documents, SOPs, policies, FAQs... Suitable for *Retrieval* (RAG).
- **Operational Data**: Transactional databases, order statuses, CRM... Typically accessed via controlled queries (DB query).
- **Contextual Data**: User profiles, chat history, location... Used for direct injection into the context.

## 2. Embedding
*Embedding*
- Aims to solve the "semantic distance" problem between input data and stored documents.
- An Embedding model is a function that converts text/images into **Numerical Vectors** (Multi-dimensional arrays of real numbers).
- Searching is performed by measuring the distance between Vectors. The most common is **Cosine Similarity** (measuring the angle between 2 vectors, ignoring magnitude).
- Embedding helps recognize similar meanings even with different keywords, or across different languages (Cross-lingual).

## 3. Vector Store
*Vector Store*
- Vector Store does not just store Vectors, but stores: **ID, Original Chunk (source text), Vector, and Metadata (key-value)**.
- Upon querying, the system searches Vectors to retrieve the top-k results, then injects the Original Chunk into the Prompt for the LLM.
- **Metadata** plays a crucial role in filtering data before vector comparison (e.g., searching only within internal documents, excluding old files).

## 4. Data Processing & Chunking
- Never feed raw text (like error-prone scanned PDFs) directly into Chunking because retrieval quality will degrade drastically. (Data Quality Pyramid: Raw -> Cleaned -> Structured -> Enriched).
- The most optimal format for LLMs is **Markdown**, saving 30-50% in tokens compared to HTML.
- **Chunking**: Breaking documents into smaller segments to maintain information focus.
   - Chunks too large: Context noise, exceeding token limits.
   - Chunks too small: Loss of context, disjointed sentences.
   - Strategies: Chunk by Structure/Heading, Semantic Chunking, or by Token (fixed length with overlap).

## 5. Retrieval Pipeline Process
Includes 2 distinct phases:
- **Ingestion (Offline processing)**: Document -> Chunk -> Embed -> Store (Saving Vectors & Metadata).
- **Retrieval (Online querying)**: User Question -> Embed Query -> Search in Vector DB -> Inject Chunk into LLM Prompt.
