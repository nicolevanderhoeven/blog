---
title: "Watching the Watchers: How We do Continuous Reliability at Grafana Labs (KubeCon NA 2024)"
date: 2024-11-13T09:37:19-07:00
draft: false
---

Today I did a talk at [KubeCon North America 2024](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) in Salt Lake City, Utah, USA. [Here's the abstract](https://kccncna2024.sched.com/event/1i7m6):

> Nothing is foolproof. Everything fails eventually. Observability tools help predict and lessen the impact of those failures, as the watchers of your software systems. But who watches the watchers?
> 
> At Grafana Labs, we're not immune to production incidents. Just like any company, we still sometimes move too quickly. We run complex, microservices-based systems ourselves, so we have to eat our own dogfood on a daily basis.
> 
> In this talk, I reveal:
> - how we solved a years-long mystery that cost us $100,000+
> - how we got our internal Mimir clusters to reliably hold 1.3 billion time series for metrics
> - what we've had to do to scale our Loki clusters to handle 324 TB of logs a day
> - what our Grafana dashboards to monitor Grafana Cloud look like
> 
> Sometimes, it's easier to learn from failures in observability than from successes. This talk is a confession of some of our worst sins as well as a realistic look under the hood at how we're improving the continuous reliability of our stack.

{{< youtube pCxmwvqTklo >}}

You can find the slides [here](https://www.canva.com/design/DAGV-7UbEVo/QVrjCs0kKvtiEG_LlNLrvA/view?utm_content=DAGV-7UbEVo&utm_campaign=designshare&utm_medium=link&utm_source=editor) and a PDF version [here](/assets/20241113-kubecon-na-2024-watching-the-watchers.pdf).