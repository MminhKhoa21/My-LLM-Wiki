---
type: overview
title: "Day 12: Deployment - Đưa Agent Lên Cloud"
description: "Hướng dẫn containerize và đưa Agent lên môi trường production với các kiến trúc từ tự deploy đến Managed Services."
tags: [ai, 20k, day12, deployment, cloud, docker]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/12/day12-deployment-dua-agent-len-cloud.pdf"]
---

# Day 12: Deployment — Đưa Agent Lên Cloud

## Nội dung chính
Khác với ứng dụng web truyền thống (CRUD), AI Agent có thời gian phản hồi (latency) lâu hơn rất nhiều do phụ thuộc vào reasoning loop và việc gọi các API bên ngoài. Điều này khiến việc deploy AI Agent đối mặt với các vấn đề về timeout và statelessness.

## Đóng gói ứng dụng (Containerization)
- **Docker**: Sử dụng Dockerfile (Multi-stage build) để đóng gói mã nguồn và môi trường (dependencies, OS layer) thành một Image độc lập, nhỏ gọn (ví dụ dùng `python-slim`, `uv`).
- Mục đích để đảm bảo tính đồng nhất giữa môi trường phát triển (Dev) và môi trường thật (Production).

## Các Thách thức của Agent Deployment
1. **Timeout**: Gateway thường ngắt kết nối nếu Agent suy nghĩ quá lâu (ví dụ 30s-60s). Cách giải quyết: Sử dụng **Streaming (SSE - Server-Sent Events)** để gửi heartbeat giữ kết nối, hoặc chuyển sang kiến trúc **Async Job** (Submit-and-poll).
2. **Statefulness**: Nguyên tắc 12-Factor App yêu cầu ứng dụng phải *stateless*. Nhưng Agent cần lưu giữ bộ nhớ hội thoại/quá trình thực thi. Giải pháp là chuyển trạng thái ra bộ nhớ ngoài (Externalize state vào Redis/Postgres) để scale nhiều instance mà không bị mất dấu vết.
3. **Concurrency & Cold Start**: Các instance cần chờ I/O khá lâu, việc tải model hoặc khởi tạo tốn tài nguyên.

## Các tầng Deployment (Tiers)
- **Tier 0 (Managed Agent Runtime)**: Platform lo hạ tầng, session, memory (AWS Bedrock AgentCore, Vertex AI, v.v.). Thích hợp ship nhanh.
- **Tier 1 (PaaS/Serverless Containers)**: Render, Railway, Fly.io. Tự lo container, nhưng hạ tầng triển khai nhanh gọn. Phù hợp cho MVP.
- **Tier 2/3 (CaaS/Kubernetes)**: Cloud Run, ECS Fargate, Kubernetes. Dành cho các hệ thống scale lớn và cần tối ưu chi phí.

## API Gateway & Security
- Cần triển khai API Gateway đứng trước Agent để làm nhiệm vụ **Authentication** (API Key, OAuth), **Rate Limiting** và **Cost Protection** (cảnh báo hoặc ngắt kết nối trước khi cạn ngân sách do LLM call liên tục).
