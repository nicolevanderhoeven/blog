---
title: "The Great Doubt: What Building an AI Agent Taught Us About Trust (KubeCon Japan 2026)"
date: 2026-07-28T09:00:00+09:00
draft: false
tags: ["observability", "presentation", "AI", "grafana labs", "evals", "llm", "open telemetry", "kubernetes", "kubecon", "grafana", "english"]
---

This week I spoke at [KubeCon + CloudNativeCon Japan 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-japan/) in Yokohama, Japan. I gave a talk called *The Great Doubt: What Building an AI Agent Taught Us About Trust*. Here's the abstract:

> When we started building an AI assistant for observability, we thought the hard part would be making it smart. We were wrong. The hard part was knowing when to trust it.
>
> AI agents hallucinate, forget context, and confidently give wrong answers. Traditional testing doesn't catch these failures. What's needed is evaluation grounded in systematic doubt.
>
> This talk shares lessons from shipping an AI agent to production: how to build a golden dataset of use cases you must get right, how to use LLM-as-judge when there's no ground truth, and how to use OpenTelemetry traces to debug eval failures. You'll also hear what's still unsolved: evaluating multi-agent handoffs and closing the feedback loop between what users ask and what your evals cover.
>
> Kyoto School philosopher Nishitani Keiji called this "The Great Doubt" (大疑): questioning every assumption until only what survives is real. For AI agents, that's not philosophy. It's the job.

The talk walks through the layers of doubt we worked through while building [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant): doubting the agent itself, then doubting our tests, then the LLM-as-judge, then our own scores — and finally doubting whether the doubt was even justified. Each layer needed a different tool, from a golden dataset run in a fully synthetic observability environment, through online evals on live traffic, to per-conversation OpenTelemetry traces that link every eval score back to the exact LLM and tool calls that produced it.

You can find the slides at [nicole.to/doubtslides](https://nicole.to/doubtslides).

I'll update this post with the recording once KubeCon publishes it.

## Resources

Grafana Assistant (generally available for Grafana OSS, Grafana Cloud, and Grafana Play):

- [Docs](https://grafana.com/docs/grafana-cloud/machine-learning/assistant/)
- [Try it out on Grafana Play](https://play.grafana.org)

Assistant Investigations (Grafana Cloud):

- [Docs](https://gra.fan/investigations)

Agent Observability (Grafana Cloud):

- [Docs](https://gra.fan/agento11y)

o11y-bench (OSS):

- [Site](https://gra.fan/o11ybench)

Investigations Arena:

- [Video](https://youtu.be/YPfqchw8LCo)

## Related reading

- My notes on [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant)
- My Context Horizon piece [*Unlearnings from building Grafana Assistant*](https://contexthorizon.substack.com/p/unlearnings-from-building-grafana)
- [*The Way of Zen*](https://amzn.to/4vZNlPD) by Alan W. Watts
- [*Zen Mind, Beginner's Mind*](https://amzn.to/3RgXGIP) by Shunryu Suzuki
- [*Religion and Nothingness, Volume 1*](https://amzn.to/4vQW2eQ) by Nishitani Keiji
- [*Philosophers of Nothingness: An Essay on the Kyoto School*](https://amzn.to/4yFff6d) by James W. Heisig
