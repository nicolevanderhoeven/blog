---
title: "New in Obsidian: Obsidian Callouts (available now)"
date: 2022-03-30T17:36:20+02:00
draft: false
tags: ['obsidian', 'personal knowledge management', 'pkm', 'video', 'english']
---

{{< youtube TqYQ0kA1yAo >}}

_Transcript:_

One thing I've learned from writing technical documentation in the last few years is that good writing is skimmable, at least in the digital age. So since I look at my notes in Obsidian the same way as I do a sort of personal documentation, I think that a lot of the same principles apply. 

Today I wanna talk about an early access feature that the Obsidian team rolled out two weeks ago, and it's called Callouts. So before I demonstrate this, I want to say that this is only available right now in the Insider Build version 0.14, but that build always gets pushed to the public, it's just a little bit ahead of the public release. So think of this as a bit of a sneak preview. _(Note: Obsidian callouts is [out now](https://help.obsidian.md/How+to/Use+callouts)!)_

## What about Obsidian Admonition? 

Now, before Obsidian Callouts was released, I was using something called Obsidian Admonition. So if we go here, I can bring up my Obsidian Admonition page, and it looked something like this. 

You would do three backticks. That's kind of the code block syntax. And you would do something like add note. Maybe you'd have a title here, like reminder, and then you'd have your note here. And because I have Live Preview turned on, if I enter out of this, it's going to look like this. So this is what Obsidian Admonition always looked like. 

So in general, the idea here is that to make your writing more skimmable, you have these kind of, well, callout boxes that highlight sections of your text and make sure that they address something that is about the notes that you're writing, kind of like meta notes, they're notes about your notes, but because they're visually distinguished from the rest of the text, it's a lot easier for you or for your readers to easily figure out whether something is important to read or only in specific situations. 

### Admonition/callout example

And that happens a lot in technical documentation, so it's no secret that I have used it a lot in sort of programming kind of notes. So if we go back to my vault here, let's look at [my note on g](https://notes.nicolevanderhoeven.com/g). g is a package manager for Go, the language. 

And here's a type of callout or admonition that I used. And this is kind of like this page tells you how to use, what g is and how to use it. But this note, this particular callout, is kind of like an aside. It's like, hey, just in case you get this error, here's how to troubleshoot it. And it's really cool that it's hidden by, it's collapsed by default. And you can just click on that, and then it says, oh, if you get the error, g not found, hey, maybe restart your shell session after installation. 

So that sort of callout really helps when you're trying to quickly skim a page. So programming is certainly one use for it, and another one is tutorials in general. You know, I have this a lot for my Obsidian stuff in case I need to say that this only works for Mac or this only works for windows or something like that. 

And I also use it a lot in my D&D games. As a Dungeon Master, I have different scenarios that I may not even need to go into depending on what my players decide to do. That is the perfect task for callouts or for admonitions. 

## Enter Obsidian Callouts

So I was using this admonitions format with a code block for, basically, since I learned about it. It is made by a TTRPG plugin developer called Jeremy Valentine, and he's made a lot of very popular ones, like the Dice Roller and the Initiative Tracker and Leaflet, and it just goes on and on. But I'm digressing. 

This plugin was apparently so good that even the Obsidian team realized that it really should be part of Obsidian, because a key part of Obsidian's functionality is documentation. 

So the big release is that they've now incorporated Admonitions-like functionality into core Obsidian, not a core plugin, so it's not something that you even have to install or enable, it just ships by default with Obsidian, which is really awesome. 

## How to use Obsidian Callouts

So let's look into how to use it. I'm going to go to my Obsidian Callouts page here. And the syntax is a little bit different from the admonitions one. Instead of the code blocks with the three backticks, this callouts functionality now uses blockquotes. 

```markdown
> [!info] Your title
> The contents of your note here
```

So you do a single blockquote like an arrow, and then you do brackets, and then an exclamation point. And then there are a bunch of different types, which we'll get into, but the most common one, I guess, is note. Then you would put your title here, and then you can put the rest of the note here. So this is now doing it as a blockquote. And if I exit out of that, you'll see that it has a nice icon of a kinda pencil or pen there, and it is visually distinguished from the rest of the note. 

## Types of Callouts

### note

Now, let's go into the types, 'cause there are a few of them. 

The first one I already showed you, this is a note. I put this within code blocks just to show you the syntax. And then this is what it looks like. Basically, this is the standard format of callouts, you just change whatever's here. And then you always put the title outside of the brackets, and then the content of the note below it. So this is what a note looks like. That's probably the most common. 

### abstract, summary, tldr

And then another one is abstract, summary, or TLDR. 

Now, all of these are the same, so like this is a TLDR, so I can actually edit it here as well. So here in this case, I was using TLDR, but if I do abstract, it's going to look, actually, it looks a little bit different now that I think about it I thought it was going to look the same, but it's also dependent on the theme that you're using. 

Yeah, so these three are actually different, even though they're semantically the same. Well, that's interesting. I just literally found that out right now as well. 

### info, todo

And there's info and todo. So this I believe is the todo. And if I go to info, it looks slightly different, just has a little eye here. 

This is what I use for descriptions. What we call it in TTRPG is what we call box text, when players enter a new scene and there's a part that you read out word for word, rather than improvising it. This is what I use for it. 

### tip, hint, important

Then you have tips, hint, tip, hint, or important. This one is a tip. 

Let's see what important looks like. All right. Yeah, all right. So there's some highlighting going on there as well, and it's marked by an asterisk. 

### success, check, done

There's success, check, done. I particularly like, I think it was done. It's kind of like the todo had a checkbox. This one actually has the check. 

### questions, help, faq

There's questions, help, or faq. 

### warning, caution, attention

There's warning, caution, or attention, which is what I use for errors or gotchas when you're programming or something things that you might fall into that I want to call out, because I did fall into it. 

### fail, failure, missing

And there's also fail, failure, and missing. So this is all bad stuff, essentially. 

### danger, error

There's danger, error. It looks like this with a little lightning symbol. 

### bug

There's bug, which I use quite a bit when I'm reporting bugs or documenting bugs, anyway. This example, which kind of looks like abstract, actually. 

### quote, cite

Quote, and cite, which is kind of a blockquote, except a little bit fancier. 

## Collapsing and expanding callouts

So as you can see, there are a lot of different types of callouts. And aside from all of those, you can also choose whether it's collapsed or expanded, and that's kind of the folding behavior that I showed you earlier. So let's just do that now as well. 

I'm going to say bug, and I'll say bug detected, let's say. And this time though, where just before the title, right outside of the parenthesis for the type that I'm using, I'm going to type a minus. And I'll put, this is a bug. And I get out of that. This is what it looks like. 

So it is very different from this one where it's just expanded by default, that's a default behavior, but if you add the minus there, that means that you're saying that this must be minimized or collapsed by default. So then you can always click on that, and look, you see what was in the text there. You can also specify that it's always expanded by default, but it already is always expanded by default, so you don't really have to set that, unless you've changed the settings. 

## Benefits of Obsidian Callouts

### Better documentation

So this is a really cool and easy way of having these different colors. I know a lot of people that have come from Notion are kind of missing some of that in Obsidian. Well, this is an easy way to do that. 

### Ability to modify callouts

And you can also change how it looks by modifying either the CSS of the theme or by selecting themes that just really use it and display it to its advantages. 

This theme here that I'm using is, let me check that, because I'm sure that people will ask. This is one of the gems of the year, one of the themes that won, it's called Primary. Yeah, it's really cool, and it's on the light setting. This is a test vault. 

### Callouts are native on Obsidian Publish

And one of the coolest things about this new callouts feature is that it now works natively on Obsidian Publish. So I use Obsidian Publish for my public Obsidian vault, that's [notes.nicolevanderhoeven.com](https://notes.nicolevanderhoeven.com/Obsidian+Callouts). There'll be a link in the description if you want to see what that looks like. It's basically my way of learning in public. And I select different notes to publish on there for people to see, for anybody to see. 

Now, for a long time, admonitions, because it's a plugin, wouldn't show up up there. And then there was a way to do it where you can change the CSS and then kind of do it that way, but now that callouts is in core Obsidian, you don't even have to do that. It's just going to work right out of the box. So all of your notes that have the Obsidian callout syntax on them will show up the same way in your Obsidian Publish site, which is really awesome. 

## Why did the format change from Admonition to callouts?

So you might think, this is really just a format change, right? From admonition to callout, and part of it is that. I asked about why they changed the format, and the answer was that having the blockquote format falls back to blockquotes in unsupported Markdown renderer. 

### New format works better even if callouts aren't supported

So for example, if you're reading this note in an ID and IDE that doesn't support that syntax, it's at least still just going to look like a blockquote, which does make more sense than it looking like a code block, because you might not have code there. This is not just for code, this is for any sort of like sticky note that you wanna put on your notes. 

### Markdown inside blockquotes gets parsed

And also because it just uses blockquotes, this means that all of the Markdown inside it also gets parsed, including links and embeds and even Dataview queries apparently. 

And that also means that spellcheck can check it. Because if you put something in a code block, that's kind of a signal for spellchecks not to have a look at the contents of that code block. 

## Does this completely replace Obsidian Admonition?

So, what happens with admonition? Because it's been around for a while, it's actually still up. And in fact, admonition-style code blocks will continue to work. They're now supporting, Obsidian is now supporting both the callouts and admonition if you have admonition plugin still enabled, then you're still going to be able to use both. So it's not like it's going away, but you should probably use the callout syntax going forward, just because that's what everyone's going to be developing based off of. 

### Admonition can convert between formats

So there is also another thing that admonition is going to do is it does conversion. So if you have existing code block admonitions, then those can be converted to callouts. Actually, I want to show where you can find that. 

So if you go to settings here and look at admonition, there are a bunch of settings here, but let's look at, yeah, the conversions. You convert MSDoc admonitions to callouts, and you can convert code block admonitions to callouts as well. Now, this will modify your notes, so just be a little bit careful with it. Save a backup or do a push to Git if you save it in a Git repo like I do. But that's what admonition is going to be doing. 

### Admonition lets you change callout appearance

And in addition to that, it's also shifted to being able to let you change the appearance of those callouts. 

So it has a bunch of functionality like, do you wanna add drop shadows? And do you want it to be collapsible by default? Because I said that it's expanded by default, but you could change that behavior and toggle it. And then, you could still just expand it on a case-by-case basis. But if you don't specify anything, then it'll just say that it should be collapsed. 

There's also the add copy button, which is actually really interesting because a lot of times that is something that I just want to copy and paste to like my players or something if I wanna paste a description or if it actually is a code block or some sort of troubleshooting thing, so I enable that. And you can set admonition colors. 

You can also change the icons that are loaded there. So right now, admonition uses the Font Awesome icons. So I was showing you all of these different types of callouts, right? But those are the default ones. And admonition adds the Font Awesome ones as well. And you can even add your own types of icons. So you can load additional icons. There's Octicons and RPG-Awesome, which sounds really interesting, actually. 

And a cool effect of that is we need to do this in admonition syntax, so it's code blocks. Let's say, let's just go with question. This is a question. A cool thing that you can do with admonition is you can do icon, and then choose an icon that isn't already in there. So as an example, I happen to know that there is a Font Awesome icon that's a cloud, so I'm just going to put cloud there and then I'm going to put, here's the answer. If I go out there, look, now it looks like a little green cloud, so I can change everything about how it looks. This is still in the admonition syntax, though, but it functions the same way as callouts, just extended. 

I really like this for being able to give instructions and then say, you know, this is Apple-only and not for Windows. So that's really cool. 

## Should you keep using Obsidian Admonition?

So I guess the question is, and this was my question when I learned about these changes, is it still worthwhile to use admonitions because of all these quality-of-life improvements? 

I think it is, because, don't get me wrong, I'm very happy that callouts is part of Obsidian now, that just made sense for an app that is so focused on notes and note-taking and documentation. You really need these different ways to take notes on your notes. 

### Custom icons and admonition types

But I do think think that admonition is still worthwhile installing and using if you want to delve down into the specifics of this feature. So if you want different icons that make sense to you, but maybe not to other people, this is still the best way to do it. 

### User interface for inserting callouts OR admonitions

Another cool thing that I didn't show, let me show that now, is maybe you don't want to remember the syntax with either with the blockquotes or with the code blocks. 

So with admonition turned on and enable, installed and enabled, you can bring up your command pane, which for me is Command + P, and I'm gonna type in admonition, and then you can just either a callout or an admonition and a bunch of other things as well, but I'm just going to insert a callout. And if you didn't remember what the types were, they're all here. And this is what they're going to look like. 

Now, as I mentioned, I think these, the ones that I grouped, are actually supposed to look the same without the admonition plugin, it's just that either the admonition plugin or my theme is making them look a little bit different, but these are the standard ones. 

So then you can choose which one you want. You can have the title there. You can choose whether or not it is collapsible. It even shows you a preview. So let's insert that. And look, I didn't have to type out any of that and I didn't have to remember any of that syntax. So that's just a nice little upgrade that you can only get with admonitions. 

## Obsidian callouts is available now

_Note: Obsidian callouts is available for all users for free now!_

Again, Obsidian callouts, at the time of this recording, is only available in Insider Build version 0.14, which means you can only get it right now, if you need to get it right now, you'd have to pay for the Catalyst plan, which is a one-off $25 fee. I've paid that just because I wanted to give back to the Obsidian developers for this amazing tool that they just give for free. 

But if you're willing to wait, this feature, like all features, will soon be publicly available, Insiders just get it a little bit earlier. And when that happens, I'll pin a comment in the comments below for this video so that you know when it's available.

And if you'd like to learn about other Obsidian plugins, I do have [a video on the top 10 Obsidian plugins](https://youtu.be/W7kTtn9empU), so maybe check that out. 

Thank you for watching!