---
title: "How to import Shortform highlights to Obsidian via Readwise"
date: 2021-08-16T21:40:16+02:00
draft: false
tags: ['english', 'text', 'obsidian', 'zettelkasten', 'taking notes', 'readwise', 'books', shortform]
---
{{< rawhtml >}}
<meta property=“og:image” content="/assets/20210816-shortform-to-readwise-title.png.png" />
<meta property=”og:image:width” content=”1200″ />
<meta property=”og:image:height” content=”628″ />
{{< /rawhtml >}}

![Shortform to Readwise hero photo](/assets/20210816-shortform-to-readwise-title.png)

I've always been dubious of those book summary apps. You know the ones-- they tend to have obnoxious ads that promise to help you "read 5 books a day" or learn the world's secrets in 15 minutes. Having tried a few of them, I've been disappointed with the quality of their summaries (or lack thereof). They attempt to distill the message of a 300+ page book into a handful of bullet points, which I've found neither accurate nor useful. Recently, though, I found myself happily subscribing to one, and here's why.

## What's Shortform and why is it awesome?

[Shortform](https://shortform.com) really took me aback because it isn't just a book summary. I should mention here that I'm not affiliated with Shortform and gain nothing by recommending them. I'm just a happy subscriber.

When I read their guide for the book _Why We Sleep_, I was pleasantly surprised to find that Shortform not only summarized it succinctly, but they also added intelligent counterarguments to the author's points. In some cases, when the author made a false claim, there were Shortform notes that linked to studies that showed _why_ the claim was false. In other cases, Shortform mentioned related concepts proposed in other books that strengthened the author's viewpoint. I found myself looking up their guides of books I'd already read, just because I was curious to see if I had missed anything. And I had!

In short, Shortform is the only book summary reader I've found that goes beyond summarizing and actually _adds value_ to the reading experience, _even if you've read the book._

They also have a one-page summary of the book AND a summary per chapter, so information is presented at different levels of detail. In my time with it, my most frequent workflow with it has involved reading the one-page summary of a book, buying it if it was interestering enough, reading the book, and then going back to Shortform to go read the chapter summaries. And both the one-page and detailed chapter summaries, including Shortform notes, can be highlighted!

Naturally I wanted to take it further than that. I already [sync my Kindle highlights to Obsidian](https://nicolevanderhoeven.com/blog/20210810-readwise-to-obsidian-redux) automatically and incrementally process them in Obsidian, so I wrote a script to have my Shortform highlights going to [Readwise](https://readwise.io) as well.

![Shortform highlights in my Obsidian vault](/assets/20210816-shortform-01.png)

_My Shortform highlights for the book Mindset, in my Obsidian vault._

The screenshot above shows the final result: highlights I made in the Shortform web or mobile app that have been synced to a page in my Obsidian vault. Here's how I did that.

## What you need

- A [Shortform](https://shortform.com) account.
- A [Readwise](https://readwise.io) account.
- A tool that Readwise can export to, such as [Obsidian](https://obsidian.md), [Roam Research](https://roamresearch.com), [Notion](https://notion.so), or [Evernote](https://evernote.com). You can also use their CSV and Markdown exports.
- A local installation of Python 3, which you can [download here](https://www.python.org/downloads/).

Obsidian is my Personal Knowledge Management tool of choice, and I use the [Readwise Official community plugin](https://nicolevanderhoeven.com/blog/20210810-readwise-to-obsidian-redux/) to get Readwise to send highlights to Obsidian. However, using Obsidian is not necessary as my script connects only Shortform to Readwise.

## The setup

Clone [my Shortform-to-Readwise repository on GitHub](https://github.com/nicolevanderhoeven/shortform-to-readwise) or download it to your computer.

### Enter your tokens

The file `variables.py` requires two tokens: one from your Shortform account and another from your Readwise account:

```python
# Your authorization token for Shortform
authToken = ''

# Your Readwise API token
# Retrieve this token from https://readwise.io/access_token
readwiseToken = ''
```

#### Getting your Shortform token

This is a little hacky, because Shortform doesn't expose an API token in their web app. So you'll need to log in to your Shortform account and open up DevTools in your browser. In Chrome, go to Options > More Tools > Developer Tools (or, on Mac, hit CMD+OPTION+I). Click on the Network panel.

You should now see Shortform on one side, and DevTools on another in the same browser window.

Then, go to [your Highlights page](https://www.shortform.com/app/highlights). Doing so will populate the Network panel with a bunch of requests that look like this:

![DevTools open in Chrome, showing requests from Shortform](/assets/20210816-shortform-02.png)

_DevTools open in Chrome, showing requests from Shortform._

Click on the request with the name `?sort=date`, highlighted above. That'll open another side panel that will show Headers. Scroll down to the section marked "Request Headers", and look for where it says `Authorization: Basic ` followed by a bunch of characters.

![Authorization headers for Shortform, in DevTools](/assets/20210816-shortform-03.png)

_Authorization headers for Shortform, in DevTools._

I've removed my personal authorization token from the screenshot above, but it's a long series of characters that comes after `Authorization: Basic `. Go ahead and right click on it and click Copy Value. Paste it into `variables.py` as the value for `authToken`, and then _remove `Basic ` (including the space after it) so that you're saving only everything that comes afterwards.

#### Getting your Readwise token

Thankfully, this one's a little easier. Go to [this page on Readwise](https://readwise.io/access_token) after logging in. Click "Get Token", click "Copy to clipboard", and then paste it into `variables.py`.

Save `variables.py`.

Note: Don't share either of these tokens with anyone else, as they will then be able to access your Shortform or Readwise accounts.

### Run the script

Open up your terminal, and `cd` into the `/shortform-to-readwise` repository. Then, run:

```bash
python3 getHighlights.py
```

It should finish in a few seconds (depending on how many Shortform highlights you have), and then you can verify that it worked by going to [your Readwise library](https://readwise.io/books).

![Shortform exports showing up in your Readwise library](/assets/20210816-shortform-04.png)

_Shortform exports showing up in your Readwise library._

You should see books that have the `Shortform-` prefix. If you do, then you're done! If you've got your Readwise account set up to push your highlights elsewhere (such as Obsidian), then you're all set!

In case you're wondering why I added the `Shortform-` prefix, it's because I often read the Shortform guide, and then read the book itself. Rather than end up in a sticky situation where the Shortform guide highlights might override the actual book highlights, I titled it differently so that I get two pages for the two sets of highlights.

## What about running the script regularly?

The whole point of this, at least for me, was to set it up so that I've got highlights going to Obsidian _automatically_, without needing my intervention. What I did was to use `crontab` on macOS to run the script every 30 minutes, but you can set up your own schedule.

### Give cron full system access

Cron needs to have the right permissions to run scripts on your behalf, so you may have to go to System Preferences > Security & Privacy > Privacy > Full Disk Access on your laptop and add `/usr/bin/cron` to the "allowed" list.

### Find the path for your python3 installation

In your terminal, run:

```bash
which python3
```

This will give you a path. For me, it was `/Library/Frameworks/Python.framework/Versions/3.9/bin/python3`. Copy this.

### Open crontab

Then, from your terminal, run the command `env EDITOR=nano crontab -e` to open up a list of cronjobs. If you don't have any other jobs, this will be blank.

### Set a schedule

Add a line to crontab for the schedule you want to create. This line has to be in the format

```shell
* * * * * command
```

where the five asterisks correspond to:

- minute
- hour
- day of the month
- month
- day of the week

In my case, I wanted it to run every 30 minutes, so here's what my schedule looks like:

```bash
*/30 * * * * /Library/Frameworks/Python.framework/Versions/3.9/bin/python3 /Users/nic/python/shortform-to-readwise/gethighlights.py
```

Make sure you change `/Users/nic/python/` to the path where you put the repository and your python3 path instead of `/Library/Frameworks/Python.framework/Versions/3.9/bin/python3`. Now exit out of it and save it (CTRL+X, and yes). The Python script should automatically run every 30 minutes.

## That's it!

I consume a lot of content daily, but without systems in place to capture insights from that content and process it, it all just gets forgotten eventually. That's why I love services like Shortform and Readwise-- they let me get what I've read/watched/heard out of my head and into Obsidian, where I can review them more critically and truly learn the important parts.

Both are paid services (which I paid for out of my own money), but I really think they're worth it.