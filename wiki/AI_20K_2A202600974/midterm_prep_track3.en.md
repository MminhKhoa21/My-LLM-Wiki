---
type: concept
title: "Midterm Exam Preparation - Track 3 (App Build)"
description: "Bộ tài liệu và câu hỏi ôn tập thi giữa kỳ Chương trình Phát triển Năng lực AI Thực Chiến dành cho Track 3 (App Build)"
tags: [ai, 20k, exam, prep, track3]
timestamp: 2026-07-06
sources: ["wiki/AI_20K_2A202600974/day21_track3.md", "wiki/AI_20K_2A202600974/day24_track3.md", "wiki/AI_20K_2A202600974/day23_track3.md", "wiki/AI_20K_2A202600974/day19_track3.md", "wiki/AI_20K_2A202600974/day16_track3.md"]
---



---



### 1. AI Design Patterns & Agent Architectures
* **Multi-Agent Orchestration:** 

### 2. RAG Pipeline & Prompt Engineering

### 3. Observability & AI Security

---



### 1. Advanced Agent Patterns

### 2. Advanced RAG (GraphRAG & Hybrid Search)

### 3. Fine-tuning LLMs (LoRA/QLoRA)
  $$\Delta W = B \cdot A$$

### 4. RAGAS Metrics

---







---




```python
from langgraph.graph import StateGraph, END
from typing import TypedDict

class AgentState(TypedDict):
    code: str
    error_log: str
    iterations: int

workflow = StateGraph(AgentState)

workflow.add_node("generate_code", generate_code_node)
workflow.add_node("test_code", test_code_node)
workflow.add_node("debug_code", debug_code_node)

workflow.set_entry_point("generate_code")
workflow.add_edge("generate_code", "test_code")

# Định nghĩa luồng rẽ nhánh điều kiện sau khi test code
def route_after_test(state: AgentState):
    if not state.get("error_log"):
        return "end"
    else:
        return "debug_code"

workflow.add_conditional_edges(
    "test_code",
    route_after_test,
    {
        "end": END,
        "debug_code": "debug_code"
    }
)

# LỖI NẰM Ở ĐÂY: Kết nối từ debug_code quay lại test_code
workflow.add_edge("debug_code", "test_code")

app = workflow.compile()
```




```python
# 1. Khởi tạo trạng thái mặc định
# Trong node generate_code_node, ta thiết lập state["iterations"] = 1
# Trong node debug_code_node, ta cộng dồn state["iterations"] += 1

MAX_ITERATIONS = 3

def route_after_test(state: AgentState):
    # Kiểm tra nếu hết lượt debug cho phép
    if state.get("iterations", 0) >= MAX_ITERATIONS:
        print("Đã đạt giới hạn sửa lỗi tối đa. Thoát luồng.")
        return "end"
        
    if not state.get("error_log"):
        return "end"
    else:
        return "debug_code"
```

---





---

