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

***Lộ trình:** [[track3_ai_app|Track 3: AI Application]]*

# *Ngày 22 – Track 3: DPO, ORPO & Alignment*

***Giảng viên:** VinUniversity*  
***Khóa:** AICB Phase 2 · Track 3 · Ngày 22*

---

## *1. Từ SFT đến Preference Learning*

*SFT (Supervised Fine-Tuning) dạy cho model biết format và style (model học "nói **gì**").*

*Tuy nhiên, SFT-only thường có tính chất quá thận trọng (over-hedges), lan man (verbose) hoặc từ chối quá mức (refusal).*

***Alignment** (dạy model "nói **như thế nào**") là bước giúp model học được *margin* giữa một câu trả lời tốt và xấu (helpful, harmless, honest) dựa trên **Preference Data** (Cặp chosen vs rejected).*

---

## *2. RLHF và Bước tiến DPO*

### *Sự đắt đỏ của RLHF (PPO)*

*Quy trình InstructGPT: SFT → Reward Model (giám khảo) → PPO (tối ưu).*

*Nhược điểm là cần tải đồng thời 3 models, tốn VRAM, PPO instability và hyperparams rất nhạy cảm.*


*Ý tưởng cốt lõi của **DPO (2023)**: Loại bỏ hẳn Reward Model trung gian.*

*Toán học chứng minh rằng Optimal RL Policy có closed-form solution.*

*Ta có thể map trực tiếp cặp preference vào Loss để model tự học:*

  ***Công thức DPO Loss:** Tối ưu hóa cross-entropy trên log-ratio probabilities của `chosen` vs `rejected`.*
  ***Hyperparameter β (KL penalty):** Kiểm soát độ phân kỳ so với Reference Model.*
      *Tăng β (vd 0.2): Ép bảo thủ, gần với SFT base.*
      *Giảm β (vd 0.05): Tránh conservative, model tự do hơn.*
  ***Ưu điểm:** Offline learning (ổn định hơn PPO), tốn ít components. Vẫn là default choice mạnh mẽ cho các bài toán Helpfulness, tone, safety.*

---

## *3. ORPO, SimPO & Alternatives (Thế hệ Single-Stage / No-Ref)*

*DPO vẫn đòi hỏi SFT stage và Reference model. Các phương pháp mới loại bỏ dần các thành phần:*

  ***SimPO (2024):** Không cần reference model. Dùng *average log-prob* (length-normalized) để tránh model học lách luật viết dài (length hacking). Rất tốt khi VRAM hạn chế.*
  ***ORPO (2024):** Single-stage Alignment. Train thẳng từ Base Model lên Aligned Model mà **không cần SFT stage**. Tích hợp Odds Ratio preference vào loss.*
  ***KTO:** Cần mỗi nhãn Thumbs Up/Down (phù hợp log từ production) thay vì cặp ranking. Dựa trên Prospect Theory (mô hình loss aversion).*

---

## *4. GRPO & RLVR: RL Trở Lại Cho Reasoning*

*Năm 2025 (DeepSeek R1 series), RL quay lại nhưng với phiên bản tối ưu, **không dùng Value Model / Reward Model mạng nơ-ron**:*

  ***GRPO (Group Relative Policy Optimization):** Thay vì dùng mạng Value Model, tính Reward trung bình của 1 nhóm G outputs làm baseline. Tiết kiệm 50% VRAM và rất mạnh cho Reasoning.*
  ***RLVR (RL from Verifiable Rewards):** Reward không đến từ judge học được, mà từ *programmatic verification* (regex, code unit tests, math format). Chặn đứng learned-RM reward hacking, nhưng đẻ ra Verifier Gaming. Phù hợp cho code/math generation.*

> ***Rule of Thumb (Tulu 3 / Llama 3):** Alignment pipeline hiện đại thường xếp chồng: **SFT → Iterative DPO → GRPO/RLVR**.*

---

## *5. Đánh Giá Alignment (LLM Benchmarks)*

*Đánh giá Alignment phức tạp vì open-ended tasks không có Ground-Truth duy nhất. Thường kết hợp 3 lớp:*

   ***Static Suites (Capability):** MMLU (Kiến thức), GSM8K/MATH (Lý luận logic), IFEval (Format), HumanEval (Code). Theo dõi hiện tượng *Alignment Tax* (chỉ số logic giảm sau khi alignment).*
   ***Judge-Based Suites (Response Quality):** MT-Bench, AlpacaEval 2 LC (Sửa length-bias), Arena-Hard (Khó hơn, phân loại kỹ năng). LLM-as-Judge đo Win-rate.*
   ***RewardBench:** Benchmark đánh giá chính các "Judges" và Reward Models (meta-evaluation).*

---

## *Liên kết*

  *[[day21_track3]] – LoRA/QLoRA (bước trước fine-tuning alignment)*  
