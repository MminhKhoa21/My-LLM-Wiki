---
type: summary
title: "Day 24 Track 1: AI Ethics, AI Safety and Responsible AI"
description: "Summary of Day 24 Track 1 covering AI safety, harm mapping, system mapping, and responsible AI practices."
tags: [ai-ethics, ai-safety, responsible-ai, harm-map, track1]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/24/d24-slide-v1.pdf", "AI_20K_2A202600974/24/day24-track1-lab.pdf"]
---
# Day 24 Track 1: AI Ethics & Safety
*# Ngày 24 Track 1: Đạo đức và An toàn AI*

This page summarizes the lecture and lab on AI Ethics and Safety for Track 1.
*Trang này tóm tắt bài giảng và bài thực hành về Đạo đức và An toàn AI cho Track 1.*

## Key Concepts
*## Các Khái niệm Chính*

### AI Safety & Ethics
### *An toàn & Đạo đức AI*

AI safety is not just about whether a system functions correctly, but how it impacts real users in real-world contexts, and whether there are sufficient guardrails and accountability mechanisms in place before deployment. "Safe AI is a system placed in the right context, with the right guardrails, and someone taking responsibility when things go wrong."
*An toàn AI không chỉ đơn thuần là hệ thống có hoạt động chính xác hay không, mà còn là cách nó tác động đến người dùng thực trong bối cảnh thực tế, và liệu có đủ các rào chắn an toàn cùng cơ chế chịu trách nhiệm trước khi triển khai hay không. "AI an toàn là một hệ thống được đặt đúng bối cảnh, có đúng rào chắn, và có người chịu trách nhiệm khi mọi thứ xảy ra sai sót."*

### Failure Modes of AI
### *Các Chế độ Hỏng hóc của AI*

- **Hallucination:** Fabricating facts, policies, data, or links with high confidence.
  *- **Ảo giác:** Bịa đặt sự thật, chính sách, dữ liệu hoặc liên kết với độ tự tin cao.*
- **Bias / Fairness:** Providing skewed results across different demographics or creating subtle inequalities.
  *- **Thiên vị / Công bằng:** Cung cấp kết quả lệch lạc giữa các nhóm nhân khẩu học khác nhau hoặc tạo ra bất bình đẳng tinh vi.*
- **Sycophancy:** Agreeing with the user even when the user is wrong.
  *- **Xu nịnh:** Đồng tình với người dùng ngay cả khi người dùng sai.*
- **Over-reliance:** Users trusting the AI's output as the absolute truth and failing to verify it.
  *- **Phụ thuộc quá mức:** Người dùng tin tưởng đầu ra của AI như chân lý tuyệt đối và không kiểm chứng lại.*
- **Harmful Advice:** Giving dangerous medical, legal, financial, or self-harm advice.
  *- **Lời khuyên có hại:** Đưa ra lời khuyên nguy hiểm về y tế, pháp lý, tài chính hoặc tự gây hại.*
- **Privacy Leak:** Exposing PII, prompts, internal documents, or other users' data.
  *- **Rò rỉ quyền riêng tư:** Tiết lộ thông tin nhận dạng cá nhân (PII), prompt, tài liệu nội bộ hoặc dữ liệu của người dùng khác.*
- **Escalation Failure:** Failing to refuse or hand off to a human agent when necessary.
  *- **Lỗi chuyển tiếp:** Không từ chối hoặc chuyển cho nhân viên con người khi cần thiết.*
- **Misuse / Jailbreak:** Users forcing the AI to bypass its guardrails or constraints.
  *- **Lạm dụng / Phá khóa:** Người dùng buộc AI vượt qua các rào chắn hoặc ràng buộc của nó.*

### System Map for Debugging
### *Bản đồ Hệ thống để Gỡ lỗi*

When an AI system fails, it's crucial to identify which layer originated the error rather than just blaming the model:
*Khi một hệ thống AI gặp lỗi, điều quan trọng là xác định lớp nào đã gây ra lỗi thay vì chỉ đổ lỗi cho mô hình:*

1. **User Experience (UX):** The interface users interact with. If the UI makes the AI look too official without uncertainty cues, users might over-rely on it.
   *1. **Trải nghiệm người dùng (UX):** Giao diện mà người dùng tương tác. Nếu UI khiến AI trông quá chính thức mà không có dấu hiệu không chắc chắn, người dùng có thể phụ thuộc quá mức vào nó.*
2. **System Message & Grounding:** Instructions guiding the model and the sources it relies on. Errors here lead to hallucinations or out-of-scope answers.
   *2. **Thông điệp Hệ thống & Nền tảng:** Các hướng dẫn điều khiển mô hình và các nguồn mà nó dựa vào. Lỗi ở đây dẫn đến ảo giác hoặc câu trả lời ngoài phạm vi.*
3. **Safety System:** Guardrails that block, refuse, or escalate requests. Weaknesses here allow harmful or sensitive requests to pass through.
   *3. **Hệ thống An toàn:** Các rào chắn chặn, từ chối hoặc chuyển tiếp yêu cầu. Điểm yếu ở đây cho phép các yêu cầu có hại hoặc nhạy cảm đi qua.*
4. **Model:** The core AI model. If it's too weak for the task or inherently flawed, it will fail despite good instructions.
   *4. **Mô hình:** Mô hình AI cốt lõi. Nếu nó quá yếu cho nhiệm vụ hoặc có lỗi cố hữu, nó sẽ thất bại dù có hướng dẫn tốt.*

### Harm Map Framework
### *Khung Bản đồ Tác hại*

To systematically analyze AI risks, we evaluate them across four dimensions:
*Để phân tích rủi ro AI một cách có hệ thống, chúng ta đánh giá chúng qua bốn khía cạnh:*

- **Severity:** The impact of the harm (Low: minor annoyance, Medium: reversible harm, High: financial/legal/opportunity loss, Critical: physical harm or irreversible damage).
  *- **Mức độ nghiêm trọng:** Tác động của tác hại (Thấp: khó chịu nhỏ, Trung bình: tác hại có thể khắc phục, Cao: mất mát tài chính/pháp lý/cơ hội, Nghiêm trọng: tổn hại thể chất hoặc thiệt hại không thể khắc phục).*
- **Scale:** The number of people or groups affected.
  *- **Quy mô:** Số lượng người hoặc nhóm bị ảnh hưởng.*
- **Probability:** The likelihood of the harm occurring.
  *- **Xác suất:** Khả năng xảy ra tác hại.*
- **Frequency:** How often the harm repeats if it occurs.
  *- **Tần suất:** Mức độ thường xuyên tác hại lặp lại nếu nó xảy ra.*

## Lab 24: Case Study Hunt & Harm Map
*## Lab 24: Săn tìm Nghiên cứu Tình huống & Bản đồ Tác hại*

The lab focuses on selecting an industry (e.g., HR, Education, Healthcare, Mobility, Media, Content Creator) and finding 2-3 real-world AI failure case studies within that domain.
*Phần thực hành tập trung vào việc chọn một ngành (ví dụ: Nhân sự, Giáo dục, Y tế, Di động, Truyền thông, Người sáng tạo nội dung) và tìm 2-3 nghiên cứu tình huống thất bại AI thực tế trong lĩnh vực đó.*

- **Industry Risk Snapshot:** Evaluate the industry's overall risk profile (physical harm potential, high-stakes decisions, sensitive data, blast radius).
  *- **Ảnh chụp nhanh Rủi ro Ngành:** Đánh giá hồ sơ rủi ro tổng thể của ngành (tiềm năng tổn hại thể chất, quyết định có rủi ro cao, dữ liệu nhạy cảm, bán kính ảnh hưởng).*
- **Harm Map Worksheet:** For each case study, students must identify the high-risk moment, affected stakeholders, failure mode, the layer where the error originated, the actual harm, the harm lens (e.g., misinformation, injury, privacy loss), and score it based on Severity, Scale, Probability, and Frequency.
  *- **Bảng tính Bản đồ Tác hại:** Với mỗi nghiên cứu tình huống, sinh viên phải xác định thời điểm rủi ro cao, các bên liên quan bị ảnh hưởng, chế độ hỏng hóc, lớp phát sinh lỗi, tác hại thực tế, lăng kính tác hại (ví dụ: thông tin sai lệch, thương tích, mất quyền riêng tư), và chấm điểm dựa trên Mức độ nghiêm trọng, Quy mô, Xác suất và Tần suất.*
