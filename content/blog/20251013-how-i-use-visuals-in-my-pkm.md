---
title: "One Year Later: How I Use Visuals in My PKM (Sketch Your Mind Conference)"
date: 2025-10-13T13:33:18-07:00
draft: false
tags: ["observability", "presentation", "obsidian", "excalidraw", "visual thinking", "grafana labs", "metrics", "logs", "loki", "prometheus", "grafana", "english"]
---
Today I gave [a talk](https://sketch-your-mind.com/2025/sessions/nicole/) at my friend Zsolt Viczián's [Sketch Your Mind Conference](https://sketchyourmind.com/) about how I use visuals in my PKM, a follow-up to my video about Obsidian Excalidraw last year where I shared that I'd changed all my Obsidian templates to hybrid Obsidian Excalidraw notes:

{{< youtube zmgqMZi6QL8 >}}

In the talk, I shared how I've evolved my use of visuals in my PKM over the last year, including:
- Referring to icon and logo libraries that dynamically compile all the atomic visuals I use in my notes
- Adopting a visual Zettelkasten-like approach
- Creating notes at conferences to track people I've met and talks I've attended
- Using Obsidian Excalidraw to create compelling presentations in lieu of slides
- Combining visuals with audio recordings to create literature notes of books I'm reading
- Using a full observability pipeline to monitor and analyze the notes in my Obsidian vault

I was particularly excited about the last point. I work at Grafana Labs and help people monitor their computer systems using opensource software. I realized that I could use the same tools to monitor my PKM system, so I set up a pipeline where a Python script scrapes note metadata, and sends information to Loki and Prometheus via Alloy, and then I visualize it all in Grafana. It's a pretty nerdy and totally unnecessary setup, but [here's the repo](https://github.com/nicolevanderhoeven/obsidian-grafana) for anyone interested in replicating it.