---
type: summary
title: "Day 18 Track 2: Data Lakehouse Architecture"
description: "Summary of Data Lakehouse concepts, including Delta Lake, Apache Iceberg, and Medallion architecture for AI workloads."
tags: [Data Lakehouse, Delta Lake, Apache Iceberg, Medallion Architecture, ACID, Storage]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/18/2-Day 18 - Track 2 - Data Lakehouse Architecture.pdf"]
---
# Data Lakehouse Architecture (Day 18 - Track 2)

## 1. Evolution of Data Platforms

- **Traditional (1990s-2010s):** Data Warehouses (Structured, SQL, rigid schema, high cost).

- **ML Era (2010s-2020s):** Data Lakes (S3, cheap, flexible, but prone to becoming "data swamps").

- **LLM Era (2020s+):** Data Lakehouses combining ACID transactions, open formats (Delta/Iceberg), and cheap object storage. Ideal for multi-modal data, embeddings, and RAG.

## 2. Core Technologies: Delta Lake, Iceberg, and Hudi

- **Delta Lake:** Uses a JSON transaction log (`_delta_log/`) to provide ACID properties on object storage. Supports schema evolution, Time Travel, and Deletion Vectors.

- **Apache Iceberg:** Renowned for **Hidden Partitioning** (prevents full table scans by abstracting partition logic from users) and partition evolution without rewriting data.

- **Apache Hudi:** Strong for mutation-heavy workloads (Merge-On-Read).

- **UniForm / XTable:** Tools enabling interoperability between Delta, Iceberg, and Hudi.

## 3. Storage Optimization and Anti-Patterns

- **Columnar Storage (Parquet):** Highly efficient for reading specific columns compared to row-oriented formats (JSON/CSV). Uses compression (Snappy, ZSTD) and min/max stats to skip files.

- **Z-ORDER and Partitioning:** Co-locating data to optimize queries. Avoid partitioning by high-cardinality columns (e.g., `user_id`).

- **Anti-Patterns to Avoid:**
  1. "Dump everything into S3" (Data Swamp).
  2. Partitioning by high-cardinality columns.
  3. Ignoring `OPTIMIZE` (leading to the small-file problem).
  4. Setting `VACUUM 0 HOURS` (destroys Time Travel and concurrent reads).
  5. Using Spark clusters for tiny queries (use DuckDB instead).

## 4. Medallion Architecture for AI

- **Bronze (Raw):** Immutable, append-only raw data (e.g., raw JSON logs, user inputs).

- **Silver (Cleaned):** Validated, deduplicated, and schema-enforced data (using `MERGE`).

- **Gold (Aggregated):** Analytics-ready, feature store, or refined doc chunks for RAG pipelines.

## 5. Production Ops and Governance

- **Data Versioning:** Integrating Delta versions with MLflow run IDs to ensure model reproducibility.

- **Change Data Capture (CDC):** Streaming changes from OLTP databases (like Postgres) via Debezium and Kafka into Lakehouses.

- **Data Contracts:** Enforcing schemas and constraints to maintain data quality.

- **Security:** Handling PII with tokenization, encryption, RBAC/ABAC, and respecting Right-to-Forget laws (PDPL, GDPR).
