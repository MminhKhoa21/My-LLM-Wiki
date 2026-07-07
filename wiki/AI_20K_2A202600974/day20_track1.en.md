---
type: summary
title: "Day 20 Track 1: Retention, Engagement & Habit Loop"
description: "Detailed lab instructions for analyzing use cases, defining retention metrics, optimizing onboarding, and applying the Hook Model."
tags: [day20, track1, product-management, retention, habit-loop, engagement, onboarding]
timestamp: 2026-07-05
sources: ["AI_20K_2A202600974/20/student-day20-v1.pdf"]
---
# Day 20 Lab: Retention, Engagement & Habit Loop  

## 1. Overview  

This module focuses on applying product management concepts—from use case discovery to defining core actions, retention metrics, onboarding journeys, and building habit loops. The goal is to build upon a prototype (from Day 18) and optimize it for user activation and engagement.  

## 2. Customer Retention Canvas & Use Case  

Understanding the **Use Case** and **Persona** is the foundation of retention.  

* **The Problem:** Defined in the user's own words.  

* **The Persona:** Specifically targeted individuals, including their roles and goals. Also identifying the **Anti-persona** (who the product is *not* for).  

* **The Why:** The core motivation or outcome the persona seeks.  

* **The Alternative:** How the user currently solves the problem (e.g., manually, using Google, asking someone).  

* **The Frequency:** How often the problem naturally occurs (daily, weekly, monthly, quarterly). This determines the natural rhythm of product usage.  

## 3. Core Action and Retention Metric  

* **Core Action:** The specific behavior that demonstrates the user has received value (e.g., completing a language lesson, taking a ride). It is not merely logging in or opening the app.  

* **Active User:** Defined by the completion of the Core Action within a specific timeframe.  

* **Retention Metric:** Must align with the natural frequency.  
  * *Daily natural frequency:* DAU, D1/D7/D30 Retention.  
  * *Weekly natural frequency:* WAU, weekly cohort retention.  
  * *Monthly natural frequency:* MAU.  

## 4. Onboarding to First Core Action  

The onboarding journey must lead users to their **First Core Action** and **Aha Moment** as efficiently as possible.  

* **Audit Flow:** Identify steps to Keep, Remove, Delay, or Simplify.  

* **Time to First Core Action:** Measure and minimize the time it takes.  

* **Time to Value (TTV):** Measure the time until the user experiences the product's value.  

* **Recovery Paths:** Design flows to handle drop-offs, missing data, or permission denials without leading to dead ends.  

## 5. Measurement Ladder & North Star Metric  

* **Measurement Ladder:** A structured approach from Marketing/Traffic -> Usage/Active -> Activation & Retention -> Engagement & Stickiness -> Business Value (Revenue, LTV, CAC).  

* **North Star Metric:** The single leading indicator that reflects core value creation.  

* **Input Metrics:** Up to three metrics that directly drive the North Star Metric. Must be distinguished between leading and lagging indicators.  

## 6. Nature vs Nurture & The Hook Model  

* **Nature:** The natural frequency of the user's problem.  

* **Nurture:** Proactive steps the product takes (notifications, emails, triggers) to amplify that natural frequency.  

* **Hook Model (Nir Eyal):**  
  1. **Trigger:** Internal (user's emotion/need) and External (notifications, UI prompts).  
  2. **Action:** The simplest behavior to get the reward. Must minimize friction (Time, Brain cycles, Money, Physical effort).  
  3. **Variable Reward:** Satisfying the user's need through the Tribe (social), the Hunt (resources), or the Self (mastery).  
  4. **Investment:** What the user puts into the product (data, content, reputation) that makes the next trigger more likely.  

## 7. Metric Tracking Requirements  

Define exactly how metrics will be tracked in the product:  

* Define event names, triggers, and properties.  

* Ensure data hygiene (e.g., avoiding duplicate events on refresh).  

* Tie every tracked event directly back to a specific metric from the Measurement Ladder.  
