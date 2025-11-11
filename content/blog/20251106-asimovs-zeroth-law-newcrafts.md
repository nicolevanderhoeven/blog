---
title: "Asimov's Zeroth Law of Robotics: Observability for AI (Newcrafts 2025)"
date: 2025-11-06T12:23:19+01:00
draft: false
tags: ["observability", "presentation", "AI", "grafana labs", "metrics", "logs", "traces", "testing", "k6", "loki", "grafana", "tempo", "openlit", "open telemetry", "english"]
---
Today I presented at [Newcrafts](https://ncrafts.io/) in Paris, France. I gave a talk I've given before, called *Asimov's Zeroth Law of Robotics: Observability for AI*, which I had previously presented at [KubeCon EU](/blog/20250402-asmiovs-zeroth-law-of-robotics/) in London and at [Dutch Cloud Native Day 2025](/blog/20250703-asimovs-zeroth-law-dutch-cloud-native-day/) in Utrecht. I was happy to present it again, as it gave me the chance to further refine my demo application, which you can find on [GitHub](https://nicole.to/asimov).

The main change I made was to use the "AI as judge" approach that I had previously only talked about in theory. In this version of the demo app, I use AI in both the game as well as in the testing of the game, showing how AI can be integrated into both the application and its observability/testing stack. It was really interesting to note that testing with AI ended up exposing more defects than my hardcoded test cases did, which goes to show the potential of AI-driven testing.
