---
type: summary
title: "Summary: Attention Is All You Need"
description: "A summary of the seminal 2017 paper that introduced the Transformer architecture, replacing RNNs with self-attention mechanisms."
tags: [Transformer, Self-Attention, LLM, Deep Learning, Paper]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/1/NIPS-2017-attention-is-all-you-need-Paper.pdf"]
---

# Attention Is All You Need

## 1. Introduction
"Attention Is All You Need" is a seminal paper published in 2017 by researchers at Google. It introduced the **Transformer**, a novel neural network architecture based solely on attention mechanisms, dispensing entirely with recurrence (RNNs/LSTMs) and convolutions. This architecture significantly improved the quality of machine translation while requiring much less time to train due to its highly parallelizable nature.

## 2. The Problem with RNNs
Prior to the Transformer, the dominant sequence transduction models relied on Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) networks.
- **Sequential Computation:** RNNs process data sequentially (token by token). To compute the hidden state at step $t$, the network needs the hidden state from step $t-1$.
- **Lack of Parallelization:** This sequential dependency prevents parallelization across sequence lengths during training, making it computationally expensive and slow, especially for long sequences.
- **Long-term Dependencies:** RNNs struggle to retain information over long distances in a sequence.

## 3. The Transformer Architecture
The Transformer solves these issues by eschewing recurrence and relying entirely on an attention mechanism to draw global dependencies between inputs and outputs. The architecture follows an encoder-decoder structure:

### Scaled Dot-Product Attention
The core of the model is the "Scaled Dot-Product Attention" function. It maps queries ($Q$), keys ($K$), and values ($V$) to an output.
- The attention weights are calculated by taking the dot product of queries and keys.
- To prevent the dot products from growing too large and pushing the softmax function into regions with extremely small gradients, the dot products are scaled by $\frac{1}{\sqrt{d_k}}$ (where $d_k$ is the dimension of the keys).

### Multi-Head Attention
Instead of performing a single attention function, the Transformer linearly projects the queries, keys, and values $h$ times with different learned linear projections.
- Attention is performed in parallel on each of these projected versions, yielding $d_v$-dimensional output values.
- These are concatenated and projected again.
- Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions.

### Positional Encoding
Since the model contains no recurrence or convolution, it has no inherent sense of token order. To inject sequence order information, **positional encodings** are added to the input embeddings. The authors used sine and cosine functions of different frequencies to encode position.

### Feed-Forward Networks
Each layer in the encoder and decoder contains a fully connected, position-wise feed-forward network applied to each position separately and identically.

## 4. Key Results and Impact
- **Superior Quality:** The Transformer achieved state-of-the-art results on the WMT 2014 English-to-German and English-to-French translation tasks.
- **Training Efficiency:** It trained significantly faster than competing architectures, reaching new benchmarks in just 3.5 days on 8 GPUs.
- **Legacy:** This paper laid the groundwork for modern Large Language Models (LLMs) such as BERT, GPT, and Claude, shifting the entire field of Natural Language Processing away from RNNs toward Transformer-based foundation models.
