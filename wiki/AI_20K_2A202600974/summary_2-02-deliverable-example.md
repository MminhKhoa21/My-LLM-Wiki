---
type: summary
title: "Summary: Day 02 Deliverable Example"
description: "A summary of the Day 02 lab deliverable example detailing problem discovery, workflow mapping, and AI decision making."
tags: [Lab Example, Workflow, Problem Statement, Delivery]
timestamp: 2026-07-05
sources: ["raw/AI_20K_2A202600974/2/2-02-deliverable-example.pdf"]
---

# Summary: Day 02 Deliverable Example

## Overview
This document provides a complete example of the Day 02 lab assignment. It walks through the journey of a Junior Product Manager named Minh as he performs problem scanning, designs current and future workflows, drafts a Problem Statement, and ultimately decides on implementing an AI Workflow solution for automating weekly reports.

## Key Phases

### Phase 1: Individual Problem Scan
- Minh lists various daily pain points using different lenses (repetitive tasks, time-consuming tasks, areas where AI could excel, and pains experienced by others).
- Examples include summarizing Jira/Slack for weekly reports, reviewing PRDs, searching Slack for past decisions, and writing meeting notes.
- **Top Candidates Selected:** Weekly Report, PRD Review, and Slack Search.

### Phase 2: Group Problem Statement (Convergence)
- The group aggregates individual ideas and scores them based on clarity of actor, workflow, pain evidence, measurable impact, lab feasibility, and domain understanding.
- **Selected Problem:** "Weekly Report" is chosen because it has a highly structured workflow, a clear baseline metric (90 minutes), and easily measurable impact.

### Phase 3: Validation and Research
- The group briefly validates the problem with other PMs. They find that the true pain is not just "pulling numbers" but writing the *narrative* from raw data.
- They research existing tools (e.g., Jira Reports, Slack AI, Gemini in Drive) to understand current patterns. The takeaway is that AI should assist in drafting the narrative while a human retains review control.

### Phase 4: Workflow Mapping
- **Current State (90 mins):** Export Jira -> Pull Sheets -> Read Slack -> Compile -> Write Narrative (Bottleneck) -> Format -> Send.
- **Future State (21 mins):** Auto-pull data (Rule) -> Structure data (Workflow/AI) -> Draft narrative (Workflow/AI) -> PM Review & Edit (Human Boundary) -> Send.
- **Impact:** Decreases overall time significantly while maintaining quality through manual review.

### Phase 5: Problem Statement and Decision
- **Problem Statement:** Defines the actor (Junior PM), workflow, bottleneck (writing narrative), impact, success metric (under 30 mins total), and strict boundaries.
- **AI Decision:** 
  - **Rule:** Insufficient because it cannot generate dynamic narratives.
  - **Workflow:** Chosen. Linear process where AI assists specifically in drafting, with PM review.
  - **Agent:** Rejected. Too broad, unneeded autonomy, and higher risks.
- **Final Decision:** **Go** with a small pilot using historical report data to evaluate edit time and AI hallucination rates.

### Phase 6: Individual Reflection
- Reflects on the use of AI during the lab process (e.g., generating mermaid diagrams, brainstorming ideas) and correcting AI when it suggested overly complex Agent solutions prematurely. 
- Emphasizes that the best problems have clear workflows and metrics, and that agents are not the default answer.
