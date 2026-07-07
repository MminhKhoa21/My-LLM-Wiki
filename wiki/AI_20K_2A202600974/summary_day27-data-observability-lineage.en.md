---
type: summary
title: "Summary of day27-data-observability-lineage.pdf"
description: "Tổng hợp kiến thức về Data Observability, 7 chiều đo lường chất lượng dữ liệu, Data Contracts, Lineage và các thách thức trong hạ tầng AI."
tags: [ai, 20k, day27]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/27/day27-data-observability-lineage.pdf"]
---

# Summary: Data Observability & Lineage

## 1. Why do we need Data Observability?
- **Core difference:** System Monitoring like measuring CPU, RAM, latency does not help catch errors in data content. A "successful" pipeline can still output wrong data. Schema checks only detect about 7.8% of real incidents.
- **Data Downtime:** The core KPI of data quality, measured by the time from when an error is detected until it is fixed. Formula: $N \times (TTD + TTR)$.
- **Consequences:** Incorrect data costs time to clean up (accounting for ~40% of Data Engineer's time) and leads to real financial damage if fed into prediction models.

## 2. The 7 Dimensions of Data Observability
From the original 5 pillars of Monte Carlo, the system is expanded to 7 dimensions:
1. **Freshness:** Is the data new? How long is it delayed?
2. **Volume:** Are there enough records? Is there a sudden decrease/increase?
3. **Distribution:** Are the values within a reasonable range? Are there any outliers?
4. **Schema:** Have the columns been renamed/changed data types?
5. **Lineage:** Where does the data come from and which report/model does it affect?
6. **Contract:** Is it in accordance with the initial commitments (Data Contract)?
7. **Trust:** The aggregated trust score of the dataset.

## 3. Tools & Ecosystem
- **OSS Tools (Open Source Software):**
  - **Great Expectations (GX 1.0):** Data validation via Python API.
  - **Soda Core 4.0:** Defining quality rules via "Contracts".
  - **Pandera:** Used for validation at the Python DataFrame boundary.
  - **dbt-expectations / dbt unit tests:** For systems using dbt.
- **SaaS (Rules vs ML):** Monte Carlo, Anomalo, Bigeye... use Machine Learning to automatically detect anomalies instead of creating static rules/thresholds to avoid false alerts.

## 4. Anomaly & Drift Detection
- Use dynamic threshold ranges or distribution analysis instead of static levels. Decompose-then-detect (remove trend & seasonality before alerting) to reduce false alarms.
- Measure distribution distance with formulas: PSI, Wasserstein, KS, JS, MMD.

## 5. Data Contracts
- **ODCS Standard (Open Data Contract Standard):** Describes schema, quality, SLA, ownership... in YAML format (e.g., v3.1.0).
- Data Contracts need to be enforced across 3 layers (Shift-left CI gate, streaming runtime, post-ingest batch) rather than just sitting in a Catalog (text repository).

## 6. Lineage
- **OpenLineage:** Standardized JSON describing the lineage event stream. Quality is an attribute attached to the lineage steps.
- **Multi-dimensional querying:**
  - **Forward (Blast radius):** Who does this error affect?
  - **Backward (Root cause):** Which stage did the incorrect data originate from?

## 7. AI-Infra
- **Feature Stores:** Manage *Training-serving skew* (data structure deviation between training and serving) and *Point-in-time correctness* (avoiding looking into the future).
- **Embeddings & RAG:** Need to check for embedding drift (change in vector distance over time) and the staleness of the corpus in RAG.
- **Telemetry:** Need to monitor the entire LLM pipeline, ensuring contamination prevention and training data cleaning.
