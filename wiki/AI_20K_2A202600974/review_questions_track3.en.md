---
type: summary
title: "Câu hỏi ôn tập - Track3"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track3"
tags: [review, track3]
timestamp: 2026-07-06
sources: []
---
# Track 3 Review Questions

### Day 3 Review Questions

1. According to the lecture content, which of the following is **not** one of the 4 criteria of the Agentic Fit Framework?
   - A. Multi-step Reasoning
   - B. Tool Interaction
   - C. Single-turn Response
   - D. Long Horizon

2. In the ReAct pattern, which component represents the "observing the result of the action" step?
   - A. Thought
   - B. Action
   - C. Observation
   - D. Memory

3. What is the main advantage of Native Tool Calling compared to Text-ReAct?
   - A. Consumes fewer tokens
   - B. Forces the model to generate formatted text itself
   - C. Increases stability thanks to standard JSON schema from the API provider
   - D. Allows the agent to create new tools itself

4. What type of error occurs when an agent continuously calls a tool endlessly, unable to escape the loop?
   - A. Hallucinated Tool
   - B. Empty Observation
   - C. Timeout/Loop
   - D. Parse Error

5. To evaluate Agent quality, which method is recommended instead of just looking at the final result?
   - A. Eval-by-Trace (measuring tokens, latency, loop count)
   - B. Blind-test with users
   - C. Comparing with rule-based bots
   - D. Only checking the tool's accuracy

---

### Day 15 Review Questions

1. Which of the following techniques is **NOT** mentioned in the main content of Track 3?
   - A. GraphRAG & knowledge graphs
   - B. Fine-tuning with LoRA, QLoRA, DPO
   - C. Basic prompt engineering (few-shot, chain-of-thought)
   - D. Production evaluation systems

2. According to the lecture, Track 3 is suitable for learners with which characteristics?
   - A. Likes working with structured data and pure SQL
   - B. Interested in ReAct design, tool calling, supervisor-worker architecture
   - C. Wants to focus on image and video processing with CNN
   - D. Prioritizes no-code solutions

3. What challenge is explicitly stated when pursuing Track 3?
   - A. Light content volume, easy to absorb
   - B. The field already has clear best practices, no need to experiment
   - C. Benchmark and evaluation require a lot of effort
   - D. Does not require reading original documents (research papers)

4. What is the target role (CP3) that Track 3 aims for?
   - A. Data Analyst, Business Intelligence Developer
   - B. AI Engineer, LLM Engineer, Agent Developer
   - C. Frontend Developer, UI/UX Designer
   - D. DevOps Engineer, Cloud Architect

---

### Day 16 Review Questions

1. What main weakness of Single Agent (ReAct) does Reflexion address?
   - A. Cannot use multiple tools simultaneously.
   - B. Lacks the ability to self-evaluate and backtrack when encountering errors.
   - C. Computation cost is too high for each step.
   - D. Does not support structured output.

2. In the Reflexion architecture, which component is responsible for drawing lessons from mistakes and saving them to memory?
   - A. Actor
   - B. Evaluator
   - C. Reflector
   - D. Retry

3. What is the prominent feature of LATS (Language Agent Tree Search) compared to Reflexion?
   - A. Uses Reflection Memory to store errors.
   - B. Combines MCTS to try multiple solution branches and has the ability to undo.
   - C. Automatically records new skills into the library.
   - D. Only suitable for data reading tasks.

4. Which safety measure is recommended when deploying Single-agent in production?
   - A. Always use Multi-agent from the beginning.
   - B. No need to configure max_attempts because the agent knows when to stop.
   - C. Risk tiering, setting up human approval gates for sensitive operations.
   - D. Only use unstructured output for flexibility.

---

### Day 17 Review Questions

1. Which type of memory in an agent is managed within the LLM's context window, has fast access speed but is limited by the token budget?
   - A. Long-term (Declarative) Memory
   - B. Episodic Memory
   - C. Short-term (Working) Memory
   - D. Semantic Memory

2. In the Memory Management Flow, which step occurs immediately after storing data in the Buffer?
   - A. Persist (External Store)
   - B. Extract Key Facts
   - C. Summarize (LLM call)
   - D. Retrieve from Vector DB

3. The "Privacy-by-Design" feature in agent memory includes which of the following elements?
   - A. Store all user data indefinitely
   - B. Only allow memory access from a single user
   - C. "Right to be Forgotten" mechanism and Time-to-Live (TTL) limit
   - D. Encrypt all data using vector embeddings

4. The "Compaction" trend in agent memory (2025-2026) refers to:
   - A. Expanding the context window capacity indefinitely
   - B. Compressing sessions into summaries, decisions, and persistent notes
   - C. Creating multiple data replicas to increase reliability
   - D. Using the AGENTS.md configuration file for access control

---

### Day 18 Review Questions

1. Which enrichment technique in the OFFLINE stage uses an LLM to generate questions that a chunk can answer, and then embeds those questions along with the chunk?
   - A. Contextual Embeddings
   - B. Hypothetical Q&A
   - C. Matryoshka Representation Learning
   - D. Late Chunking

2. In the ONLINE stage, which component uses Cross-Encoders to re-rank the retrieved chunks, helping to improve accuracy with a small latency cost?
   - A. PreRAG
   - B. Retrieval
   - C. Reranking
   - D. Augmentation

3. According to RAGAS, which metric measures the faithfulness of the answer (whether it closely follows the provided content)?
   - A. Context Recall
   - B. Context Precision
   - C. Faithfulness
   - D. Answer Relevancy

4. Which limitation of embeddings is mentioned in the lecture, such as being unable to distinguish between "allowed" and "not allowed"?
   - A. Entity Swapping
   - B. Temporal Blindness
   - C. Negation Insensitivity
   - D. Numerical Blindness

5. Which chunking technique builds a recursive summary tree to answer high-level comprehensive questions?
   - A. Semantic Chunking
   - B. Hierarchical Chunking
   - C. RAPTOR
   - *C. RAPTOR*
   - D. Late Chunking

---

### Day 19 Review Questions

1. Flat RAG (Vector RAG) typically fails with which of the following types of questions?
   - A. Simple factoid questions located within a single document.
   - B. Questions requiring reasoning across multiple entities (multi-hop).
   - C. Questions about basic concept definitions.
   - D. Questions extracting information from a short paragraph.

2. What is the atomic unit of a Knowledge Graph?
   - A. Individual Nodes and Edges.
   - B. A Triple consisting of Subject - Predicate - Object.
   - C. Any Subgraph.
   - D. A complete sentence in the original text.

3. In the standard GraphRAG pipeline, which step converts the subgraph into text format to be fed into the LLM?
   - A. Seed Node Matching.
   - B. Graph Traversal.
   - C. Textualization.
   - D. Generation.
   - *D. Sinh.*

4. Through what architecture does LightRAG improve speed and cost compared to Microsoft GraphRAG?
   - A. Using Community Detection and Hierarchical Summarization.
   - B. Dual-level retrieval with embeddings for both Nodes and Edges.
   - C. Graph traversal with a maximum depth of 3.
   - D. Combining Vector DB and Graph DB via Hybrid Search mechanism.

---

### Day 20 Review Questions

1. When should you consider transitioning from a single agent to a multi-agent system?
   - A. When the task requires interaction with multiple external APIs.
   - B. When a single agent cannot achieve >80% accuracy.
   - C. When wanting to reduce the total operating cost of the system.
   - D. When a larger language model needs to be deployed.

2. Which of Anthropic's 5 workflow patterns operates by classifying the input and routing it to the most specialized handler?
   - A. Prompt Chaining
   - B. Routing
   - C. Orchestrator-Workers
   - D. Evaluator-Optimizer

3. Which architecture is typically used to implement the Supervisor Pattern in a multi-agent system?
   - A. Star Architecture
   - B. Mesh Architecture
   - C. Hub-Spoke Architecture
   - D. Tree Architecture

4. What is the main benefit of using Debate Agents?
   - A. Doubles the processing speed.
   - B. Reduces hallucination by 15% to 25%.
   - C. Reduces API costs by half.
   - D. Completely eliminates the need for a Judge agent.

5. Which of the following frameworks is described as “state machine driven” and suitable for production environments requiring strict control?
   - A. CrewAI
   - *A. CrewAI*
   - B. AutoGen
   - *B. AutoGen*
   - C. LangGraph
   - *C. LangGraph*
   - D. LangChain
   - *D. LangChain*

---

### Day 21 Review Questions

1. According to the lecture, in standard procedures, when should one switch to Fine-tuning instead of continuing with Prompt Engineering and RAG?
   - A. When new knowledge needs to be added to the model.
   - B. When Prompt Engineering and RAG have maxed out but the model still lacks specialized formatting or needs reduced latency/cost at scale.
   - C. When the number of requests is under 50k per day.
   - D. When the dataset has over 10k samples.

2. How does LoRA differ from Full Fine-tuning?
   - A. LoRA updates all parameters of the original model.
   - B. LoRA freezes the original weights and only trains two small matrices A and B (low-rank).
   - C. LoRA increases inference latency due to computing additional matrices.
   - D. LoRA requires more VRAM than Full Fine-tuning.

3. What technique combination allows QLoRA to fine-tune a 7B model on a 24GB GPU?
   - A. Only using Gradient Checkpointing and FlashAttention.
   - B. Quantizing the original model down to 4-bit (NF4) and using bf16 LoRA adapters, combined with PagedAdamW.
   - C. Reducing LoRA rank to r=1.
   - D. Compressing the entire model down to 2-bit.

4. According to the lecture, which of the following is true regarding Datasets when fine-tuning?
   - A. Sample quantity is more important than quality; 10k noisy samples are better than 500 clean ones.
   - B. Ensure the test set is not in the training set to avoid "Data contamination".
   - C. Just 100 samples are enough for any task.
   - D. The original model's test set can be reused without checking for duplicates.

---

### Day 22 Review Questions

1. In DPO, when increasing the hyperparameter β (KL penalty), what happens to the trained model?
   - A. The model becomes more free, loosely adhering to the SFT base.
   - B. The model becomes more conservative, staying closer to the reference model.
   - C. No effect on model behavior.
   - D. The model learns faster but easily overfits.

2. How does ORPO mainly differ from DPO?
   - A. ORPO requires a separate reward model, DPO does not.
   - B. ORPO is single-stage alignment, requiring no SFT stage.
   - C. ORPO uses preference pairs, DPO uses thumbs up/down labels.
   - D. ORPO is only used for math, DPO is for chatbots.

3. What improvement does GRPO (Group Relative Policy Optimization) bring over traditional PPO?
   - A. Completely eliminates the value model network by calculating the average reward of output groups.
   - B. Replaces the reward model with a smaller neural network.
   - C. Requires more VRAM but increases accuracy.
   - D. Only used for coding tasks, not for reasoning.

4. Which of the following benchmarks uses LLM-as-Judge to evaluate response quality in alignment?
   - A. MMLU
   - *A. MMLU*
   - B. GSM8K
   - *B. GSM8K*
   - C. MT-Bench
   - *C. MT-Bench*
   - D. HumanEval
   - *D. HumanEval*

---

### Day 23 Review Questions

1. When is a linear pipeline (LCEL) no longer sufficient for an agent?
   - A. When only a simple processing flow is needed, with no branching.
   - B. When the agent needs loop retries, human-in-the-loop, dynamic routing, and crash recovery.
   - C. When the number of tools is less than 5.
   - D. When checkpointing is not needed.

2. What is a reducer used for in LangGraph?
   - A. Determines which node runs next.
   - B. Merges state during updates, e.g., appending to message history.
   - C. Creates a checkpoint after each step.
   - D. Calls an external tool.

3. What does the "Time Travel" feature in LangGraph allow you to do?
   - A. Run multiple graphs in parallel at the same time.
   - B. Replay from any checkpoint for debugging or trying a different approach.
   - C. Automatically retry failed nodes.
   - D. Send a notification to the user upon completion.

4. Which function is used to pause the graph to wait for human approval?
   - A. `interrupt()`
   - *A. `interrupt()`*
   - B. `checkpoint()`
   - *B. `checkpoint()`*
   - C. `retry()`
   - *C. `retry()`*
   - D. `breakpoint()`
   - *D. `breakpoint()`*

---

### Day 24 Review Questions

1. Which metric does RAGAS use to measure the extent to which the context supports the answer (intrinsic hallucination)?
   - A. Context Recall
   - B. Answer Relevancy
   - C. Faithfulness
   - D. Context Precision

2. When using LLM-as-Judge, which bias is mitigated using the "swap-and-average" method?
   - A. Length Bias
   - B. Position Bias
   - C. Self-Enhancement Bias
   - D. Style Bias

3. In the Guardrails architecture, which layer is responsible for detecting prompt injections and checking topic scope with under 30ms latency?
   - A. L1 Input Layer
   - B. L2 LLM Layer
   - C. L3 Output Layer
   - D. L4 Audit Layer

4. Which of the following techniques detects hallucinations by sampling multiple answers with temperature > 0 and measuring consistency?
   - A. NLI (DeBERTa)
   - *A. NLI (DeBERTa)*
   - B. Semantic Entropy
   - C. SelfCheckGPT
   - *C. SelfCheckGPT*
   - D. Cohen's Kappa
   - *D. Cohen's Kappa*

---

### Day 25 Review Questions

1. When an LLM agent system encounters a 429 (Rate Limit) or 500 (Internal Server Error) from the provider, which failure mode does this belong to?
   - A. Tool/cache failure
   - B. Incorrect business action
   - C. Provider transient
   - D. Orchestration loop

2. In which state does a Circuit Breaker allow performing a probe call to check for recovery?
   - A. CLOSED
   - B. OPEN
   - C. HALF-OPEN
   - D. FAILED

3. In the fallback ladder, which step is typically performed before using a cached response?
   - A. Best model
   - B. Backup provider
   - C. Cheaper/smaller model
   - D. Static fallback message

4. When semantic cache similarity > threshold, what is the correct action?
   - A. Call LLM and store new result
   - B. Return cached result
   - C. Reset threshold
   - D. Log the error

5. How is SLI (Service Level Indicator) defined in the lecture?
   - A. External commitment to customers
   - B. Internal quality targets
   - C. Actual measured metric (e.g., P95 latency)
   - D. Allowed error budget

---

### Day 26 Review Questions

1. How is the N×M problem in LLM tool integration solved by MCP?
   - A. By requiring each LLM provider to write their own adapter.
   - B. By introducing a standard protocol, reducing the complexity from N×M to N+M.
   - C. By completely eliminating the need for external tools.
   - D. By only supporting a single LLM provider.

2. In the MCP architecture, which component is responsible for providing callable functions for the LLM to decide to use?
   - A. Resources
   - B. Prompts
   - C. Tools
   - D. Roots

3. When building an MCP Server using FastMCP, which factor is emphasized as the most important for the LLM to decide to call the correct tool?
   - A. Function name and input data type.
   - B. Clear tool description (docstring).
   - C. Number of function parameters.
   - D. Processing speed of the server.

4. To secure a remote MCP Server, which protocol is mandatory to use?
   - A. Unencrypted HTTP.
   - B. SSH with private key.
   - C. OAuth 2.0 and TLS.
   - D. Only API key authentication is needed.

5. According to Claude Code best practices, which flow should be prioritized for design before performing mutations?
   - A. Write flow for quick impact.
   - B. Read/search flow to get accurate context.
   - C. Delete flow to clean up data.
   - D. Update flow for immediate synchronization.

---

### Day 27 Review Questions

1. According to the lecture, what does the concept of "Bounded Autonomy" in HITL mean?
   - A. The agent is fully autonomous, requiring no human intervention
   - B. The agent can automatically perform any action but must log it
   - C. The agent is autonomous within safe boundaries (read/search) and must ask for permission when crossing risky boundaries
   - D. The agent is only allowed to perform pre-approved actions

2. When should an agent interrupt to ask for a human's opinion, according to the Confidence Routing principle?
   - A. When the agent's confidence score is below 50%
   - B. When the action is reversible and causes external impact
   - C. When the action is reversible, prioritize automation; if it has an external impact or lacks information, it needs review/approval
   - D. Only interrupt when the agent is unsure about the result

3. Among the 6 HITL interaction patterns, which one is used when the agent needs a human to review draft output (e.g., code PR, draft email)?
   - A. Approval
   - B. Clarification
   - C. Review Checkpoint
   - D. Escalation
   - *D. Leo thang*

4. According to HITL UX best practices, when should a human be asked in order to reduce cognitive load?
   - A. Always ask early for every action
   - B. Ask early for missing data, ask late for irreversible actions
   - C. Only ask when the action has a high risk
   - D. Ask late for all actions to avoid bothering

---

### Day 28 Review Questions

1. According to the lecture, the principle of choosing a value metric for AI pricing is based on which two factors?
   - A. API costs and personnel costs
   - B. Attribution (ability to measure results) and Autonomy (automation)
   - C. Number of users and average revenue
   - D. Model type and inference costs

2. When determining the floor price for an AI product, the minimum cost for a job includes all of the following factors, **except**:
   - A. API costs
   - B. Infra costs
   - C. Marketing costs
   - D. HITL (Human-In-The-Loop) costs

3. What is the core rule of Go-To-Market (GTM) for AI?
   - A. Create a completely new interface to impress
   - B. Don't force users to open a new tab or learn a new workflow
   - C. Prioritize the Sales-Led channel for all products
   - D. Focus on impressive demos before having evidence

4. According to the lecture, the "ARPU-CAC Dead Zone" is which ARPU range that causes difficulties because it fits neither self-serve nor sales teams?
   - A. Under $50
   - B. Over $1000
   - C. From $50 to $1000
   - D. From $1000 to $5000
