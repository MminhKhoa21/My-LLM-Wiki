---
type: overview
title: "Day 12: Deployment - Đưa Agent Lên Cloud"
description: "Hướng dẫn containerize và đưa Agent lên môi trường production với các kiến trúc từ tự deploy đến Managed Services."
tags: [ai, 20k, day12, deployment, cloud, docker]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/12/day12-deployment-dua-agent-len-cloud.pdf"]
---
# Day 12: Deployment — Putting the Agent on the Cloud

## Main Content

Unlike traditional web applications (CRUD), AI Agents have much longer response times (latency) because they depend on reasoning loops and external API calls. This makes deploying AI Agents face issues with timeouts and statelessness.

## Containerization

- **Docker**: Use a Dockerfile (Multi-stage build) to package the source code and environment (dependencies, OS layer) into a self-contained, lightweight Image (e.g., using `python-slim`, `uv`).
- Purpose: Ensure consistency between the development (Dev) environment and the production environment.

## Challenges of Agent Deployment

1. **Timeout**: Gateways often drop the connection if the Agent thinks too long (e.g., 30s-60s). Solution: Use **Streaming (SSE - Server-Sent Events)** to send heartbeats and keep the connection alive, or switch to an **Async Job** architecture (submit-and-poll).

2. **Statefulness**: The 12-Factor App principle requires applications to be *stateless*. However, an Agent needs to persist conversation / execution memory. The solution is to externalize state (e.g., move state to Redis/Postgres) so that multiple instances can scale without losing context.

3. **Concurrency & Cold Start**: Instances have to wait for I/O for a long time; loading models or initialization consumes significant resources.

## Deployment Tiers

- **Tier 0 (Managed Agent Runtime)**: The platform handles infrastructure, sessions, and memory (AWS Bedrock AgentCore, Vertex AI, etc.). Suitable for fast shipping.

- **Tier 1 (PaaS/Serverless Containers)**: Render, Railway, Fly.io. You manage the container, but infrastructure deployment is quick. Suitable for MVPs.

- **Tier 2/3 (CaaS/Kubernetes)**: Cloud Run, ECS Fargate, Kubernetes. For large-scale systems that need cost optimization.

## API Gateway & Security
*## API Gateway & Security*

- It is necessary to deploy an API Gateway in front of the Agent to handle **Authentication** (API Key, OAuth), **Rate Limiting** and **Cost Protection** (alert or disconnect before the budget runs out due to continuous LLM calls).
