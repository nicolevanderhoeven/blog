---
title: "When to use Grafana Assistant vs MCP vs GCX: Grafana GCX"
date: 2026-08-21T09:00:00+01:00
draft: false
tags: ["grafana", "english", "video", "grafana labs", "gcx", "ai", "short"]
---

Three AI tools people confuse: Assistant, MCP, and GCX. [Last time]({{< ref "20260819-when-to-use-grafana-mcp.md" >}}) I talked about the easy hand — the MCP server. Now the *power* hand: **GCX**, a CLI built for AI agents.

{{< youtube bWtlNE8GdAI >}}

If Assistant is the brain and Grafana MCP is the easy hand, then GCX is the **power hand** — a CLI built for an agent to drive. (Quick refresher: a **CLI** is a command line interface — no clicking, just typed commands.)

So when does GCX win?

- **When you're using terminal coding agents** — Claude Code, Cursor, Codex. It writes code, pulls the exact log or metric, and verifies against it — without leaving the editor.
- **When you need *everything.*** GCX wraps the *entire* Grafana Cloud API — SLOs, Synthetics, IRM, k6, Fleet — the esoteric corners MCP skips. The full banana.
- **When you want automation and CI/CD.** Dry-run mode, JSON output, and exit codes an agent can act on — built for GitOps.

Do you need Grafana Assistant for this? **No — not even a subscription.** Bring your own brain, same as MCP: metrics, logs, dashboards, and alerts run on nothing but a service account token. You only really pay for Assistant if you call `gcx assistant` directly — which taps its reasoning, billed separately.

So there's your map: **Assistant's the brain, MCP's the easy hand, GCX is the power hand.** It's not one versus another — they work really well together to give you the best choice in how to access your Grafana stack.

## Transcript

I'm differentiating Assistant, Grafana MCP and GCX and in this one I'm talking about **GCX**. If Assistant is the brain and Grafana MCP is the easy hand, then GCX is the power hand — a CLI built for AI agents.

Quick refresher: a **CLI** is a command line interface — no clicking, just typed commands. GCX is a CLI built for an agent to drive.

So when does GCX win?

- **When you're using terminal coding agents** — Claude Code, Cursor, Codex. It writes code, pulls the exact log or metric, and verifies against it — without leaving the editor.
- **When you need *everything.*** GCX wraps the *entire* Grafana Cloud API — SLOs, Synthetics, IRM, k6, Fleet — the esoteric corners MCP skips — the full banana.
- **When you want to do automation and CI/CD.** Dry-run mode, JSON output, exit codes an agent can act on — built for GitOps.

Do you need Grafana Assistant for this? **No — not even a subscription.** Bring your own brain, same as MCP: metrics, logs, dashboards, alerts run on nothing but a service account token. You only really pay for Assistant if you call `gcx assistant` directly — which taps its reasoning, billed separately.

So there's your map: **Assistant's the brain, MCP's the easy hand, GCX is the power hand.** It's not one versus another. They actually work really well together to give you the best choice in how to access your Grafana stack.

## Resources

- [My notes on GCX](https://notes.nicolevanderhoeven.com/GCX)
- [When to use Grafana Assistant]({{< ref "20260817-when-to-use-grafana-assistant.md" >}})
- [When to use Grafana MCP]({{< ref "20260819-when-to-use-grafana-mcp.md" >}})

