---
type: summary
title: "Summary: Training Language Models to Follow Instructions with Human Feedback (InstructGPT)"
description: "A summary of the InstructGPT paper detailing how Reinforcement Learning from Human Feedback (RLHF) is used to align language models."
tags: [RLHF, InstructGPT, Alignment, Human Feedback, LLM]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/1/NeurIPS-2022-training-language-models-to-follow-instructions-with-human-feedback-Paper-Conference.pdf"]
---

# Training Language Models to Follow Instructions with Human Feedback
*Huấn luyện Mô hình Ngôn ngữ tuân theo Hướng dẫn với Phản hồi từ Con người*

## 1. Introduction / Giới thiệu
The InstructGPT paper (published at NeurIPS 2022) addresses a critical issue in Large Language Models: alignment. Standard LLMs are trained to predict the next token on a massive corpus of internet text, which means they often generate outputs that are untruthful, toxic, or simply unhelpful to the user's actual intent. To solve this, the authors introduce a method to align models to follow user instructions using **Reinforcement Learning from Human Feedback (RLHF)**.

*Bài báo InstructGPT (được công bố tại NeurIPS 2022) giải quyết một vấn đề quan trọng trong các Mô hình Ngôn ngữ Lớn (LLM): sự liên kết (alignment). Các LLM tiêu chuẩn được huấn luyện để dự đoán token tiếp theo trên một kho dữ liệu văn bản internet khổng lồ, điều này có nghĩa là chúng thường tạo ra các kết quả đầu ra không trung thực, độc hại hoặc đơn giản là không hữu ích đối với ý định thực sự của người dùng. Để giải quyết vấn đề này, các tác giả giới thiệu một phương pháp để liên kết các mô hình tuân theo hướng dẫn của người dùng bằng cách sử dụng **Học tăng cường từ Phản hồi của Con người (RLHF)**.*

## 2. The Alignment Problem / Vấn đề Liên kết
Pre-trained models simply autocomplete text. When prompted with a question, they might answer it, but they might also generate more questions or continue a tangent. The goal of alignment is to make the model "helpful, honest, and harmless" by fine-tuning it to follow the explicit instructions provided in user prompts.

*Các mô hình đã được huấn luyện trước (pre-trained) chỉ đơn giản là tự động hoàn thành văn bản. Khi được nhắc bằng một câu hỏi, chúng có thể trả lời câu hỏi đó, nhưng chúng cũng có thể tạo ra nhiều câu hỏi hơn hoặc tiếp tục lạc đề. Mục tiêu của sự liên kết là làm cho mô hình trở nên "hữu ích, trung thực và vô hại" bằng cách tinh chỉnh (fine-tune) nó để tuân theo các hướng dẫn rõ ràng được cung cấp trong lời nhắc của người dùng.*

## 3. The RLHF Methodology / Phương pháp RLHF
The process of creating InstructGPT involves three main steps:

*Quá trình tạo ra InstructGPT bao gồm ba bước chính:*

### Step 1: Supervised Fine-Tuning (SFT) / Bước 1: Tinh chỉnh có giám sát (SFT)
- Human labelers write prompts and provide the desired, high-quality responses.
- The pre-trained LLM is fine-tuned on this dataset using standard supervised learning.
- This creates the initial SFT model, which learns the basic format of answering instructions but is expensive to scale since human experts must write every full response.

*- Những người gắn nhãn (labelers) viết các lời nhắc và cung cấp các câu trả lời mong muốn, chất lượng cao.*
*- LLM đã được huấn luyện trước được tinh chỉnh trên tập dữ liệu này bằng phương pháp học có giám sát tiêu chuẩn.*
*- Điều này tạo ra mô hình SFT ban đầu, học được định dạng cơ bản để trả lời các hướng dẫn nhưng rất tốn kém để mở rộng quy mô vì các chuyên gia con người phải viết đầy đủ mọi câu trả lời.*

### Step 2: Reward Model (RM) Training / Bước 2: Huấn luyện Mô hình Phần thưởng (RM)
- The SFT model generates several different responses for a given prompt.
- Human labelers rank these responses from best to worst based on helpfulness and safety.
- A reward model is trained on these rankings. The reward model learns to predict a scalar reward representing human preference for any given prompt-response pair.

*- Mô hình SFT tạo ra một vài câu trả lời khác nhau cho một lời nhắc nhất định.*
*- Những người gắn nhãn xếp hạng các câu trả lời này từ tốt nhất đến kém nhất dựa trên mức độ hữu ích và an toàn.*
*- Một mô hình phần thưởng được huấn luyện trên các xếp hạng này. Mô hình phần thưởng học cách dự đoán một phần thưởng vô hướng (scalar) đại diện cho sở thích của con người đối với bất kỳ cặp lời nhắc-câu trả lời nào.*

### Step 3: Reinforcement Learning (PPO) / Bước 3: Học tăng cường (PPO)
- The SFT model is further optimized against the reward model using the Proximal Policy Optimization (PPO) reinforcement learning algorithm.
- The environment presents a random prompt, the model generates a response, and the reward model scores it. PPO updates the model's policy to maximize this reward.
- A KL-divergence penalty is added to ensure the model doesn't drift too far from the original SFT model (which prevents the model from exploiting the reward model by generating gibberish that technically scores high).

*- Mô hình SFT được tối ưu hóa thêm so với mô hình phần thưởng bằng cách sử dụng thuật toán học tăng cường Proximal Policy Optimization (PPO).*
*- Môi trường đưa ra một lời nhắc ngẫu nhiên, mô hình tạo ra một câu trả lời, và mô hình phần thưởng chấm điểm nó. PPO cập nhật chính sách của mô hình để tối đa hóa phần thưởng này.*
*- Một hình phạt phân kỳ KL (KL-divergence penalty) được thêm vào để đảm bảo mô hình không trôi đi quá xa so với mô hình SFT ban đầu (điều này ngăn mô hình lợi dụng mô hình phần thưởng bằng cách tạo ra những từ ngữ vô nghĩa nhưng về mặt kỹ thuật lại đạt điểm cao).*

## 4. Key Results / Kết quả Chính
- **Human Preference:** Human evaluators overwhelmingly preferred the outputs of InstructGPT (1.3B parameters) over a much larger pre-trained GPT-3 (175B parameters), despite having 100x fewer parameters.
- **Improved Metrics:** InstructGPT showed improvements in truthfulness and reductions in toxic output generation compared to the base model.
- **Generalization:** The model generalized well to instructions outside the RLHF distribution, meaning it could follow instructions it hadn't explicitly been trained on during the fine-tuning phase.

*- **Sở thích của Con người:** Các đánh giá viên con người cực kỳ thích các kết quả đầu ra của InstructGPT (1,3 tỷ tham số) hơn so với GPT-3 đã được huấn luyện trước lớn hơn nhiều (175 tỷ tham số), mặc dù có số lượng tham số ít hơn 100 lần.*
*- **Các Chỉ số được Cải thiện:** InstructGPT cho thấy sự cải thiện về tính trung thực và giảm việc tạo ra kết quả đầu ra độc hại so với mô hình cơ sở.*
*- **Khả năng Tổng quát hóa:** Mô hình tổng quát hóa tốt đối với các hướng dẫn nằm ngoài phân phối RLHF, nghĩa là nó có thể tuân theo các hướng dẫn mà nó chưa được huấn luyện một cách rõ ràng trong giai đoạn tinh chỉnh.*

## 5. Conclusion / Kết luận
This paper established RLHF as the standard paradigm for aligning large language models, paving the way for conversational models like ChatGPT that are highly responsive to human intent rather than merely autocompleting text.

*Bài báo này đã thiết lập RLHF làm mô hình tiêu chuẩn để liên kết các mô hình ngôn ngữ lớn, mở đường cho các mô hình trò chuyện như ChatGPT có khả năng phản hồi cao đối với ý định của con người thay vì chỉ đơn thuần là tự động hoàn thành văn bản.*
