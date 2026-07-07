---
type: summary
title: "Summary: Day 10 Data Pipeline and Data Observability"
description: "A detailed summary of the Day 10 lecture covering Data Pipeline architecture, Data Quality, and Observability for AI systems."
tags: [data-pipeline, observability, etl, data-quality, ai-agent, rag]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/10/Day 10 Data Pipeline and Data Observability.pdf"]
---

# Summary: Day 10 Data Pipeline and Data Observability

This document provides a comprehensive summary of the lecture "Data Pipeline & Data Observability" from Day 10 of the AI in Action course. It addresses the "garbage in, garbage out" problem in AI systems by focusing on ETL processes, data quality, and system observability before data reaches the Agent or Vector Store.

## 1. The Core Problem: Garbage In, Garbage Out
Even a powerful AI Agent will hallucinate or provide incorrect answers if the underlying data is dirty, outdated (stale), or missing context. 
- **Key Insight**: Do not debug the AI model before debugging the data pipeline.
- **Observability**: The goal is to detect issues (e.g., failed syncs, stale data) *before* users complain.
- **Example Scenario**: A data pipeline fails to sync the latest refund policy. The vector store retains the old policy, and the Agent confidently outputs outdated information (e.g., "14 days" instead of "7 days").

## 2. RACI and Roles in Data Pipelines
Managing an AI data pipeline requires clear boundaries and responsibilities to avoid overloading the AI Engineer:
- **AI / Applied Data**: Define data contracts for the agent's corpus and conduct before/after evaluations.
- **Data Engineer**: Ensure robust ingestion, data modeling, and pipeline SLA adherence.
- **SRE / Platform**: Manage alerts, on-call runbooks, and quota/secrets.
- **Product / SME (Subject Matter Expert)**: Define the "correct" policy and sign-off on the source of truth.

## 3. Data Pipeline Architecture: ETL vs. ELT & Batch vs. Streaming
A data pipeline moves data from sources (DB, API, Files) to serving layers (Vector Store, Agent).
- **ETL (Extract, Transform, Load)**: Transform data before loading. Good for masking PII before it enters the warehouse.
- **ELT (Extract, Load, Transform)**: Load data first, transform later. Suitable for large batch jobs like monthly CSVs.
- **Batch**: Processing data in scheduled blocks (e.g., nightly PDF syncs).
- **Streaming**: Processing data continuously (e.g., webhook for P1 support tickets).

## 4. Ingestion Layer and Risks
Ingestion from diverse sources (PostgreSQL, APIs, PDFs) involves unique failure points:
- **PostgreSQL**: Handled via CDC (Change Data Capture) or snapshots. Risks: CDC lag, schema drift.
- **External API**: Handled via polling or pagination. Risks: Rate limits (HTTP 429), auth issues, checkpoint stalls. Mitigation involves exponential backoff, jitter, and pagination cursors.
- **PDF / HTML**: Handled via parsers and OCR. Risks: Bad OCR confidence, missing metadata. Mitigation requires content hashing and logical versioning.
- **Event Streams/Webhooks**: Risks include consumer lag and backpressure. Recommended architecture uses a Message Queue + Buffer (Redis/SQS) feeding into a Consumer (Worker) with a Dead-Letter Queue (DLQ) for poison messages.

## 5. Transformation and Dirty Data Repair
Transformation is required to clean and normalize data before it reaches the AI agent.
- **Cleaning Rules**: Trim whitespace, parse dates consistently (YYYY-MM-DD UTC), normalize Unicode (NFC), and standardise formats.
- **Rejection/Quarantine**: Drop empty content, deduplicate based on primary keys, and flag records with missing critical fields (e.g., missing dates) for manual review rather than failing the entire batch.

## 6. Data Quality as Code
Implementing Data Quality checks ensures that only valid data progresses through the pipeline.
- **6 Dimensions**:
  1. **Completeness**: Essential fields (like content) must not be null.
  2. **Accuracy**: Dates and facts must align with business truth.
  3. **Consistency**: Consistent formats and keys.
  4. **Timeliness**: Data must meet freshness SLAs.
  5. **Validity**: Conformance to schema and data contracts.
  6. **Uniqueness**: No duplicate records.
- **Expectation Suites**: Using tools like Great Expectations to enforce these rules programmatically. Violations can Halt the pipeline, Quarantine the row, or simply Warn the operators depending on severity.

## 7. The 5 Pillars of Data Observability
Observability provides visibility into the pipeline's health to preemptively stop bad data:
1. **Freshness**: Is the data updating on time? (e.g., tracking `freshness_hours`).
2. **Distribution**: Are there abnormal spikes in null rates or content length?
3. **Volume**: Did the number of ingested records suddenly drop?
4. **Schema**: Are there breaking changes or schema drifts from the source?
5. **Lineage**: Can an error be traced from the output back to the specific source table or file?

## 8. Incident Triage Workflow
When an Agent gives a bad answer, follow a structured, time-boxed debugging flow:
1. **Detect (0-5 mins)**: Check Freshness and SLA breach metrics.
2. **Isolate (5-12 mins)**: Check Volume drops and error rates by pipeline step.
3. **Validate (12-20 mins)**: Look for Schema drift or parsing errors.
4. **Trace Lineage**: Trace the exact source file and step that failed.
5. **Fix & Rerun**: Fix the root cause and rerun the pipeline safely utilizing **Idempotency** (rerunning should not create duplicate vectors).

## 9. Orchestration and Idempotency
Pipelines must be robust and re-runnable.
- **Idempotency**: Essential for safe reruns. Use natural keys (upsert by doc_id + version) instead of random UUIDs. Delete-then-insert within a transaction, or swap staging collections.
- **Orchestrators** (e.g., Airflow, Prefect, Dagster): Manage Directed Acyclic Graphs (DAGs) of tasks, handling triggers, retry policies (backoffs), DLQs, and alerting for SLA breaches.

## 10. Service Level Indicators (SLIs) for RAG
Connect data observability directly to user experience:
- **Citation Freshness**: Average age of the chunks cited by the Agent.
- **Grounding Rate**: Percentage of answers strictly grounded in retrieved context.
- **Retrieval hit@k**: Quality of retrieval on a golden test set.
- **Pipeline Latency**: Time from source ingestion to vector publish. 
