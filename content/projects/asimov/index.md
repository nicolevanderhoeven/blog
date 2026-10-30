---
title: "Asimov"
date: 2025-04-02
weight: 50
summary: "An AI app built to be observed and tested: a Star Trek text adventure with Claude as the game master, instrumented with OpenTelemetry and checked by a k6 test suite. The demo behind my talk Asimov's Zeroth Law of Robotics."
image: /assets/projects/asimov-dashboard.webp
repo: https://github.com/nicolevanderhoeven/asimov
talks:
  - title: "Asimov's Zeroth Law of Robotics at KubeCon Europe 2025"
    url: /blog/20250402-asimovs-zeroth-law-of-robotics/
  - title: "Asimov's Zeroth Law of Robotics at Dutch Cloud Native Day 2025"
    url: /blog/20250703-asimovs-zeroth-law-dutch-cloud-native-day/
  - title: "Asimov's Zeroth Law of Robotics at Newcrafts 2025"
    url: /blog/20251106-asimovs-zeroth-law-newcrafts/
  - title: "Asimov's Zeroth Law of Robotics: Observability for AI (ExpoQA Madrid 2026)"
    url: /blog/20260526-asimovs-zeroth-law-expoqa-madrid/
  - title: "Asimov's Zeroth Law of Robotics: Testing for AI (HUSTEF 2026)"
    url: /blog/20261007-asimovs-zeroth-law-testing-for-ai-hustef/
tags: ["ai", "testing", "observability", "opentelemetry", "k6", "grafana", "go"]
tech_stack:
  - "Go"
  - "Claude"
  - "OpenTelemetry"
  - "Grafana Tempo"
  - "Prometheus"
  - "Grafana Loki"
  - "Grafana"
  - "Grafana Cloud Agent Observability"
  - "k6"
  - "Docker"
draft: false
---

**Asimov** is the companion project to my talk *Asimov's Zeroth Law of Robotics*. It's an AI app built to be observed and tested: **The Silent Enterprise**, a single-player Star Trek text adventure. You play Data, and Claude is the game master. Every model call, dice roll, and turn shows up as telemetry in a Grafana that you can run on your own machine or in Grafana Cloud, and a k6 test suite, some of it judged by Claude, checks whether the AI follows the rules.

The game master has some known flaws, kept on purpose. It sometimes narrates a rescue that didn't happen, or "destroys" a drone that's still standing. The point of the demo is catching those flaws with telemetry, tests, and online evaluators.

## The idea

Isaac Asimov's three Laws of Robotics govern how robots behave. The talk argues for a law that comes before all of them: a robot must be observable, and, in its newest version, testable. AI systems fail differently from traditional software. There's no single correct output to assert against, a response can be fluent and completely wrong, and models drift. You can't test what you can't see, and you can't trust what you can't test.

## What's in it

- **The game.** A Go program with a command-line interface and an HTTP API. The game engine owns the rules and the state. Claude interprets the player's input, makes the game master's own rolls through a tool, and narrates, so a narration that contradicts the saved state is a defect that can be caught.
- **Telemetry.** Traces, metrics, and logs go over OpenTelemetry to a local Grafana stack (Tempo, Prometheus, and Loki, with the game's dashboard already loaded) or to Grafana Cloud. Generations can also go to Grafana Cloud's Agent Observability, where online evaluators judge a sample of them.
- **Tests.** A k6 suite with code checks, LLM judges, dice-trajectory evals, and whole playthroughs. All of it can run for free against a mock game master and judge.
- **No account needed to start.** You can play offline with no API key, and see the local monitoring stack with one command and Docker.

The screenshot above is the game's local Grafana dashboard.

## The talks

I've given the talk, in several versions, at KubeCon Europe 2025, Dutch Cloud Native Day 2025, Newcrafts 2025, ExpoQA Madrid 2026, and HUSTEF 2026. The write-ups are linked below. The earlier talks used a Python and Flask version of the app, which has since been rewritten in Go.

## Try it

The [repository](https://github.com/nicolevanderhoeven/asimov) has a quick start for playing offline, a Docker-only path, and release binaries for Windows, macOS, and Linux.
