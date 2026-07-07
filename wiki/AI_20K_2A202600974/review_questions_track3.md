---
type: summary
title: "Câu hỏi ôn tập - Track3"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track3"
tags: [review, track3]
timestamp: 2026-07-06
sources: []
---

# Bộ câu hỏi ôn tập Track3
# Track 3 Review Questions

### Câu hỏi ôn tập Ngày 3
### Day 3 Review Questions

1. Theo nội dung bài giảng, yếu tố nào sau đây **không** thuộc 4 tiêu chí của Agentic Fit Framework?
According to the lecture content, which of the following is **not** one of the 4 criteria of the Agentic Fit Framework?
   - A. Multi-step Reasoning
   - B. Tool Interaction
   - C. Single-turn Response
   - D. Long Horizon
   **Đáp án / Answer:** C

2. Trong ReAct pattern, thành phần nào đại diện cho bước "quan sát kết quả của hành động"?
In the ReAct pattern, which component represents the "observing the result of the action" step?
   - A. Thought
   - B. Action
   - C. Observation
   - D. Memory
   **Đáp án / Answer:** C

3. Ưu điểm chính của Native Tool Calling so với Text-ReAct là gì?
What is the main advantage of Native Tool Calling compared to Text-ReAct?
   - A. Tiêu tốn ít token hơn / Consumes fewer tokens
   - B. Bắt buộc model tự sinh văn bản định dạng / Forces the model to generate formatted text itself
   - C. Tăng tính ổn định nhờ JSON schema chuẩn từ API provider / Increases stability thanks to standard JSON schema from the API provider
   - D. Cho phép agent tự tạo tool mới / Allows the agent to create new tools itself
   **Đáp án / Answer:** C

4. Loại lỗi nào xảy ra khi agent liên tục gọi một tool không hồi kết, không thoát được vòng lặp?
What type of error occurs when an agent continuously calls a tool endlessly, unable to escape the loop?
   - A. Hallucinated Tool
   - B. Empty Observation
   - C. Timeout/Loop
   - D. Parse Error
   **Đáp án / Answer:** C

5. Để đánh giá chất lượng Agent, phương pháp nào được đề xuất thay vì chỉ nhìn kết quả cuối?
To evaluate Agent quality, which method is recommended instead of just looking at the final result?
   - A. Eval-by-Trace (đo tokens, latency, loop count) / Eval-by-Trace (measuring tokens, latency, loop count)
   - B. Blind-test với người dùng / Blind-test with users
   - C. So sánh với rule-based bot / Comparing with rule-based bots
   - D. Chỉ kiểm tra độ chính xác của tool / Only checking the tool's accuracy
   **Đáp án / Answer:** A

---

### Câu hỏi ôn tập Ngày 15
### Day 15 Review Questions

1. Kỹ thuật nào sau đây **KHÔNG** được đề cập trong nội dung chính của Track 3?
Which of the following techniques is **NOT** mentioned in the main content of Track 3?
   - A. GraphRAG & knowledge graphs
   - B. Fine-tuning với LoRA, QLoRA, DPO / Fine-tuning with LoRA, QLoRA, DPO
   - C. Prompt engineering cơ bản (few-shot, chain-of-thought) / Basic prompt engineering (few-shot, chain-of-thought)
   - D. Production evaluation systems
   **Đáp án / Answer:** C

2. Theo bài giảng, Track 3 phù hợp với người học có đặc điểm nào?
According to the lecture, Track 3 is suitable for learners with which characteristics?
   - A. Thích làm việc với dữ liệu có cấu trúc và SQL thuần túy / Likes working with structured data and pure SQL
   - B. Hứng thú với thiết kế ReAct, tool calling, supervisor-worker architecture / Interested in ReAct design, tool calling, supervisor-worker architecture
   - C. Muốn tập trung vào xử lý ảnh và video với CNN / Wants to focus on image and video processing with CNN
   - D. Ưu tiên các giải pháp không cần code (no-code) / Prioritizes no-code solutions
   **Đáp án / Answer:** B

3. Thách thức nào được nêu rõ khi theo đuổi Track 3?
What challenge is explicitly stated when pursuing Track 3?
   - A. Khối lượng nội dung nhẹ, dễ tiếp thu / Light content volume, easy to absorb
   - B. Lĩnh vực đã có best practice rõ ràng, không cần thử nghiệm / The field already has clear best practices, no need to experiment
   - C. Benchmark và evaluation tốn nhiều công sức / Benchmark and evaluation require a lot of effort
   - D. Không yêu cầu đọc tài liệu gốc (research paper) / Does not require reading original documents (research papers)
   **Đáp án / Answer:** C

4. Vai trò mục tiêu (CP3) mà Track 3 hướng đến là gì?
What is the target role (CP3) that Track 3 aims for?
   - A. Data Analyst, Business Intelligence Developer
   - B. AI Engineer, LLM Engineer, Agent Developer
   - C. Frontend Developer, UI/UX Designer
   - D. DevOps Engineer, Cloud Architect
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 16
### Day 16 Review Questions

1. Điểm yếu chính nào của Single Agent (ReAct) mà Reflexion khắc phục?
What main weakness of Single Agent (ReAct) does Reflexion address?
   - A. Không thể sử dụng nhiều tool cùng lúc. / Cannot use multiple tools simultaneously.
   - B. Thiếu khả năng tự đánh giá và backtrack khi gặp lỗi. / Lacks the ability to self-evaluate and backtrack when encountering errors.
   - C. Chi phí tính toán quá cao cho mỗi bước. / Computation cost is too high for each step.
   - D. Không hỗ trợ structured output. / Does not support structured output.
   **Đáp án / Answer:** B

2. Trong kiến trúc Reflexion, thành phần nào chịu trách nhiệm rút ra bài học từ sai lầm và lưu vào bộ nhớ?
In the Reflexion architecture, which component is responsible for drawing lessons from mistakes and saving them to memory?
   - A. Actor
   - B. Evaluator
   - C. Reflector
   - D. Retry
   **Đáp án / Answer:** C

3. Đặc điểm nổi bật của LATS (Language Agent Tree Search) so với Reflexion là gì?
What is the prominent feature of LATS (Language Agent Tree Search) compared to Reflexion?
   - A. Sử dụng Reflection Memory để lưu lỗi. / Uses Reflection Memory to store errors.
   - B. Kết hợp MCTS để thử nhiều nhánh giải pháp và có khả năng undo. / Combines MCTS to try multiple solution branches and has the ability to undo.
   - C. Tự động ghi nhận kỹ năng mới vào thư viện. / Automatically records new skills into the library.
   - D. Chỉ phù hợp với các tác vụ đọc dữ liệu. / Only suitable for data reading tasks.
   **Đáp án / Answer:** B

4. Biện pháp an toàn nào được khuyến nghị khi triển khai Single-agent trong production?
Which safety measure is recommended when deploying Single-agent in production?
   - A. Luôn sử dụng Multi-agent ngay từ đầu. / Always use Multi-agent from the beginning.
   - B. Không cần cấu hình max_attempts vì agent tự biết dừng. / No need to configure max_attempts because the agent knows when to stop.
   - C. Phân cấp rủi ro, đặt human approval gate cho thao tác nhạy cảm. / Risk tiering, setting up human approval gates for sensitive operations.
   - D. Chỉ dùng unstructured output để linh hoạt. / Only use unstructured output for flexibility.
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 17
### Day 17 Review Questions

1. Loại bộ nhớ nào trong agent được quản lý trong context window của LLM, có tốc độ truy cập nhanh nhưng bị giới hạn bởi token budget?
Which type of memory in an agent is managed within the LLM's context window, has fast access speed but is limited by the token budget?
   - A. Long-term (Declarative) Memory
   - B. Episodic Memory
   - C. Short-term (Working) Memory
   - D. Semantic Memory
   **Đáp án / Answer:** C

2. Trong quy trình quản lý bộ nhớ (Memory Management Flow), bước nào diễn ra ngay sau khi lưu trữ dữ liệu trong bộ đệm (Buffer)?
In the Memory Management Flow, which step occurs immediately after storing data in the Buffer?
   - A. Persist (External Store)
   - B. Extract Key Facts
   - C. Summarize (LLM call)
   - D. Retrieve từ Vector DB / Retrieve from Vector DB
   **Đáp án / Answer:** C

3. Tính năng "Privacy-by-Design" trong bộ nhớ agent bao gồm yếu tố nào sau đây?
The "Privacy-by-Design" feature in agent memory includes which of the following elements?
   - A. Lưu trữ vô thời hạn tất cả dữ liệu người dùng / Store all user data indefinitely
   - B. Chỉ cho phép truy cập bộ nhớ từ một user duy nhất / Only allow memory access from a single user
   - C. Cơ chế "Right to be Forgotten" và giới hạn thời gian tồn tại (TTL) / "Right to be Forgotten" mechanism and Time-to-Live (TTL) limit
   - D. Mã hóa tất cả dữ liệu bằng vector embeddings / Encrypt all data using vector embeddings
   **Đáp án / Answer:** C

4. Xu hướng "Compaction" trong agent memory (2025-2026) đề cập đến việc:
The "Compaction" trend in agent memory (2025-2026) refers to:
   - A. Mở rộng không giới hạn dung lượng context window / Expanding the context window capacity indefinitely
   - B. Nén các phiên họp thành tóm tắt, quyết định và ghi chú bền vững / Compressing sessions into summaries, decisions, and persistent notes
   - C. Tạo nhiều bản sao dữ liệu để tăng độ tin cậy / Creating multiple data replicas to increase reliability
   - D. Sử dụng file cấu hình AGENTS.md để kiểm soát truy cập / Using the AGENTS.md configuration file for access control
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 18
### Day 18 Review Questions

1. Kỹ thuật enrichment nào trong giai đoạn OFFLINE sử dụng LLM để tạo ra các câu hỏi mà một chunk có thể trả lời, sau đó nhúng các câu hỏi đó cùng với chunk?
Which enrichment technique in the OFFLINE stage uses an LLM to generate questions that a chunk can answer, and then embeds those questions along with the chunk?
   - A. Contextual Embeddings
   - B. Hypothetical Q&A
   - C. Matryoshka Representation Learning
   - D. Late Chunking
   **Đáp án / Answer:** B

2. Trong giai đoạn ONLINE, thành phần nào sử dụng Cross-Encoders để sắp xếp lại các chunk đã truy xuất, giúp cải thiện độ chính xác với chi phí độ trễ nhỏ?
In the ONLINE stage, which component uses Cross-Encoders to re-rank the retrieved chunks, helping to improve accuracy with a small latency cost?
   - A. PreRAG
   - B. Retrieval
   - C. Reranking
   - D. Augmentation
   **Đáp án / Answer:** C

3. Theo RAGAS, metric nào đo lường mức độ trung thực của câu trả lời (có bám sát nội dung được cung cấp hay không)?
According to RAGAS, which metric measures the faithfulness of the answer (whether it closely follows the provided content)?
   - A. Context Recall
   - B. Context Precision
   - C. Faithfulness
   - D. Answer Relevancy
   **Đáp án / Answer:** C

4. Hạn chế nào của embedding được nhắc đến trong bài giảng, ví dụ như không phân biệt được "allowed" và "not allowed"?
Which limitation of embeddings is mentioned in the lecture, such as being unable to distinguish between "allowed" and "not allowed"?
   - A. Entity Swapping
   - B. Temporal Blindness
   - C. Negation Insensitivity
   - D. Numerical Blindness
   **Đáp án / Answer:** C

5. Kỹ thuật chunking nào xây dựng một cây tóm tắt đệ quy để trả lời các câu hỏi tổng hợp ở mức cao?
Which chunking technique builds a recursive summary tree to answer high-level comprehensive questions?
   - A. Semantic Chunking
   - B. Hierarchical Chunking
   - C. RAPTOR
   - D. Late Chunking
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 19
### Day 19 Review Questions

1. Flat RAG (Vector RAG) thường thất bại với loại câu hỏi nào dưới đây?  
Flat RAG (Vector RAG) typically fails with which of the following types of questions?
   - A. Câu hỏi factoid đơn giản nằm trong một tài liệu. / Simple factoid questions located within a single document.
   - B. Câu hỏi yêu cầu suy luận qua nhiều thực thể (multi-hop). / Questions requiring reasoning across multiple entities (multi-hop).
   - C. Câu hỏi về định nghĩa khái niệm cơ bản. / Questions about basic concept definitions.
   - D. Câu hỏi trích xuất thông tin từ một đoạn văn ngắn. / Questions extracting information from a short paragraph.
   **Đáp án / Answer:** B  

2. Đơn vị nguyên tử (atomic unit) của Knowledge Graph là gì?  
What is the atomic unit of a Knowledge Graph?
   - A. Node và Edge riêng lẻ. / Individual Nodes and Edges.
   - B. Bộ ba (Triple) gồm Chủ thể – Vị ngữ – Tân ngữ. / A Triple consisting of Subject - Predicate - Object.
   - C. Một đồ thị con (Subgraph) bất kỳ. / Any Subgraph.
   - D. Câu văn hoàn chỉnh trong văn bản gốc. / A complete sentence in the original text.
   **Đáp án / Answer:** B  

3. Trong pipeline GraphRAG tiêu chuẩn, bước nào chuyển đổi subgraph thành dạng văn bản để đưa vào LLM?  
In the standard GraphRAG pipeline, which step converts the subgraph into text format to be fed into the LLM?
   - A. Seed Node Matching.
   - B. Graph Traversal.
   - C. Textualization (Văn bản hóa). / Textualization.
   - D. Generation.
   **Đáp án / Answer:** C  

4. LightRAG cải thiện tốc độ và chi phí so với Microsoft GraphRAG nhờ kiến trúc nào?  
Through what architecture does LightRAG improve speed and cost compared to Microsoft GraphRAG?
   - A. Sử dụng Community Detection và Tóm tắt phân cấp. / Using Community Detection and Hierarchical Summarization.
   - B. Truy xuất hai cấp độ (Dual-level retrieval) với embedding cho cả Node và Edge. / Dual-level retrieval with embeddings for both Nodes and Edges.
   - C. Duyệt đồ thị với độ sâu (depth) tối đa là 3. / Graph traversal with a maximum depth of 3.
   - D. Kết hợp Vector DB và Graph DB theo cơ chế Hybrid Search. / Combining Vector DB and Graph DB via Hybrid Search mechanism.
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 20
### Day 20 Review Questions

1. Khi nào bạn nên cân nhắc chuyển từ một agent duy nhất sang multi-agent system?  
When should you consider transitioning from a single agent to a multi-agent system?
   - A. Khi nhiệm vụ cần tương tác với nhiều API bên ngoài. / When the task requires interaction with multiple external APIs.
   - B. Khi một agent đơn lẻ không đạt độ chính xác >80%. / When a single agent cannot achieve >80% accuracy.
   - C. Khi muốn giảm tổng chi phí vận hành hệ thống. / When wanting to reduce the total operating cost of the system.
   - D. Khi cần triển khai mô hình ngôn ngữ lớn hơn. / When a larger language model needs to be deployed.
   **Đáp án / Answer:** B  

2. Mô hình workflow nào trong số 5 pattern của Anthropic hoạt động bằng cách phân loại đầu vào và chuyển hướng đến handler chuyên biệt nhất?  
Which of Anthropic's 5 workflow patterns operates by classifying the input and routing it to the most specialized handler?
   - A. Prompt Chaining  
   - B. Routing  
   - C. Orchestrator-Workers  
   - D. Evaluator-Optimizer  
   **Đáp án / Answer:** B  

3. Kiến trúc nào thường được dùng để triển khai Supervisor Pattern trong multi-agent system?  
Which architecture is typically used to implement the Supervisor Pattern in a multi-agent system?
   - A. Star Architecture  
   - B. Mesh Architecture  
   - C. Hub-Spoke Architecture  
   - D. Tree Architecture  
   **Đáp án / Answer:** C  

4. Lợi ích chính của việc sử dụng Debate Agents (agents tranh luận) là gì?  
What is the main benefit of using Debate Agents?
   - A. Tăng tốc độ xử lý lên gấp đôi. / Doubles the processing speed.
   - B. Giảm ảo giác (hallucination) từ 15% đến 25%. / Reduces hallucination by 15% to 25%.
   - C. Giảm chi phí API xuống một nửa. / Reduces API costs by half.
   - D. Loại bỏ hoàn toàn nhu cầu dùng Judge agent. / Completely eliminates the need for a Judge agent.
   **Đáp án / Answer:** B  

5. Framework nào trong số sau đây được mô tả là “state machine driven” và phù hợp cho môi trường production cần kiểm soát chặt chẽ?  
Which of the following frameworks is described as “state machine driven” and suitable for production environments requiring strict control?
   - A. CrewAI  
   - B. AutoGen  
   - C. LangGraph  
   - D. LangChain  
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 21
### Day 21 Review Questions

1. Theo bài giảng, trong quy trình chuẩn, khi nào nên chuyển sang Fine-tune thay vì tiếp tục dùng Prompt Engineering và RAG?
According to the lecture, in standard procedures, when should one switch to Fine-tuning instead of continuing with Prompt Engineering and RAG?
   - A. Khi cần thêm kiến thức mới vào mô hình. / When new knowledge needs to be added to the model.
   - B. Khi Prompt Engineering và RAG đã hết sức nhưng mô hình vẫn thiếu format chuyên ngành hoặc cần giảm latency/cost ở quy mô lớn. / When Prompt Engineering and RAG have maxed out but the model still lacks specialized formatting or needs reduced latency/cost at scale.
   - C. Khi số lượng request (req) mỗi ngày dưới 50k. / When the number of requests is under 50k per day.
   - D. Khi tập dữ liệu có trên 10k mẫu. / When the dataset has over 10k samples.
   **Đáp án / Answer:** B

2. LoRA khác với Full Fine-tune ở điểm nào?
How does LoRA differ from Full Fine-tuning?
   - A. LoRA cập nhật tất cả các tham số của mô hình gốc. / LoRA updates all parameters of the original model.
   - B. LoRA đóng băng trọng số gốc và chỉ huấn luyện hai ma trận nhỏ A và B (low-rank). / LoRA freezes the original weights and only trains two small matrices A and B (low-rank).
   - C. LoRA làm tăng độ trễ suy luận (inference latency) do phải tính thêm ma trận. / LoRA increases inference latency due to computing additional matrices.
   - D. LoRA yêu cầu nhiều VRAM hơn Full Fine-tune. / LoRA requires more VRAM than Full Fine-tuning.
   **Đáp án / Answer:** B

3. QLoRA cho phép fine-tune mô hình 7B trên GPU 24GB nhờ kết hợp kỹ thuật nào?
What technique combination allows QLoRA to fine-tune a 7B model on a 24GB GPU?
   - A. Chỉ dùng Gradient Checkpointing và FlashAttention. / Only using Gradient Checkpointing and FlashAttention.
   - B. Lượng tử hóa (quantization) mô hình gốc xuống 4-bit (NF4) và dùng bộ điều chỉnh bf16 LoRA, kết hợp PagedAdamW. / Quantizing the original model down to 4-bit (NF4) and using bf16 LoRA adapters, combined with PagedAdamW.
   - C. Giảm rank của LoRA xuống r=1. / Reducing LoRA rank to r=1.
   - D. Nén toàn bộ mô hình xuống còn 2-bit. / Compressing the entire model down to 2-bit.
   **Đáp án / Answer:** B

4. Theo bài giảng, điều nào sau đây là đúng về Dataset khi fine-tune?
According to the lecture, which of the following is true regarding Datasets when fine-tuning?
   - A. Số lượng mẫu quan trọng hơn chất lượng; 10k mẫu nhiễu vẫn tốt hơn 500 mẫu sạch. / Sample quantity is more important than quality; 10k noisy samples are better than 500 clean ones.
   - B. Cần đảm bảo tập test không nằm trong tập huấn luyện để tránh “Data contamination”. / Ensure the test set is not in the training set to avoid "Data contamination".
   - C. Chỉ cần 100 mẫu là đủ cho mọi tác vụ. / Just 100 samples are enough for any task.
   - D. Có thể dùng lại tập test của mô hình gốc mà không cần kiểm tra trùng lặp. / The original model's test set can be reused without checking for duplicates.
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 22
### Day 22 Review Questions

1. Trong DPO, khi tăng hyperparameter β (KL penalty), điều gì xảy ra với mô hình sau huấn luyện?  
In DPO, when increasing the hyperparameter β (KL penalty), what happens to the trained model?
   - A. Mô hình trở nên tự do hơn, ít bám sát SFT base. / The model becomes more free, loosely adhering to the SFT base.
   - B. Mô hình bảo thủ hơn, giữ gần với reference model. / The model becomes more conservative, staying closer to the reference model.
   - C. Không ảnh hưởng đến hành vi mô hình. / No effect on model behavior.
   - D. Mô hình học nhanh hơn nhưng dễ overfit. / The model learns faster but easily overfits.
   **Đáp án / Answer:** B  

2. ORPO khác biệt chính so với DPO ở điểm nào?  
How does ORPO mainly differ from DPO?
   - A. ORPO yêu cầu reward model riêng, DPO thì không. / ORPO requires a separate reward model, DPO does not.
   - B. ORPO là single-stage alignment, không cần SFT stage. / ORPO is single-stage alignment, requiring no SFT stage.
   - C. ORPO dùng cặp preference, DPO dùng nhãn thumbs up/down. / ORPO uses preference pairs, DPO uses thumbs up/down labels.
   - D. ORPO chỉ dùng cho toán học, DPO dùng cho chatbot. / ORPO is only used for math, DPO is for chatbots.
   **Đáp án / Answer:** B  

3. GRPO (Group Relative Policy Optimization) cải tiến gì so với PPO truyền thống?  
What improvement does GRPO (Group Relative Policy Optimization) bring over traditional PPO?
   - A. Loại bỏ hoàn toàn mạng value model bằng cách tính reward trung bình của nhóm outputs. / Completely eliminates the value model network by calculating the average reward of output groups.
   - B. Thay thế reward model bằng một mạng neural nhỏ hơn. / Replaces the reward model with a smaller neural network.
   - C. Yêu cầu nhiều VRAM hơn nhưng tăng độ chính xác. / Requires more VRAM but increases accuracy.
   - D. Chỉ dùng cho tác vụ code, không dùng cho reasoning. / Only used for coding tasks, not for reasoning.
   **Đáp án / Answer:** A  

4. Benchmark nào sau đây dùng LLM-as-Judge để đánh giá chất lượng phản hồi (response quality) trong alignment?  
Which of the following benchmarks uses LLM-as-Judge to evaluate response quality in alignment?
   - A. MMLU  
   - B. GSM8K  
   - C. MT-Bench  
   - D. HumanEval  
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 23
### Day 23 Review Questions

1. Khi nào một pipeline tuyến tính (LCEL) không còn đủ cho agent?
When is a linear pipeline (LCEL) no longer sufficient for an agent?
   - A. Khi chỉ cần một luồng xử lý đơn giản, không có rẽ nhánh. / When only a simple processing flow is needed, with no branching.
   - B. Khi agent cần loop retry, human-in-the-loop, dynamic routing và crash recovery. / When the agent needs loop retries, human-in-the-loop, dynamic routing, and crash recovery.
   - C. Khi số lượng tool nhỏ hơn 5. / When the number of tools is less than 5.
   - D. Khi không cần checkpointing. / When checkpointing is not needed.
   **Đáp án / Answer:** B

2. Trong LangGraph, reducer được dùng để làm gì?
What is a reducer used for in LangGraph?
   - A. Xác định node nào chạy tiếp theo. / Determines which node runs next.
   - B. Merge state khi cập nhật, ví dụ append cho message history. / Merges state during updates, e.g., appending to message history.
   - C. Tạo checkpoint sau mỗi bước. / Creates a checkpoint after each step.
   - D. Gọi tool bên ngoài. / Calls an external tool.
   **Đáp án / Answer:** B

3. Tính năng "Time Travel" trong LangGraph cho phép làm gì?
What does the "Time Travel" feature in LangGraph allow you to do?
   - A. Chạy song song nhiều graph cùng lúc. / Run multiple graphs in parallel at the same time.
   - B. Replay lại từ một checkpoint bất kỳ để debug hoặc thử hướng đi khác. / Replay from any checkpoint for debugging or trying a different approach.
   - C. Tự động retry node bị lỗi. / Automatically retry failed nodes.
   - D. Gửi thông báo cho người dùng khi hoàn thành. / Send a notification to the user upon completion.
   **Đáp án / Answer:** B

4. Để tạm dừng graph chờ con người phê duyệt, ta sử dụng hàm nào?
Which function is used to pause the graph to wait for human approval?
   - A. `interrupt()`
   - B. `checkpoint()`
   - C. `retry()`
   - D. `breakpoint()`
   **Đáp án / Answer:** A

---

### Câu hỏi ôn tập Ngày 24
### Day 24 Review Questions

1. RAGAS sử dụng chỉ số nào để đo lường mức độ hỗ trợ của ngữ cảnh cho câu trả lời (hallucination nội tại)?
Which metric does RAGAS use to measure the extent to which the context supports the answer (intrinsic hallucination)?
   - A. Context Recall
   - B. Answer Relevancy
   - C. Faithfulness
   - D. Context Precision
   **Đáp án / Answer:** C

2. Khi sử dụng LLM-as-Judge, bias nào được khắc phục bằng phương pháp "swap-and-average"?
When using LLM-as-Judge, which bias is mitigated using the "swap-and-average" method?
   - A. Length Bias
   - B. Position Bias
   - C. Self-Enhancement Bias
   - D. Style Bias
   **Đáp án / Answer:** B

3. Trong kiến trúc Guardrails, lớp nào chịu trách nhiệm phát hiện prompt injection và kiểm tra chủ đề (topic scope) với độ trễ dưới 30ms?
In the Guardrails architecture, which layer is responsible for detecting prompt injections and checking topic scope with under 30ms latency?
   - A. L1 Input Layer
   - B. L2 LLM Layer
   - C. L3 Output Layer
   - D. L4 Audit Layer
   **Đáp án / Answer:** A

4. Kỹ thuật nào sau đây phát hiện hallucination bằng cách lấy mẫu nhiều câu trả lời với temperature > 0 và đo độ nhất quán?
Which of the following techniques detects hallucinations by sampling multiple answers with temperature > 0 and measuring consistency?
   - A. NLI (DeBERTa)
   - B. Semantic Entropy
   - C. SelfCheckGPT
   - D. Cohen's Kappa
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 25
### Day 25 Review Questions

1. Khi hệ thống LLM agent gặp lỗi 429 (Rate Limit) hoặc 500 (Internal Server Error) từ provider, đó thuộc failure mode nào?
When an LLM agent system encounters a 429 (Rate Limit) or 500 (Internal Server Error) from the provider, which failure mode does this belong to?
   - A. Tool/cache failure
   - B. Business action sai / Incorrect business action
   - C. Provider transient
   - D. Orchestration loop
   **Đáp án / Answer:** C

2. Circuit Breaker ở trạng thái nào cho phép thực hiện một probe call để kiểm tra recovery?
In which state does a Circuit Breaker allow performing a probe call to check for recovery?
   - A. CLOSED
   - B. OPEN
   - C. HALF-OPEN
   - D. FAILED
   **Đáp án / Answer:** C

3. Trong fallback ladder, bước nào thường được thực hiện trước khi dùng cached response?
In the fallback ladder, which step is typically performed before using a cached response?
   - A. Best model
   - B. Backup provider
   - C. Cheaper/smaller model
   - D. Static fallback message
   **Đáp án / Answer:** C

4. Khi semantic cache có similarity > threshold, hành động đúng là gì?
When semantic cache similarity > threshold, what is the correct action?
   - A. Gọi LLM và lưu kết quả mới / Call LLM and store new result
   - B. Trả về kết quả cached / Return cached result
   - C. Reset threshold
   - D. Ghi log lỗi / Log the error
   **Đáp án / Answer:** B

5. SLI (Service Level Indicator) được định nghĩa trong bài giảng là gì?
How is SLI (Service Level Indicator) defined in the lecture?
   - A. Cam kết bên ngoài với khách hàng / External commitment to customers
   - B. Chỉ tiêu nội bộ về chất lượng / Internal quality targets
   - C. Metric đo lường thực tế (ví dụ: P95 latency) / Actual measured metric (e.g., P95 latency)
   - D. Ngân sách lỗi cho phép / Allowed error budget
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 26
### Day 26 Review Questions

1. Vấn đề N×M trong tích hợp công cụ LLM được giải quyết như thế nào bởi MCP?
How is the N×M problem in LLM tool integration solved by MCP?
   - A. Bằng cách yêu cầu mỗi nhà cung cấp LLM viết adapter riêng. / By requiring each LLM provider to write their own adapter.
   - B. Bằng cách giới thiệu một giao thức chuẩn, giảm độ phức tạp từ N×M xuống N+M. / By introducing a standard protocol, reducing the complexity from N×M to N+M.
   - C. Bằng cách loại bỏ hoàn toàn nhu cầu sử dụng công cụ bên ngoài. / By completely eliminating the need for external tools.
   - D. Bằng cách chỉ hỗ trợ một nhà cung cấp LLM duy nhất. / By only supporting a single LLM provider.
   **Đáp án / Answer:** B

2. Trong kiến trúc MCP, thành phần nào chịu trách nhiệm cung cấp các hàm có thể gọi được (callable functions) cho LLM quyết định sử dụng?
In the MCP architecture, which component is responsible for providing callable functions for the LLM to decide to use?
   - A. Resources
   - B. Prompts
   - C. Tools
   - D. Roots
   **Đáp án / Answer:** C

3. Khi xây dựng MCP Server bằng FastMCP, yếu tố nào được nhấn mạnh là quan trọng nhất để LLM quyết định gọi tool chính xác?
When building an MCP Server using FastMCP, which factor is emphasized as the most important for the LLM to decide to call the correct tool?
   - A. Tên hàm và kiểu dữ liệu đầu vào. / Function name and input data type.
   - B. Mô tả tool (docstring) rõ ràng. / Clear tool description (docstring).
   - C. Số lượng tham số của hàm. / Number of function parameters.
   - D. Tốc độ xử lý của server. / Processing speed of the server.
   **Đáp án / Answer:** B

4. Để bảo mật MCP Server từ xa (remote), giao thức nào bắt buộc phải được sử dụng?
To secure a remote MCP Server, which protocol is mandatory to use?
   - A. HTTP không mã hóa. / Unencrypted HTTP.
   - B. SSH với private key. / SSH with private key.
   - C. OAuth 2.0 và TLS.
   - D. Chỉ cần xác thực qua API key. / Only API key authentication is needed.
   **Đáp án / Answer:** C

5. Theo best practices của Claude Code, nên ưu tiên thiết kế luồng nào trước khi thực hiện các thay đổi (mutations)?
According to Claude Code best practices, which flow should be prioritized for design before performing mutations?
   - A. Luồng ghi (write) để tác động nhanh. / Write flow for quick impact.
   - B. Luồng đọc/tìm kiếm (search/read) để lấy ngữ cảnh chính xác. / Read/search flow to get accurate context.
   - C. Luồng xóa (delete) để dọn dẹp dữ liệu. / Delete flow to clean up data.
   - D. Luồng cập nhật (update) để đồng bộ ngay lập tức. / Update flow for immediate synchronization.
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 27
### Day 27 Review Questions

1. Theo bài giảng, khái niệm "Bounded Autonomy" trong HITL có nghĩa là gì?
According to the lecture, what does the concept of "Bounded Autonomy" in HITL mean?
   - A. Agent hoàn toàn tự động, không cần sự can thiệp của con người / The agent is fully autonomous, requiring no human intervention
   - B. Agent có thể tự động thực hiện mọi hành động nhưng phải ghi log lại / The agent can automatically perform any action but must log it
   - C. Agent tự động trong các ranh giới an toàn (đọc/tìm kiếm) và phải xin phép khi vượt ranh giới rủi ro / The agent is autonomous within safe boundaries (read/search) and must ask for permission when crossing risky boundaries
   - D. Agent chỉ được thực hiện các hành động đã được phê duyệt trước / The agent is only allowed to perform pre-approved actions
   **Đáp án / Answer:** C

2. Khi nào agent nên ngắt quãng (interrupt) để hỏi ý kiến con người, theo nguyên tắc Confidence Routing?
When should an agent interrupt to ask for a human's opinion, according to the Confidence Routing principle?
   - A. Khi confidence score của agent dưới 50% / When the agent's confidence score is below 50%
   - B. Khi hành động có thể đảo ngược (reversible) và gây ảnh hưởng bên ngoài / When the action is reversible and causes external impact
   - C. Khi hành động có thể đảo ngược, ưu tiên tự động; nếu có tác động bên ngoài hoặc thiếu thông tin thì cần review/phê duyệt / When the action is reversible, prioritize automation; if it has an external impact or lacks information, it needs review/approval
   - D. Chỉ ngắt khi agent không chắc chắn về kết quả / Only interrupt when the agent is unsure about the result
   **Đáp án / Answer:** C

3. Trong 6 mẫu tương tác HITL, pattern nào được sử dụng khi agent cần con người kiểm tra bản nháp đầu ra (ví dụ: code PR, email nháp)?
Among the 6 HITL interaction patterns, which one is used when the agent needs a human to review draft output (e.g., code PR, draft email)?
   - A. Approval
   - B. Clarification
   - C. Review Checkpoint
   - D. Escalation
   **Đáp án / Answer:** C

4. Theo best practices của HITL UX, khi nào nên hỏi con người để giảm tải nhận thức?
According to HITL UX best practices, when should a human be asked in order to reduce cognitive load?
   - A. Luôn hỏi sớm cho mọi hành động / Always ask early for every action
   - B. Hỏi sớm cho dữ liệu thiếu, hỏi muộn cho hành động không thể đảo ngược / Ask early for missing data, ask late for irreversible actions
   - C. Chỉ hỏi khi hành động có rủi ro cao / Only ask when the action has a high risk
   - D. Hỏi muộn cho mọi hành động để tránh làm phiền / Ask late for all actions to avoid bothering
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 28
### Day 28 Review Questions

1. Theo bài giảng, nguyên tắc chọn value metric cho AI pricing dựa trên hai yếu tố nào?
According to the lecture, the principle of choosing a value metric for AI pricing is based on which two factors?
   - A. Chi phí API và chi phí nhân sự / API costs and personnel costs
   - B. Attribution (khả năng đo lường kết quả) và Autonomy (tự động hóa) / Attribution (ability to measure results) and Autonomy (automation)
   - C. Số lượng người dùng và doanh thu trung bình / Number of users and average revenue
   - D. Loại mô hình và chi phí suy luận / Model type and inference costs
   **Đáp án / Answer:** B

2. Khi xác định giá bán (floor price) cho sản phẩm AI, chi phí tối thiểu cho một job bao gồm tất cả các yếu tố sau, **ngoại trừ**:
When determining the floor price for an AI product, the minimum cost for a job includes all of the following factors, **except**:
   - A. API costs
   - B. Infra costs
   - C. Chi phí marketing / Marketing costs
   - D. HITL (Human-In-The-Loop) costs
   **Đáp án / Answer:** C

3. Quy tắc cốt lõi của Go-To-Market (GTM) cho AI là gì?
What is the core rule of Go-To-Market (GTM) for AI?
   - A. Tạo giao diện hoàn toàn mới để gây ấn tượng / Create a completely new interface to impress
   - B. Không bắt người dùng mở tab mới hoặc học workflow mới / Don't force users to open a new tab or learn a new workflow
   - C. Ưu tiên kênh Sales-Led cho mọi sản phẩm / Prioritize the Sales-Led channel for all products
   - D. Tập trung vào demo ấn tượng trước khi có bằng chứng / Focus on impressive demos before having evidence
   **Đáp án / Answer:** B

4. Theo bài giảng, "ARPU-CAC Dead Zone" là khoảng ARPU nào gây khó khăn vì không phù hợp với cả self-serve lẫn sales team?
According to the lecture, the "ARPU-CAC Dead Zone" is which ARPU range that causes difficulties because it fits neither self-serve nor sales teams?
   - A. Dưới $50 / Under $50
   - B. Trên $1000 / Over $1000
   - C. Từ $50 đến $1000 / From $50 to $1000
   - D. Từ $1000 đến $5000 / From $1000 to $5000
   **Đáp án / Answer:** C
