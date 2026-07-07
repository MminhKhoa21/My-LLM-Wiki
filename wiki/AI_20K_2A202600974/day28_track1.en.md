---
type: summary
title: "Summary of 1-ai_system_architectures_duong_trung_tin_pdf_ready"
description: "A comprehensive overview of real-world AI system architectures across ADAS, delivery robots, CCTV, humanoid robots, and satellite imaging."
tags: [ai, 20k, day28]
timestamp: 2026-07-06
sources: ["raw/AI_20K_2A202600974/28/1-ai_system_architectures_duong_trung_tin_pdf_ready.pdf"]
---
# Real-World AI System Architectures

## Overview
This document provides an overview of how real-world AI systems transition from a "working model" to a "production system." It covers five main AI systems:


- **ADAS / Autonomous Driving**
- **Autonomous Delivery Robot**
- **AI System for CCTV**
- **Humanoid Robot**
- **Satellite Image Application**

The core architectural layers common to these systems are:


1. **Data / Sensor:** Cameras, radars, lidars, logs, satellite imagery.
2. **Perception:** Detection, segmentation, tracking, embeddings.
3. **World State:** BEV (Bird's Eye View), maps, scene graphs.
4. **Decision / Policy:** Planner, VLA (Vision-Language-Action), anomaly scorers.
5. **Action / Product:** Control, delivery, alerts, dashboards.
6. **Ops / Safety:** ODD (Operational Design Domain), HITL (Human-in-the-loop), telemetry, audit, and retraining.

## 1. ADAS / Autonomous Driving

- **Architecture:** Transitioning from modular to planning-oriented End-to-End (E2E) approaches.
- **Key Concepts:**
  - **UniAD & VAD:** Incorporating perception, tracking, prediction, and planning in a single pipeline.
  - **DriveLM:** Utilizing VLM (Vision-Language Models) for reasoning and graph VQA for decision making.
  - **GAIA-1 / GAIA-2:** Using World Models for rare scenario simulation.
- **Lessons Learned:** ODD must be defined before the model. An E2E policy still needs an independent safety shell.

## 2. Autonomous Delivery Robot

- **Architecture:** Sidewalk autonomy involves low-speed navigation, social awareness, fleet economics, and remote assistance.
- **Key Concepts:**
  - **Hybrid Autonomy:** Autonomy combined with remote human assistance.
  - **Social Navigation:** Anticipating pedestrian behaviors.
- **Lessons Learned:** Fleet operations (docking, maintenance) are the main moat. Remote assistants need high observability to handle stuck cases effectively.

## 3. AI System for CCTV

- **Architecture:** Transitioning from fixed-class real-time detection to open-vocabulary and semantic search.
- **Key Concepts:**
  - **Edge Inference:** Utilizing YOLOv8/v10 for lightweight edge detection.
  - **Open-Vocabulary:** Using SAM / Grounded SAM for text-conditioned detection.
  - **VLM Anomaly:** Using VLMs to detect and explain anomalies in long videos.
- **Lessons Learned:** The goal is to reduce the number of clips for human review, not just applying large models to every frame. Edge computation is crucial for privacy and bandwidth optimization.

## 4. Humanoid Robot

- **Architecture:** Contact-rich manipulation combining System 1 (fast control loop) and System 2 (VLA reasoning).
- **Key Concepts:**
  - **VLA Models:** RT-2, GR00T.
  - **Imitation & RL:** Teleoperation data (Mobile ALOHA) and Sim-to-Real reinforcement learning.
- **Lessons Learned:** Robot data is more expensive than web data. Sim-to-real gap necessitates domain randomization. Safety guards (e-stops, torque limits) must be independent of the policy.

## 5. Satellite Image Application

- **Architecture:** GeoAI involves massive data engineering, optical/SAR processing, and temporal fusion.
- **Key Concepts:**
  - **Geospatial Foundation Models:** Prithvi, Clay.
  - **Multi-temporal & Multi-modal:** Combining different temporal baselines and sensors (Optical + SAR + text).
- **Lessons Learned:** Change detection requires temporal baselines. Uncertainty mapping and Human Analyst Loops are vital for production.

## Key Takeaways

1. **Architecture Beats Benchmark:** A good model requires the correct data path, latency constraints, safety shell, and ops loop.
2. **End-to-End Doesn't Mean No System:** E2E policies still need ODD and monitoring.
3. **Data Flywheel:** Systems scale effectively by capturing edge cases and feeding them back into training loops.

- [[day28_overview]]
