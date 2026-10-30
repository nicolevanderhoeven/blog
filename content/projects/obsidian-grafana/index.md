---
title: "obsidian-grafana"
date: 2025-10-13
weight: 40
summary: "A full local open source setup for visualizing an Obsidian vault with Alloy, Loki, Prometheus, and Grafana: your notes, treated as telemetry."
image: /assets/projects/obsidian-grafana-dashboard.webp
repo: https://github.com/nicolevanderhoeven/obsidian-grafana
tags: ["obsidian", "grafana", "loki", "prometheus", "alloy", "pkm", "observability"]
tech_stack:
  - "Python"
  - "Grafana Alloy"
  - "Grafana Loki"
  - "Prometheus"
  - "Grafana"
  - "Grafana Assistant"
  - "Docker Compose"
draft: false
---

**obsidian-grafana** turns an [Obsidian](https://obsidian.md) vault into time-series data and dashboards. I work at Grafana Labs, helping people monitor their systems with open source tools, and at some point I realized I could use the same tools to monitor my personal knowledge management system. It's a nerdy and totally unnecessary setup, and I enjoy it a lot. I mention it in my post on [how I use visuals in my PKM](/blog/20251013-how-i-use-visuals-in-my-pkm/).

The screenshot above was made by running the repo's own Grafana setup on a copy of the posts from this website.

## How it works

A Python script reads the Markdown files in your vault and extracts metadata: word, line, and character counts, file size, frontmatter fields, tags, wikilinks, and timestamps. It runs every five minutes and has two paths:

- **A log path for history.** Only the notes that changed since the last run are written, as structured JSON, to a log file. Grafana Alloy tails that file and forwards it to Loki, with tags and frontmatter fields as labels, so you can see how your notes change over time.
- **A metrics path for the current state.** A metrics exporter exposes totals such as note count, word count, unique tags, and wikilinks, and Prometheus scrapes them.

Grafana ties the two together with pre-configured dashboards: an overview, a time series dashboard for individual notes, a relationships dashboard for wikilinks, a dashboard of frontmatter types, and a word cloud of your most used words. Everything runs in Docker Compose.

## What it's useful for

Understanding your writing habits and how your vault grows, checking how consistently your notes are tagged, finding the notes that everything links to, and keeping an eye on notes with a given frontmatter status or priority. The README also covers installing the Grafana Assistant plugin into the local Grafana.

## Try it

The [repository](https://github.com/nicolevanderhoeven/obsidian-grafana) has a quick start. You'll need Docker and Python 3, and a vault to point it at.
