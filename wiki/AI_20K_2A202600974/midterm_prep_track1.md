---
type: concept
title: "Midterm Exam Preparation - Track 1 (Business/PM)"
description: "Bộ tài liệu và câu hỏi ôn tập thi giữa kỳ Chương trình Phát triển Năng lực AI Thực Chiến dành cho Track 1 (Business/Product)"
tags: [ai, 20k, exam, prep, track1]
timestamp: 2026-07-06
sources: ["wiki/AI_20K_2A202600974/day15_track1.md", "wiki/AI_20K_2A202600974/day16_track1.md", "wiki/AI_20K_2A202600974/day17_track1.md", "wiki/AI_20K_2A202600974/day19_track1.md", "wiki/AI_20K_2A202600974/day21_track1.md", "wiki/AI_20K_2A202600974/day24_track1.md"]
---

# BỘ ÔN TẬP THI GIỮA KỲ — TRACK 1 (BUSINESS / PM)

Tài liệu này tổng hợp kiến thức trọng tâm và các dạng câu hỏi ôn tập chuyên sâu (Trắc nghiệm, Multi-select, Scenario Debug, Case Study) bám sát phần thi của **Track 1: Business / Product Management / BA** trong kỳ thi giữa kỳ.

---

## PHẦN I: KIẾN THỨC TRỌNG TÂM TRACK 1

### 1. AI Product Management vs Traditional PM
* **Hệ thống xác suất (Probabilistic):** Sản phẩm AI mang tính bất định cao (không có kết quả đúng 100%). PM cần thiết kế sản phẩm đối phó với sự sai sót của AI thông qua cơ chế *Feedback Loop* và hiệu chuẩn niềm tin của người dùng (*Trust Calibration*).
* **Vòng phản hồi dữ liệu (Data Flywheel):** 
  `Người dùng sử dụng` -> `Tạo ra dữ liệu thực tế` -> `Mô hình được huấn luyện lại` -> `AI thông minh hơn` -> `Thu hút thêm người dùng`.
* **Trust Calibration (Hiệu chuẩn niềm tin):**
  * *Overtrust (Quá tin tưởng):* Dẫn đến người dùng lười kiểm tra, gây ra rủi ro nghiêm trọng khi AI ảo giác.
  * *Undertrust (Thiếu tin tưởng):* Người dùng bỏ qua sản phẩm AI vì nghĩ nó không đáng tin.
  * *Giải pháp:* Thiết kế UX giải thích lý do (explainability), hiển thị độ tự tin (confidence score), và luôn có nút để người dùng chỉnh sửa kết quả.

### 2. Phát triển sản phẩm giai đoạn đầu (Prototyping & MVP)
* **Wizard of Oz MVP:** Kỹ thuật giả lập hệ thống AI. Khách hàng tương tác với giao diện bên ngoài trông như AI tự động, nhưng thực tế đằng sau là con người xử lý thủ công (HITL) để test nhu cầu thị trường trước khi bỏ chi phí huấn luyện mô hình.
* **JTBD (Jobs-To-Be-Done):** Tập trung vào động cơ của người dùng. Người dùng không mua "mô hình AI 70B parameters", họ mua giải pháp giải quyết một "công việc" cụ thể (Job) nhanh gấp 10 lần.

### 3. Chỉ số đo lường hiệu quả (Metrics & ROI)
* **ROI (Return on Investment) của AI:** 
  $$\text{ROI} = \frac{\text{Giá trị tăng thêm (Tiết kiệm thời gian, Tăng doanh thu)} - \text{Chi phí AI (Token, GPU, Nhân sự, Bảo trì)}}{\text{Chi phí AI}}$$
* **RICE Prioritization:** Phương pháp ưu tiên tính năng dựa trên:
  * *Reach (Độ phủ)*
  * *Impact (Tác động)*
  * *Confidence (Độ tự tin về kỹ thuật/thị trường)*
  * *Effort (Nỗ lực phát triển - đo bằng man-months).*
* **Habit Loop & Hook Model:** Áp dụng thiết kế Agent để giữ chân người dùng thông qua: *Trigger (Kích hoạt)* -> *Action (Hành động)* -> *Variable Reward (Phần thưởng thay đổi)* -> *Investment (Đầu tư lại dữ liệu)*.

### 4. Pháp lý & Đạo đức AI (AI Regulations & Ethics)
* **EU AI Act:** Phân loại rủi ro của hệ thống AI thành 4 cấp độ:
  1. *Unacceptable Risk (Không thể chấp nhận):* Chấm điểm xã hội (Social scoring), nhận diện khuôn mặt hàng loạt nơi công cộng -> **CẤM**.
  2. *High Risk (Rủi ro cao):* Tuyển dụng, y tế, chấm điểm tín dụng -> **Yêu cầu tuân thủ nghiêm ngặt (Audit, Data governance, Human oversight)**.
  3. *Limited Risk (Rủi ro hạn chế):* Chatbot, sinh nội dung (Generative AI) -> **Yêu cầu minh bạch (phải thông báo cho người dùng biết họ đang chat với AI)**.
  4. *Minimal Risk (Rủi ro tối thiểu):* Bộ lọc spam, game -> **Tự do phát triển**.
* **Luật TTNT Việt Nam (Bản thảo):** Tập trung vào việc bảo vệ chủ quyền dữ liệu, an ninh thông tin, và quy định trách nhiệm của nhà phát triển mô hình lớn.

### 5. Quản trị dự án & Đội ngũ AI
* **RACI Matrix:** 
  * *Responsible (Người thực hiện trực tiếp)*
  * *Accountable (Người chịu trách nhiệm cuối cùng - chỉ có 1)*
  * *Consulted (Người được tham vấn ý kiến)*
  * *Informed (Người được nhận thông báo)*
* **Agentic SDLC:** Quy trình phát triển phần mềm có sự tham gia của AI Agents ở các khâu lập trình, kiểm thử và viết tài liệu.

---

## CÂU HỎI ÔN TẬP THỰC CHIẾN (TRACK 1)

### Dạng 1: Trắc nghiệm & Multi-Select

#### Câu 1 (Multi-select): Doanh nghiệp tuyển dụng A muốn ứng dụng AI để tự động quét CV và xếp hạng ứng viên trước khi chuyển cho bộ phận HR. Theo EU AI Act, ứng dụng này thuộc nhóm rủi ro nào và cần tuân thủ những gì? (Chọn tất cả các đáp án đúng)
- [x] A. Thuộc nhóm High Risk (Rủi ro cao).
- [ ] B. Thuộc nhóm Unacceptable Risk (Không thể chấp nhận) và bị cấm hoàn toàn.
- [x] C. Cần phải có quy trình giám sát của con người (Human Oversight) trước khi đưa ra quyết định từ chối ứng viên.
- [x] D. Phải thực hiện đánh giá chất lượng dữ liệu đầu vào chống thiên vị (bias) đối với các nhóm giới tính, sắc tộc.

*Giải thích:* Ứng dụng AI trong tuyển dụng/quản lý nhân sự thuộc nhóm High Risk (A), yêu cầu bắt buộc phải có Human Oversight (C) và rà soát Bias dữ liệu đầu vào (D).

#### Câu 2 (Single choice): Phương pháp "Wizard of Oz" trong giai đoạn làm MVP sản phẩm AI nhằm mục đích chính là gì?
- ( ) A. Huấn luyện mô hình học máy nhỏ hoạt động tốt hơn trước khi nâng cấp lên LLM.
- (x) B. Giả lập tính năng của AI bằng con người để kiểm chứng nhu cầu thực sự của khách hàng trước khi đầu tư kỹ thuật.
- ( ) C. Tự động hóa hoàn toàn quy trình xử lý dữ liệu đầu vào cho mô hình RAG.
- ( ) D. Tăng độ tin tưởng (overtrust) của người dùng vào tính năng của sản phẩm.

*Giải thích:* Wizard of Oz là phương pháp giả lập AI bằng con người ở back-end để validate thị trường nhanh và rẻ.

---

### Dạng 2: Scenario Debug (Case Study xử lý lỗi sản phẩm)

#### Tình huống:
Một startup ra mắt công cụ viết email bán hàng tự động cho nhân viên Sales. Hệ thống sinh email tự động và tự gửi đi sau 3 giây nếu người dùng không bấm nút "Hủy".
Sau 2 tuần ra mắt, tỷ lệ hủy kích hoạt sản phẩm (Churn rate) lên tới 65%. Nhân viên Sales phản nàn rằng AI viết email quá sáo rỗng, đôi khi bị sai lệch thông tin sản phẩm (ảo giác) dẫn tới mất khách hàng VIP, và họ cảm thấy không kiểm soát được những gì hệ thống gửi đi.

#### Câu hỏi phân tích:
1. **Lỗi thiết kế UX/AI** nào đã xảy ra trong sản phẩm trên khiến người dùng quay lưng?
2. **Đề xuất giải pháp sửa đổi** cụ thể cho PM để khắc phục tình trạng này.

#### Lời giải đề xuất:
1. **Phân tích lỗi:**
   * *Thiếu cơ chế Kiểm soát (Lack of Agency):* Thiết kế tự động gửi sau 3 giây tước đi quyền kiểm soát của người dùng, bắt họ phải luôn canh chừng nút hủy.
   * *Mắc bẫy Overtrust / Thiếu Trust Calibration:* Hệ thống mặc định AI viết đúng 100% và tự gửi đi, trong khi LLM có tỷ lệ ảo giác cao.
   * *Thiếu Feedback Loop:* Không cho phép người dùng chỉnh sửa trực tiếp trên giao diện để lưu lại làm dữ liệu huấn luyện cho lần sau.
2. **Giải pháp khắc phục:**
   * *Chuyển từ Autopilot sang Copilot (HITL):* Bỏ cơ chế tự động gửi. AI sinh email nháp (Draft), hiển thị trên trình biên tập để nhân viên Sales kiểm tra, chỉnh sửa thủ công và chủ động bấm nút "Gửi".
   * *Confidence Score:* Hiển thị mức độ tự tin của AI đối với các phần số liệu được trích xuất.
   * *Edit In-place & Feedback:* Lưu lại các phần người dùng chỉnh sửa nhiều nhất để tinh chỉnh (Fine-tune) mô hình cho phong cách viết phù hợp hơn với thương hiệu của doanh nghiệp.

---

### Dạng 3: Case Study Thiết kế AI Roadmap & ROI

#### Đề bài:
Doanh nghiệp bán lẻ Y muốn triển khai hệ thống AI hỗ trợ khách hàng. PM đề xuất 2 phương án:
* **Option A:** Xây dựng hệ thống RAG tra cứu chính sách mua hàng và trả lời câu hỏi cơ bản của khách. Chi phí ban đầu là 10.000 USD, vận hành 200 USD/tháng. Dự kiến tiết kiệm 2.000 man-hours/năm cho phòng hỗ trợ (trị giá 12.000 USD/năm).
* **Option B:** Huấn luyện một mô hình riêng chuyên biệt tự động trả lời và thực hiện hoàn tiền tự động qua API. Chi phí huấn luyện và tích hợp ban đầu là 80.000 USD, vận hành 1.000 USD/tháng. Dự kiến tiết kiệm 40.000 USD/năm.

#### Hãy đóng vai trò PM và thực hiện:
1. Tính ROI sau 1 năm cho cả 2 Option.
2. Vẽ ma trận ưu tiên (RICE hoặc Impact vs Effort) và đưa ra quyết định chọn phương án nào cho Roadmap quý tiếp theo (Now/Next/Later).

#### Lời giải đề xuất:
1. **Tính toán ROI sau 1 năm:**
   * **Option A (RAG):**
     * Tổng chi phí năm 1: $10.000 + (200 \times 12) = 12.400$ USD.
     * Giá trị mang lại: $12.000$ USD.
     * ROI năm 1: \(\frac{12.000 - 12.400}{12.400} \approx -3.2\%\) (Gần như hòa vốn ngay năm đầu).
   * **Option B (Fine-tuning & API Integration):**
     * Tổng chi phí năm 1: $80.000 + (1.000 \times 12) = 92.000$ USD.
     * Giá trị mang lại: $40.000$ USD.
     * ROI năm 1: \(\frac{40.000 - 92.000}{92.000} \approx -56.5\%\) (Lỗ nặng trong năm đầu, cần ít nhất 3 năm mới hòa vốn đầu tư ban đầu).
2. **Quyết định lộ trình (Roadmap Decision):**
   * **Option A** có *Impact trung bình* nhưng *Effort cực kỳ thấp* (tự tin kỹ thuật cao, triển khai trong 2-4 tuần). Nên xếp vào danh mục **NOW** (Làm ngay lập tức để lấy Quick-win).
   * **Option B** có *Impact rất lớn* nhưng đòi hỏi *Effort rất cao* (8-12 tuần phát triển, rủi ro tích hợp API thanh toán). Nên xếp vào danh mục **NEXT** hoặc **LATER** sau khi Option A đã vận hành ổn định và chứng minh được giá trị dữ liệu tích lũy từ người dùng.
