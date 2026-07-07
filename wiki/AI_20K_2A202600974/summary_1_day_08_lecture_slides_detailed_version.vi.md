---
type: summary
title: "Summary: 1-Day 08 Lecture Slides_Detailed version.pdf"
description: "A detailed summary of the Day 8 lecture slides covering the complete Retrieval-Augmented Generation (RAG) paradigm, from indexing and retrieval to generation and evaluation."
tags: [ai, 20k, day8, rag, retrieval, generation, evaluation]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/1-Day 08 Lecture Slides_Detailed version.pdf"]
---
Yêu cầu đã rõ. Tôi sẽ giữ nguyên cấu trúc Markdown, mỗi phần tiếng Anh giữ nguyên, bên dưới là bản dịch tiếng Việt in nghiêng. Đối với các heading, tôi sẽ giữ heading gốc và thêm heading tiếng Việt in nghiêng bên dưới. Danh sách và các dòng sẽ được tách cặp.

---

*# Tóm tắt: Bài giảng Ngày 8 - Phiên bản chi tiết*

*## Tổng quan*

*Tài liệu này tóm tắt các slide bài giảng toàn diện về **Quy trình RAG (Retrieval-Augmented Generation - Sinh văn bản tăng cường bằng truy xuất)** trong Ngày 8. Bài giảng nhấn mạnh rằng RAG không chỉ đơn thuần là thêm ngữ cảnh mà là sự phối hợp đồng bộ của ba hệ thống chính: Lập chỉ mục (Indexing), Truy xuất (Retrieval) và Sinh văn bản (Generation). Nó cũng đề cập đến các khuôn khổ đánh giá, nhấn mạnh rằng chất lượng truy xuất thường quyết định chất lượng của câu trả lời cuối cùng.*

*## 1. Mô hình RAG & Kiến trúc Lập chỉ mục*

  *- **Tại sao lại là RAG?** Các LLM gặp phải "Giới hạn kiến thức" và "Ảo giác". Việc tinh chỉnh (Fine-tuning) rất tốn kém và kém hiệu quả trong việc đưa dữ liệu thực tế vào, trong khi RAG hoạt động như một "bài thi mở", cung cấp các sự kiện có cơ sở, kiểm soát truy cập và cập nhật theo thời gian thực.*

  *- **AI lấy dữ liệu làm trung tâm:** Nút thắt thực sự thường nằm ở hệ thống truy xuất (80% lỗi) chứ không phải ở LLM (20% lỗi).*

  *- **Quy trình Lập chỉ mục:***
    *- **Phân tích cú pháp (Parsing):** Dữ liệu thực tế rất lộn xộn (bố cục PDF, bảng biểu). Các giải pháp bao gồm các trình phân tích cú pháp chuyên dụng (LlamaParse, Unstructured) hoặc Vision LLM (Phân tích đa phương thức) để trích xuất các thành phần cấu trúc như Markdown/HTML.*
  - **Data Cleaning:** Normalization and Redaction (che mờ PII).
    *- **Làm sạch dữ liệu:** Chuẩn hóa và ẩn danh (che mờ PII).*
    *- **Chiến lược thu thập (Ingestion):** Xử lý hàng loạt (Batch processing) so với Hướng sự kiện (Event-driven / Delta Sync) thông qua webhooks để xử lý các bản cập nhật động.*

  *- **Chiến lược Phân mảnh (Chunking) Nâng cao:***
    *- *Kích thước cố định (Fixed-Size):* Cắt một cách máy móc, có nguy cơ phá vỡ ý nghĩa ngữ nghĩa.*
    *- *Phân mảnh đệ quy (Recursive Chunking):* Cách tiếp cận tiêu chuẩn (LangChain), tôn trọng ranh giới đoạn văn và câu.*
    *- *Phân mảnh ngữ nghĩa/Cấu trúc:* Sử dụng các tiêu đề Markdown hoặc Cây cú pháp trừu tượng (AST) cho mã.*
    *- *Truy xuất Từ nhỏ đến lớn (Parent-Child):* Tìm kiếm bằng cách sử dụng các đoạn nhỏ để có độ chính xác, nhưng đưa ngữ cảnh gốc lớn hơn vào LLM.*

  *- **Nhúng (Embeddings) & Siêu dữ liệu (Metadata):** *
    *- *Tìm kiếm Vector* xuất sắc ở ngữ nghĩa và diễn giải nhưng thất bại ở các kết quả khớp từ khóa chính xác (ví dụ: mã lỗi như ERR-x09).*
    *- *Lọc Siêu dữ liệu:* Lọc trước (Pre-filtering) so với Lọc sau (Post-filtering). Lọc trước an toàn hơn và nhanh hơn.*

*## 2. Xử lý Truy vấn & Truy xuất Nâng cao*

  *- **Chuyển đổi Truy vấn:** *
    *- *Mở rộng Truy vấn:* Thêm các từ đồng nghĩa để khắc phục khoảng trống từ vựng của người dùng.*
    *- *Phân tách Truy vấn:* Chia nhỏ các truy vấn đa bước.*
    *- *Step-Back Prompting:* Trừu tượng hóa các câu hỏi quá chi tiết.*
    *- *HyDE (Hypothetical Document Embeddings - Nhúng Tài liệu Giả định):* Tạo một câu trả lời giả và nhúng nó để tìm các tài liệu thực có ngữ nghĩa tương tự.*

  *- **Truy xuất Dày đặc (Dense) vs. Thưa thớt (Sparse):** *
    *- *Thưa thớt (BM25):* Khớp chính xác, trọng số cao cho các từ hiếm, nhanh nhưng không nhận diện được từ đồng nghĩa.*
    *- *Dày đặc (Vector):* Tìm kiếm ngữ nghĩa, thân thiện với việc diễn giải lại, nhưng bỏ sót các ID chính xác.*

  *- **Tìm kiếm Lai & Xếp hạng lại (Reranking):** *
    *Kết hợp các tìm kiếm Dày đặc và Thưa thớt bằng cách sử dụng **RRF (Reciprocal Rank Fusion)** hoặc Alpha-tuning.*
    *- **Xếp hạng lại Hai giai đoạn:** Sử dụng Tìm kiếm Lai diện rộng cho Top-100, sau đó áp dụng **Cross-Encoder** để chấm điểm mức độ liên quan sâu sắc cho Top-5.*
    *- **MMR (Mức độ liên quan cận biên tối đa):** Ngăn ngừa sự dư thừa trong các cửa sổ ngữ cảnh bằng cách phạt các đoạn quá giống nhau.*

*## 3. Sinh văn bản, Nền tảng (Grounding) & Trải nghiệm Người dùng (UX)*

  *- **Tiêm Ngữ cảnh:** *
    *- Hiệu ứng "Lạc ở giữa" (Lost in the Middle): LLM nhớ rõ nhất phần đầu và phần cuối của lời nhắc. Giải pháp: **Sắp xếp lại Tài liệu** (đặt các kết quả hàng đầu ở các ranh giới).*
    *- Sử dụng các thẻ XML hoặc Markdown có cấu trúc để phân định ranh giới các quy tắc hệ thống, ngữ cảnh và câu hỏi của người dùng. Giới hạn ngữ cảnh ở khoảng 60% ngân sách token.*

  *- **Kỹ thuật Prompt để có Nền tảng Chặt chẽ:** *
    *- Bắt buộc trích dẫn (ví dụ: `[doc_1]`).*
    *- Suy giảm tinh tế (Graceful Degradation): Hướng dẫn LLM nói rõ "Tôi không biết" hoặc đề xuất các lựa chọn thay thế khi ngữ cảnh không đủ.*
    *- **Chuỗi Suy nghĩ (Chain-of-Thought - CoT):** Buộc LLM phải vạch ra lập luận của mình trước khi tạo ra câu trả lời cuối cùng.*

  *- **Trải nghiệm Người dùng Đầu ra:** *
    *- Tạo các đầu ra dễ quét với các trích dẫn nội tuyến, khối nguồn và điểm tin cậy.*
  - Use streaming states ("Đang tìm kiếm...") to improve perceived latency.
    *- Sử dụng các trạng thái luồng (streaming states - ví dụ: "Đang tìm kiếm...") để cải thiện độ trễ được cảm nhận.*

  *- **Các Lỗi Sinh văn bản Phổ biến:** *
    *- *Ngữ cảnh Mâu thuẫn:* Hướng dẫn LLM ưu tiên ngày gần nhất.*
    *- *Suy diễn quá mức:* Thực thi nền tảng chặt chẽ để ngăn LLM đoán mò bên ngoài các sự kiện.*

*## 4. Đánh giá, Đưa vào Sản xuất & Các Bước Tiếp theo*

  *- **Bộ ba Đánh giá RAG (RAGAS):** *
     *1. **Độ thu hồi Ngữ cảnh (Context Recall):** Trình truy xuất có tìm thấy tất cả các bằng chứng cần thiết không?*
     *2. **Độ trung thực (Faithfulness):** Trình tạo có bám sát chặt chẽ các sự kiện được truy xuất mà không bị ảo giác không?*
     *3. **Sự liên quan của Câu trả lời (Answer Relevance):** Câu trả lời có thực sự giải quyết câu hỏi của người dùng không?*

  *- **LLM đóng vai trò Giám khảo (LLM-as-a-Judge):** Tự động hóa việc đánh giá bằng cách cho một LLM mạnh chấm điểm các đầu ra RAG dựa trên một Tập dữ liệu Vàng (Golden Dataset).*

  *- **Thử nghiệm A/B:** Đánh giá ROI (Lợi tức đầu tư) cho các tính năng nâng cao (ví dụ: Cross-encoder tăng 5% độ liên quan nhưng làm tăng độ trễ thêm 3 giây). Triển khai CI/CD dữ liệu để chặn việc triển khai nếu các chỉ số giảm sút.*

  *- **Tương lai của Tác nhân (Agentic Future):** RAG đơn lượt đang phát triển thành các hệ thống Đa Tác nhân (sử dụng LangGraph) nơi Truy xuất chỉ trở thành một trong nhiều công cụ mà LLM có thể gọi.*
