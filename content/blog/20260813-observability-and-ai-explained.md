---
title: "Observability and AI explained"
date: 2026-08-13T09:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "video", "grafana labs", "grafana assistant", "ai observability"]
---

"AI observability" gets thrown around a lot, and it can mean one of two very different things. So in this video I map out the whole landscape of AI-related work at Grafana across the entire software development lifecycle — and show how AI and observability come together in two directions: **AI for observability** (AI that helps you observe your systems) and **observability for AI** (observing the AI itself).

The framing is deliberate: AI in observability isn't about replacing engineers. It's about handing back the exhausting parts of the job — the 3am triage, the repetitive queries, the report nobody wanted to write — so you can spend your energy on the work only humans can do.

I walk through each phase of the lifecycle and where the tools fit:

- **Planning** — clarity about what's really going on, with [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana%20Assistant): not just a chatbot, but an agent that knows your telemetry, writes your queries, and builds your dashboards.
- **Building** — momentum without losing control: Assistant, the open-source [GCX](https://notes.nicolevanderhoeven.com/GCX) CLI, the Grafana MCP server, the specialized Loki/Tempo/k6 MCP servers, and the AI SDK for building your own agents in Go.
- **Operating** — staying calm under load: Investigations for agentic incident triage, Assistant Automations and the Watcher Agent for staying proactive, plus [Grafana Machine Learning](https://notes.nicolevanderhoeven.com/Grafana%20Machine%20Learning) (Metrics Forecasting, Outlier Detection) and Adaptive Telemetry.
- **Testing & evaluating** — [doubt is a form of care](https://notes.nicolevanderhoeven.com/Doubt%20is%20a%20form%20of%20care): [k6](https://notes.nicolevanderhoeven.com/k6%20%28tool%29) and agentic testing on the systems side, and Agent Observability plus the open-source o11y-bench benchmark on the "observing your AI" side.
- **Collaborating** — bringing it all to where your team already works: Assistant in Slack (and coming to Teams), on mobile, on the desktop, and via API/MCP, plus Assistant Search across your Grafana artifacts.

If you're new to the Grafana stack itself, start with my open source observability video for the non-AI foundations that all of this builds on.

{{< youtube OTmgMF6gD1k >}}

## Resources

- My notes on [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana%20Assistant)
- My notes on [GCX](https://notes.nicolevanderhoeven.com/GCX)
- My notes on [k6](https://notes.nicolevanderhoeven.com/k6%20%28tool%29)
- [o11ybench.ai](https://o11ybench.ai) — the open leaderboard for AI agents doing observability work
