---
type: summary
title: "Summary: Training Language Models to Follow Instructions with Human Feedback (InstructGPT)"
description: "A summary of the InstructGPT paper detailing how Reinforcement Learning from Human Feedback (RLHF) is used to align language models."
tags: [RLHF, InstructGPT, Alignment, Human Feedback, LLM]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/1/NeurIPS-2022-training-language-models-to-follow-instructions-with-human-feedback-Paper-Conference.pdf"]
---

*Huấn luyện Mô hình Ngôn ngữ tuân theo Hướng dẫn với Phản hồi từ Con người*

## 1. Introduction / Giới thiệu

*Bài báo InstructGPT (được công bố tại NeurIPS 2022) giải quyết một vấn đề quan trọng trong các Mô hình Ngôn ngữ Lớn (LLM): sự liên kết (alignment). Các LLM tiêu chuẩn được huấn luyện để dự đoán token tiếp theo trên một kho dữ liệu văn bản internet khổng lồ, điều này có nghĩa là chúng thường tạo ra các kết quả đầu ra không trung thực, độc hại hoặc đơn giản là không hữu ích đối với ý định thực sự của người dùng. Để giải quyết vấn đề này, các tác giả giới thiệu một phương pháp để liên kết các mô hình tuân theo hướng dẫn của người dùng bằng cách sử dụng **Học tăng cường từ Phản hồi của Con người (RLHF)**.*

## 2. The Alignment Problem / Vấn đề Liên kết

*Các mô hình đã được huấn luyện trước (pre-trained) chỉ đơn giản là tự động hoàn thành văn bản. Khi được nhắc bằng một câu hỏi, chúng có thể trả lời câu hỏi đó, nhưng chúng cũng có thể tạo ra nhiều câu hỏi hơn hoặc tiếp tục lạc đề. Mục tiêu của sự liên kết là làm cho mô hình trở nên "hữu ích, trung thực và vô hại" bằng cách tinh chỉnh (fine-tune) nó để tuân theo các hướng dẫn rõ ràng được cung cấp trong lời nhắc của người dùng.*

## 3. The RLHF Methodology / Phương pháp RLHF

*Quá trình tạo ra InstructGPT bao gồm ba bước chính:*

### Step 1: Supervised Fine-Tuning (SFT) / Bước 1: Tinh chỉnh có giám sát (SFT)

*- Những người gắn nhãn (labelers) viết các lời nhắc và cung cấp các câu trả lời mong muốn, chất lượng cao.*
*- LLM đã được huấn luyện trước được tinh chỉnh trên tập dữ liệu này bằng phương pháp học có giám sát tiêu chuẩn.*
*- Điều này tạo ra mô hình SFT ban đầu, học được định dạng cơ bản để trả lời các hướng dẫn nhưng rất tốn kém để mở rộng quy mô vì các chuyên gia con người phải viết đầy đủ mọi câu trả lời.*

### Step 2: Reward Model (RM) Training / Bước 2: Huấn luyện Mô hình Phần thưởng (RM)

*- Mô hình SFT tạo ra một vài câu trả lời khác nhau cho một lời nhắc nhất định.*
*- Những người gắn nhãn xếp hạng các câu trả lời này từ tốt nhất đến kém nhất dựa trên mức độ hữu ích và an toàn.*
*- Một mô hình phần thưởng được huấn luyện trên các xếp hạng này. Mô hình phần thưởng học cách dự đoán một phần thưởng vô hướng (scalar) đại diện cho sở thích của con người đối với bất kỳ cặp lời nhắc-câu trả lời nào.*

### Step 3: Reinforcement Learning (PPO) / Bước 3: Học tăng cường (PPO)

*- Mô hình SFT được tối ưu hóa thêm so với mô hình phần thưởng bằng cách sử dụng thuật toán học tăng cường Proximal Policy Optimization (PPO).*
*- Môi trường đưa ra một lời nhắc ngẫu nhiên, mô hình tạo ra một câu trả lời, và mô hình phần thưởng chấm điểm nó. PPO cập nhật chính sách của mô hình để tối đa hóa phần thưởng này.*
*- Một hình phạt phân kỳ KL (KL-divergence penalty) được thêm vào để đảm bảo mô hình không trôi đi quá xa so với mô hình SFT ban đầu (điều này ngăn mô hình lợi dụng mô hình phần thưởng bằng cách tạo ra những từ ngữ vô nghĩa nhưng về mặt kỹ thuật lại đạt điểm cao).*

## 4. Key Results / Kết quả Chính

*- **Sở thích của Con người:** Các đánh giá viên con người cực kỳ thích các kết quả đầu ra của InstructGPT (1,3 tỷ tham số) hơn so với GPT-3 đã được huấn luyện trước lớn hơn nhiều (175 tỷ tham số), mặc dù có số lượng tham số ít hơn 100 lần.*
*- **Các Chỉ số được Cải thiện:** InstructGPT cho thấy sự cải thiện về tính trung thực và giảm việc tạo ra kết quả đầu ra độc hại so với mô hình cơ sở.*
*- **Khả năng Tổng quát hóa:** Mô hình tổng quát hóa tốt đối với các hướng dẫn nằm ngoài phân phối RLHF, nghĩa là nó có thể tuân theo các hướng dẫn mà nó chưa được huấn luyện một cách rõ ràng trong giai đoạn tinh chỉnh.*

## 5. Conclusion / Kết luận

*Bài báo này đã thiết lập RLHF làm mô hình tiêu chuẩn để liên kết các mô hình ngôn ngữ lớn, mở đường cho các mô hình trò chuyện như ChatGPT có khả năng phản hồi cao đối với ý định của con người thay vì chỉ đơn thuần là tự động hoàn thành văn bản.*
