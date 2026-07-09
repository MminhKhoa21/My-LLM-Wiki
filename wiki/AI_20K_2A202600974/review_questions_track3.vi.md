---
type: summary
title: "Câu hỏi ôn tập - Track3"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track3"
tags: [review, track3]
timestamp: 2026-07-06
sources: []
---
Bộ câu hỏi ôn tập Track 3

Câu hỏi ôn tập Ngày 3

   Theo nội dung bài giảng, yếu tố nào sau đây **không** thuộc 4 tiêu chí của Agentic Fit Framework?
   - A. Lập luận nhiều bước
   - B. Tương tác công cụ
   - C. Phản hồi một lượt
   - D. Tầm nhìn dài
   **Đáp án / Answer:** C

   Trong ReAct pattern, thành phần nào đại diện cho bước "quan sát kết quả của hành động"?
   - A. Suy nghĩ
   - B. Hành động
   - C. Quan sát
   - D. Bộ nhớ
   **Đáp án / Answer:** C

   Ưu điểm chính của Native Tool Calling so với Text-ReAct là gì?
   - A. Tiêu tốn ít token hơn
   - B. Bắt buộc model tự sinh văn bản định dạng
   - C. Tăng tính ổn định nhờ JSON schema chuẩn từ API provider
   - D. Cho phép agent tự tạo tool mới
   **Đáp án / Answer:** C

   Loại lỗi nào xảy ra khi agent liên tục gọi một tool không hồi kết, không thoát được vòng lặp?
   - A. Công cụ tạo ảo giác
   - B. Quan sát trống
   - C. Hết thời gian/Vòng lặp
   - D. Lỗi phân tích
   **Đáp án / Answer:** C

   Để đánh giá chất lượng Agent, phương pháp nào được đề xuất thay vì chỉ nhìn kết quả cuối?
   - A. Đánh giá theo vết (đo tokens, độ trễ, số vòng lặp)
   - B. Kiểm tra mù với người dùng
   - C. So sánh với bot dựa trên quy tắc
   - D. Chỉ kiểm tra độ chính xác của tool
   **Đáp án / Answer:** A

---

Câu hỏi ôn tập Ngày 15

   Kỹ thuật nào sau đây **KHÔNG** được đề cập trong nội dung chính của Track 3?
   - A. GraphRAG và đồ thị tri thức
   - B. Tinh chỉnh với LoRA, QLoRA, DPO
   - C. Kỹ thuật prompt cơ bản (few-shot, chuỗi suy luận)
   - D. Hệ thống đánh giá sản xuất
   **Đáp án / Answer:** C

   Theo bài giảng, Track 3 phù hợp với người học có đặc điểm nào?
   - A. Thích làm việc với dữ liệu có cấu trúc và SQL thuần túy
   - B. Hứng thú với thiết kế ReAct, gọi công cụ, kiến trúc giám sát-công nhân
   - C. Muốn tập trung vào xử lý ảnh và video với CNN
   - D. Ưu tiên các giải pháp không cần code
   **Đáp án / Answer:** B

   Thách thức nào được nêu rõ khi theo đuổi Track 3?
   - A. Khối lượng nội dung nhẹ, dễ tiếp thu
   - B. Lĩnh vực đã có best practice rõ ràng, không cần thử nghiệm
   - C. Benchmark và evaluation tốn nhiều công sức
   - D. Không yêu cầu đọc tài liệu gốc (bài báo nghiên cứu)
   **Đáp án / Answer:** C

   Vai trò mục tiêu (CP3) mà Track 3 hướng đến là gì?
   - A. Nhà phân tích dữ liệu, Nhà phát triển thông minh kinh doanh
   - B. Kỹ sư AI, Kỹ sư LLM, Nhà phát triển Agent
   - C. Nhà phát triển giao diện, Nhà thiết kế UI/UX
   - D. Kỹ sư DevOps, Kiến trúc sư đám mây
   **Đáp án / Answer:** B

---

Câu hỏi ôn tập Ngày 16

   Điểm yếu chính nào của Single Agent (ReAct) mà Reflexion khắc phục?
   - A. Không thể sử dụng nhiều tool cùng lúc.
   - B. Thiếu khả năng tự đánh giá và backtrack khi gặp lỗi.
   - C. Chi phí tính toán quá cao cho mỗi bước.
   - D. Không hỗ trợ đầu ra có cấu trúc.
   **Đáp án / Answer:** B

   Trong kiến trúc Reflexion, thành phần nào chịu trách nhiệm rút ra bài học từ sai lầm và lưu vào bộ nhớ?
   - A. Tác nhân
   - B. Bộ đánh giá
   - C. Bộ phản chiếu
   - D. Thử lại
   **Đáp án / Answer:** C

   Đặc điểm nổi bật của LATS (Language Agent Tree Search) so với Reflexion là gì?
   - A. Sử dụng Reflection Memory để lưu lỗi.
   - B. Kết hợp MCTS để thử nhiều nhánh giải pháp và có khả năng undo.
   - C. Tự động ghi nhận kỹ năng mới vào thư viện.
   - D. Chỉ phù hợp với các tác vụ đọc dữ liệu.
   **Đáp án / Answer:** B

   Biện pháp an toàn nào được khuyến nghị khi triển khai Single-agent trong production?
   - A. Luôn sử dụng Multi-agent ngay từ đầu.
   - B. Không cần cấu hình max_attempts vì agent tự biết dừng.
   - C. Phân cấp rủi ro, đặt human approval gate cho thao tác nhạy cảm.
   - D. Chỉ dùng unstructured output để linh hoạt.
   **Đáp án / Answer:** C

---

Câu hỏi ôn tập Ngày 17

   Loại bộ nhớ nào trong agent được quản lý trong context window của LLM, có tốc độ truy cập nhanh nhưng bị giới hạn bởi token budget?
   - A. Bộ nhớ dài hạn (Khai báo)
   - B. Bộ nhớ tình huống
   - C. Bộ nhớ ngắn hạn (Làm việc)
   - D. Bộ nhớ ngữ nghĩa
   **Đáp án / Answer:** C

   Trong quy trình quản lý bộ nhớ (Memory Management Flow), bước nào diễn ra ngay sau khi lưu trữ dữ liệu trong bộ đệm (Buffer)?
   - A. Lưu trữ vĩnh viễn (Kho ngoài)
   - B. Trích xuất sự kiện chính
   - C. Tóm tắt (Gọi LLM)
   - D. Truy xuất từ Vector DB
   **Đáp án / Answer:** C

   Tính năng "Privacy-by-Design" trong bộ nhớ agent bao gồm yếu tố nào sau đây?
   - A. Lưu trữ vô thời hạn tất cả dữ liệu người dùng
   - B. Chỉ cho phép truy cập bộ nhớ từ một user duy nhất
   - C. Cơ chế "Quyền được lãng quên" và giới hạn thời gian tồn tại (TTL)
   - D. Mã hóa tất cả dữ liệu bằng vector embeddings
   **Đáp án / Answer:** C

   Xu hướng "Compaction" trong agent memory (2025-2026) đề cập đến việc:
   - A. Mở rộng không giới hạn dung lượng context window
   - B. Nén các phiên họp thành tóm tắt, quyết định và ghi chú bền vững
   - C. Tạo nhiều bản sao dữ liệu để tăng độ tin cậy
   - D. Sử dụng file cấu hình AGENTS.md để kiểm soát truy cập
   **Đáp án / Answer:** B

---

Câu hỏi ôn tập Ngày 18

   Kỹ thuật enrichment nào trong giai đoạn OFFLINE sử dụng LLM để tạo ra các câu hỏi mà một chunk có thể trả lời, sau đó nhúng các câu hỏi đó cùng với chunk?
   - A. Nhúng ngữ cảnh
   - B. Hỏi-Đáp giả định
   - C. Học biểu diễn Matryoshka
   - D. Chunk muộn
   **Đáp án / Answer:** B

   Trong giai đoạn ONLINE, thành phần nào sử dụng Cross-Encoders để sắp xếp lại các chunk đã truy xuất, giúp cải thiện độ chính xác với chi phí độ trễ nhỏ?
   - A. Tiền RAG
   - B. Truy xuất
   - C. Sắp xếp lại
   - D. Tăng cường
   **Đáp án / Answer:** C

   Theo RAGAS, metric nào đo lường mức độ trung thực của câu trả lời (có bám sát nội dung được cung cấp hay không)?
   - A. Độ thu hồi ngữ cảnh
   - B. Độ chính xác ngữ cảnh
   - C. Độ trung thực
   - D. Mức độ liên quan của câu trả lời
   **Đáp án / Answer:** C

   Hạn chế nào của embedding được nhắc đến trong bài giảng, ví dụ như không phân biệt được "allowed" và "not allowed"?
   - A. Hoán đổi thực thể
   - B. Mù thời gian
   - C. Không nhạy cảm với phủ định
   - D. Mù số học
   **Đáp án / Answer:** C

   Kỹ thuật chunking nào xây dựng một cây tóm tắt đệ quy để trả lời các câu hỏi tổng hợp ở mức cao?
   - A. Chunk ngữ nghĩa
   - B. Chunk phân cấp
   - D. Chunk muộn
   **Đáp án / Answer:** C

---

Câu hỏi ôn tập Ngày 19

   Flat RAG (Vector RAG) thường thất bại với loại câu hỏi nào dưới đây?
   - A. Câu hỏi factoid đơn giản nằm trong một tài liệu.
   - B. Câu hỏi yêu cầu suy luận qua nhiều thực thể (multi-hop).
   - C. Câu hỏi về định nghĩa khái niệm cơ bản.
   - D. Câu hỏi trích xuất thông tin từ một đoạn văn ngắn.
   **Đáp án / Answer:** B

   Đơn vị nguyên tử (atomic unit) của Knowledge Graph là gì?
   - A. Nút và Cạnh riêng lẻ.
   - B. Bộ ba (Triple) gồm Chủ thể – Vị ngữ – Tân ngữ.
   - C. Một đồ thị con (Subgraph) bất kỳ.
   - D. Câu văn hoàn chỉnh trong văn bản gốc.
   **Đáp án / Answer:** B

   Trong pipeline GraphRAG tiêu chuẩn, bước nào chuyển đổi subgraph thành dạng văn bản để đưa vào LLM?
   - A. Khớp nút gốc.
   - B. Duyệt đồ thị.
   - C. Văn bản hóa.
   **Đáp án / Answer:** C

   LightRAG cải thiện tốc độ và chi phí so với Microsoft GraphRAG nhờ kiến trúc nào?
   - A. Sử dụng Phát hiện cộng đồng và Tóm tắt phân cấp.
   - B. Truy xuất hai cấp độ với embedding cho cả Node và Edge.
   - C. Duyệt đồ thị với độ sâu tối đa là 3.
   - D. Kết hợp Vector DB và Graph DB qua cơ chế Hybrid Search.
   **Đáp án / Answer:** B

---

Câu hỏi ôn tập Ngày 20

   Khi nào bạn nên cân nhắc chuyển từ một agent duy nhất sang multi-agent system?
   - A. Khi nhiệm vụ cần tương tác với nhiều API bên ngoài.
   - B. Khi một agent đơn lẻ không đạt độ chính xác >80%.
   - C. Khi muốn giảm tổng chi phí vận hành hệ thống.
   - D. Khi cần triển khai mô hình ngôn ngữ lớn hơn.
   **Đáp án / Answer:** B

   Mô hình workflow nào trong số 5 pattern của Anthropic hoạt động bằng cách phân loại đầu vào và chuyển hướng đến handler chuyên biệt nhất?
   - A. Chuỗi Prompt
   - B. Định tuyến
   - C. Điều phối-Công nhân
   - D. Đánh giá-Tối ưu hóa
   **Đáp án / Answer:** B

   Kiến trúc nào thường được dùng để triển khai Supervisor Pattern trong multi-agent system?
   - A. Kiến trúc hình sao
   - B. Kiến trúc lưới
   - C. Kiến trúc trung tâm-nan hoa
   - D. Kiến trúc cây
   **Đáp án / Answer:** C

   Lợi ích chính của việc sử dụng Debate Agents (agents tranh luận) là gì?
   - A. Tăng tốc độ xử lý lên gấp đôi.
   - B. Giảm ảo giác (hallucination) từ 15% đến 25%.
   - C. Giảm chi phí API xuống một nửa.
   - D. Loại bỏ hoàn toàn nhu cầu dùng Judge agent.
   **Đáp án / Answer:** B

   Framework nào trong số sau đây được mô tả là “state machine driven” và phù hợp cho môi trường production cần kiểm soát chặt chẽ?
   **Đáp án / Answer:** C

---

Câu hỏi ôn tập Ngày 21

   Theo bài giảng, trong quy trình chuẩn, khi nào nên chuyển sang Fine-tune thay vì tiếp tục dùng Prompt Engineering và RAG?
   - A. Khi cần thêm kiến thức mới vào mô hình.
   - B. Khi Prompt Engineering và RAG đã hết sức nhưng mô hình vẫn thiếu format chuyên ngành hoặc cần giảm latency/cost ở quy mô lớn.
   - C. Khi số lượng request (req) mỗi ngày dưới 50k.
   - D. Khi tập dữ liệu có trên 10k mẫu.
   **Đáp án / Answer:** B

   LoRA khác với Full Fine-tune ở điểm nào?
   - A. LoRA cập nhật tất cả các tham số của mô hình gốc.
   - B. LoRA đóng băng trọng số gốc và chỉ huấn luyện hai ma trận nhỏ A và B (low-rank).
   - C. LoRA làm tăng độ trễ suy luận (inference latency) do phải tính thêm ma trận.
   - D. LoRA yêu cầu nhiều VRAM hơn Full Fine-tune.
   **Đáp án / Answer:** B

   QLoRA cho phép fine-tune mô hình 7B trên GPU 24GB nhờ kết hợp kỹ thuật nào?
   - A. Chỉ dùng Gradient Checkpointing và FlashAttention.
   - B. Lượng tử hóa (quantization) mô hình gốc xuống 4-bit (NF4) và dùng bộ điều chỉnh bf16 LoRA, kết hợp PagedAdamW.
   - C. Giảm rank của LoRA xuống r=1.
   - D. Nén toàn bộ mô hình xuống còn 2-bit.
   **Đáp án / Answer:** B

   Theo bài giảng, điều nào sau đây là đúng về Dataset khi fine-tune?
   - A. Số lượng mẫu quan trọng hơn chất lượng; 10k mẫu nhiễu vẫn tốt hơn 500 mẫu sạch.
   - B. Cần đảm bảo tập test không nằm trong tập huấn luyện để tránh “Data contamination”.
   - C. Chỉ cần 100 mẫu là đủ cho mọi tác vụ.
   - D. Có thể dùng lại tập test của mô hình gốc mà không cần kiểm tra trùng lặp.
   **Đáp án / Answer:** B

---

Câu hỏi ôn tập Ngày 22

   Trong DPO, khi tăng hyperparameter β (KL penalty), điều gì xảy ra với mô hình sau huấn luyện?
   - A. Mô hình trở nên tự do hơn, ít bám sát SFT base.
   - B. Mô hình bảo thủ hơn, giữ gần với reference model.
   - C. Không ảnh hưởng đến hành vi mô hình.
   - D. Mô hình học nhanh hơn nhưng dễ overfit.
   **Đáp án / Answer:** B

   ORPO khác biệt chính so với DPO ở điểm nào?
   - A. ORPO yêu cầu reward model riêng, DPO thì không.
   - B. ORPO là single-stage alignment, không cần SFT stage.
   - C. ORPO dùng cặp preference, DPO dùng nhãn thumbs up/down.
   - D. ORPO chỉ dùng cho toán học, DPO dùng cho chatbot.
   **Đáp án / Answer:** B

   GRPO (Group Relative Policy Optimization) cải tiến gì so với PPO truyền thống?
   - A. Loại bỏ hoàn toàn mạng value model bằng cách tính reward trung bình của nhóm outputs.
   - B. Thay thế reward model bằng một mạng neural nhỏ hơn.
   - C. Yêu cầu nhiều VRAM hơn nhưng tăng độ chính xác.
   - D. Chỉ dùng cho tác vụ code, không dùng cho reasoning.
   **Đáp án / Answer:** A

   Benchmark nào sau đây dùng LLM-as-Judge để đánh giá chất lượng phản hồi (response quality) trong alignment?
   **Đáp án / Answer:** C

---

Câu hỏi ôn tập Ngày 23

   Khi nào một pipeline tuyến tính (LCEL) không còn đủ cho agent?
   - A. Khi chỉ cần một luồng xử lý đơn giản, không có rẽ nhánh.
   - B. Khi agent cần loop retry, human-in-the-loop, dynamic routing và crash recovery.
   - C. Khi số lượng tool nhỏ hơn 5.
   - D. Khi không cần checkpointing.
   **Đáp án / Answer:** B

   Trong LangGraph, reducer được dùng để làm gì?
   - A. Xác định node nào chạy tiếp theo.
   - B. Merge state khi cập nhật, ví dụ append cho message history.
   - C. Tạo checkpoint sau mỗi bước.
   - D. Gọi tool bên ngoài.
   **Đáp án / Answer:** B

   Tính năng "Time Travel" trong LangGraph cho phép làm gì?
   - A. Chạy song song nhiều graph cùng lúc.
   - B. Replay lại từ một checkpoint bất kỳ để debug hoặc thử hướng đi khác.
   - C. Tự động retry node bị lỗi.
   - D. Gửi thông báo cho người dùng khi hoàn thành.
   **Đáp án / Answer:** B

   Để tạm dừng graph chờ con người phê duyệt, ta sử dụng hàm nào?
   **Đáp án / Answer:** A

---

Câu hỏi ôn tập Ngày 24

   RAGAS sử dụng chỉ số nào để đo lường mức độ hỗ trợ của ngữ cảnh cho câu trả lời (hallucination nội tại)?
   - A. Độ thu hồi ngữ cảnh
   - B. Mức độ liên quan của câu trả lời
   - C. Độ trung thực
   - D. Độ chính xác ngữ cảnh
   **Đáp án / Answer:** C

   Khi sử dụng LLM-as-Judge, bias nào được khắc phục bằng phương pháp "swap-and-average"?
   - A. Thiên lệch độ dài
   - B. Thiên lệch vị trí
   - C. Thiên lệch tự khuếch đại
   - D. Thiên lệch phong cách
   **Đáp án / Answer:** B

   Trong kiến trúc Guardrails, lớp nào chịu trách nhiệm phát hiện prompt injection và kiểm tra chủ đề (topic scope) với độ trễ dưới 30ms?
   - A. Lớp đầu vào L1
   - B. Lớp LLM L2
   - C. Lớp đầu ra L3
   - D. Lớp kiểm toán L4
   **Đáp án / Answer:** A

   Kỹ thuật nào sau đây phát hiện hallucination bằng cách lấy mẫu nhiều câu trả lời với temperature > 0 và đo độ nhất quán?
   - B. Entropy ngữ nghĩa
   **Đáp án / Answer:** C

---

Câu hỏi ôn tập Ngày 25

   Khi hệ thống LLM agent gặp lỗi 429 (Rate Limit) hoặc 500 (Internal Server Error) từ provider, đó thuộc failure mode nào?
   - A. Lỗi công cụ/bộ nhớ đệm
   - B. Hành động kinh doanh sai
   - C. Lỗi tạm thời từ nhà cung cấp
   - D. Vòng lặp điều phối
   **Đáp án / Answer:** C

   Circuit Breaker ở trạng thái nào cho phép thực hiện một probe call để kiểm tra recovery?
   - A. ĐÓNG
   - B. MỞ
   - C. MỞ MỘT NỬA
   - D. HỎNG
   **Đáp án / Answer:** C

   Trong fallback ladder, bước nào thường được thực hiện trước khi dùng cached response?
   - A. Mô hình tốt nhất
   - B. Nhà cung cấp dự phòng
   - C. Mô hình rẻ hơn/nhỏ hơn
   - D. Thông báo dự phòng tĩnh
   **Đáp án / Answer:** C

   Khi semantic cache có similarity > threshold, hành động đúng là gì?
   - A. Gọi LLM và lưu kết quả mới
   - B. Trả về kết quả cached
   - C. Đặt lại ngưỡng
   - D. Ghi log lỗi
   **Đáp án / Answer:** B

   SLI (Service Level Indicator) được định nghĩa trong bài giảng là gì?
   - A. Cam kết bên ngoài với khách hàng
   - B. Chỉ tiêu nội bộ về chất lượng
   - C. Metric đo lường thực tế (ví dụ: P95 latency)
   - D. Ngân sách lỗi cho phép
   **Đáp án / Answer:** C

---

Câu hỏi ôn tập Ngày 26

   Vấn đề N×M trong tích hợp công cụ LLM được giải quyết như thế nào bởi MCP?
   - A. Bằng cách yêu cầu mỗi nhà cung cấp LLM viết adapter riêng.
   - B. Bằng cách giới thiệu một giao thức chuẩn, giảm độ phức tạp từ N×M xuống N+M.
   - C. Bằng cách loại bỏ hoàn toàn nhu cầu sử dụng công cụ bên ngoài.
   - D. Bằng cách chỉ hỗ trợ một nhà cung cấp LLM duy nhất.
   **Đáp án / Answer:** B

   Trong kiến trúc MCP, thành phần nào chịu trách nhiệm cung cấp các hàm có thể gọi được (callable functions) cho LLM quyết định sử dụng?
   - A. Tài nguyên
   - B. Lời nhắc
   - C. Công cụ
   - D. Gốc
   **Đáp án / Answer:** C

   Khi xây dựng MCP Server bằng FastMCP, yếu tố nào được nhấn mạnh là quan trọng nhất để LLM quyết định gọi tool chính xác?
   - A. Tên hàm và kiểu dữ liệu đầu vào.
   - B. Mô tả tool (docstring) rõ ràng.
   - C. Số lượng tham số của hàm.
   - D. Tốc độ xử lý của server.
   **Đáp án / Answer:** B

   Để bảo mật MCP Server từ xa (remote), giao thức nào bắt buộc phải được sử dụng?
   - A. HTTP không mã hóa.
   - B. SSH với private key.
   - C. OAuth 2.0 và TLS.
   - D. Chỉ cần xác thực qua API key.
   **Đáp án / Answer:** C

   Theo best practices của Claude Code, nên ưu tiên thiết kế luồng nào trước khi thực hiện các thay đổi (mutations)?
   - A. Luồng ghi (write) để tác động nhanh.
   - B. Luồng đọc/tìm kiếm (search/read) để lấy ngữ cảnh chính xác.
   - C. Luồng xóa (delete) để dọn dẹp dữ liệu.
   - D. Luồng cập nhật (update) để đồng bộ ngay lập tức.
   **Đáp án / Answer:** B

---

Câu hỏi ôn tập Ngày 27

   Theo bài giảng, khái niệm "Bounded Autonomy" trong HITL có nghĩa là gì?
   - A. Agent hoàn toàn tự động, không cần sự can thiệp của con người
   - B. Agent có thể tự động thực hiện mọi hành động nhưng phải ghi log lại
   - C. Agent tự động trong các ranh giới an toàn (đọc/tìm kiếm) và phải xin phép khi vượt ranh giới rủi ro
   - D. Agent chỉ được thực hiện các hành động đã được phê duyệt trước
   **Đáp án / Answer:** C

   Khi nào agent nên ngắt quãng (interrupt) để hỏi ý kiến con người, theo nguyên tắc Confidence Routing?
   - A. Khi confidence score của agent dưới 50%
   - B. Khi hành động có thể đảo ngược (reversible) và gây ảnh hưởng bên ngoài
   - C. Khi hành động có thể đảo ngược, ưu tiên tự động; nếu có tác động bên ngoài hoặc thiếu thông tin thì cần review/phê duyệt
   - D. Chỉ ngắt khi agent không chắc chắn về kết quả
   **Đáp án / Answer:** C

   Trong 6 mẫu tương tác HITL, pattern nào được sử dụng khi agent cần con người kiểm tra bản nháp đầu ra (ví dụ: code PR, email nháp)?
   - A. Phê duyệt
   - B. Làm rõ
   - C. Điểm kiểm tra đánh giá
   **Đáp án / Answer:** C

   Theo best practices của HITL UX, khi nào nên hỏi con người để giảm tải nhận thức?
   - A. Luôn hỏi sớm cho mọi hành động
   - B. Hỏi sớm cho dữ liệu thiếu, hỏi muộn cho hành động không thể đảo ngược
   - C. Chỉ hỏi khi hành động có rủi ro cao
   - D. Hỏi muộn cho mọi hành động để tránh làm phiền
   **Đáp án / Answer:** B

---

Câu hỏi ôn tập Ngày 28

   Theo bài giảng, nguyên tắc chọn value metric cho AI pricing dựa trên hai yếu tố nào?
   - A. Chi phí API và chi phí nhân sự
   - B. Attribution (khả năng đo lường kết quả) và Autonomy (tự động hóa)
   - C. Số lượng người dùng và doanh thu trung bình
   - D. Loại mô hình và chi phí suy luận
   **Đáp án / Answer:** B

   Khi xác định giá bán (floor price) cho sản phẩm AI, chi phí tối thiểu cho một job bao gồm tất cả các yếu tố sau, **ngoại trừ**:
   - A. Chi phí API
   - B. Chi phí hạ tầng
   - C. Chi phí marketing
   - D. Chi phí HITL (Human-In-The-Loop)
   **Đáp án / Answer:** C

   Quy tắc cốt lõi của Go-To-Market (GTM) cho AI là gì?
   - A. Tạo giao diện hoàn toàn mới để gây ấn tượng
   - B. Không bắt người dùng mở tab mới hoặc học workflow mới
   - C. Ưu tiên kênh Sales-Led cho mọi sản phẩm
   - D. Tập trung vào demo ấn tượng trước khi có bằng chứng
   **Đáp án / Answer:** B

   Theo bài giảng, "ARPU-CAC Dead Zone" là khoảng ARPU nào gây khó khăn vì không phù hợp với cả self-serve lẫn sales team?
   - A. Dưới $50
   - B. Trên $1000
   - C. Từ $50 đến $1000
   - D. Từ $1000 đến $5000
   **Đáp án / Answer:** C
