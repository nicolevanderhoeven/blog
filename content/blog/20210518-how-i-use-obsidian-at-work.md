---
title: "How I Use Obsidian at Work"
date: 2021-05-18T22:33:18+02:00
draft: false
tags: ['english', 'obsidian', 'zettelkasten', 'text', 'k6']
---
Note-taking and personal knowledge management get talked about in academic circles, by both students and teachers. But there's not much said about its use outside of the academe.

![Obsidian for work](/assets/graphview-transparent.png)

I'll admit, due to my job description, I may be in a better position than most to take advantage of note-taking in a professional context. My background is in software performance testing. My job for several years has been to make sure that applications are prepared to withstand traffic from many users accessing it, usually by writing code to simulate that traffic before it's released to real users. Currently, though, I'm a Developer Advocate at [k6.io](https://k6.io), which means a significant part of my job now is sharing with people what I've learned.

I consider myself a knowledge worker: a significant part of my job depends on how quickly I learn new technologies _and_ how clearly I can impart what I've learned to others. I'd argue, though, that most people who work in a field as fast-moving as tech are knowledge workers too. It's naive to think we won't one day forget some skills we've learned, even if we were using them daily at one point. Yet nobody talks about note-taking.

Recently, my note-taking and personal knowledge management tool of choice has been [Obsidian.md](https://obsidian.md). I have no affiliation with the Obsidian team, and in fact I'm an investor of [a competing product](https://roamresearch.com). Here are some ways I use Obsidian at work that might help you understand why Obsidian is my daily driver.

## My setup

I have multiple Obsidian vaults, and each of them is a version-controlled [Git](https://git-scm.com/) repository, hosted on [GitHub](https://github.com). I keep my main Obsidian vault in a [Dropbox](https://dropbox.com) for extra version control and as a backup. Just for overkill, I also use [Obsidian Sync](https://obsidian.md/sync) as another backup and as the easiest way to get access to my Obsidian vault on my iPad Pro and my Android mobile.

I use [Obsidian Publish](https://obsidian.md/publish) to make some of my notes [publicly available](https://notes.nicolevanderhoeven.com) on a custom domain directly from my vault, as an experiment in learning in public that's gone pretty well so far.

This setup isn't free. All up, I'm giving Obsidian about US $16 a month. However, I want to point out that Obsidian itself is free for personal use, and if mobile access, cloud sync, and publishing your notes online aren't important to you, you can really go a long way with using it for free.

## Processing information

Remaining relevant in tech pretty much requires that you learn a lot, learn quickly, and enjoy the hell out of it. Luckily, Obsidian is pretty great at this.

### Consume and collect

I consume a lot of content, and in different formats: articles, books, videos, presentations, podcasts are all great sources of free education. I initially capture my notes on them in different ways, but they all lead back to using [Readwise](https://readwise.io/), which I use as a collector and sorter of all these notes. Then, I import data from Readwise to Obsidian using a process I describe in more detail [here](https://nicolevanderhoeven.com/blog/20210206-readwise-to-obsidian/). 

For now, suffice it to say that all these notes and highlights end up in Obsidian for processing. [Here's an example of my notes during a presentation](https://notes.nicolevanderhoeven.com/Presentation/In+the+kitchen+-+a+sprinkle+of+fire+and+chaos) (called _In the kitchen - a sprinkle of fire and chaos_ by [Ana Medina](https://www.anammedina.com/), about chaos engineering).

When trying to learn something, many people stop at this phase. They've read the thing, they've highlighted passages from the thing, and now they think they've learned the thing. That hasn't been my experience, because I forget many things I consume shallowly.

### Process iteratively

Then, I process notes iteratively, first restating things into my own words and then creating my own notes about concepts I've learned. Each time I do that, I try to identify key concepts and create backlinks for them, which in Obsidian just means typing `[[Chaos engineering]]`, with a topic between double brackets. If I click on that new link, it creates  a page for it. Over time, I end up with a page [like this one on Chaos Engineering](https://notes.nicolevanderhoeven.com/Chaos+Engineering) that is a consolidation of what I've learned.

Interestingly, if I go to the Chaos Engineering page, I can also see all the instances I've linked to it from other notes:

![Linked mentions in Obsidian](/assets/linked-mentions.png)

What if I didn't have the foresight to link to Chaos Engineering from an article I read? Obsidian also tracks _unlinked_ mentions as well. I can see all the times I've used the words "chaos engineering" in other notes, even if I haven't created formal links using `[[Chaos engineering]]`.

Over time, things I'm interested in start to emerge this way, and topics grow deeper and more detailed, with branches of pages spinning off from it.

### Situate and solidify

Then, I try to think about where this new piece of knowledge fits into the hierarchy of things I'm interested in. This is less about trying to classify the world and more about putting it somewhere on _my personal_ map of interests so that I'm more likely to use that knowledge later. For me, chaos engineering fit into my page on [Nonfunctional testing](https://notes.nicolevanderhoeven.com/Nonfunctional+testing). Doing so helps me pit it against other things I've classified as forms of nonfunctional testing and think critically about whether it belongs there, or whether other things I already know contradict it in some way. Sometimes I'll make notes about my reasoning for classification, such as [this note on why I think chaos engineering is a testing discipline](https://notes.nicolevanderhoeven.com/Chaos+engineering+is+a+testing+discipline).

None of this is set in stone. I'm always changing notes around as I learn more things that change my mind. For example, I'm considering merging my nonfunctional testing and functional testing pages after a conversation where someone questioned whether it wasn't a misnomer to call application performance "nonfunctional". The point is to create a living, breathing second brain that helps me make connections between concepts and remember what I've learned.

Obsidian's built-in graph view illustrates this point nicely:

![Built-in graph view](/assets/graph_view-20210518.png)

This is my main Obsidian vault as of the time of this writing - all 5443 notes of it. The graph view plots every note and the connections between notes, so I've ended up with a slick visual representation of what I've been thinking and writing about. The graph view is actually _functional_, too-- I can assign colors to nodes based on the directory they're in, their tags, words they can contain, and a lot of other criteria. Because each node is sized according to how many links lead to it, this view makes it easy to see clusters in things I've thought or written about.

### Publish

One of the advantages of Obsidian over something like Notion or Roam Research is how easy it is to publish notes from it.

#### Obsidian Publish (paid)

There's the paid Publish service, which I've subscribed to for US $8 a month. After [setting it up to publish on my own domain](https://notes.nicolevanderhoeven.com/Using+a+custom+domain+with+Obsidian+Publish) rather than the default at `publish.obsidian.md`, going from a note to a published post is as easy as clicking the Publish icon, selecting the notes to add, delete, or modify, and then selecting Publish.

![Dialog for Obsidian Publish](/assets/publish-dialog.png)

#### Open folder as vault

If you don't want to pay for Publish, Obsidian still saves all files locally in Markdown (`.md`) format. This is the same format that many static site generators take for content. This site that you're reading this on is generated using [Hugo](https://gohugo.io/), so everything written here is kept as a Markdown file before it's turned into HTML. Since an "Obsidian vault" is just a folder with Markdown files, I can just open the directory containing the files for my site and write blog posts in Obsidian with no noticeable difference.

At work, we happen to store our main [product documentation](https://k6.io/docs/) as Markdown files in a [GitHub repo](https://github.com/k6io/docs), which make it perfect for opening in Obsidian as well. I prefer to write documentation in Obsidian over VSCode for a few reasons:
- I can install plugins, like [Advanced Tables](https://github.com/tgrosinger/advanced-tables-obsidian) to make Markdown tables easier to deal with, create templates to standardize the format of notes you make often, see an outline of what you're writing based on Markdown headings.

![See an outline of your current note](/assets/outlines-obsidian.png)
_Outline core plugin for Obsidian_

- When I want to link to another page, it's easier to just hit CMD + O to search through existing notes instead of finding it on GitHub.
- I can choose an Obsidian theme that matches the theme of the published site. [This "Gitsidian" theme](https://github.com/ishgunacar/gitsidian) has an Edit view in dark mode (my preference) but a rendered Preview mode that looks more like GitHub's Markdown format, so I can see what it will actually look like for users.

![Gitsidian theme preview for Obsidian](https://github.com/ishgunacar/gitsidian/raw/master/showcase.png)

When I'm done, I can still jump to my terminal and push my change to GitHub as normal.

#### Obsidian URIs

Another cool feature is the fact that every note in Obsidian has what's called an Obsidian URI - it's a link that opens up a note within a specified vault. The URI looks like this:

`obsidian://open?vault=docs&file=src%2Fdata%2Fmarkdown%2Fdocs%2F03%20cloud%2F02%20Analyzing%20Results%2F02%20Performance%20Insights`

Adding it and publishing that to internal documentation means I can switch easily from browsing on GitHub to modifying the same page in Obsidian on my local machine, which is a great little bonus.

#### Embedding published work

After publishing, I use iframes in Obsidian to update my notes with the final result. Here's a video on YouTube about chaos engineering that my colleague [Simme](https://simme.dev) and I planned out collaboratively on Obsidian, embedded into Obsidian:

![Embedding a video in an iframe](/assets/embedded-youtube-iframe.png)

The video plays in Obsidian with all the same controls. The Obsidian desktop app is an Electron app, so it behaves just like a normal browser for playing back the video. To embed the video, I just used the Share > Embed code on YouTube and pasted it straight into Obsidian:

```html
<iframe width="560" height="315" src="https://www.youtube.com/embed/gVwJZPo30rk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

## Meetings

I take meeting notes to help me focus on the meeting, and I create templates for recurring meetings. Templates let you define the format of a note. Once created, you can insert templates into notes with a keyboard shortcut (I set mine to `CMD + ;`). Here's an example of what that looks like, with the template on the left and the inserted template on the right:

![Template (left) and inserted template in a new note (right) in Obsidian](/assets/obsidian-meeting-templates.png)
_Template (left) and inserted template in a new note (right) in Obsidian_

You may notice that the frontmatter includes `{{date}}` in the template, which gets automatically converted to today's date when the template is used.

If anyone asks for a copy of my meeting notes, that's no problem-- any note can be exported to Obsidian by clicking on Options > Export to PDF.

![Options for exporting a note to a PDF in Obsidian](/assets/obsidian-pdf-export.png)
_Options for exporting a note to a PDF in Obsidian_

I don't want to actually publish any real meeting notes, so here's what my note on the chaos engineering process looks like [as a PDF](https://nicolevanderhoeven.com/assets/The%20process%20of%20chaos%20engineering.pdf), straight from Obsidian. And here's what it looks like [as a note](https://notes.nicolevanderhoeven.com/The+process+of+chaos+engineering).

## Presentations

### The easier way

Obsidian has a presentation mode! It's basic, but it's functional. You can create a presentation really easily by adding `---` between paragraphs of text to delineate slides, right within a note. Here's what that looks like:

![Creating a presentation from Markdown notes](/assets/obsidian-slides-markdown.png)

Then you can click Options > Start presentation, and you get something like this:

![An Obsidian presentation](/assets/obsidian-slides.png)

A little plain, but given the minimal amount of effort to "convert" a note into a presentation, it's pretty awesome.

### The harder way

Sometimes the basic slides just don't cut it, and it can be handy to be able to publish the slides in presentation format (since publishing them straight from Obsidian Publish would only publish the Markdown version). For those cases, I've figured out a way to do just that while still keeping my slides as Markdown files in my vault. [Here's a whole post on how to do that](https://nicolevanderhoeven.com/blog/20210302-presentation-slides-as-code/). This is definitely more complicated, but at the end of it, you get a nice page [like this](https://slides.nicolevanderhoeven.com/2021-load-tests-as-code/#/) to send to attendees after a presentation. (_Tip: Hit `s` to see the speaker notes while on those slides._)

![A sample custom slide using revealJS with Obsidian](/assets/20210302-reveal-hugo-sample.png)

## Task management

I use a few community plugins to keep track of things I want to.

### Kanban

The [Kanban plugin](https://github.com/mgmeyers/obsidian-kanban) turns Markdown task lists into full-on Kanban boards.

![Kanban plugin in action](/assets/obsidian-kanban.png)

On the left is the markdown note, and the on the right is the rendered Kanban board. You can customize the titles of the lists that are there, and you can add due dates to each task.

### Calendar

The [Calendar plugin](https://github.com/liamcain/obsidian-calendar-plugin) is [Obsidian's most popular plugin](https://www.youtube.com/watch?v=fo6BKY2xR2w), and with good reason.

It lets me add a calendar on the sidebar:

![Obsidian calendar](/assets/obsidian-calendar.png)

I have the weekly notes option enabled, so clicking on the `W` column in the calendar takes me to a note that is automatically created for that week. I use it to keep track of weekly goals and to do a review at the end of the week.

Clicking on a date in the calendar takes me to the...

### Daily Note

The Daily Notes core plugin comes with Obsidian, but you have to enable it. Once enabled, clicking on a day in the calendar creates/takes you to that day's corresponding note. I use daily notes like a log or workbench for that day, with timestamped headings to help me remember later on what I did at what time. It's a loose way to do time management as well.

## Dataview

The [Dataview plugin](https://github.com/blacksmithgu/obsidian-dataview) is my favorite recent discovery, and it's changing the way I do frontmatter. This plugin brings something akin to SQL (albeit not as powerful) to Obsidian. It lets you query your notes based on some file-related metadata __as well as parameters you set in your frontmatter__.

For example, this query:

```dataview
table file.ctime as Date
from "Meeting"
where file.ctime >= date(today) -dur(1 month)
```

when rendered (i.e., viewed in Preview mode in Obsidian), returns a list of all my notes under the subfolder `Meeting` in the last month:

![Obsidian Dataview results as a table](/assets/obsidian-dataview-meetings.png)

This is huge! I'm still updating my notes with the appropriate frontmatter to make more use of this feature, but here are some use cases I can think of that would be handy at work:
- Find all customers with tag `annual` that I haven't spoken to in the last year.
- Find a load testing tool with feature `Slack_integration = true`.
- Find that woman I met at the Automation Test Guild conference by searching for `job = tester` and `tag = AutomationTestGuild`.
- Return all notes tagged `#plugin_ideas`.

And that's just the beginning!

## Collaboration

Obsidian itself does not (yet) have collaboration features. This is a bummer, but given how quickly they've delivered on features that the community has clamored for (block references and mobile apps come immediately to mind), I'm hopeful that they'll eventually improve in this area.

In the meantime, I've still found ways to work on the same vault with other people.

Remember how any folder of .md files can be opened as an Obsidian vault? Well, I'm technically collaborating with other people on that repo for work documentation, even if most people don't use Obsidian. All I had to do was add the `.obsidian` directory to the `.gitignore` file, and now, nobody really even needs to know I'm using Obsidian to view/edit the documentation. They just see me pushing to the repository as if I had used a text editor like VSCode.

I've also had the experience of collaborating with someone who also used Obsidian. Since we were working closely together on the same document, we opted to put our shared vault on Dropbox. Dropbox's main advantage over the Git solution is that Dropbox let us edit notes and see each other's edits in real time. If you're looking for an experience similar to Google Docs, this way got the closest to that. We did run into some quirks: if the Dropbox vault is also a Git repository, be aware that checking out a different branch will also change the contents of the directory for the other person.

## Conclusion

Note-taking and personal management aren't just for students and teachers; I think they're particularly useful in tech, where knowledge work is highly prized. I'm talking about Obsidian because that's my current tool of choice, but I think the tool you use is less important than the systems you put in place to help yourself learn and create.