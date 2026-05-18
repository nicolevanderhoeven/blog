---
title: "Continuous Profiling, the OpenTelemetry Way (Grafana ❤️🔥 OpenTelemetry Community Call #7)"
date: 2026-05-18T05:00:00+01:00
draft: false
tags: ["opentelemetry", "english", "video", "grafana labs", "grafana otel community call", "profiling", "pyroscope", "continuous profiling", "flame graphs"]
---

In this community call, I sat down with my coworker **Christian Simon**, who works on Grafana Pyroscope, to dig into profiling as the **fourth signal** in OpenTelemetry. Metrics, logs, and traces are the classic three pillars — but a significant portion of latency lives *inside* a span, in the actual code execution, where the other three can't see. Profiling fills that gap by giving you continuous, code-level visibility into where time is being spent.

{{< youtube N47wy9pp7Lo >}}

## What we covered

### 🔥 Profiling as the fourth signal

Most observability conversations stop at logs, metrics, and traces. But when you see a slow span and ask *"what was the code actually doing?"* — none of the three pillars can answer. Christian made the case that profiling is the missing piece: continuous, low-overhead, code-level visibility, typically visualized as flame graphs that attribute latency to specific functions and execution paths.

### 📊 What flame graphs actually tell you

If you haven't worked with flame graphs before: wide bars = lots of time spent in that function, and the stack reads bottom-up. Once you understand how to read them, they become surprisingly fast to interpret. We walked through what to look for and how to spot the patterns that matter.

### 🌐 The current state of profiling in OpenTelemetry

Profiling is the newest signal to enter the OpenTelemetry spec, and the conversation around it is still evolving. Christian gave a clear-eyed status update on where things are — what's stable, what's experimental, and what the path to GA looks like.

### 🚀 Running profiling in production

The most common pushback on continuous profiling is *"what's the overhead?"* — and the honest answer is that modern continuous profilers typically add 1–3% CPU overhead, which makes them safe to run in production all the time. We talked through deployment patterns, including Kubernetes / containerized environments, and how to think about cost and storage.

### 🧵 Correlating profiles with traces and metrics

This is where profiling really earns its place. Trace ID → profile is the killer pattern: you see a slow span, you click through to the flame graph for that exact execution, and you immediately see which function ate the time. Christian showed how this correlation works in practice and how it changes incident response.

### 🤝 How to get involved

OpenTelemetry profiling is genuinely an area where the community has room to shape the future. If the conversation sparked something, there's a working group, open issues, and a friendly path in.

## Resources

- [Grafana Pyroscope](https://grafana.com/oss/pyroscope/)
- [OpenTelemetry Profiling SIG](https://github.com/open-telemetry/community/blob/main/projects/profiling.md)
- [Pyroscope docs](https://grafana.com/docs/pyroscope/latest/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)

Thanks to Christian for joining, and to everyone who showed up live with questions.
