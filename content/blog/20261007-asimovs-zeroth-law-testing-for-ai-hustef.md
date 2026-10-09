---
title: "Asimov's Zeroth Law of Robotics: Testing for AI (HUSTEF 2026)"
date: 2026-10-07T10:00:00+02:00
draft: false
tags: ["testing", "presentation", "AI", "grafana labs", "evals", "observability", "trust", "k6", "english"]
---

This week I gave a keynote at [HUSTEF 2026](https://hustef.com/nicole_van_der_hoeven_2026/) in Budapest, Hungary. The talk is called *Asimov's Zeroth Law of Robotics: Testing for AI* — a testing-focused evolution of a talk I've been giving (and rewriting) for a while, previously as *Observability for AI* at [KubeCon EU 2025](/blog/20250402-asimovs-zeroth-law-of-robotics/) in London, [Dutch Cloud Native Day 2025](/blog/20250703-asimovs-zeroth-law-dutch-cloud-native-day/) in Utrecht, [NewCrafts](/blog/20251106-asimovs-zeroth-law-newcrafts/) in Paris, and [ExpoQA Madrid 2026](/blog/20260526-asimovs-zeroth-law-expoqa-madrid/). Here's the abstract:

> A robot may not harm humans. A robot must obey humans. A robot must protect its own existence. These are Isaac Asimov's three Laws of Robotics, created to govern the ethical programming of artificial intelligences. From the Butlerian Jihad to Skynet to cylons, we've been immortalizing our collective nightmares about artificial intelligence for years. But there's an unmentioned law that comes as a prerequisite to all of that: a robot must be testable.

The big shift in this version is right there in the Zeroth Law itself. In earlier iterations I argued that *a robot must be observable*. That's still true — observability is the only way to see the reasoning behind a system and find out what actually happened. But I've come to think that pure knowledge isn't the same as trust. You can know exactly what a system did and still not trust it. The only way to trust something is to put it through its paces: to know how it behaves in the situations you foresee, and even the ones you don't. So the Zeroth Law has become **a robot must be *testable*.**

I framed the whole thing around Asimov's short story *Runaround* (from *I, Robot*) and its robot, Speedy. Speedy's smuggler owners sent him to collect selenium on Mercury, and he got stuck in a loop — circling the selenium pool, unable to resolve the conflict between obedience (the second law) and self-preservation (the third). His owners couldn't predict his behaviour and couldn't reason about it, so they had to do the only thing left: go out into the danger zone and fix him in production. Speedy wasn't untestable because his owners were incompetent or lacked the tools — he was untestable because he was never *built* to be tested. That's the trap I think a lot of AI systems are walking into right now.

The through-line for a testing audience: AI is rewriting *how* software gets built, but it doesn't rewrite the discipline of trust. Trust that a system does what we say it does, and that when it breaks we know why and can fix it — that's always been the job, and it isn't going anywhere. There's a whole generation of AI engineers shipping software they haven't tested and can't explain, and when someone says "the agent does this," our job is still to ask *how do you know?* Testing isn't just going to survive the age of AI — testing is the reason AI gets to survive, if we make it testable.

I demoed this with my TTRPG side project: an AI Dungeon Master, instrumented and put under test. It turns out that writing evals for something non-deterministic forces you to confront your real requirements. I thought I knew exactly when a dungeon master should call for a dice roll — I GM myself! — but trying to put it into words ("in *this* situation I'd roll, but in *that* one I wouldn't, because I want to keep the story moving") surfaced decisions I'd never had to make explicit. Those are things we'd normally discover much later, in production. Having to figure them out up front is a win.

The Q&A was genuinely great and ranged well beyond the slides:

- **"When has an AI been tested *enough*?"** Same answer as for anything else — it's a mix of risk and budget. If it were a life-critical robot like Speedy, you test every scenario the people relying on it need. For my little demo app, less so.
- **Testers vs. developers in the age of AI.** I said I'd fire developers before testers — provocatively, but the point stands: anyone can write code now. What made a good developer good was never the coding; it was communicating with business *and* engineers, translating requirements, finding creative-but-safe solutions. Testers already think at that level and translate across teams, which makes them *more* important in the age of AI, not less.
- **Defining expected results for non-deterministic systems**, multi-turn evals (I give the simulated user a *personality* — adversarial, cooperative, beginner — rather than a script), and the broader shift from imperative to declarative: we no longer instruct step by step, we declare the end state we want, the way we do with Kubernetes.
- **Convincing colleagues not to fear AI.** I don't, really. AI is here to stay; the question isn't whether you approve of it, it's whether you want to stay in this industry and help make it safe and trustworthy — or sit on the sidelines.

I also recommended the book [*Slow AI*](https://nicole.to/asimov), which lands where I do: not an AI apologist, not a boycott, but a clear-eyed list of what AI is and isn't good for — and the reminder to keep checking whether a given use of AI is making you *more* capable or less.

The demo app (the instrumented AI DM) lives on [GitHub](https://nicole.to/asimov), and I keep refining it with each iteration of this talk.

I'll update this post with the recording once HUSTEF publishes it.

## Resources

- [Demo app on GitHub](https://nicole.to/asimov)
- Previous versions of this talk: [KubeCon EU 2025](/blog/20250402-asimovs-zeroth-law-of-robotics/) · [Dutch Cloud Native Day 2025](/blog/20250703-asimovs-zeroth-law-dutch-cloud-native-day/) · [NewCrafts 2025](/blog/20251106-asimovs-zeroth-law-newcrafts/) · [ExpoQA Madrid 2026](/blog/20260526-asimovs-zeroth-law-expoqa-madrid/)
