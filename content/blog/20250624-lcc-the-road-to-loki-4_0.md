---
title: "The Road to Loki 4.0 (Loki Community Call June 2025)"
date: 2025-06-24T13:56:45+02:00
draft: false
tags: ["loki community call", "loki", "grafana labs", "observability", "english", "video"]
---
In this video, my colleague [Jay Clifford](https://www.linkedin.com/in/jaymand13/) and I interview Ed Welch, Principal Engineer on the Loki team at Grafana Labs, about the upcoming Loki 4.0 release. We talk about some pretty big features that make this next release almost an entire rewrite of Loki, including:
- A shift towards columnar storage, using a new storage format called "DataObject"
- A new Kafka/WarpStream architecture that decouples the read and write paths
- A new Loki Query Engine that decouples the query language from the rest of the system, allowing for more options in, for example, allowing for SQL queries against Loki in the future

{{< youtube LWDeIHfAC9A>}}