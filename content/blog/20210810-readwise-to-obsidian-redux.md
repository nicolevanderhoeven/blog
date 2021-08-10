---
title: "The easiest way to sync Kindle highlights to Obsidian: Readwise to Obsidian Redux"
date: 2021-08-10T19:50:40+02:00
draft: false
tags: ['english', 'text', 'obsidian', 'zettelkasten', 'taking notes', 'readwise']
---

{{< rawhtml >}}
<meta property=“og:image” content="/assets/readwise-official-plugin.png" />
<meta property=”og:image:width” content=”1200″ />
<meta property=”og:image:height” content=”628″ />
{{< /rawhtml >}}

![Readwise to Obsidian workflow](/assets/readwise-official-plugin.png)

Almost exactly six months ago, I [wrote a blog post](https://nicolevanderhoeven.com/blog/20210206-readwise-to-obsidian/) detailing my workflow for processing content. Specifically, I wrote about how I used a python script to take my highlights from Instapaper, Kindle, Twitter, and Airr and automatically put them into Obsidian.

That method worked, and you can read the original article in the link above. However, today, Readwise announced that they now have [an official Obsidian community plugin](https://help.readwise.io/article/125-how-does-the-readwise-to-obsidian-export-integration-work), and I disabled my trusty old python script for good.

You see, although my old script worked, there were quirks-- not the least of which was that making changes to it meant programming in Python. I'm not a developer, so while I made do, it was never a painless experience. I also ran into issues with time zones and invalid characters being used in titles. So I'm thrilled to have something significantly better from Readwise itself! Here's how to get started.

## Install the Obsidian plugin.

In your Obsidian vault, go to Settings > Community plugins. You'll need to turn Safe mode off for community plugins if you haven't already.

Then, click Browse and search for Readwise Official.

![Screenshot of the Readwise Official plugin within Obsidian](/assets/readwise-official.png)

Install it, and then enable it.

## Connect your Readwise account to the Obsidian plugin

Head back to the Settings menu and scroll down to the "Plugin Options" section, and then click Readwise Official.

![Screenshot of the initial screen of the Readwise Official plugin](/assets/readwise-official-connect.png)

Click connect as highlighted in orange above, and a browser window will open, showing the [Obsidian Export](https://readwise.io/export/obsidian/preferences) options. You'll need to sign into your Readwise account if you haven't already.

![Obsidian export page](/assets/obsidian-export.png)

At this point, your Readwise account will have been connected to the Readwise Official plugin, but you won't have triggered any syncs yet. If you don't want to change any of the configuration settings, you can then skip ahead to triggering the sync on Obsidian, but let's run through the options anyway.

## Modifying configuration settings

On the Obsidian Exports page, you'll be presented with a few options.

### Group Files in Category Folders

By default, this will be enabled. When enabled, Readwise will put your highlights in different folders depending on its source. For example, Kindle highlights will appear in the folder `Books`. Disabling this option means all new notes will be created in the directory specified in the Obsidian plugin settings, which we'll cover later. I left this enabled in case I read a book that has the same name as a blog post about the book, for example.

### Use Custom Formatting

Custom formatting is disabled by default, and lets you choose how the final note looks. Here are the things you can change in this section
- Page title
- Page metadata
- Highlights header
- Highlight
- YAML front matter
- Sync notification

I did make some changes in this section just to tweak how I want information to be displayed.

#### Page metadata

I don't see the need for Page metadata since this is what I use YAML front matter for, so I removed the matadata section and the document tags (I never use those either). So my Page metadata section looks like this:

```
{% if image_url -%}
![rw-book-cover]({{image_url}})

{% endif -%}
{% if url -%}
URL: {{url}}
{% endif -%}
```

#### Highlight

By default, highlights are entered in bullet-point form. That's fine when _I'm_ taking notes, but when I'm highlighting someone else's words, I like to be very careful to use blockquotes. I frequently do block searches in Obsidian, and I do NOT want to accidentally pass off a quote as something I said.

To this end, I added a `>` before each highlight and two newlines (carriage returns) at the end to delineate each highlight. That way, I can quote just one highlight at a time.

```
> {{ highlight_text }}{% if highlight_location and highlight_location_url %} ([{{highlight_location}}]({{highlight_location_url}})){% elif highlight_location %} ({{highlight_location}}){% endif %}{% if highlight_note %}
    - Note: {{ highlight_note }}{% endif %}


```

As you can see above, I also removed highlight tags, which I never use.

#### YAML front matter

Metadata has to be quite specific, so I added parameters I already use for other notes in this section. The `TVZ` is a tag I use that means "To Verzettelen", meaning pages that I need to process further. 

```
Title: {{full_title}}
Author: {{author}}
Tags: TVZ, readwise, {{category}}
date: {{date}}
```

#### Sync notification

As someone who has worked on a syncing plugin for Readwise to Obsidian, I know that things go wrong sometimes. Enabling this outputs a synchronization log to a note, which has come in handy MANY times in the past. _Has that book been synced, or did something go wrong?_ So I copied what the Readwise team suggested:

```
- [[{{date|date('Y-m-d')}}]] {{time}} — Synced {{num_highlights}} highlight{{num_highlights|pluralize}} from {{num_books}} document{{num_books|pluralize}}.
{% for book in books %}    - {{ book.num_highlights_added}} highlights from {{ book.title }}
{%endfor %}
```

### Select Items to be Exported

In this section, you can choose which books/podcasts/other content in Readwise you want to export. It is disabled by default. If you haven't synced Readwise to Obsidian before, and you just want to pull in everything, leave it disabled.

In my case, I have already synchronized everything using the plugin I mentioned, and didn't want to create another few hundred duplicate notes in my vault. So I enabled it and selected a few more recent books.

A weird thing about this Export settings page is that there is no saving-- it just automatically saves it. Just a note, because I was scrolling up and down that page looking for an indication that it had been saved before I realized it is done automatically.

## Initiate Sync from Obsidian

Head back to Obsidian and to the Readwise Official plugin options page. You should see a "Initiate Sync" button where the "Connect" one was before.

![Screenshot of Initiate Sync button](/assets/readwise-official-initiate.png)

That's a good sign - that means your Readwise account has been connected, and your configuration settings from the previous step will be fetched.

Before you click the button, note that the _Customize base folder_ option is set to `Readwise`. This is the directory that all your Readwise notes will be created. So if you enabled _Group Files in Category Folders_ earlier, your Kindle highlights will be saved in `Readwise/Books/booktitle.md`. You can change the base folder if you prefer, but I just kept the default.

Time to click the button!

![Screenshot of synced status from Readwise plugin](/assets/readwise-synced.png)

You'll see a few messages popping up on the upper right corner of your screen, and you'll also see a _Synced!_ message appear next to the button you just clicked.

## Verifying results

In your Obsidian vault, search for one of the items you synced. Here's what my note for Pat Flynn's _Superfans_ looks like:

![An example of Kindle highlights imported to Obsidian](/assets/readwise-obsidian-kindle.png)

Great! It looks exactly how I want it to look.

## Set up automatic sync

If you leave it there, the plugin will only sync when you tell it to, so you'd need to go into the plugin options each time. That's not particularly useful for me, because I want it to just happen.

If you feel similarly, head back into Plugin Options one more time and select your desired frequency in the _Configure resync frequency_ dropdown menu. I chose 1 hour, the minimum. I also enabled the automatic sync when Obsidian opens.

![Screenshot of auto sync options for Readwise Official plugin](/assets/readwise-official-auto-sync.png)

## Conclusion

I love this new plugin! It was very much needed, because existing options for accomplishing the same thing were flawed in some way, mainly because they were community-driven-- meaning the people who created these workarounds (myself included) were "just" users who had other jobs. I'm grateful that the Readwise team has acknowledged the popularity of Obsidian and taken on the maintenance burden. I've experimented with the plugin quite a bit and haven't found any major issues so far. It is a seamless way to get the best of the content I've consumed from various sources into one single source of truth: Obsidian. I highly recommend it to anyone looking to streamline content processing and creation processes.