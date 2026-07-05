---
type: summary
title: "Summary of Day 14"
description: "Tổng hợp kiến thức đo lường chất lượng AI một cách khoa học, đánh giá RAG, Multi-Agent và LLMOps."
tags: [ai, 20k, day14]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/14/Day 14.pdf"]
---

# AICB-P1 - Ngày 14: Đo lường chất lượng AI một cách khoa học

> [!NOTE] Bài học rút ra
> Evaluation (Đánh giá) là một mảng kỹ thuật (engineering discipline) đòi hỏi tính chính xác bằng toán học, không phải dựa trên cảm tính. Các thước đo cũ không còn phù hợp với AI Tạo sinh (Generative AI).

---

## 1. The Mathematics of Evaluation (Traditional vs. Generative)

### Sự sụp đổ của các thước đo truyền thống
- **Machine Learning Truyền thống**: Dựa trên Exact Match (Khớp chính xác), Precision, Recall và điểm F1.
- **Vấn đề trong GenAI**: AI có hàng ngàn cách diễn đạt khác nhau cho cùng một ý nghĩa. Áp dụng Exact Match vào văn bản sinh ra dẫn đến điểm số cực thấp dù ý nghĩa đúng 100%.

### Điểm mù của N-Gram (BLEU, ROUGE, WER)
- **BLEU & ROUGE**: Thiên lệch vào N-gram chồng chéo. Trừng phạt sự đa dạng từ vựng (Paraphrase penalty) nhưng lại "mù" trước phủ định logic (VD: câu đúng và câu mâu thuẫn trực tiếp có thể có độ khớp từ vựng cao).
- **WER (Word Error Rate)**: Đòi hỏi bản sao 1:1, lỗi sinh văn bản dài hoặc dùng từ đồng nghĩa cũng bị đánh dấu lỗi.

### Chuyển dịch sang Semantic Similarity (Tương đồng ngữ nghĩa)
- **Vector Embeddings & Cosine Similarity**: Ánh xạ câu vào không gian vector đa chiều để đo lường ý nghĩa. 
- **Cạm bẫy "Contradiction"**: Hai câu đối lập nhau (VD: "yêu thích" và "căm ghét") thường có chung context nên điểm tương đồng Cosine vẫn rất cao (>0.9). Do đó, cần đến **LLM-as-a-Judge**.
- **Đo sự đồng thuận (Cohen's Kappa - $\kappa$)**: Dùng để tính toán độ tin cậy giữa các chuyên gia chấm điểm. 

---

## 2. RAG Evaluation Algorithms (Deep Dive)

**RAGAS** là framework tiêu chuẩn giúp chia nhỏ pipeline RAG và đánh giá độc lập *Generator* và *Retriever*.

### 2.1 Đánh giá Generator
- **Faithfulness (Độ trung thực - Phát hiện ảo giác)**: Dùng Natural Language Inference (NLI) để kiểm tra xem câu trả lời có được suy ra hoàn toàn từ ngữ cảnh hay không.
  - *Bước 1*: Trích xuất các phát biểu đơn lẻ từ câu trả lời.
  - *Bước 2*: Tính xác suất Entailment (Kéo theo) giữa ngữ cảnh và từng phát biểu.
- **Answer Relevance (Độ trọng tâm)**: Giải quyết độ lan man bằng "Reverse-Engineering". Judge LLM sẽ đọc câu trả lời và đoán ngược lại câu hỏi ban đầu, sau đó tính Cosine Similarity giữa câu hỏi dự đoán và câu hỏi gốc.

### 2.2 Đánh giá Context Retrieval
- **Context Recall**: Có lấy được đủ thông tin cần thiết không?
- **Ranking Metrics**: Giải quyết hội chứng *Lost in the Middle*.
  - **MAP (Mean Average Precision)**: Đo đếm tài liệu đúng hạng cao.
  - **NDCG (Normalized Discounted Cumulative Gain)**: Phạt logarit nếu tài liệu liên quan nằm ở thứ hạng thấp.

### 2.3 Synthetic Test Data Generation
- Dùng LLM mạnh (VD: GPT-4) và thuật toán tiến hóa (Evol-Instruct) để tự tạo **Golden Dataset** (Tập dữ liệu chuẩn) thay vì dùng sức người. Các bước: Trích xuất khái niệm $\rightarrow$ Đột biến câu hỏi $\rightarrow$ Tạo câu trả lời $\rightarrow$ Sàng lọc.

---

## 3. Evaluating Multi-Agent Systems & Tool Calling

Chuyển từ pipeline phi trạng thái (stateless) sang stateful dựa trên **Markov Decision Process (MDP)**.

### Trajectory Evaluation (Đánh giá Quỹ đạo)
- Đánh giá toàn bộ hành trình Agent từ lúc nhận câu hỏi đến khi ra đáp án (Vòng lặp ReAct).
- **Step Count Efficiency**: Tỷ lệ giữa số bước tối thiểu và số bước thực tế Agent đã đi.
- **Redundant Tool Calling Rate**: Bị trừ điểm nếu gọi thừa hoặc gọi lại một công cụ với tham số y hệt.
- **Phát hiện Deadlocks**: Agent bị kẹt trong vòng lặp vô hạn do lỗi tham số.

### Tool/Function Calling Accuracy
- **Độ chính xác Lựa chọn**: Xử lý như phân loại đa lớp (Multi-Class Classification). Gọi nhầm/không gọi đúng tool.
- **Độ chính xác Payload**: Schema JSON của LLM có tuân thủ đặc tả không? (Sai kiểu dữ liệu, thiếu trường).
- **Ảo giác tham số API**: Lỗi nguy hiểm khi Agent tự "bịa" ra tham số thay vì hỏi lại người dùng.

### Conversational/Session Metrics
- **Multi-Turn Coherence**: Agent có nhớ ràng buộc ở các lượt trước không hay bị "Context Decay" (Suy giảm ngữ cảnh).
- Dùng **Dialog State Tracking (DST)** bằng Judge LLM để trích xuất trạng thái người dùng qua từng lượt hội thoại.

---

## 4. The Science of LLM-as-a-Judge & SOTA Benchmarks

### Giải phẫu Judge Prompt
Một prompt giám khảo cần phải chặt chẽ:
1. **System Persona**: Vai trò giám khảo khắt khe.
2. **Context Block**: Tách bạch User Query, Context, Agent Answer.
3. **Rubric**: Định nghĩa điểm số cụ thể rõ ràng.
4. **CoT (Chain-of-Thought)**: Ép mô hình sinh ra phần giải thích `<thought_process>` trước khi ra điểm số cuối cùng để tránh thiên kiến.

### Các Thiên kiến của LLM (LLM Biases) và Cách khắc phục
- **Vị trí (Order Bias)** $\rightarrow$ Dùng *Swap-Testing* (So sánh cả A vs B và B vs A).
- **Dài dòng (Verbosity Bias)** và **Định dạng** $\rightarrow$ Dùng *Few-Shot Calibration* với ví dụ "Vàng".
- **Tự ưu ái (Self-Preference Bias)** $\rightarrow$ Dùng *Ensembling* (Hội đồng giám khảo bỏ phiếu).

### Đánh giá cặp (Pairwise Evaluation)
Thay vì điểm tuyệt đối, hãy hỏi mô hình "A hay B tốt hơn?". Kết hợp với mô hình **Bradley-Terry** và hệ thống tính điểm **Elo** (như Chatbot Arena) để tạo bảng xếp hạng ổn định. Dùng mô hình chuyên biệt (như Prometheus 8B) cho tác vụ đánh giá thay vì Frontier Model lớn để tối ưu chi phí.

---

## 5. MLOps, Cost, and Continuous Improvement

### Tam giác Production
Khi đưa AI lên Production, kỹ sư phải cân bằng: **Accuracy** (Độ chính xác) – **Latency** (Độ trễ) – **Cost** (Chi phí).

### Các thước đo Latency
- **TTFT (Time to First Token)**: Cảm giác tốc độ tức thời. < 1.0 giây là tốt nhất.
- **TPS (Tokens Per Second)**: Tốc độ phát luồng (> 10 TPS để nhanh hơn tốc độ đọc của con người).

### Đánh giá trong CI/CD
- Tích hợp RAGAS và LLM Judge vào GitHub Actions.
- **Quality Gates**: Tự động chặn build nếu điểm giảm (Ví dụ: `Faithfulness < 0.85`).
- **Dark Launching / Shadow Testing**: Định tuyến 10% lưu lượng thật ngầm chạy qua Agent mới và so sánh (Semantic Diffing) với Agent cũ trước khi thay thế hoàn toàn.

### Failure Clustering
Thay vì "Vá Prompt" (Prompt Patching) lắt nhắt gây lỗi hồi quy, hãy gom cụm (Clustering) các phản hồi lỗi để tìm và **sửa nguyên nhân gốc rễ** từ pipeline dữ liệu.

> [!TIP] Vòng lặp cải tiến liên tục
> Evaluate $\rightarrow$ Analyze (Failure Clustering) $\rightarrow$ Improve $\rightarrow$ Augment Benchmark. Lặp lại qua mỗi sprint.
