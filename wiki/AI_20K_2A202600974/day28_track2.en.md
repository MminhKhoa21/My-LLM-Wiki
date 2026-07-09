---
type: summary
title: "Summary of day28-platform-engineering-documentation"
description: "An end-to-end guide on AI platform engineering, covering integration patterns, performance profiling, and production readiness."
tags: [ai, 20k, day28, platform-engineering, mlops]
timestamp: 2026-07-06
sources: ["raw/AI_20K_2A202600974/28/day28-platform-engineering-documentation.pdf"]
---
# Platform Engineering & Documentation
**Instructor:** VinUniversity (AICB-P2T2 · Phase 2 · Track 2)

## Overview
This document covers the integration of isolated AI components into a fully functional end-to-end AI Platform. The focus is on moving from data ingestion to model serving with comprehensive observability and production readiness.

## 5 Layers of the AI Platform
1. **Compute:** Kubernetes, GPU nodes, vLLM serving, auto-scaling.
2. **Data:** Lakehouse (Delta Lake), Airflow, Kafka, Vector Store.
3. **ML:** MLflow experiments, DVC versioning, Feature Store (Feast).
4. **Ops:** GitHub Actions CI/CD, LangSmith LLMOps, Prometheus/Grafana.
5. **Governance:** RBAC, PII pipelines, encryption, compliance automation.

## Integration Patterns vs. Anti-patterns
- **Anti-pattern:** Tightly coupled components (leads to cascading failures).
  - **Pattern:** Event-driven integration using tools like Kafka or Redis Streams to decouple producers and consumers.
- **Anti-pattern:** Hardcoded configurations.
  - **Pattern:** GitOps (ArgoCD, Helm) to maintain all configurations in Git.
- **Anti-pattern:** Shared mutable state.
  - **Pattern:** Immutable events and event sourcing via append-only logs (Kafka).
- **Anti-pattern:** Cascading failures across services.
  - **Pattern:** Bulkhead pattern (using K8s namespaces and resource quotas) to separate critical inference paths from non-critical batch training.

## End-to-End Request Flow
A typical production AI request flow involves:
1. User Request → API Gateway → Routing Layer → Agent Orchestrator.
2. Parallel calls to Feature Store (<5ms), Vector Search (<50ms), and LLM Inference (<500ms).
3. Guardrails for PII checks (<20ms).
4. Response delivered within 1 second.

All calls must be traced using OpenTelemetry, Jaeger, and LangSmith.

## Integration Testing & Profiling
- **Testing:** Integration tests must ensure API contracts remain intact. Test against both the "golden path" (happy flow) and failure paths (timeouts, retries). Use Testcontainers for spinning up real databases in CI.
- **Profiling Tools:**
  - `Jaeger`: End-to-end latency breakdown and identifying bottlenecks in parallel vs. sequential calls.
  - `cProfile` / `py-spy`: Identifying CPU hotspots.
  - `tracemalloc`: Memory tracking and finding leaks.

## Production Readiness: 5 Pillars
A platform must meet these criteria before deployment:
1. **Reliability:** Circuit breakers, retries, graceful shutdowns.
2. **Observability:** Structured JSON logs, Prometheus metrics, OpenTelemetry traces, automated alerts.
3. **Security:** Vault/KMS for secrets, RBAC, PII handling.
4. **Performance:** Latency SLAs, memory management.
5. **Operations:** Automated CI/CD, disaster recovery plans, load testing.

*Crucial Rule:* The Production Readiness checklist must be automated in the CI pipeline, not reliant on human memory.

## Key Takeaways
1. **Integration:** Integration is where "works on my machine" meets reality. Always test integration points heavily before production.
2. **Automation:** Checklists for production readiness must be automated.
3. **Platform Mindset:** A platform implies other teams consume it. Clear API contracts, SLAs, and documentation are more important than isolated internal code quality.

## Links
- [[day28_overview]]

---

### Day 28 Review Questions

1. **According to the lecture, what is an **anti-pattern** in integrating AI Platform components?**  
   - A. Using event-driven integration with Kafka  
   - B. Maintaining configuration in Git (GitOps)  
   - C. Tightly coupling between components  
   - D. Applying the Bulkhead pattern to separate inference and training  
   **Answer:** C  

2. **In the end-to-end request flow, what is the target time for each component?**  
   - A. Vector Search < 5ms, Feature Store < 50ms, LLM Inference < 500ms  
     *A. Vector Search < 5ms, Feature Store < 50ms, LLM Inference < 500ms*  
   - B. Feature Store < 5ms, Vector Search < 50ms, LLM Inference < 500ms  
     *B. Feature Store < 5ms, Vector Search < 50ms, LLM Inference < 500ms*  
   - C. Feature Store < 50ms, Vector Search < 500ms, LLM Inference < 5ms  
     *C. Feature Store < 50ms, Vector Search < 500ms, LLM Inference < 5ms*  
   - D. All need to be under 100ms  
   **Answer:** B  

3. **Which tool is recommended for **detailed latency breakdown analysis** across the entire flow?**  
   - A. Py-spy  
     *A. Py-spy*  
   - B. Tracemalloc  
     *B. Tracemalloc*  
   - C. Jaeger  
     *C. Jaeger*  
   - D. cProfile  
     *D. cProfile*  
   **Answer:** C  

4. **What is the prerequisite for deploying the Platform to production according to the 5 Pillars?**  
   - A. Manual checking of the Production Readiness checklist by an engineer  
   - B. Automating the checklist in the CI pipeline  
   - C. Ensuring all code runs in the local environment  
   - D. Using a single framework for the entire stack  
   **Answer:** B  

5. **Which of the following models is the correct **integration pattern** to avoid shared mutable state?**  
   - A. Using a shared database with concurrent writes  
   - B. Immutable events and event sourcing via append-only log (Kafka)  
   - C. Storing state in a global variable  
   - D. Using a static JSON configuration file  
   **Answer:** B
