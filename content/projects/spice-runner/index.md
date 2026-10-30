---
title: "Spice Runner"
date: 2025-11-05
weight: 10
summary: "A Dune-themed endless runner that shows how much telemetry even a throwaway game produces, and what it costs. It runs on Kubernetes with a full Grafana observability stack and autoscaling that follows the players."
image: /assets/spice-runner.png
live: https://nvdh.dev/spice
live_label: "Play it"
repo: https://github.com/nicolevanderhoeven/spice-runner
dashboard: https://nicole.to/spicedashboard
talks:
  - title: "The Spice Must Flow: The Fremen Guide to Sustainable Observability (Øredev 2025)"
    url: /blog/20251105-the-spice-must-flow/
tags: ["observability", "sustainability", "kubernetes", "grafana", "faro", "keda", "kepler", "opentelemetry"]
tech_stack:
  - "Vanilla JavaScript"
  - "Nginx"
  - "Go"
  - "PostgreSQL"
  - "Redis"
  - "Grafana Faro"
  - "OpenTelemetry"
  - "Grafana Alloy"
  - "Prometheus"
  - "Grafana Loki"
  - "Grafana Tempo"
  - "Grafana"
  - "Grafana Assistant"
  - "KEDA"
  - "GKE Cluster Autoscaler"
  - "Kepler"
  - "k6"
  - "Kubernetes (GKE)"
aliases: ["/spice-runner/"]
draft: false
---

**Spice Runner** is a browser-based endless runner. Think of the "unable to connect" dinosaur game in Chrome, except you are a Fremen running across the sands of Arrakis, jumping sandworms and Harkonnen ornithopters. It's the demo app for my talk [*The Spice Must Flow: The Fremen Guide to Sustainable Observability*](/blog/20251105-the-spice-must-flow/), and it exists to make one point: even a simple, throwaway game generates a surprising amount of telemetry, and that telemetry has real financial and environmental costs.

The Fremen live on a planet that is rich in spice and poor in water, and they thrive by wasting nothing. Our systems are rich in telemetry and poor in budget, and in carbon. Spice Runner is a small, playable version of that problem: a real app, with real players, running on real infrastructure that scales up and down with them while I watch what it costs.

![Spice Runner gameplay: a Fremen runner jumps sandworms as an ornithopter flies overhead](/assets/projects/spice-runner-gameplay.gif)

## What it demonstrates

- **Real user monitoring with [Grafana Faro](https://grafana.com/oss/faro/).** Game sessions, game starts, scores, collisions, restarts, and game overs are all sent as custom events, so the dashboard shows how people actually play.
- **A leaderboard that's instrumented end to end.** A Go API backed by PostgreSQL and Redis serves a public top-10 leaderboard. It's instrumented with OpenTelemetry for traces and custom metrics, so a score can be followed from the browser through the API to the database and the cache.
- **Metrics, logs, and traces on Kubernetes.** Prometheus, Grafana Loki, and Grafana Tempo run in the cluster, with Grafana Alloy as the collector and Grafana for dashboards. Telemetry is also sent to Grafana Cloud.
- **Autoscaling that follows the players.** [KEDA](https://keda.sh/) scales the game's pods on HTTP request rate, CPU, and memory, and the GKE Cluster Autoscaler adds and removes nodes behind them. Production settings keep at least one pod running and cap it at 20, with a separate demo profile that is far more eager for live demonstrations.
- **Energy monitoring with [Kepler](https://sustainable-computing.io/).** Power and energy use are tracked per workload, so "what does this cost the planet?" is a query rather than a guess.
- **Load testing with [k6](https://k6.io).** k6 drives load against the leaderboard API and, with a browser script, plays the game to keep the dashboard populated.

## The dashboard

The live dashboard on Grafana Play shows real player data as it happens. The dashboard is also entirely AI-generated: it was built with [Grafana Assistant](https://grafana.com/docs/grafana-cloud/machine-learning/assistant/).

**[Open the live dashboard](https://nicole.to/spicedashboard)**

## Architecture

The app has two layers. The first is the game and its leaderboard: a vanilla JavaScript game served by Nginx, with a Go leaderboard API backed by PostgreSQL and Redis. The second is the observability stack: Faro instruments the browser, and the Nginx exporter, Alloy, Loki, Tempo, and Prometheus cover the backend. Everything runs on Google Kubernetes Engine, with persistent volumes so telemetry survives pod restarts, and autoscalers at both the pod and node level.

![Spice Runner architecture: the game and leaderboard, the observability stack, and the autoscalers](/assets/projects/spice-runner-architecture.png)

## The talk

*The Spice Must Flow* uses Dune as its framing. It covers the hidden environmental and financial costs of an observability stack, how hard it is to measure the cost of ephemeral resources on Kubernetes, how to use KEDA to right-size resources when you don't know what the right size is, and the most effective thing you can do to cut cost: deleting the telemetry you don't need.

I first gave it at [Øredev 2025](https://oredev.org/) in Malmö, Sweden. You can read the [write-up and abstract](/blog/20251105-the-spice-must-flow/) and see the [slides](https://nicole.to/spiceslides).

## Run it yourself

Everything you need to deploy it on your own GKE cluster, including the Kubernetes manifests, the dashboards, and the load tests, is in the [GitHub repository](https://github.com/nicolevanderhoeven/spice-runner). Its README has a quick start.
