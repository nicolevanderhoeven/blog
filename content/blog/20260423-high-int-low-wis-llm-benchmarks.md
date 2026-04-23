---
title: "High INT, Low WIS: What LLM Benchmarks Miss"
date: 2026-04-23T09:00:00+01:00
draft: false
tags: ["ai", "english", "llm", "evaluation", "benchmarks", "observability", "grafana labs", "context horizon"]
---

Originally posted [here](https://contexthorizon.substack.com/p/high-int-low-wis-what-llm-benchmarks) on Context Horizon.

In the tabletop roleplaying game Dungeons & Dragons (D&D), the very first thing you do when you create a character is to choose ability scores. Ability scores are numbers that determine how good you are at the game's main characteristics: Strength (STR), Dexterity (DEX), Constitution (CON), Intelligence (INT), Wisdom (WIS), and Charisma (CHA). 20 is the default maximum that a character can have in any ability, though some in-game events/items can increase that.

Here's the thing, though: every D&D player knows that a 20 Intelligence doesn't mean your wizard aces every check. Whether you have proficiency in the specific skill still matters. That 20 INT wizard, for all their raw cognitive horsepower, can absolutely still fail to identify a magical rune. The ability score is a starting point, not a verdict.

This is exactly what's happening to LLM benchmarks. All the general LLM/AI model benchmarks are ability scores. They tell you something real about a model's general capabilities, the same way a 20 INT tells you something real about a wizard. But as frontier models crowd toward the top of every leaderboard, we're running into a problem D&D solved decades ago: the stat block isn't the character. And it was never supposed to be.

![A screenshot of the stats of my Level 10 bard. Low INT, but look at that CHA!](/assets/20260423-safira-l10-stats.png)

*A screenshot of the stats of my Level 10 bard. Low INT, but look at that CHA!*

## The stat block: A tour of the ability scores everyone's maxing out

There are so many new models and model versions out there that it's hard to keep up with what we're supposed to be using for which tasks. LLM benchmarks have come to be relied on to give a somewhat objective assessment of each model's capability. Here are a few big ones that exist.

### General knowledge/reasoning

#### MMLU (Measuring Massive Multitask Language Understanding, 2020)

MMLU is the classic "general knowledge" INT check. It was [released in September 2020 by Hendrycks et al.](https://arxiv.org/abs/2009.03300) and contains 15,908 multiple-choice questions across 57 subjects (humanities, social science, STEM, other). However, there were a few issues with it:

- [a study in 2024](https://arxiv.org/abs/2406.04127) showed that 6.49% of those questions contained errors
- [The New York Times reported](https://www.nytimes.com/2024/04/15/technology/ai-models-measurement.html) (2024) that data contamination was an issue — models could be trained on the MMLU questions (and answers) to inflate their MMLU scores
- many frontier LLMs soon consistently achieved high scores

In response, a new benchmark called [MMLU-Pro](https://github.com/TIGER-AI-Lab/MMLU-Pro) was created with 12,000 questions that each have 10 options. The increase in options theoretically required more reasoning capability than the original benchmark, but frontier models are already knocking at 90% on the MMLU-Pro.

#### Humanity's Last Exam (HLE, 2025)

HLE was developed specifically to address the fact that LLMs "now achieve over 90% accuracy on popular benchmarks like MMLU" (from [the HLE site](https://lastexam.ai)). The [paper by Phan et al](https://arxiv.org/abs/2501.14249) explains the lengths they took to make it hard enough to be meaningful:

- they solicited high-quality questions from nearly 1000 subject matter experts, even going as far as paying them for successful submissions (with a total prize pool of US $500,000)
- they included graduate-level classics (one of the questions includes translating Palmyrene script)
- they reviewed potential submissions using current LLMs and only proceeded with submissions if the LLMs are unable to answer correctly
- experts then reviewed the submissions further

As a result, HLE scores are low — intentionally so:

> While current LLMs achieve very low accuracy on HLE, recent history shows benchmarks are quickly saturated – with models dramatically progressing from near-zero to near-perfect performance in a short timeframe [13, 45]. Given the rapid pace of AI development, it is plausible that models could exceed 50% accuracy on HLE by the end of 2025. ([Phan et al., 2025](https://arxiv.org/abs/2501.14249))

### Software engineering

#### HumanEval (OpenAI, 2021)

In 2021, OpenAI released [a paper](https://arxiv.org/abs/2107.03374) and [an evaluation harness](https://github.com/openai/human-eval) for a benchmark consisting of 164 Python programming problems based on publicly available code on GitHub. It was developed to test coding in particular.

Eventually, though, experts found that the problem sets in HumanEval were insufficient and ambiguous ([Liu et al., 2023](https://arxiv.org/abs/2305.01210)). HumanEval+ was released to include more tests, but the next benchmark's authors [suggested that models might be overfitting](https://arxiv.org/abs/2403.07974) to HumanEval+ as well, memorizing the dataset and answers rather than genuinely demonstrating reasoning ability.

#### LiveCodeBench (2024)

[Jain et al.](https://arxiv.org/abs/2403.07974) tried a different approach to HumanEval to avoid data contamination: it was released with a continuously-updated coding benchmark. Problems have release dates and models can only be evaluated using problems released *after* their training data cutoff dates.

LiveCodeBench represents a shift in benchmarks towards a more continuous, dynamic measure. However, the last submission to the benchmark was [9 months ago](https://github.com/LiveCodeBench/submissions) at the time of this writing, and [the leaderboard](https://livecodebench.github.io/) has not been updated since then either, suggesting the benchmark is no longer being actively maintained.

#### SWE-bench (2024)

This benchmark was created by [Jimenez et al.](https://openreview.net/pdf?id=VTF8yNQM66) to include 2,294 actual GitHub issues from 12 Python projects. When it launched, it was a much harder benchmark than predecessors, with models scoring 2-4%. Today, models are scoring around 70-80% on the original benchmark. There were enough issues with the original's dataset quality that variants were introduced, including [OpenAI's SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/). Today, [the SWE-bench website](https://www.swebench.com/) shows these variants:

- SWE-bench
- SWE-bench Verified
- SWE-bench Multilingual
- SWE-bench Multimodal
- SWE-bench Lite

### Agents and tool use

This last category is a preview of where I think the field should go: benchmarks that measure *what a model does* rather than just *what a model knows*. Here are some of them:

- GAIA ([Mialon et al., 2023](https://arxiv.org/abs/2311.12983)) — 466 real-world assistant tasks that combine web browsing, file reading, and multi-step reasoning. Easy for humans (92% success), hard for models (15% success for GPT-4), at least at launch.
- [Terminal-Bench](https://www.tbench.ai/) — agents working in actual Linux terminals. Tasks include "build the Linux kernel from source" and "configure a git server plus a webserver on port 8080." No mocks; if it doesn't actually build, it fails.
- WebArena ([Zhou et al., 2023](https://arxiv.org/abs/2307.13854)) — realistic simulated websites (Reddit, GitLab, e-commerce) where agents complete actual user goals like "filter the last six months of orders by refund status."

These benchmarks are harder to saturate than general-knowledge ones, because passing means the thing actually has to work in the real world. A model can memorise a question; it can't memorise a Linux kernel that isn't there until it builds it.

## The wrong answer: Build a harder general benchmark

By now, you probably see that benchmarks tend to go the same way: A benchmark is created, models get too good at it and perform too well to be useful, and then a variant benchmark is created to address the problem.

This is the *saturation problem* in a nutshell: a benchmark that once provided meaningful information to help distinguish models eventually fails to do so because all the models' scores cluster at the top.

Saturation occurs for two reasons:

- *Contamination*: Many benchmarks publish their problem sets online, and models train on data scraped from the web. The benchmark now measures memorization, not capability.
- *Overfitting*: Model providers are incentivized to optimize specifically for gaming performance on benchmarks. Scores go up without corresponding capability improvements.

When you have a party of wizards with 20 INT, "What's your INT score?" stops being an interesting question because any wizard's Fireball will hit the same. Building harder benchmarks is like an arms race for ability scores, when what you actually want to know is whether your wizard can kill a dragon.

Harder benchmarks don't tell us what we want to know: *can this model do my specific job?*

## The right answer: skill checks with real DCs

The fix isn't a harder ability check. It's a different kind of check altogether. In D&D, straight ability checks are rare compared to skill checks. There are 18 official skills that break down the six ability scores into more granular activities. For example, your wizard is much more likely to roll one of these instead of a straight INT check:

- Arcana
- History
- Investigation
- Nature
- Religion

All of these are still based on INT, but test narrow *types of intelligence* rather than general intelligence.

Specific, domain-grounded benchmarks are what the field actually needs. The evaluations that actually help practitioners share a structure: they test a specific skill in a specific context, and they're judged by the people who have to live with the results.

[MedQA](https://arxiv.org/abs/2009.13081) tests whether a model can answer the kind of clinical question a physician might face. [LegalBench](https://arxiv.org/abs/2308.11462) tests whether a model can correctly identify enforceability clauses, classify contract language, and apply legal reasoning. [FinanceBench](https://arxiv.org/abs/2311.11944) tests whether a model can answer the kind of question a financial analyst would actually ask about a real 10-K filing. None of these are trying to rank models on general intelligence. They're asking the only question that matters downstream: *can this model do this specific job well enough?*

This week, Grafana released [o11y-bench](https://github.com/grafana/o11y-bench), an open benchmark for observability-specific agent tasks. I'm biased — I work there — but it's a useful illustration of the shape I'm describing. o11y-bench doesn't ask whether a model is smart in general. It asks whether an agent can do the things observability engineers actually do: read production traces, correlate logs with metrics, figure out why the thing that's supposed to be working isn't. [Its leaderboard](https://o11ybench.ai/) shows models' performance for each activity.

Does that mean that more specific benchmarks won't get saturated? No. We've already seen this play out with SWE-bench. But they'll get saturated more slowly and remain more meaningful measures along the way.

These are skill checks with DCs that matter to someone. They're not trying to produce a single scalar ranking of "which model is smartest." They're asking whether the wizard recognizes the family crest belonging to a political faction or knows this specific cult's practices, not whether the wizard is good at "wizarding" in the abstract.

## Roll for initiative: What this means in practice

If you're an engineer picking a model for production: stop picking by leaderboard. Find or build an eval that reflects your actual use case. A handful of representative examples, graded the way you'd grade them if you were doing the work yourself, will tell you more than a dozen public benchmarks.

If you're a researcher thinking about what to build next: the interesting work is at the specific-and-grounded end of the spectrum, not the general-and-bigger end. Another harder general-knowledge benchmark will saturate in eighteen months. A well-designed domain benchmark, co-built with the people who actually do the work, can stay useful for years.

And if you're anyone else watching this field from the outside: be skeptical of the headlines. When a new model scores 94% on a benchmark you've never heard of, ask what it measures and whether the thing it measures is the thing you actually care about. Usually the answer is "not really," and that's the most important thing a benchmark score won't tell you.

The goal of a character sheet was never to produce one number that ranks the character. It was to give a DM enough information to run a meaningful encounter — and to give the player enough to know when to try, when to pass, and when to roll with advantage. LLM evaluation should work the same way. Not a ranking; a readiness check. Can this specific model clear this specific challenge? Roll for initiative.
