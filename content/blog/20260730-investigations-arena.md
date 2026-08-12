---
title: "Investigations Arena: how we test Assistant investigations"
date: 2026-07-30T09:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "video", "grafana labs", "grafana assistant", "evals", "ai evaluation", "testing"]
---

How do you test an AI agent whose whole job is to investigate incidents — when every investigation is different and "correct" isn't a single deterministic answer? In this interview I sit down with **Will**, a software engineer at Grafana who's spent the last year focused on AI: the Grafana Assistant, investigations, and memory features.

The story here is how the team got from Investigations V1 to a much better V2. V1 hit a ceiling, and the demo environment they'd been testing against turned out to be the problem — the cases were too easy and too far from the messy reality of a production cluster. So they built an **arena**: think competitive bot programming, but the "game" is investigating real incidents in Grafana's own production environment. Different AI agents, each with its own strategy and tools, all take a swing at the same incident, and an LLM-as-judge scores their answers against a human-verified root cause.

What's interesting is that the *score* wasn't even the most valuable output at first — the **insights** were. Watching which strategies worked, which tools returned so much noise that they poisoned the context, and which agents wandered off is what let the team optimize bit by bit into the V2 release. The arena also compares more than models: different harnesses running Sonnet vs. Opus, Claude Code with the Grafana MCP, even just hitting the public API directly with `curl`.

A couple of my favorite moments: Will explains the **guardrails** that stop agents from "cheating" (they can only look at data from within the incident's time window, so they can't peek at the fix commit that resolved it) — and how the models mostly play fair because they treat it like a game. And there's a lovely example of emergent creativity: an agent reached for tools the team hadn't even considered, they turned out to be genuinely useful for investigation, and those tools got promoted into the real harness. Will's hope for the future is to open this up — an OliBench-style shared benchmark where the community can throw their own investigation agents into the arena and raise quality across the board.

{{< youtube YPfqchw8LCo >}}

## Transcript

**Will:**
Hey, my name is Will. I'm a software engineer at Grafana. I've been there for three years, and for the last year I've been focusing on AI — the Grafana Assistant, investigations, and memory features.

**Nicole:**
And what's the latest thing you've been working on?

**Will:**
So we developed Investigations V1, and we saw that we hit a ceiling at some point. We came up with a different approach, but this time we needed a good evaluation environment — the demo environment wasn't enough, because those cases were too easy and too far from the reality of a production environment. So we decided to build an arena.

It's a little bit like the idea of competitive bot programming, where bots fight against each other on specific tasks or games. In this case, the topic was investigations in our production cluster — real incidents. We started building bots that had different strategies and different tools; these were AI agents. Comparing a diversity of strategies let us surface the best approaches, and from there we could iterate, bring in more test cases from more incidents, and reach higher and higher quality.

The idea is that the bots try to solve the same case, and we use an LLM as a judge to compare the different approaches. We have different criteria, because for each incident we have a root cause that's been verified by a human. That gives us our ground truth, and the LLM-as-judge compares that ground truth against the answers the agents came up with.

The important part at first wasn't even the score — it was the insights. This tool was better with this strategy; this one had noise in the results that poisoned the context; the results returned from this specific tool were just too much. So we managed to really optimize bit by bit and come up with Investigations V2, which we just released. It's a massive improvement compared to our V1 approach.

**Nicole:**
So is it comparing just different models for investigations, or is it also comparing things like Claude Code and the Grafana MCP versus Assistant?

**Will:**
Both, actually. We have different versions of our harness for investigations that we run with Sonnet and with Opus, but we also use the Claude Code harness with the Grafana MCP — and even just using `curl` to directly hit our public API.

**Nicole:**
Do the models ever cheat?

**Will:**
So far it's been quite good. We have guardrails. Because we investigate past incidents, we need to make sure the LLM only looks at a specific time window — only from when the incident started — otherwise it would be able to find the pull request that was used to solve the incident. But they're pretty good at following the rules; they take it as a game a little bit. We even have an agent that checks afterward, with the judge, to make sure they followed every rule.

It's funny, actually — we had a case using Claude Code where it started to use some tools we hadn't thought about in the first place, and they turned out to be very useful for investigation. We'd never considered them, so we brought them into our investigation harness and it helped a lot. Giving the agents freedom and creativity in this kind of environment is really useful. That diversity sponsors new ideas that we can put into our own work.

**Nicole:**
Cool. Do you have any plans to publish this and share it so that other people can do it too — kind of like OliBench?

**Will:**
Yeah, I think, why not? I think we can go this way too. I'm sure it would be useful for other agents. And it would be very nice if we could compare agents from other people and other companies — maybe with different harnesses, maybe even different tools — because right now it's mostly about our MCP, our CLI, and our investigation harness. But if the community comes up with their own investigation agents — and I think I've seen a few — it would be fun to put them in the arena and help not just our product, but any product improve in quality.

## Resources

- My notes on [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant)
