---
title: "OpenTelemetry's Graduation: What It Took (Grafana ❤️🔥 OpenTelemetry Community Call #8)"
date: 2026-06-22T16:00:00+01:00
draft: false
tags: ["opentelemetry", "english", "video", "grafana labs", "grafana otel community call", "cncf", "semantic conventions", "open source"]
---

OpenTelemetry graduated from the CNCF — so for this community call I gathered a panel of people who were in the room for it to talk about what graduation actually *means*, what it took to get there, and where the project goes next. We covered the roughly two-year road to graduation, why semantic conventions are so genuinely hard, the state of the signals (traces, metrics, logs — and the newer profiles), AI's double-edged impact on the project, and the most practical ways for new contributors to get involved.

{{< youtube P9CfVEGwcgo >}}

## What we covered

### 🎓 What graduation actually took

Graduation from the CNCF took about two years, with OTel evaluated on traces, metrics, and logs across the major server-side languages. Profiling, mobile, and other newer signals were explicitly out of scope for the graduation criteria. One of the most concrete pieces of CNCF feedback: stop camping on `0.x` versions for components that are actually production-ready. The fix is to mark maintained, stable packages as `1.0` (reserving `2.0` for future breaking changes) — which unblocks the enterprises that simply aren't allowed to ship anything still labeled "beta."

### 📚 Documentation that's actually findable

A recurring theme was that the documentation bar isn't just "does it exist" — it's "can someone find it." Collector component docs are spread across 100+ GitHub repos, which makes discovery painful. The stopgap is an auto-updated component list with metadata on the OpenTelemetry website that links out to the relevant READMEs; the longer-term answer is the **Ecosystem Explorer** project, which aims to unify instrumentation details, versioning, and component metadata in one place.

### 🏷️ Why semantic conventions are so hard

Semantic conventions define normalized attribute names so that the same event — say, an HTTP request — looks identical no matter the language or library that produced it. The naming debates are slow for real reasons: the database SIG took over a year to stabilize a single set of attributes. The process is propose names → check them against all the major databases → build a proof-of-concept in three or more languages → iterate. A name that's obvious for one database may not even exist as a concept in another. (OTel itself is the product of merging OpenTracing, OpenCensus, and Elastic Common Schema — and yes, the name was chosen specifically because it's boring and self-describing. Everything is named what it does.)

### 🧳 Signals, baggage, and stability

All three original signals — traces, metrics, and logs — are now stable, and that includes **baggage**: a context-propagation mechanism that carries a small "bag" of attributes (trace ID, span ID, and more) across network hops. It was originally built for tracing but designed to be reusable for other cross-cutting concerns like security and feature flags, and it sat largely unused while the rest of OTel was being finished. **Profiles**, meanwhile, hit alpha at KubeCon in March and are treated as a bonus on top of the graduation baseline rather than part of it.

### 🤖 AI's impact on OpenTelemetry — the good and the painful

The good: the explosion of GenAI and agentic systems is creating real demand for OTel-style observability. The Gen AI SIG is growing fast to standardize telemetry for AI systems, and there's a whole crop of AI-observability startups building on OpenTelemetry. Maintainers are also using AI coding tools to move faster — the **Weaver** tool is being developed to constrain the problem space so AI-generated instrumentation code is more accurate, with the goal of going from spec to implementation with coding tools.

The painful: a massive influx of low-quality, AI-generated PRs across all of open source. Some are genuinely malicious (bot accounts farming credibility for supply-chain attacks); others are just thoughtless. One proposed mitigation is to cap the number of open PRs per contributor without merge rights to something like three to five.

### 🚀 Post-graduation priorities and how to get involved

The post-graduation backlog ("postgrad app") focuses on stability cleanup, easier deployment, and self-observability. The deployment north star is something close to `apt-get install opentelemetry` that auto-instruments everything — including outside Kubernetes. New stable YAML-based collector config lets operators manage all languages from a single file, and the **Blueprint** project pairs a specific challenge with OTel guidelines and concrete implementation steps.

If you want in, the panel was refreshingly practical about the fastest path to approver/maintainer status:

- **Review other people's PRs** in your subject area.
- Ask maintainers *"what can I take off your plate?"* rather than only filing your own issues.
- Quality over quantity — AI-heavy contributions you can't explain won't earn status.
- **Localization** is one of the easiest entry points; around ten language teams are active and docs translation is always welcome.

We also went around the panel on how everyone *got* started — from debugging giant distributed systems, to a beginner-questions live stream, to Elastic Common Schema work, to copy-editing PRs as a former librarian. The throughline: pick a small, real thing, do it well, and document your learning journey as you go.

## Resources

- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [OpenTelemetry community & SIGs](https://github.com/open-telemetry/community)
- [CNCF](https://www.cncf.io/)
- [My notes on OpenTelemetry](https://notes.nicolevanderhoeven.com/OpenTelemetry)

Thanks to the panel — **Ted Young**, **Marylia Gutierrez**, **Imma Valls**, **Tiffany Hrabusa**, and **Tiffany Jernigan** — for joining, and to everyone who showed up live with questions.
