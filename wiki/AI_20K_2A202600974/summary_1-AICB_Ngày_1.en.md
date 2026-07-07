---
type: summary
title: "Summary: AICB Day 1 - AI & LLM Foundation"
description: "A comprehensive overview of AI evolution, LLM fundamentals, Transformer architecture, token economy, and practical API usage."
tags: [AI, LLM, Transformer, Token Economy, API, VibeCoding, Agentic AI]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/1/1-AICB_Ngày_1.pdf"]
---
# AICB Day 1 - AI & LLM Foundation

## 1. Overview and AI Evolution
The lecture covers the transition of Artificial Intelligence through several phases, highlighting the shift from classical Machine Learning and Deep Learning to Generative AI and finally to **Agentic AI**.
- **Generative AI** allows for the creation of content (text, images, video) from prompts.
- **Agentic AI** goes beyond single-step generation. It sets goals, plans, and takes actions iteratively by connecting to external tools and APIs.

### The Evolution Timeline
1. Perceptron (1957)
1. *Perceptron (1957)*
2. Deep Learning Boom (2012)
3. Transformer Architecture (2017)
4. ChatGPT (2022)
4. *ChatGPT (2022)*
5. AI Agents (2024-2026)

## 2. LLMs: The Engine of Modern AI
Large Language Models (LLMs) act as the foundational reasoning engines for both Generative and Agentic AI.

### Transformer Architecture
The core architecture powering LLMs is the **Decoder-only Transformer**. It relies on predicting the next token sequentially (Next-Token Prediction) based on all preceding context.
Key mechanisms include:
- **Self-Attention**: Every token "attends" to every other token, capturing complex contextual relationships.
- **Multi-Head Attention**: Multiple attention mechanisms run in parallel, allowing the model to capture different types of relationships simultaneously.
- **Positional Encoding**: Injects sequence order information into the model since self-attention inherently lacks a sense of position.

### LLM Training Pipeline
1. **Pre-training**: Reading massive amounts of internet text to learn language and general knowledge.
2. **Supervised Fine-Tuning (SFT)**: Learning from examples to format responses appropriately.
3. **RLHF / DPO**: Aligning the model with human preferences for safety and helpfulness.

## 3. Token Economy
Tokens are the fundamental units of text processing for LLMs (roughly 0.75 of an English word).
- **Cost**: The API cost is determined by the number of Input Tokens and Output Tokens. Output tokens are typically more expensive.
- **Latency**: Processing more tokens increases latency. Context window limits the maximum number of tokens an LLM can process in a single request.
- **Language Nuances**: Non-English languages (like Vietnamese) and code typically require more tokens to encode, increasing costs.

## 4. API Usage and Model Selection
The lecture provides a practical guide on calling LLM APIs (OpenAI, Anthropic) and managing parameters:
- **Temperature**: Controls creativity (0 is deterministic, 1 is highly diverse).
- **Model Selection**: Trade-offs between cost, latency, and quality. Examples include using Claude Haiku for fast, cheap routing and Claude Opus or GPT-4o for complex reasoning.
- **Streaming**: Receiving responses chunk by chunk to reduce perceived latency for the user.

## 5. VibeCoding
*## 5. VibeCoding*
VibeCoding is a new programming paradigm where the developer describes the intent and context to an AI, which then generates the code.
- **Mindset Shift**: From writing manual code to directing an AI, reviewing its logic, and refining the output.
- **Principles**:
  1. Intent-driven: Clearly articulate goals.
  2. Context-first: Provide the necessary files, examples, and constraints.
  3. Human Review: Always review and validate the AI-generated code.
