---
title: "Cartography of the Deep: Distributed Tracing for Testing (Romanian Testing Conference)"
date: 2024-06-13T12:24:02-07:00
draft: false
tags: ["tracing", "testing", "observability", "grafana labs", "k6", "alloy", "english", "presentation", "tempo", "grafana", "opentelemetry"]
---
I presented a talk today at the Romanian Testing Conference 2024 in Cluj-Napoca, Romania! My talk was called "Cartography of the Deep: Distributed Tracing for Testing" and it covered how to tie in distributed tracing into tests to get a better understanding of your system under test.

[Here are my slides](https://nicole.to/rtc2024)!

![](/assets/rtc2024-02.jpg)

![](/assets/rtc2024-01.jpg)

## Abstract
From the Scandinavian Kraken that drags entire ships to their early graves to the Philippine Bakunawa said to rise from the waters to swallow the moon, our existential fears about what lurks at the bottom of our own oceans has inspired us to create hundreds of folkloric monsters across cultures. We've charted the surface of our planet, but the vast majority of the ocean floor remains a mystery.

The mysterious depths of modern software architectures makes it difficult for us to test a system for performance and reliability. The easy solution? Unmanned underwater probes: send inputs to the system, and judge its state based on the outputs that return. But this method is often too limited to tell us what's really going on when something goes wrong. What if there were a way to make our tests themselves more observable?

In this talk, you will learn how to use open-source tools to instrument performance tests, identify bottlenecks at the code level using distributed tracing, and map out a system using a type of software bathymetry. You'll also learn about the Mariana Trench expeditions, the difficulties of operating in a high-pressure underwater environment, and how to come face to face with monsters of our mythologies.