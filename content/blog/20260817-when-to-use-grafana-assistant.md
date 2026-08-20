---
title: "When to use Grafana Assistant vs MCP vs GCX: The Brain"
date: 2026-08-17T09:00:00+01:00
draft: false
tags: ["grafana", "english", "video", "grafana labs", "grafana assistant", "ai", "short"]
---

Grafana has three AI things people keep confusing — Assistant, MCP, and GCX. They're not competitors. Think of it as **a brain and two hands.** In this short, I start with the brain: **Grafana Assistant**.

{{< youtube xo7meD4Yn0k >}}

Assistant isn't just a chatbot — it's the *reasoning layer*. It manages context and knows your Grafana: your dashboards, your data sources, a knowledge graph of your infrastructure. Instead of clicking around, you tell Assistant *what* you want to do and it figures out the *how*.

Reach for the Assistant when the work is **visual or exploratory**:

- **Building a dashboard?** Assistant.
- **"Teach me how to do this" or "where is this in the UI"?** Assistant.
- **A real incident that needs root-cause analysis across multiple data sources?** Assistant. That's its sweet spot — it forms a hypothesis, correlates your signals, and can even open a pull request with the fix.

Here's the key thing though: Assistant is Grafana's *own* brain — but it's **not the only brain that can drive Grafana.** That's where the two hands come in, and I'll cover the first of those (the MCP server) next.

## Transcript

Grafana has three AI things people keep confusing — Assistant, MCP, and GCX. I'm going to talk a bit about each one so you know which one is best for your use case.

Spoiler: They're not competitors. Think of it as **a brain and two hands.**

Let's start with **Grafana Assistant**, which is the brain.

It's not just a chatbot — it's the *reasoning layer*. It manages context, it knows your Grafana: your dashboards, your data sources, a knowledge graph of your infrastructure. So instead of you clicking around to do something, you can say what you want to do to Assistant and it figures out the *how.*

Reach for the Assistant when the work is **visual or exploratory.**

- If you're building a dashboard? Assistant.
- "Teach me how to do this" or "where is this in the UI"? Assistant.
- You have a real incident where you need root-cause analysis across multiple data sources? Assistant.
  - That's its sweet spot — it forms a hypothesis, correlates your signals, and can even open a pull request with the fix.

Here's the key thing though: Assistant is Grafana's *own* brain — but it's **not the only brain that can drive Grafana.** That's where the two hands come in… and I'll show you those next.

## Resources

- [Grafana Assistant](https://grafana.com/products/cloud/ai-tools/) (product page)
- [My notes on Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant)
- [My notes on GCX](https://notes.nicolevanderhoeven.com/GCX)
- [Unlearnings from building Grafana Assistant](https://contexthorizon.substack.com/p/unlearnings-from-building-grafana) — my Context Horizon piece
