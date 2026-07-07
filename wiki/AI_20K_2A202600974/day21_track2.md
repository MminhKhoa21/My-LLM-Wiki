---
type: summary
title: "Day 21 Track 2: CI/CD AI Systems"
description: "Tự động hóa vòng đời mô hình AI từ thí nghiệm đến production bằng MLflow, DVC và GitHub Actions."
tags: [ai, 20k, day21, track2, cicd, mlflow, dvc, github-actions]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/21/Day 21 - Track 2 - CICD AI SYSTEMS.pptx"]
---
> **Lộ trình:** [[track2_ai_engineer|Track 2: AI Engineer]]  
> **Roadmap:** [[track2_ai_engineer|Track 2: AI Engineer]]  

# CI/CD for AI Systems (Day 21 - Track 2)  
# CI/CD cho Hệ Thống AI (Ngày 21 - Track 2)  

**Giảng viên**: VinUniversity  
**Instructor**: VinUniversity  

**Khóa**: AICB Phase 2 · Track 2  
**Course**: AICB Phase 2 · Track 2  

> **Câu hỏi trọng tâm**: Code thay đổi mỗi ngày — model cũng vậy. CI/CD cho AI khác gì CI/CD cho software thông thường? Nếu quản lý thủ công, model dễ bị regression mà không ai hay biết.  
> **Key question**: Code changes daily — models do too. How is CI/CD for AI different from CI/CD for regular software? If managed manually, models can regress without anyone knowing.  

## 1. Tổng Quan về CI/CD trong AI  
## 1. Overview of CI/CD in AI  

- Automating the model lifecycle (from experimentation to production) is critical to prevent model regression.  
  *Việc tự động hóa vòng đời model (từ lúc thử nghiệm đến production) là cực kỳ quan trọng để ngăn chặn model regression.*  

- **Goal:** Set up a pipeline so that every change in code, data, or parameters is tested, evaluated, and deployed automatically and safely.  
  ***Mục tiêu:** Setup pipeline để mọi thay đổi về code, data, hoặc parameters đều được test, evaluate và deploy tự động một cách an toàn.*  

## 2. Các Thành Phần và Công Cụ Chính  
## 2. Key Components and Tools  

- **MLflow Experiment Tracking & Model Registry:** Log experiments systematically. Record parameters, metrics, and artifacts. Compare runs via UI. Manage model lifecycle (Model Registry).  
  ***MLflow Experiment Tracking & Model Registry:** Lưu vết (log) các experiments một cách có hệ thống. Ghi lại parameters, metrics, và artifacts. So sánh các "runs" qua UI. Quản lý vòng đời mô hình (Model Registry).*  

- **DVC (Data Version Control) & Pipelines:** Manage data versioning and define reproducible ML pipelines via `dvc.yaml`.  
  ***DVC (Data Version Control) & Pipelines:** Quản lý phiên bản dữ liệu (data versioning) và định nghĩa các bước thực thi (reproducible ML pipelines) thông qua `dvc.yaml`.*  

- **GitHub Actions CI/CD Pipeline:** CI/CD automation platform. Runs auto test, auto train, and evaluate automatically whenever new code is pushed.  
  ***GitHub Actions CI/CD Pipeline:** Nền tảng tự động hóa CI/CD. Chạy auto test, auto train, và evaluate tự động mỗi khi có code mới.*  

- **CD Model Deployment Strategies:** Apply safe deployment strategies to minimize risk when releasing a new model:  
  ***CD Model Deployment Strategies:** Áp dụng các chiến lược triển khai an toàn để giảm thiểu rủi ro khi release model mới:*  
  - Canary deployment.  
    *Triển khai Canary.*  
  - Blue/Green deployment.  
    *Triển khai Blue/Green.*  
  - Shadow deployment.  
    *Triển khai Shadow.*  

- **Testing Pyramid & Model Serving:** Apply the testing pyramid for AI systems and model serving combined with A/B Testing via MLflow.  
  ***Testing Pyramid & Model Serving:** Áp dụng tháp kiểm thử cho hệ thống AI và phục vụ (serving) model kết hợp với A/B Testing thông qua MLflow.*  

## 3. Deliverables của Lab  
## 3. Lab Deliverables  

- **MLflow Tracking Server:** Log at least 3 tracked experiments with full params, metrics, and artifacts. The model is pushed to the Registry.  
  ***MLflow Tracking Server:** Ghi lại (log) ít nhất 3 tracked experiments với đầy đủ params, metrics, artifacts. Model được đẩy lên Registry.*  

- **DVC Pipeline:** At least 3 stages (prepare -> train -> evaluate) that can be successfully reproduced using `dvc repro`.  
  ***DVC Pipeline:** Có ít nhất 3 stages (prepare -> train -> evaluate) có thể chạy lại thành công bằng lệnh `dvc repro`.*  

- **GitHub Actions Workflow:** A pipeline that passes the check gates (test -> train -> eval gate -> deploy) on the repository.  
  ***GitHub Actions Workflow:** Pipeline vượt qua các cổng kiểm tra (test -> train -> eval gate -> deploy) trên repository.*  

## 4. Liên Kết  
## 4. Links  

[[day21_overview]]
