---
title: "Do Androids Dream of Second Brains?"
date: 2026-05-18T07:00:00+01:00
draft: false
tags: ["pkm", "english", "video", "obsidian", "ai", "observability", "grafana assistant", "openclaw"]
---

We often describe our personal knowledge management systems as "second brains" — but can we really say they think for themselves? In this video, I make the case for instrumenting your vault with an observability stack and layering AI on top, not because it'll turn your notes into a brain, but because it might get us closer than anything else has.

{{< youtube BeuaPO0Ezuk >}}

This is the video version of the talk I gave at [PKM Summit 2026](/blog/20260321-do-androids-dream-of-second-brains/) in Utrecht earlier this year, with the live demos cleaner and the dashboards working without the conference wifi gods getting in the way.

## What I cover

### 🐑 Why "second brain" is the wrong framing

I take a small detour through Philip K. Dick's *Do Androids Dream of Electric Sheep?* — the inspiration for *Blade Runner* — and the Voigt-Kampff test, which measures empathy through observed responses to staged scenarios. It's a useful lens for asking what we actually mean when we say a knowledge system "thinks": we're really asking whether it can respond to us in a way that surprises us. Most second-brain setups can't, yet.

### 📊 Observability for PKM

Observability is a concept I've borrowed wholesale from how we monitor software systems — the idea that you can understand a complex system by what it emits, not by reading its internals. Three steps: instrumentation, analysis, improvement. I walk through what each one looks like for a personal vault:

- **Instrumentation**: a small script that emits metrics about my Obsidian vault — note counts, link density, growth over time, what folders are loud and which are quiet
- **Analysis**: a Grafana dashboard sitting on top of Loki + Prometheus, surfacing things I genuinely didn't know about my own vault
- **Improvement**: the part where seeing the data actually changes how you work

There's a live dashboard tour, and a section where I ask **Grafana Assistant** to edit the dashboard for me in natural language — including writing the PromQL queries I never want to write by hand.

### 👁️ Meet Iris

About halfway through the video I introduce **Iris** — the AI agent I built using [OpenClaw](https://openclaw.ai) that lives in my vault, reads my notes, and works alongside me. I walk through:

- What "agentic AI" actually means in practice (vs. just chatting with an LLM)
- The OpenClaw setup — Docker sandbox, Syncthing, the whole pipeline
- Iris rewriting my observability map of content
- Iris doing talk-topic analysis on my vault
- Iris running benchmark research for a blog post
- Iris OCRing my reMarkable handwriting

### 🌙 Dreaming

The last section is the one I had the most fun with. I argue that the thing most second-brain setups are missing isn't *more notes* or *better search* — it's **synthesis**. The capacity to take everything you've captured and surface patterns, contradictions, and ideas you hadn't formed yet.

I introduce OpenClaw's *dreaming* feature: a memory consolidation process inspired by how sleep stages work in the brain. Light sleep, REM, and deep sleep each do different work — surfacing recent material, finding unexpected connections, and consolidating long-term memory. I show how each phase actually behaves in my own system.

And there's a Zhuangzi reference. (You'll see.)

## Resources

- 🎤 [PKM Summit 2026 talk recap (with photos)](/blog/20260321-do-androids-dream-of-second-brains/)
- 🎞 [Slides](https://nicole.to/androids)
- 👁️ [OpenClaw](https://openclaw.ai)
- 📓 [Obsidian](https://obsidian.md)
- 🔄 [Syncthing](https://syncthing.net)
- 📊 [Grafana](https://grafana.com)

### Related reading

- [*The Architecture of Forgetting*](https://contexthorizon.substack.com/p/the-architecture-of-forgetting) — the essay version of why memory consolidation matters
- [*Unlearnings from building Grafana Assistant*](https://contexthorizon.substack.com/p/unlearnings-from-building-grafana)

If you want to follow more of how Iris works and what I'm learning about AI + PKM, [Context Horizon](https://contexthorizon.substack.com) is where I write about it.
