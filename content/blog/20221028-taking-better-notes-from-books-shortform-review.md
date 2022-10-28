---
title: "Taking Better Notes From Books: Shortform-Readwise-Obsidian"
date: 2022-10-28T16:00:34+02:00
draft: false
tags: ['shortform', 'video', 'english', 'obsidian', 'blinkist', 'pkm', 'readwise']
---

{{< youtube JfL9iAEfSCg >}}

I've been using [Shortform](https://shortform.com/nicole) for over a year. I've written [some code](https://github.com/nicolevanderhoeven/shortform-to-readwise) for it and I've also written [a blog post](https://nicolevanderhoeven.com/blog/20210815-shortform-to-readwise/) about it. It's an essential part of my workflow for taking better notes from books, particularly in conjunction with [Readwise](https://readwise.io/nicole) and my current note-taking tool of choice, [Obsidian](https://obsidian.md/). Here's what you need to know!

## What is Shortform?

Shortform is a service that creates book summaries out of popular books, but it's also so much more than that! They're like Netflix but for books, if you can imagine that. The summaries that Shortform gives you are not just your typical high school level summaries of a book report that we used to do when we were younger.

Sound familiar?

## What makes Shortform different?

Here are things that differentiate Shortform from other book summary services.

### Researched commentary

Shortform has really thoughtful and nuanced commentary that place it firmly head and shoulders above other services.

Here's a screenshot of some Shortform commentary from the book [Why We Sleep](https://amzn.to/3gO0gmP), taken on the Shortform mobile app.

![Screenshot of Shortform commentary from the book "Why We Sleep"](/assets/shortform-why-we-sleep.jpg)

The highlighted section is a Shortform note-- additional commentary that the Shortform team added. In this case, they are fact-checking the author, citing [sources](https://www.sleep.pitt.edu/wp-content/uploads/2020/03/The-AASM-Manual-for-Scoring-of-Sleep-and-Associated-Events-2007-.pdf) that prove a statement the author made to be false. 

When I was reading this book, I didn't really think about questioning those claims. But Shortform thoroughly goes over every claim that Walker, the author, made in thsi book. 

Reading with Shortform is like having somebody else read a book with you-- a more critical and more well-informed someone who has the time to fact-check statements. It's a bit like having your own personal book club.

#### Shortform vs. Blinkist

Another service in this vein that I've used is [Blinkist](https://blinkist.com/). Let's look at the same book in Shortform and Blinkist to figure out why I like Shortform so much better. 

This is what the Blinkist summary for the book [Indistractable](https://amzn.to/3W8rFQH) looks like.

![Screenshot of Blinkist summary of Indistractable](/assets/blinkist-indistractable-summary.jpg)

Blinkist is based on the idea that every book can be distilled into these *blinks*: very short summaries of every idea. For this book it has eight. Each of these blinks is a few paragraphs long. Here's what the first looks like.

![Screenshot of Blinkist's Indistractable blink](/assets/blinkist-indistractable-first-section.jpg)

A blink is a straight summary. There's no commentary. There's no research or anything like that. It seems like the whole focus of this is to be able to distill exactly what the author has said and let other people do the work of trying to figure out for themselves whether something is true or not. There's really not much more than just these blinks. 

In contrast, if we look at the one on Shortform, this is the same book and it also has like a one page summary like Blinkist did. 

![Screenshot of Shortform summary of Indistractable](/assets/shortform-indistractable-summary.jpg)

But then it also has a full book guide, which goes through every single chapter or part and adds more detail into it. 

![Screenshot of Shorform's Indistractable first part](/assets/shortform-indistractable-first-section.jpg)

As you can see, Shortform takes a different approach: instead of just summarizing the book, they're truly trying to explain it in their own unique way, providing examples and making it more readable using bullet points.

### Action-oriented exercises

Shortform also has these exercises based on the things that the author has said in the book. These exercises are peppered throughout and between these chapters, and they really force you to put things into practice right away as soon as you learn them, which is another element of learning. 

![Screenshot of an exercise in Shortform's Indistractable summary](/assets/shortform-indistractable-exercises.jpg)

### Critical thinking: comparisons to other ideas

Shortform tries to examine ideas in the context of other books they've made summaries for. Here's an example of a Shortform note where Shortform suggests the summary of the book [How to Stop Worrying and Start Living](https://amzn.to/3NdqE5C). 

![Screenshot of Shortform note connecting Indistractable to another book](/assets/shortform-indistractable-comparison.jpeg)

Fans of the Zettelkasten method will be happy to see this, because Shortform often prompts me to consider the differences or similarities between ideas from different authors. It helps me see connections I might not have considered. Incidentally, I've also found many good books this way!

## How to use Shortform with Obsidian

The other thing that really sells it for me is the integration. Because I don't want that learning to stop in the Shortform app. You know me, and I want everything in Obsidian. And Shortform has an integration that Blinkist does not. 

I actually tried to solve this problem myself a year ago, because no integration existed. I [wrote a Python script](https://nicolevanderhoeven.com/blog/20210815-shortform-to-readwise/) that would take the Shortform highlights, because it has an API, and then call the Readwise API and kind of string them together. Now, that still works as far as I know, but that's not what I recommend anymore. I talked to the Readwise founders and suggested to them that Shortform was a great company to partner with. Not too long after that, they came out with [an awesome integration](https://readwise.io/changelog/shortform-import)! 

1. First, sign up to both [Shortform](https://readwise.io/nicole) and [Readwise](https://readwise.io/nicole). They both have free trials, so you don't have to commit to anything just yet.
2. Then, [click on this link to connect](https://readwise.io/welcome/sync#shortform) your Readwise account to Shortform.
3. (optional) If you use Obsidian like I do, [follow these instructions](https://nicolevanderhoeven.com/blog/20210810-readwise-to-obsidian-redux/) to install the Readwise Official plugin for Obsidian.

That's pretty much it!

From now on, here's how things will work:
- You make highlights on books on Shortform.
- Those highlights are sent to Readwise automatically.
- Through the Readwise official plugin, those highlights get synced into your Obsidian vault.

### The result: Shortform highlights in Obsidian

Here's what my Shortform highlights look like in Obsidian. Note that after setting this up, all I had to do was make highlights on Shortform-- it's quite low-touch after that.

![Shorform highlights synced to Obsidian vault via Readwise](/assets/obsidian-shortform-indistractable.png)

I tweaked the export settings in Readwise to set the format I want the note to have in Obsidian. You don't have to do this, but if you want to, you can change those settings [here](https://readwise.io/export/obsidian/preferences).

## My Shortform workflow for taking notes on books

This is pretty much how a lot of my book-buying and -reading goes:

- I start by browsing books on Shortform and read the one-page summaries.
- If I find one I like, I buy the book on Kindle. 
- I make highlights on the Kindle version. (Those are synced to Obsidian too!)
- If I really like the book, I flip back to the Shortform detailed chapter summaries as I finish each chapter, because they provide more context. I make highlights and notes from Shortform here sometimes.
- Sometimes I do the Shortform exercises too.
- After I finish the book, I go back to the Shortform summary and make more highlights/notes.
- After I've read my fill of both the Shortform summary and the book itself, I go back to Obsidian and write my own notes that combine what I've learned.

If that sounds like a lot, it is! But keep in mind that I don't do this for *every* book. At every step of the way, Shortform helps me filter out books that I don't want to read, or don't want to finish. 

Shortform definitely saves me money: it costs less than a book a month and it stops me from reading more than one book a month. From that perspective, it's already worth it. 

But more than that, the thoughtfulness of the summaries and the research that goes into those commentaries save me more than just money: *they save me time*. And that's really what I keep coming back for. 


## Related

- [The easiest way to sync Kindle highlights to Obsidian - Readwise to Obsidian](/blog/20210810-readwise-to-obsidian-redux/)
- [How to process notes in Obsidian with Readwise](/blog/20220323-how-to-process-notes-in-obsidian-with-readwise/)
- [I can finally tell you about Readwise Reader](/blog/20220907-what-is-readwise-reader/)
- [How to take notes from a book with Obsidian](/blog/20220902-how-to-take-notes-from-a-book-with-obsidian/)
- [Use it or lose it: what to do with all those notes](/blog/20220519-use-it-or-lose-it/)


*Some of the links on this page are affiliate links. Click [here](https://nicolevanderhoeven.com/ethics/) to check out my ethics statement and see how I decide what to promote in this way.*