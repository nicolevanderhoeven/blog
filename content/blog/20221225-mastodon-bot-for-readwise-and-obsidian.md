---
title: "Mastobot: a Mastodon Bot for Readwise and Obsidian"
date: 2022-12-25T00:31:28Z
draft: false
tags: ['mastodon', 'english', 'code', 'readwise', 'mastodon', 'nodejs', 'javascript', 'obsidian']
---

I've had a love affair with [Readwise](https://readwise.io/nicole) for a while, enough to write some code to extend it. I [wrote a Python script to save Readwise highlights to my Obsidian vault](/blog/20210206-readwise-to-obsidian/), switched to the [Readwise Official plugin](/blog/20210810-readwise-to-obsidian-redux/) when they released it, [wrote another script sending Shortform highlights to Readwise](https://nicolevanderhoeven.com/blog/20210815-shortform-to-readwise/), and then was happy when the two companies established an official integration thanks to me introducing them.

Maybe I should have learned to just be patient and wait for the awesome Readwise team to build integrations I want, but remembered I'm not that patient. This is about how I created a Mastodon bot to send Mastodon posts I like to my Readwise account, and, by extension, to my [Obsidian](https://obsidian.md/) vault.

You might say there's a pattern here.

## The problem

I've been dabbling in [Mastodon](https://joinmastodon.org/) for a while, but only recently got extremely involved with it when I decided to start and maintain a Mastodon server, [pkm.social](https://pkm.social), for the personal knowledge management community.

Readwise already has an awesome [Twitter integration](https://youtu.be/Rw1L5sxlnuU?t=400) that I really enjoyed. Basically, once you've set it up, sending any tweet to [@readwise](https://twitter.com/readwise) adds it to your Readwise account. This means that whenever someone says something actually meaningful or interesting on Twitter, I can make sure it gets sent to Readwise, and then from there to my notes in Obsidian.

I wanted the same setup for Mastodon.

## The result

First, the end result: I managed to get Mastodon posts I send to my bot to be sent to my Readwise account. Here are some early posts in the "Tweets" section of my Readwise Library:

![](/assets/mastodon-on-readwise.png)

And here are the resulting notes in Obsidian, also automatically synced and formatted:

![](/assets/mastodon-in-obsidian.png)

## The solution

Next, here's how to set it up.

### Pre-requisites

You'll need a few things to get started:
- A Mastodon account (I use and co-host [pkm.social](https://pkm.social) for free)
- A Readwise account ([Here's an affiliate link](https://readwise.io/nicole))
- Familiarity with GitHub, the command line, Node.js (although I'm not a Node.js developer, so you don't have to be, either)
- The willingness/ability to leave a Node.js script running on a server somewhere

### Setup

1. Clone [my Mastobot repository](https://github.com/nicolevanderhoeven/mastobot).
2. In your Mastodon account settings, go to the Development section for your Mastodon server (e.g. `https://pkm.social/settings/applications`) and click New Application.
3. Fill in the application name (this can be anything you want), leave everything else the same, and then click Save Changes.
4. Click on the application you just created, and note your client key, client secret, and access token. You'll need these later.
5. In this repository, copy the contents of `.env.sample` to a new file called `.env`.

It should look like this:
```javascript
ACCESS_TOKEN=
CLIENT_SECRET=
CLIENT_KEY=
READWISE_TOKEN=
DOMAIN=
```

6. Fill out the fields in `.env` with the information you just obtained from your Mastodon account.
7. For the `READWISE_TOKEN` field, enter your [Readwise access token](https://readwise.io/access_token).
8. For the `DOMAIN` field, enter your Mastodon server's domain (e.g. `https://pkm.social`).
9. Run `npm install` to install the dependencies.
10. Run `node bot.js` to start the bot.
11. In Mastodon, find a post you like and reply to it with `@accountname Your comment here.` Within a few minutes, the original post you replied to will be sent to your Readwise account as a highlight and your comment as a note.

## Limitations

This workflow is not without its limitations:
- You need to keep the script running somewhere to be able to use it. I considered using a polling approach, but decided I wanted to experiment with Mastodon't streaming API, which would also be more responsive, so I went with that.
- Right now, because the bot takes environment variables about _your_ particular setup, it's not as versatile as the official Twitter implementation. As it is, it's for one person's use only.
- It uses the "Tweets" category in Readwise, which is not ideal, but I can't really do anything about that until they give Mastodon its own category. This isn't really a big deal.
- Right now, the bot doesn't support images or other media embedded to posts.

I may address some of these issues, but for now, I'm just happy with the result. I fully expect that the Readwise team will eventually be able to flesh this out into a more robust integration, so I'm hesitant to spend too much more effort now that I've got it doing the minimum of what I wanted.

## Resources

If you're interested in doing this for yourself, here are some resources that might be useful:

- [Mastobot on GitHub](https://github.com/nicolevanderhoeven/mastobot)
- [Mastodon API client for NodeJS](https://github.com/vanita5/mastodon-api)
- [Mastodon official API](https://docs.joinmastodon.org/api/)
- Great video tutorial series by [The Coding Train](https://www.youtube.com/watch?v=sKSxBd56H70) on creating a Mastodon bot

## Related

- 📝 [Readwise to Obsidian (Redux)](/blog/20210810-readwise-to-obsidian-redux/)
- 🎥 [How to process notes in Obsidian - Readwise Official Obsidian plugin](/blog/20220323-how-to-process-notes-in-obsidian-with-readwise/)
- 🎥 [I can finally tell you about Readwise Reader](/blog/20220907-what-is-readwise-reader/)
- 📝🎥 [Taking better notes from books: Shortform-Readwise-Obsdian](/blog/20221028-taking-better-notes-from-books-shortform-review/)]
- 🎥 [Reading and taking notes on Kindle and Obsidian](/blog/20221216-reading-and-taking-notes-on-kindle-and-obsidian/)

_Note: I've included affiliate links for [Readwise](https://readwise.io/nicole) in this post, in accordance with my [Ethics Statement](https://nicolevanderhoeven.com/ethics/)._