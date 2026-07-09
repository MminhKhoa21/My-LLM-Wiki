---
type: summary
title: "Câu hỏi ôn tập - Track2"
description: "Bộ câu hỏi ôn tập tổng hợp cho Track2"
tags: [review, track2]
timestamp: 2026-07-06
sources: []
---
# *Bộ câu hỏi ôn tập Track2*

### *Câu hỏi ôn tập Ngày 3*

   Theo bài giảng, điểm khác biệt chính giữa Agent và LLM Chatbot là gì?
     A. Agent không sử dụng mô hình ngôn ngữ lớn (LLM).
     B. Agent có vòng lặp tư duy dài hạn (long-horizon goal) và sử dụng tools để quan sát từng bước.
     C. LLM Chatbot có khả năng thực hiện nhiều quyết định liên tiếp hơn Agent.
     D. Agent chỉ hoạt động dựa trên quy tắc cố định (rule-based).
   ***Đáp án:** B*

   Tiêu chí nào sau đây KHÔNG thuộc bộ bốn tiêu chí của Agentic Fit Framework?
   ***Đáp án:** C*

   Trong ReAct Pattern, thứ tự đúng của một vòng lặp cơ bản là:
   ***Đáp án:** C*

   Khi gỡ lỗi (debug) Agent loop, bước đầu tiên nên kiểm tra là gì?
     A. Kiểm tra tool description có đủ chi tiết không.
     B. Xem xét "Thought" của Agent có đúng mục tiêu không.
     C. Cài đặt fallback retry ngay lập tức.
     D. Tăng số lượng tools tối đa.
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 4*

   Theo bài giảng, một Agent đáng tin cậy được xây dựng dựa trên bốn trụ cột nào?
   ***Đáp án:** A*

   Hiện tượng "Lost in the Middle" trong Context Engineering được khắc phục bằng cách nào?
     A. Nhồi nhét tất cả thông tin vào giữa context
     B. Sắp xếp thông tin quan trọng ở đầu và cuối context
     C. Lọc bỏ toàn bộ thông tin lịch sử hội thoại
     D. Sử dụng nhiều ví dụ hơn trong prompt
   ***Đáp án:** B*

   Trong Tool Calling, yếu tố nào đóng vai trò như instruction để LLM quyết định chọn tool?
     A. Kết quả trả về từ tool
     B. Tên tool và mô tả chi tiết
     C. Định dạng JSON của tool
     D. Số lượng tool được khai báo
   ***Đáp án:** B*

   Cơ chế "Human-in-the-Loop" (HITL) được áp dụng khi nào?
     A. Khi tool thực hiện thao tác đọc dữ liệu
     B. Khi tool thực hiện thao tác thay đổi trạng thái (ví dụ: thanh toán, xóa DB)
     C. Khi LLM trả về kết quả không đúng format
     D. Khi context bị nhiễu (Context Rot)
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 15*

   Track 2 (AI Infrastructure & Data) trong Phase 2 tập trung đào tạo kỹ năng gì?
     A. Phát triển mô hình AI mới và tối ưu hóa kiến trúc
     B. Tự dựng và vận hành backend của hệ thống AI ở mức production
     C. Thiết kế UI/UX cho ứng dụng AI
     D. Xây dựng chiến lược kinh doanh sản phẩm AI
   ***Đáp án:** B*

   Điều kiện cứng nào được đề cập để có thể thực hành các lab về serving và FinOps trong Track 2?
     A. Có tài khoản GitHub Enterprise
     B. Cần có GPU hoặc Cloud free-tier
     C. Phải có chứng chỉ Kubernetes
     D. Cần có máy tính có RAM > 32GB
   ***Đáp án:** B*

   Vai trò mục tiêu (CP2) nào sau đây được đề cập trong bài giảng là phù hợp với Track 2?
   ***Đáp án:** C*

   Theo bài giảng, Track 2 phù hợp với những người có tư duy về các khái niệm nào dưới đây?
     A. UI/UX, trải nghiệm người dùng, A/B testing
     B. SLA, SLO, P95, Chi phí
     C. Thiết kế đồ họa, animation, storytelling
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 16*

   Theo chiến lược Hybrid Cloud cho AI, cách kết hợp nào sau đây được khuyến nghị để tối ưu cả chi phí và khả năng mở rộng?
     A. Training và Serving đều dùng PaaS
     B. Training dùng IaaS, Serving dùng PaaS
     C. Training dùng AI-aaS, Serving dùng IaaS
     D. Training dùng PaaS, Serving dùng IaaS
   ***Đáp án:** B*

   GPU nào được mô tả là "sleeper pick" cho tác vụ Inference với mức giá $0.40-$0.86/giờ?
   ***Đáp án:** C*

   Giải pháp nào giúp giảm 60-70% chi phí khi training model AI trên cloud?
     A. Sử dụng Reserved Instances
     B. Sử dụng Spot/Preemptible Instances
     C. Sử dụng On-Demand Instances
     D. Sử dụng Dedicated Hosts
   ***Đáp án:** B*

   Trong Kubernetes, để quản lý tài nguyên GPU cho AI workload, cấu hình nào sau đây là đúng?
     A. Đặt requests nhỏ hơn limits cho GPU
     B. Dùng `nvidia.com/gpu` với requests = limits
     C. Không cần chỉ định resource requests cho GPU
     D. Dùng `cpu` và `memory` thay vì GPU resource
   ***Đáp án:** B*

   Serving engine nào sử dụng RadixAttention để tái sử dụng KV cache, tối ưu cho Agent và Multi-turn chat?
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 17*

   Trong Medallion Architecture, lớp nào chứa dữ liệu đã được làm sạch, khử trùng lặp và áp dụng schema?
   ***Đáp án:** B*

   Kỹ thuật nào được sử dụng để phát hiện các bản ghi lỗi trong pipeline mà không làm hỏng toàn bộ luồng xử lý?
     A. Ghi log lỗi vào file tạm
     B. Chuyển bản ghi lỗi vào Dead-Letter Queue (DLQ)
     C. Dừng pipeline ngay lập tức
     D. Ghi đè dữ liệu lỗi bằng giá trị null
   ***Đáp án:** B*

   Phương pháp nào giúp giảm thiểu training-serving skew bằng cách tạo features theo thời gian thực?
     A. Batch processing hàng ngày
     B. Streaming với Kafka và Flink
     C. Sử dụng File Store thay vì Feature Store
     D. Chỉ dùng CDC từ database
   ***Đáp án:** B*

   Trong quy trình ingestion cho LLM, bước nào diễn ra sau khi parsing dữ liệu phi cấu trúc?
     A. Embedding vào Vector Store
     B. Chunking (ví dụ: 512 token)
     C. Lưu trữ dạng raw
     D. Kiểm tra schema
   ***Đáp án:** B*

   "Data Flywheel" trong AI pipeline sử dụng loại dữ liệu nào làm nguồn cho lớp Bronze?
     A. Dữ liệu giao dịch tài chính
     B. Agent traces (prompt, tool calls, phản hồi người dùng)
     C. Dữ liệu cảm biến IoT
     D. Log hệ thống thuần túy
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 18*

   Công nghệ nào nổi bật với tính năng **Hidden Partitioning** giúp tự động trừu tượng hóa logic phân vùng khỏi người dùng?
   ***Đáp án:** B*

   Anti-pattern nào sau đây thường dẫn đến **vấn đề file nhỏ** trong Data Lakehouse?
     A. Phân vùng theo cột có nhiều giá trị (cardinality cao)
     B. Bỏ qua lệnh `OPTIMIZE`
     C. Đặt `VACUUM 0 HOURS`
     D. Sử dụng Spark cho các truy vấn nhỏ
   ***Đáp án:** B*

   Trong kiến trúc Medallion, lớp nào chứa dữ liệu **bất biến (immutable) và chỉ nối thêm (append-only)**?
   ***Đáp án:** A*

   Để đảm bảo tính tái lập mô hình (model reproducibility), nên tích hợp **phiên bản Delta** với yếu tố nào?
     A. Mã nguồn Git
     B. ID chạy MLflow (run ID)
     C. Dấu thời gian hệ thống
     D. Tên file Parquet
   ***Đáp án:** B*

   Định dạng lưu trữ nào được khuyến nghị cho hiệu suất đọc cột và nén tốt trong Lakehouse?
   ***Đáp án:** C*

---

### *Câu hỏi ôn tập Ngày 19*

   Điều gì xảy ra nếu bạn thay đổi model embedding sau khi đã index dữ liệu trong vector database?
     A. Vector database tự động cập nhật embedding cho tất cả dữ liệu cũ.
     B. Không ảnh hưởng gì vì vector database lưu trữ vector độc lập với model.
     C. Bắt buộc phải re-index toàn bộ dữ liệu vì vector từ model cũ và mới không tương thích.
     D. Chỉ cần thay đổi model ở khâu query, index vẫn giữ nguyên.
   ***Đáp án:** C*

   Khi các vector đã được chuẩn hóa (unit-norm), mệnh đề nào sau đây là đúng?
     A. Cosine Similarity và Dot Product cho thứ tự xếp hạng khác nhau.
     B. Thứ tự xếp hạng của Cosine, Dot Product và Euclidean Distance là giống nhau.
     C. Chỉ có Cosine Similarity mới cho kết quả chính xác.
     D. Euclidean Distance không thể sử dụng với vector đã chuẩn hóa.
   ***Đáp án:** B*

   Yếu tố nào được cho là chiếm tới 80% chất lượng của hệ thống RAG?
     A. Lựa chọn vector database (Qdrant, Weaviate).
     B. Kỹ thuật ANN (HNSW, IVF).
     C. Chiến lược chunking (kích thước và độ chồng lấp).
     D. Sử dụng hybrid search kết hợp BM25.
   ***Đáp án:** C*

   Vấn đề "Training-Serving Skew" trong Feature Store được giải quyết bằng cách nào?
     A. Sử dụng Point-in-time Join để ghép dữ liệu theo thời gian thực.
     B. Đảm bảo cả huấn luyện và inference dùng cùng một bộ xử lý tính toán feature.
     C. Lưu trữ tất cả features trong Online Store thay vì Offline Store.
     D. Tăng kích thước dataset để giảm sai lệch.
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 20*

   Chỉ số nào dưới đây được coi là thước đo quan trọng nhất trong sản xuất (production) vì nó phản ánh khả năng đáp ứng các mục tiêu về chất lượng dịch vụ (SLO)?
     C. Throughput (tổng số token/giây)
     D. Goodput@SLO (tốc độ yêu cầu thỏa mãn SLO của TTFT và TPOT)
   ***Đáp án:** D*

   Kỹ thuật lượng tử hóa nào được khuyên dùng cho môi trường CPU/Edge inference và sử dụng định dạng Q4_K_M?
   ***Đáp án:** C*

   Phát biểu nào sau đây đúng về PagedAttention?
     A. Chỉ hoạt động trên kiến trúc GPT, không hỗ trợ các mô hình khác.
     B. Loại bỏ phân mảnh bộ nhớ KV cache và cho phép continuous batching, tăng throughput lên đến 24x.
     C. Là phương pháp nén KV cache bằng cách chiếu xuống không gian tiềm ẩn (latent space).
     D. Yêu cầu phần cứng chuyên dụng (NVIDIA Hopper) và không thể chạy trên GPU thế hệ cũ.
   ***Đáp án:** B*

   Trong các chiến lược song song hóa, kỹ thuật nào tách biệt pha prefill và decode thành các cụm (pool) riêng để tránh tắc nghẽn do các prompt dài?
   ***Đáp án:** D*

---

### *Câu hỏi ôn tập Ngày 21*

   Điểm khác biệt cốt lõi nhất khi áp dụng CI/CD cho hệ thống AI so với phần mềm thông thường là gì?
     A. Cần tự động hóa việc kiểm thử giao diện người dùng.
     B. Phải quản lý phiên bản dữ liệu và theo dõi thí nghiệm để ngăn model regression.
     C. Không cần kiểm thử vì model luôn hoạt động tốt.
     D. Chỉ sử dụng một công cụ duy nhất cho toàn bộ pipeline.
   ***Đáp án:** B*

   Trong MLflow, chức năng Model Registry được sử dụng chủ yếu để làm gì?
     A. Lưu trữ dữ liệu huấn luyện dưới dạng artifact.
     B. So sánh các runs trên giao diện UI.
     C. Quản lý vòng đời mô hình, bao gồm staging, production và versioning.
     D. Tự động deploy model lên production không cần kiểm tra.
   ***Đáp án:** C*

   Khi sử dụng DVC, lệnh nào được dùng để chạy lại toàn bộ pipeline một cách tái lập (reproducible)?
   ***Đáp án:** C*

   Chiến lược triển khai nào cho phép chạy model mới song song với model cũ mà không ảnh hưởng đến người dùng, chỉ để thu thập log và so sánh?
   ***Đáp án:** C*

---

### *Câu hỏi ôn tập Ngày 22*

   Điểm khác biệt cốt lõi giữa LLMOps và MLOps truyền thống là gì?
     A. LLMOps tập trung vào quản lý dữ liệu hơn là code
     B. LLMOps coi việc quản lý phiên bản Prompt quan trọng như quản lý code và data
     C. MLOps không cần đến evaluation
     D. LLMOps chỉ dùng cho các mô hình ngôn ngữ nhỏ
   ***Đáp án:** B*

   Công cụ nào được mô tả như "GitHub dành riêng cho prompt" trong bài giảng?
   ***Đáp án:** C*

   Theo bài giảng, RAGAS được sử dụng để đánh giá những khía cạnh nào của LLM?
     A. Chỉ độ chính xác (accuracy)
     B. Tốc độ inference và chi phí
     C. Faithfulness, relevance và hallucination
     D. Khả năng phát hiện Prompt Injection
   ***Đáp án:** C*

   Một trong những mục tiêu của Guardrails & Safety Monitoring là gì?
     A. Tăng tốc độ sinh token
     B. Chặn lộ thông tin cá nhân (PII) và phát hiện Prompt Injection
     C. Tự động tạo prompt mới từ dữ liệu
     D. Tối ưu hóa chi phí API
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 23*

   Theo bài giảng, ngoài các golden signals truyền thống, LLM cần thêm những tín hiệu nào để đảm bảo observability?
   ***Đáp án:** B*

   Cardinality là “kẻ giết hóa đơn thầm lặng” vì:
     A. Nó làm tăng độ trễ của hệ thống
     B. Nó làm tăng số lượng unique label combinations, dẫn đến chi phí lưu trữ và xử lý cao
     C. Nó làm giảm số lượng metrics có thể thu thập
     D. Nó gây lỗi khi sử dụng Prometheus
   ***Đáp án:** B*

   Sự tiến hóa từ DevOps lên AgentOps được mô tả trong “The Ops Trinity” bao gồm:
   ***Đáp án:** A*

   Theo bài giảng, telemetry từ các ngày trước được tích hợp vào Day 23, ví dụ:
     A. Ngày 16: Spark UI metrics
     B. Ngày 19: GPU util (DCGM)
     C. Ngày 22: Eval-pass-rate dưới dạng Prometheus gauge
     D. Ngày 17: llama.cpp tokens/sec
   ***Đáp án:** C*

---

### *Câu hỏi ôn tập Ngày 24*

   Theo nguyên tắc Least Privilege, role nào sau đây có quyền xóa dữ liệu production?
   ***Đáp án:** C*

   Trong mô hình envelope encryption, Data Encryption Key (DEK) được bảo vệ như thế nào?
     A. Lưu trữ dưới dạng plaintext trong code
     B. Được mã hóa bởi Key Encryption Key (KEK)
     C. Xoay vòng hàng năm thay vì hàng tháng
     D. Được nhúng trực tiếp vào mô hình
   ***Đáp án:** B*

   Kỹ thuật xử lý PII nào có thể đảo ngược và thường được dùng cho phân tích nội bộ?
   ***Đáp án:** D*

   Trong Security Testing Pyramid, công cụ nào được sử dụng để phát hiện secret bị lộ trong kho lưu trữ mã nguồn?
   ***Đáp án:** C*

---

### *Câu hỏi ôn tập Ngày 25*

   Theo bài giảng, dấu hiệu nào cho thấy cần phải right-sizing GPU ngay lập tức?
   ***Đáp án:** B*

   Chiến lược nào giúp tận dụng spot instances với mức giảm 60-70% chi phí mà vẫn đảm bảo độ tin cậy?
     A. Chỉ sử dụng 100% spot instances
     B. Mixed Fleet Strategy: 20% on-demand + 80% spot, kết hợp checkpoint thường xuyên
     C. Sử dụng on-demand cho training và spot cho inference
     D. Dùng reserved instances thay cho spot
   ***Đáp án:** B*

   Để theo dõi hiệu suất GPU, chỉ số nào đặc biệt quan trọng đối với tác vụ compute-bound (ví dụ: training, prefill)?
   ***Đáp án:** C*

   Kỹ thuật nào trong inference optimization giúp giảm chi phí per token bằng cách sử dụng mô hình nhỏ hơn cho hầu hết các truy vấn đơn giản?
   ***Đáp án:** C*

   Để phân bổ chi phí GPU cho các nhóm (chargeback), bài giảng khuyến nghị sử dụng chiến lược nào?
     A. Tính chi phí trung bình cho tất cả nhóm
     B. Thiết lập tagging (team, project, env) và dùng Kubecost để phân tích
     C. Dùng một tài khoản cloud duy nhất không phân chia
     D. Chỉ theo dõi tổng chi phí hàng tháng
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 26*

   MCP (Model Context Protocol) cung cấp những primitives nào để LLM tương tác với công cụ và dữ liệu?
   ***Đáp án:** A*

   Trong giao thức A2A, một task có thể chuyển sang trạng thái nào để yêu cầu thêm thông tin từ caller thay vì thất bại ngay lập tức?
   ***Đáp án:** C*

   Chiến lược routing nào được mô tả là linh hoạt nhất nhưng chậm và tốn kém?
   ***Đáp án:** C*

   Theo bài giảng, phương pháp quản lý trạng thái nào được khuyến nghị ban đầu vì dễ mở rộng theo chiều ngang?
     A. Stateful với sticky sessions
     B. Stateless với context lưu trong Redis hoặc PostgreSQL
     C. Stateful với lưu trữ cục bộ
     D. Stateless không lưu context
   ***Đáp án:** B*

   Nguyên tắc bảo mật nào yêu cầu con người phải phê duyệt các hành động rủi ro cao như ghi cơ sở dữ liệu?
   ***Đáp án:** C*

---

### *Câu hỏi ôn tập Ngày 27*

   Điểm khác biệt cốt lõi giữa **Pipeline Monitoring** và **Data Observability** là gì?
     A. Pipeline Monitoring chỉ kiểm tra thời gian chạy, còn Data Observability kiểm tra tính đúng đắn của dữ liệu.
     B. Pipeline Monitoring dùng cho batch, Data Observability dùng cho streaming.
     C. Pipeline Monitoring tập trung vào logs, Data Observability tập trung vào schema.
     D. Không có sự khác biệt, cả hai đều giống nhau.
   ***Đáp án:** A*

   Trong 5 trụ cột của Data Observability, trụ cột nào phát hiện sự thay đổi về tên cột hoặc kiểu dữ liệu?
   ***Đáp án:** C*

   Trong Great Expectations, **Checkpoint** có vai trò gì?
     A. Lưu trữ các rule kiểm tra dữ liệu (Expectation Suite).
     B. Tích hợp Expectation Suite vào pipeline sản xuất và kích hoạt hành động (alert, block) khi thất bại.
     C. Tự động sinh dữ liệu mẫu để kiểm tra.
     D. Thay thế hoàn toàn cho dbt tests.
   ***Đáp án:** B*

   Trong SLO Engineering, **Error Budget** được sử dụng để làm gì?
     A. Đo lường mức độ tươi mới của dữ liệu.
     B. Cân bằng giữa tính ổn định và tính năng mới: nếu ngân sách lỗi cạn kiệt, ưu tiên sửa lỗi thay vì phát hành tính năng.
     C. Xác định ngưỡng cảnh báo cho anomaly detection.
     D. Phân loại mức độ nghiêm trọng của sự cố (P0-P3).
   ***Đáp án:** B*

---

### *Câu hỏi ôn tập Ngày 28*

   Theo bài giảng, đâu là **anti-pattern** trong tích hợp các thành phần AI Platform?
     A. Sử dụng event-driven integration với Kafka
     B. Duy trì cấu hình trong Git (GitOps)
     C. Gắn kết chặt chẽ (tightly coupled) giữa các thành phần
     D. Áp dụng Bulkhead pattern để tách biệt inference và training
   ***Đáp án:** C*

   Trong luồng request end-to-end, thời gian mục tiêu cho mỗi thành phần là bao nhiêu?
     D. Tất cả đều cần dưới 100ms
   ***Đáp án:** B*

   Công cụ nào được khuyến nghị để **phân tích chi tiết độ trễ (latency breakdown)** trong toàn bộ luồng?
   ***Đáp án:** C*

   Điều kiện tiên quyết để triển khai Platform ra production theo 5 Pillars là gì?
     A. Kiểm tra checklist Production Readiness bằng tay bởi kỹ sư
     B. Tự động hóa checklist trong CI pipeline
     C. Đảm bảo tất cả code đều chạy trên môi trường local
     D. Sử dụng duy nhất một framework cho toàn bộ stack
   ***Đáp án:** B*

   Mô hình nào sau đây là **integration pattern** đúng để tránh shared mutable state?
     A. Dùng cơ sở dữ liệu chung có thể ghi đồng thời
     B. Immutable events và event sourcing qua append-only log (Kafka)
     C. Lưu trạng thái trong biến toàn cục (global variable)
     D. Sử dụng file cấu hình JSON tĩnh
   ***Đáp án:** B*
