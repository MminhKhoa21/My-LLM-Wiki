---
type: summary
title: "Day 22 – Track 3: DPO, ORPO & Alignment"
description: "Từ SFT đến Preference Learning: DPO, ORPO, SimPO, Constitutional AI và các phương pháp alignment hiện đại."
tags: [ai, 20k, day22, track3, dpo, orpo, alignment, fine-tuning]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/22/Day 22 - Track 3 - DPO-ORPO-Alignment_v2.pdf"]
---

> **Lộ trình:** [[track3_ai_app|Track 3: AI Application]]


# Day 22 – Track 3: DPO, ORPO & Alignment

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 3 · Ngày 22

---

## Tại sao SFT chưa đủ?

SFT (Supervised Fine-tuning) dạy model "nói **gì**" – nhưng chưa dạy model "nói **như thế nào**" để phù hợp với giá trị và kỳ vọng của con người.

---

## RLHF – Bức tranh toàn cảnh

1. **SFT**: Train trên demonstration data  
2. **Reward Model**: Train từ human preference pairs (chosen vs rejected)  
3. **PPO**: Tối ưu policy bằng RL để tối đa reward  

⚠️ Nhược điểm: Cần reward model riêng, pipeline phức tạp, tốn kém.

---

## DPO – Direct Preference Optimization

DPO loại bỏ reward model, tối ưu **trực tiếp** từ preference data:

$$\mathcal{L}_{DPO} = -\mathbb{E}_{(x,y_w,y_l)}\left[\log \sigma\left(\beta \log\frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log\frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)\right]$$

- **y_w**: chosen response, **y_l**: rejected response  
- β: temperature kiểm soát độ phân kỳ khỏi reference policy  
- Đơn giản hơn RLHF, kết quả tương đương hoặc tốt hơn

---

## ORPO, SimPO & Alternatives

| Phương pháp | Điểm khác biệt |
|------------|---------------|
| **ORPO** | Tích hợp preference optimization ngay trong SFT loss, không cần reference model |
| **SimPO** | Dùng average log-prob thay vì ratio, ổn định hơn |
| **GRPO** | RL comeback – Group Relative Policy Optimization (DeepSeek R1) |

---

## Constitutional AI & Red-teaming

- **Constitutional AI** (Anthropic): Model tự phê bình và sửa output dựa trên "hiến pháp" nguyên tắc  
- **Red-teaming**: Tìm kiếm chủ động các failure modes trước khi deploy

---

## Liên kết
- [[day21_track3]] – LoRA/QLoRA (bước trước fine-tuning alignment)
- [[day22_overview]]
