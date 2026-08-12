---
title: "AI Week Day 3: Operations & Maintenance (Grafana AI Week — Wednesday)"
date: 2026-07-29T09:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "video", "short", "grafana labs", "grafana ai week", "grafana assistant", "incident response"]
---

Day three of AI Week is about **operations and maintenance** — because once code reaches production, the operational work is still surprisingly manual: someone's watching dashboards, deciding whether an error spike is real, and writing up what happened, every single day. Two Grafana Assistant features went GA to take that off your plate. **Assistant Automations** handle recurring work — save a prompt and run it on a schedule (like a morning brief on your service's health), each run keeping its own history and able to notify you in Slack. **Assistant Investigations** is for when something actually breaks: it digs across metrics, logs, traces, and profiles, develops and tests hypotheses, and hands you a structured report you can follow along with in a Workspace. You're offloading vigilance, not accountability — the evidence is always there to review, and you still make the call.

{{< youtube 5P7qSKIRSek >}}

## Transcript

It's day three of AI Week, and Wednesday is all about **operations and maintenance**. Because here's the thing: once your code reaches production, the operational work is still surprisingly manual. Someone's watching dashboards, someone's deciding whether that error spike is real, and someone's writing up what happened — every single day.

Today, two features of Grafana Assistant are now generally available to take that burden off your plate: **Investigations** and **Automations**.

**Assistant Automations** handle the recurring work of operating a system. Save an Assistant prompt and run it on a schedule — like a morning brief that summarizes the operational health of your service over the last 24 hours. Every run keeps its own conversation and history, and it can notify you in Slack when it's done or needs approval.

**Assistant Investigations** is for when something actually breaks. Investigations digs into issues across your metrics, logs, traces, and profiles, develops and tests hypotheses, and hands you a structured report. You can follow along in a Workspace, see what's been ruled out, and add guidance while it works.

You're offloading vigilance, not accountability — the evidence and reasoning are always there to review, and you still make the call.

Everything's at **grafana.ai** — see you tomorrow for day four: evaluating your agents.
