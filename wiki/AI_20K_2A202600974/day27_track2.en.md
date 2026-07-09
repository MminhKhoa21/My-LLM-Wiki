---
type: summary
title: "Summary: Day 27 Track 2 - Data Observability & Lineage"
description: "A comprehensive guide on data observability, Great Expectations, anomaly detection, SLO engineering, and data incident response."
tags: [data-observability, data-engineering, great-expectations, slo, anomaly-detection]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/27/Day27 - Track 2 - Data-observability-lineage.pdf"]
---
# Day 27 Track 2 - Data Observability & Lineage

This document summarizes the Day 27 Track 2 lecture focusing on ensuring data reliability, moving beyond simple pipeline monitoring to true data observability.

## 1. Pipeline Monitoring vs Data Observability

- **Pipeline Monitoring:** Asks "Is the machine running?" (e.g., Did the Airflow job finish? Are CPU/logs normal?).
- **Data Observability:** Asks "Is the data trustworthy?" (e.g., Is the data fresh, complete, consistent?).
- **Silent Failures:** AI/ML systems often fail due to bad data (silent failures) rather than service crashes. A successful pipeline execution does not guarantee correct data.

## 2. Five Pillars of Data Observability

Using the Monte Carlo framework, data observability is defined by 5 pillars:
1. **Freshness:** Is the data up to date?
2. **Volume:** Is the row count anomalous?
3. **Distribution:** Are the values within expected ranges?
4. **Schema:** Did column names or types change?
5. **Lineage:** Which downstream assets are affected by an incident?

Observing unstructured AI data (text, images, embeddings) requires monitoring derived measurable features (e.g., embedding drift, text length distribution, blur scores).

## 3. Great Expectations (GX) & Checkpoints
## *3. Great Expectations (GX) & Checkpoints*

Instead of keeping implicit assumptions about data in engineers' heads, tools like Great Expectations encode them as runnable, version-controlled tests.
- **Expectation Suite:** A collection of rules (e.g., `ExpectColumnValuesToNotBeNull`, `ExpectColumnValuesToBeBetween`).
- **Checkpoints:** Integrate suites into production pipelines (e.g., inside Airflow). If a checkpoint fails, actions like Slack alerts or blocking downstream jobs are triggered.
- **Hard Fails:** Block the pipeline (e.g., duplicate primary keys).
- **Soft Fails:** Trigger warnings (e.g., slight distribution drift).

## 4. Anomaly Detection vs Rules

- **Rules (e.g., GX, dbt tests):** Catch known issues, deterministic, hard fail pipelines.
- **Anomaly Detection (e.g., Z-score, Prophet):** Catch unknown unknowns based on historical baselines (e.g., row count drops by 50%). Requires human review due to false positives. Z-score flags anomalies if deviations exceed a threshold (e.g., > 3 standard deviations).

## 5. dbt Tests (Transformation Layer)

The SQL transformation layer requires close monitoring because errors here rarely crash the pipeline but heavily corrupt data.
- **dbt Built-in Tests:** `not_null`, `unique`, `accepted_values`, `relationships`.
- **Custom SQL Tests:** Ensure business logic holds true.
- **Test Pyramid:** Unit tests (run fast, close to the model) should be prioritized over costly End-to-End tests.

## 6. SLO Engineering for Data & AI

Data platforms treat reliability as a product feature.
- **SLI (Service Level Indicator):** A measurable metric (e.g., `freshness_minutes`, `null_rate`).
- **SLO (Service Level Objective):** The target goal (e.g., "freshness < 60 mins for 99.5% of the time").
- **Error Budget:** `1 - SLO`. If the budget burns too fast, feature releases are halted to prioritize stability.

## 7. Data Incident Response

Observability is only valuable if the team knows how to react.
- **Incident Lifecycle:** Detection → Triage → Mitigation → Root Cause Analysis → Recovery → Postmortem.
- **Runbooks:** Standardized procedural guides for handling incidents.
- **Severity Levels:** Classify incidents (P0 to P3) to determine response times.
- **Blameless Postmortems & Chaos Engineering:** Cultivate learning without pointing fingers. Use "5 Whys" to find systemic root causes.

---

### Day 27 Review Questions

1. **What is the core difference between **Pipeline Monitoring** and **Data Observability**?**  
   - A. Pipeline Monitoring only checks runtime, while Data Observability checks data correctness.  
   - B. Pipeline Monitoring is used for batch, Data Observability is used for streaming.  
   - C. Pipeline Monitoring focuses on logs, Data Observability focuses on schema.  
   - D. There is no difference, both are the same.  
   **Answer:** A  

2. **Among the 5 pillars of Data Observability, which pillar detects changes in column names or data types?**  
   - A. Freshness  
     *A. Freshness*  
   - B. Volume  
     *B. Volume*  
   - C. Schema  
     *C. Schema*  
   - D. Lineage  
     *D. Lineage*  
   **Answer:** C  

3. **In Great Expectations, what is the role of a **Checkpoint**?**  
   - A. Storing data validation rules (Expectation Suite).  
   - B. Integrating the Expectation Suite into the production pipeline and triggering actions (alert, block) upon failure.  
   - C. Automatically generating sample data for testing.  
   - D. Completely replacing dbt tests.  
   **Answer:** B  

4. **In SLO Engineering, what is the **Error Budget** used for?**  
   - A. Measuring data freshness.  
   - B. Balancing stability and new features: if the error budget is depleted, prioritize bug fixes over feature releases.  
   - C. Determining the alert threshold for anomaly detection.  
   - D. Classifying incident severity (P0-P3).  
   **Answer:** B
