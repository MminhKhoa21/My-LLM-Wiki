---
type: summary
title: "Câu hỏi ôn tập - Track1"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track1"
tags: [review, track1]
timestamp: 2026-07-06
sources: []
---
# Track 1 Review Questions  

### Day 3 Review Questions  

1. What is the main difference between an Agent and an LLM Chatbot?  
   - A. Agents only operate based on rigid if/else rules.  
   - B. Agents are proactively goal-oriented and can use tools.  
   - C. Chatbots have more complex multi-step reasoning capabilities than Agents.  
   - D. Agents do not have long-term memory capabilities.  

2. In the Agentic Fit Framework, which criterion indicates that the problem requires interaction with the external environment?  
   - A. Multi-step Reasoning  
   - B. Tool Interaction  
   - C. Dynamic Decision  
   - D. Long Horizon  

3. Which component in the Agent architecture is responsible for deciding to call a tool and processing its output?  
   - A. Perception  
   - B. Reasoning  
   - C. Action  
   - D. Memory  

4. What is the biggest benefit of the ReAct pattern compared to other methods?  
   - A. Reduces operational costs.  
   - B. Increases response speed.  
   - C. Ability to debug and intervene in the reasoning process.  
   - D. Completely eliminates parse errors.  

---

### Day 4 Review Questions  

1. According to the RTCF model, which component is considered the top priority in a good prompt?  
   - A. Role  
   - B. Task  
   - C. Context  
   - D. Format  

2. Which technique is recommended to force the LLM to output a stable format, typically using 2-5 examples focusing on edge-cases?  
   - A. Zero‑shot  
     *A. Zero‑shot*  
   - B. Chain‑of‑Thought (CoT)  
     *B. Chain‑of‑Thought (CoT)*  
   - C. Few‑shot  
     *C. Few‑shot*  
   - D. Dynamic Prompting  
     *D. Dynamic Prompting*  

3. In the Tool Calling architecture, what data does the LLM return in the second step (after receiving user input) so the app can execute the tool?  
   - A. Raw text response  
     *A. Raw text response*  
   - B. JSON `tool_calls`  
     *B. JSON `tool_calls`*  
   - C. An SQL command  
   - D. A dictionary containing `tool_outputs`  

4. When encountering an error during tool execution, what is the recommended error handling strategy?  
   - A. Stop the entire agent and notify the user of the error  
   - B. Send the raw error message back to the LLM so it can fix the error itself  
   - C. Ignore the error and continue executing another tool  
   - D. Recall the tool with default parameters  

5. In LangGraph, which mechanism is used to store and update `messages` throughout the graph?  
   - A. Global variable  
   - B. Append‑only Reducer  
     *B. Append‑only Reducer*  
   - C. Conditional Edge  
     *C. Conditional Edge*  
   - D. Router Node  
     *D. Router Node*  

---

### Day 15 Review Questions  

1. What is the main goal of Track 1 (Phase 2)?  
   - A. Learn to code and deploy AI models from scratch  
   - B. Shift from "building AI" to making AI product decisions (strategy, ROI, governance)  
   - C. Focus on improving the accuracy of deep learning algorithms  
   - D. Build management skills for AI technical teams  

2. Who is the most suitable person for this Track?  
   - A. Engineers who only like to code and don't care about the business case  
   - B. People who like writing Problem Statements, distinguishing Need vs. Feature, and are comfortable with ambiguity  
   - C. Legal experts who understand the AI Act but don't build products  
   - D. Data scientists specializing in optimizing models without caring about UX  

3. Which capability is NOT built in this Track?  
   - A. Problem framing and defining success metrics  
   - B. Designing trust/UX for AI products  
   - C. Programming model deployment and fine-tuning  
   - D. ROI & business case, pilot plan & measuring adoption  

4. What is the biggest challenge when following this Track?  
   - A. Lack of data to train AI models  
   - B. Having to live with ambiguity, making decisions when data is insufficient, and persuading stakeholders  
   - C. No job opportunities because the market doesn't need AI PMs  
   - D. Technical results (accuracy, F1) are immediately visible  

---

### Day 16 Review Questions  

1. According to the lecture, what factor determines whether customers will switch from an old product to a new AI product?  
   - A. The AI product is completely free  
   - B. The value received from the new product is 10 times greater than the old product  
   - C. The AI product has a more beautiful interface  
   - D. The AI product is heavily advertised  

2. In the Job-to-be-Done (JTBD) Framework, how is a “Job Story” structured?  
   - A. As a [persona], I want [feature] to achieve [goal]  
   - B. When [context], I want to [motivation/job], so I can [expected outcome]  
   - C. If [condition], then [action] will lead to [result]  
   - D. From [current state] to [desired state] through [solution]  

3. When using the Job Map (JTBD Lite Map), what is the main purpose of identifying “Pain Points”?  
   - A. Listing all technical errors of the current product  
   - B. Finding out which steps users perform slowly, with errors, taking effort, or lacking reliability  
   - C. Measuring customer satisfaction  
   - D. Identifying direct competitors  

4. According to the lecture, what is the main difference when building a Product Hypothesis in the AI era?  
   - A. Need to focus on technological features rather than user needs  
   - B. Need to validate assumptions about shifting user expectations and how work gets done  
   - C. Just relying on historical usage data of the old product  
   - D. Skipping validation steps because AI always provides superior value  

5. Which of the following is an example of an “AI Shock” mentioned in the lecture?  
   - A. A company increases revenue by adding a chatbot feature to their product  
   - B. Chegg is disrupted when users switch from paying for solutions to asking AI for free and getting instant answers  
   - C. A successful AI startup by maintaining the old business model  
   - D. Loyal users to the old product despite AI providing similar value  

---

### Day 17 Review Questions  

1. According to the lecture, "Leap of Faith Assumptions" include four main types of risks. Which risk relates to the question "Can users figure out how to use the product?"  
   - A. Value risk  
   - B. Usability risk  
   - C. Feasibility risk  
   - D. Business viability risk  

2. Which type of prototype is most suitable to test the accuracy of workflows and see if users recognize the main features?  
   - A. High-fidelity prototype  
     *A. High-fidelity prototype*  
   - B. Clickable prototype  
     *B. Clickable prototype*  
   - C. Low-fidelity prototype  
     *C. Low-fidelity prototype*  
   - D. Mockup  
     *D. Mockup*  

3. In the Wizard of Oz MVP example, the two founders manually transcribed meetings under the name "Fred" to test what hypothesis?  
   - A. Users will trust AI to create lesson plans  
   - B. People are willing to pay for an AI transcription service  
   - C. It's possible to build an automated transcription app  
   - D. A static web interface is enough to attract customers  

4. In the Lab Assignment, the "Three Cheaper Test Alternatives" step requires brainstorming different ways to test. Which of the following is NOT a valid artifact for this step?  
   - A. Sketch  
     *A. Sketch*  
   - B. Storyboard  
     *B. Storyboard*  
   - C. A completely developed software feature  
   - D. Wizard of Oz setup  
     *D. Wizard of Oz setup*  

---

### Day 18 Review Questions  

1. The **Trust Calibration** formula includes Expectation, Explainability, and Control. Which element helps users understand why the AI produced a specific result?  
   - A. Expectation  
   - B. Explainability  
   - C. Control  
   - D. Automation  

2. In the **Augmentation vs Automation** decision, when should AI act automatically?  
   - A. Low certainty, high cost of mistakes  
   - B. High certainty, low cost of mistakes  
   - C. Medium certainty, significant impact  
   - D. Always automate to save time  

3. When the AI encounters an error or is uncertain, which of the following handling methods is recommended?  
   - A. Hide results to avoid confusion  
   - B. Display results with confidence levels and provide an escape hatch  
   - C. Force users to accept the results  
   - D. Do not collect feedback from errors  

4. "Users clicking the **like/dislike** button or rating the product" belongs to which type of feedback?  
   - A. User Feedback (Implicit)  
   - B. User Feedback (Explicit)  
   - C. System Feedback (Explicit)  
   - D. System Feedback (Implicit)  

---

### Day 19 Review Questions  

1. **Why is Retention considered more important than Acquisition in a growth strategy?**  
   - A. Because the Customer Acquisition Cost (CAC) is always lower than retention costs.  
   - B. Because Retention helps evaluate whether the product truly delivers core value.  
   - C. Because PR and advertising activities cannot increase the number of users.  
   - D. Because Retention is the only metric affecting long-term revenue.  

2. **What does the concept of "Natural Frequency" refer to in the context of Retention?**  
   - A. The frequency the product sends reminder notifications to users.  
   - B. The frequency users naturally encounter the problem the product solves (daily, weekly, monthly...).  
   - C. The frequency the product team conducts A/B tests.  
   - D. The frequency users share the product on social media.  

3. **According to the Hook Model (Habit Loop), which element creates internal motivation for users to return the next time?**  
   - A. External Trigger, such as notifications.  
   - B. Variable Reward, creating curiosity and excitement.  
   - C. Action, being simple and easy to perform.  
   - D. Investment - users putting effort into the product.  

4. **Which metric is commonly used to measure user Stickiness?**  
   - A. DAU/MAU  
     *A. DAU/MAU*  
   - B. CAC/LTV  
     *B. CAC/LTV*  
   - C. D7 Retention  
     *C. D7 Retention*  
   - D. Time to Value (TTV)  
     *D. Time to Value (TTV)*  

5. **When a product's D1 Retention reaches only around 10%, where does the main cause usually lie?**  
   - A. Unattractive UI, needing button color changes.  
   - B. Core Value not properly solving the users' needs.  
   - C. Communication campaigns not strong enough to attract the right audience.  
   - D. Notification frequency not high enough.  

---

### Day 20 Review Questions  

1. According to the lecture, what is the exact definition of "Core Action"?  
   - A. The action of logging into the application.  
   - B. A specific action proving the user has received value (e.g., completing a lesson).  
   - C. Homepage visits.  
   - D. Number of times the application is opened.  

2. When determining the Retention metric, what is the most important thing?  
   - A. Choosing a fixed 7-day cycle.  
   - B. It must match the natural frequency of the user's problem.  
   - C. Always using DAU.  
   - D. Only measuring after 30 days.  

3. In the Hook Model (Nir Eyal), the "Variable Reward" step is divided into three types. Which one is NOT one of those three?  
   - A. Tribe (social)  
   - B. Hunt (resources)  
   - C. Self (mastery)  
   - D. Profit  

4. What is the "North Star Metric" in the Measurement Ladder?  
   - A. Monthly revenue measurement metric.  
   - B. The leading indicator reflecting the creation of core value.  
   - C. Total registered users.  
   - D. Average time spent on the app.  

---

### Day 21 Review Questions  

1. In an AI product, how does the role of the Product Manager (PM) change compared to a traditional product?  
   - A. PM still focuses on Usage Flow and Conversion Rate as before.  
   - B. PM shifts to managing Agent Success Rate and Quality Distributions.  
   - C. PM is only responsible for the technical side of the model.  
   - D. PM hands over all evaluation tasks to the Data Science team.  

2. Which grading system is considered the "gold standard" to calibrate other grading systems?  
   - A. Code-based grader  
     *A. Code-based grader*  
   - B. Model-based grader (LLM as Judge)  
     *B. Model-based grader (LLM as Judge)*  
   - C. Human grader  
     *C. Human grader*  
   - D. Automatic metric grader  
     *D. Automatic metric grader*  

3. According to the AI Evals lifecycle, when should the "Vibe Check" phase be performed?  
   - A. After releasing the product to the market.  
   - B. During the build phase, before deploy.  
   - C. Before writing the PRD, at the prototype stage.  
   - D. Only when there's a critical error from users.  

4. What content does an AI-native PRD need to add that traditional PRDs usually lack?  
   - A. Detailed UI description.  
   - B. Evaluation Rubric and Golden Outputs.  
   - C. Gantt chart for the development roadmap.  
   - D. Marketing plan for the product.  

5. When designing a Scenario Dataset, which tool should a PM use to ensure realistic coverage?  
   - A. Have LLMs generate 50 random prompts.  
   - B. User Input Grid with dimensions WHO, WHAT, HOW, CONTEXT, RISK.  
   - C. Only use cases from real users.  
   - D. Take all data from the model's training set.  

---

### Day 22 Review Questions  

1. Why are Automated Evals needed instead of Manual Review?  
   - A. Manual review is always more accurate  
   - B. Automated evals cannot scale  
   - C. Manual review cannot scale when the volume of traces reaches 100k+  
   - D. Automated evals do not need calibration  

2. Which evaluation layer is priority number 1 and always enabled in the eval system?  
   - A. LLM-as-Judge  
     *A. LLM-as-Judge*  
   - B. Code-based Evals  
     *B. Code-based Evals*  
   - C. Human Review  
     *C. Human Review*  
   - D. Online Monitoring  
     *D. Online Monitoring*  

3. When should LLM-as-Judge be used instead of Code-based Evals?  
   - A. When criteria can be verified by rules, regex, or schema  
   - B. When deterministic and fast evaluation is needed  
   - C. When criteria depend on context and language nuances  
   - D. When purposefully sampling suspicious cases is needed  

4. In the Eval Lifecycle (bringing AI to production), which step acts as a Release Gate to block errors before deployment?  
   - A. Vibe Check (10-30 cases)  
     *A. Vibe Check (10-30 cases)*  
   - B. Offline Evals (100-1000 cases)  
     *B. Offline Evals (100-1000 cases)*  
   - C. Online Monitoring (production)  
     *C. Online Monitoring (production)*  
   - D. Human Review (fallback)  
     *D. Human Review (fallback)*  

5. Which metric is the North Star Metric for Agents?  
   - A. P95 latency  
     *A. P95 latency*  
   - B. Cost per request  
     *B. Cost per request*  
   - C. Agent Success Rate (aggregated from task correctness, schema pass rate, etc.)  
   - D. User feedback count  
     *D. User feedback count*  

---

### Day 23 Review Questions  

1. In the RAGAS framework, which metric measures "hallucination" by checking whether the answer is supported by the context?  
   - A. Context Precision  
     *A. Context Precision*  
   - B. Answer Relevancy  
     *B. Answer Relevancy*  
   - C. Faithfulness  
     *C. Faithfulness*  
   - D. Context Recall  
     *D. Context Recall*  

2. When using an LLM as a judge (LLM-as-Judge), which bias occurs when the LLM tends to choose the first or last option in a list?  
   - A. Length Bias  
     *A. Length Bias*  
   - B. Self-Enhancement Bias  
     *B. Self-Enhancement Bias*  
   - C. Style Bias  
     *C. Style Bias*  
   - D. Position Bias  
     *D. Position Bias*  

3. In the 4-layer Guardrails architecture, which layer is responsible for blocking PII (Personally Identifiable Information) using Regex or Presidio?  
   - A. L2 – LLM Layer  
     *A. L2 – LLM Layer*  
   - B. L4 – Audit Layer  
     *B. L4 – Audit Layer*  
   - C. L1 – Input Layer  
     *C. L1 – Input Layer*  
   - D. L3 – Output Layer  
     *D. L3 – Output Layer*  

4. Which method uses a Natural Language Inference (NLI) model to detect contradictions between the answer and context, thereby identifying hallucinations?  
   - A. SelfCheckGPT  
     *A. SelfCheckGPT*  
   - B. Semantic Similarity  
     *B. Semantic Similarity*  
   - C. NLI-based Detection  
     *C. NLI-based Detection*  
   - D. RAGAS Answer Relevancy  
     *D. RAGAS Answer Relevancy*  

5. Which metric in RAGAS is reference-free (no ground truth needed) and can be used directly in a production environment?  
   - A. Context Recall  
     *A. Context Recall*  
   - B. Exact Match  
     *B. Exact Match*  
   - C. Faithfulness  
     *C. Faithfulness*  
   - D. BLEU  
     *D. BLEU*  

---

### Day 24 Review Questions  

1. According to the lecture, which of the following definitions best describes "Safe AI"?  
   - A. An AI system with high accuracy that never makes mistakes.  
   - B. An AI system placed in an appropriate context, with guardrails and human accountability when incidents occur.  
   - C. An AI system capable of self-learning and improvement without humans.  
   - D. An AI system that complies with all current legal regulations.  

2. What phenomenon does the state of “Sycophancy” in AI refer to?  
   - A. AI makes up false information but is very confident.  
   - B. AI always agrees with the user even when the user is wrong.  
   - C. AI discloses other users' personal information.  
   - D. AI refuses to answer all sensitive questions.  

3. When an AI system gives a wrong answer due to insufficient grounding in the system message, which layer in the System Map does this error belong to?  
   - A. UX (User Experience)  
   - B. Safety System  
   - C. Model  
   - D. System Message & Grounding  

4. In the Harm Map Framework, what does the “Scale” factor assess?  
   - A. The severity of the harm (from low to critical).  
   - B. The number of people or groups affected.  
   - C. The probability of harm occurring.  
   - D. The frequency of the harm repeating once it has occurred.  

---

### Day 25 Review Questions  

1. Which element in the RICE Framework is evaluated on a scale from 0.25 (very small) to 3 (very large)?  
   - A. Reach  
     *A. Reach*  
   - B. Impact  
     *B. Impact*  
   - C. Confidence  
     *C. Confidence*  
   - D. Effort  
     *D. Effort*  

2. According to the Now/Next/Later method, how is the level of detail for the "NEXT" section (3-6 months) described?  
   - A. High detail, low risk  
   - B. Medium detail, medium risk  
   - C. Low detail, high risk  
   - D. No specific description  

3. In OKRs, which type of Key Result is "predictive user behavior"?  
   - A. Lagging  
     *A. Lagging*  
   - B. Leading  
     *B. Leading*  
   - C. Quality  
     *C. Quality*  
   - D. Output  
     *D. Output*  

4. For an AI startup, what is typically the "critical path" that determines the launch date?  
   - A. User interface development  
   - B. AI model optimization  
   - C. Data pipeline and legal compliance  
   - D. Marketing campaign  

---

### Day 26 Review Questions  

1. According to the lecture, what field are current VC investment trends focusing on?  
   - A. General E-commerce  
   - B. AI-Native Service Companies, AI + Hardware, AI + Deeptech, Software for Agents  
     *B. AI-Native Service Companies, AI + Hardware, AI + Deeptech, Software for Agents*  
   - C. Traditional Edtech  
   - D. Non-AI startups  

2. Which of the following is one of the keys to successful fundraising?  
   - A. Focusing only on tech ("tech-first") without caring about customers  
   - B. A reliable and committed founding team  
   - C. Products labeled "AI" even if they don't solve the core problem  
   - D. Unclear financial plans  

3. What is the most effective method for finding suitable investors?  
   - A. Mass cold emailing  
   - B. Introductions through connections (referrals)  
   - C. Posting job openings on LinkedIn  
   - D. Buying email lists from Crunchbase  

4. In the lab, the "Market Positioning Memo" step requires estimating what parameters to solve the "Unclear financials" issue?  
   - A. Number of employees and offices  
   - B. Unit Economics, Cash Needs, and KPIs  
   - C. Number of competitors  
   - D. Marketing and PR costs  

5. Before meeting with investors, what should be researched first?  
   - A. Personal hobbies of each partner  
   - B. Typical ticket size and the fund's current investment portfolio  
   - C. The fund's logo colors  
   - D. The fund CEO's birth date  

---

### Day 27 Review Questions  

1. In the 4-quadrant stakeholder management model, which group has the **Strategy: Persuade, mitigate risks early, address concerns before they ask**?  
   - A. Champions  
   - B. Blockers  
   - C. Supporters  
   - D. Bystanders  

2. In the RACI matrix, which member must be **only one person per task** and holds the ultimate decision-making responsibility?  
   - A. Responsible  
   - B. Accountable  
   - C. Consulted  
   - D. Informed  

3. What does the **"Conclusion first"** principle require when communicating with stakeholders?  
   - A. Provide all data first, then conclude  
   - B. Start with the conclusion, then provide reasons and data  
   - C. Only present the conclusion when asked  
   - D. Focus on technical details first  

4. What factor did Project Aristotle identify as the **most important** for an effective AI team?  
   - A. Hybrid team structure (Hub-and-Spoke)  
   - B. L3 Capability (AI Builder)  
   - C. Psychological Safety  
   - D. Applying Agentic SDLC  

---

### Day 28 Review Questions  

1. Which architectural layer in a real-world AI system is responsible for defining the ODD (Operational Design Domain) and safety monitoring?  
   - A. Data / Sensor  
   - B. Perception  
   - C. Decision / Policy  
   - D. Ops / Safety  

2. According to lessons from ADAS/Autonomous Driving systems, which of the following is true about End-to-End models?  
   - A. E2E models can completely replace other architectural layers  
   - B. E2E models still need an independent safety shell and a pre-defined ODD  
   - C. E2E models do not need training data from rare situations  
   - D. E2E models only apply to autonomous vehicles, not used for robots  

3. What is the main goal when deploying AI for CCTV systems?  
   - A. Applying large models to every frame to increase accuracy  
   - B. Reducing the number of clips that humans need to review  
   - C. Completely eliminating processing on edge devices  
   - D. Completely replacing humans in monitoring  

4. In Humanoid Robot architecture, which of the following is an important lesson learned?  
   - A. Robot data is cheaper than web data  
   - B. Sim-to-real gap can be ignored thanks to perfect simulation  
   - C. Robot data is more expensive than web data and needs domain randomization to reduce the sim-to-real gap  
   - D. Safety guards (e-stop, torque limits) must depend on the policy to ensure consistency  

---
