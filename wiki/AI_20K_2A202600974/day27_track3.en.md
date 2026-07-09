---
type: summary
title: "Summary: Day 27 Track 3 - Human-in-the-Loop UX"
description: "A summary on designing Human-in-the-Loop (HITL) interactions, bounded autonomy, and approval workflows for AI agents."
tags: [human-in-the-loop, ai-agents, ux, langgraph, governance]
timestamp: 2026-07-05
sources: ["../raw/AI_20K_2A202600974/27/Day12 - Track 3 - Human-in-the-loop-ux-khi-nao-agent-can-xin-phep.pdf"]
---
# Day 27 Track 3 - Human-in-the-Loop UX

This document summarizes the Day 27 Track 3 lecture on the User Experience (UX) of Human-in-the-Loop (HITL) systems, focusing on when and how AI agents should ask for human permission.


## 1. The Danger of Full Autonomy

Allowing an AI agent full autonomy can lead to catastrophic consequences if the agent makes a high-confidence but incorrect decision (e.g., deleting a database without approval). 
The 2026 industry standard shifts from "full autonomy" to **Bounded Autonomy**: agents can act automatically within defined safe boundaries (e.g., read/search), but must ask for permission when crossing risk boundaries (e.g., side-effects, sending emails, prod deployments).


## 2. HITL Taxonomy - 6 Interaction Patterns

There is a spectrum from Full Manual to Full Auto. The "sweet spot" depends on risk and trust. The 6 key interaction patterns are:


1. **Approval:** For side effects (e.g., Deploy, delete data).
2. **Clarification:** For ambiguous inputs (e.g., "Report Q1 or Q2?").
3. **Structured Elicitation:** For missing mandatory fields (e.g., form to select environment).
4. **Review Checkpoint:** For inspecting draft outputs (e.g., Code PRs, draft emails).
5. **Edit / Correction:** Allowing humans to edit arguments before execution.
6. **Escalation:** Bumping decisions to higher authorities for legal/security risks.

## 3. Confidence Routing: When to Interrupt?

Agents shouldn't interrupt solely based on a single confidence score. Interruptions should occur based on heuristic action classes:


- **Reversible?** If yes, prefer auto-execution.
- **External Side-effects?** If yes, require review/approval.
- **Missing Information?** If yes, ask using structured forms.

*Note:* Policy-aware gating is crucial. Even a highly confident model must stop if it touches sensitive data or strict policy boundaries.


## 4. Approval Workflows & Implementation

Using tools like **LangGraph**, HITL can be programmed systematically:


- **Interrupt / Resume:** Pause at policy nodes, allowing humans to approve, edit, or reject. Resuming must happen on the same thread/checkpoint.
- **Granular Decisions:** Define per-tool policies (e.g., `send_email` allows `approve/edit/reject`, while `ask_user` allows `respond`).
- **Review Cards & Structured Forms:** Instead of simple Yes/No modals, present users with Review Cards containing What/Why/Risk/Rollback info, alongside editable fields.

## 5. 2026 Product Landscape

Big tech companies are converging on bounded autonomy:


- **OpenAI Codex:** Separates permission boundaries from reasoning. Supports `requestUserInput` and async remote approvals.
- **Anthropic Claude Code:** Exposes permission modes (default, acceptEdits, plan, auto) directly to the user, with programmable hooks.
- **Google Gemini (Computer Use):** Pauses right before the final irreversible step (e.g., clicking "Confirm Purchase").
- **Cursor:** Reduces approval fatigue with Plan Mode and Auto-review (using classifier subagents).

## 6. Feedback Loops, Analytics & Audit Trails

To safely scale autonomy, robust tracking is required:


- **Audit Trails:** Log *who* (agent & reviewer), *what* (action), *when*, and *why* for compliance (SOC2/GDPR).
- **Decision Analytics:** Track Approval Rate, Review Latency, and Regret Rate. Only increase autonomy when approval rates are high and regret rates are low.

## 7. HITL UX Best Practices

Avoid simple Yes/No prompts for complex actions. Ask early for missing data, ask late for irreversible actions. Reduce cognitive load with dropdowns and scoped approvals (e.g., "approve for this session"). Interruptions should feel like small, structured interactions, not roadblocks.

---

### Day 27 Review Questions

1. According to the lecture, what does the concept of "Bounded Autonomy" in HITL mean?
   - A. The agent is fully autonomous, requiring no human intervention
   - B. The agent can automatically perform any action but must log it
   - C. The agent is autonomous within safe boundaries (read/search) and must ask for permission when crossing risky boundaries
   - D. The agent is only allowed to perform pre-approved actions

2. When should an agent interrupt to ask for a human's opinion, according to the Confidence Routing principle?
   - A. When the agent's confidence score is below 50%
   - B. When the action is reversible and causes external impact
   - C. When the action is reversible, prioritize automation; if it has an external impact or lacks information, it needs review/approval
   - D. Only interrupt when the agent is unsure about the result

3. Among the 6 HITL interaction patterns, which one is used when the agent needs a human to review draft output (e.g., code PR, draft email)?
   - A. Approval
   - B. Clarification
   - C. Review Checkpoint
   - D. Escalation
   - *D. Leo thang*

4. According to HITL UX best practices, when should a human be asked in order to reduce cognitive load?
   - A. Always ask early for every action
   - B. Ask early for missing data, ask late for irreversible actions
   - C. Only ask when the action has a high risk
   - D. Ask late for all actions to avoid bothering
