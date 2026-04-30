---
title: "Grafana k6 Community Call — Secrets Management & AI Script Authoring"
date: 2026-04-30T16:30:00+01:00
draft: false
tags: ["k6", "english", "livestream", "grafana labs", "k6 community call", "ai", "grafana assistant", "secrets management", "openapi"]
---

The first k6 Community Call in over a year, and we packed it. I sat down with four of the people building k6 — **Bukola Ayodele**, **Facundo Batista** (Software Engineer), **Vicente Ortega** (Senior Backend Engineer), and **Charlie Burnett** (Product Manager) — to walk through two new pieces of work that have shipped recently, plus a look at what's coming in k6 v2.

{{< youtube mYpnaE_J2lM >}}

## What we covered

### 🔐 Secrets management in k6 Cloud (Facundo)

A new way to store API tokens, passwords, and other sensitive values for your tests — centralized in Grafana's secrets manager, encrypted at rest, and never visible in the UI or API once written. Your scripts reference secrets by name, and at runtime the values are injected and **automatically redacted from logs**.

Why this matters for load testers:
- No more hardcoded credentials sitting in scripts or in Git
- Easy rotation — change the secret value, every script that uses it picks up the new value, no script edits needed
- Same script works across dev/staging/prod by just swapping which secrets are scoped to which environment
- Works with k6 OSS locally too — your local runs can pull cloud-managed secrets when you want them

Facundo Batista demoed the full flow: creating a secret in the Grafana Cloud UI (name, description, labels — up to 10 per secret, all write-only), and using it in a script with one line. There's also an API for programmatic management.

### 🤖 Grafana Assistant k6 script authoring mode (Vicente)

This is the AI-powered script generation that's been in the works for a while — fine-tuned specifically for k6 best practices, not a generic "ask an LLM to write you a load test" workflow. The interesting bit is the **context sources** Assistant can pull from when generating a script:

- **A service name** — Assistant analyzes the existing telemetry data to discover endpoints and shapes
- **A GitHub repository URL** — pulls the code to understand the API
- **An OpenAPI specification** — generates tests that exercise every endpoint with realistic request shapes
- **Existing observability data** — metrics, logs, traces from your actual production traffic

Generated scripts come with proper structure, error handling, checks, and `TODO` comments where the model genuinely doesn't know what to write (e.g. for auth tokens, request bodies, or anything that needs your secrets — by design, Assistant won't fabricate those). You can also point it at an existing script and ask it to refactor or extend.

### 🚀 k6 v2 (Charlie)

Release candidate 1 is out, GA is *very* soon. The headline changes:

- **Extensions marketplace** — community protocols and integrations
- **Enhanced Playwright browser support** with compatible syntax
- **New assertions library**
- **MCP / agent connectivity** for AI-driven workflows
- **DNS, MQTT, and other network protocols**

Migration advice from Charlie Burnett: pin your script versions, test your existing scripts against the RC before GA hits, and don't rush.

### 🔮 What's next on the AI roadmap (next 1–2 months)

- Visual browser-based testing experience
- Enhanced observability workflow automation
- Improved user-journey creation across both personal and enterprise apps
- Integration with autonomous monitoring systems

## Resources

- [k6 documentation](https://grafana.com/docs/k6/)
- [Grafana Assistant docs](https://grafana.com/docs/grafana-cloud/grafana-assistant/)
- [k6 v2 release candidate](https://github.com/grafana/k6/releases) (GA very soon)
- [Secrets management in k6 Cloud](https://grafana.com/docs/grafana-cloud/k6/secrets/)

### Related Context Horizon pieces
- [*Unlearnings from building Grafana Assistant*](https://contexthorizon.substack.com/p/unlearnings-from-building-grafana)
- [*High INT, Low WIS — what LLM benchmarks miss*](https://contexthorizon.substack.com/p/high-int-low-wis-what-llm-benchmarks)

Thanks to Bukola, Facundo, Vicente, and Charlie for joining, and to everyone who showed up live.
