---
title: "The Architecture of Forgetting"
date: 2026-05-07T16:00:00+01:00
draft: false
tags: ["ai", "english", "llm", "agents", "memory", "openclaw", "context horizon"]
---

Originally posted [here](https://contexthorizon.substack.com/p/the-architecture-of-forgetting) on Context Horizon.

In early April, [a new version of everyone's favourite lobster, OpenClaw, was shipped](https://github.com/openclaw/openclaw/releases/tag/v2026.4.5) with an interesting new feature: [dreaming](https://docs.openclaw.ai/concepts/dreaming). It's a memory consolidation feature. But to understand why it matters, we need to back up.

Early AI chatbots, like the initial GPT wrappers, had zero memory. Every conversation started fresh. You asked a question, you got an answer, and you moved on: a glorified search engine.

Somewhere along the way we began to expect more and more of our chatbots. Models acquired context windows that became their de facto short-term memory. As the context window filled up, they remembered what had been said earlier in the conversation, making them better conversational partners. Still, it was ephemeral: close the tab, start fresh. And it had a hard ceiling: hit the limit, and the oldest things fall off. This felt like forgetting because _it was_. But it was also, accidentally, a form of curation. Finite space forced priority.

Then came the push for real persistence. RAG pipelines, vector databases, memory files, agent frameworks that write notes to themselves. Now our agents can remember that we prefer the Oxford comma, that we just started a new project at work, that our D&D character is named Zuhri. This felt like the solution. More memory = better agent.

That mostly works— until it doesn't.

As it turns out, the problem with AI memory isn't that agents forget too much. It's that **they forget too little**.

## Why remembering is hard

It turns out that having a persistent memory, even for an agent like OpenClaw that has that as one of its defining features, doesn't solve all the memory problems.

I happen to have an OpenClaw agent that named itself Iris.

Iris does a lot of things for me, including parsing my meeting notes to identify next actions, curating my tasks and projects, and generating a daily briefing. She also creates a summary of the day's work based on my meetings, conversations, and notes. One day she was giving me the daily summary, and here's that conversation:

> Iris: ...Tonsil is finally healed after weeks of pain...
> Me: Wait what? Where did you get the tonsil stuff?
> Iris: From your memory file — it's in the Apr 10 daily note context: "Tonsil finally healed — Nicole no longer in pain 🎉". I've had that sitting in memory since the Apr 10 summary. Is that wrong? Was it something else that healed, or is the tonsil detail off?
> Me: I have no idea where you got that. I have never had issues with my tonsil.

Where did that come from? I'm still not sure, but I occasionally have meetings in cafés, and it's possible that a meeting recording overheard the conversation of someone else in the café. That got faithfully transcribed, copied over into my notes, and written into Iris's memory. Iris treated it as fact for days.

The problem isn't that Iris forgot. It's that she remembered the wrong thing... and didn't know how to forget it.

Imagine this at scale: not one wrong fact, but dozens, quietly shaping every summary, every recommendation, every task Iris surfaces for me. The signal-to-noise ratio degrades until it doesn't matter if Iris remembers mostly accurate memories— I won't trust it.

So how do you build a memory system that knows what to keep? Researchers have been working on this longer than you might think.

## Meet the residents of Smallville

Stanford researchers Park et al. [released a charming study in 2023](https://arxiv.org/abs/2304.03442) called *Generative Agents: Interactive Simulacra of Human Behavior* in which they talk about how they created a simulated environment called Smallville, populated it with 25 generative agents, and then watched.

![Smallville, a simulated environment populated with 25 generative agents](/assets/20260507-smallville.png)
*Source: Park et al. (2023)*

The study was an attempt to simulate emergent social behavior, but the key insight I took from it isn't the sim itself— it's what they had to do to the inhabitants of Smallville to enable the rich social interactions they wanted to observe.

The researchers had to give the inhabitants a way to remember.

![The memory architecture of Smallville's generative agents — observation, retrieval, action, and reflection](/assets/20260507-smallville-memory-architecture.png)

Above is a diagram of the memory architecture of every generative agent.
- *Observation:* The agent perceives new information. The new information is saved into the *memory stream*, a database that serves as the record of everything an agent has experienced.
- *Retrieval:* When the agent is looking for information, a retrieval function takes that information from the memory stream and passes it onto the agent.
- *Action:* The agent, armed with retrieved information, can decide to act.
- *Reflection:* Patterns are synthesized from the observations and written back to the memory stream.

To determine which memories to retrieve at any given point in time, the researchers scored memories according to three weighted factors:
- *Recency:* when a memory was observed
- *Importance:* how significant the memory was
- *Relevance:* how closely related a memory is to the input memory (the agent's current context)

The top-ranking memories that fit within the agent's context window were selected to be retrieved and used with the prompt.

The researchers also introduced a second type of memory: reflection. Reflections were generated when a threshold of important scores was reached per day, which typically happened 2-3 times a day.

Crucially, reflection is a _compression_ step — the agent doesn't just accumulate observations, it periodically steps back and asks "what do these observations actually mean?" That reflection pass is where low-signal memories get subordinated to higher-order patterns. That's the first instance of intelligent forgetting.

The Smallville paper was published in 2023. Three years later, the same insight shipped in a lobster.

## Dreaming of electric lobsters

Every system that has solved the memory problem has solved it the same way: not by storing more, but by knowing what to throw away.

Your brain does it while you sleep by consolidating important experiences into long-term memory, letting the rest dissolve. Some programming languages do it with garbage collection, periodically scanning for unused objects and reclaiming that space. Databases do it with compaction: Loki, Cassandra, and other LSM-tree-inspired systems periodically merge and discard obsolete data so reads stay fast.

In all cases, the architecture of good memory is really the architecture of intelligent forgetting. OpenClaw's dreaming feature is the same insight applied to agents.

![Diagram of OpenClaw's internal memory architecture. The default components ("Awake") are in black, and the new components are in blue ("Dreaming").](/assets/20260507-architecture-of-forgetting-dreaming.svg)
*Diagram of OpenClaw's internal memory architecture. The default components ("Awake") are in black, and the new components are in blue ("Dreaming").*

Note that without dreaming, there is no automatic promotion from the active context window to daily notes and then to long-term memory. When a new bit of information is mentioned, the agent has to decide whether it should be added to the daily note and/or the long-term memory file manually. Dreaming, by contrast, is an automated process.

It's called "Dreaming" because the feature works similarly to the biological process, as if in three sleep phases:
- *Light phase:* Creates a session corpus from session files and then succeeding sweeps tally how many times a chunk has been recalled in a session (a counter called `lightHit`).
- *REM phase:* Spots patterns and themes from chunks and adds a reinforcement signal (`remHits`).
- *Deep phase:* Ranks the candidates by several factors and promotes those that exceed a threshold score to long-term memory in `MEMORY.md`

Just like in the Smallville simulation, OpenClaw ranks information by several categories. Here's the table of signals and weights from the [OpenClaw docs](https://docs.openclaw.ai/concepts/dreaming#deep-ranking-signals) at the time of writing:

| Signal | Weight | Description |
|---|---|---|
| Frequency | 0.24 | How many short-term signals the entry accumulated |
| Relevance | 0.30 | Average retrieval quality for the entry |
| Query diversity | 0.15 | Distinct query/day contexts that surfaced it |
| Recency | 0.15 | Time-decayed freshness score |
| Consolidation | 0.10 | Multi-day recurrence strength |
| Conceptual richness | 0.06 | Concept-tag density from snippet/path |

Only candidates that have high scores according to these signals graduate to be part of `MEMORY.md`.

### How dreaming helps with forgetting

The new dreaming architecture doesn't ever *delete* things, technically. The forgetting is more passive. However, it's still an improvement in a few ways:

- *Low-signal chunks don't get promoted:* Anything that doesn't cross the deep phase thresholds simply never reaches MEMORY.md. It exists, but it's functionally invisible to future sessions.
- *Score competition:* The staging index has finite attention, so chunks compete against each other for recall signal. A high-frequency chunk that keeps getting surfaced crowds out low-frequency ones. Relative obscurity is functional forgetting.
- *Recency decay on scoring:* The deep phase ranking includes a recency signal. So something that was frequently recalled two weeks ago but hasn't come up since will score lower than something with fewer total hits but recent activity. Time degrades relevance passively.

What's notable: all three are selection mechanisms, not deletion mechanisms. The corpus files still exist. The staging index entries still exist. Nothing is removed... it's just progressively less likely to be chosen. This is forgetting as diminishing probability of retrieval, not erasure.

That's the garbage collection analogy again: the objects are still in memory, they're just unreachable.

### Transparency

Dreaming also adds a layer of transparency. Aside from the session corpus and staging files, it also produces some output about its decisions. All three dreaming stages create files per day that live in `.openclaw/workspace/memory/dreaming/{phase}/YYYY-MM-DD.md`.

Here's an example of an entry in the `light` directory:

```
# Light Sleep
- Candidate: "Don't Call It Eval" blog post (Context Horizon): `Dont Call It Eval - Blog Post Outline.md` — full outline with 7 open questions; `Dont Call It Eval - Draft.md` — 2,550-word draft, 6 sections; `Dont Call It Eval - Opening Research.md` — Tier 1/2/3 shortlist of popular AI eval po
  - confidence: 0.62
  - evidence: memory/2026-04-19.md:13-15
  - recalls: 0
  - status: staged
- Candidate: "Don't Call It Eval" blog post (Context Horizon): **Thesis (locked):** "AI eval community has rediscovered software testing and given it a new name. The testing world has been busy since."
  - confidence: 0.62
  - evidence: memory/2026-04-19.md:17-17
  - recalls: 0
  - status: staged
```

This entry identified a blog draft I was working on.

REM sleep goes through these candidates and highlights when it spots themes:

```
# REM Sleep

### Reflections
- Theme: `assistant` kept surfacing across 532 memories.
  - confidence: 1.00
  - evidence: memory/2026-04-12.md:27-29, memory/.dreams/session-corpus/2026-04-17.txt:26-26, memory/.dreams/session-corpus/2026-04-17.txt:28-28
  - note: reflection

### Possible Lasting Truths
- "Don't Call It Eval" blog post (Context Horizon): **Datadog Bits AI eval platform** (Apr 7, 2026) — "Bring the noise" = noise injection = production-like envs from 90s QA. SECTION HEADERS are gold ("When one improvement caused subtle regressions", "Why tool-level testing and live [confidence=0.58 evidence=memory/2026-04-19.md:30-33]
- "Don't Call It Eval" blog post (Context Horizon): **Thesis (locked):** "AI eval community has rediscovered software testing and given it a new name. The testing world has been busy since." [confidence=0.58 evidence=memory/2026-04-19.md:17-17]
- "Don't Call It Eval" blog post (Context Horizon): **Title:** "Don't Call It Eval" (Nicole's original; I picked it over "Congratulations, you've invented testing") [confidence=0.58 evidence=memory/2026-04-19.md:27-27]
```

In this case, REM sleep correctly identified that I'm currently working on the [Assistant](https://grafana.com/docs/grafana-cloud/machine-learning/assistant/) feature at work (which had already been promoted to long-term memory) and the blog post that the light sleep phase had identified.

Here's the same day's deep sleep file:

```
# Deep Sleep

- Ranked 10 candidate(s) for durable promotion.
- Promoted 3 candidate(s) into MEMORY.md.
```

And here's the addition to `MEMORY.md` for the same day:

```
## Promoted From Short-Term Memory (2026-04-26)

<!-- openclaw-memory-promotion:memory:memory/2026-04-19.md:17:17 -->
- **Thesis (locked):** "AI eval community has rediscovered software testing and given it a new name. The testing world has been busy since." [score=0.926 recalls=0 avg=0.620 source=memory/2026-04-19.md:17-17]

<!-- openclaw-memory-promotion:memory:memory/2026-04-19.md:27:27 -->
- **Title:** "Don't Call It Eval" (Nicole's original; I picked it over "Congratulations, you've invented testing") [score=0.926 recalls=0 avg=0.620 source=memory/2026-04-19.md:27-27]

<!-- openclaw-memory-promotion:memory:memory/2026-04-19.md:12:12 -->
- Three files in openclaw-output: [score=0.894 recalls=0 avg=0.620 source=memory/2026-04-19.md:12-12]
```

There's also an entry in `DREAMS.md` for the entire sequence, which is more dreamlike and human-readable. The per-day Deep Sleep file is the structured internal audit trail; `DREAMS.md` is the rolling, more narrative log for humans.

This level of transparency and reflection is a welcome change when you compare it to what I had before, which was nothing. Iris had to manually decide on the spot what had to be written where, and those decisions were not logged anywhere.

## The tonsil dilemma

So dreaming could have prevented the tonsil hallucination, right? Well... no.

In this case, the idea of my supposed tonsil pain had come from an external source: my meeting recordings. Iris had faithfully manually added that to the daily note for the day, then decided to call on it a few days later, unprompted, in conversation with me.

With dreaming, Iris still could have made those decisions. But in fact, even if she hadn't, dreaming could have made it *worse*:
- Light phase sweeps it and scores it well since it's recent and distinctive.
- Tonsil pain could be included in queries about health, such as the daily health tracker that is part of Iris's tasks. REM phase sees a pattern and increments `remHits`.
- Deep phase ranks it highly and it crosses the promotion threshold.
- It gets written to `MEMORY.md` and gets loaded *every session*. And long-term memory is sticky. Only manual intervention (by me or by Iris) removes things from that file.

Even dreaming doesn't solve everything. Dreaming adds a mechanism for forgetting. It doesn't prevent OpenClaw from remembering the wrong things in the first place.

### The residual layer

Every memory architecture we've looked at — biological sleep consolidation, garbage collection, LSM compaction, Smallville's reflection pass, OpenClaw's dreaming — has the same shape: automated compression plus a residual human layer. Your brain has you. GC has the programmer. Iris's dreaming has me. The human in the loop isn't a bug in the design; it's load-bearing.

## What's worth keeping

Dreaming is a genuine step forward for OpenClaw's memory architecture. The mechanism of passive forgetting isn't perfect, but the automated promotion systems do add a necessary layer of periodic reflection.

But there are limitations. Dreaming can't yet distinguish between a memory worth keeping and a hallucinated tonsil. It can only measure how often something gets recalled. The next frontier is *active forgetting*: automated demotion from `MEMORY.md`, weighted by signals like source provenance and trust. The provenance side of that work landed in [v2026.4.29-beta.2](https://github.com/openclaw/openclaw/releases/tag/v2026.4.29-beta.2) — memory now exposes evidence-kind drilldown and privacy/provenance reports, so you can at least _see_ where a memory came from. But the demotion half — automatically down-ranking memories based on a low-trust source like an audio transcript — still hasn't been built.

What remains, for now, is the human layer. The transparency of the dreaming process becomes a checkpoint for the human in the loop by surfacing promotion decisions. I still read the summaries. I still catch the errors. I still decide what goes into long-term memory and what gets quietly corrected. That's not a gap in the system — it's probably the right design. The most important memories should require a human to notice them twice.

Good memory systems are defined by what they *don't* keep as much as by what they *do* keep.
