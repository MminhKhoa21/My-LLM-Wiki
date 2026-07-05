---
type: summary
title: "Summary: grading_questions.pdf"
description: "A detailed summary of the Day 8 RAG grading questions dataset, illustrating how to evaluate complex RAG capabilities like cross-document synthesis, temporal scoping, and hallucination resistance."
tags: [ai, 20k, day8, rag, evaluation, dataset]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/grading_questions.pdf"]
---

# Summary: RAG Grading Questions (Day 08)

## Overview
This document summarizes the contents of `grading_questions.pdf`, which contains a suite of 10 test questions designed to evaluate the robustness and accuracy of a Retrieval-Augmented Generation (RAG) pipeline. These questions are structured to test specific RAG capabilities, highlighting common failure modes and expected criteria for high-quality responses.

## Key Themes and RAG Capabilities Tested

### 1. Freshness & Version Reasoning (Question: `gq01`)
- **Focus:** Differentiating between updated and outdated metrics (e.g., SLA resolution time dropping from 6 hours to 4 hours in v2026.1).
- **Skill Tested:** Evaluating whether the pipeline retrieves the latest chunk or gets confused by older metadata.
- **Expected Behavior:** Must explicitly mention the historical change and cite the correct version.

### 2. Multi-Document Synthesis (Questions: `gq02`, `gq06`)
- **Focus:** Answering questions that require fusing information from multiple distinct documents.
  - *Example (`gq02`):* VPN requirements from the HR Leave Policy synthesized with device limits from the IT Helpdesk FAQ.
  - *Example (`gq06`):* Synthesizing emergency escalation steps from the Access Control SOP with contact info from the SLA P1 document.
- **Skill Tested:** Cross-document retrieval and complete synthesis without omitting parts of the answer.

### 3. Completeness & Exception Handling (Question: `gq03`)
- **Focus:** Identifying multiple conditions or exceptions within a single policy (e.g., refund exceptions for Flash Sale items *and* activated items).
- **Skill Tested:** Ensuring the retriever fetches the entire relevant section (chunk completeness) and that the LLM mentions *all* exceptions, not just the first one it encounters.

### 4. Specific Numeric Fact Retrieval (Question: `gq04`)
- **Focus:** Extracting an exact percentage or number buried in a text (e.g., 110% store credit alternative to a refund).
- **Skill Tested:** Faithfulness and precision. The model must not hallucinate a standard number like 100% or 120%.

### 5. Multi-Detail Retrieval & Scope Identification (Questions: `gq05`, `gq09`)
- **Focus:** Extracting multiple prerequisites for an action (e.g., granting Admin Access requires IT Manager + CISO approval, 5 days processing, and mandatory training; password reset intervals and reminder times).
- **Skill Tested:** Multi-chunk reasoning within the same document and extracting composite details from FAQ-style content.

### 6. Hallucination Resistance & Abstention (Question: `gq07`)
- **Focus:** Asking a plausible-sounding question whose answer does *not* exist in the corpus (e.g., "What is the penalty for violating SLA P1?").
- **Skill Tested:** The model's ability to confidently state that the information is missing ("Insufficient Context") instead of guessing or fabricating a penalty based on general internet knowledge.

### 7. Disambiguation (Question: `gq08`)
- **Focus:** Handling instances where the same keyword/number appears in different contexts (e.g., "3 days" notice for annual leave vs. "3 days" sick leave requiring a medical certificate).
- **Skill Tested:** Semantic disambiguation. The pipeline must not mix up the rules tied to identical numeric values.

### 8. Temporal Scoping & Metadata-Aware Retrieval (Question: `gq10`)
- **Focus:** Querying policies based on specific dates (e.g., applying Refund Policy v4 only to orders placed after 01/02/2026).
- **Skill Tested:** Verifying if the pipeline uses `effective_date` metadata to filter and reason about temporal constraints to avoid answering using stale documents.

## Conclusion
This dataset serves as an excellent benchmark ("Golden Dataset") for evaluating a RAG pipeline across the core metrics of Context Recall, Faithfulness, and Answer Relevance (the RAGAS Triad). It specifically targets complex edge cases that basic semantic search often fails to handle correctly.
