---
type: summary
title: "Circuit Breakers, Caching & Reliability for Production Agents"
description: "Summary of Day 10 on reliability primitives including failure modes, circuit breakers, caching, observability, and chaos testing for production LLM agents."
tags: [reliability, circuit breaker, caching, observability, slo, chaos testing, llm agents]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/25/day10_reliability_student.pdf"]
---

# Circuit Breakers, Caching & Reliability for Production Agents

This document summarizes the content from the AICB-P2T3 Day 10 session on Agent Production-Ready concepts, focusing on reliability primitives.

## 1. Failure Modes

Reliability starts with correctly naming the errors. The 6 common failure modes to monitor in production LLM agents are:

1.  **Provider transient**: Errors like 429 (Rate Limit), 500 (Internal Server Error), or timeouts.
2.  **Degraded latency**: A sharp increase in P95 latency.
3.  **Full outage**: The provider stops responding completely.
4.  **Orchestration loop**: Errors related to state or incorrect retries.
5.  **Tool/cache failure**: Issues like stale cache, incorrect schema, or authentication failures.
6.  **Business action sai**: Incorrect business actions with side effects that cannot be rolled back.

### Silent Degradation
A system can degrade without explicit errors (e.g., error rate = 0%). This happens when:
- The provider updates the model silently.
- Prompt/schema changes but evaluation does not.
- Knowledge base becomes stale or retrieval weakens.
- Cache returns a previously correct but currently incorrect answer.

## 2. Circuit Breaker & Fallback

A **Circuit Breaker** stops calls to a failing provider, while a **Fallback** chain maintains user experience at an acceptable level.

### 3 States of a Circuit Breaker
- **CLOSED**: Normal calls proceed.
- **OPEN**: Fail fast. Transitions from CLOSED when the failure threshold is reached.
- **HALF-OPEN**: Probe call to test if the provider has recovered. Transitions from OPEN after a reset timeout. Transitions back to CLOSED on success, or OPEN on failure.

### Fallback Ladder (Graceful Degradation)
A typical fallback policy:
1.  **Best model** (Highest quality)
2.  **Backup provider** (Same feature set)
3.  **Cheaper/smaller model** (Limited quality)
4.  **Cached response**
5.  **Static fallback message**

*Note: Feature compatibility (JSON mode, tool calling, context length, latency/cost, policy behavior) must be checked when falling back to a weaker model.*

## 3. Caching & Cost Budgeting

Proper caching reduces latency and cost; improper caching causes stale answers and stable hallucinations.

### 3 Caching Layers for LLM Applications
1.  **Provider prompt/prefix cache**: Reduces cost when long prefixes are reused.
2.  **App semantic response cache**: Reuses responses for semantically similar queries.
3.  **Tool/result cache**: Caches expensive but deterministic API/DB results.

### Semantic Cache Flow
- **HIT**: `similarity > threshold` -> Return cache.
- **MISS**: `similarity < threshold` -> Call LLM -> Store result.
*Caution: Cache poisoning occurs when two queries are very close in cosine similarity but have different intents. Monitor hit rate and false-hit rate.*

### Cost Budgeting
Control costs at 3 layers:
1.  Per-request cap (max tokens, max tools, timeout).
2.  Per-user/app rate limit (token bucket).
3.  Monthly budget (warn at 80%, hard stop/route to cheaper model at 100%).

## 4. Observability & SLO

Without monitoring, it is impossible to know if the system is good, slow, expensive, or returning incorrect answers.

- **SLI (Service Level Indicator)**: The measured metric (e.g., availability, P95 latency, cache hit rate).
- **SLO (Service Level Objective)**: Internal target (e.g., availability >= 99%, P95 < 2.5s, fallback success >= 95%).
- **SLA (Service Level Agreement)**: External commitment (e.g., 99.5% uptime/month for customer-facing APIs).
- **Error budget**: The allowed failure rate before action is taken (e.g., freezing features to prioritize reliability).

*Note: LLM agents require quality SLOs in addition to uptime SLOs (e.g., faithfulness, safety pass rate, escalation correctness).*

## 5. Lab: Reliability Engineering

The lab involves building a reliability gateway that implements:
- Circuit breaker + semantic/tool cache
- Metrics instrumentation (JSON/CSV)
- Chaos testing and reporting

**Chaos Testing Scenarios:**
- Primary provider timeout 100%.
- Primary provider intermittent 50%.
- Cache returns stale candidate.
- Cost cap almost reached.

Expected evidence includes metrics showing the circuit breaker transitioning (CLOSED -> OPEN), gateway routing to fallback without a retry storm, and logged recovery time.
