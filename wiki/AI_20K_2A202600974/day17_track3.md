---
type: summary
title: "Memory Systems for Agents (Track 3)"
description: "Summary of Day 17 Track 3 on designing memory systems for AI agents, including Short-term, Long-term, Episodic, and Semantic memory."
tags: [AI_20K_2A202600974, Day17, AI_Agents, Memory]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/17/Day17 - Track 3 - Memory-systems-for-agents.pdf"]
---

# Memory Systems for Agents (Day 17 - Track 3)

This track addresses a major challenge in deploying AI agents: agents are stateless by default and "forget" information between sessions. A robust memory system combines the fast access of the context window with the persistent storage of external databases.

## 4 Types of Cognitive Memory for Agents

1. **Short-term (Working) Memory:** Managed within the LLM context window. Fast, temporary, and limited by token budget. Best managed via a sliding window strategy (system prompt + summary + last K turns) to avoid hitting token limits.
2. **Long-term (Declarative) Memory:** Persistent across sessions, storing user profiles, preferences, and facts (e.g., using Redis). Info is loaded into the system prompt when a new session begins.
3. **Episodic Memory:** A sequential log of past experiences and reflections (e.g., "I tried approach X and it failed because of Y"). Useful for learning from past trajectories.
4. **Semantic Memory:** Domain knowledge encoded into embeddings and stored in a Vector DB. Agents retrieve relevant facts via cosine similarity search.

## Implementation & Frameworks

- **Memory Management Flow:** Buffer (Context Window) -> Summarize (LLM call) -> Extract Key Facts -> Persist (External Store like Redis or Chroma).
- **LangGraph Integration:** Specialized nodes for loading memory (`retrieve_memory`) and saving memory.
- **Frameworks:** Mem0 and Zep provide managed memory layers with auto-classification and smart retrieval, but custom implementations offer more control.
- **Privacy-by-Design:** Crucial for agent memory. Includes data minimization, TTL storage limitation, and mechanisms for "Right to be Forgotten".

## Trends in Agent Memory (2025-2026)

1. **Cross-session memory:** Shifting from thread-scoped history to user-scoped profiles and episodic stores.
2. **Compaction:** Instead of retaining full transcripts, agents compact sessions into summaries, decisions, and durable notes to preserve token budgets and improve accuracy.
3. **Identity Files:** Using configuration files like `AGENTS.md` and `SOUL.md` as control planes for agent identity and rules, separate from retrieval memory.
4. **Heartbeat Loops:** Agents wake up periodically in the background to refresh states, clean notes, and process backlogs.
5. **Compiled Knowledge Base (LLM Wiki):** Instead of raw RAG on documents, the LLM continuously curates and edits a "wiki" of concepts, entities, and timelines, solving the problem of repetitive RAG queries on the same corpus.
