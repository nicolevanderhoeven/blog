---
title: "Zero to Dashboard with Grafana Assistant and the Infinity datasource plugin"
date: 2026-05-22T17:00:00+01:00
draft: false
tags: ["grafana", "english", "video", "grafana labs", "grafana assistant", "infinity", "ai", "tutorial"]
---

What if you didn't have to write a single query to get a useful dashboard?

In this short video, I go from nothing to a working dashboard in a few minutes — no queries — using [Grafana Assistant](https://grafana.com/products/cloud/ai-tools/) and the [Infinity datasource plugin](https://grafana.com/docs/plugins/yesoreyeram-infinity-datasource/). The data I'm visualising is the [RAWG video game database API](https://rawg.io/apidocs), so I end up with a dashboard that helps me decide what to play next.

{{< youtube X3TZk_qywlo >}}

## Why Infinity is fun here

Most Grafana data sources are scoped to a specific kind of backend — Prometheus, Loki, a SQL database. **Infinity** is different: it lets you treat *any* REST/JSON/CSV/HTML endpoint as a data source. That means anything with an API can become a dashboard, which is exactly the right shape for goofing around with a games API on a Friday afternoon.

Pair Infinity with Assistant and you don't even have to know what queries to write — Assistant configures the data source, asks the API the right questions, and builds the panels for you.

## Timestamps

- 00:00 — Intro
- 00:35 — The RAWG video game database
- 01:01 — Setting up the Infinity datasource
- 05:10 — Customising the dashboard with Assistant
- 09:31 — Closing thoughts

## Resources

- [Step-by-step blog post: using Assistant with the Infinity datasource](https://grafana.com/blog/use-ai-to-turn-any-api-into-a-grafana-dashboard/)
- [Grafana Assistant documentation](https://grafana.com/docs/grafana-cloud/alerting-and-irm/machine-learning/assistant/)
- [Infinity datasource plugin](https://grafana.com/docs/plugins/yesoreyeram-infinity-datasource/)
- [RAWG video game database API](https://rawg.io/apidocs)
- [Get started with Grafana Cloud (free tier)](https://grafana.com/g/cloud)
- [My notes on Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant) — everything I'm learning as I work on it
