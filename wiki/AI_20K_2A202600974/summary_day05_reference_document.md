---
type: summary
title: "Summary of Day 5 Reference Document: AI Product Design for Probabilities"
description: "A detailed summary of the Day 5 reference document from VinUni A20 on designing AI products for uncertainty, including frameworks, case studies, and UX/eval best practices."
tags: [AI product, product management, uncertainty, UX, evaluation, metrics]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/5/05-reference-document.pdf"]
---

# Summary of Day 5 Reference Document: AI Product Design for Probabilities
# Tóm tắt Tài liệu Tham khảo Ngày 5: Thiết kế Sản phẩm AI cho các Xác suất

This document serves as the main reference for Day 5 of the VinUni A20 AI in Action course. It emphasizes that AI outputs are probabilistic (probabilities with margins of error), not exact results. Designing for AI means designing for uncertainty.
Tài liệu này đóng vai trò là tài liệu tham khảo chính cho Ngày 5 của khóa học VinUni A20 AI in Action. Tài liệu nhấn mạnh rằng kết quả đầu ra của AI là có tính xác suất (xác suất với sai số), không phải là kết quả chính xác tuyệt đối. Thiết kế cho AI có nghĩa là thiết kế cho sự không chắc chắn.

## 1. Key Frameworks & Models
## 1. Các Khung & Mô hình Chính

### Core Frameworks
### Các Khung Cốt lõi
- **AI = Probabilistic**: AI outputs are probabilities with margins of error. Products must be designed to handle this uncertainty gracefully.
- **AI = Có tính xác suất**: Kết quả đầu ra của AI là các xác suất với sai số. Các sản phẩm phải được thiết kế để xử lý sự không chắc chắn này một cách khéo léo.
- **Automation vs. Augmentation**: Two main deployment paths. Automation acts on behalf of the user, while augmentation suggests actions for the user to decide. Choosing incorrectly cascades to all future product decisions.
- **Tự động hóa vs. Tăng cường**: Hai con đường triển khai chính. Tự động hóa hành động thay cho người dùng, trong khi tăng cường đề xuất các hành động để người dùng quyết định. Lựa chọn sai sẽ ảnh hưởng đến tất cả các quyết định sản phẩm trong tương lai.
- **Agency Progression (V1 → V3)**: Start with augmentation and gradually move to automation. (e.g., V1: routing -> V2: copilot -> V3: automatic). Each step collects data for the next.
- **Tiến trình Đại diện (V1 → V3)**: Bắt đầu với việc tăng cường và dần chuyển sang tự động hóa. (ví dụ: V1: định tuyến -> V2: trợ lý ảo -> V3: tự động). Mỗi bước thu thập dữ liệu cho bước tiếp theo.
- **Three Pillars (Requirement, UX, Eval)**: AI changes these core areas. Requirements need thresholds and failure modes; UX must handle errors gracefully; Eval must measure quality distribution rather than binary pass/fail.
- **Ba Trụ cột (Yêu cầu, UX, Đánh giá)**: AI thay đổi các lĩnh vực cốt lõi này. Yêu cầu cần có các ngưỡng và các chế độ lỗi; UX phải xử lý lỗi một cách khéo léo; Đánh giá phải đo lường sự phân phối chất lượng thay vì chỉ là đạt/trượt (nhị phân).
- **Failure Mode Library**: Instead of listing features, list how the product can fail (Trigger / Impact / Mitigation).
- **Thư viện Chế độ Lỗi**: Thay vì liệt kê các tính năng, hãy liệt kê cách sản phẩm có thể bị lỗi (Kích hoạt / Tác động / Giảm thiểu).
- **Precision vs. Recall**: Product Managers must choose between high precision (fewer false positives) or high recall (fewer false negatives) depending on the "cost of error" for their product.
- **Độ chuẩn xác (Precision) vs. Độ bao phủ (Recall)**: Các Giám đốc Sản phẩm (Product Managers) phải chọn giữa độ chuẩn xác cao (ít dương tính giả) hoặc độ bao phủ cao (ít âm tính giả) tùy thuộc vào "chi phí của lỗi" đối với sản phẩm của họ.
- **4 Paths UX for AI**: What happens when AI is right (value moment)? When it's low-confidence (escalate)? When it's wrong (correction path)? When trust is lost (explain & opt-out)?
- **4 Con đường UX cho AI**: Điều gì xảy ra khi AI đúng (khoảnh khắc giá trị)? Khi độ tin cậy thấp (leo thang)? Khi sai (con đường sửa lỗi)? Khi mất niềm tin (giải thích & chọn không tham gia)?
- **Graceful Failure + Trust**: UX design must account for AI errors. Show confidence levels, explain why, allow users to correct the output, and provide an opt-out.
- **Thất bại Khéo léo + Niềm tin**: Thiết kế UX phải tính đến các lỗi của AI. Hiển thị mức độ tin cậy, giải thích lý do, cho phép người dùng sửa kết quả đầu ra và cung cấp tùy chọn không tham gia.
- **AI Product Canvas**: A 3-column canvas (Value, Trust, Feasibility) plus a Learning Signal row, merging requirements, UX, and evaluation into one artifact.
- **Khung Sản phẩm AI**: Một khung gồm 3 cột (Giá trị, Niềm tin, Tính khả thi) cộng với một hàng Tín hiệu Học tập, hợp nhất các yêu cầu, UX và đánh giá thành một cấu trúc.
- **Feedback Loop & Data Flywheel**: An AI product is an organism. The loop is: Ingest → Digest → Output → Repeat. Model capabilities are commoditized; proprietary data is the true moat.
- **Vòng lặp Phản hồi & Bánh đà Dữ liệu**: Sản phẩm AI là một sinh vật. Vòng lặp là: Tiêu hóa → Hấp thụ → Xuất ra → Lặp lại. Khả năng của mô hình đang bị thương mại hóa; dữ liệu độc quyền mới là con hào bảo vệ thực sự.

### External Frameworks
### Các Khung Bên ngoài
- **Reforge - AI Product Management Course**: The source of many strategy frameworks like "Four Critical AI Product Strategy Mistakes," "Cost-Capability-Speed," and "AI Feature Map."
- **Reforge - Khóa học Quản lý Sản phẩm AI**: Nguồn của nhiều khung chiến lược như "Bốn Sai lầm Quan trọng trong Chiến lược Sản phẩm AI," "Chi phí-Khả năng-Tốc độ," và "Bản đồ Tính năng AI."
- **Zwee Dao - AI Product Design Series**: Source for UX frameworks on automation/augmentation, graceful failure, and explainability.
- **Zwee Dao - Chuỗi bài Thiết kế Sản phẩm AI**: Nguồn cho các khung UX về tự động hóa/tăng cường, thất bại khéo léo và khả năng giải thích.

## 2. Case Studies
## 2. Các Nghiên cứu Điển hình (Case Studies)

- **Google AI Overview vs. Perplexity**: Same tech but different product strategy. Google "sprinkled AI" on search, causing errors, while Perplexity built a new product around it.
- **Tổng quan về Google AI vs. Perplexity**: Cùng một công nghệ nhưng chiến lược sản phẩm khác nhau. Google "rắc AI" vào tìm kiếm, gây ra lỗi, trong khi Perplexity xây dựng một sản phẩm mới xoay quanh nó.
- **Chegg**: Disrupted by ChatGPT. Although Chegg had data, they didn't leverage it as an AI advantage. Quizlet pivoted better.
- **Chegg**: Bị gián đoạn bởi ChatGPT. Mặc dù Chegg có dữ liệu, họ đã không tận dụng nó như một lợi thế AI. Quizlet đã chuyển hướng tốt hơn.
- **GitHub Copilot**: Even with only 30% accuracy, it has 20 million users because the "cost of rejection" is practically zero (just keep typing). An example of speed-first ROI.
- **GitHub Copilot**: Ngay cả khi độ chính xác chỉ 30%, nó vẫn có 20 triệu người dùng vì "chi phí từ chối" gần như bằng không (chỉ cần tiếp tục gõ). Một ví dụ về ROI ưu tiên tốc độ.
- **Harvey**: Legal AI where errors can lose a case. Needs high precision. High cost but clients accept it due to the value. Capability-first ROI.
- **Harvey**: AI pháp lý nơi các lỗi có thể làm thua một vụ kiện. Cần độ chuẩn xác cao. Chi phí cao nhưng khách hàng chấp nhận vì giá trị mang lại. ROI ưu tiên khả năng.
- **Microsoft Tay**: Lacked a failure design and turned into a racist bot. Shows the necessity of the "when AI is wrong" UX path.
- **Microsoft Tay**: Thiếu thiết kế cho sự cố thất bại và biến thành một bot phân biệt chủng tộc. Cho thấy sự cần thiết của con đường UX "khi AI sai".
- **Descript**: Tied AI quality to pricing tiers. Quality is a spectrum, not binary.
- **Descript**: Gắn chất lượng AI với các mức giá. Chất lượng là một dải quang phổ, không phải là nhị phân.
- **Microsoft Dragon**: AI for medical scribes. Transitioned from synthetic data (30-60% acceptance) to real data (75-83% acceptance). Real data creates a powerful flywheel.
- **Microsoft Dragon**: AI cho thư ký y khoa. Chuyển từ dữ liệu tổng hợp (tỷ lệ chấp nhận 30-60%) sang dữ liệu thực (tỷ lệ chấp nhận 75-83%). Dữ liệu thực tạo ra một bánh đà mạnh mẽ.
- **Customer Support Agent V1→V3**: A team tried to jump straight to V3 (automation) and failed due to errors. They had to step back and progress from augmentation to automation using collected data.
- **Trợ lý Hỗ trợ Khách hàng V1→V3**: Một nhóm đã cố gắng nhảy thẳng lên V3 (tự động hóa) và thất bại do lỗi. Họ đã phải lùi lại và tiến triển từ tăng cường sang tự động hóa bằng cách sử dụng dữ liệu đã thu thập.

## 3. Core Principles
## 3. Các Nguyên tắc Cốt lõi

1. **AI is not standard software**: Requirements, UX, and Evals must be approached differently.
1. **AI không phải là phần mềm tiêu chuẩn**: Yêu cầu, UX và Đánh giá phải được tiếp cận một cách khác biệt.
2. **Design for Uncertainty**: If your product uses AI, you are designing for uncertainty.
2. **Thiết kế cho sự Không chắc chắn**: Nếu sản phẩm của bạn sử dụng AI, bạn đang thiết kế cho sự không chắc chắn.
3. **Deployment Strategy**: Different deployment strategies (Copilot vs. Spam filter) yield opposite results with the same AI.
3. **Chiến lược Triển khai**: Các chiến lược triển khai khác nhau (Trợ lý ảo vs. Bộ lọc thư rác) mang lại kết quả trái ngược nhau với cùng một AI.
4. **The Last 20%**: Getting from 0 to 80% takes a week; 80 to 95% takes 4x the effort. A demo is not a product.
4. **20% Cuối cùng**: Đi từ 0 đến 80% mất một tuần; 80 đến 95% tốn nỗ lực gấp 4 lần. Một bản demo không phải là một sản phẩm.
5. **Failure over Features**: List failure modes instead of features.
5. **Thất bại quan trọng hơn Tính năng**: Liệt kê các chế độ lỗi thay vì các tính năng.
6. **Visibility of Errors**: If users don't see the error, prioritize precision. If they see it immediately, recall might be okay.
6. **Khả năng Hiển thị Lỗi**: Nếu người dùng không thấy lỗi, hãy ưu tiên độ chuẩn xác. Nếu họ thấy ngay lập tức, độ bao phủ có thể là chấp nhận được.
7. **Data Flywheel**: Models are commodities; proprietary data is the real advantage.
7. **Bánh đà Dữ liệu**: Các mô hình đang bị thương mại hóa; dữ liệu độc quyền mới là lợi thế thực sự.
8. **Constant Evolution**: Today's model is the worst model you will ever use.
8. **Sự Tiến hóa Không ngừng**: Mô hình của ngày hôm nay là mô hình tồi tệ nhất bạn từng sử dụng (so với tương lai).
9. **The Loop is the Product**: The feedback loop is the core IP.
9. **Vòng lặp là Sản phẩm**: Vòng lặp phản hồi là cốt lõi của tài sản trí tuệ (IP).
10. **The Utility Equation**: Intelligence × Context × UI = Utility. If any factor is zero, utility is zero.
10. **Phương trình Tiện ích**: Trí thông minh × Ngữ cảnh × Giao diện = Tiện ích. Nếu bất kỳ yếu tố nào bằng 0, tiện ích sẽ bằng 0.
11. **Qualitative > Quantitative**: An 87% accuracy metric can hide crucial flaws. Understand WHERE and WHY the AI fails.
11. **Định tính > Định lượng**: Một số liệu độ chính xác 87% có thể che giấu các sai sót nghiêm trọng. Hãy hiểu AI thất bại ở ĐÂU và TẠI SAO.

## 4. Further Reading & Resources
## 4. Đọc thêm & Tài nguyên

The document lists additional resources for AI Product Management, Precision/Recall & Eval, UX for AI, PRD templates, Feedback Loops, ROI measurement, and Automation vs. Augmentation. Notable mentions include Lenny's Podcast interviews, Google's PAIR Guidebook, a16z reports, and Stanford HAI research.
Tài liệu liệt kê các tài nguyên bổ sung về Quản lý Sản phẩm AI, Độ chuẩn xác/Độ bao phủ & Đánh giá, UX cho AI, các mẫu PRD (Tài liệu Yêu cầu Sản phẩm), Vòng lặp Phản hồi, Đo lường ROI, và Tự động hóa vs. Tăng cường. Các đề cập đáng chú ý bao gồm các cuộc phỏng vấn trên Lenny's Podcast, Hướng dẫn PAIR của Google, báo cáo của a16z và nghiên cứu của Stanford HAI.
