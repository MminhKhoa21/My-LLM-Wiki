---
type: summary
title: "Day 21 Track 2: CI/CD AI Systems"
description: "Tự động hóa vòng đời mô hình AI từ thí nghiệm đến production bằng MLflow, DVC và GitHub Actions."
tags: [ai, 20k, day21, track2, cicd, mlflow, dvc, github-actions]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/Day 21 - Track 2 - CICD AI SYSTEMS.pptx"]
---
> **Roadmap:** [[track2_ai_engineer|Track 2: AI Engineer]]  

# CI/CD for AI Systems (Day 21 - Track 2)  

**Instructor**: VinUniversity  

**Course**: AICB Phase 2 · Track 2  

> **Key question**: Code changes daily — models do too. How is CI/CD for AI different from CI/CD for regular software? If managed manually, models can regress without anyone knowing.  

## 1. Overview of CI/CD in AI  

- Automating the model lifecycle (from experimentation to production) is critical to prevent model regression.  

- **Goal:** Set up a pipeline so that every change in code, data, or parameters is tested, evaluated, and deployed automatically and safely.  

## 2. Key Components and Tools  

- **MLflow Experiment Tracking & Model Registry:** Log experiments systematically. Record parameters, metrics, and artifacts. Compare runs via UI. Manage model lifecycle (Model Registry).  

- **DVC (Data Version Control) & Pipelines:** Manage data versioning and define reproducible ML pipelines via `dvc.yaml`.  

- **GitHub Actions CI/CD Pipeline:** CI/CD automation platform. Runs auto test, auto train, and evaluate automatically whenever new code is pushed.  

- **CD Model Deployment Strategies:** Apply safe deployment strategies to minimize risk when releasing a new model:  
  - Canary deployment.  
  - Blue/Green deployment.  
  - Shadow deployment.  

- **Testing Pyramid & Model Serving:** Apply the testing pyramid for AI systems and model serving combined with A/B Testing via MLflow.  

## 3. Lab Deliverables  

- **MLflow Tracking Server:** Log at least 3 tracked experiments with full params, metrics, and artifacts. The model is pushed to the Registry.  

- **DVC Pipeline:** At least 3 stages (prepare -> train -> evaluate) that can be successfully reproduced using `dvc repro`.  

- **GitHub Actions Workflow:** A pipeline that passes the check gates (test -> train -> eval gate -> deploy) on the repository.  

## 4. Links  

[[day21_overview]]
