---
title: "AI Week Day 4: Evaluating (Grafana AI Week — Thursday)"
date: 2026-07-30T09:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "video", "short", "grafana labs", "grafana ai week", "evals", "ai evaluation", "k6"]
---

Day four of AI Week is all about **evaluating** — because building an agent is the easy part; *trusting* it is where things get hard. The headline: **Grafana Agent Observability is now generally available** — the tool Grafana built for itself while scaling Assistant, once it grew too complex to evaluate with unit tests. Instrument your agent with the SDK and your conversations, tool calls, traces, latency, token use, and cost all become observable in one place; add evaluators (LLM judges plus deterministic checks) to score quality on live traffic, feed low-scoring conversations into your test suite, and gate CI on experiments comparing a candidate against a baseline. And because evaluator metrics land in Prometheus, you can get paged when a bad prompt change tanks quality. The fun bonus: **k6 agentic testing** — describe a browser test in plain language and an agent embedded in k6 drives the browser, no script required (they proved it by getting it to beat Wordle).

{{< youtube FOHdEm-_DEQ >}}

## Transcript

It's day four of Grafana Labs' AI Week, and Thursday is all about **evaluating** — because building an agent is the easy part. _Trusting_ it is where things get hard.

The big news: **Grafana Agent Observability is now generally available.** This is the tool we built for ourselves while scaling Grafana Assistant, when it grew too complex to evaluate with unit tests. Now it's available to everyone on Grafana Cloud.

Here's how it works: instrument your agent with the SDK, and your conversations, tool calls, traces, latency, token use, and cost all become observable in one place. Then add evaluators — LLM judges plus deterministic checks — to score quality on live traffic. Low-scoring conversations feed your test suite, and experiments let you compare a candidate against a baseline before you ship — you can even make it a CI gate. And because evaluator metrics land in Prometheus, you can get paged if a bad prompt change tanks quality in production.

But my favorite part of today? **k6 agentic testing.** Describe a browser test in plain natural language, and an agent embedded in k6 drives the browser for you — no script at all. And to prove it, we gave it one job: beat Wordle. Go watch that video. I'll wait.

Everything's at **grafana.ai** — see you tomorrow for the finale: using AI where your team already works.
