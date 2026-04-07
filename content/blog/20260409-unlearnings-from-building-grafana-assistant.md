---
title: "Unlearnings from building Grafana Assistant"
date: 2026-04-09T09:00:00+01:00
draft: false
tags: ["ai", "english", "grafana labs", "grafana assistant", "llm", "agents", "observability"]
---

Originally posted [here](https://open.substack.com/pub/contexthorizon/p/unlearnings-from-building-grafana?r=7xe6zg&utm_campaign=post&utm_medium=web&showWelcomeOnShare=true)

Everyone's talking about what you need to _learn_ to build AI agents: Prompt engineering. Tool calling. Retrieval strategies. The content ecosystem is full of it. But while I was watching Context Window Episode 1, it struck me that Mat Ryer, Cyril Tovena, and Sven Großmann-- some of the team behind Grafana Assistant-- spent most of their time on something different: what they had to _unlearn_.

Grafana Assistant started as a weekend hackathon project. By the time it shipped, the team had thrown out a popular framework, flipped their assumptions about tool design, and discovered that some of the instincts you bring from conventional software development actively work against you when you're building agents.

I pulled out the ten moments where received wisdom turned out to be wrong. If you're building anything agentic right now, these are worth sitting with.

{{< youtube TGWVqBAeIzI >}}

## ❌ LangChain will help us build faster

[LangChain](https://github.com/langchain-ai/langchain) is an opensource framework for building applications that use LLMs. It provides structured components that can be used for rapid prototyping.

In the video, Tovena talks about how they started with LangChain during the initial hackathon because they thought it would help them build more quickly, but instead it became obvious fairly early on that the opposite was true. They didn't end up using a lot of the features that LangChain provided and felt they needed more flexibility and speed.

### Abstraction overhead

One possible reason for their troubles with LangChain is that LangChain has standard abstractions for prompts, tool use, and orchestration-- things that sound good in theory. But sometimes abstractions lend themselves to creating a sort of black box in your stack, where you don't know what's happening inside it. It sounds like the Assistant team missed the oversight and control of what was happening.

## ❌ Use the same prompt for every model

They also talked about how for the sake of simplicity and consistency, they initially used the same prompt for every model. However, they found out that this actually led to worse results. They found more success in creating slightly different prompts for different models, playing to their strengths and weaknesses a bit more.

There is even an argument ([Mizrahi et al.'s "State of What Art? A Call for Multi-Prompt LLM Evaluation](https://arxiv.org/abs/2401.00595)) that AI benchmarks that involve sending multiple LLMs the same prompt is a brittle and unreliable way to assess LLM capabilities. Different models respond differently to prompt variations.

In practice, what this means is that switching models isn't a drop-in replacement. Even if a new model scores better on benchmarks, your prompts were written with a specific model's tendencies in mind. The unlearning here is letting go of the idea that a prompt is model-agnostic — it's more like a conversation style, and different models have different conversational defaults.

## ❌ Treat errors as failures

Traditionally in software, you catch errors and hide them from the user: you log them, handle them, but treat that transaction as a failed one.

The Assistant team had to unlearn this habit when dealing with an LLM, because with agents, error messages *are* useful data. Feeding it back to the LLM often results in it learning from its own mistake and trying again. It's basically letting the agent debug itself, in a manner that Ryer noted was remarkably similar to how we humans debug errors too.

## ❌ Return errors in structured JSON

On the subject of error messages, Großmann mentioned that at one point they were trying to format the errors in JSON or stringified JSON. This practice shows solid engineer intuition because usually, structuring information helps machines process it faster and more accurately. What they found here was the reverse: it was easier and yielded better results when the LLM was just passed the entire error in natural language.

## ❌ Build as many tools as possible

The team mentioned that at the start, they were inclined to create as many tools/skills for Assistant: one for everything that could be done in Grafana. This made sense until they saw LLMs struggle to determine which tool to use in which context.

To help LLMs identify the correct tool, they added tool descriptions and also experimented with combining multiple tools into fewer, parameterized, tools. These helped, although the team still observed that allowing users to create their own tools (with potentially very general tool descriptions) could potentially confuse LLMs.

## ❌ Bigger context window = better

[Gemini 1.5 Pro announced](https://developers.googleblog.com/en/new-features-for-the-gemini-api-and-google-ai-studio/) it had a 2M context window back in 2024, and it might seem that other providers had lagged behind: [OpenAI](https://openai.com/index/gpt-4-1/) only announced support for 1M tokens in 2025 and [Anthropic](https://www.anthropic.com/news/claude-opus-4-6) followed in 2026. However, the Assistant team pointed out that context wasn't everything. They said that they noticed that bigger wasn't necessarily better, also pointing out that the chat summarization feature on IDEs like [Cursor](https://cursor.com/) could still sometimes lose important details when summarizing.

This finding seems to coincide with a 2023 Stanford study ([Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)) that found there was a performance degradation when models access information within a very large context. In the video, they talked about how their system prompts were often 40k tokens long (half for the prompt itself and then the other half for tools).

## ❌ Start with a multi-agent architecture

Tovena mentioned that creating a multi-agent architecture for Assistant yielded more mixed results than he expected. He said that passing context between agents is difficult, outputs were inconsistent, and there was a bit of a "telephone game" problem where agents didn't always perfectly understand the intent or output of other agents.

In early 2026, [Khatua et al. released a study](https://arxiv.org/abs/2601.13295) called "CooperBench: Why Coding Agents Cannot Be Your Teammates Yet" that showed that AI agents aren't great at collaboration. The study suggests, surprisingly, that this might be because AI agents lack human social habits that help us collaborate better, such as feeling obliged to do what we say and having a good understanding of what others' plans are.

The Assistant team's experience is also a perfect example of [Gall's Law](https://www.laws-of-software.com/laws/gall/), which states that it's easier to start with simplicity and build complexity than the other way around.

## ❌ Plan around models as they are now

Software has always moved quickly, but it feels like AI models are moving faster. [Stanford's AI Index Report 2025](https://hai.stanford.edu/assets/files/hai_ai_index_report_2025.pdf) reported that models went from having a 50% chance to near-human performance in roughly 2 years (2021-2023). In fact, benchmarks keep getting retired as AI saturates them-- meaning that benchmarks can't reliably be used to distinguish between good and bad models because all the models are testing near the ceiling.

The rapid pace of development around AI requires us to not be so attached to our work: Großmann recalled an incident where someone wrote a joke prompt that spoke like a dog that shockingly did better than their other system prompts. Ryer also mentioned that at one point someone deleted all the system prompts and Assistant weirdly became more accurate.

The lesson is clear: plan for models to improve, and plan to redo a lot of your work when they do.

## ❌ We don't need evals

The Assistant team said that they went from having no evals to employing several types of evals:
- integration-style evals that exercise whole workflows
- unit-style evals that feed inputs plus a system prompt and check the output
- LLM-as-judge, where they pass conversations to an LLM to ask it to judge whether it answered the user's questions.
- user feedback in the form of thumbs during conversations with Assistant

Beyond evaluation, they talked about how important it was to be able to observe AI. At the very minimum, showing what Assistant is doing at all times (thinking out loud) is very important to them because it builds users' trust in the thinking process and, eventually, in the result.

Evals aren't a sign that you don't trust your product. They're how you build the confidence to keep shipping it.

## ❌ Assume people already know how to work with AI

When you ship an AI feature, it's tempting to assume the hard work is done. You've built the thing. Users will figure it out.

What the Grafana Assistant team found was that this assumption doesn't hold. Users came in with wildly different mental models of what an AI assistant could or should do — some treating it like a search box, others expecting it to read their minds, most not yet sure how to prompt it effectively.

Their insight was that this isn't just a UX problem to solve on your end. It's a shared responsibility: AI should try to help the user, but the user also needs to learn how to work with AI. And building an assistant that teaches people how to use it well (through good responses, gentle corrections, showing its work) is part of building the product.

There's also a deeper point here specific to observability. Grafana Assistant isn't just an AI feature; it's a way of interacting with your own infrastructure. Every good interaction teaches you something about what questions to ask, what signals to look for, what it means to understand a system. In other words: learning to use AI well makes you a better engineer. The tool and the skill co-evolve.

This is the unlearning that sits furthest from the code. It's not about prompts or architectures or frameworks. It's about recognising that you're not just shipping a feature-- you're introducing a new way of working. That takes time. And it's worth designing for explicitly.

## Summary

What strikes me most about this list isn't any single item — it's the pattern. Most of these unlearnings point in the same direction: _less is more, and messiness is the point._

Less abstraction. Fewer tools. Smaller context. Simpler architecture. And rather than hiding the mess — the errors, the reasoning, the uncertainty — let it show. That's where the trust gets built.

We're all still early with this. The team that built one of the most thoughtful AI products I've seen up close still didn't have evals when they launched. That's not a criticism — it's a reminder. You don't need to have it all figured out before you ship. You just need to commit to keep unlearning.
