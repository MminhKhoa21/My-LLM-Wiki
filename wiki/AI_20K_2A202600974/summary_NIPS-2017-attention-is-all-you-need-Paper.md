---
type: summary
title: "Summary: Attention Is All You Need"
description: "A summary of the seminal 2017 paper that introduced the Transformer architecture, replacing RNNs with self-attention mechanisms."
tags: [Transformer, Self-Attention, LLM, Deep Learning, Paper]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/1/NIPS-2017-attention-is-all-you-need-Paper.pdf"]
---

# Attention Is All You Need
*Attention Is All You Need (Chỉ cần Cơ chế Chú ý)*

## 1. Introduction / Giới thiệu
"Attention Is All You Need" is a seminal paper published in 2017 by researchers at Google. It introduced the **Transformer**, a novel neural network architecture based solely on attention mechanisms, dispensing entirely with recurrence (RNNs/LSTMs) and convolutions. This architecture significantly improved the quality of machine translation while requiring much less time to train due to its highly parallelizable nature.

*"Attention Is All You Need" là một bài báo có ảnh hưởng lớn được xuất bản vào năm 2017 bởi các nhà nghiên cứu tại Google. Bài báo giới thiệu **Transformer**, một kiến trúc mạng nơ-ron mới dựa hoàn toàn trên các cơ chế chú ý (attention mechanisms), loại bỏ hoàn toàn tính hồi quy (RNNs/LSTMs) và tích chập (convolutions). Kiến trúc này cải thiện đáng kể chất lượng dịch máy trong khi đòi hỏi ít thời gian huấn luyện hơn nhiều nhờ vào bản chất có thể song song hóa cao của nó.*

## 2. The Problem with RNNs / Vấn đề với các RNN
Prior to the Transformer, the dominant sequence transduction models relied on Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks.
- **Sequential Computation:** RNNs process data sequentially (token by token). To compute the hidden state at step $t$, the network needs the hidden state from step $t-1$.
- **Lack of Parallelization:** This sequential dependency prevents parallelization across sequence lengths during training, making it computationally expensive and slow, especially for long sequences.
- **Long-term Dependencies:** RNNs struggle to retain information over long distances in a sequence.

*Trước khi có Transformer, các mô hình chuyển đổi chuỗi phổ biến thường dựa vào Mạng Nơ-ron Hồi quy (RNNs) và mạng Bộ nhớ Ngắn-Dài hạn (LSTM).*
*- **Tính toán tuần tự:** Các RNN xử lý dữ liệu theo cách tuần tự (từng token một). Để tính toán trạng thái ẩn tại bước $t$, mạng cần trạng thái ẩn từ bước $t-1$.*
*- **Thiếu sự song song hóa:** Sự phụ thuộc tuần tự này ngăn cản việc song song hóa trên độ dài chuỗi trong quá trình huấn luyện, làm cho nó trở nên tốn kém về mặt tính toán và chậm trễ, đặc biệt đối với các chuỗi dài.*
*- **Phụ thuộc dài hạn:** Các RNN gặp khó khăn trong việc duy trì thông tin trong khoảng cách dài trong một chuỗi.*

## 3. The Transformer Architecture / Kiến trúc Transformer
The Transformer solves these issues by eschewing recurrence and relying entirely on an attention mechanism to draw global dependencies between inputs and outputs. The architecture follows an encoder-decoder structure:

*Transformer giải quyết các vấn đề này bằng cách tránh dùng tính hồi quy và dựa hoàn toàn vào một cơ chế chú ý để vẽ ra các sự phụ thuộc toàn cục giữa đầu vào và đầu ra. Kiến trúc này tuân theo cấu trúc bộ mã hóa - bộ giải mã (encoder-decoder):*

### Scaled Dot-Product Attention / Cơ chế Chú ý Tích vô hướng được thu nhỏ
The core of the model is the "Scaled Dot-Product Attention" function. It maps queries ($Q$), keys ($K$), and values ($V$) to an output.
- The attention weights are calculated by taking the dot product of queries and keys.
- To prevent the dot products from growing too large and pushing the softmax function into regions with extremely small gradients, the dot products are scaled by $\frac{1}{\sqrt{d_k}}$ (where $d_k$ is the dimension of the keys).

*Cốt lõi của mô hình là hàm "Cơ chế Chú ý Tích vô hướng được thu nhỏ". Nó ánh xạ các truy vấn ($Q$), khóa ($K$), và giá trị ($V$) tới một đầu ra.*
*- Các trọng số chú ý được tính toán bằng cách lấy tích vô hướng của các truy vấn và các khóa.*
*- Để ngăn các tích vô hướng này trở nên quá lớn và đẩy hàm softmax vào các vùng có độ dốc (gradients) cực nhỏ, các tích vô hướng này được thu nhỏ bằng cách nhân với $\frac{1}{\sqrt{d_k}}$ (trong đó $d_k$ là số chiều của các khóa).*

### Multi-Head Attention / Cơ chế Chú ý Đa đầu (Multi-Head Attention)
Instead of performing a single attention function, the Transformer linearly projects the queries, keys, and values $h$ times with different learned linear projections.
- Attention is performed in parallel on each of these projected versions, yielding $d_v$-dimensional output values.
- These are concatenated and projected again.
- Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions.

*Thay vì thực hiện một hàm chú ý duy nhất, Transformer chiếu tuyến tính các truy vấn, khóa và giá trị $h$ lần với các phép chiếu tuyến tính được học khác nhau.*
*- Việc chú ý được thực hiện song song trên mỗi phiên bản được chiếu này, mang lại các giá trị đầu ra có số chiều $d_v$.*
*- Sau đó chúng được nối lại với nhau và chiếu thêm một lần nữa.*
*- Cơ chế chú ý đa đầu cho phép mô hình cùng lúc tập trung vào thông tin từ nhiều không gian biểu diễn khác nhau tại các vị trí khác nhau.*

### Positional Encoding / Mã hóa Vị trí
Since the model contains no recurrence or convolution, it has no inherent sense of token order. To inject sequence order information, **positional encodings** are added to the input embeddings. The authors used sine and cosine functions of different frequencies to encode position.

*Do mô hình không chứa tính hồi quy hay tính tích chập, nó không có ý thức bẩm sinh về thứ tự token. Để đưa thông tin thứ tự chuỗi vào, **các mã hóa vị trí (positional encodings)** được thêm vào các nhúng đầu vào. Các tác giả đã sử dụng các hàm sin và cos của nhiều tần số khác nhau để mã hóa vị trí.*

### Feed-Forward Networks / Mạng Truyền thẳng
Each layer in the encoder and decoder contains a fully connected, position-wise feed-forward network applied to each position separately and identically.

*Mỗi lớp trong bộ mã hóa và bộ giải mã chứa một mạng truyền thẳng kết nối đầy đủ (fully connected), áp dụng cho từng vị trí một cách riêng biệt và giống hệt nhau.*

## 4. Key Results and Impact / Các Kết quả Chính và Tác động
- **Superior Quality:** The Transformer achieved state-of-the-art results on the WMT 2014 English-to-German and English-to-French translation tasks.
- **Training Efficiency:** It trained significantly faster than competing architectures, reaching new benchmarks in just 3.5 days on 8 GPUs.
- **Legacy:** This paper laid the groundwork for modern Large Language Models (LLMs) such as BERT, GPT, and Claude, shifting the entire field of Natural Language Processing away from RNNs toward Transformer-based foundation models.

*- **Chất lượng Vượt trội:** Transformer đạt được kết quả tốt nhất (state-of-the-art) trên các tác vụ dịch tiếng Anh sang tiếng Đức và tiếng Anh sang tiếng Pháp của WMT 2014.*
*- **Hiệu quả Huấn luyện:** Mô hình này huấn luyện nhanh hơn đáng kể so với các kiến trúc cạnh tranh, đạt các tiêu chuẩn mới chỉ trong 3,5 ngày trên 8 GPU.*
*- **Di sản:** Bài báo này đã đặt nền móng cho các Mô hình Ngôn ngữ Lớn (LLMs) hiện đại như BERT, GPT và Claude, dịch chuyển toàn bộ lĩnh vực Xử lý Ngôn ngữ Tự nhiên khỏi RNN hướng tới các mô hình nền tảng dựa trên Transformer.*
