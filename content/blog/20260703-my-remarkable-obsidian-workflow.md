---
title: "My reMarkable Obsidian workflow"
date: 2026-07-03T17:00:00+01:00
draft: false
tags: ["pkm", "obsidian", "remarkable", "handwriting", "ocr", "ai", "video", "english", "note-taking"]
---

I'm a big note-taker — but what most people don't realise is that digital notes have only ever been a small part of that. I love analog notes, and lately I've loved *meshing* the analog with the digital using E Ink tablets. The problem with the reMarkable has always been the workflow: there hasn't been an easy way to get everything back into [Obsidian](/blog/), which — as you know — is kind of important for me.

In this video I show how there's *finally* a clean way to tie it all together: reMarkable → Obsidian as a PDF → searchable, OCR'd text.

{{< youtube h1Sv7sXMEj0 >}}

## The setup: a lot of E Ink

I've tried a lot of E Ink tablets and readers. My everyday carry is the **reMarkable Paper Pro Move**, and I keep a full-size **reMarkable Paper Pro** at my desk. I love them more than the Kobo or Kindle Scribe lines — but the deciding factor was always going to be whether I could get my handwriting into Obsidian without friction.

## Step 1 — Sync the PDF into Obsidian

The piece that makes this work is a community plugin: **[reMarkable Sync](https://github.com/TimDommett/Remarkable-Sync---Obsidian-Plugin) by Tim Dommett**.

- In Obsidian, go to **Community plugins → Browse**, search for *reMarkable*, install and enable it.
- The first time, you'll **register** the plugin — it sends you to your reMarkable page, gives you a one-time code, and you paste that in and hit register.
- In settings, choose a **sync sub-folder**. I put mine under `plugins/reMarkable`.
- Set the **sync interval** — I have mine sync every 30 minutes, but you can go more frequently, manually, or trigger it on demand from the command palette (`reMarkable Sync: Sync documents`).

Once that's done, anything I write on the reMarkable lands in my vault as a **PDF** — diagrams, cursive, print, colours and all. In the video I write out a page (neural nets, as explained by my partner Noel), trigger a manual sync, and watch it appear in Obsidian.

## Step 2 — OCR the handwriting into real text

A PDF in Obsidian is a start, but it isn't *searchable* or editable. That's where **OCR** (optical character recognition) comes in — turning the handwritten image into text that behaves like any other note: searchable, linkable, modifiable. I keep the PDF too (I like preserving the colours and the handwriting, especially when someone else wrote on my tablet), but I want the durable text version as well.

I automate this with **[OpenClaw](https://openclaw.ai)** — my AI agent, [Iris](https://openclaw.ai), runs a skill on a heartbeat that watches my reMarkable folder, notices new files as they drop in, and OCRs them automatically. It even fills in properties I like and, because it knows my context (and sometimes has the transcript too), it can describe diagrams more completely than I'd expect. It correctly read *"Neural nets as explained by Noel"* and *"get diagrams from WhatsApp"* — whether I wrote in print or cursive.

**That setup is admittedly overkill**, and not something I'd recommend to everyone. So in the video I also show the more accessible version:

### The accessible alternative: Claude Cowork / Claude Desktop

If you'd like to automate OCR without a full agent setup, the **Claude Desktop app** (with Cowork) is a great option — especially if you already keep notes, since your vault is exactly the kind of context that makes AI immediately useful.

The prompt I use, roughly:

> *You are in my Obsidian vault, in the folder `plugins/reMarkable`. Look for the very latest PDF I've put in there and OCR it. If there's a diagram, describe the diagram. If there's text — handwritten cursive or print — transcribe it. Print all of your findings into a note in the `plugins/Claude output` folder, using the same file name as the original PDF.*

It reads the latest PDF, describes the diagram (it got "neuron" and "perceptron" — words that were never actually written), and writes the note. Interestingly it did as well as my own setup, because under the hood we were both using the same model (4.8).

**Then turn it into a skill.** I tell Claude: *"Please turn all of these instructions into a skill and call it OCR."* It writes the skill, preserving the paths, and I hit save. Now next time I have a reMarkable PDF to transcribe, I just run `/OCR` and name the file. If you want to go further, you can even ask it to make this a scheduled task.

*(Tip: I use [Spokenly](https://spokenly.app/) to dictate these instructions to Claude rather than type them.)*

## Why this matters

This simple workflow has made it so I can *actually use* my reMarkables. I love typing notes on my laptop, but when I'm face-to-face with someone — in a talk, at a conference — a screen between me and the speaker feels distancing, and a little rude. I feel more present without it. And the little Paper Pro Move is far easier to carry than a laptop or iPad.

Now that I know everything ends up in Obsidian anyway, I get to pick whatever note-taking method I feel like in the moment — typing, reMarkable, or fully analog. That same OCR process (minus the reMarkable Sync plugin) also works for OCRing photos of pages from my paper traveller's journal.

If you'd like to go deeper on how I use AI in my note-taking, check out my [AI note-taking workflows video](/blog/20260529-my-ai-notetaking-workflows/) — I cover the different audio transcription tools I use there too.

_Arigatō gozaimashita! Mata kondo ne~_

## Resources

- 🖊️ [reMarkable Sync by Tim Dommett](https://github.com/TimDommett/Remarkable-Sync---Obsidian-Plugin) — the Obsidian community plugin that syncs reMarkable documents into your vault as PDFs
- 🧠 [My notes on OpenClaw](https://notes.nicolevanderhoeven.com/OpenClaw) — the agent runtime Iris runs on
- 🎥 [My AI note-taking workflows](/blog/20260529-my-ai-notetaking-workflows/) — the companion video on transcription and AI capture
- 🗣️ [Spokenly](https://spokenly.app/) — the dictation app I use to talk to Claude
- 💛 [My Patreon](https://patreon.com/nicolevdh)
