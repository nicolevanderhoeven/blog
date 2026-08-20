---
title: "When to use Grafana Assistant vs MCP vs GCX: The Easy Hand (MCP)"
date: 2026-08-19T09:00:00+01:00
draft: false
tags: ["grafana", "english", "video", "grafana labs", "grafana mcp", "mcp", "ai", "short"]
---

Three AI tools people confuse: Assistant, MCP, and GCX. [Last time]({{< ref "20260817-when-to-use-grafana-assistant.md" >}}) I talked about the brain — Assistant. Now hand number one: **the MCP server**, the *easy* hand.

{{< youtube HDmJyo9cyf8 >}}

Grafana MCP — Model Context Protocol — lets *any* AI client reach into Grafana. The magic part: **you bring your own brain.**

Using MCP requires **two pieces**:

- The **client** is your AI app — the brain you bring: claude.ai, ChatGPT, Cursor.
- The **server** is the door into Grafana that exposes the tools.

There are two ways to get that server. The easiest is the **Grafana Cloud hosted** one — already running, auth built in, just connect and go. But you can also **self-host** the open-source one on your own infra.

So when do you reach for Grafana MCP?

- **When you're using hosted chat tools with no terminal** — claude.ai, ChatGPT, your phone. No shell means no CLI, so MCP is the only way in.
- **When you want to bolt Grafana onto a tool you already use** — already in Cursor or Claude? Just add the server. No new workflow.
- **When you want the best discovery out of the box** — the tools describe themselves up front, so even smaller or cheaper models just *know* what's available. No trial-and-error.

One honest catch: those tool definitions *can* eat some context if you load everything — but modern hosts fix that with lazy tool search.

MCP is deliberately curated — it doesn't expose *every* corner of Grafana. So what do you do when you need the esoteric stuff? That's exactly what the power hand, **GCX**, is for — next up.

## Transcript

Three AI tools people confuse: Assistant, MCP, GCX. Last time, I talked about the brain — Assistant. Now hand number one: **the MCP server,** the *easy* hand.

Grafana MCP — Model Context Protocol — lets *any* AI client reach into Grafana. The magic part: **you bring that AI client - you bring your own brain.**

Using MCP requires **two pieces.** The **client** is your AI app — the brain you bring: claude.ai, ChatGPT, Cursor. The **server** is the door into Grafana that exposes the tools.

Two ways to get that server: the easiest way is to use the **Grafana Cloud hosted** one — already running, auth built in, just connect and go. But you can also **self-host** the open-source one on your own infra.

So when do you reach for Grafana MCP?

- **When you're using hosted chat tools with no terminal** — claude.ai, ChatGPT, your phone. No shell means no CLI, so MCP is the only way in.
- **When you want to bolt Grafana onto a tool you already use** — already in Cursor or Claude? Just add the server. No new workflow.
- **When you want the best discovery out of the box** — the tools describe themselves up front, so even smaller or cheaper models just *know* what's available. No trial-and-error.

One honest catch: those tool definitions *can* eat some context if you load everything — but modern hosts fix that with lazy tool search.

But MCP is deliberately curated — it doesn't expose *every* corner of Grafana. So what do you do when you need the esoteric stuff? That's exactly what the power hand is for. Next up is **GCX.**

## Resources

- [Grafana MCP server](https://github.com/grafana/mcp-grafana)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [My notes on GCX](https://notes.nicolevanderhoeven.com/GCX)
