---
title: "How I use Obsidian for D&D - Player's Edition"
date: 2021-08-09T17:46:51+02:00
draft: false
tags: ['zettelkasten', 'obsidian', 'Markdown', 'roam research', 'text', 'english', 'D&D']
---
{{< rawhtml >}}
<meta property=“og:image” content="/assets/Forgotten-Realms-workspace-in-Obsidian.png" />
<meta property=”og:image:width” content=”1200″ />
<meta property=”og:image:height” content=”628″ />
{{< /rawhtml >}}

I've previously written about [how I use Obsidian for work](https://nicolevanderhoeven.com/blog/20210518-how-i-use-obsidian-at-work/), and I've also talked about [how I use Roam Research for D&D](https://nicolevanderhoeven.com/blog/20201214-roam-for-dnd/). Shortly after the latter post, however, I moved to Obsidian. That was six months ago, so I thought it was time for an update.

## Before the game

### World

My World page is the main jumping-off point for all my notes for a specific campaign, and each campaign gets one. It contains:

- The main locations in the world
- The player characters, and links to their individual pages with information about what my character knows or thinks of them
- A link to Open Loops (Quests and Questions and Agenda, as discussed below)
- The list of all the sessions I've played for the campaign
- Campaign-specific house rules that the DM has introduced

![The World page for my Forgotten Realms campaign](/assets/world-page.png)


### Quests and Questions

I like to play high-intelligence characters, so I like to keep track of unanswered questions and other adventure hooks my DM has dropped that the party hasn't quite gotten around to resolving yet. Some of them are critical quest or story arcs, and others are random tidbits of information that NPCs have mentioned. I organize them by location, and then by quest, so that it's easy to follow a thread depending on where the party is or how much downtime we have. Here's an example of that page:

![Quests and Questions page](/assets/quests-and-questions.png)

### Agenda

While the Quests and Questions page records unfinished business that my character is actively thinking about but may not quite know how to explore yet, my Agenda page is where I write down specific tasks. I loosely follow the [Getting Things Done](https://gettingthingsdone.com/) methodology and divide this page into Next Actions and Waiting For. I group tasks by person and/or by location.

![Agenda page](/assets/Agenda-sample.png)

I use the Obsidian [Completed Area plugin](https://github.com/DahaWong/obsidian-completed-area) so that hitting a CTRL + ENTER on a task automatically checks it and then moves that task to a separate Completed section at the bottom of the note. This helps me keep the agenda clean and relevant.

## During a game

### Workspace

One of the best parts about Obsidian is that it allows me to save and load custom workspaces. This is useful because I use Obsidian for work as well as play, so I can set up the two workspaces differently. I also DM one campaign and play in another, and I have a workspace for each of them because I need different information available to me. The workspace features lets me customize my dashboard. Here's what my workspace looks like for the 4e game that I play in:

![My Forgotten Realms campaign workspace in Obsidian](/assets/Forgotten-Realms-workspace-in-Obsidian.png)

At the beginning of a game, I'll create a new session page in the last pane, enter into it, and then stay in the workspace for the rest of the game. I have my character's stats sheet handy (which I need to do manually since I haven't found a D&D Beyond-like service for 4e) and all the powers and abilities I need to refer to.

### Session template

I love Obsidian templates! I use templates for things like inserting an HP tracker with all my party's names, their max HP, healing surges (4e); a defense table to keep track of a creature's defenses (again, 4e); and campaign-specific session log formats.

At the beginning of the game, I'll create a new page in the Session List, click into it, and insert a session log template (I have this hotkeyed to CMD+`;`). Here's what a fresh one looks like, in Edit mode:

![My session template, newly inserted](/assets/session-template-fresh.png)

I add metadata to every session so that I can query it later using the excellent [Obsidian Dataview plugin](https://github.com/blacksmithgu/obsidian-dataview), though I do this more often for the campaign I DM rather than the one I play in.

We usually do a recap at the beginning of the game, so I jump into the `Recap of the last session` section and embed the summary from the previous session using ` ![](/assets/86_20210717 Day 16 Hunting the Ice Phase Spider#^summary)`, which pulls in the section marked with `^summary` from the last session. That embeds just that portion of the last session in the current session, like this:

![Session recap using block embed](/assets/Recap.png)

This helps me get back up to speed quickly instead of doing the usual "Where were we again?" that takes up time. 

### HP table

My character is a multiclassed healer, so it's important for me to know who needs heals or other buffs. I keep track of this separately, and it helps out my DM as well because it's easy to miss something in the excitement of a battle. I do include the HP table in my workspace, in Preview mode, but here's what it looks like in Edit mode: 

![A table of the party's HP, surges, and conditions](/assets/HP-table.png)

Tables in Markdown can be a pain, but the [Advanced Tables plugin](https://github.com/tgrosinger/advanced-tables-obsidian) goes a long way towards making this easier by adding some nice features like tabbing to the next cell, adding commands for inserting and deleting a column or row, and just automatically formatting a table so that it's not a jumble of lines. I also heavily use this plugin for my characters stats and skills, both of which I keep in tables.

### Keeping track of fights

When a fight breaks out, I insert an intiative template, which is just a list of all the characters in the party:

```markdown
Initiative!
- Ka'ira
- Maestro
- Xio
- Eraithe
- Keren
```

This makes it easier to add the initiative value rolled, as well as that of any other baddies we're fighting. I use the [Outliner plugin](https://github.com/vslinko/obsidian-outliner) to be able to easily move people on the list up or down as needed without having to copy or paste. I have the shortcuts set to CMD+SHIFT+UP and CMD+SHIFT+DOWN so I don't even need to use my mouse.

I also have a template for Defenses. D&D 4th Edition has four different kinds of defenses, and since my character's powers target a few of them, I keep track of the defenses of each monster. Here's what that template looks like, in Edit mode:

```markdown
| Defense               | Value |
| --------------------- | ----- |
| [[Reflex Defense]]    |       |
| [[Fortitude Defense]] |       |
| [[Will Defense]]      |       |
| [[Armor Class]]       |       |
```

You'll notice that I also link to the pages I have for each defense type, in case I need to remind myself which stat a defense is comprised of.

### Character powers

Like many, I have migrated from playing games on a literal tabletop to doing it virtually. These days, I play 100% online, using a bunch of different tools. For the most part, though, I still prefer to roll actual dice. There's just something satisfying about the feel of a die in my hand. Since I switched to Obsidian, though, I have looked into virtual dice. On the off chance I don't have any dice (ha) or all my dice have betrayed me (much more likely), I use the [Dice Roller plugin](https://github.com/valentine195/obsidian-dice-roller). It turns 

```markdown
`dice: 1d20+7`
```

into a random die roll. Here it is when incorporated into my character's list of powers:

![My character's powers page](/assets/powers-sample.png)

Sometimes, when I'm feeling superstitious about my dice, I'll switch to using this dice roller "just to be safe". It has other cool features too, which I'll cover more in detail in the Dungeon Master's edition of this article.

### Search, linked, unlinked mentions

Frequently, something comes up in a game that I'm *sure* we've heard of before, but I can't quite remember where or when. Actually, sometimes something comes up that I'm quite sure we've *never* heard of before, but it turns out we have. Luckily, Obsidian is quick to tell me that using the linked/unlinked mentions and the search features.

Here are the mentions in my note for the word "Netheril":

![Linked mentioned for the word Netheril](/assets/Netheril-mentions.png)

Unlinked mentions show up too, in case the word came up somewhere and I didn't think to specifically create a page on it.

On monster pages, mentions remind me when we fought them last, and any tips for fighting them. It can be handy when one of the other players has forgotten something that happened to them, too. If I want to remember how Ka'ira got her festering wound, I can type it into the Obsidian search bar:

![A search in Obsidian for "festering wound"](/assets/festering-wound.png)

and be able to confidently say that Ka'ira got her last festering wound on session 68, in the Blue Crystal Fortress that we now know to be the Twisted Fane, while fighting aberrations.

## After a game

I think I might use Obsidian even more between games than during the game, because after the game is when I process everything my character learned.

### Session summary

Immediately after the game is when I create a short session summary. I like to do this when the session is still fresh in my mind. Then, I add `^summary` at the end of the paragraph to identify it and to be able to pull it into the next session's recap. Block references and block embeds are some of my most frequently used Obsidian features.

### Creating new pages

I then create new pages for any people, places, magical items, or events that we encountered. I like to use a standard frontmatter:

```
---
type: 
location: [Neverwinter]
world: "Forgotten Realms"
campaign: "Order of the Wandering Mind"
date: 2021-06-23
---
```

Here's an example of the page for an NPC:

![An NPC page in my campaign](/assets/npc-sample.png)

If my DM has given us character art, I include it in the page.

And here's an example of a page for a location:

![Location page: Twisted Fane](/assets/twisted-fane-location-example.png)

For this page, I used a plugin called [Obsidian Leaflet](https://github.com/valentine195/obsidian-leaflet-plugin), which lets me add maps to my notes! In this case, my DM gave us this map of the structure as a guide, but during combats we didn't use a map. To keep myself oriented between games, I added red pawprint pins where we had spotted or fought monsters, green thumbtacks to mark where we'd ended sessions, and green markers where we had spotted allies. I also like to add links to monsters or sessions on the pins/markers so that I can jump to those pages quickly if I need to.

### History

To keep historical events straight in my head, especially since we tend to discover them out of sequence, I use the [Obsidian Timelines plugin](https://github.com/Darakah/obsidian-timelines), which lets me create pages like this:

![Obsidian Timeline in my game](/assets/obsidian-timeline-for-dnd.png)

by using this code in the timeline page:

```markdown
```timeline
fr
\```
```
(without the backtick) and this for every event that I want to include:

```markdown
---
date: [2021-06-23]
tags: [timeline, fr]
---
<span 
	  class='ob-timelines' 
	  data-date='1443-00' 
	  data-title='Xionerys is born' 
	  data-class='orange' 
          data-img = 'assets/xionerys.jpg' 
	  data-type='range' 
	  data-end='1443-00'> 
	Xionerys is born in Calimshan.
</span>

```

Using this method, I've been able to call out discrepancies in what two different NPCs told us and figure out that one was lying-- or at least misinformed.

### Replace all

When I inevitably get a fantasy name wrong, having pages as flat .md files is great because I can do a find and replace on ALL mentions of a certain NPC name/place I've misspelled (those fantasy names!). I do this with my usual code/text editor, VSCode, just because I usually already have it up, but you can do it using terminal commands. If it's just the name of a page, updating the spelling in Obsidian changes it everywhere else it's linked to as well, which is useful.

### Updating open loops

To finish processing the last session, I update Open Loops: I add new points or update existing points in Quests and Questions, and then add tasks to Agenda that I want to do in the next session. I find that it's best to do it after a game because it's a week, sometimes more, between games and there's a high likelihood I'll have forgotten what I want to do by then!

### Publish

I also publish my D&D notes, just for transparency. My DM has joked that he looks in there sometimes when he's forgotten something. Even if he doesn't, I enjoy having my notes so easily accessible. I often navigate there myself when I have a spare moment, remembering old sessions and thinking about some loose threads. If you're interested, [here they are](https://notes.nicolevanderhoeven.com/ForgottenRealms/World)! Just be warned that the plugins won't work in the web version, so sometimes you'll come across bits of code that didn't render. I also migrated these notes from Roam Research, and haven't gone back and updated all the older notes.

## Conclusion

Since I've switched to Obsidian, it's been an indispensable part of my workflow for D&D. Without it, I'd be just another murder hobo with no notes. And no DM wants that!