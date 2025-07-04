---
title: "Asmiov's Zeroth Law of Robotics: Observability for AI (KubeCon EU 2025)"
date: 2025-04-02T13:46:42+02:00
draft: false
tags: ["observability", "video", "presentation", "AI", "grafana labs", "metrics", "logs", "traces", "testing", "k6", "loki", "grafana", "tempo"]
---
Today I gave a talk at [KubeCon EU 2025 in London](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) called "Asmiov's Zeroth Law of Robotics: Observability for AI". Here's the abstract:

> A robot may not harm humans. A robot must obey humans. A robot must protect its own existence. These are Isaac Asimov's three Laws of Robotics, created to govern the ethical programming of artificial intelligences. From the Butlerian Jihad to Skynet to cylons, we've been immortalizing our collective nightmares about artificial intelligence for years. But there's an unmentioned law that comes as a prerequisite to all of that: a robot must be observable.
> 
> 
> In this talk, I discuss the different types of AI, the factors that make observing AI different from observing applications, and the telemetry signals specific to AI that we might want to listen to. How do we deal with large data sets? How do we observe for model drift? How do we take into account the costs of LLMs? How can we use distributed tracing to follow event sequences? Part cautionary tale and part technical demo, this talk shows how to instrument and monitor AI apps using OpenTelemetry, Prometheus, OpenLit, and more.

{{< youtube x6EKTCAWtn8 >}}