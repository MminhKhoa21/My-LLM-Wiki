---
type: summary
title: "Day 22 – Track 3: DPO, ORPO & Alignment"
description: "Sự dịch chuyển từ SFT sang Preference Learning, chi tiết phương pháp DPO, ORPO, SimPO, GRPO và cách đánh giá Alignment qua LLM Benchmarks."
tags: [ai, 20k, day22, track3, dpo, orpo, alignment, rlhf, grpo]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/Day 22 - Track 3 - DPO-ORPO-Alignment.pdf", "raw/AI_20K_2A202600974/22/Day 22 - Track 3 - DPO-ORPO-Alignment_v2.pdf"]
---
Nội dung bạn cung cấp đã ở dạng song ngữ (Anh – Việt) hoàn chỉnh với đúng định dạng Markdown, mỗi phần đều có tiếng Anh trước và tiếng Việt in nghiêng bên dưới (hoặc viết liền trên cùng một dòng nhưng vẫn rõ ràng hai ngôn ngữ). Không phát hiện phần nào bị thiếu ngôn ngữ.

Dưới đây là bản giữ nguyên như file gốc, không thay đổi gì thêm:

**Path:** [[track3_ai_app|Track 3: AI Application]]  
***Lộ trình:** [[track3_ai_app|Track 3: AI Application]]*

# Day 22 – Track 3: DPO, ORPO & Alignment  
# *Ngày 22 – Track 3: DPO, ORPO & Alignment*

**Instructor:** VinUniversity  
***Giảng viên:** VinUniversity*  
**Course:** AICB Phase 2 · Track 3 · Day 22  
***Khóa:** AICB Phase 2 · Track 3 · Ngày 22*

---

## 1. From SFT to Preference Learning  
## *1. Từ SFT đến Preference Learning*

SFT (Supervised Fine-Tuning) teaches the model format and style (the model learns what to say).  
*SFT (Supervised Fine-Tuning) dạy cho model biết format và style (model học "nói **gì**").*

However, SFT-only models often tend to be overly cautious (over-hedges), verbose, or excessively refuse.  
*Tuy nhiên, SFT-only thường có tính chất quá thận trọng (over-hedges), lan man (verbose) hoặc từ chối quá mức (refusal).*

**Alignment** (teaching the model "how to say") is the step that helps the model learn the *margin* between a good and a bad answer (helpful, harmless, honest) based on **Preference Data** (chosen vs. rejected pairs).  
***Alignment** (dạy model "nói **như thế nào**") là bước giúp model học được *margin* giữa một câu trả lời tốt và xấu (helpful, harmless, honest) dựa trên **Preference Data** (Cặp chosen vs rejected).*

---

## 2. RLHF and the DPO Breakthrough  
## *2. RLHF và Bước tiến DPO*

### The Cost of RLHF (PPO)  
### *Sự đắt đỏ của RLHF (PPO)*

The InstructGPT pipeline: SFT → Reward Model (judge) → PPO (optimization).  
*Quy trình InstructGPT: SFT → Reward Model (giám khảo) → PPO (tối ưu).*

Disadvantages: requires loading three models simultaneously, high VRAM usage, PPO instability, and very sensitive hyperparameters.  
*Nhược điểm là cần tải đồng thời 3 models, tốn VRAM, PPO instability và hyperparams rất nhạy cảm.*

### DPO (Direct Preference Optimization)  
### *DPO (Direct Preference Optimization)*

Core idea of **DPO (2023)**: Eliminate the intermediate Reward Model entirely.  
*Ý tưởng cốt lõi của **DPO (2023)**: Loại bỏ hẳn Reward Model trung gian.*

Mathematics proves that the Optimal RL Policy has a closed-form solution.  
*Toán học chứng minh rằng Optimal RL Policy có closed-form solution.*

We can directly map preference pairs into a loss function for the model to learn:  
*Ta có thể map trực tiếp cặp preference vào Loss để model tự học:*

- **DPO Loss formula:** Optimizes cross-entropy on log-ratio probabilities of `chosen` vs `rejected`.  
  ***Công thức DPO Loss:** Tối ưu hóa cross-entropy trên log-ratio probabilities của `chosen` vs `rejected`.*
- **Hyperparameter β (KL penalty):** Controls the divergence from the Reference Model.  
  ***Hyperparameter β (KL penalty):** Kiểm soát độ phân kỳ so với Reference Model.*
    - Increasing β (e.g., 0.2): Forces conservatism, stays close to the SFT base.  
      *Tăng β (vd 0.2): Ép bảo thủ, gần với SFT base.*
    - Decreasing β (e.g., 0.05): Avoids conservatism, model is more free.  
      *Giảm β (vd 0.05): Tránh conservative, model tự do hơn.*
- **Advantages:** Offline learning (more stable than PPO), fewer components. Still the strong default choice for helpfulness, tone, and safety problems.  
  ***Ưu điểm:** Offline learning (ổn định hơn PPO), tốn ít components. Vẫn là default choice mạnh mẽ cho các bài toán Helpfulness, tone, safety.*

---

## 3. ORPO, SimPO & Alternatives (Single-Stage / No-Ref Generation)  
## *3. ORPO, SimPO & Alternatives (Thế hệ Single-Stage / No-Ref)*

DPO still requires an SFT stage and a Reference model. New methods gradually remove these components.  
*DPO vẫn đòi hỏi SFT stage và Reference model. Các phương pháp mới loại bỏ dần các thành phần:*

- **SimPO (2024):** No reference model needed. Uses *average log-prob* (length-normalized) to avoid length hacking. Very good when VRAM is limited.  
  ***SimPO (2024):** Không cần reference model. Dùng *average log-prob* (length-normalized) để tránh model học lách luật viết dài (length hacking). Rất tốt khi VRAM hạn chế.*
- **ORPO (2024):** Single-stage Alignment. Trains directly from Base Model to Aligned Model **without needing an SFT stage**. Integrates Odds Ratio preference into the loss.  
  ***ORPO (2024):** Single-stage Alignment. Train thẳng từ Base Model lên Aligned Model mà **không cần SFT stage**. Tích hợp Odds Ratio preference vào loss.*
- **KTO:** Only needs Thumbs Up/Down labels (suitable for production logs) instead of ranking pairs. Based on Prospect Theory (loss aversion model).  
  ***KTO:** Cần mỗi nhãn Thumbs Up/Down (phù hợp log từ production) thay vì cặp ranking. Dựa trên Prospect Theory (mô hình loss aversion).*

---

## 4. GRPO & RLVR: RL Returns for Reasoning  
## *4. GRPO & RLVR: RL Trở Lại Cho Reasoning*

In 2025 (DeepSeek R1 series), RL returns but in an optimized version, **without using Value Model / neural network Reward Model**:  
*Năm 2025 (DeepSeek R1 series), RL quay lại nhưng với phiên bản tối ưu, **không dùng Value Model / Reward Model mạng nơ-ron**:*

- **GRPO (Group Relative Policy Optimization):** Instead of using a Value Model network, it computes the average reward of a group of $G$ outputs as a baseline. Saves 50% VRAM and is very powerful for Reasoning.  
  ***GRPO (Group Relative Policy Optimization):** Thay vì dùng mạng Value Model, tính Reward trung bình của 1 nhóm G outputs làm baseline. Tiết kiệm 50% VRAM và rất mạnh cho Reasoning.*
- **RLVR (RL from Verifiable Rewards):** Reward comes not from a learned judge, but from *programmatic verification* (regex, code unit tests, math format). Blocks learned-RM reward hacking, but introduces Verifier Gaming. Suitable for code/math generation.  
  ***RLVR (RL from Verifiable Rewards):** Reward không đến từ judge học được, mà từ *programmatic verification* (regex, code unit tests, math format). Chặn đứng learned-RM reward hacking, nhưng đẻ ra Verifier Gaming. Phù hợp cho code/math generation.*

> **Rule of Thumb (Tulu 3 / Llama 3):** Modern alignment pipelines often stack: **SFT → Iterative DPO → GRPO/RLVR**.  
> ***Rule of Thumb (Tulu 3 / Llama 3):** Alignment pipeline hiện đại thường xếp chồng: **SFT → Iterative DPO → GRPO/RLVR**.*

---

## 5. Evaluating Alignment (LLM Benchmarks)  
## *5. Đánh Giá Alignment (LLM Benchmarks)*

Evaluating alignment is complex because open-ended tasks have no single ground truth. It typically combines three layers:  
*Đánh giá Alignment phức tạp vì open-ended tasks không có Ground-Truth duy nhất. Thường kết hợp 3 lớp:*

1. **Static Suites (Capability):** MMLU (Knowledge), GSM8K/MATH (Logical reasoning), IFEval (Format), HumanEval (Code). Monitors *Alignment Tax* (logic scores drop after alignment).  
   ***Static Suites (Capability):** MMLU (Kiến thức), GSM8K/MATH (Lý luận logic), IFEval (Format), HumanEval (Code). Theo dõi hiện tượng *Alignment Tax* (chỉ số logic giảm sau khi alignment).*
2. **Judge-Based Suites (Response Quality):** MT-Bench, AlpacaEval 2 LC (Corrects length-bias), Arena-Hard (Harder, skill-level classification). LLM-as-Judge measures Win-rate.  
   ***Judge-Based Suites (Response Quality):** MT-Bench, AlpacaEval 2 LC (Sửa length-bias), Arena-Hard (Khó hơn, phân loại kỹ năng). LLM-as-Judge đo Win-rate.*
3. **RewardBench:** A benchmark that evaluates "Judges" and Reward Models (meta-evaluation).  
   ***RewardBench:** Benchmark đánh giá chính các "Judges" và Reward Models (meta-evaluation).*

---

## References  
## *Liên kết*

- [[day21_track3]] – LoRA/QLoRA (pre-alignment fine-tuning step)  
  *[[day21_track3]] – LoRA/QLoRA (bước trước fine-tuning alignment)*  
- [[day22_overview]]  
  *[[day22_overview]]*
