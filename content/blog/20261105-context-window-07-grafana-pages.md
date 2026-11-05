---
title: "Build Apps on Your Data with Grafana Pages (The Context Window #07)"
date: 2026-11-05T18:00:00+00:00
draft: false
tags: ["ai", "observability", "english", "livestream", "grafana labs", "the context window", "grafana pages", "observabilitycon", "dashboards", "grafana assistant"]
---

My favourite announcement out of ObservabilityCON was [Grafana Pages](https://grafana.com/) — a way to build a live, interactive data app right from your Grafana instance, with just prompts and no code. In this episode of *The Context Window* — Grafana's livestream series on AI in observability — I'm joined by my co-host **Tiffany Clifford** and by **Stephanie** and **Tom** from Grafana's AI department, who built Pages (it started as a hackathon project to give [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant) a proper Linux sandbox, and turned into something much bigger). We dig into what Pages actually is, build one live from a prompt, and get into the stuff I find genuinely delightful about it: a page is still *real* Grafana — same data sources, same RBAC, same production-ready panels — it's just no longer you arranging things on a grid. We also cover personal data Pages (my sleep-vs-flight tracker, Stephanie's StairMaster world tour), Pages vs dashboards, how it all works under the hood (React in a locked-down iframe, served from a micro-VM sandbox), and the current limitations and roadmap.

Fun fact dropped mid-stream: the ObservabilityCON keynote itself was a Grafana Page. So was this presentation.

{{< youtube TjzXIMfLSTg >}}

## What Grafana Pages is

As Tom put it, a Page is "all of Grafana, minus the panel grid." It's the same data sources, the same RBAC, the same underlying panels and visualization libraries — but instead of you arranging panels on a grid (or Assistant trying to squeeze your intent into what a dashboard can represent), you unlock Assistant and let it do the thing modern models are genuinely good at: writing code and building a website. You keep everything that makes Grafana production- and enterprise-ready, carefully worked out over nine years, and you add interactive, tailored, *pretty* ways to look at your data.

It builds on the Grafana-managed sandboxes announced in the same release — the same underlying layer of Linux compute for AI agents that also powers auto-remediation and investigations.

## Seeing it on Grafana Play

The fastest way to understand Pages is to go poke at it on [Grafana Play](https://play.grafana.org/) — no login, no Cloud account needed. Stephanie showed a few:

- An **observability-survey quiz game** in comic-book style, pulling real data already on Play — built from *one* prompt ("make it higher-lower, comic-book style").
- A **quarterly-review** page, fully interactive with drill-downs by region and customer sentiment — also one prompt, with "make it look pretty" doing most of the design work.
- A teammate's page that pulls your **GitHub contribution data** and thanks you — and, because it uses the inline Assistant, renders the thank-you in the viewer's native language (inferred from internal data).

The point Stephanie and Tom kept coming back to: Pages aren't static. A page can fetch recent data every time you open it and tell you the most noteworthy events in the last 24 hours — so an on-call summary page genuinely updates itself.

## Building a Page from a prompt

We built one live on Play against the demo incident/outage data: *"Create a page to summarize what is noisy and needs attention from the on-call engineer — give us the top three things."* Assistant loops through alerts, shows the queries it's running in a **Sources** tab (no hand-waving about what it's doing), takes live screenshots of the rendered page as it edits so it actually *knows* how it looks, and comes back with dynamic top-three items. Making a page really is just that easy now.

## Personal data Pages

This is where I got carried away. I hooked up my two smart-ring data sources (Oura and Ultrahuman — both have API endpoints) and, from one prompt, got a whole page summarizing years of sleep: best month, worst month, seasonal breakdowns, the slightly-depressing reveal that I average just under seven hours. I didn't ask for the blue-purple theming. I also didn't ask it to correlate my **flights** (TripIt + Flighty, ten years of data) with my sleep — it just did, because the flight data was there. A second prompt gave me an animated replay of every flight I've taken.

Stephanie's was my favourite: a **StairMaster world tour**, ranking gyms she's visited for work by how good the view is (so she doesn't have to think about being on a StairMaster), complete with an out-of-order-machine mini-game and motivational quotes from ultrarunners. And a summit-conditions page pulling weather data for different mountains.

## Pages vs dashboards

So when do you build a page instead of a dashboard? The honest answer from the team is: it's early, and Pages already cover many dashboard use cases. Tom's product-brain answer is "make it a page, period" — but if you have a well-understood dashboard that serves you well, there's no urgent reason to change it, and dashboards still win where you need a **dashboards-as-code** story (Pages has no as-code path yet). For me, I reach for a page when I want to tell a **story** with data — a narrative, some annotation, something I'd present to my manager without drowning her in every metric. Pages is great at filtering down to the readable essentials without deleting anything.

A nice pro tip from Tom: if you ever present real data on a big screen, Pages is for you — you can ask for presentation style and still get real panels backed by real data, instead of screenshotting them out. We're both using Pages for KubeCon talks.

## Remixing, editing, and building from a dashboard

There are several ways to create a page:

- **Ask Assistant** directly in chat.
- **Create new page** with a starter example (service health, minimal, etc.) that pre-seeds the prompt with styling hints.
- **Remix** an existing page — reuses it as a reference and changes style, data sources, or format; saved as its own new page.
- **Start from a dashboard** — turn an existing dashboard into a page (handy when the dashboard is the ongoing stream and you want a "how was last quarter" narrative view).

Editing happens through Assistant too: highlight an element and it's attached as context (it carries the DOM node / `data-page-id`), so you can ask "how did you get this data?" or request a change to that specific element. **Templates** are coming — define a house style once and have everyone in your org generate pages or presentations that match.

## Sharing and access control

Sharing today works a lot like Google Docs/Slides: add specific people, generate a link, or drop it in a folder (folder view/edit permissions carry over). But viewers **must be logged into the Grafana instance** — there is **no fully public "share with the world" option yet**, and no share-by-email-domain yet either. Both are open feature requests; the team explicitly asked for feedback on whether people want them.

Crucially, **data access still respects user permissions**. If you can open a page but don't have access to its data sources, the page opens but shows no data — exactly like dashboards, because the queries still go through your regular data sources with full authorization and RBAC.

## How Pages work: React, sandboxes, and iframes

A dashboard is configuration — a (very large) JSON blob that Grafana lays out into the panel grid at runtime. A Page is a layer lower: what the agent produces is **React source code for a website**, which Grafana renders inside a heavily locked-down, isolated **iframe**, piping through only carefully chosen data.

But something has to safely compile that TypeScript/JSX and bundle it — running arbitrary model output is exactly the kind of unsafe operation you don't want on your main infrastructure. So each conversation gets a thin **Linux micro-VM**. The hard engineering problem was making it *fast*: nobody waits two or three minutes for an EC2 to spin up before losing interest. The team got it to start in under 10 seconds, with each command finishing in under two.

Tom clarified that "sandbox" is overloaded here — there are **two**:

1. The **Linux micro-VM** used only *while building or editing* a page. Once built, the output is just HTML in an S3 bucket — no VM involved anymore.
2. The **iframe isolation layer** inside Grafana, so AI-generated website content renders safely without leaking your data. You control what hosts a page can call out to, per page (important — not every page should be as shareable as, say, my health data). MCP server connections are supported too, and any viewer gets asked for permission before anything runs on their behalf.

## Limitations and roadmap (no promises)

Pages is in **public preview across Grafana Cloud** (not OSS yet, and it will always require Assistant to drive the prompt → page step). Known rough edges and wishes, with the usual "nothing here is a commitment":

- **Multi-editing**: today you don't know if someone else is editing the same page, so you can clobber each other. A "someone else is editing" warning is coming before GA, with proper multiplayer later. (We hit this building the KubeCon deck.)
- **Public sharing** and **share-by-domain**: open questions, driven by feedback.
- **Storage**: pages and their remixes naturally form a graph of related code artifacts, so a Git-inspired storage model feels like the next natural step.
- Higher environment fidelity, templates (rolling out now), and more examples.

If you want it for OSS — which I personally do — leave a comment so the team can champion it internally.

## Resources

- [Grafana Play](https://play.grafana.org/) — try the public Pages (games included), no login required
- [Grafana Cloud](https://grafana.com/products/cloud/) — sign up free; Pages is in public preview
- [Grafana Community Slack](https://slack.grafana.com) — there's a Grafana Pages channel for feedback

### Related reading
- My notes on [Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant)

### More from The Context Window
- [#05: An Overview of AI Evaluation](/blog/20260626-context-window-05-ai-evaluation/)
- [#04: CLI and MCP Basics for AI Agents](/blog/20260603-context-window-04-cli-mcp/)
- [#03: All About AI Observability](/blog/20260422-context-window-03-ai-observability/)

## Transcript

### Intro, guests, and ObservabilityCON recap

**Nicole:**
Hi everyone, welcome to another episode of The Context Window. Today we're talking about the hottest thing — in my opinion — to come out of ObservabilityCON: Grafana Pages. It's a way to build a live, interactive data app right from your Grafana instance, with just prompts and no code. I'm not the only one excited about it, so — Tiffany, do you want to introduce yourself, my awesome co-host?

**Tiffany:**
Hi, I'm Tiffany, a developer advocate. Until literally a couple of days ago I was focused on Tempo, Pyroscope, and AI — and now just AI, so I get to dive into all this really cool stuff. This one's new to me anyway.

**Stephanie:**
Hello, I'm Stephanie. I work in the AI department with Tom. We did a hackathon together for Pages and have been working on getting it released for ObservabilityCON. That's been fun. Tom?

**Tom:**
Hi, I'm Tom, also in the AI department — I've been at Grafana seven years. For the last couple of months Stephanie and I were toying with the idea of giving Assistant a proper Linux sandbox and a proper way to execute code. We didn't even set out to build Pages — then we realized we could just let it write React code, and that gives you so much better visualizations and tailored outcomes than dashboards.

**Nicole:**
I'm Nicole van der Hoeven, a developer advocate mainly focused on AI right now. And I wanted to mention ObservabilityCON, which just passed — I wasn't there in person, but a lot came out of it. The keynote on YouTube is really good.

**Tom:**
Can I tell you a secret? The keynote is a Page. And, sneakily, so is this presentation. The three ObservabilityCON themes were autonomous operations — and look, there's Grafana Pages right there — cloud economics, and context. We'll focus on Pages.

### What Grafana Pages is

**Stephanie:**
We started by working on sandboxing for coding agents, then in a hackathon realized we could use those sandboxes for Grafana Pages. It lets you see your data in more interactive ways — you can prompt Assistant with "I want to look at my business revenue for the past quarter," or weather on a mountain, and it creates unique interactive ways to look at data.

**Tom:**
If I had to describe it, it's all of Grafana minus the panel grid. Same data sources, same RBAC, same underlying panels, same visualization libraries. It's just no longer you arranging them on a grid, or Assistant trying to fuse your thoughts into what a dashboard can represent — we unlock Assistant and let it write code and build a website. But you're not giving up the things that make Grafana production- and enterprise-ready, carefully worked out over nine years.

**Tiffany:**
And the sandboxes you mentioned — is that the Grafana-managed sandboxes that also got released?

**Tom:**
Those were coined more towards auto-remediation and investigations, where we use sandboxes to look at your source code and check a hypothesis for why something's broken. But it's the very same underlying layer of Linux compute for AI agents that powers Pages too.

### Grafana Pages examples on Grafana Play

**Nicole:**
The best way to understand Pages is to dive in on Grafana Play — this playground for all things Grafana. No login, no Cloud account. You can just mess around and see what people have already created.

**Stephanie:**
Here's an observability survey — we run one every year — turned into a game. It's pulling in real data that's already on Play, with little animations, streaks, ten questions. Maybe you think reading the survey is dry; a game could help. And this was *one* prompt: "make me a higher-lower game, comic-book style." I'm not a front-end engineer — I did not do this.

Here's a quarterly-review example, also one prompt, all interactive — drill into what the customer is thinking, different regions, fake sales data. I can't get over how pretty it is. There's also a Sources tab so you can see the queries behind the data. A teammate made one that pulls your GitHub data and thanks you for your contributions.

**Tom:**
That one uses the inline Assistant, so the page itself can make model generations — it shows the thank-you in the viewer's native language, guessed from internal data.

**Stephanie:**
The powerful part is it's not static. You can make a page that summarizes recent data, and it's not hard-coding the summary — every time you open it, it first fetches recent data and tells you the most noteworthy events in the last 24 hours. I made an on-call rotation page that surfaces the most urgent things every time I look.

### Build a Grafana Page from a prompt

**Tom:**
Since it's so easy to prompt — can we build one from scratch on Play?

**Stephanie:**
You go to Pages, create a new page, pick from starter examples that give Assistant some styling direction so you don't need a huge prompt.

**Nicole:**
Let's say: *"Create a page to summarize what is noisy and needs attention from the on-call engineer — give us a summary of the top three things."* It's so cool that making a page is now just that easy.

**Stephanie:**
It's looping through alerts, figuring out the alert states, and showing its queries in the Sources tab — so it's not hand-wavy; you can check it's actually doing what you asked.

**Tom:**
Depending on what you ask, it can take a bit longer. Let's leave it and jump to some other things.

### Personal data Pages: sleep and flight tracking

**Nicole:**
I have two smart rings — Ultrahuman and Oura. I hooked up both data sources (they have API endpoints), and this whole page was one prompt: how much sleep I get each year, best and worst months, by season. I average just under seven hours. I didn't ask for the blue-purple theming either.

Then it added a travel page — I realized it's correlating my flights with my sleep, because I have flight data in here too (TripIt and Flighty, ten years). I didn't ask it to do that.

**Tiffany:**
I was literally looking into TripIt yesterday — and apparently they closed the API in late September to anyone not already using it. I'm so glad you've been using it.

**Nicole:**
This replay — this one I *did* ask for, so two prompts — animates all my flights, new countries, busiest month. Pages has been useful for more than the usual outages.

### Grafana Pages vs dashboards

**Nicole:**
When would you build a page versus a dashboard? Are you all-Pages all the time now?

**Tom:**
The product person in me says "make it a page, period." Honestly we don't fully know yet — Pages cover many dashboard use cases. If you have a well-understood dashboard that serves you well, there might be no immediate reason to change it. But in general Pages should replace most dashboard use cases, and if they fall short, that's a reason to talk to us.

**Stephanie:**
For dashboards, if you need a dashboards-as-code story — running the same dashboard across many clusters — we don't have Pages-as-code right now, so dashboards still win there.

**Tom:**
Pages will not come to OSS without Assistant — the way it works, you have to prompt Assistant to make it into a page. Assistant has a lot of smarts about correlating Grafana data; a vanilla model wouldn't have the opinionated, docs-backed best practices.

**Tom:**
Pages are very much a Grafana thing. Grafana has always stood for two things — that it's pretty, and that it's serious, as in real data, not made up. We tried hard to preserve both: lots of tuning so a small prompt gives a pretty page, and it still retains inspectability and real data rather than looking like LLM slop. If you just want to post something up, tools like Claude artifacts already exist.

### Remix a Page or create one from a dashboard

**Stephanie:**
The main way is prompting. There's also "make your own," where you prompt it much more specifically about the look. Templates are coming — define a style for your whole org's presentations. And you can **remix** a page: it uses the page as a reference and changes style, data sources, or format depending on what you ask; saved as its own new page.

For editing, you highlight an element and it's attached as context — the DOM node with its `data-page-id` — so you can ask how it got the data, or request a change to that specific element. You can also start a page **from a dashboard**.

**Nicole:**
I tend to build a page when I want to tell a story with the data — some narrative, maybe annotation. My dashboards get cluttered; Pages lets me streamline to what's readable without deleting anything. Great for explaining something to my manager.

### Share Pages and control access

**Stephanie:**
To share, you can add specific people, say "anyone with this link," or put it in a folder so folder permissions apply. There's no fully public "share with the world" option today — that's a feature request; let us know in the comments. And data access respects user permissions: if you can open a page but lack access to its data sources, it opens but shows no data, just like dashboards.

**Tom:**
It's best described as the Google Docs/Slides model — share with specific people or generate a link — but viewers must be logged into the Grafana instance. There's no public option yet.

### How Pages work: React, sandboxes, and iframes

**Tom:**
A dashboard is configuration — a big JSON blob Grafana lays out into the panel grid at runtime. A Page is lower-level: what the agent produces is React source code for a website, which we render in a heavily locked-down, isolated iframe, piping through carefully chosen data.

Something has to safely compile that JSX and bundle it, which is unsafe to do with arbitrary model output — so each conversation gets a thin micro-VM. Making that scalable took most of the platform time: you don't want to wait two or three minutes for an EC2. We got it to start in under 10 seconds, every command finishing in under two.

The term "sandbox" is overloaded. There are two: the Linux micro-VM used while building or editing a page — once built, it's just HTML in an S3 bucket, no VM anymore — and the iframe isolation layer inside Grafana, so AI-generated content renders safely without leaking your data.

**Stephanie:**
There's a setting for what a page can call out to, and you can control it per page — some things, like my health data, shouldn't be broadly available. MCP server connections are supported too, and viewers are asked for permission before anything runs on their behalf.

**Stephanie:**
Data sources still use the user's permissions — if you don't have access, it won't show data. It builds on battle-tested, enterprise-ready foundations, so authorization and RBAC carry forward.

### Limitations, roadmap, and more Page examples

**Nicole:**
Beyond sharing, what other limitations should people be aware of?

**Stephanie:**
Multi-editing is difficult — right now you don't know if someone else is editing a page, so you can overwrite their work. Until GA, just tell people if you're editing. We'll have a "someone else is editing" warning before GA and proper multi-edit later. Templates are rolling out now.

**Tom:**
Pages and remixed pages form a graph of relationships and are code artifacts, so some Git-inspired storage system feels like the natural next step — but it needs careful thinking.

**Nicole:**
I have an unnecessary setup where Alloy on my laptop sends metrics about my Obsidian notes into Loki and Prometheus — and I have a page for all of it: top topic this month, a GitHub-style contribution heat map, a graph view. I didn't ask for any of the styling; I just said "here's some data, build me a page."

**Stephanie:**
My favourite is my StairMaster world tour — I do mountaineering, so as I travel for work I find StairMasters with pretty views. One prompt ranked the gyms by view, added a mini-game for out-of-order machines, and pulled motivational quotes from ultrarunners. I also made one for summit weather conditions on different mountains.

**Nicole:**
There's a Grafana Play page on Singapore weather and haze that's beautiful — it shows wind direction and air quality across regions, with a 72-hour replay. I have family in Singapore, so I care about the air quality. Amazing stuff.

If you want to try this, sign up for a free Grafana Cloud account — Pages is in public preview, nothing to contact anyone about — or just play with the ones on Grafana Play. And please give feedback: there's a Grafana Pages channel in the community Slack and a Reddit post. Comment on the video too, especially if you want it for OSS so we can champion it internally.

**Nicole:**
Thank you all for joining — this was a fun one. The next Context Window livestream is later this month with William Dumont, about Assistant Watchers. Stay tuned.

**Tom:**
Thanks for building this amazing tool — it's my favourite feature on Grafana now.
