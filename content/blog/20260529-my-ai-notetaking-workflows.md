---
title: "My AI note-taking workflows"
date: 2026-05-29T17:00:00+01:00
draft: false
tags: ["pkm", "ai", "obsidian", "video", "english", "note-taking", "voice", "plaud", "granola", "voicenotes", "spokenly"]
---

Just over a year ago, if you'd asked me how I felt about AI and note-taking, I would have told you I didn't want AI anywhere near my notes. The world is different now, and so am I — I rely on AI in a lot of ways, and one of the easiest places to start is speech-to-text: using AI to convert my voice into something my [PKM](/blog/) system can actually work with.

In this video, I walk through **three tiers of AI note-taking workflows** — free, paid, and (a little) overkill — and show what I'm using at each level.

{{< youtube 2Jl6H9Ri8iI >}}

## The framing: note-taking vs. note-making

[Nick Milo](https://www.youtube.com/@LinkingYourThinking) draws a useful distinction between note-*taking* and note-*making*:

- **Note-taking** is collecting — recording information, paraphrasing what an author said, highlighting.
- **Note-making** is connecting — active thinking, engaging with the information, linking it to other ideas, working out how it fits into your PKM system.

The best use of AI right now, for me, is to help with the note-taking part. I like to start with speech because speech used to be a form of input my PKM system couldn't take very much of. Pre-AI, voice was lossy — you'd have to transcribe it yourself or lose the thought. Now: you speak, AI transcribes it, it lands in your notes, and the AI can keep working with it from there.

## Tier 1 — Free

Use your phone's recording app. iOS Voice Memos transcribes recordings, and the Notes app does too on newer Apple devices. Samsung's Voice Recorder app does the same on Galaxy devices. For desktop, I demo [Spokenly](https://spokenly.app/) (Mac, Windows, iOS) — drop audio in, get text out.

- **The friction is manual:** remember to record, remember to transcribe, remember to paste.
- **What you get:** quick notes to yourself, captured instantly.
- **Best for:** people who want to get started as easily as possible without paying for anything.

If you want to go local-first, I'd point you at [NVIDIA Parakeet](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) and the [Qwen](https://huggingface.co/Qwen) models for offline transcription.

## Tier 2 — Paid

The second tier is paying for the convenience layer. These tools collapse the first two steps — you record, the transcript appears, and you usually get extras like AI summaries or the ability to ask questions of the transcript (sometimes live).

Tools: [Voicenotes](https://voicenotes.com), [Otter.ai](https://otter.ai), [Letterly](https://letterly.app), [Granola](https://www.granola.ai), [Gemini](https://gemini.google.com) on Google Meet, [Zoom AI Companion](https://www.zoom.com/en/ai-assistant/).

For Granola specifically, I use the [Granola Sync Obsidian plugin](https://github.com/tomelliot/obsidian-granola-sync) plus a [QuickAdd](https://github.com/chhoumann/quickadd) macro (`QuickAdd: Macro - Link Granola`) to automatically link a transcript to the right note in my vault — in the video I link a [Dungeon Crawler Carl](https://www.youtube.com/@Bookborn) recap to its Granola transcript. *(The linking script and macro are on my [Patreon](https://patreon.com/nicolevdh).)*

**Tradeoffs:**
- Your notes live in their system, not yours. Shutdowns, pricing changes, and acquisitions all take your archive with them.
- The friction reduction is real, though — if it means you actually capture instead of *intending* to capture, that's worth a lot.

**Best for:** people who want to capture meetings, games, or lectures.

## Tier 3 — Overkill

This is my setup. It's a little ridiculous; I'm going to show it anyway.

- **Hardware:** a [Plaud](https://plaudus.sjv.io/MA4GQN) AI recorder. Small, clips to my phone or sits in a pocket. Always running, or started deliberately for important conversations and walks. It can run entirely locally, or upload to Plaud's servers.
- **Plugin:** [my fork](https://github.com/nicolevanderhoeven/plaud-sync-for-obsidian) of [Leonard Sellem's Plaud Sync plugin for Obsidian](https://github.com/leonardsellem/plaud-sync-for-obsidian), installed via [BRAT](https://github.com/tfthacker/obsidian42-brat). The fork adds a couple of things I needed for my own daily workflow.
- **AI layer:** [Iris](https://openclaw.ai), my [OpenClaw](https://openclaw.ai)-powered AI agent, watches the synced files. Every morning she reads the previous day's transcripts, plus my calendar and daily notes, and outputs a daily summary, extracted tasks, and flags anything I've said I wanted to remember.

I also use **"Hey Iris" memos** — voice notes I record into Plaud while I'm out, addressed to Iris, that she processes the next time she runs. *"Hey Iris, remind me to follow up with X."* *"Hey Iris, add this restaurant to my places-to-try list."* They land in my system without me opening anything.

**Benefits:** I don't think about capture at all. I just live and talk, and the relevant pieces land in my notes.

**Cons:** the privacy of people around me. I'm careful about when this is on, and especially careful about explicit consent.

## Why three tiers, not one

The slightly absurd thing is that I still use all three levels — in parallel, for different things:

- **Spokenly** for dictating at my desk, sometimes straight into Obsidian, sometimes into a chat.
- **Granola** for meeting notes, and increasingly for transcribing videos I'm watching.
- **Voicenotes** for diary-style entries.
- **Plaud** when it's ethical to (especially when I'm travelling with my partner and I want a clean record of conversations and ideas we had on the move).

For me, voice is the **lowest-friction capture method that exists**. No stopping, no finding my phone, no opening an app, no typing. Just talk — and the system handles everything downstream.

That means the gap between *thinking of something* and *writing it down* is basically gone for me. Note-*taking* — the tedious part — gets offloaded. So when I'm in a meeting I can be present, knowing the tool is faithfully tracking what's said. Whatever notes I *do* take are then what *I* think about what I'm hearing, which lets me start synthesising a lot faster.

If you want more details about any of these workflows, let me know in the comments. _Arigatō gozaimashita! Mata kondo ne~_

## Resources

- 🎙️ [The Mechanics of Knowledge Management podcast episode](/blog/20250427-mechanics-of-knowledge-management-podcast/) where Malik interviewed me on this stuff
- 🧠 [My notes on OpenClaw](https://notes.nicolevanderhoeven.com/OpenClaw) — the agent runtime Iris runs on
- 🎤 [My notes on Voicenotes](https://notes.nicolevanderhoeven.com/Voicenotes)
- 💛 [My Patreon](https://patreon.com/nicolevdh), where I share the QuickAdd linking scripts and macros
