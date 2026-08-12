---
title: "AI Week Day 2: Building (Grafana AI Week — Tuesday)"
date: 2026-07-28T09:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "video", "short", "grafana labs", "grafana ai week", "mcp", "gcx"]
---

Day two of AI Week is all about **building** — the AI tools that help you write software with confidence. Two big announcements went generally available: **gcx** (the Grafana CLI) and the **Grafana MCP server**. Both connect your coding agents — Claude Code, Cursor, and friends — to your Grafana telemetry. The MCP server gives agents opinionated, ready-made tools for the common cases (querying metrics and logs, reading and updating dashboards); gcx is the more flexible, less opinionated option, built for agents from the ground up with read-only guardrails and its own bundle of agent skills. Both work for OSS and Grafana Cloud. The point: when an agent writes your code, it shouldn't be guessing — it should be looking at how your system *actually* behaves in production. That's telemetry-driven development.

{{< youtube Y3QtH94f77U >}}

## Transcript

It's day two of Grafana Labs' AI Week, and Tuesday is all about **building** — the AI tools that help you build software with confidence.

Today we have two big announcements: **gcx** and the **Grafana MCP server** are both now generally available.

Both of them connect your coding agents — think Claude Code or Cursor — to your Grafana telemetry. So what's the difference?

The **Grafana MCP server** gives your agent opinionated, ready-made tools for the most common use cases: querying your metrics and logs, reading and updating dashboards, that kind of thing. You can run it yourself, or use the hosted MCP server with your Grafana Cloud stack — so yes, it works for both **OSS and Grafana Cloud**.

**gcx** is the Grafana CLI, and it's the more flexible, less opinionated option. Agents can explore it and build their own workflows, and it was designed for agents from the ground up, with read-only guardrails so your agent can't touch anything you didn't approve. It works with Cloud stacks and self-managed instances, and it even ships with its own bundle of agent skills.

Why does this matter? Because when an agent writes your code, it shouldn't be guessing — it should be looking at how your system _actually_ behaves in production. That's telemetry-driven development.

Head to **grafana.ai** for everything we're shipping this week, and I'll see you tomorrow for day three.
