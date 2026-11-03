---
title: "Context Engineering Fundamentals (The Context Window #06)"
date: 2026-10-02T18:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "livestream", "grafana labs", "the context window", "context engineering", "context", "ai agents", "rag", "embeddings"]
---

What actually counts as "context" for an AI agent — and how does it find the right things to put in a limited window? In this episode of *The Context Window* — Grafana's livestream series on AI in observability — I dig into **context engineering fundamentals** with [Ben Sully](https://www.linkedin.com/in/ben-sully/) and [Ioanna Armouti](https://www.linkedin.com/in/ioanna-armouti/). We treat the context window as an **attention budget**, walk through Assistant Search and semantic retrieval, embeddings, and how you actually *evaluate* whether the retrieved context was any good.

{{< youtube Vn04wQ0T9PU >}}

## What we cover

- **What counts as context** — and why the context window behaves more like an *attention budget* than just a size limit.
- **Finding the right context** — Assistant Search, semantic retrieval, and embeddings: how an agent surfaces what it needs instead of being handed everything.
- **Evaluating retrieved context** — because retrieval that *looks* relevant isn't the same as retrieval that *is*.
- **The tool tax and tool deferral** — every tool definition costs context, so when do you load it versus defer it?
- **Progressive disclosure and long-term memory** — giving the agent what it needs, when it needs it.
- **Why removing 80% of a system prompt can change nothing** — a nice illustration that more context is not automatically better context.

## Resources

- [My notes on Context Engineering](https://notes.nicolevanderhoeven.com/Context+Engineering)
- [My notes on Context](https://notes.nicolevanderhoeven.com/Context)
- [My notes on Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant)

