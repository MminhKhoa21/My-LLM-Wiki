---
type: summary
title: "Summary of Day 28 Deck"
description: "Insights on AI product monetization, GTM strategy, and building evidence for B2B sales."
tags: [ai, 20k, day28, product, gtm, sales]
timestamp: 2026-07-06
sources: ["raw/AI_20K_2A202600974/28/Day 28 Deck.pdf"]
---

# From A Working Product To A Sellable Product
# Từ Một Sản Phẩm Hoạt Động Được Đến Một Sản Phẩm Có Thể Bán Được
**Instructor:** Đàm Bá Quyền (Frost) - Founder & CEO, BIVA
**Giảng viên:** Đàm Bá Quyền (Frost) - Founder & CEO, BIVA

## Overview
## Tổng quan
This deck covers the business side of AI, specifically how to turn a technical demo into a product that customers will pay for. It emphasizes that a functional model is just a technical problem, while selling it is a survival problem.

Tài liệu này bao gồm khía cạnh kinh doanh của AI, cụ thể là cách biến một bản demo kỹ thuật thành một sản phẩm mà khách hàng sẵn sàng trả tiền. Tài liệu nhấn mạnh rằng một mô hình hoạt động được chỉ là vấn đề kỹ thuật, trong khi bán nó là vấn đề sống còn.

## 1. AI Pricing
## 1. Định giá AI (AI Pricing)
Unlike traditional SaaS, the marginal cost of an AI application never approaches zero due to computational costs (e.g., tokens, inference). Therefore, pricing must be carefully structured.

Không giống như SaaS truyền thống, chi phí biên của một ứng dụng AI không bao giờ giảm xuống bằng 0 do các chi phí tính toán (ví dụ: số token, quá trình suy luận). Do đó, việc định giá phải được cấu trúc cẩn thận.

### Choosing the Value Metric
### Lựa chọn Chỉ số Giá trị (Value Metric)
There are four common ways to structure pricing:

Có bốn cách phổ biến để cấu trúc việc định giá:
- **Seat:** Fixed fee per user (e.g., Notion AI). Easy to sell, but risky if usage is high.
- **Theo Chỗ (Seat):** Phí cố định cho mỗi người dùng (ví dụ: Notion AI). Dễ bán, nhưng rủi ro nếu mức sử dụng quá cao.
- **Usage:** Pay-as-you-go based on consumption. Safest for margins but can cause bill-shock for customers.
- **Theo Mức sử dụng (Usage):** Trả tiền theo mức độ sử dụng (Pay-as-you-go). An toàn nhất cho tỷ suất lợi nhuận nhưng có thể gây sốc hóa đơn cho khách hàng.
- **Outcome:** Charging based on the results generated. Requires perfect attribution.
- **Theo Kết quả (Outcome):** Tính phí dựa trên kết quả được tạo ra. Đòi hỏi việc quy kết (attribution) hoàn hảo.
- **Hybrid:** Base subscription plus usage fees.
- **Kết hợp (Hybrid):** Đăng ký thuê bao cơ bản cộng thêm phí sử dụng.

*Rule of Thumb:* Choose the metric based on **Attribution** (can you measure the result?) and **Autonomy** (does it run without human intervention?).
*Quy tắc Kinh nghiệm:* Lựa chọn chỉ số dựa trên **Khả năng quy kết (Attribution)** (bạn có thể đo lường kết quả không?) và **Tính tự trị (Autonomy)** (nó có chạy mà không cần sự can thiệp của con người không?).

### Floor Price and Anchoring
### Giá sàn và Neo giá
- **Cost/Job:** API costs + Infra costs + HITL (Human-In-The-Loop) costs + Retry overhead.
- **Chi phí/Công việc:** Chi phí API + Chi phí Hạ tầng + Chi phí HITL (Con người tham gia vào vòng lặp) + Chi phí Thử lại (Retry overhead).
- **Pricing:** Should be at least 3x the Cost/Job to maintain healthy margins.
- **Định giá:** Nên ít nhất bằng 3 lần Chi phí/Công việc để duy trì tỷ suất lợi nhuận lành mạnh.
- **Anchoring:** Never anchor pricing to a $20 ChatGPT subscription. Anchor it to the cost of human labor or the business value it generates.
- **Neo giá (Anchoring):** Không bao giờ neo giá theo gói đăng ký $20 của ChatGPT. Hãy neo nó vào chi phí lao động của con người hoặc giá trị kinh doanh mà nó mang lại.

## 2. Go-To-Market (GTM) Strategy
## 2. Chiến lược Tiếp cận Thị trường (GTM)
The core rule of GTM for AI is: **Do not make the user open a new tab or learn a new workflow.** Embed your AI directly into the customer's existing workflow.

Quy tắc cốt lõi của GTM cho AI là: **Không bắt người dùng mở một tab mới hoặc học một quy trình làm việc mới.** Hãy nhúng AI của bạn trực tiếp vào quy trình làm việc hiện tại của khách hàng.

### Distribution Channels
### Kênh Phân phối
Select one primary channel for the first 90 days:

Chọn một kênh chính trong 90 ngày đầu tiên:
1. **Product-Led Growth (PLG):** Self-serve. For simple, low-cost products (ARPU < $50).
1. **Tăng trưởng qua Sản phẩm (PLG):** Tự phục vụ. Dành cho các sản phẩm đơn giản, chi phí thấp (ARPU < $50).
2. **Sales-Led:** Direct sales teams. For complex, high-value enterprise products (ARPU > $1000).
2. **Tăng trưởng qua Bán hàng (Sales-Led):** Đội ngũ bán hàng trực tiếp. Dành cho các sản phẩm doanh nghiệp phức tạp, giá trị cao (ARPU > $1000).
3. **Partner-Led:** Integrating into existing platforms. Helps bypass CAC (Customer Acquisition Cost) by leveraging partners.
3. **Tăng trưởng qua Đối tác (Partner-Led):** Tích hợp vào các nền tảng hiện có. Giúp bỏ qua Chi phí chuyển đổi khách hàng (CAC) bằng cách tận dụng các đối tác.

*The ARPU-CAC Dead Zone:* Avoid being stuck with an ARPU between $50 - $1000 where it's too expensive for self-serve but doesn't yield enough margin to support a sales team.
*Vùng chết ARPU-CAC:* Tránh bị mắc kẹt với ARPU từ $50 - $1000, nơi quá tốn kém để tự phục vụ nhưng lại không mang lại đủ tỷ suất lợi nhuận để duy trì một nhóm bán hàng.

## 3. Evidence-Based Sales
## 3. Bán hàng Dựa trên Bằng chứng
Demos generate applause, but evidence closes deals. Enterprise procurement and IT departments require concrete evidence before buying.

Các bản demo tạo ra những tràng pháo tay, nhưng bằng chứng mới là thứ chốt được hợp đồng. Các bộ phận mua sắm và CNTT của doanh nghiệp yêu cầu bằng chứng cụ thể trước khi mua.

### Critical Questions from Buyers
### Những Câu hỏi Quan trọng từ Người Mua
- Will this AI hallucinate and give wrong answers to my customers?
- AI này có bị ảo giác và đưa ra câu trả lời sai cho khách hàng của tôi không?
- Will my data be used to train your models?
- Dữ liệu của tôi có bị sử dụng để đào tạo mô hình của bạn không?
- What happens to my data if your startup fails?
- Điều gì xảy ra với dữ liệu của tôi nếu startup của bạn thất bại?

### The Evidence Pack
### Bộ Bằng chứng (The Evidence Pack)
Sales teams must be armed with documentation, evaluation metrics, and security guarantees to bypass procurement blockers.

Đội ngũ bán hàng phải được trang bị tài liệu, các chỉ số đánh giá và các đảm bảo về bảo mật để vượt qua các rào cản mua sắm.

## Key Takeaways
## Những Điểm Chính
1. **Choose the Right Value Metric:** Ensure it balances risk and aligns with customer value.
1. **Chọn Đúng Chỉ số Giá trị:** Đảm bảo nó cân bằng rủi ro và phù hợp với giá trị của khách hàng.
2. **Embed in Habits:** Integrate into existing workflows rather than forcing new ones.
2. **Nhúng vào Thói quen:** Tích hợp vào các quy trình làm việc hiện có thay vì ép buộc những quy trình mới.
3. **Sell Results, Not AI:** Customers care about saving time, reducing costs, and better sleep—not the underlying LLM architecture.
3. **Bán Kết quả, Không phải bán AI:** Khách hàng quan tâm đến việc tiết kiệm thời gian, giảm chi phí và ngủ ngon hơn—chứ không phải kiến trúc LLM đằng sau nó.


## Liên kết
## Links
- [[day28_overview]]
