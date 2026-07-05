---
type: summary
title: "Day 27 – Track 1: Human-in-the-Loop UX"
description: "Khi nào Agent cần xin phép? HITL taxonomy, confidence routing, approval workflows và UX best practices."
tags: [ai, 20k, day27, track1, hitl, ux, human-in-the-loop]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/27/Day12 - Track 3 - Human-in-the-loop-ux-khi-nao-agent-can-xin-phep.pdf"]
---

> **Lộ trình:** [[track1_ba|Track 1: AI Product / BA]]


# Day 27 – Track 1: Human-in-the-Loop UX

**Giảng viên**: VinUniversity  
**Khóa**: AICB Phase 2 · Track 3 · Ngày 27

> **Câu hỏi trọng tâm**: Agent tự quyết hay hỏi người dùng – ranh giới nào là an toàn và không làm phiền?

---

## Tại sao Full Autonomy nguy hiểm?

Các sự cố thực tế cho thấy Agent hoạt động hoàn toàn tự động dẫn đến:
- Hành động không thể hoàn tác (gửi email, xóa file, thực hiện giao dịch)
- Tích lũy sai lệch qua nhiều bước (error compounding)
- Mất trust từ phía người dùng khi xảy ra lỗi

---

## HITL Taxonomy – 6 Interaction Patterns

| Pattern | Khi nào dùng | Ví dụ |
|---------|-------------|-------|
| **Always ask** | Action có rủi ro cao, không thể hoàn tác | Gửi email cho client |
| **Ask if uncertain** | Agent confidence thấp | Chưa chắc về địa chỉ giao hàng |
| **Show then do** | Action quan trọng, có thể undo | Tạo file, book meeting |
| **Do then show** | Low-risk, reversible | Tóm tắt tài liệu |
| **Silent execution** | Routine, high-confidence, reversible | Log ghi chú |
| **Async approval** | Không cần phản hồi ngay | Approve PR sau khi review |

---

## Confidence Routing – Khi nào Interrupt?

```python
def route_action(action, confidence_score):
    if action.is_irreversible and confidence_score < 0.95:
        return "request_approval"
    elif confidence_score < 0.70:
        return "request_clarification"
    elif action.risk_level == "high":
        return "show_then_do"
    else:
        return "silent_execution"
```

---

## Approval Workflows

**Synchronous**: User phải approve ngay → block execution  
**Asynchronous**: Gửi notification, tiếp tục sau khi có approval  
**Timeout policy**: Nếu không có approval sau X phút → cancel hoặc escalate

---

## HITL UX Best Practices

1. **Rõ ràng**: Hiển thị chính xác Agent định làm gì
2. **Preview**: Cho xem kết quả trước khi thực thi
3. **Easy reject**: Nút "Từ chối" luôn dễ bấm, không bị che khuất
4. **Undo**: Với action đã thực hiện, cung cấp cách hoàn tác
5. **Audit trail**: Log mọi quyết định để debug sau này

---

## Liên kết
- [[day23_track3]] – LangGraph HITL implementation
- [[day11_overview]] – Guardrails & AI Safety
- [[day27_overview]]
