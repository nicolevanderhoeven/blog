---
title: "Asimov's Zeroth Law of Robotics: Observability for AI (ExpoQA Madrid 2026)"
date: 2026-05-26T10:00:00+02:00
draft: false
tags: ["observability", "presentation", "AI", "grafana labs", "metrics", "logs", "traces", "testing", "k6", "loki", "grafana", "tempo", "openlit", "open telemetry", "english"]
---

This week I gave the opening keynote at [ExpoQA Madrid 2026](https://expoqa.eu/events/cd1-t1-kn2/) in Madrid, Spain. I presented a talk called *Asimov's Zeroth Law of Robotics: Observability for AI*, which I had previously given at [KubeCon EU 2025](/blog/20250402-asimovs-zeroth-law-of-robotics/) in London, at [Dutch Cloud Native Day 2025](/blog/20250703-asimovs-zeroth-law-dutch-cloud-native-day/) in Utrecht, and at [Newcrafts](/blog/20251106-asimovs-zeroth-law-newcrafts/) in Paris. Here's the abstract:

> A robot may not harm humans. A robot must obey humans. A robot must protect its own existence. These are Isaac Asimov's three Laws of Robotics, created to govern the ethical programming of artificial intelligences. From the Butlerian Jihad to Skynet to cylons, we've been immortalizing our collective nightmares about artificial intelligence for years. But there's an unmentioned law that comes as a prerequisite to all of that: a robot must be observable.
>
> In this talk, I discuss the different types of AI, the factors that make observing AI different from observing applications, and the telemetry signals specific to AI that we might want to listen to. How do we deal with large data sets? How do we observe for model drift? How do we take into account the costs of LLMs? How can we use distributed tracing to follow event sequences? Part cautionary tale and part technical demo, this talk shows how to instrument and monitor AI apps using OpenTelemetry, Prometheus, OpenLit, and more.

This was a keynote slot at a testing-focused audience, which gave me the chance to lean more into the *evals vs. observability* framing — what evals can and can't tell you about an AI system in production, and how distributed tracing fills the gap that benchmarks leave behind. The demo app (a Flask-based "play.py" instrumented with OpenTelemetry, flowing into Tempo for traces, Prometheus for metrics, and Loki for logs) is still on [GitHub](https://nicole.to/asimov), and I've been refining it with each iteration.

I'll update this post with the recording once ExpoQA publishes it.

## Resources

- [Demo app on GitHub](https://nicole.to/asimov)
