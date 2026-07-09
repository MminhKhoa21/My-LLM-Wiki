---
type: summary
title: "Summary: 1-day08-rag-pipeline-v2.pdf"
description: "A detailed summary of the Day 8 RAG Pipeline v2 slides focusing on bridging retrieval, augmentation, and generation, alongside pre-RAG query transformations and evaluation techniques."
tags: [ai, 20k, day8, rag, pipeline, augmentation]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/8/1-day08-rag-pipeline-v2.pdf"]
---
# *Tóm tắt: Pipeline RAG v2*

## *Tổng quan*
This document summarizes the slides from "1-day08-rag-pipeline-v2.pdf" (by M.Sc Trần Minh Tú). It details the evolution from a simple Indexing pipeline (Day 07) to a fully orchestrated **Retrieval-Augmented Generation (RAG)** pipeline. The lecture highlights how RAG solves the LLM illusion of knowledge, making it a compulsory architecture for enterprise AI applications.
Tài liệu này tóm tắt các slide từ "1-day08-rag-pipeline-v2.pdf" (của ThS. Trần Minh Tú). Nó nêu chi tiết quá trình phát triển từ một pipeline Lập chỉ mục đơn giản (Ngày 07) sang một pipeline **Retrieval-Augmented Generation (RAG - Tạo sinh tăng cường truy xuất)** được điều phối hoàn chỉnh. Bài giảng nhấn mạnh cách RAG giải quyết ảo giác kiến thức của LLM, khiến nó trở thành một kiến trúc bắt buộc cho các ứng dụng AI của doanh nghiệp.

## *1. Chuyển từ Truy xuất (Retrieval) sang RAG*
- ***Tại sao lại dùng RAG?** LLMs có giới hạn kiến thức tại một thời điểm nhất định và có bản chất xác suất, dẫn đến hiện tượng ảo giác (hallucinations). RAG giải quyết vấn đề này bằng cách cung cấp ngữ cảnh động, có cơ sở (giống như bài thi tự luận được mở tài liệu) thay vì phụ thuộc vào việc tinh chỉnh (fine-tuning) tốn kém và tĩnh.*
- ***Bộ ba R-A-G:***
  - ***Retrieval (R - Truy xuất):** Tìm kiếm bằng chứng phù hợp (Tìm kiếm dày đặc, thưa thớt, kết hợp).*
  - ***Augmentation (A - Tăng cường):** Cấu trúc lại ngữ cảnh để giảm thiểu hiệu ứng "mất thông tin ở giữa" (lost in the middle) và nhiễu.*
  - ***Generation (G - Tạo sinh):** Đưa ra câu trả lời có cơ sở với các trích dẫn nghiêm ngặt và tự kiểm tra.*

## *2. Đi sâu vào Truy xuất (Retrieval)*
- ***Tìm kiếm Ngữ nghĩa (Semantic) vs. Tìm kiếm Từ vựng (Lexical):***
  - *Dense Vector (Ngữ nghĩa):* Nắm bắt ý nghĩa, diễn giải lại, nhưng gặp khó khăn với các từ khóa chính xác như ID hoặc mã.
  - *Sparse Vector (BM25):* Khớp từ khóa chính xác một cách nhanh chóng nhưng bỏ qua ngữ cảnh và các từ đồng nghĩa.
- ***Tìm kiếm Kết hợp (Hybrid) & Dung hợp (Fusion):***
  - Kết hợp cả hai phương pháp bằng cách sử dụng **RRF (Reciprocal Rank Fusion)** hoặc Trọng số Alpha (Alpha-weighting).
- ***Xếp hạng lại (Reranking) & MMR:***
  - Sau khi tìm kiếm top-K rộng rãi, sử dụng **Cross-Encoder** để chấm điểm mức độ liên quan chính xác.
  - Áp dụng **MMR (Maximum Marginal Relevance - Mức độ liên quan cận biên tối đa)** để giảm bớt các đoạn dư thừa và giữ lại ngữ cảnh đa dạng.

## *3. Các Chiến lược Tăng cường (Augmentation)*
- ***Tiêm Ngữ cảnh (Context Injection):***
  - ***Sắp xếp lại tài liệu:** Vì LLMs ghi nhớ phần đầu và phần cuối của câu lệnh tốt hơn, hãy đặt các tài liệu phù hợp nhất ở hai đầu `[1, 3, 5, 4, 2]`.*
- ***Đảm bảo Tính có cơ sở (Grounding) và Xác thực:***
  - Cô lập các Quy tắc Hệ thống, Ngữ cảnh và Câu hỏi Người dùng qua các thẻ XML.
  - Tích hợp **Siêu dữ liệu (Metadata)** và **Định dạng Trích dẫn** để đảm bảo trách nhiệm giải trình.
- ***Quản lý Ngân sách Token:** Giữ ngữ cảnh dưới 60% giới hạn token để tránh làm loãng câu lệnh. Sử dụng Nén Ngữ cảnh nếu cần thiết.*

## *4. Kiểm soát Tạo sinh (Generation) & Đầu ra*
- ***Lựa chọn Mô hình & Định dạng:** Chọn các mô hình dựa trên độ phức tạp của tác vụ (ví dụ: các mô hình cục bộ nhỏ so với API lớn của doanh nghiệp). Chuẩn hóa đầu ra thông qua Markdown hoặc JSON.*
- ***An toàn và Căn chỉnh:** Lọc thông tin nhận dạng cá nhân (PII) và áp dụng các quy tắc từ chối ("Graceful Degradation" - thừa nhận "Tôi không biết" khi thiếu ngữ cảnh).*
- ***Tự Sửa lỗi & Chuỗi Suy luận (CoT):***
  - Sử dụng **Chuỗi Suy luận (Chain-of-Thought - CoT)** (`<thought_process>`) để ép buộc việc suy luận từng bước trước khi trả lời.
  - Thực hiện tự kiểm tra với ngữ cảnh trước khi đưa ra câu trả lời cuối cùng.
- ***Trải nghiệm Người dùng (UX):** Định dạng đầu ra rất quan trọng. Văn bản dễ nhìn, trích dẫn nội dòng, cửa sổ bật lên (popups) về nguồn, và tạo sinh luồng (streaming) sẽ tạo niềm tin cho người dùng.*

## *5. Tiền RAG (Pre-RAG) & RAG Tác nhân (Agentic RAG)*
- ***Chuyển đổi Câu truy vấn:***
  - Sử dụng LLMs để tiền xử lý các câu truy vấn trước khi tìm kiếm vector: *Multi-Query* (các biến thể), *HyDE* (các câu trả lời tạo từ ảo giác), *Mở rộng Truy vấn* (từ đồng nghĩa), *Phân tách* (chia nhỏ các truy vấn đa bước), và *Step-Back Prompting* (trừu tượng hóa).
  - Tiền lọc qua siêu dữ liệu (metadata) sẽ tăng tốc mạnh mẽ và tập trung vào mục tiêu tìm kiếm.
- ***RAG Tác nhân (Agentic RAG):** Nâng cấp hệ thống để tự truy vấn, tự sửa lỗi (C-RAG) và thích ứng. Truy xuất chỉ trở thành một trong nhiều "công cụ" trong một hệ thống đa tác nhân.*

## *6. Đánh giá RAG (RAGAS)*
Việc "kiểm tra theo cảm tính" (vibe check) là không đủ. Một khuôn khổ đánh giá nghiêm ngặt, tự động bao gồm ba trục chính:
1. ***Độ hồi tưởng Ngữ cảnh (Context Recall):** Trình truy xuất có thu thập các tài liệu cần thiết không?*
2. ***Độ trung thực (Faithfulness):** Câu trả lời của LLM có bám sát vào ngữ cảnh được truy xuất không?*
3. ***Độ liên quan của Câu trả lời (Answer Relevance):** Câu trả lời có thỏa mãn yêu cầu của người dùng mà không bị lan man không?*
- Việc triển khai các đường ống CI/CD cho AI bao gồm việc kiểm thử "hành vi" của AI so với Tập dữ liệu Chuẩn (Golden Dataset).
