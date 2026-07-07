---
type: overview
title: "Day 1 Overview - AI & LLM Foundation"
description: "Tổng quan về bức tranh AI 2026, nền tảng LLM, kiến trúc Transformer và cách tính chi phí API."
tags: [ai, 20k, day1]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/1/1-AICB_Ngày_1.pdf"]
---
# Day 1: AI & LLM Foundation

## 1. The AI Landscape in 2026

The shift from Machine Learning and Generative AI to **Agentic AI**. AI is no longer just about "answering well" but also about **acting, connecting to tools, and generating ROI**. Agents are becoming more versatile, deeply personalized, and self-operating across multiple systems.

## 2. LLM — The Heart of Modern AI

- **Large Language Model (LLM)** is based on the **Transformer** architecture.

- **Transformer**: Uses the Self-Attention mechanism so that the model "pays attention" to the most relevant tokens in the context when generating the next word.

- Instead of sequential processing, the Transformer processes in parallel and understands context better through components such as Input Embedding, Positional Encoding, and Multi-Head Attention.

- Current LLMs operate mainly based on the **Next-token prediction** mechanism.

## 3. Token Economy
*## 3. Token Economy*

- **Token** is the smallest unit that an LLM processes (1 token ~ 0.75 English words, ~ 0.5 Vietnamese words).

- The cost of LLM APIs depends on the number of input tokens and output tokens, where output tokens are usually more expensive than input tokens.

- Languages like Vietnamese often consume more tokens due to Unicode encoding, leading to higher costs for the same content.

- The trade-off between **Latency** and **Cost**: The more tokens, the slower and more expensive the system becomes. Therefore, optimizing the Prompt and Context is essential.

## 4. Vibe Coding
*## 4. Vibe Coding*

Programming by collaborating with AI: Describe ideas and requirements in natural language so that the AI automatically generates code.

- The skill lies not in remembering syntax but in the ability to express logic and break down problems.

- Using APIs (OpenAI) to integrate LLMs into real-world applications.

- An API call involves three things to control: **quality, latency, cost**.

## 5. Common Models

- Categorize when to use expensive/high-capability models (e.g., GPT-4o, Claude Opus) vs. cheap/fast models (e.g., Claude Haiku, Gemini Flash).

- Rule of thumb: Start with a model that is **good enough and cheap enough**. Only upgrade when quality blocks the use case.
