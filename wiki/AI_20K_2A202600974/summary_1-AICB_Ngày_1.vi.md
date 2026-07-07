---
type: summary
title: "Summary: AICB Day 1 - AI & LLM Foundation"
description: "A comprehensive overview of AI evolution, LLM fundamentals, Transformer architecture, token economy, and practical API usage."
tags: [AI, LLM, Transformer, Token Economy, API, VibeCoding, Agentic AI]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/1/1-AICB_Ngày_1.pdf"]
---
*# AICB Ngày 1 - Nền tảng AI & LLM*

*## 1. Tổng quan và Sự tiến hóa của AI*
*Bài giảng bao quát sự chuyển tiếp của Trí tuệ Nhân tạo qua nhiều giai đoạn, làm nổi bật sự chuyển dịch từ Học máy (Machine Learning) và Học sâu (Deep Learning) cổ điển sang AI Tạo sinh (Generative AI) và cuối cùng là **AI Tác nhân (Agentic AI)**.*
- * **Generative AI (AI Tạo sinh)** cho phép tạo ra nội dung (văn bản, hình ảnh, video) từ các câu lệnh (prompts).*
- * **Agentic AI (AI Tác nhân)** vượt qua khả năng tạo ra nội dung đơn bước. Nó thiết lập mục tiêu, lập kế hoạch và hành động lặp đi lặp lại bằng cách kết nối với các công cụ và API bên ngoài.*

*### Dòng thời gian tiến hóa*
2. *Sự bùng nổ của Deep Learning (2012)*
3. *Kiến trúc Transformer (2017)*
5. *Tác nhân AI (AI Agents) (2024-2026)*

*## 2. LLMs: Động cơ của AI hiện đại*
*Các Mô hình Ngôn ngữ Lớn (LLMs) hoạt động như những động cơ suy luận nền tảng cho cả Generative AI và Agentic AI.*

*### Kiến trúc Transformer*
*Kiến trúc cốt lõi vận hành LLMs là **Decoder-only Transformer**. Nó hoạt động dựa trên việc dự đoán token tiếp theo một cách tuần tự (Next-Token Prediction) dựa trên toàn bộ ngữ cảnh trước đó.*
*Các cơ chế chính bao gồm:*
- * **Self-Attention (Tự chú ý)**: Mỗi token "chú ý" đến mọi token khác, nắm bắt các mối quan hệ ngữ cảnh phức tạp.*
- * **Multi-Head Attention (Chú ý đa đầu)**: Nhiều cơ chế chú ý chạy song song, cho phép mô hình nắm bắt đồng thời các loại mối quan hệ khác nhau.*
- * **Positional Encoding (Mã hóa vị trí)**: Đưa thông tin thứ tự chuỗi vào mô hình vì bản thân cơ chế self-attention thiếu đi nhận thức về vị trí.*

*### Quy trình huấn luyện LLM*
1. * **Pre-training (Tiền huấn luyện)**: Đọc một lượng khổng lồ văn bản trên internet để học ngôn ngữ và kiến thức chung.*
2. * **Supervised Fine-Tuning (SFT) (Tinh chỉnh có giám sát)**: Học từ các ví dụ để định dạng câu trả lời một cách phù hợp.*
3. * **RLHF / DPO**: Căn chỉnh mô hình theo sở thích của con người để đảm bảo tính an toàn và hữu ích.*

*## 3. Nền kinh tế Token*
*Token là đơn vị xử lý văn bản cơ bản của LLMs (khoảng 0.75 của một từ tiếng Anh).*
- * **Cost (Chi phí)**: Chi phí API được xác định bởi số lượng Input Tokens (Token đầu vào) và Output Tokens (Token đầu ra). Token đầu ra thường đắt hơn.*
- * **Latency (Độ trễ)**: Xử lý nhiều token hơn làm tăng độ trễ. Context window (Cửa sổ ngữ cảnh) giới hạn số lượng token tối đa mà một LLM có thể xử lý trong một yêu cầu duy nhất.*
- * **Language Nuances (Sự khác biệt ngôn ngữ)**: Các ngôn ngữ không phải tiếng Anh (như tiếng Việt) và mã nguồn thường yêu cầu nhiều token hơn để mã hóa, làm tăng chi phí.*

*## 4. Sử dụng API và Lựa chọn Mô hình*
*Bài giảng cung cấp hướng dẫn thực tế về cách gọi LLM APIs (OpenAI, Anthropic) và quản lý các tham số:*
- * **Temperature (Nhiệt độ)**: Kiểm soát mức độ sáng tạo (0 là tất định, 1 là tính đa dạng cao).*
- * **Model Selection (Lựa chọn mô hình)**: Sự đánh đổi giữa chi phí, độ trễ và chất lượng. Ví dụ như sử dụng Claude Haiku cho các tác vụ điều hướng nhanh, rẻ và Claude Opus hoặc GPT-4o cho suy luận phức tạp.*
- * **Streaming**: Nhận các câu trả lời theo từng phần nhỏ để giảm độ trễ theo cảm nhận của người dùng.*

*VibeCoding là một mô hình lập trình mới nơi nhà phát triển mô tả mục đích và ngữ cảnh cho AI, sau đó AI sẽ tạo ra mã nguồn.*
- * **Mindset Shift (Thay đổi tư duy)**: Từ việc viết mã thủ công chuyển sang điều hướng AI, xem xét logic của nó và tinh chỉnh kết quả đầu ra.*
- * **Principles (Nguyên tắc)**:*
  1. *Dẫn dắt bởi mục đích: Trình bày rõ ràng các mục tiêu.*
  2. *Ưu tiên ngữ cảnh: Cung cấp các tệp, ví dụ và ràng buộc cần thiết.*
  3. *Đánh giá của con người: Luôn xem xét và xác thực mã nguồn do AI tạo ra.*
