---
type: concept
title: "Midterm Exam Preparation - Track 3 (App Build)"
description: "Bộ tài liệu và câu hỏi ôn tập thi giữa kỳ Chương trình Phát triển Năng lực AI Thực Chiến dành cho Track 3 (App Build)"
tags: [ai, 20k, exam, prep, track3]
timestamp: 2026-07-06
sources: ["wiki/AI_20K_2A202600974/day21_track3.md", "wiki/AI_20K_2A202600974/day24_track3.md", "wiki/AI_20K_2A202600974/day23_track3.md", "wiki/AI_20K_2A202600974/day19_track3.md", "wiki/AI_20K_2A202600974/day16_track3.md"]
---

# BỘ ÔN TẬP THI GIỮA KỲ — TRACK 3 (APP BUILD)

Tài liệu này tổng hợp kiến thức trọng tâm và các dạng câu hỏi ôn tập (Trắc nghiệm, Multi-select, Scenario Debug, Case Study) bám sát cấu trúc đề thi giữa kỳ (100 điểm) dành riêng cho học viên **Track 3: App Build (Agent Developer)**.

---

## PHẦN I: KIẾN THỨC CHUNG (Trọng tâm Phần I — 50 điểm)

Phần này bắt buộc cho tất cả học viên, tập trung vào các nền tảng thiết kế hệ thống AI, RAG, Prompt, Agent, Observability và Bảo mật.

### 1. AI Design Patterns & Agent Architectures
* **ReAct Pattern (Reasoning + Acting):** Sự kết hợp giữa suy luận (Thought) và hành động (Action/Observation). LLM tạo ra suy luận để quyết định gọi công cụ (Tool Calling), nhận kết quả trả về, và tiếp tục lặp lại cho đến khi đạt được kết quả cuối cùng.
* **State Machine & Graph-based (LangGraph):** Quản lý trạng thái (State) của Agent một cách rõ ràng. Tránh việc LLM bị lặp vô hạn (Infinite loop) bằng cách định nghĩa các Node (hành động/gọi LLM) và Edge (luồng điều hướng có điều kiện).
* **Multi-Agent Orchestration:** 
  * *Supervisor Pattern:* Một Agent trung tâm điều phối và chia việc cho các Worker Agents.
  * *Debate Pattern:* Các Agents đối thoại chéo để tự sửa lỗi và tăng chất lượng phản hồi.
  * *Parallel Pattern:* Thực thi nhiều tác vụ Agent độc lập song song rồi tổng hợp kết quả (Reduce).

### 2. RAG Pipeline & Prompt Engineering
* **Trực quan hóa Pipeline RAG cơ bản:** `Tài liệu` -> `Chunking` -> `Embedding` -> `Vector DB` -> `Retrieval` -> `Augmentation` -> `Generation`.
* **Context Engineering:** Xây dựng gói ngữ cảnh tối ưu, xử lý giới hạn token (Context Window) và tránh hiện tượng "lost in the middle" (thông tin quan trọng nằm ở giữa ngữ cảnh bị LLM bỏ qua).
* **System Prompting:** Đóng vai (Persona), chỉ thị nghiêm ngặt (System constraints), định dạng đầu ra (JSON schema), và chống tiêm nhiễm câu lệnh (Jailbreak protection).

### 3. Observability & AI Security
* **LLM-Native Observability:** Giám sát thông qua Traces, Spans của các cuộc gọi API LLM (sử dụng LangSmith, Phoenix). Đo lường chi phí (Token usage), độ trễ (Latency), và tỷ lệ lỗi.
* **Bảo mật & Guardrails:**
  * Phòng chống **Prompt Injection** và **Jailbreak**.
  * Sử dụng **Guardrails đa lớp** (Input Guardrails chặn nội dung độc hại trước khi gửi tới LLM; Output Guardrails kiểm tra tính hợp lệ và rò rỉ dữ liệu nhạy cảm PII trước khi trả về User).

---

## PHẦN II: CHUYÊN SÂU TRACK 3 (Trọng tâm Phần II/III/IV)

Phần này đi sâu vào các kỹ thuật lập trình Agent, tối ưu RAG nâng cao, Fine-tuning (LoRA) và đánh giá hệ thống (RAGAS).

### 1. Advanced Agent Patterns
* **Reflexion:** Cơ chế tự phản hồi (Self-reflection). Agent lưu lịch sử sai sót vào bộ nhớ tập phim (Episodic Memory) để lần sau rút kinh nghiệm và sửa lỗi hành động.
* **LATS (Language Agent Tree Search):** Kết hợp tìm kiếm cây Monte Carlo (MCTS) với LLM đóng vai trò bộ đánh giá giá trị (Value function) để duyệt các nhánh quyết định tối ưu.
* **Voyager:** Agent tự học trọn đời thông qua việc tự sinh giáo trình học (Curriculum) và lưu các kỹ năng viết bằng code JavaScript thành thư viện kỹ năng (Skill Library) để tái sử dụng.

### 2. Advanced RAG (GraphRAG & Hybrid Search)
* **GraphRAG vs Flat RAG:** Flat RAG dựa trên khoảng cách Vector (Semantic Similarity) dễ mất đi cái nhìn toàn cảnh (Global queries). GraphRAG trích xuất các Thực thể (Entities), Mối quan hệ (Relationships) để tạo Đồ thị tri thức (Knowledge Graph) và gom cụm thành các Community Summaries nhằm trả lời tốt các câu hỏi dạng khái quát tổng thể.
* **Hybrid Search:** Kết hợp **Dense Retrieval** (Vector search hiểu ngữ nghĩa sâu) và **Sparse Retrieval** (BM25 tìm kiếm từ khóa chính xác). Kết quả được hợp nhất bằng thuật toán **RRF (Reciprocal Rank Fusion)**.
* **Query Translation:** Kỹ thuật viết lại câu truy vấn (Query Rewriting), sinh nhiều câu truy vấn tương tự (Multi-Query), hoặc phân rã câu hỏi phức tạp thành các câu hỏi con (Sub-queries).

### 3. Fine-tuning LLMs (LoRA/QLoRA)
* **Cơ chế LoRA (Low-Rank Adaptation):** Giữ nguyên trọng số gốc \(W_0 \in \mathbb{R}^{d \times k}\), huấn luyện thêm 2 ma trận phân rã hạng thấp \(A \in \mathbb{R}^{r \times k}\) và \(B \in \mathbb{R}^{d \times r}\) với Rank \(r \ll d\). 
  $$\Delta W = B \cdot A$$
  * Giảm số lượng tham số huấn luyện xuống >99% và tiết kiệm bộ nhớ GPU tối đa.
* **QLoRA (Quantized LoRA):** Sử dụng định dạng lượng tử hóa **4-bit NormalFloat (NF4)** cho mô hình gốc, kết hợp với Double Quantization và Paged Optimizers để tránh hiện tượng tràn bộ nhớ GPU (OOM) khi kích thước batch tăng đột biến.
* **FlashAttention:** Tối ưu hóa IO của GPU bằng cách tính toán Attention trực tiếp trên bộ nhớ SRAM tốc độ cao theo từng khối (Tiling), tránh việc ghi và đọc liên tục các ma trận kích thước lớn từ bộ nhớ HBM có độ trễ cao.

### 4. RAGAS Metrics
Đánh giá RAG tự động dựa trên LLM-as-Judge chia làm 4 chiều chính:
1. **Faithfulness (Độ trung thực):** Câu trả lời tạo ra có được suy ra trực tiếp từ Context được truy xuất hay không? (Chống ảo giác - Hallucination).
2. **Answer Relevance (Độ liên quan của câu trả lời):** Câu trả lời có giải quyết đúng trọng tâm câu hỏi của User không?
3. **Context Precision (Độ chính xác của ngữ cảnh):** Context được truy xuất có chứa thông tin hữu ích nằm ở các vị trí đầu tiên không?
4. **Context Recall (Độ phủ của ngữ cảnh):** Context truy xuất được có bao phủ toàn bộ câu trả lời chuẩn (Ground Truth) không?

---

## CÂU HỎI ÔN TẬP THỰC CHIẾN

### Dạng 1: Trắc nghiệm chuyên sâu & Multi-Select

#### Câu 1 (Multi-select): Khi nào bạn nên chọn Fine-tuning (LoRA/QLoRA) thay vì RAG cho hệ thống AI của doanh nghiệp? (Chọn tất cả các đáp án đúng)
- [ ] A. Khi cần bổ sung kiến thức động, thay đổi liên tục theo thời gian thực (như giá cổ phiếu, tin tức hàng ngày).
- [x] B. Khi cần thay đổi phong cách viết (Tone & Voice), định dạng đầu ra cực kỳ nghiêm ngặt (ví dụ: luôn trả về JSON chuẩn).
- [ ] C. Khi cần trích xuất nguồn gốc thông tin (Citations) chính xác từ tài liệu nội bộ để người dùng kiểm chứng.
- [x] D. Khi cần tối ưu hóa mô hình nhỏ (như Llama-3-8B) để đạt hiệu năng xử lý một tác vụ chuyên biệt tương đương với mô hình lớn (như GPT-4) nhằm giảm độ trễ và chi phí API.

*Giải thích:* RAG phù hợp nhất cho kiến thức động (A) và trích xuất nguồn thông tin kiểm chứng (C). Fine-tuning tối ưu nhất cho việc thay đổi hành vi, định dạng đầu ra (B) và huấn luyện mô hình nhỏ chuyên biệt để tiết kiệm tài nguyên (D).

#### Câu 2 (Single choice): Trong cơ chế QLoRA, kỹ thuật "Double Quantization" có vai trò gì?
- ( ) A. Lượng tử hóa cả mô hình gốc và các ma trận adapter LoRA xuống 4-bit.
- ( ) B. Lượng tử hóa mô hình gốc hai lần bằng hai phương pháp NF4 và FP4 khác nhau.
- [x] C. Lượng tử hóa thêm các tham số hằng số của chính quá trình lượng tử hóa trước đó (Quantization Constants), giúp tiết kiệm thêm khoảng 0.37 bits/parameter.
- ( ) D. Nhân đôi số lượng GPU ảo dùng cho huấn luyện thông qua ảo hóa bộ nhớ.

*Giải thích:* Double Quantization là quá trình lượng tử hóa các hằng số lượng tử hóa, giúp giảm lượng bộ nhớ cần thiết để lưu trữ siêu tham số lượng tử hóa mà không làm suy giảm độ chính xác của mô hình.

---

### Dạng 2: Scenario Debug (Sửa lỗi Code & Kiến trúc)

#### Tình huống:
Bạn xây dựng một luồng Agent tự sửa code bằng **LangGraph**. Luồng hoạt động như sau:
1. Node `generate_code` gọi LLM để viết code.
2. Node `test_code` chạy code vừa sinh ra qua bộ unit test.
3. Nếu tất cả test pass, chuyển sang Node `end`.
4. Nếu test fail, chuyển sang Node `debug_code` để LLM sửa code dựa trên log lỗi, sau đó chuyển ngược lại Node `test_code`.

Dưới đây là đoạn code cấu hình đồ thị của bạn:

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

#### Câu hỏi Debug:
1. **Lỗi nghiêm trọng nào** có thể xảy ra với đồ thị trên khi LLM không thể tự sửa được một lỗi code cứng đầu?
2. **Cách khắc phục:** Sửa đổi `AgentState` và hàm `route_after_test` như thế nào để ngăn chặn lỗi trên trên môi trường Production?

#### Lời giải chi tiết:
1. **Lỗi xảy ra:** Hiện tượng **Vòng lặp vô hạn (Infinite Loop / Circular Loop)**. Nếu LLM liên tục viết sai code và test fail, luồng sẽ chạy mãi mãi giữa `test_code` -> `debug_code` -> `test_code` -> `debug_code`. Điều này dẫn đến treo hệ thống, cạn kiệt tài nguyên bộ nhớ và làm phát sinh chi phí API LLM khổng lồ (bị sập thẻ tín dụng).
2. **Cách khắc phục:** Sử dụng kỹ thuật giới hạn số vòng lặp tối đa (Max Iterations Guard). 
   * Cập nhật `iterations` trong `AgentState`.
   * Kiểm tra điều kiện `iterations >= MAX_ITERATIONS` tại hàm rẽ nhánh để ép buộc thoát luồng hoặc trả về thông báo lỗi cho User.

**Code sửa đổi:**

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

### Dạng 3: Case Study Thiết kế Hệ thống (RAG & Agent)

#### Yêu cầu bài toán:
Doanh nghiệp X muốn xây dựng một hệ sinh thái AI hỗ trợ khách hàng tra cứu thông tin sản phẩm và tự động thực hiện các tác vụ như: Kiểm tra đơn hàng, Hoàn tiền, hoặc Đổi trả sản phẩm. Hệ thống yêu cầu:
1. Tra cứu chính xác từ tập dữ liệu PDF hướng dẫn sử dụng sản phẩm lớn (hơn 10,000 trang).
2. Gọi API hệ thống CRM để lấy thông tin đơn hàng và thực hiện hoàn tiền.
3. Phải đảm bảo an toàn tuyệt đối, không được tự động hoàn tiền vượt quá 5.000.000 VNĐ mà không có sự phê duyệt của con người.

#### Hãy thiết kế kiến trúc hệ thống bằng cách trả lời các câu hỏi sau:
1. Bạn chọn kiến trúc RAG nào để tra cứu hiệu quả trên 10,000 trang tài liệu phức tạp? (Gợi ý: Phân chia Chunking, Indexing).
2. Áp dụng Design Pattern nào cho tác vụ phê duyệt hoàn tiền tự động? Cấu hình luồng xử lý cụ thể ra sao?
3. Thiết kế hệ thống Guardrails bảo vệ luồng thanh toán hoàn tiền này.

#### Hướng dẫn trả lời Case Study:
1. **Kiến trúc RAG nâng cao:**
   * *Chunking & Indexing:* Không thể dùng Flat RAG cơ bản. Cần sử dụng **Parent-Child Chunking** (lưu trữ các chunk nhỏ chứa ngữ nghĩa chi tiết để tìm kiếm Vector, nhưng khi đưa vào LLM thì mở rộng ra Parent Chunk lớn hơn để đủ ngữ cảnh). Kết hợp xây dựng **Semantic Chunking** dựa trên cấu trúc đề mục tài liệu.
   * *Search:* Áp dụng **Hybrid Search (BM25 + Vector Embeddings)** kết hợp thuật toán rerank **Cohere Rerank** để lọc ra top 5 chunks chất lượng nhất.
2. **Design Pattern Phê duyệt (Human-in-the-Loop - HITL):**
   * Áp dụng cơ chế **Bounded Autonomy (Tự trị trong ranh giới)** và **State Persistence (Lưu trạng thái)** của LangGraph.
   * Khi người dùng yêu cầu hoàn tiền: Agent kiểm tra số tiền. Nếu số tiền \(\le\) 5.000.000 VNĐ, Agent tự động gọi API hoàn tiền.
   * Nếu số tiền > 5.000.000 VNĐ, Agent lưu trạng thái vào DB (Checkpoint), gửi thông báo phê duyệt tới Dashboard của nhân viên CSKH và **tạm dừng luồng (Interrupt)**. Sau khi nhân viên CSKH bấm nút phê duyệt (Approve/Reject), luồng Agent sẽ đọc tiếp Checkpoint và đi tiếp hành động tương ứng.
3. **Thiết kế Guardrails:**
   * *Input Guardrail:* Kiểm tra câu lệnh nhập vào có dấu hiệu Prompt Injection ép buộc hoàn tiền hay không.
   * *Output Guardrail:* Chặn không cho mô hình tự sinh mã xác thực hoàn tiền giả lập hoặc xuất thông tin thẻ tín dụng của khách hàng khác (rò rỉ PII).

---

## LIÊN KẾT HỌC TẬP (Xem chi tiết tại các ngày học)
* Chi tiết về kiến trúc Agent nâng cao (Reflexion, LATS): [[day16_track3]]
* Chi tiết về thiết kế RAG thực tế và tối ưu RAGAS: [[day18_track3]] và [[day24_track3]]
* Chi tiết về GraphRAG & Đồ thị tri thức: [[day19_track3]]
* Chi tiết về Fine-tuning LoRA/QLoRA: [[day21_track3]] và [[day22_track3]]
* Chi tiết về LangGraph và Human-in-the-Loop: [[day23_track3]] và [[day27_track3]]
* Chi tiết về Circuit Breakers & Caching tối ưu vận hành: [[day25_track3]]
