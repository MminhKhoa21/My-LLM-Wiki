---
type: summary
title: "Data Pipeline Engineering (Track 2)"
description: "Summary of Day 17 Track 2 on building robust data pipelines, Medallion Architecture, and streaming ingestion."
tags: [AI_20K_2A202600974, Day17, Data_Pipeline, ETL, Kafka]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/17/Day 17 - Track 2 - Data Pipeline.pdf"]
---
# Data Pipeline Engineering (Day 17 - Track 2)

This track emphasizes that data pipelines are a critical dependency of AI models. A faulty pipeline can silently destroy model accuracy in production ("Garbage in, garbage out").

## Key Concepts

### ETL vs. ELT & Medallion Architecture

- **ELT (Extract, Load, Transform)** is the default for cloud-native AI pipelines due to cheap compute in the lakehouse.
- **Medallion Architecture:**
  - **Bronze:** Raw, append-only, kept forever.
  - **Silver:** Cleaned, conformed, deduplicated, and schema-enforced.
  - **Gold:** Business-ready, aggregated, ML features.

### Extract Patterns and Ingestion

- **Extract Patterns:** Full, Incremental (cursor-based), CDC (Change Data Capture using Debezium to read transaction logs).
- **Ingestion for LLMs:** Ingesting unstructured data involves parsing, chunking (e.g., recursive 512 tokens), and embedding into a Vector store.

### Orchestration

- **Airflow 3.0:** Transitioning from pure task-based workflows to asset-aware workflows, event-driven scheduling, and data assets.
- **Declarative Asset Pipelines (Dagster, DLT):** Focus on declaring *what* the datasets and dependencies are, rather than *how* to run them. Example: `Materialized View` vs `Streaming Table`.

### Streaming Ingestion

- **Kafka Architecture:** Used for streaming ingestion. Kafka 4.0 removes ZooKeeper (KRaft mode).
- **Streaming vs Batch:** Streaming (e.g., Kafka + Flink) ensures very low latency for real-time feature generation, reducing training-serving skew compared to batch processing.

### Validation, Quality Gates, and Contracts

- **Validation Gates:** Implement "fail early" strategies using tools like Pandera or Great Expectations (GX). Bad records go into a Quarantine/DLQ (dead-letter queue) rather than breaking the pipeline.
- **LLM-as-a-Judge:** Used for data quality checks that standard rules miss, such as semantic duplicates or contextual anomalies.
- **Data Contracts:** Establish agreements between data producers and consumers defining schema, semantics, quality, and SLAs to prevent silent schema drift.

### AI-Specific Pipelines

- **Data Flywheel:** Using agent traces (prompts, tool calls, responses, user feedback) as a raw data source (Bronze layer) to build evaluation and fine-tuning datasets.
- **Deduplication:** Extremely important for AI training to prevent verbatim regurgitation. Techniques include lexical dedup (MinHash+LSH) and semantic dedup (SemDeDup).
- **Feature Store:** Centralized system to define features once and serve them identically for offline training and online inference, solving training-serving skew.
