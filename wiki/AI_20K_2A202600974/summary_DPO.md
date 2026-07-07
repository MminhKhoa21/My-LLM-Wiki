---
type: summary
title: "Summary: Direct Preference Optimization (DPO)"
description: "A summary of Direct Preference Optimization, a lightweight alternative to RLHF that aligns language models without requiring a separate reward model or complex reinforcement learning."
tags: [DPO, Alignment, RLHF, Preference Optimization, LLM]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/1/DPO.pdf"]
---

# Direct Preference Optimization (DPO)
# Tối ưu hóa Sở thích Trực tiếp (Direct Preference Optimization - DPO)

## 1. Introduction
## 1. Giới thiệu
Direct Preference Optimization (DPO) is a method for aligning large language models with human preferences. While Reinforcement Learning from Human Feedback (RLHF) has been highly successful for model alignment, it is notoriously complex and unstable, requiring the training of a separate reward model and the use of algorithms like PPO. DPO simplifies this process entirely by treating the language model itself as a reward model, allowing alignment directly from preference data using standard cross-entropy loss.
Tối ưu hóa Sở thích Trực tiếp (DPO) là một phương pháp để tinh chỉnh các mô hình ngôn ngữ lớn sao cho phù hợp với sở thích của con người. Mặc dù Học tăng cường từ Phản hồi của Con người (RLHF) đã rất thành công trong việc tinh chỉnh mô hình, nhưng nó nổi tiếng là phức tạp và không ổn định, đòi hỏi phải huấn luyện một mô hình phần thưởng riêng biệt và sử dụng các thuật toán như PPO. DPO đơn giản hóa hoàn toàn quá trình này bằng cách coi chính mô hình ngôn ngữ như một mô hình phần thưởng, cho phép tinh chỉnh trực tiếp từ dữ liệu sở thích bằng cách sử dụng hàm mất mát cross-entropy tiêu chuẩn.

## 2. The Problem with RLHF
## 2. Vấn đề với RLHF
Standard RLHF pipelines (like InstructGPT) are a complex, multi-stage process:
Các quy trình RLHF tiêu chuẩn (như InstructGPT) là một quá trình đa giai đoạn phức tạp:
1. Train a Supervised Fine-Tuning (SFT) model.
1. Huấn luyện một mô hình Tinh chỉnh có Giám sát (SFT).
2. Collect human preference data (pairs of good and bad responses).
2. Thu thập dữ liệu sở thích của con người (các cặp câu trả lời tốt và xấu).
3. Train a separate Reward Model (RM) to predict human preferences.
3. Huấn luyện một Mô hình Phần thưởng (RM) riêng biệt để dự đoán sở thích của con người.
4. Optimize the policy (the SFT model) against the RM using Reinforcement Learning (e.g., PPO).
4. Tối ưu hóa chính sách (mô hình SFT) dựa trên RM bằng Học tăng cường (ví dụ: PPO).

The RL phase (PPO) is computationally expensive, requires careful hyperparameter tuning, and is prone to instability and reward hacking.
Giai đoạn Học tăng cường (PPO) tốn kém về mặt tính toán, đòi hỏi phải tinh chỉnh siêu tham số cẩn thận, và dễ bị mất ổn định cũng như xảy ra hiện tượng "reward hacking" (mô hình tìm ra lỗ hổng để tối đa hóa phần thưởng).

## 3. How DPO Works
## 3. DPO hoạt động như thế nào
The core mathematical insight of DPO is that the objective used in RLHF to learn the optimal policy can be solved perfectly without the reinforcement learning step.
Sự hiểu biết toán học cốt lõi của DPO là mục tiêu được sử dụng trong RLHF để học chính sách tối ưu có thể được giải quyết hoàn hảo mà không cần bước học tăng cường.
- DPO leverages an analytical mapping between the reward function and the optimal language model policy.
- DPO tận dụng một ánh xạ phân tích giữa hàm phần thưởng và chính sách mô hình ngôn ngữ tối ưu.
- By reparameterizing the reward model directly in terms of the language model's policy, the RL phase is bypassed entirely.
- Bằng cách tái tham số hóa mô hình phần thưởng trực tiếp theo chính sách của mô hình ngôn ngữ, giai đoạn Học tăng cường (RL) được bỏ qua hoàn toàn.
- Instead of training an RM and then doing PPO, DPO optimizes the language model directly on the human preference data using a simple binary cross-entropy loss.
- Thay vì huấn luyện một RM và sau đó chạy PPO, DPO tối ưu hóa mô hình ngôn ngữ trực tiếp trên dữ liệu sở thích của con người bằng cách sử dụng hàm mất mát cross-entropy nhị phân đơn giản.

### The Objective
### Mục tiêu
In DPO, the model increases the relative probability of the preferred response over the dispreferred response. It achieves the exact same mathematical optimum as RLHF with a KL-divergence constraint, but through direct gradient descent on the language model weights.
Trong DPO, mô hình làm tăng xác suất tương đối của câu trả lời được ưa thích so với câu trả lời không được ưa thích. Nó đạt được điểm tối ưu toán học giống hệt như RLHF với ràng buộc khoảng cách KL, nhưng thông qua việc hạ gradient (gradient descent) trực tiếp trên các trọng số của mô hình ngôn ngữ.

## 4. Key Benefits of DPO
## 4. Những lợi ích chính của DPO
- **Simplicity:** Eliminates the need for PPO and the separate reward model. The pipeline shrinks to just SFT followed by DPO.
- **Sự đơn giản:** Loại bỏ nhu cầu sử dụng PPO và mô hình phần thưởng riêng biệt. Quy trình được thu gọn chỉ còn SFT tiếp theo là DPO.
- **Stability:** Because it uses simple classification loss rather than RL, training is much more stable and hyperparameter-robust.
- **Sự ổn định:** Bởi vì nó sử dụng hàm mất mát phân loại đơn giản thay vì RL, quá trình huấn luyện ổn định hơn nhiều và mạnh mẽ với các siêu tham số.
- **Efficiency:** Reduces memory and compute requirements, as there is no need to keep multiple models (the reference model, policy model, reward model, and value model) in memory simultaneously during the RL loop.
- **Hiệu quả:** Giảm yêu cầu về bộ nhớ và tính toán, vì không cần phải giữ đồng thời nhiều mô hình (mô hình tham chiếu, mô hình chính sách, mô hình phần thưởng và mô hình giá trị) trong bộ nhớ trong vòng lặp RL.
- **Performance:** DPO matches or exceeds the performance of PPO-based RLHF in controlling sentiment, improving generation quality, and aligning with human preferences on tasks like summarization and dialogue.
- **Hiệu suất:** DPO đạt hiệu quả tương đương hoặc vượt trội so với RLHF dựa trên PPO trong việc kiểm soát cảm xúc, cải thiện chất lượng văn bản sinh ra, và điều chỉnh theo sở thích của con người trong các tác vụ như tóm tắt và hội thoại.

## 5. Conclusion
## 5. Kết luận
DPO has rapidly become a standard technique in the open-source AI community for aligning models (such as Llama and Mistral fine-tunes) because of its elegant mathematical formulation, stability, and ease of implementation compared to traditional RLHF.
DPO đã nhanh chóng trở thành một kỹ thuật tiêu chuẩn trong cộng đồng AI mã nguồn mở để tinh chỉnh các mô hình (như Llama và Mistral) nhờ vào công thức toán học tối ưu, tính ổn định và sự dễ dàng trong việc triển khai so với RLHF truyền thống.
