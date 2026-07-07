---
type: summary
title: "Câu hỏi ôn tập - Track1"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track1"
tags: [review, track1]
timestamp: 2026-07-06
sources: []
---
*# Bộ câu hỏi ôn tập Track1*

### *Câu hỏi ôn tập Ngày 3*

   *Điểm khác biệt chính giữa Agent và LLM Chatbot là gì?*  
     *A. Agent chỉ hoạt động dựa trên luật if/else cứng.*  
     *B. Agent chủ động định hướng theo mục tiêu và có thể sử dụng tools.*  
     *C. Chatbot có khả năng suy luận nhiều bước phức tạp hơn Agent.*  
     *D. Agent không có khả năng ghi nhớ dài hạn.*  
   **Answer / Đáp án:** B

   *Trong Agentic Fit Framework, tiêu chí nào cho thấy bài toán cần sự tương tác với môi trường bên ngoài?*  
     *A. Suy luận nhiều bước*  
     *B. Tương tác công cụ*  
     *C. Quyết định động*  
     *D. Tầm nhìn dài*  
   **Answer / Đáp án:** B

   *Thành phần nào trong kiến trúc Agent chịu trách nhiệm quyết định gọi tool và xử lý đầu ra?*  
     *A. Tri giác*  
     *B. Suy luận*  
     *C. Hành động*  
     *D. Bộ nhớ*  
   **Answer / Đáp án:** C

   *Lợi ích lớn nhất của ReAct pattern so với các phương pháp khác là gì?*  
     *A. Giảm chi phí vận hành.*  
     *B. Tăng tốc độ phản hồi.*  
     *C. Khả năng debug và can thiệp vào quá trình suy luận.*  
     *D. Loại bỏ hoàn toàn lỗi parse.*  
   **Answer / Đáp án:** C

---

### *Câu hỏi ôn tập Ngày 4*

   *Theo mô hình RTCF, thành phần nào được coi là ưu tiên hàng đầu trong một prompt tốt?*  
     *A. Vai trò*  
     *B. Nhiệm vụ*  
     *C. Bối cảnh*  
     *D. Định dạng*  
   **Answer / Đáp án:** B

   *Kỹ thuật nào được khuyên dùng để ép LLM đưa ra output format ổn định, thường dùng 2-5 ví dụ tập trung vào edge‑cases?*  
   **Answer / Đáp án:** C

   *Trong kiến trúc Tool Calling, bước thứ hai (sau khi nhận user input) LLM trả về dữ liệu gì để app có thể thực thi tool?*  
     *C. Một câu lệnh SQL*  
     *D. Một dictionary chứa `tool_outputs`*  
   **Answer / Đáp án:** B

   *Khi gặp lỗi trong quá trình thực thi tool, chiến lược xử lý lỗi được đề xuất là gì?*  
     *A. Dừng toàn bộ agent và thông báo lỗi cho user*  
     *B. Gửi raw error message lại cho LLM để nó tự sửa lỗi*  
     *C. Bỏ qua lỗi và tiếp tục thực thi tool khác*  
     *D. Gọi lại tool với tham số mặc định*  
   **Answer / Đáp án:** B

   *Trong LangGraph, cơ chế nào được dùng để lưu trữ và cập nhật `messages` xuyên suốt đồ thị?*  
     *A. Biến toàn cục*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 15*

   *Mục tiêu chính của Track 1 (Phase 2) là gì?*  
     *A. Học cách code và triển khai mô hình AI từ đầu*  
     *B. Chuyển từ việc "build AI" sang ra quyết định sản phẩm AI (chiến lược, ROI, governance)*  
     *C. Tập trung vào cải thiện độ chính xác của thuật toán deep learning*  
     *D. Xây dựng kỹ năng quản lý đội ngũ kỹ thuật AI*  
   **Answer / Đáp án:** B

   *Ai là người phù hợp nhất với Track này?*  
     *A. Kỹ sư chỉ thích code và không quan tâm đến business case*  
     *B. Người thích viết Problem Statement, phân biệt Need vs Feature, và thoải mái với sự mơ hồ*  
     *C. Chuyên gia luật am hiểu AI Act nhưng không làm sản phẩm*  
     *D. Data scientist chuyên tối ưu mô hình mà không cần quan tâm đến UX*  
   **Answer / Đáp án:** B

   *Năng lực nào KHÔNG được xây dựng trong Track này?*  
     *A. Problem framing và định nghĩa success metric*  
     *B. Thiết kế trust/UX cho sản phẩm AI*  
     *C. Lập trình model deployment và fine-tuning*  
     *D. ROI & business case, pilot plan & đo lường adoption*  
   **Answer / Đáp án:** C

   *Thách thức lớn nhất khi theo Track này là gì?*  
     *A. Thiếu dữ liệu để huấn luyện mô hình AI*  
     *B. Phải sống với sự mơ hồ, ra quyết định khi dữ liệu chưa đủ, và thuyết phục stakeholder*  
     *C. Không có cơ hội việc làm vì thị trường không cần AI PM*  
     *D. Kết quả đo bằng kỹ thuật (accuracy, F1) nên dễ thấy ngay*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 16*

   *Theo nội dung bài giảng, yếu tố nào quyết định khách hàng sẽ chuyển từ sản phẩm cũ sang sản phẩm AI mới?*  
     *A. Sản phẩm AI miễn phí hoàn toàn*  
     *B. Giá trị nhận được từ sản phẩm mới lớn hơn gấp 10 lần so với sản phẩm cũ*  
     *C. Sản phẩm AI có giao diện đẹp hơn*  
     *D. Sản phẩm AI được quảng cáo nhiều*  
   **Answer / Đáp án:** B

   *Trong Job-to-be-Done (JTBD) Framework, “Job Story” được viết theo cấu trúc nào?*  
     *A. Với vai trò [persona], tôi muốn [tính năng] để đạt [mục tiêu]*  
     *B. Khi [bối cảnh], tôi muốn [động lực/công việc], để tôi có thể [kết quả mong đợi]*  
     *C. Nếu [điều kiện], thì [hành động] sẽ dẫn đến [kết quả]*  
     *D. Từ [trạng thái hiện tại] đến [trạng thái mong muốn] nhờ [giải pháp]*  
   **Answer / Đáp án:** B

   *Khi sử dụng Job Map (JTBD Lite Map), mục đích chính của việc xác định “Pain Points” là gì?*  
     *A. Liệt kê tất cả lỗi kỹ thuật của sản phẩm hiện tại*  
     *B. Tìm ra bước nào người dùng thực hiện chậm, sai sót, tốn công sức, hoặc thiếu tin cậy*  
     *C. Đo lường mức độ hài lòng của khách hàng*  
     *D. Xác định đối thủ cạnh tranh trực tiếp*  
   **Answer / Đáp án:** B

   *Theo bài giảng, sự khác biệt chính khi xây dựng Product Hypothesis trong thời đại AI là gì?*  
     *A. Cần tập trung vào tính năng công nghệ hơn là nhu cầu người dùng*  
     *B. Cần kiểm chứng giả định về sự thay đổi kỳ vọng của người dùng và cách thức hoàn thành công việc*  
     *C. Chỉ cần dựa trên dữ liệu lịch sử sử dụng sản phẩm cũ*  
     *D. Bỏ qua các bước kiểm chứng vì AI luôn mang lại giá trị vượt trội*  
   **Answer / Đáp án:** B

   *Trường hợp nào dưới đây là ví dụ về “AI Shock” được đề cập trong bài giảng?*  
     *A. Một công ty tăng doanh thu nhờ thêm tính năng chatbot vào sản phẩm*  
     *B. Chegg bị gián đoạn khi người dùng chuyển từ trả tiền lời giải sang hỏi AI miễn phí và nhận câu trả lời tức thì*  
     *C. Một startup AI thành công nhờ giữ nguyên mô hình kinh doanh cũ*  
     *D. Người dùng trung thành với sản phẩm cũ dù AI cung cấp giá trị tương tự*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 17*

   *Theo bài giảng, "Leap of Faith Assumptions" bao gồm bốn loại rủi ro chính. Loại rủi ro nào liên quan đến câu hỏi "Người dùng có thể tìm ra cách sử dụng sản phẩm không?"*  
     *A. Rủi ro giá trị*  
     *B. Rủi ro khả dụng*  
     *C. Rủi ro khả thi*  
     *D. Rủi ro khả năng kinh doanh*  
   **Answer / Đáp án:** B

   *Loại prototype nào phù hợp nhất để kiểm tra tính chính xác của quy trình làm việc và xem người dùng có nhận ra các tính năng chính hay không?*  
   **Answer / Đáp án:** C

   *Trong ví dụ về Wizard of Oz MVP, hai người sáng lập đã thủ công ghi chép cuộc họp dưới danh nghĩa "Fred" để kiểm tra giả thuyết gì?*  
     *A. Người dùng sẽ tin tưởng AI tạo kế hoạch bài giảng*  
     *B. Mọi người sẵn sàng trả tiền cho dịch vụ ghi chú AI*  
     *C. Có thể xây dựng một ứng dụng ghi chú tự động*  
     *D. Giao diện web tĩnh có đủ để thu hút khách hàng*  
   **Answer / Đáp án:** B

   *Trong Lab Assignment, bước "Three Cheaper Test Alternatives" yêu cầu brainstorm các cách kiểm tra khác nhau. Điều nào sau đây KHÔNG phải là một dạng artifact hợp lệ cho bước này?*  
     *C. Một tính năng phần mềm hoàn chỉnh*  
   **Answer / Đáp án:** C

---

### *Câu hỏi ôn tập Ngày 18*

   *Công thức **Trust Calibration** bao gồm Expectation, Explainability và Control. Yếu tố nào giúp người dùng hiểu tại sao AI đưa ra một kết quả cụ thể?*  
     *A. Kỳ vọng*  
     *B. Khả năng giải thích*  
     *C. Kiểm soát*  
     *D. Tự động hóa*  
   **Answer / Đáp án:** B

   *Trong quyết định **Augmentation vs Automation**, khi nào AI nên tự động thực hiện hành động (Act)?*  
     *A. Độ chắc chắn thấp, chi phí sai lầm cao*  
     *B. Độ chắc chắn cao, chi phí sai lầm thấp*  
     *C. Độ chắc chắn trung bình, tác động đáng kể*  
     *D. Luôn luôn tự động để tiết kiệm thời gian*  
   **Answer / Đáp án:** B

   *Khi AI gặp lỗi hoặc không chắc chắn, cách xử lý nào sau đây được khuyến khích?*  
     *A. Ẩn kết quả để tránh gây nhầm lẫn*  
     *B. Hiển thị kết quả với mức độ tin cậy và cung cấp lối thoát*  
     *C. Bắt buộc người dùng chấp nhận kết quả*  
     *D. Không thu thập phản hồi từ lỗi*  
   **Answer / Đáp án:** B

   *"Người dùng nhấn nút **thích/không thích** hoặc đánh giá sản phẩm" thuộc loại phản hồi nào?*  
     *A. Phản hồi người dùng (Implicit)*  
     *B. Phản hồi người dùng (Explicit)*  
     *C. Phản hồi hệ thống (Explicit)*  
     *D. Phản hồi hệ thống (Implicit)*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 19*

   **Tại sao Retention lại được coi là quan trọng hơn Acquisition trong chiến lược tăng trưởng?**  
     *A. Vì chi phí thu hút người dùng mới (CAC) luôn thấp hơn chi phí giữ chân.*  
     *B. Vì Retention giúp đánh giá liệu sản phẩm có thực sự mang lại giá trị cốt lõi hay không.*  
     *C. Vì các hoạt động PR và quảng cáo không thể làm tăng số lượng người dùng.*  
     *D. Vì Retention là mét duy nhất ảnh hưởng đến doanh thu dài hạn.*  
   **Answer / Đáp án:** B

   **Khái niệm "Natural Frequency" trong bối cảnh Retention chỉ điều gì?**  
     *A. Tần suất sản phẩm gửi thông báo nhắc nhở cho người dùng.*  
     *B. Tần suất người dùng tự nhiên gặp vấn đề mà sản phẩm giải quyết (hàng ngày, tuần, tháng...).*  
     *C. Tần suất đội ngũ sản phẩm thực hiện các thử nghiệm A/B.*  
     *D. Tần suất người dùng chia sẻ sản phẩm lên mạng xã hội.*  
   **Answer / Đáp án:** B

   **Theo mô hình Hook (Habit Loop), yếu tố nào đóng vai trò tạo ra động lực nội tại cho người dùng quay lại lần tiếp theo?**  
     *A. Kích hoạt bên ngoài, như thông báo.*  
     *B. Phần thưởng biến đổi, tạo cảm giác tò mò và hứng thú.*  
     *C. Hành động, đơn giản và dễ thực hiện.*  
     *D. Đầu tư – người dùng bỏ công sức vào sản phẩm.*  
   **Answer / Đáp án:** B

   **Chỉ số nào thường được dùng để đo lường mức độ gắn bó (Stickiness) của người dùng?**  
   **Answer / Đáp án:** A

   **Khi D1 Retention của sản phẩm chỉ đạt khoảng 10%, nguyên nhân chủ yếu thường nằm ở đâu?**  
     *A. Giao diện người dùng chưa đẹp, cần thay đổi màu sắc nút bấm.*  
     *B. Core Value (giá trị cốt lõi) chưa giải quyết đúng nhu cầu của người dùng.*  
     *C. Chiến dịch truyền thông chưa đủ mạnh để thu hút đúng đối tượng.*  
     *D. Tần suất gửi thông báo (notification) chưa đủ dày.*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 20*

   *Theo bài giảng, đâu là định nghĩa chính xác về "Core Action"?*  
     *A. Hành động đăng nhập vào ứng dụng.*  
     *B. Hành động cụ thể chứng tỏ người dùng đã nhận được giá trị (ví dụ: hoàn thành một bài học).*  
     *C. Lượt truy cập trang chủ.*  
     *D. Số lần mở ứng dụng.*  
   **Answer / Đáp án:** B

   *Khi xác định chỉ số Retention, điều quan trọng nhất là gì?*  
     *A. Chọn chu kỳ cố định là 7 ngày.*  
     *B. Phải phù hợp với tần suất tự nhiên của vấn đề người dùng.*  
     *C. Luôn sử dụng DAU.*  
     *D. Chỉ đo lường sau 30 ngày.*  
   **Answer / Đáp án:** B

   *Trong Hook Model (Nir Eyal), bước "Variable Reward" được chia thành ba loại. Đâu không phải là một trong ba loại đó?*  
     *A. Tribe (xã hội)*  
     *B. Hunt (tài nguyên)*  
     *C. Self (sự thành thạo)*  
     *D. Profit (lợi nhuận)*  
   **Answer / Đáp án:** D

   *"North Star Metric" trong Measurement Ladder là gì?*  
     *A. Chỉ số đo lường doanh thu hàng tháng.*  
     *B. Chỉ số hàng đầu phản ánh việc tạo ra giá trị cốt lõi.*  
     *C. Tổng số người dùng đăng ký.*  
     *D. Thời gian trung bình trên ứng dụng.*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 21*

   *Trong sản phẩm AI, vai trò của Product Manager (PM) thay đổi như thế nào so với sản phẩm truyền thống?*  
     *A. PM vẫn tập trung vào Usage Flow và Conversion Rate như trước.*  
     *B. PM chuyển sang quản lý Agent Success Rate và Quality Distributions.*  
     *C. PM chỉ chịu trách nhiệm về mặt kỹ thuật của mô hình.*  
     *D. PM giao toàn bộ việc đánh giá cho đội ngũ Data Science.*  
   **Answer / Đáp án:** B

   *Bộ chấm điểm nào được coi là "chuẩn vàng" để hiệu chỉnh các bộ chấm khác?*  
   **Answer / Đáp án:** C

   *Theo vòng đời AI Evals, giai đoạn "Vibe Check" nên được thực hiện vào thời điểm nào?*  
     *A. Sau khi phát hành sản phẩm ra thị trường.*  
     *B. Trong giai đoạn build, trước khi deploy.*  
     *C. Trước khi viết PRD, ở giai đoạn prototype.*  
     *D. Chỉ khi có lỗi nghiêm trọng từ người dùng.*  
   **Answer / Đáp án:** C

   *Một AI-native PRD cần bổ sung nội dung nào sau đây mà PRD truyền thống thường không có?*  
     *A. Mô tả chi tiết giao diện người dùng.*  
     *B. Evaluation Rubric và Golden Outputs.*  
     *C. Biểu đồ Gantt cho lộ trình phát triển.*  
     *D. Kế hoạch marketing cho sản phẩm.*  
   **Answer / Đáp án:** B

   *Khi thiết kế Scenario Dataset, PM nên sử dụng công cụ nào để đảm bảo coverage thực tế?*  
     *A. Nhờ LLM sinh ra 50 prompts ngẫu nhiên.*  
     *B. User Input Grid với các dimension WHO, WHAT, HOW, CONTEXT, RISK.*  
     *C. Chỉ dùng các case từ người dùng thực tế.*  
     *D. Lấy toàn bộ dữ liệu từ train set của mô hình.*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 22*

   *Tại sao cần Automated Evals thay vì Manual Review?*  
     *A. Manual review luôn chính xác hơn*  
     *B. Automated evals không thể scale*  
     *C. Manual review không thể mở rộng khi lượng sản phẩm (traces) lên tới 100k+*  
     *D. Automated evals không cần calibration*  
   **Answer / Đáp án:** C

   *Lớp đánh giá nào được ưu tiên số 1 và luôn bật trong hệ thống eval?*  
   **Answer / Đáp án:** B

   *Khi nào nên sử dụng LLM-as-Judge thay vì Code-based Evals?*  
     *A. Khi tiêu chí xác minh được bằng rule, regex, hoặc schema*  
     *B. Khi cần đánh giá deterministic và nhanh*  
     *C. Khi tiêu chí phụ thuộc vào ngữ cảnh, sắc thái ngôn ngữ*  
     *D. Khi cần sample có chủ đích các trường hợp nghi ngờ*  
   **Answer / Đáp án:** C

   *Trong Eval Lifecycle (quy trình đưa AI ra production), bước nào đóng vai trò Release Gate để chặn lỗi trước khi deploy?*  
   **Answer / Đáp án:** B

   *Metric nào là North Star Metric (chỉ số tổng hợp chính) cho Agent?*  
     *C. Agent Success Rate (tổng hợp từ task correctness, schema pass rate, v.v.)*  
   **Answer / Đáp án:** C

---

### *Câu hỏi ôn tập Ngày 23*

   *Trong RAGAS framework, metric nào đo mức độ "ảo giác" (hallucination) bằng cách kiểm tra câu trả lời có được hỗ trợ bởi ngữ cảnh (context) hay không?*  
   **Answer / Đáp án:** C

   *Khi sử dụng LLM làm người đánh giá (LLM-as-Judge), bias nào xảy ra khi LLM có xu hướng chọn phương án đầu tiên hoặc cuối cùng trong danh sách?*  
   **Answer / Đáp án:** D

   *Trong kiến trúc Guardrails 4 lớp, lớp nào chịu trách nhiệm chặn dữ liệu PII (thông tin nhận dạng cá nhân) bằng cách sử dụng Regex hoặc Presidio?*  
   **Answer / Đáp án:** C

   *Phương pháp nào dùng mô hình Natural Language Inference (NLI) để phát hiện mâu thuẫn giữa câu trả lời và ngữ cảnh, từ đó nhận diện hallucination?*  
   **Answer / Đáp án:** C

   *Metric nào trong RAGAS là reference-free (không cần ground truth) và có thể sử dụng trực tiếp trong môi trường production?*  
   **Answer / Đáp án:** C

---

### *Câu hỏi ôn tập Ngày 24*

   *Theo bài giảng, định nghĩa nào dưới đây mô tả đúng nhất về “AI an toàn”?*  
     *A. Một hệ thống AI có độ chính xác cao và không bao giờ mắc lỗi.*  
     *B. Một hệ thống AI được đặt trong bối cảnh phù hợp, có rào chắn và có người chịu trách nhiệm khi xảy ra sự cố.*  
     *C. Một hệ thống AI có khả năng tự học và cải thiện mà không cần con người.*  
     *D. Một hệ thống AI tuân thủ tất cả các quy định pháp luật hiện hành.*  
   **Answer / Đáp án:** B

   *Trạng thái “Sycophancy” trong AI đề cập đến hiện tượng gì?*  
     *A. AI tự bịa ra thông tin sai lệch nhưng rất tự tin.*  
     *B. AI luôn đồng ý với người dùng ngay cả khi người dùng sai.*  
     *C. AI tiết lộ thông tin cá nhân của người dùng khác.*  
     *D. AI từ chối trả lời mọi câu hỏi nhạy cảm.*  
   **Answer / Đáp án:** B

   *Khi một hệ thống AI đưa ra câu trả lời sai do không có đủ nguồn tham khảo (grounding) trong system message, lỗi này thuộc lớp nào trong System Map?*  
     *A. UX (Trải nghiệm người dùng)*  
     *B. Safety System (Hệ thống an toàn)*  
     *C. Model (Mô hình)*  
     *D. System Message & Grounding (Thông báo hệ thống và nền tảng)*  
   **Answer / Đáp án:** D

   *Trong Harm Map Framework, yếu tố “Scale” đánh giá điều gì?*  
     *A. Mức độ nghiêm trọng của tác hại (từ thấp đến nguy kịch).*  
     *B. Số lượng người hoặc nhóm bị ảnh hưởng.*  
     *C. Khả năng xảy ra tác hại.*  
     *D. Tần suất tác hại lặp lại nếu đã xảy ra.*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 25*

   *Yếu tố nào trong RICE Framework được đánh giá trên thang điểm từ 0.25 (rất nhỏ) đến 3 (rất lớn)?*  
   **Answer / Đáp án:** B

   *Theo phương pháp Now/Next/Later, mức độ chi tiết của phần "NEXT" (3-6 tháng) được mô tả như thế nào?*  
     *A. Chi tiết cao, rủi ro thấp*  
     *B. Chi tiết trung bình, rủi ro trung bình*  
     *C. Chi tiết thấp, rủi ro cao*  
     *D. Không có mô tả cụ thể*  
   **Answer / Đáp án:** B

   *Trong OKRs, loại Key Result nào là "hành vi người dùng mang tính dự báo"?*  
   **Answer / Đáp án:** B

   *Đối với startup AI, yếu tố nào thường là "đường găng" (critical path) quyết định ngày ra mắt?*  
     *A. Phát triển giao diện người dùng*  
     *B. Tối ưu hóa mô hình AI*  
     *C. Pipeline dữ liệu và tuân thủ pháp lý*  
     *D. Chiến dịch marketing*  
   **Answer / Đáp án:** C

---

### *Câu hỏi ôn tập Ngày 26*

   *Theo bài giảng, xu hướng đầu tư mới của các VC hiện nay tập trung vào lĩnh vực nào?*  
     *A. Thương mại điện tử tổng quát*  
     *C. Edtech truyền thống*  
     *D. Startup không sử dụng AI*  
   **Answer / Đáp án:** B

   *Yếu tố nào sau đây là một trong những chìa khóa để gọi vốn thành công?*  
     *A. Chỉ tập trung vào công nghệ ("tech-first") mà không quan tâm khách hàng*  
     *B. Đội ngũ sáng lập đáng tin cậy và cam kết*  
     *C. Sản phẩm có gắn nhãn "AI" dù chưa giải quyết vấn đề cốt lõi*  
     *D. Kế hoạch tài chính không rõ ràng*  
   **Answer / Đáp án:** B

   *Phương pháp hiệu quả nhất để tìm nhà đầu tư phù hợp là gì?*  
     *A. Gửi email lạnh hàng loạt*  
     *B. Giới thiệu từ người quen (referrals)*  
     *C. Đăng bài tuyển dụng trên LinkedIn*  
     *D. Mua danh sách email từ Crunchbase*  
   **Answer / Đáp án:** B

   *Trong bài lab, bước "Market Positioning Memo" yêu cầu ước tính những thông số nào để giải quyết vấn đề "Unclear financials"?*  
     *A. Số nhân viên và văn phòng*  
     *B. Unit Economics, Cash Needs và KPIs*  
     *C. Số lượng đối thủ cạnh tranh*  
     *D. Chi phí marketing và PR*  
   **Answer / Đáp án:** B

   *Trước buổi gặp nhà đầu tư, điều nào cần tìm hiểu trước tiên?*  
     *A. Sở thích cá nhân của từng partner*  
     *B. Ticket size điển hình và danh mục đầu tư hiện tại của quỹ*  
     *C. Màu sắc logo của quỹ*  
     *D. Ngày sinh của CEO quỹ*  
   **Answer / Đáp án:** B

---

### *Câu hỏi ôn tập Ngày 27*

   *Trong mô hình 4 góc phần tư quản lý stakeholders, nhóm nào có **Chiến lược: Thuyết phục, giảm thiểu rủi ro từ sớm, giải quyết mối quan tâm trước khi họ hỏi**?*  
     *A. Người ủng hộ*  
     *B. Người cản trở*  
     *C. Người hỗ trợ*  
     *D. Người đứng ngoài*  
   **Answer / Đáp án:** B

   *Trong ma trận RACI, thành viên nào phải là **duy nhất một người cho mỗi nhiệm vụ** và chịu trách nhiệm quyết định cuối cùng?*  
     *A. Người thực hiện*  
     *B. Người chịu trách nhiệm*  
     *C. Người được tham vấn*  
     *D. Người được thông báo*  
   **Answer / Đáp án:** B

   *Nguyên tắc **"Kết luận trước"** khi giao tiếp với stakeholders yêu cầu điều gì?*  
     *A. Đưa ra tất cả dữ liệu trước, sau đó mới kết luận*  
     *B. Bắt đầu bằng kết luận, sau đó đưa ra lý do và dữ liệu*  
     *C. Chỉ trình bày kết luận khi được hỏi*  
     *D. Tập trung vào chi tiết kỹ thuật trước*  
   **Answer / Đáp án:** B

   *Yếu tố nào được Project Aristotle xác định là **quan trọng nhất** cho một nhóm AI hiệu quả?*  
     *A. Cấu trúc nhóm Hybrid (Hub-and-Spoke)*  
     *B. Năng lực L3 (AI Builder)*  
     *C. An toàn tâm lý (Psychological Safety)*  
     *D. Áp dụng Agentic SDLC*  
   **Answer / Đáp án:** C

---

### *Câu hỏi ôn tập Ngày 28*

   *Lớp kiến trúc nào trong hệ thống AI thực tế chịu trách nhiệm định nghĩa ODD (Operational Design Domain) và giám sát an toàn?*  
     *A. Dữ liệu / Cảm biến*  
     *B. Tri giác*  
     *C. Quyết định / Chính sách*  
     *D. Vận hành / An toàn*  
   **Answer / Đáp án:** D

   *Theo bài học từ hệ thống ADAS/Autonomous Driving, điều nào sau đây là đúng về mô hình End-to-End?*  
     *A. Mô hình E2E hoàn toàn thay thế được các lớp kiến trúc khác*  
     *B. Mô hình E2E vẫn cần một safety shell độc lập và ODD được định nghĩa từ trước*  
     *C. Mô hình E2E không cần dữ liệu huấn luyện từ các tình huống hiếm*  
     *D. Mô hình E2E chỉ áp dụng cho xe tự hành, không dùng cho robot*  
   **Answer / Đáp án:** B

   *Mục tiêu chính khi triển khai AI cho hệ thống CCTV là gì?*  
     *A. Áp dụng mô hình lớn vào mọi khung hình để tăng độ chính xác*  
     *B. Giảm số lượng clip cần con người kiểm tra*  
     *C. Loại bỏ hoàn toàn việc xử lý trên thiết bị biên (edge)*  
     *D. Thay thế hoàn toàn con người trong việc giám sát*  
   **Answer / Đáp án:** B

   *Trong kiến trúc Humanoid Robot, điều nào sau đây là bài học quan trọng được rút ra?*  
     *A. Dữ liệu robot rẻ hơn dữ liệu web*  
     *B. Sim-to-real gap có thể bỏ qua nhờ mô phỏng hoàn hảo*  
     *C. Dữ liệu robot đắt hơn dữ liệu web và cần domain randomization để giảm sim-to-real gap*  
     *D. Safety guards (e-stop, torque limits) phải phụ thuộc vào policy để đảm bảo tính nhất quán*  
   **Answer / Đáp án:** C

---
