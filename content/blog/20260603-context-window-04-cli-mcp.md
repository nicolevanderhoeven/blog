---
title: "CLI and MCP Basics for AI Agents (The Context Window #04)"
date: 2026-06-03T18:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "livestream", "grafana labs", "the context window", "mcp", "cli", "ai agents", "gcx"]
---

MCP vs CLI: which one should your AI agent actually use? In this episode of *The Context Window* — Grafana's livestream series on AI in observability — I'm joined by [Tiffany Jernigan](https://www.linkedin.com/in/tiffanyjerniganm/) and three of the engineers and PMs behind Grafana's agent tooling: Ben Sully (who wrote the Grafana MCP server), and Ward Bekker and Dafydd Thomas from the team building `gcx`. We get into the two main ways an AI agent can reach the outside world — the Model Context Protocol (MCP) and good old command-line interfaces — and look at when each one makes sense, the tradeoffs around context windows, tool sprawl, token cost, and reliability. We walk through Grafana's cloud and open-source MCP servers along with `gcx`, the Grafana Cloud CLI built for agents, do a live side-by-side demo of both creating an SLO, and talk about how we benchmark them against each other with o11y-bench.

{{< youtube ZR6U4TN8-Cw >}}

## Timestamps

- 00:00:00 — Introductions
- 00:02:49 — The last month in AI news
- 00:10:19 — What is Grafana Assistant?
- 00:12:30 — What does it mean for Assistant to use tools?
- 00:13:30 — What is MCP?
- 00:16:56 — What is a CLI in an AI context?
- 00:19:17 — What are skills?
- 00:24:37 — Can you use a custom MCP server with Grafana Assistant?
- 00:25:55 — Why team MCP?
- 00:28:22 — The context-window cost of MCP tool definitions
- 00:31:50 — Tool discoverability
- 00:39:25 — What is gcx, and why a CLI?
- 00:46:13 — Demo: creating an SLO with MCP vs gcx
- 00:52:58 — Benchmarking MCP vs gcx with o11y-bench
- 00:58:10 — How MCP and gcx relate to Grafana Assistant
- 01:02:35 — k6 MCP vs Grafana MCP
- 01:03:00 — When to use which (decision guide)
- 01:04:29 — Adding the OSS Grafana MCP to Assistant
- 01:05:41 — Turtles all the way down

## Resources

### MCP and CLI for agents
- [Model Context Protocol](https://modelcontextprotocol.io)
- [Grafana MCP server (OSS)](https://github.com/grafana/mcp-grafana)
- [gcx — the Grafana Cloud CLI](https://github.com/grafana/gcx)
- [Introducing o11y-bench: an open benchmark for observability agents](https://grafana.com/blog/o11y-bench-open-benchmark-for-observability-agents/)
- [Grafana Community Slack](https://slack.grafana.com)

### Related reading
- [My Context Horizon piece: *Unlearnings from building Grafana Assistant*](https://contexthorizon.substack.com/p/unlearnings-from-building-grafana)

### More from The Context Window
- [#03: All About AI Observability](/blog/20260422-context-window-03-ai-observability/)
