---
title: "Projects"
date: 2026-04-10
draft: false
---

A collection of things I've built — demos, tools, and experiments that go beyond a single talk or post.

---

## Spice Runner

**[🎮 Play it](https://nvdh.dev/spice)** | **[📊 Live dashboard](https://nicole.to/spicedashboard)** | **[💻 Source code](https://nicole.to/spicerepo)**

Spice Runner is a browser-based endless runner game I built as a demo app for my talk [*The Spice Must Flow: The Fremen Guide to Sustainable Observability*](/blog/20251105-the-spice-must-flow/), first presented at [Øredev 2025](https://oredev.org/) in Malmö, Sweden.

The game is a reskin of the classic Chromium T-Rex runner. It exists to make a point: even a simple, throwaway game generates a surprising amount of telemetry — and that telemetry has real financial and environmental costs. The Spice Runner dashboard on Grafana Play shows real player data, live.

![Spice Runner game screenshot](/assets/spice-runner.png)

### What it demonstrates

- **[Grafana Faro](https://grafana.com/oss/faro/)** for Real User Monitoring (RUM) — every jump, game start, score, and collision is instrumented as a custom event
- **Full observability stack on Kubernetes**: Prometheus for metrics, Grafana Loki for logs, Grafana Tempo for traces, Grafana Alloy as the collector, Grafana for dashboards
- **[KEDA](https://keda.sh/)** for event-driven autoscaling — the cluster grows when players are active and shrinks when they're not, demonstrating cost-aware infrastructure
- **k6** for load testing the leaderboard API

### Architecture

The app has two layers:

**Game + leaderboard** — vanilla JavaScript game (`runner.js`) served by Nginx, with a Golang leaderboard API backed by PostgreSQL and Redis for score storage and caching.

**Observability stack** — Grafana Faro instruments the frontend; Nginx exporter, Alloy, Loki, Tempo, and Prometheus cover the backend. Everything is deployed on Kubernetes on GCP with persistent volumes so telemetry survives pod restarts.

### The talk

The *Spice Must Flow* talk uses Dune as its framing. Arrakis is rich in spice but poor in water; our systems are rich in telemetry but poor in budget and carbon budget. The Fremen survive by wasting nothing — the talk argues we should apply the same philosophy to observability.

Key themes: the hidden environmental cost of observability, using KEDA to right-size resources dynamically, and the single most effective thing you can do to reduce cost — deleting telemetry you don't actually need.

The talk has been given at [Øredev 2025](https://oredev.org/) and will be given again at [ExpoQA Madrid 2026](https://expoqa.eu/).
