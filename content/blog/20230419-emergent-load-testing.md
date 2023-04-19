---
title: "Emergent Load Testing - rules for organized chaos"
date: 2023-04-19T00:21:06+02:00
draft: false
tags: ['english', 'presentation', 'load testing', 'kubernetes', 'performance']
---

Today I spoke at [KubeCon EU 2023](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/program/schedule/) about [emergent load testing](https://sched.co/1HyYH).

## Resources

[Here are the slides](https://slides.nicolevanderhoeven.com/2023-emergent-load-testing/#).

Below are some links to extensions and experimental modules that I mentioned:
- [Grafana](https://grafana.com/)
- [k6 site](https://k6.io/)
- [k6 repo](https://github.com/grafana/k6)
- [k6 docs](https://k6.io/docs/)
- [k6 browser](https://k6.io/docs/using-k6-browser/overview/) (experimental module)
- [Prometheus Remote Write](https://k6.io/docs/results-output/real-time/prometheus-remote-write/) (experimental module)
- [k6 tracing](https://k6.io/docs/javascript-api/k6-experimental/tracing/) (experimental module)
- [xk6-kubernetes](https://github.com/grafana/xk6-kubernetes) (extension)
- [k6 redis](https://k6.io/docs/javascript-api/k6-experimental/redis/) (experimental module)
- [xk6 disruptor](https://github.com/grafana/xk6-disruptor) (extension)

And here's the abstract:

## Abstract

When we write load testing scripts against our applications, we write them sequentially: A, then B, then C. But this doesn't accurately reflect the organized chaos of a system in production, nor does it prepare the system for the unexpected.

Emergence is a phenomenon where parts of a whole independently develop properties not originally present in the whole. Emergence is what helps ant workers develop roles without leadership, prompts animals to evolve adaptive traits without forethought, and facilitates non-toxic communities without moderators.

The growing field of emergent software applies this swarm logic to the programs that we write. What would it take to write emergent load testing scripts? It turns out that there are a few ingredients for emergence: a large population size, opportunities to interact, feedback, and an element of control.

In this talk, Nicole van der Hoeven discusses how to bring these elements to load testing by writing a script in Grafana k6 that can independently decide what requests to make next, modify Kubernetes app pods, and disrupt services based on a continual feed of results during runtime-- all without manual intervention. She shows how to wield this new breed of load testing to improve confidence in the complex systems we build.