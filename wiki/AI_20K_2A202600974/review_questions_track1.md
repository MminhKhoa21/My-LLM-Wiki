---
type: summary
title: "Câu hỏi ôn tập - Track1"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track1"
tags: [review, track1]
timestamp: 2026-07-06
sources: []
---

# Bộ câu hỏi ôn tập Track1
# Track 1 Review Questions

### Câu hỏi ôn tập Ngày 3
### Day 3 Review Questions
1. Điểm khác biệt chính giữa Agent và LLM Chatbot là gì?
   What is the main difference between an Agent and an LLM Chatbot?
   - A. Agent chỉ hoạt động dựa trên luật if/else cứng.
     A. Agents only operate based on rigid if/else rules.
   - B. Agent chủ động định hướng theo mục tiêu và có thể sử dụng tools.
     B. Agents are proactively goal-oriented and can use tools.
   - C. Chatbot có khả năng suy luận nhiều bước phức tạp hơn Agent.
     C. Chatbots have more complex multi-step reasoning capabilities than Agents.
   - D. Agent không có khả năng ghi nhớ dài hạn.
     D. Agents do not have long-term memory capabilities.
   **Đáp án / Answer:** B

2. Trong Agentic Fit Framework, tiêu chí nào cho thấy bài toán cần sự tương tác với môi trường bên ngoài?
   In the Agentic Fit Framework, which criterion indicates that the problem requires interaction with the external environment?
   - A. Multi-step Reasoning
   - B. Tool Interaction
   - C. Dynamic Decision
   - D. Long Horizon
   **Đáp án / Answer:** B

3. Thành phần nào trong kiến trúc Agent chịu trách nhiệm quyết định gọi tool và xử lý đầu ra?
   Which component in the Agent architecture is responsible for deciding to call a tool and processing its output?
   - A. Perception
   - B. Reasoning
   - C. Action
   - D. Memory
   **Đáp án / Answer:** C

4. Lợi ích lớn nhất của ReAct pattern so với các phương pháp khác là gì?
   What is the biggest benefit of the ReAct pattern compared to other methods?
   - A. Giảm chi phí vận hành.
     A. Reduces operational costs.
   - B. Tăng tốc độ phản hồi.
     B. Increases response speed.
   - C. Khả năng debug và can thiệp vào quá trình suy luận.
     C. Ability to debug and intervene in the reasoning process.
   - D. Loại bỏ hoàn toàn lỗi parse.
     D. Completely eliminates parse errors.
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 4
### Day 4 Review Questions
1. Theo mô hình RTCF, thành phần nào được coi là ưu tiên hàng đầu trong một prompt tốt?
   According to the RTCF model, which component is considered the top priority in a good prompt?
   - A. Role (Vai trò)
     A. Role
   - B. Task (Nhiệm vụ)
     B. Task
   - C. Context (Bối cảnh)
     C. Context
   - D. Format (Định dạng)
     D. Format
   **Đáp án / Answer:** B

2. Kỹ thuật nào được khuyên dùng để ép LLM đưa ra output format ổn định, thường dùng 2-5 ví dụ tập trung vào edge‑cases?
   Which technique is recommended to force the LLM to output a stable format, typically using 2-5 examples focusing on edge-cases?
   - A. Zero‑shot
   - B. Chain‑of‑Thought (CoT)
   - C. Few‑shot
   - D. Dynamic Prompting
   **Đáp án / Answer:** C

3. Trong kiến trúc Tool Calling, bước thứ hai (sau khi nhận user input) LLM trả về dữ liệu gì để app có thể thực thi tool?
   In the Tool Calling architecture, what data does the LLM return in the second step (after receiving user input) so the app can execute the tool?
   - A. Raw text response
   - B. JSON `tool_calls`
   - C. Một câu lệnh SQL
     C. An SQL command
   - D. Một dictionary chứa `tool_outputs`
     D. A dictionary containing `tool_outputs`
   **Đáp án / Answer:** B

4. Khi gặp lỗi trong quá trình thực thi tool, chiến lược xử lý lỗi được đề xuất là gì?
   When encountering an error during tool execution, what is the recommended error handling strategy?
   - A. Dừng toàn bộ agent và thông báo lỗi cho user
     A. Stop the entire agent and notify the user of the error
   - B. Gửi raw error message lại cho LLM để nó tự sửa lỗi
     B. Send the raw error message back to the LLM so it can fix the error itself
   - C. Bỏ qua lỗi và tiếp tục thực thi tool khác
     C. Ignore the error and continue executing another tool
   - D. Gọi lại tool với tham số mặc định
     D. Recall the tool with default parameters
   **Đáp án / Answer:** B

5. Trong LangGraph, cơ chế nào được dùng để lưu trữ và cập nhật `messages` xuyên suốt đồ thị?
   In LangGraph, which mechanism is used to store and update `messages` throughout the graph?
   - A. Global variable
   - B. Append‑only Reducer
   - C. Conditional Edge
   - D. Router Node
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 15
### Day 15 Review Questions
1. Mục tiêu chính của Track 1 (Phase 2) là gì?
   What is the main goal of Track 1 (Phase 2)?
   - A. Học cách code và triển khai mô hình AI từ đầu
     A. Learn to code and deploy AI models from scratch
   - B. Chuyển từ việc "build AI" sang ra quyết định sản phẩm AI (chiến lược, ROI, governance)
     B. Shift from "building AI" to making AI product decisions (strategy, ROI, governance)
   - C. Tập trung vào cải thiện độ chính xác của thuật toán deep learning
     C. Focus on improving the accuracy of deep learning algorithms
   - D. Xây dựng kỹ năng quản lý đội ngũ kỹ thuật AI
     D. Build management skills for AI technical teams
   **Đáp án / Answer:** B

2. Ai là người phù hợp nhất với Track này?
   Who is the most suitable person for this Track?
   - A. Kỹ sư chỉ thích code và không quan tâm đến business case
     A. Engineers who only like to code and don't care about the business case
   - B. Người thích viết Problem Statement, phân biệt Need vs Feature, và thoải mái với sự mơ hồ
     B. People who like writing Problem Statements, distinguishing Need vs. Feature, and are comfortable with ambiguity
   - C. Chuyên gia luật am hiểu AI Act nhưng không làm sản phẩm
     C. Legal experts who understand the AI Act but don't build products
   - D. Data scientist chuyên tối ưu mô hình mà không cần quan tâm đến UX
     D. Data scientists specializing in optimizing models without caring about UX
   **Đáp án / Answer:** B

3. Năng lực nào KHÔNG được xây dựng trong Track này?
   Which capability is NOT built in this Track?
   - A. Problem framing và định nghĩa success metric
     A. Problem framing and defining success metrics
   - B. Thiết kế trust/UX cho sản phẩm AI
     B. Designing trust/UX for AI products
   - C. Lập trình model deployment và fine-tuning
     C. Programming model deployment and fine-tuning
   - D. ROI & business case, pilot plan & đo lường adoption
     D. ROI & business case, pilot plan & measuring adoption
   **Đáp án / Answer:** C

4. Thách thức lớn nhất khi theo Track này là gì?
   What is the biggest challenge when following this Track?
   - A. Thiếu dữ liệu để huấn luyện mô hình AI
     A. Lack of data to train AI models
   - B. Phải sống với sự mơ hồ, ra quyết định khi dữ liệu chưa đủ, và thuyết phục stakeholder
     B. Having to live with ambiguity, making decisions when data is insufficient, and persuading stakeholders
   - C. Không có cơ hội việc làm vì thị trường không cần AI PM
     C. No job opportunities because the market doesn't need AI PMs
   - D. Kết quả đo bằng kỹ thuật (accuracy, F1) nên dễ thấy ngay
     D. Technical results (accuracy, F1) are immediately visible
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 16
### Day 16 Review Questions

1. Theo nội dung bài giảng, yếu tố nào quyết định khách hàng sẽ chuyển từ sản phẩm cũ sang sản phẩm AI mới?
   According to the lecture, what factor determines whether customers will switch from an old product to a new AI product?
   - A. Sản phẩm AI miễn phí hoàn toàn
     A. The AI product is completely free
   - B. Giá trị nhận được từ sản phẩm mới lớn hơn gấp 10 lần so với sản phẩm cũ
     B. The value received from the new product is 10 times greater than the old product
   - C. Sản phẩm AI có giao diện đẹp hơn
     C. The AI product has a more beautiful interface
   - D. Sản phẩm AI được quảng cáo nhiều
     D. The AI product is heavily advertised
   **Đáp án / Answer:** B

2. Trong Job-to-be-Done (JTBD) Framework, “Job Story” được viết theo cấu trúc nào?
   In the Job-to-be-Done (JTBD) Framework, how is a “Job Story” structured?
   - A. Với vai trò [persona], tôi muốn [tính năng] để đạt [mục tiêu]
     A. As a [persona], I want [feature] to achieve [goal]
   - B. Khi [bối cảnh], tôi muốn [động lực/công việc], để tôi có thể [kết quả mong đợi]
     B. When [context], I want to [motivation/job], so I can [expected outcome]
   - C. Nếu [điều kiện], thì [hành động] sẽ dẫn đến [kết quả]
     C. If [condition], then [action] will lead to [result]
   - D. Từ [trạng thái hiện tại] đến [trạng thái mong muốn] nhờ [giải pháp]
     D. From [current state] to [desired state] through [solution]
   **Đáp án / Answer:** B

3. Khi sử dụng Job Map (JTBD Lite Map), mục đích chính của việc xác định “Pain Points” là gì?
   When using the Job Map (JTBD Lite Map), what is the main purpose of identifying “Pain Points”?
   - A. Liệt kê tất cả lỗi kỹ thuật của sản phẩm hiện tại
     A. Listing all technical errors of the current product
   - B. Tìm ra bước nào người dùng thực hiện chậm, sai sót, tốn công sức, hoặc thiếu tin cậy
     B. Finding out which steps users perform slowly, with errors, taking effort, or lacking reliability
   - C. Đo lường mức độ hài lòng của khách hàng
     C. Measuring customer satisfaction
   - D. Xác định đối thủ cạnh tranh trực tiếp
     D. Identifying direct competitors
   **Đáp án / Answer:** B

4. Theo bài giảng, sự khác biệt chính khi xây dựng Product Hypothesis trong thời đại AI là gì?
   According to the lecture, what is the main difference when building a Product Hypothesis in the AI era?
   - A. Cần tập trung vào tính năng công nghệ hơn là nhu cầu người dùng
     A. Need to focus on technological features rather than user needs
   - B. Cần kiểm chứng giả định về sự thay đổi kỳ vọng của người dùng và cách thức hoàn thành công việc
     B. Need to validate assumptions about shifting user expectations and how work gets done
   - C. Chỉ cần dựa trên dữ liệu lịch sử sử dụng sản phẩm cũ
     C. Just relying on historical usage data of the old product
   - D. Bỏ qua các bước kiểm chứng vì AI luôn mang lại giá trị vượt trội
     D. Skipping validation steps because AI always provides superior value
   **Đáp án / Answer:** B

5. Trường hợp nào dưới đây là ví dụ về “AI Shock” được đề cập trong bài giảng?
   Which of the following is an example of an “AI Shock” mentioned in the lecture?
   - A. Một công ty tăng doanh thu nhờ thêm tính năng chatbot vào sản phẩm
     A. A company increases revenue by adding a chatbot feature to their product
   - B. Chegg bị gián đoạn khi người dùng chuyển từ trả tiền lời giải sang hỏi AI miễn phí và nhận câu trả lời tức thì
     B. Chegg is disrupted when users switch from paying for solutions to asking AI for free and getting instant answers
   - C. Một startup AI thành công nhờ giữ nguyên mô hình kinh doanh cũ
     C. A successful AI startup by maintaining the old business model
   - D. Người dùng trung thành với sản phẩm cũ dù AI cung cấp giá trị tương tự
     D. Loyal users to the old product despite AI providing similar value
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 17
### Day 17 Review Questions
1. Theo bài giảng, "Leap of Faith Assumptions" bao gồm bốn loại rủi ro chính. Loại rủi ro nào liên quan đến câu hỏi "Người dùng có thể tìm ra cách sử dụng sản phẩm không?"
   According to the lecture, "Leap of Faith Assumptions" include four main types of risks. Which risk relates to the question "Can users figure out how to use the product?"
   - A. Value risk
   - B. Usability risk
   - C. Feasibility risk
   - D. Business viability risk
   **Đáp án / Answer:** B

2. Loại prototype nào phù hợp nhất để kiểm tra tính chính xác của quy trình làm việc và xem người dùng có nhận ra các tính năng chính hay không?
   Which type of prototype is most suitable to test the accuracy of workflows and see if users recognize the main features?
   - A. High-fidelity prototype
   - B. Clickable prototype
   - C. Low-fidelity prototype
   - D. Mockup
   **Đáp án / Answer:** C

3. Trong ví dụ về Wizard of Oz MVP, hai người sáng lập đã thủ công ghi chép cuộc họp dưới danh nghĩa "Fred" để kiểm tra giả thuyết gì?
   In the Wizard of Oz MVP example, the two founders manually transcribed meetings under the name "Fred" to test what hypothesis?
   - A. Người dùng sẽ tin tưởng AI tạo kế hoạch bài giảng
     A. Users will trust AI to create lesson plans
   - B. Mọi người sẵn sàng trả tiền cho dịch vụ ghi chú AI
     B. People are willing to pay for an AI transcription service
   - C. Có thể xây dựng một ứng dụng ghi chú tự động
     C. It's possible to build an automated transcription app
   - D. Giao diện web tĩnh có đủ để thu hút khách hàng
     D. A static web interface is enough to attract customers
   **Đáp án / Answer:** B

4. Trong Lab Assignment, bước "Three Cheaper Test Alternatives" yêu cầu brainstorm các cách kiểm tra khác nhau. Điều nào sau đây KHÔNG phải là một dạng artifact hợp lệ cho bước này?
   In the Lab Assignment, the "Three Cheaper Test Alternatives" step requires brainstorming different ways to test. Which of the following is NOT a valid artifact for this step?
   - A. Sketch
   - B. Storyboard
   - C. Một tính năng phần mềm hoàn chỉnh
     C. A completely developed software feature
   - D. Wizard of Oz setup
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 18
### Day 18 Review Questions
1. Công thức **Trust Calibration** bao gồm Expectation, Explainability và Control. Yếu tố nào giúp người dùng hiểu tại sao AI đưa ra một kết quả cụ thể?
   The **Trust Calibration** formula includes Expectation, Explainability, and Control. Which element helps users understand why the AI produced a specific result?
   - A. Expectation
   - B. Explainability
   - C. Control
   - D. Automation
   **Đáp án / Answer:** B

2. Trong quyết định **Augmentation vs Automation**, khi nào AI nên tự động thực hiện hành động (Act)?
   In the **Augmentation vs Automation** decision, when should AI act automatically?
   - A. Độ chắc chắn thấp, chi phí sai lầm cao
     A. Low certainty, high cost of mistakes
   - B. Độ chắc chắn cao, chi phí sai lầm thấp
     B. High certainty, low cost of mistakes
   - C. Độ chắc chắn trung bình, tác động đáng kể
     C. Medium certainty, significant impact
   - D. Luôn luôn tự động để tiết kiệm thời gian
     D. Always automate to save time
   **Đáp án / Answer:** B

3. Khi AI gặp lỗi hoặc không chắc chắn, cách xử lý nào sau đây được khuyến khích?
   When the AI encounters an error or is uncertain, which of the following handling methods is recommended?
   - A. Ẩn kết quả để tránh gây nhầm lẫn
     A. Hide results to avoid confusion
   - B. Hiển thị kết quả với mức độ tin cậy và cung cấp lối thoát
     B. Display results with confidence levels and provide an escape hatch
   - C. Bắt buộc người dùng chấp nhận kết quả
     C. Force users to accept the results
   - D. Không thu thập phản hồi từ lỗi
     D. Do not collect feedback from errors
   **Đáp án / Answer:** B

4. "Người dùng nhấn nút **thích/không thích** hoặc đánh giá sản phẩm" thuộc loại phản hồi nào?
   "Users clicking the **like/dislike** button or rating the product" belongs to which type of feedback?
   - A. User Feedback (Implicit)
   - B. User Feedback (Explicit)
   - C. System Feedback (Explicit)
   - D. System Feedback (Implicit)
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 19
### Day 19 Review Questions

1. **Tại sao Retention lại được coi là quan trọng hơn Acquisition trong chiến lược tăng trưởng?**
   **Why is Retention considered more important than Acquisition in a growth strategy?**
   - A. Vì chi phí thu hút người dùng mới (CAC) luôn thấp hơn chi phí giữ chân.
     A. Because the Customer Acquisition Cost (CAC) is always lower than retention costs.
   - B. Vì Retention giúp đánh giá liệu sản phẩm có thực sự mang lại giá trị cốt lõi hay không.
     B. Because Retention helps evaluate whether the product truly delivers core value.
   - C. Vì các hoạt động PR và quảng cáo không thể làm tăng số lượng người dùng.
     C. Because PR and advertising activities cannot increase the number of users.
   - D. Vì Retention là mét duy nhất ảnh hưởng đến doanh thu dài hạn.
     D. Because Retention is the only metric affecting long-term revenue.
   **Đáp án / Answer:** B

2. **Khái niệm "Natural Frequency" trong bối cảnh Retention chỉ điều gì?**
   **What does the concept of "Natural Frequency" refer to in the context of Retention?**
   - A. Tần suất sản phẩm gửi thông báo nhắc nhở cho người dùng.
     A. The frequency the product sends reminder notifications to users.
   - B. Tần suất người dùng tự nhiên gặp vấn đề mà sản phẩm giải quyết (hàng ngày, tuần, tháng...).
     B. The frequency users naturally encounter the problem the product solves (daily, weekly, monthly...).
   - C. Tần suất đội ngũ sản phẩm thực hiện các thử nghiệm A/B.
     C. The frequency the product team conducts A/B tests.
   - D. Tần suất người dùng chia sẻ sản phẩm lên mạng xã hội.
     D. The frequency users share the product on social media.
   **Đáp án / Answer:** B

3. **Theo mô hình Hook (Habit Loop), yếu tố nào đóng vai trò tạo ra động lực nội tại cho người dùng quay lại lần tiếp theo?**
   **According to the Hook Model (Habit Loop), which element creates internal motivation for users to return the next time?**
   - A. External Trigger (Kích hoạt bên ngoài) như thông báo.
     A. External Trigger, such as notifications.
   - B. Variable Reward (Phần thưởng biến đổi) tạo cảm giác tò tự mài và hứng thú.
     B. Variable Reward, creating curiosity and excitement.
   - C. Action (Hành động) đơn giản và dễ thực hiện.
     C. Action, being simple and easy to perform.
   - D. Investment (Đầu tư) – người dùng bỏ công sức vào sản phẩm.
     D. Investment - users putting effort into the product.
   **Đáp án / Answer:** B

4. **Chỉ số nào thường được dùng để đo lường mức độ gắn bó (Stickiness) của người dùng?**
   **Which metric is commonly used to measure user Stickiness?**
   - A. DAU/MAU
   - B. CAC/LTV
   - C. D7 Retention
   - D. Time to Value (TTV)
   **Đáp án / Answer:** A

5. **Khi D1 Retention của sản phẩm chỉ đạt khoảng 10%, nguyên nhân chủ yếu thường nằm ở đâu?**
   **When a product's D1 Retention reaches only around 10%, where does the main cause usually lie?**
   - A. Giao diện người dùng chưa đẹp, cần thay đổi màu sắc nút bấm.
     A. Unattractive UI, needing button color changes.
   - B. Core Value (giá trị cốt lõi) chưa giải quyết đúng nhu cầu của người dùng.
     B. Core Value not properly solving the users' needs.
   - C. Chiến dịch truyền thông chưa đủ mạnh để thu hút đúng đối tượng.
     C. Communication campaigns not strong enough to attract the right audience.
   - D. Tần suất gửi thông báo (notification) chưa đủ dày.
     D. Notification frequency not high enough.
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 20
### Day 20 Review Questions

1. Theo bài giảng, đâu là định nghĩa chính xác về "Core Action"?  
   According to the lecture, what is the exact definition of "Core Action"?
   - A. Hành động đăng nhập vào ứng dụng.  
     A. The action of logging into the application.
   - B. Hành động cụ thể chứng tỏ người dùng đã nhận được giá trị (ví dụ: hoàn thành một bài học).  
     B. A specific action proving the user has received value (e.g., completing a lesson).
   - C. Lượt truy cập trang chủ.  
     C. Homepage visits.
   - D. Số lần mở ứng dụng.  
     D. Number of times the application is opened.
   **Đáp án / Answer:** B

2. Khi xác định chỉ số Retention, điều quan trọng nhất là gì?  
   When determining the Retention metric, what is the most important thing?
   - A. Chọn chu kỳ cố định là 7 ngày.  
     A. Choosing a fixed 7-day cycle.
   - B. Phải phù hợp với tần suất tự nhiên của vấn đề người dùng.  
     B. It must match the natural frequency of the user's problem.
   - C. Luôn sử dụng DAU.  
     C. Always using DAU.
   - D. Chỉ đo lường sau 30 ngày.  
     D. Only measuring after 30 days.
   **Đáp án / Answer:** B

3. Trong Hook Model (Nir Eyal), bước "Variable Reward" được chia thành ba loại. Đâu không phải là một trong ba loại đó?  
   In the Hook Model (Nir Eyal), the "Variable Reward" step is divided into three types. Which one is NOT one of those three?
   - A. Tribe (xã hội)
     A. Tribe (social)
   - B. Hunt (tài nguyên)
     B. Hunt (resources)
   - C. Self (sự thành thạo)
     C. Self (mastery)
   - D. Profit (lợi nhuận)
     D. Profit
   **Đáp án / Answer:** D

4. "North Star Metric" trong Measurement Ladder là gì?  
   What is the "North Star Metric" in the Measurement Ladder?
   - A. Chỉ số đo lường doanh thu hàng tháng.  
     A. Monthly revenue measurement metric.
   - B. Chỉ số hàng đầu phản ánh việc tạo ra giá trị cốt lõi.  
     B. The leading indicator reflecting the creation of core value.
   - C. Tổng số người dùng đăng ký.  
     C. Total registered users.
   - D. Thời gian trung bình trên ứng dụng.  
     D. Average time spent on the app.
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 21
### Day 21 Review Questions

1. Trong sản phẩm AI, vai trò của Product Manager (PM) thay đổi như thế nào so với sản phẩm truyền thống?  
   In an AI product, how does the role of the Product Manager (PM) change compared to a traditional product?
   - A. PM vẫn tập trung vào Usage Flow và Conversion Rate như trước.  
     A. PM still focuses on Usage Flow and Conversion Rate as before.
   - B. PM chuyển sang quản lý Agent Success Rate và Quality Distributions.  
     B. PM shifts to managing Agent Success Rate and Quality Distributions.
   - C. PM chỉ chịu trách nhiệm về mặt kỹ thuật của mô hình.  
     C. PM is only responsible for the technical side of the model.
   - D. PM giao toàn bộ việc đánh giá cho đội ngũ Data Science.  
     D. PM hands over all evaluation tasks to the Data Science team.
   **Đáp án / Answer:** B

2. Bộ chấm điểm nào được coi là "chuẩn vàng" để hiệu chỉnh các bộ chấm khác?  
   Which grading system is considered the "gold standard" to calibrate other grading systems?
   - A. Code-based grader  
   - B. Model-based grader (LLM as Judge)  
   - C. Human grader  
   - D. Automatic metric grader  
   **Đáp án / Answer:** C

3. Theo vòng đời AI Evals, giai đoạn "Vibe Check" nên được thực hiện vào thời điểm nào?  
   According to the AI Evals lifecycle, when should the "Vibe Check" phase be performed?
   - A. Sau khi phát hành sản phẩm ra thị trường.  
     A. After releasing the product to the market.
   - B. Trong giai đoạn build, trước khi deploy.  
     B. During the build phase, before deploy.
   - C. Trước khi viết PRD, ở giai đoạn prototype.  
     C. Before writing the PRD, at the prototype stage.
   - D. Chỉ khi có lỗi nghiêm trọng từ người dùng.  
     D. Only when there's a critical error from users.
   **Đáp án / Answer:** C

4. Một AI-native PRD cần bổ sung nội dung nào sau đây mà PRD truyền thống thường không có?  
   What content does an AI-native PRD need to add that traditional PRDs usually lack?
   - A. Mô tả chi tiết giao diện người dùng.  
     A. Detailed UI description.
   - B. Evaluation Rubric và Golden Outputs.  
     B. Evaluation Rubric and Golden Outputs.
   - C. Biểu đồ Gantt cho lộ trình phát triển.  
     C. Gantt chart for the development roadmap.
   - D. Kế hoạch marketing cho sản phẩm.  
     D. Marketing plan for the product.
   **Đáp án / Answer:** B

5. Khi thiết kế Scenario Dataset, PM nên sử dụng công cụ nào để đảm bảo coverage thực tế?  
   When designing a Scenario Dataset, which tool should a PM use to ensure realistic coverage?
   - A. Nhờ LLM sinh ra 50 prompts ngẫu nhiên.  
     A. Have LLMs generate 50 random prompts.
   - B. User Input Grid với các dimension WHO, WHAT, HOW, CONTEXT, RISK.  
     B. User Input Grid with dimensions WHO, WHAT, HOW, CONTEXT, RISK.
   - C. Chỉ dùng các case từ người dùng thực tế.  
     C. Only use cases from real users.
   - D. Lấy toàn bộ dữ liệu từ train set của mô hình.  
     D. Take all data from the model's training set.
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 22
### Day 22 Review Questions
1. Tại sao cần Automated Evals thay vì Manual Review?
   Why are Automated Evals needed instead of Manual Review?
   - A. Manual review luôn chính xác hơn
     A. Manual review is always more accurate
   - B. Automated evals không thể scale
     B. Automated evals cannot scale
   - C. Manual review không thể mở rộng khi lượng sản phẩm (traces) lên tới 100k+
     C. Manual review cannot scale when the volume of traces reaches 100k+
   - D. Automated evals không cần calibration
     D. Automated evals do not need calibration
   **Đáp án / Answer:** C

2. Lớp đánh giá nào được ưu tiên số 1 và luôn bật trong hệ thống eval?
   Which evaluation layer is priority number 1 and always enabled in the eval system?
   - A. LLM-as-Judge
   - B. Code-based Evals
   - C. Human Review
   - D. Online Monitoring
   **Đáp án / Answer:** B

3. Khi nào nên sử dụng LLM-as-Judge thay vì Code-based Evals?
   When should LLM-as-Judge be used instead of Code-based Evals?
   - A. Khi tiêu chí xác minh được bằng rule, regex, hoặc schema
     A. When criteria can be verified by rules, regex, or schema
   - B. Khi cần đánh giá deterministic và nhanh
     B. When deterministic and fast evaluation is needed
   - C. Khi tiêu chí phụ thuộc vào ngữ cảnh, sắc thái ngôn ngữ
     C. When criteria depend on context and language nuances
   - D. Khi cần sample có chủ đích các trường hợp nghi ngờ
     D. When purposefully sampling suspicious cases is needed
   **Đáp án / Answer:** C

4. Trong Eval Lifecycle (quy trình đưa AI ra production), bước nào đóng vai trò Release Gate để chặn lỗi trước khi deploy?
   In the Eval Lifecycle (bringing AI to production), which step acts as a Release Gate to block errors before deployment?
   - A. Vibe Check (10-30 cases)
   - B. Offline Evals (100-1000 cases)
   - C. Online Monitoring (production)
   - D. Human Review (fallback)
   **Đáp án / Answer:** B

5. Metric nào là North Star Metric (chỉ số tổng hợp chính) cho Agent?
   Which metric is the North Star Metric for Agents?
   - A. P95 latency
   - B. Cost per request
   - C. Agent Success Rate (tổng hợp từ task correctness, schema pass rate, v.v.)
     C. Agent Success Rate (aggregated from task correctness, schema pass rate, etc.)
   - D. User feedback count
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 23
### Day 23 Review Questions

1. Trong RAGAS framework, metric nào đo mức độ "ảo giác" (hallucination) bằng cách kiểm tra câu trả lời có được hỗ trợ bởi ngữ cảnh (context) hay không?
   In the RAGAS framework, which metric measures "hallucination" by checking whether the answer is supported by the context?
   - A. Context Precision
   - B. Answer Relevancy
   - C. Faithfulness
   - D. Context Recall
   **Đáp án / Answer:** C

2. Khi sử dụng LLM làm người đánh giá (LLM-as-Judge), bias nào xảy ra khi LLM có xu hướng chọn phương án đầu tiên hoặc cuối cùng trong danh sách?
   When using an LLM as a judge (LLM-as-Judge), which bias occurs when the LLM tends to choose the first or last option in a list?
   - A. Length Bias
   - B. Self-Enhancement Bias
   - C. Style Bias
   - D. Position Bias
   **Đáp án / Answer:** D

3. Trong kiến trúc Guardrails 4 lớp, lớp nào chịu trách nhiệm chặn dữ liệu PII (thông tin nhận dạng cá nhân) bằng cách sử dụng Regex hoặc Presidio?
   In the 4-layer Guardrails architecture, which layer is responsible for blocking PII (Personally Identifiable Information) using Regex or Presidio?
   - A. L2 – LLM Layer
   - B. L4 – Audit Layer
   - C. L1 – Input Layer
   - D. L3 – Output Layer
   **Đáp án / Answer:** C

4. Phương pháp nào dùng mô hình Natural Language Inference (NLI) để phát hiện mâu thuẫn giữa câu trả lời và ngữ cảnh, từ đó nhận diện hallucination?
   Which method uses a Natural Language Inference (NLI) model to detect contradictions between the answer and context, thereby identifying hallucinations?
   - A. SelfCheckGPT
   - B. Semantic Similarity
   - C. NLI-based Detection
   - D. RAGAS Answer Relevancy
   **Đáp án / Answer:** C

5. Metric nào trong RAGAS là reference-free (không cần ground truth) và có thể sử dụng trực tiếp trong môi trường production?
   Which metric in RAGAS is reference-free (no ground truth needed) and can be used directly in a production environment?
   - A. Context Recall
   - B. Exact Match
   - C. Faithfulness
   - D. BLEU
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 24
### Day 24 Review Questions

1. Theo bài giảng, định nghĩa nào dưới đây mô tả đúng nhất về “AI an toàn”?
   According to the lecture, which of the following definitions best describes "Safe AI"?
   - A. Một hệ thống AI có độ chính xác cao và không bao giờ mắc lỗi.
     A. An AI system with high accuracy that never makes mistakes.
   - B. Một hệ thống AI được đặt trong bối cảnh phù hợp, có rào chắn và có người chịu trách nhiệm khi xảy ra sự cố.
     B. An AI system placed in an appropriate context, with guardrails and human accountability when incidents occur.
   - C. Một hệ thống AI có khả năng tự học và cải thiện mà không cần con người.
     C. An AI system capable of self-learning and improvement without humans.
   - D. Một hệ thống AI tuân thủ tất cả các quy định pháp luật hiện hành.
     D. An AI system that complies with all current legal regulations.
   **Đáp án / Answer:** B

2. Trạng thái “Sycophancy” trong AI đề cập đến hiện tượng gì?
   What phenomenon does the state of “Sycophancy” in AI refer to?
   - A. AI tự bịa ra thông tin sai lệch nhưng rất tự tin.
     A. AI makes up false information but is very confident.
   - B. AI luôn đồng ý với người dùng ngay cả khi người dùng sai.
     B. AI always agrees with the user even when the user is wrong.
   - C. AI tiết lộ thông tin cá nhân của người dùng khác.
     C. AI discloses other users' personal information.
   - D. AI từ chối trả lời mọi câu hỏi nhạy cảm.
     D. AI refuses to answer all sensitive questions.
   **Đáp án / Answer:** B

3. Khi một hệ thống AI đưa ra câu trả lời sai do không có đủ nguồn tham khảo (grounding) trong system message, lỗi này thuộc lớp nào trong System Map?
   When an AI system gives a wrong answer due to insufficient grounding in the system message, which layer in the System Map does this error belong to?
   - A. UX (Trải nghiệm người dùng)
     A. UX (User Experience)
   - B. Safety System (Hệ thống an toàn)
     B. Safety System
   - C. Model (Mô hình)
     C. Model
   - D. System Message & Grounding (Thông báo hệ thống và nền tảng)
     D. System Message & Grounding
   **Đáp án / Answer:** D

4. Trong Harm Map Framework, yếu tố “Scale” đánh giá điều gì?
   In the Harm Map Framework, what does the “Scale” factor assess?
   - A. Mức độ nghiêm trọng của tác hại (từ thấp đến nguy kịch).
     A. The severity of the harm (from low to critical).
   - B. Số lượng người hoặc nhóm bị ảnh hưởng.
     B. The number of people or groups affected.
   - C. Khả năng xảy ra tác hại.
     C. The probability of harm occurring.
   - D. Tần suất tác hại lặp lại nếu đã xảy ra.
     D. The frequency of the harm repeating once it has occurred.
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 25
### Day 25 Review Questions
1. Yếu tố nào trong RICE Framework được đánh giá trên thang điểm từ 0.25 (rất nhỏ) đến 3 (rất lớn)?
   Which element in the RICE Framework is evaluated on a scale from 0.25 (very small) to 3 (very large)?
   - A. Reach
   - B. Impact
   - C. Confidence
   - D. Effort
   **Đáp án / Answer:** B

2. Theo phương pháp Now/Next/Later, mức độ chi tiết của phần "NEXT" (3-6 tháng) được mô tả như thế nào?
   According to the Now/Next/Later method, how is the level of detail for the "NEXT" section (3-6 months) described?
   - A. Chi tiết cao, rủi ro thấp
     A. High detail, low risk
   - B. Chi tiết trung bình, rủi ro trung bình
     B. Medium detail, medium risk
   - C. Chi tiết thấp, rủi ro cao
     C. Low detail, high risk
   - D. Không có mô tả cụ thể
     D. No specific description
   **Đáp án / Answer:** B

3. Trong OKRs, loại Key Result nào là "hành vi người dùng mang tính dự báo"?
   In OKRs, which type of Key Result is "predictive user behavior"?
   - A. Lagging
   - B. Leading
   - C. Quality
   - D. Output
   **Đáp án / Answer:** B

4. Đối với startup AI, yếu tố nào thường là "đường găng" (critical path) quyết định ngày ra mắt?
   For an AI startup, what is typically the "critical path" that determines the launch date?
   - A. Phát triển giao diện người dùng
     A. User interface development
   - B. Tối ưu hóa mô hình AI
     B. AI model optimization
   - C. Pipeline dữ liệu và tuân thủ pháp lý
     C. Data pipeline and legal compliance
   - D. Chiến dịch marketing
     D. Marketing campaign
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 26
### Day 26 Review Questions
1. Theo bài giảng, xu hướng đầu tư mới của các VC hiện nay tập trung vào lĩnh vực nào?
   According to the lecture, what field are current VC investment trends focusing on?
   - A. Thương mại điện tử tổng quát
     A. General E-commerce
   - B. AI-Native Service Companies, AI + Hardware, AI + Deeptech, Software for Agents
   - C. Edtech truyền thống
     C. Traditional Edtech
   - D. Startup không sử dụng AI
     D. Non-AI startups
   **Đáp án / Answer:** B

2. Yếu tố nào sau đây là một trong những chìa khóa để gọi vốn thành công?
   Which of the following is one of the keys to successful fundraising?
   - A. Chỉ tập trung vào công nghệ ("tech-first") mà không quan tâm khách hàng
     A. Focusing only on tech ("tech-first") without caring about customers
   - B. Đội ngũ sáng lập đáng tin cậy và cam kết
     B. A reliable and committed founding team
   - C. Sản phẩm có gắn nhãn "AI" dù chưa giải quyết vấn đề cốt lõi
     C. Products labeled "AI" even if they don't solve the core problem
   - D. Kế hoạch tài chính không rõ ràng
     D. Unclear financial plans
   **Đáp án / Answer:** B

3. Phương pháp hiệu quả nhất để tìm nhà đầu tư phù hợp là gì?
   What is the most effective method for finding suitable investors?
   - A. Gửi email lạnh hàng loạt
     A. Mass cold emailing
   - B. Giới thiệu từ người quen (referrals)
     B. Introductions through connections (referrals)
   - C. Đăng bài tuyển dụng trên LinkedIn
     C. Posting job openings on LinkedIn
   - D. Mua danh sách email từ Crunchbase
     D. Buying email lists from Crunchbase
   **Đáp án / Answer:** B

4. Trong bài lab, bước "Market Positioning Memo" yêu cầu ước tính những thông số nào để giải quyết vấn đề "Unclear financials"?
   In the lab, the "Market Positioning Memo" step requires estimating what parameters to solve the "Unclear financials" issue?
   - A. Số nhân viên và văn phòng
     A. Number of employees and offices
   - B. Unit Economics, Cash Needs và KPIs
     B. Unit Economics, Cash Needs, and KPIs
   - C. Số lượng đối thủ cạnh tranh
     C. Number of competitors
   - D. Chi phí marketing và PR
     D. Marketing and PR costs
   **Đáp án / Answer:** B

5. Trước buổi gặp nhà đầu tư, điều nào cần tìm hiểu trước tiên?
   Before meeting with investors, what should be researched first?
   - A. Sở thích cá nhân của từng partner
     A. Personal hobbies of each partner
   - B. Ticket size điển hình và danh mục đầu tư hiện tại của quỹ
     B. Typical ticket size and the fund's current investment portfolio
   - C. Màu sắc logo của quỹ
     C. The fund's logo colors
   - D. Ngày sinh của CEO quỹ
     D. The fund CEO's birth date
   **Đáp án / Answer:** B

---

### Câu hỏi ôn tập Ngày 27
### Day 27 Review Questions

1. Trong mô hình 4 góc phần tư quản lý stakeholders, nhóm nào có **Chiến lược: Thuyết phục, giảm thiểu rủi ro từ sớm, giải quyết mối quan tâm trước khi họ hỏi**?
   In the 4-quadrant stakeholder management model, which group has the **Strategy: Persuade, mitigate risks early, address concerns before they ask**?
   - A. Champions
   - B. Blockers
   - C. Supporters
   - D. Bystanders
   **Đáp án / Answer:** B

2. Trong ma trận RACI, thành viên nào phải là **duy nhất một người cho mỗi nhiệm vụ** và chịu trách nhiệm quyết định cuối cùng?
   In the RACI matrix, which member must be **only one person per task** and holds the ultimate decision-making responsibility?
   - A. Responsible
   - B. Accountable
   - C. Consulted
   - D. Informed
   **Đáp án / Answer:** B

3. Nguyên tắc **"Kết luận trước"** khi giao tiếp với stakeholders yêu cầu điều gì?
   What does the **"Conclusion first"** principle require when communicating with stakeholders?
   - A. Đưa ra tất cả dữ liệu trước, sau đó mới kết luận
     A. Provide all data first, then conclude
   - B. Bắt đầu bằng kết luận, sau đó đưa ra lý do và dữ liệu
     B. Start with the conclusion, then provide reasons and data
   - C. Chỉ trình bày kết luận khi được hỏi
     C. Only present the conclusion when asked
   - D. Tập trung vào chi tiết kỹ thuật trước
     D. Focus on technical details first
   **Đáp án / Answer:** B

4. Yếu tố nào được Project Aristotle xác định là **quan trọng nhất** cho một nhóm AI hiệu quả?
   What factor did Project Aristotle identify as the **most important** for an effective AI team?
   - A. Cấu trúc nhóm Hybrid (Hub-and-Spoke)
     A. Hybrid team structure (Hub-and-Spoke)
   - B. Năng lực L3 (AI Builder)
     B. L3 Capability (AI Builder)
   - C. An toàn tâm lý (Psychological Safety)
     C. Psychological Safety
   - D. Áp dụng Agentic SDLC
     D. Applying Agentic SDLC
   **Đáp án / Answer:** C

---

### Câu hỏi ôn tập Ngày 28
### Day 28 Review Questions
1. Lớp kiến trúc nào trong hệ thống AI thực tế chịu trách nhiệm định nghĩa ODD (Operational Design Domain) và giám sát an toàn?
   Which architectural layer in a real-world AI system is responsible for defining the ODD (Operational Design Domain) and safety monitoring?
   - A. Data / Sensor
   - B. Perception
   - C. Decision / Policy
   - D. Ops / Safety
   **Đáp án / Answer:** D

2. Theo bài học từ hệ thống ADAS/Autonomous Driving, điều nào sau đây là đúng về mô hình End-to-End?
   According to lessons from ADAS/Autonomous Driving systems, which of the following is true about End-to-End models?
   - A. Mô hình E2E hoàn toàn thay thế được các lớp kiến trúc khác
     A. E2E models can completely replace other architectural layers
   - B. Mô hình E2E vẫn cần một safety shell độc lập và ODD được định nghĩa từ trước
     B. E2E models still need an independent safety shell and a pre-defined ODD
   - C. Mô hình E2E không cần dữ liệu huấn luyện từ các tình huống hiếm
     C. E2E models do not need training data from rare situations
   - D. Mô hình E2E chỉ áp dụng cho xe tự hành, không dùng cho robot
     D. E2E models only apply to autonomous vehicles, not used for robots
   **Đáp án / Answer:** B

3. Mục tiêu chính khi triển khai AI cho hệ thống CCTV là gì?
   What is the main goal when deploying AI for CCTV systems?
   - A. Áp dụng mô hình lớn vào mọi khung hình để tăng độ chính xác
     A. Applying large models to every frame to increase accuracy
   - B. Giảm số lượng clip cần con người kiểm tra
     B. Reducing the number of clips that humans need to review
   - C. Loại bỏ hoàn toàn việc xử lý trên thiết bị biên (edge)
     C. Completely eliminating processing on edge devices
   - D. Thay thế hoàn toàn con người trong việc giám sát
     D. Completely replacing humans in monitoring
   **Đáp án / Answer:** B

4. Trong kiến trúc Humanoid Robot, điều nào sau đây là bài học quan trọng được rút ra?
   In Humanoid Robot architecture, which of the following is an important lesson learned?
   - A. Dữ liệu robot rẻ hơn dữ liệu web
     A. Robot data is cheaper than web data
   - B. Sim-to-real gap có thể bỏ qua nhờ mô phỏng hoàn hảo
     B. Sim-to-real gap can be ignored thanks to perfect simulation
   - C. Dữ liệu robot đắt hơn dữ liệu web và cần domain randomization để giảm sim-to-real gap
     C. Robot data is more expensive than web data and needs domain randomization to reduce the sim-to-real gap
   - D. Safety guards (e-stop, torque limits) phải phụ thuộc vào policy để đảm bảo tính nhất quán
     D. Safety guards (e-stop, torque limits) must depend on the policy to ensure consistency
   **Đáp án / Answer:** C

---
