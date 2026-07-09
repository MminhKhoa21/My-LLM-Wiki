---
type: summary
title: "Day 25 Track 2: GPU FinOps & Cost Optimization"
description: "A comprehensive guide to optimizing GPU cloud costs, utilizing spot instances, right-sizing workloads, and inference cost reduction techniques."
tags: [FinOps, GPU, cost-optimization, inference, LLMOps]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/25/Day25 - Track 2 - Gpu-finops-cost-optimization.pdf"]
---
Nội dung bạn cung cấp đã là song ngữ (Anh - Việt) hoàn chỉnh, với tiếng Anh ở dòng chính và bản dịch tiếng Việt in nghiêng ngay bên dưới. Dưới đây là nội dung được giữ nguyên định dạng Markdown và đã có đầy đủ cả hai ngôn ngữ:

Ngày 25 Track 2: Quản lý tài chính và tối ưu chi phí GPU

Tài liệu này tóm tắt các chiến lược quản lý và tối ưu chi phí GPU (FinOps) trong các môi trường AI sản xuất, bao gồm mọi thứ từ lựa chọn instance đến tối ưu suy luận nâng cao.

1. Cấu trúc chi phí GPU đám mây

Chi phí không chỉ là giá theo giờ của GPU.

  ***Chi phí ẩn**: Truyền dữ liệu (egress), NAT gateway, quản lý bí mật.*
  ***Chi tiêu lãng phí**: GPU nhàn rỗi qua đêm, instance cấp phát quá mức, dung lượng dự trữ không dùng, và môi trường phát triển chạy 24/7.*

Nguyên tắc chung: Mức sử dụng GPU < 30% cho thấy cần điều chỉnh kích thước ngay.

2. Instance Spot và Preemptible

Instance Spot có thể giảm 60-70% chi phí nhưng yêu cầu xử lý gián đoạn một cách linh hoạt.

  ***Chiến lược hỗn hợp đội tàu**: 20% on-demand (cơ sở) và 80% spot (bùng nổ) để cân bằng chi phí và độ tin cậy.*
  ***Chiến lược Checkpoint**: Lưu trạng thái mô hình thường xuyên (ví dụ: mỗi epoch hoặc 30 phút) vào S3/GCS. Nếu một spot instance bị chấm dứt, instance mới có thể tiếp tục từ checkpoint một cách liền mạch.*

3. Điều chỉnh kích thước và mức sử dụng

Tối ưu hóa mức sử dụng yêu cầu theo dõi các chỉ số phù hợp:

  ***Sử dụng GPU**: Kiểm tra xem GPU có nhàn rỗi không.*
  ***MFU (Sử dụng FLOPs của mô hình)**: Theo dõi các tác vụ bị giới hạn tính toán (vd: huấn luyện, prefill).*
  ***MBU (Sử dụng băng thông bộ nhớ)**: Theo dõi các tác vụ bị giới hạn bộ nhớ (vd: giải mã, phục vụ).*

Phục vụ đa mô hình và MIG (GPU đa instance)

Để cải thiện mức sử dụng thấp trên GPU lớn (vd: A100), sử dụng MIG để cô lập các instance hoặc triển khai phục vụ đa mô hình để hoán đổi mô hình động dựa trên yêu cầu.

4. Tối ưu chi phí suy luận

Các đòn bẩy nâng cao để giảm chi phí mỗi token:

  ***Gộp yêu cầu (Request Batching)**: Nhóm các yêu cầu giúp tăng đáng kể thông lượng và giảm chi phí.*
  ***Bộ nhớ đệm**: Sử dụng Redis hoặc bộ nhớ đệm ngữ nghĩa để tái sử dụng phản hồi prompt trước đó (tỷ lệ trúng 30-40%).*
  ***Phân tầng mô hình**: Sử dụng mô hình nhỏ hơn, rẻ hơn (vd: Llama-3-8B) cho 80% truy vấn và chỉ chuyển các truy vấn phức tạp đến mô hình lớn hơn.*
  ***Lượng tử hóa**: Các định dạng như AWQ 4-bit có thể giảm chi phí mỗi token đáng kể.*
  ***Phục vụ phân tách**: Tách prefill (nặng tính toán) và decode (nặng bộ nhớ) lên các cụm GPU riêng biệt để tránh tắc nghẽn.*
  ***Prefill theo khối và Giải mã suy luận**: Cân bằng TTFT (Thời gian đến token đầu tiên) và ITL (Độ trễ giữa các token).*
  ***Bộ nhớ đệm KV và tiền tố (Prefix Caching)**: Tái sử dụng bộ nhớ KV cho các tiền tố chung để tăng tốc TTFT cho các prompt hệ thống giống nhau.*

5. Phân bổ chi phí và tính phí lại

Thiết lập chiến lược gắn thẻ rõ ràng (`team`, `project`, `env`) được thực thi bởi các chính sách SCP/OPA. Sử dụng các công cụ như Kubecost để phân tích chi phí theo pod, đảm bảo mỗi nhóm có ngân sách được chỉ định và bảng điều khiển minh bạch.

6. AI bền vững: Carbon và năng lượng

Tối ưu hóa cũng giảm dấu chân carbon. Chọn các khu vực đám mây xanh (vd: trung tâm dữ liệu thủy điện) và sử dụng các mô hình chưng cất, nhỏ hơn khi khả thi. Theo dõi lượng phát thải carbon cùng với các chỉ số hiệu suất (vd: `CodeCarbon`).

Nếu bạn cần bất kỳ điều chỉnh nào về ngôn ngữ hoặc định dạng, hãy cho tôi biết.

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
