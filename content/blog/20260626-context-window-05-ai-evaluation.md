---
title: "An Overview of AI Evaluation (The Context Window #05)"
date: 2026-06-26T18:00:00+01:00
draft: false
tags: ["ai", "observability", "english", "livestream", "grafana labs", "the context window", "evals", "ai evaluation", "o11y-bench", "ai agents"]
---

How do you know if an AI agent is actually any good — and whether the change you just made to it made it *better* or *worse*? In this episode of *The Context Window* — Grafana's livestream series on AI in observability — I'm joined by [Yas Ekinci](https://www.linkedin.com/in/yasirekinci/), an engineer on Grafana's AI team who has spent the last several months focused almost entirely on evaluation. We talk about why trusting AI is so hard (non-deterministic models, oversized PRs, and the shift from *writing* code to *reviewing* it), the difference between online and offline evals, how we actually test [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant), and `o11y-bench`, the open observability benchmark we announced at GrafanaCON. We recorded this one ahead of Yas's two-month leave — so consider it a deep dive banked for the road.

{{< youtube _XGLBqVpL-Y >}}

## The "final answer problem"

A recurring theme — and one close to my testing heart — is what I call the final answer problem. As a tester I'm used to looking at an outcome and asking "did this pass or fail?" But with AI, a plausible-looking answer isn't enough. If the *process* was wrong, you can't trust the outcome even when it looks right — and a plausible-but-wrong answer is the dangerous case, because nothing on the surface tells you it's wrong. Yas's example: a broken Tempo tool that returned no spans, while the agent still answered convincingly by guessing from metadata. Plausible ≠ correct.

This is also why the bottleneck has moved. The cost of *writing* code has collapsed, so the burden now sits on review. Developers, as I like to put it, are becoming **shepherds of intent** — less about typing the code, more about making sure the intent is clear and faithfully implemented.

## What evals are, and online vs offline

An eval is simply a test of whether an AI agent behaves the way you want — from "who are you?" → "I'm Grafana Assistant" all the way up to multi-step querying and dashboarding. The point is to know *with confidence* whether a change made the agent better, which is what lets you improve it consistently over time.

There are two complementary flavours, and they map neatly onto testing concepts we already have:

- **Online evals** — scoring a sample of real production conversations, usually with an LLM-as-a-judge. Great as a pulse check (it'll catch a quality drop when a model provider silently swaps models), but it only tests the deployed variant and is hard to verify. Closest analogy: traditional observability / RUM.
- **Offline evals** — a "golden set" of tasks run during development and CI against a controlled, reproducible environment. You can test every change, prompt, and implementation, and drill into specific skills (PromQL vs LogQL, dashboarding). Closest analogy: integration testing.

## How we test Grafana Assistant

Assistant evals run a real agent-plus-tools *harness* against a real-ish environment (a Grafana with data sources, alerts, and dashboards), then grade the full transcript with "graders" or "verifiers." The hard tension is that the environment has to be **real and reproducible** at the same time. Because Assistant is a front-end plugin that runs some tools in the browser, the team uses Playwright to replicate real browser behaviour — which is where I made my pitch for k6's browser module (now approaching Playwright parity) as a dogfooding option. The internal eval tool is a CLI called **LLM Spec**, now on its third major iteration after the lessons from o11y-bench.

## o11y-bench

[`o11y-bench`](https://grafana.com/blog/o11y-bench-open-benchmark-for-observability-agents/) is our public benchmark, announced at GrafanaCON, with six task categories: dashboarding, investigation, logs, metrics, and traces. A few things I think make it genuinely interesting:

- It's built on the **Harbor** framework (also used by terminal-bench), which separates harness from environment from tasks — so you can swap harnesses and compare, say, `gcx` + Claude Code against the Grafana MCP.
- The leaderboard includes open models (Qwen 3.6, Kimi), not just the frontier labs.
- It distinguishes **pass@3** (got it right at least once in three runs — rough capability) from **pass^3** (got it right all three times — reliability). The 10–20% gaps between the two are the whole reliability story in a single number.
- It runs against a **synthetic environment** (Prometheus, Loki, Tempo in Docker) with generated data, so the correct answer is known in advance — and it uses **fact-based rubrics**, where the grader runs its own known-good queries against the environment and checks the agent's answer against them. That's how you catch the subtle, plausible-but-wrong failures.

The internal eval set is a superset that adds scenarios drawn from real (private) conversations and Assistant-specific behaviour — like Slack's not-quite-markdown formatting — while o11y-bench stays generic and harness-independent, grading on outcome rather than method.

## The evaluation loop

Yas's blog post (the first engineering post on Grafana's new community *Unprompted* blog) and our GrafanaCON talk both center on the **evaluation loop**: measure → make changes (new tools, prompt tweaks, bug fixes) → measure again. The crucial bit is that the loop can be driven by a coding agent — via an `LLM Spec Improve` skill — because you can't unit-test natural-language "programming" the way you test code. There's no clean relationship between the instructions you write and what the model does, so the only way to know the impact of a change is to run the loop.

## Where it's going

We closed on open questions and wishes: higher environment fidelity, more and harder tasks (very likely an o11y-bench 2.0), and getting more contributors — including PMs writing evals to capture desired product behaviour. I floated a k6-extension-style community model for evaluators, and using o11y-bench to support **bring-your-own-model**, so users can see exactly where a smaller or local model falls short instead of assuming Assistant is broken. Yas's industry hope is the neat one: if labs tune their models against o11y-bench, observability and Grafana performance improve across the board — free fine-tuning out of the box.

## Resources

- [Introducing o11y-bench: an open benchmark for observability agents](https://grafana.com/blog/o11y-bench-open-benchmark-for-observability-agents/)
- [o11y-bench on GitHub](https://github.com/grafana/o11y-bench)
- [Anthropic: Demystifying evals](https://www.anthropic.com/engineering/demystifying-evals)
- [Grafana Community Slack](https://slack.grafana.com)

### Related reading
- My notes on [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant)
- [My Context Horizon piece: *Unlearnings from building Grafana Assistant*](https://contexthorizon.substack.com/p/unlearnings-from-building-grafana)

### More from The Context Window
- [#04: CLI and MCP Basics for AI Agents](/blog/20260603-context-window-04-cli-mcp/)
- [#03: All About AI Observability](/blog/20260422-context-window-03-ai-observability/)

## Transcript

**Nicole:**
Hey everyone. Welcome to another episode of The Context Window. This is a semi-regular podcast — we try to make it every month — and it's all about the things going on with AI at Grafana. Usually this is live, and you might think looking at this that it's live, but it's actually prerecorded, because Yas has a busy schedule ahead and I wanted to get him on here before he left. So hi, I'm Nicole van der Hoeven, a senior developer advocate at Grafana Labs, and I'm assigned to the AI team these days. And one of the people on the AI team is — this person over here. How do you say your last name, actually?

**Yas:**
Oh, it's Ekinci.

**Nicole:**
Ekinci. I was totally confused because I just found out you speak Dutch. Did not know that.

**Yas:**
I'm based in Belgium, and I was like, "Nicole van der Hoeven" — okay, that sounds familiar enough to me.

**Nicole:**
Yeah, it's the name of my ex-husband, but it's okay, we still like him. So tell us what you do on the AI team.

**Yas:**
I'm an engineer on the AI team — I'm getting to five years at Grafana next week. When I joined, this was pre-AI; we had the machine learning team building predictive models, forecasting, that kind of stuff. As the AI wave came, we all got absorbed into this newer, larger AI department. It's been quite varied — the assistant, the AI agent inside Grafana — but especially the latter half of this year I've been more and more focused specifically on evals: how do we figure out the quality and reliability of these things we're deploying?

AI is a very useful tool. It has utility — it's not like NFTs. We use it day to day. My job has changed drastically over the last two years. But you still notice it needs guidance and sometimes has reliability issues. The trend is that the guidance has come down — a year or two ago I'd steer an agent 50, 60, 70 times in a session; now it's more like five or ten. But you still need to do it. If you just blindly vibe-code your way out of this, you're not going to end up in a good place.

**Nicole:**
It moves so quickly. Whenever someone tells me they tried AI and it didn't do what they wanted, I ask, "Well, when was that?" Because if it was six months ago — try it again. In this episode we'll talk all about evals, but first, some announcements. Assistant is now available for OSS and self-hosted Grafana, and I made a video showing how to do that. There's also a new Medium blog for Grafana Labs called *Unprompted* — a community-focused blog — and Yas wrote the first engineering post, about building an evaluation loop. And we've started AI weekly videos: the AI team has a weekly meeting, Mat Ryer had the idea to publish excerpts, usually the demo part. Just be warned we demo things that may never make it to production — you're getting it raw, warts and all.

**Yas:**
I need to make sure I don't wear my PJs anymore for the AI weekly.

**Nicole:**
A bit of quick AI news: Warp is now open source. There are new models — GPT-5.5, Gemini 3.1 Ultra with a two-million-token context window, Anthropic's Claude Mythos security preview. And there's a great article by Matt Shumer called "Something Big Is Happening," where he says, "I am no longer needed for the actual technical work of my job" — which hits hard — and advises leaning into what's hardest to replace.

**Yas:**
It's still that guidance thing — you need a human in the loop to guide it. But if you ask me how much code I've manually written lately, the actual technical piece is very close to zero. We'll talk about how that's different for evals, because evals don't work as well as coding does there.

**Nicole:**
So why is it so hard to trust AI? Why don't we just YOLO it and accept everything?

**Yas:**
A mix of things. Everybody knows these models are non-deterministic and not perfect — these aren't new problems; underneath it's all machine learning, numbers and math and stats. Every time you talk to it you might get a slightly different response. The second part is it writes *a lot* of code. You can 10x your output — send ten agents at ten different features and launch all those PRs — but then someone needs to review them, and the PRs are typically big and over-engineered. One thing I always do at the end of a piece of work is ask it to find a simpler way and simplify. Bigger PRs plus so many changes makes it hard to keep a mental model of the whole thing. And interestingly, I'll use AI to help review a PR — which gets you back to the same problem: if you use AI to review the AI, how much can you trust that?

**Nicole:**
I like the phrase that developers are becoming shepherds of intent — we're not writing the code so much as making sure the intent is clear and implemented. And this is the difference between process and outcome — what I call the final answer problem. I come from performance testing; I'm used to looking at the outcome and asking did it pass or fail. But now, even if the outcome looks right, if the process was wrong I don't trust it. And the reverse too: right process, wrong outcome, something else is broken.

**Yas:**
Tests are interesting here, because most of those tests are also AI-generated — and the AI doesn't shy away from just changing the test to make its branch pass. For any branch I review, I still look at all the changes; I won't blindly rubber-stamp. That's probably the biggest bottleneck right now.

**Nicole:**
One approach to trusting AI is human evaluation — thumbs up/thumbs down, or something like LMArena where you compare two answers blind. Useful, but not scalable; you can't run it in CI.

**Yas:**
On the eval side they're all complementary. So, what *is* an eval? It's testing whether the AI agent behaves like you want. A simple one: ask "who are you?" and expect "I'm Grafana Assistant." There are much more complicated ones around querying and dashboarding. At its core, an eval is how you figure out if the agent is any good — and the reason we do it is so that when we make changes, we know if it's better. Answer that with confidence and you have a path to improve consistently over time.

We split into online and offline. Online — we recently launched AI observability for agents — is about measuring how the deployed agent does against real production conversations from real users. Valuable, because you get a score based on real behaviour, but hard to verify; we typically use an LLM as a judge, so it's not as robust. Offline is used more during development, in CI — much more controlled. You have a golden set of evals covering the behaviour you expect in production, and because you always test the same set, you can see whether changes make it better, and dig into PromQL vs LogQL, or dashboarding. Online is a great pulse check — it can catch quality dropping when Anthropic swaps a model — but it only tests the deployed variant. Offline can test all your changes, your implementation, and all your prompts.

**Nicole:**
It took me a while to translate these, because the testing industry already has this — we call it pre-prod and production testing. Pre-prod is everything from unit to system integration testing in dev and staging; you can really hammer the thing. Production you have to be more careful — synthetic monitoring, real user monitoring — same idea with an AI flavour.

**Yas:**
Definitely. Online is much more like traditional observability — you're observing a system that happens to be powered by AI, turning natural language into a number you track over time and alert on. Offline is closer to an integration test: you give it a task, it runs the whole agent against a real environment, you get something out, and then separately you grade that outcome.

**Nicole:**
We did an AI observability episode without you — you were at GrafanaCON — so I'll link that. Let's talk more about offline evals, since we haven't covered those.

**Yas:**
Offline is a bit of a beast. There's a good Anthropic post called "Demystifying evals." Back when we had simple single-turn LLM calls — incident summary was one of the first — the prompt was "here's the context of the incident, summarize this," and grading checked readability, completeness, appropriate length. Easy enough to set up. Agents get more complicated, because every time you run a task the agent can take very different trajectories — five steps one time, seven the next. The agent plus its tools is roughly the harness; it runs against an environment — a real Grafana with data sources, a certain alert and dashboard state — and keeps interacting using the tools until it's done. Then we take the whole transcript and grade it with graders, sometimes called verifiers, to verify it actually got the task right.

**Nicole:**
So how do you do it for Assistant, given how broad that environment is?

**Yas:**
We have the public benchmark we released recently and our internal evals — same approach, different number of tasks and some different data sources. We want an environment as real as possible, but with the tension that we also need to control it so a benchmark is reproducible. If two people run it and get different scores, which one was right? We started, like everybody, with manual tests — listing data sources to confirm a tool is wired up, some CPU questions, showing logs — with a human as the judge. That's fine at four or five scenarios; you can't do it as a human at 500. Assistant is a front-end plugin — some tools run in your browser, which is good for auth and security but makes testing hard — so we use Playwright to replicate real behaviour and pull the telemetry out. The internal eval tool is a CLI we call LLM Spec, and it can run against cloud instances or a local controlled environment.

**Nicole:**
Before the environment — did you consider using k6 instead of Playwright?

**Yas:**
Interesting — yes and no. k6 is also a tool the assistant needs to use, but our goal isn't to load test; it's to hook into the plugin and get the messages and telemetry out, so we have a Playwright harness.

**Nicole:**
There's actually a browser module for k6 going towards feature parity with Playwright.

**Yas:**
I did not know that. Might be interesting.

**Nicole:**
Just dogfood all the things. I'd love to work with you on that. Okay, the environment.

**Yas:**
We test against cloud instances — for incidents especially, it's a lot of data. And we run LLM Spec against a local controlled environment, which is quite similar to the open benchmark we published.

**Nicole:**
You've mentioned o11y-bench — the benchmark announced at the last GrafanaCON. That was fast.

**Yas:**
o11y-bench has tasks across six categories — dashboarding, investigation, logs, metrics, traces. We wanted to bring our internal approaches outward, and it was a learning opportunity: we used a framework called Harbor, also used by the makers of terminal-bench. The nice thing is it separates harness from environment from tasks — so the default harness is a simple system prompt plus the Grafana MCP, but the folks working on GCX run Claude Code plus GCX against o11y-bench and compare GCX with MCP. There's a leaderboard with a bunch of models, including open ones like Qwen 3.6 and Kimi.

**Nicole:**
They're getting good. Qwen 3.6 is awesome — not top five, but for an open-weight model, impressive.

**Yas:**
And this is the interesting part: sort on pass@3 and it looks different from pass^3. pass@3 runs each task three times and passes if it gets it right one out of three — rough capability. pass^3 means you need three out of three on every task — reliably solving it, not just getting lucky once. You see 10–20% differences between the two scores.

**Nicole:**
That's awesome. And this is public, right?

**Yas:**
Yep — the repo's on GitHub with all the tasks. We run o11y-bench against a synthetic environment — a Prometheus, Loki, and Tempo in Docker — and we generate the data, so every run uses the same data and we know what the answer should be before we even run it. We also do fact-based rubrics: separately from what the agent does, the grading side runs its own known-good queries against the environment and checks whether the agent's answer matches. That matters because these agents fail in subtle ways. We once made a change to the Tempo tool that broke the spans — the agent got no spans but still answered, fairly realistically, from metadata. Without testing for it you'd never catch it; the text looked plausible.

**Nicole:**
That's exactly process versus outcome. If the answer were negative two seconds it's obviously wrong, but a plausible answer is the dangerous one.

**Yas:**
Exactly, and that happens a lot.

**Nicole:**
An early Assistant once told me it created a dashboard, and it didn't look right — turned out it couldn't find the data source so it just used dummy data.

**Yas:**
Same thing happened to me locally — I broke all the tools, and it still came up with tool calls it couldn't execute because of rough instructions in the system prompt.

**Nicole:**
So what's missing in o11y-bench that means you still need an internal one?

**Yas:**
Two levels. First, some scenarios are based on real conversations or our own internal environments — anything involving private data can't go public. Second, there are very Assistant-specific things we want to test — Slack, for instance, has its own version of markdown that looks like markdown but isn't, and early Slack Assistant struggled to write it consistently, so we wrote tests for that. The internal set is a superset; the public set is still part of it. The public set is generic observability tasks — asking questions about your data, dashboarding, basic Grafana API checks — and because the harness is independent, we can test GCX, MCP, our assistant, or any other agent against it, grading on the outcome rather than how it was solved.

**Nicole:**
We talked about your blog post — let's define the evaluation loop.

**Yas:**
At its core: measure the current state, see where it works and where it doesn't, make changes — a new tool, tool instructions, the system prompt, bug fixes — then measure again, and again. The key is that loop can be driven by a coding agent, not us manually. If your evals are robust enough to pass a clean feedback signal back, the agent can keep improving until it hits 100%, and then you make harder tasks or increase coverage. At scale it's nearly impossible for one human to understand the whole system and make targeted improvements, because an agent isn't programmed as code — it's programmed with natural language, and there's no clear relationship between the instructions and what the model does. The only way to probe that is to run a bunch of these loops.

**Nicole:**
Is the loop equally implemented for o11y-bench and LLM Spec?

**Yas:**
It's implemented internally. o11y-bench is really just the measurement part — we've used it for GCX and MCP, but more manually. In LLM Spec we have an `LLM Spec Improve` skill — you pick the agent, and it runs measure-improve-measure-improve.

**Nicole:**
Where are you going next — no promises?

**Yas:**
I've done a lot on the harnesses — the Playwright stuff, and there was an LLM Spec 1.0, then a 2.0 revamp for speed and robustness, then o11y-bench, and the learnings from that went into what I'd call LLM Spec 3.0. The two big challenges now are environment fidelity — more an issue for internal evals — and the number and quality of tasks: how do we cover more of Grafana? We weren't sure o11y-bench would be a recurring thing, but there's a lot of interest, so we'll probably do an o11y-bench 2.0. And I want more people contributing — I was talking at the PM all-hands about getting product managers to write evals, because the tasks capture desired behaviour: when someone asks about my product, how should the agent ideally respond?

**Nicole:**
What I'd love is something like the k6 extension model applied to evaluators. When Grafana acquired k6 — I was on k6 — k6 had extensions and modules, and we got a lot of cool community extensions. I think evaluators would be the same. After my Madrid talk, all the questions about the evaluator section were "can we add this, can we add that, why isn't this in the template?" — and it could be.

**Yas:**
It would be nice to do that across both o11y-bench and the internal ones — there are open questions on making them work together; internally we're in Go, o11y-bench is on Harbor in Python, but the tasks and most verifiers are language-independent by design. A fourth thing is getting to a better golden set over time — we haven't yet automated going from real AI-observability conversations to verifiable offline tasks. As the product changes, your tasks might not stay relevant — imagine k6 didn't exist and now people ask Assistant about k6. Bridging online and offline in a more automated way would be the fourth big thing.

**Nicole:**
I also have a wish for o11y-bench beyond being a benchmark — with no internal knowledge and no promises: it could be a step toward making Assistant bring-your-own-model. One barrier is that people try Assistant with a tiny local model and conclude it doesn't work, when really you need certain models. A standardized way to measure that and show users where their model falls short — versus where the latest Opus sits on the leaderboard — lets them make an informed decision.

**Yas:**
I'd go beyond Assistant — we've got GCX and MCP too. If you want to use your own models with them, the benchmark should reflect, for observability tasks, which are the best models and the best *open* models. It gets to your point: people can make a more informed decision.

**Nicole:**
Where are we still missing things as an industry, not just as a company?

**Yas:**
Just recently a new benchmark called DeepSWE was released, and it's a bit controversial because it flips the ranking from the most popular software-engineering benchmark — where Opus was always leading, here GPT-5.5 leads by a margin. So there's something to be said about the reliability of the benchmarks themselves, since labs test and sometimes tune their models against them. That might actually be good for o11y-bench — I'd *want* a lab to tune against it, so we get free fine-tuning out of the box: as newer models use o11y-bench to tune on observability tasks, they get better at using Grafana and solving observability problems.

**Nicole:**
Thank you — we just hit time. It was really informative, and I'm glad we both found time; this got rescheduled for various reasons. A great overview of all the evals we're doing.

**Yas:**
Thanks — it's nice to step out of the day-to-day and talk about this stuff.

**Nicole:**
And if you're watching, leave any eval questions in the comments and I'll bug Yas to answer them. Thanks everyone for watching.

**Yas:**
Bye.
