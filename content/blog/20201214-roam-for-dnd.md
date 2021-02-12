---
title: "How I use Roam Research for D&D: Session Notes"
date: 2020-12-14T20:13:13+01:00
draft: false
tags: ['english', 'zettelkasten', 'D&D', 'roam research', 'taking notes', 'text']
---

In case you thought this site was all about performance and load testing, surprise! It's not.

If you've talked to me personally for longer than ten minutes in the last year, there's a pretty good chance I've mentioned [Roam Research](https://roamresearch.com/), or the note-taking and learning methodology called [Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten). Sorrynotsorry. I've been obsessed since I discovered it.

To say Roam Research is a note-taking device is like saying Bitcoin is currency: yes, it IS that, but also so much more. To me, it's my second brain. It's a record of what I know and what I want to know, and sometimes even things I don't know yet. The real reason that Roam and the Zettelkasten idea resonated with me so much is that I can use it a lot for my work. But I've discovered another use case that Roam is perfect for: Dungeons & Dragons.

This became longer than I thought it would be, so I'll just talk about how I handle Session Notes in particular.

## Starting a new session

Everything starts with sitting down to play D&D. I write a log of events and information that comes out while I'm playing. Here's what a new session log looks like:

![](/assets/20201214-03.png)

I preface pages in this campaign with `D&D/` to make it a separate [namespace](https://forum.roamresearch.com/t/namespaces-how-do-they-work/276). A namespace is like a folder, and I use it mainly because I have two D&D campaigns, both of which would have the page `Campaign`, `Characters`, `Locations`, etc, even though the two campaigns are on different worlds. To keep them separate, and to keep from getting mixed up (_Was Gloomtoes an NPC in this campaign or that one?_) I use different namespaces for each campaign.

I add the real-world date in the page name, and then an in-game date reference. The in-game date reference is useful for keeping track of time since I might go a couple weeks (okay, maybe _one_ week; let's not get too crazy) without playing this campaign, but no time in the in-game world has elapsed. Then, I end the page name with a descriptive title, which I always end up changing after the session. Sometimes I'll title a page `Exploring Castle Never`, but then we end up getting carried away in another part of the city instead. That's okay - when I change a page name, Roam then updates all references to that page that I've made from other pages.

I don't type all this out manually - I use a [TextExpander](https://textexpander.com/) template so that to start a new session, all I have to do is create a page in Roam, type `;s.dnd` and that is automatically replaced with prompts for a few fields. 

* `Date`: This is the real-world date of when I played this particular session.

* `Tags`: When I first create session notes, this is prepopulated with `#TVZ`, which stands for _To Verzettelen_. It's just my personal way of marking a note as one that needs to be processed.

* `Location`: Here I note down the in-game places that my character visited this session. Usually I'll just put city names, but I sometimes also split locations up into districts within a city or rooms within a dungeon.

* `Characters`: I've found it helpful to keep track of which characters (players and NPCs) I've come across in this session.

* `Session Summary`: This is a section I leave blank when the session is initially created.

## Filling in the session log

The rest of the page, after `Session Summary`, is where I'll spend most of the time writing. I just write whatever comes to mind and whatever I have time to write, in bullet form. I don't worry about formatting or grammar or linking to other pages. I just type all my thoughts out in plain text.

### HP

I like to play healers, which means I care a lot about how everyone in the party is doing so that I can figure out who best needs healing. `{{[[table]]}}` in Roam lets me create a custom table, and I have a `;hp` snippet in TextExpander that recreates this table, with all the names of the people currently in my party, so that I just worry about filling in the values. Sometimes I still get it wrong, or miss a bit of damage that the DM calls out, but it's enough to give me an idea of who needs heals.

![](/assets/20201214-04.png)

I also write down initiative orders, the defenses/vulnerabilities/immunities of monsters we face, descriptions of NPCs we meet, suspicions or questions I might have... basically anything and everything that comes to mind. Session time is pretty much a brain dump, with no formatting.

### Equipment

If I acquire a new item during a session, I'll tag that line with `#[[D&D/Carrying]]`. This lets me stay on the Session Notes page while still maintaining an up-to-date record of what I'm carrying.

![](/assets/20201214-05.png)

A tag in Roam is the same as a page, so when I click on that link, it takes me to the `D&D/Carrying` page, which conveniently also shows me all the references to that page from other pages.

![](/assets/20201214-06.png)

Roam shows me not just the page, but the exact block where I made the reference to `D&D/Carrying`, so it's easy to see at a glance what I have and where I got it.

### Next Actions and Waiting For

I use David Allen's [GTD](https://gettingthingsdone.com/) methodology in D&D too. When I want to remember to do something later, I tag it with `#[[D&D/Agenda]]` and `#[[Next Actions]]` or `#[[Waiting For]]`. This presents me with the same opportunities as `D&D/Carrying`, where I can see references to those pages later as well.

![](/assets/20201214-07.png)

## Processing the session

Sometime after the session, I'll go and fill in the metadata from my template, including the session summary, which is just a paragraph or two describing what happened in the session at a high level. This is mainly to jog my memory in the next session, when I've already forgotten what we did in the previous one.

Here's what it looks like, all filled in:

![](/assets/20201214-02.png)

### Adding links and fleshing out pages

I then go back through the notes themselves and add turn any people, places, or interesting objects that I mention into links. In Roam, that's a matter of highlighting them and hitting `[[`. Then, I click on the page I've just created and try to add information that I've learned. This isn't strictly necessary, since all mentions of that page will show up as a linked reference, but it's an opportunity to consolidate my information on that subject and see how it fits into what else I've written there.

Here's a page for an NPC:

![](/assets/20201214-09.png)

Having these links means that when an NPC says "I'm from Leilon", I can type `Leilon` into Roam:

![](/assets/20201214-08.png)

... and say, "Oh, Leilon. I heard you had a dragon problem there recently. Did your family get out okay?" Boom! Instant advantage on a Diplomacy check.

Sometimes we're in a dungeon with many rooms, and this is the point where I draw a quick map on my iPad Pro and Apple Pencil using [Notability](https://www.gingerlabs.com/), and then I upload it right from my iPad to Roam.

This map is in my page for Castle Never:

![](/assets/20201214-10.png)

The little blue "8" on the upper left of the map is versions. Information rarely comes all at once in D&D; it usually comes in trickles. As I learned more about the castle, I revised the map and added a new version to it, so that I can still see previous versions and what I thought the map was like when we first explored it.

At this stage, I also add any tags I forgot to add during the session.

### Reviewing quests and questions

After I go through the session notes, I go to the page called `D&D/Quests and Questions`, where I keep a running list of all the open quest hooks and any unanswered questions I might have.

![](/assets/20201214-11.png)

Not everything on this page is meant to be resolved, but I find it comforting to track everything anyway, in case I happen to find myself in a city with nothing in particular to do. I mark these with a checkbox (`{{[[TODO]]}})` in Roam) and tick the box when one is resolved. Roam lets me filter out the resolved quests so I only see things that are outstanding.

This is where I get the most value out of taking notes. It's at this point where I'll add our progress towards quests, make connections between two seemingly disconnected quests, and situate what I've just learned in the session within the broader context of the world and the campaign. I also review and update items on the Next Actions and Waiting For.

This is the part that takes the longest, but it's also what most prepares me for when I get to the table again next week.

## Tying it all together

I use a `D&D/Campaign` page as my landing page for this campaign. It includes `D&D/Quests and Questions` as well as a list of all sessions to date, so that I always know what happened and when.

![](/assets/20201214-01.png)

## Why do I take notes for a game?

You might be wondering why I go to so much trouble. Why do I take complicated notes about something I do "just" for fun?

1. Taking notes helps me offload this all safely from my brain.

2. I take my fun as seriously as I take my work.