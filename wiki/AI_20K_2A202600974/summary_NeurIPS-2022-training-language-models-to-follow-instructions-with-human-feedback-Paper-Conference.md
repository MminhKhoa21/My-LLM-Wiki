---
type: summary
title: "Summary: Training Language Models to Follow Instructions with Human Feedback (InstructGPT)"
description: "A summary of the InstructGPT paper detailing how Reinforcement Learning from Human Feedback (RLHF) is used to align language models."
tags: [RLHF, InstructGPT, Alignment, Human Feedback, LLM]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/1/NeurIPS-2022-training-language-models-to-follow-instructions-with-human-feedback-Paper-Conference.pdf"]
---

# Training Language Models to Follow Instructions with Human Feedback

## 1. Introduction
The InstructGPT paper (published at NeurIPS 2022) addresses a critical issue in Large Language Models: alignment. Standard LLMs are trained to predict the next token on a massive corpus of internet text, which means they often generate outputs that are untruthful, toxic, or simply unhelpful to the user's actual intent. To solve this, the authors introduce a method to align models to follow user instructions using **Reinforcement Learning from Human Feedback (RLHF)**.

## 2. The Alignment Problem
Pre-trained models simply autocomplete text. When prompted with a question, they might answer it, but they might also generate more questions or continue a tangent. The goal of alignment is to make the model "helpful, honest, and harmless" by fine-tuning it to follow the explicit instructions provided in user prompts.

## 3. The RLHF Methodology
The process of creating InstructGPT involves three main steps:

### Step 1: Supervised Fine-Tuning (SFT)
- Human labelers write prompts and provide the desired, high-quality responses.
- The pre-trained LLM is fine-tuned on this dataset using standard supervised learning.
- This creates the initial SFT model, which learns the basic format of answering instructions but is expensive to scale since human experts must write every full response.

### Step 2: Reward Model (RM) Training
- The SFT model generates several different responses for a given prompt.
- Human labelers rank these responses from best to worst based on helpfulness and safety.
- A reward model is trained on these rankings. The reward model learns to predict a scalar reward representing human preference for any given prompt-response pair.

### Step 3: Reinforcement Learning (PPO)
- The SFT model is further optimized against the reward model using the Proximal Policy Optimization (PPO) reinforcement learning algorithm.
- The environment presents a random prompt, the model generates a response, and the reward model scores it. PPO updates the model's policy to maximize this reward.
- A KL-divergence penalty is added to ensure the model doesn't drift too far from the original SFT model (which prevents the model from exploiting the reward model by generating gibberish that technically scores high).

## 4. Key Results
- **Human Preference:** Human evaluators overwhelmingly preferred the outputs of InstructGPT (1.3B parameters) over a much larger pre-trained GPT-3 (175B parameters), despite having 100x fewer parameters.
- **Improved Metrics:** InstructGPT showed improvements in truthfulness and reductions in toxic output generation compared to the base model.
- **Generalization:** The model generalized well to instructions outside the RLHF distribution, meaning it could follow instructions it hadn't explicitly been trained on during the fine-tuning phase.

## 5. Conclusion
This paper established RLHF as the standard paradigm for aligning large language models, paving the way for conversational models like ChatGPT that are highly responsive to human intent rather than merely autocompleting text.
