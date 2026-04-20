---
title: "How to use Grafana Assistant with self-hosted Grafana"
date: 2026-04-20T09:00:00+01:00
draft: false
tags: ["grafana", "english", "video", "grafana labs", "grafana assistant", "ai", "tutorial"]
---

In case you missed it, possibly the biggest news to come from GrafanaCON this year is that if you're running self-hosted or open-source Grafana, you can now connect it through your Grafana Cloud account to [Grafana Assistant](https://grafana.com/products/cloud/ai-tools/), the purpose-built AI tool for all things Grafana.

In this short tutorial, I show you how to enable Assistant on a self-hosted Grafana instance and go from *nothing* to a working server-health dashboard with a single prompt.

{{< youtube 0O0ZqrruGns >}}

## A quick note on what "for open source" actually means

Assistant itself isn't open source. But you can now use it *with* your self-hosted or open-source Grafana instance. The way it works is:

- You still need a Grafana Cloud account (the free tier has [generous inclusions](https://grafana.com/pricing/) for Assistant).
- You link your self-hosted Grafana to that Cloud account.
- Assistant then lights up inside your OSS instance.

Think of the Grafana Cloud account as the key that unlocks Assistant wherever your Grafana lives.

## Prerequisites

- **Grafana OSS v13 or later**
- **A Grafana Cloud account** ([pricing here](https://grafana.com/pricing/))

## Enabling Assistant

1. Go to **Administration → Plugins**, search for **Assistant**, and click **Install**.
2. Refresh the page, then open the **Connection** tab.
3. Click **Start Connection**. You'll be prompted to log into Grafana Cloud.
4. Select the organization and stack you want, then click **Authorize connection**.
5. Close the tab. Your self-hosted Grafana is now linked to Assistant.

## A first dashboard from nothing

Every Grafana instance ships with a **TestData** data source — perfect for a first run when you don't yet have real data wired up. Enable it from Data Sources, then open Assistant (the new icon on the top right).

Switch Assistant's mode from **General** to **Dashboarding** — this mode is tuned for creating and managing dashboards — and ask in plain English, for example:

> Hi Assistant, could you create a server health dashboard for me using the TestData data source?

What comes back is a starting dashboard with CPU, memory, disk, and network panels already wired up. From there you can tweak panels, edit queries, or ask Assistant to iterate. You're not starting from scratch — you're starting from 80%.

## What else Assistant can do

I only showed dashboarding in this video, but Assistant can also:

- Answer questions about the data already in your Grafana
- Run investigations to troubleshoot production incidents
- Learn new skills
- Manage alerts
- Teach you Grafana

That list keeps growing, so stay tuned.

## Resources

- [Grafana Assistant](https://grafana.com/products/cloud/ai-tools/) (product page)
- [Grafana Cloud pricing](https://grafana.com/pricing/)
- [How Grafana Labs handles your data](https://grafana.com/legal/grafana-cloud-data-processing/)
- [My notes on Grafana Assistant](https://notes.nicolevanderhoeven.com/Grafana+Assistant) — everything I'm learning as I work on it
- [Unlearnings from building Grafana Assistant](https://contexthorizon.substack.com/p/unlearnings-from-building-grafana) — my Context Horizon piece on what the team had to unlearn
