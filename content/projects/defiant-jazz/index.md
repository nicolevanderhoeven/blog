---
title: "The Defiant Jazz Incident"
date: 2026-10-30
weight: 20
summary: "An observability murder mystery. A night supervisor is dead, the floor's power was out for five minutes, and the only witnesses are logs, metrics, and traces that you investigate in Grafana."
image: /assets/projects/defiant-jazz-title.webp
repo: https://github.com/nicolevanderhoeven/defiantjazz
tags: ["observability", "game", "grafana", "loki", "tempo", "prometheus", "ai"]
tech_stack:
  - "Grafana"
  - "Grafana Loki"
  - "Grafana Tempo"
  - "Prometheus"
  - "Grafana Assistant"
  - "Grafana MCP server"
  - "gcx"
  - "Python"
  - "Docker Compose"
draft: false
---

**The Defiant Jazz Incident** is a murder mystery you solve with observability tools. It's set on the Sleep Floor at Kipsake, a company that rents your sleep: at night, its Dreamers sleep in pods while their sleepwalking selves work the floor. During the Cocoa Hour, the floor's middle-of-the-night holiday party, the power goes out for five minutes. When it comes back, the night supervisor is dead in the elevator.

Kipsake recorded everything it could: badges, doors, chat, sleep rings, power, microphones, cameras, sleep bands, and personnel records. Your job is to work out who did it, and the only way to do that is through the telemetry.

## How it works

The case file is a set of logs, metrics, and traces. A loader sends them to [Grafana Loki](https://grafana.com/oss/loki/), Prometheus or Mimir, and [Grafana Tempo](https://grafana.com/oss/tempo/), either in Grafana Cloud or in a local Docker stack, and you investigate from there with whatever you like: Grafana itself, Grafana Assistant, an MCP server, `gcx`, or the AI agent of your choice. The data is deliberately messy. Some devices lose clock sync during the outage, some records arrive late, and not everyone on the Sleep Floor remembers what their body did.

The game itself comes in two forms. A terminal version is for demos and playtests: you watch the testimonies and choose what to investigate, while an AI that only sees the telemetry answers your questions. A web version is made to embed in a Grafana dashboard panel right next to the data.

## Why a murder mystery?

Investigating an incident is investigating an incident, whether the victim is a production service or a night supervisor. You start with a vague report, a pile of signals that don't quite agree, and a clock that can't be fully trusted, and you have to build a timeline you can defend. A case with a known answer is a safe way to practice that, to compare how different tools and AI agents cope with it, and to see how good a question you have to ask before the data answers.

## No spoilers

The repository keeps the solution in clearly marked files, and the README tells you which ones to avoid if you want to play. This page deliberately says nothing about who did it.

## Try it

The [repository](https://github.com/nicolevanderhoeven/defiantjazz) has everything: the case brief, the telemetry, the loader, and both versions of the game.
