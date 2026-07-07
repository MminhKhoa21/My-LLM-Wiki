---
type: summary
title: "Summary of day26_mcp_a2a_infrastructure_new.pptx"
description: "Phân tích và so sánh Model Context Protocol (MCP) và Agent-to-Agent Protocol (A2A) trong xây dựng hệ thống đa tác nhân (Multi-Agent Systems)."
tags: [ai, 20k, day26]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/26/day26_mcp_a2a_infrastructure_new.pptx"]
---

# Tóm tắt: MCP & A2A Infrastructure

## 1. Sự tiến hoá từ LLM đơn lẻ sang hệ thống Multi-Agent
- Hệ thống AI ngày nay ngày càng phức tạp nên việc để một LLM khổng lồ (monolithic) gánh vác mọi rủi ro về ảo giác (hallucination) đã nhường chỗ cho kiến trúc nhiều agent cùng làm việc.
- Việc kết nối các hệ thống đa tác nhân cần được chuẩn hoá với hai giao thức mới: **MCP** và **A2A**.

- Được **Anthropic** giới thiệu vào năm 2024.
- **Mục đích:** Chuẩn hoá cách kết nối một LLM (client) với các công cụ bên ngoài, tệp tin và cơ sở dữ liệu (Server). Giúp giải quyết bài toán $N \times M$ tích hợp giữa ứng dụng và tool, giảm xuống chỉ còn $N + M$.
- **Kiến trúc:** Client–Server bất đối xứng.
- Các thành phần cốt lõi của MCP Server:
  1. **Resources:** Dữ liệu chỉ đọc (file, DB snapshot, logs).
  2. **Tools:** Các hàm có side-effect tác động ra bên ngoài (gửi email, gọi SQL, tạo PR).
  3. **Prompts:** Những mẫu template tái sử dụng được.

- Được **Google** giới thiệu vào năm 2025.
- **Mục đích:** Chuẩn hoá giao tiếp giữa các AI Agents một cách chủ động như những "người đồng cấp" (peers).
- **Kiến trúc:** Peer-to-peer đối xứng.
- **Đơn vị giao tiếp:** AgentCard, Task, Message, Part, Artifact.
- Một agent có thể tự chủ kế hoạch, ủy thác (delegate) toàn bộ hoặc một phần công việc cho agent khác thông qua A2A.

## 4. MCP vs A2A: Khi nào dùng cái nào?
Hai chuẩn này **KHÔNG** cạnh tranh mà bổ trợ lẫn nhau:
- **Dùng MCP** cho mọi thứ kết nối **KHÔNG PHẢI LÀ AGENT** (như hệ thống files, CSDL, APIs thụ động). Tools gọi MCP là "thụ động", chờ đến khi được chỉ định gọi.
- **Dùng A2A** cho mọi thứ kết nối **LÀ AGENT** với nhau. Agent gọi A2A có khả năng "chủ động" tự lập kế hoạch.
- **Kết hợp thực tế:** Một Agent có thể giao tiếp với một Agent khác (qua mạng A2A), nhưng bên trong bản thân nó lại dùng nhiều kết nối MCP Server để lấy dữ liệu nội bộ.

## 5. Observability trong hệ thống đa tác nhân
- Vì quy trình truyền tay giữa nhiều Agent, các luồng request đều bắt buộc phải gắn **trace_id**. Tính quan sát (Observability) bằng trace_id là thiết yếu để trace một truy vấn xuyên suốt nhiều dịch vụ (Ví dụ qua 5 Agent phân tán).
