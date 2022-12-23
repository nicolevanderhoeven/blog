---
title: "Readwise to Obsidian"
date: 2021-02-06T09:55:36+01:00
draft: false
tags: ['english', 'text', 'obsidian', 'taking notes', 'zettelkasten', 'roam research', 'python', 'readwise']
---
{{< rawhtml >}}
<meta property=“og:image” content="/assets/20210206-06-readwise-to-obsidian.png" />
<meta property=”og:image:width” content=”1200″ />
<meta property=”og:image:height” content=”628″ />
{{< /rawhtml >}}

![Readwise to Obsidian workflow](/assets/20210206-06-readwise-to-obsidian.png)

_August 10th, 2021: Readwise just released their own Obsidian plugin, [Readwise Official](https://help.readwise.io/article/125-how-does-the-readwise-to-obsidian-export-integration-work), which is available now! I now recommend [this method](https://nicolevanderhoeven.com/blog/20210810-readwise-to-obsidian-redux/) over the one outlined in this article._

I'm about 9 months into heavily using [Roam Research](https://roamresearch.com) as my primary note-taking, task management, capture-everything system, and for the most part, that's gone very well. [Obsidian](https://obsidian.md) is another excellent personal knowledge management (PKM) system, though, and I've been curious about it for almost as long as I've been using Roam. I've had it installed for a while, but I never really _seriously_ attempted to make the switch. Until now. I've decided to use Obsidian as my primary PKM and zettelkasten for the next month, to see if it's something I can switch to.

Why I'm considering switching from Roam to Obsidian is another post, probably one I'll write at the end of this experiment, when my thoughts and opinions are more solidified. For now, I want to address one of the things I struggled with when switching over: Readwise integration.

[Readwise](https://readwise.io/nicole) is an app that's all about importing notes and highlights you've made from all over the internet and exporting them all into a single format. Readwise supports far more import sources than I use, but here are the ones I've got hooked up to it:

- Instapaper (for highlights and notes on online articles)
- Amazon Kindle (for highlights on ebooks)
- Twitter (for interesting tweets)
- (Readwise) Web highlighter (for straight highlights off any webpage)
- Airr (for quotes and notes from audio podcasts)

Readwise collates my activity in all of these input sources and automatically sends them to my Roam Research account. Here's what that looks like when it gets pulled into my Daily Note:

![Tweet, podcast, and book notes pulled into Roam Research via Readwise](/assets/20210206-01-readwiseimportsinroam.png)

Readwise also pulls metadata into Roam, depending on the source. Here's what the page for the book "Ready Player Two" looks like in Roam:

![Ready Player Two book notes in Roam, imported via Readwise](/assets/20210206-02-readyplayertwo.png)

Readwise integration is an _essential_ feature for me in any PKM, because I can take notes wherever I'm consuming my content and just have it automagically appear in my notes, tagged and ready for processing. So it's absolutely something I need to have in my Obsidian workflow.

That's where things get tricky, because Readwise doesn't _have_ an Obsidian integration. 

![Readwise doesn't automatically export to Obsidian](/assets/20210206-03-readwise-export-options.png)

Source: [Readwise Exports](https://readwise.io/export)

The closest thing is the Markdown export, but that's not automatic. You can manually trigger an export, and then copy those exports over into your Obsidian vault, and thne make sure they're in the right format with the right tags. I knew I was never going to do that, so I found a way to automate it.

## readwise2directory

I discovered that Readwise has an API, and briefly thought about building my own integration. Happily, I found [this Python project on GitHub](https://github.com/nicrivard/readwise2directory) by [nicrivard](https://github.com/nicrivard), who had already done that! Why rebuild the wheel? His solution already did what I needed:

- It connects to Readwise via your Readwise access token
- Checks for new highlights or updated ones
- Exports the new/updated highlights to a local folder of your choosing (presumably your Obsidian vault)

It even pulls in highlight tags from Readwise, if you've created any (which I haven't).

I [forked the project here](https://github.com/nicolevanderhoeven/readwise2directory) to add just a few minor touches:

- Changed date format of imported notes
- Added a section to output the import date to a comment block (an [Obsidian Insider build feature](https://forum.obsidian.md/t/obsidian-release-v0-10-12-insider-build/12295)) rather than YAML frontmatter, so that the date would actually be linked and backlinked.
- Customized tags and filename for my use
- Sort imports into folders within my Obsidian vault depending on source (`Article/`, `Tweet/`, and so on).

This works out pretty well. Here's an example of an import from the podcast app [Airr](https://airr.io) into Obsidian, in Edit mode.

![readwise2directory import from Airr into Obsidian](/assets/20210206-04-airrtoobsidian.png)

It's placed within my `Podcast` folder inside my value, is tagged appropriately, and contains links to the source. Switching to Preview mode shows an imported cover photo and even a playable recorder for the part of the podcast that I snipped on Airr:

![Preview mode of imported Airr quote in Obsidian](/assets/20210206-05-airrinobsidian_preview.png)

So that works out well, except for one thing: firing off the script that does all this is still manual.

## Scheduling the script

Luckily, it's pretty easy to schedule a Python script to run at certain intervals. I'm on macOS, so I used a built-in utility called `cron`.

### Give cron full system access

Cron needs to have the right permissions to run scripts on my behalf, so I had to go to System Preferences > Security & Privacy > Privacy > Full Disk Access on my laptop and add `/usr/bin/cron` to the "allowed" list.

### Open crontab

Then, from my terminal, I ran the command `env EDITOR=nano crontab -e` to open up the list of cronjobs I had currently.

### Set a schedule

I added a line to crontab for the schedule I wanted to create. This line has to be in the format

```shell
* * * * * command
```

where the five asterisks correspond to:

- minute
- hour
- day of the month
- month
- day of the week

In my case, I wanted it to run every hour, so here's what my schedule looks like:

```shell

0 * * * * cd /Users/nic/git/readwise2directory/ && /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/nic/git/readwise2directory/readwise-GET.py >> /Users/nic/git/readwise2directory/readwiseGET.log

```

#### Python issues

I had some trouble getting cron to work until I realized it was because I had multiple versions of Python installed. I ran a `which python3` to find the path to the version I wanted to use and added that path to the command. I also had to `cd` to the project directory, for some reason.

While I was troubleshooting, I found it really useful to output to a log so I could see what had gone wrong.

Once I added the schedule as in the example above, though, it worked a treat!

## Conclusion

This solution did require some setup at the beginning, but doesn't need any maintenance once it's going. I'm pretty happy with it as it means I can keep taking notes on various places from anywhere, and it'll all be waiting for me in my Obsidian vault whenever I'm ready to sit down and process them into my system. Thanks to nicrivard for the repo that made it possible!

_Note: This post contains an affiliate link for [Readwise](https://readwise.io/nicole). Clicking on that link will give you a two-month trial of Readwise, double the usual amount, and they give me a small percentage if you sign up for a plan. Check out [My Ethics Statement](https://nicolevanderhoeven.com/ethics/) to see my standards for promotions._