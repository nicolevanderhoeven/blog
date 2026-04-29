---
title: "All About AI Observability (The Context Window #03)"
date: 2026-04-22T18:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "livestream", "grafana labs", "the context window", "ai observability", "evaluations", "sigil"]
---

In this episode of *The Context Window* — Grafana's livestream series on AI in observability — I'm joined by [Tiffany Jernigan](https://www.linkedin.com/in/tiffanyjerniganm/) and the engineers behind the product, [Alexander Sniffin](https://www.linkedin.com/in/alexandersniffin/) and [Jack Gordley](https://www.linkedin.com/in/jack-gordley/), for a deep dive into AI Observability in Grafana Cloud. We unpack what it actually is (a new way to instrument your AI apps and see canonical data about them, sitting alongside your existing telemetry), what an evaluation is in this context (and the difference between online evals on live traffic and offline evals on dataset conversations), and we walk through real demos: setting up AI Observability and evaluators, the analytics view, instrumenting a local coding agent, and Jack's system prompt analysis tool. We also talk about the things nobody else is talking about — like LLM-as-judge as a method, evaluators that catch the most bugs, and the cheating-LLM phenomenon.

{{< youtube vzygCuuf7JQ >}}

## Timestamps

- 00:00:00 — Introductions
- 00:02:00 — The last month in AI news
- 00:11:09 — What is AI Observability in Grafana Cloud?
- 00:19:20 — What is an evaluation?
- 00:21:05 — The origin of AI Observability
- 00:25:09 — Demo: Setting up AI Observability and evaluators
- 00:32:04 — What is LLM as judge?
- 00:38:43 — Demo: AI Observability Analytics
- 00:40:52 — AI O11y is based on OpenTelemetry
- 00:42:17 — Demo: Instrumenting a local coding agent
- 00:47:18 — Potential future agentic use cases
- 00:52:00 — Evaluators that catch the most bugs
- 01:02:23 — Demo: System prompt analysis
- 01:05:11 — Guess the prompt

## Resources

### News from the episode
- [Claude Opus 4.7 release](https://www.anthropic.com/news/claude-opus-4-7)
- [Gemma 4](https://deepmind.google/models/gemma/gemma-4/)
- [Qwen 3.6](https://qwen.ai/blog?id=qwen3.6)
- [Introducing o11y-bench: an open benchmark for observability agents](https://grafana.com/blog/o11y-bench-open-benchmark-for-observability-agents/)
- [Updates to GitHub Copilot interaction data usage policy](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)
- [GrafanaCON 2026 announcements](https://gra.fan/gcon26)

### AI Observability
- [AI Observability docs](https://grafana.com/docs/grafana-cloud/machine-learning/ai-observability/)
- [Online evaluations on Grafana Cloud](https://grafana.com/docs/grafana-cloud/machine-learning/ai-observability/introduction/#online-evaluation)
- [OpenTelemetry integration with AI Observability](https://grafana.com/docs/grafana-cloud/machine-learning/ai-observability/introduction/#opentelemetry-integration)
- [The Sigil SDK](https://github.com/grafana/sigil-sdk)

### Mentioned
- [OpenCode](https://opencode.ai) — the open-source coding agent Jack instruments
- [Anthropic: Emotion concepts and their function in a large language model](https://www.anthropic.com/research/emotion-concepts-function)
- [OpenClaw](https://openclaw.ai)

### Related reading
- [My Context Horizon piece on benchmarks: *High INT, Low WIS — What LLM benchmarks miss*](https://contexthorizon.substack.com/p/high-int-low-wis-what-llm-benchmarks)
- [My Context Horizon piece on Grafana Assistant: *Unlearnings from building Grafana Assistant*](https://contexthorizon.substack.com/p/unlearnings-from-building-grafana)
