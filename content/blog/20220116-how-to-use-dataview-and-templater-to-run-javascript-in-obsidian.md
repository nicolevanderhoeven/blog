---
title: "How to use Dataview and Templater to run JavaScript in Obsidian for automating task management"
date: 2022-01-16T16:30:22+01:00
draft: false
tags: ['english', 'code', 'obsidian', 'personal knowledge management', 'JavaScript', 'task management', 'ship30for30']
---

TIL how to run JavaScript in @obsdmd. A friend of mine had an interesting use case: He had a long reading list from his studies, and wanted to use Obsidian to decide what he could read given a certain amount of time.


TL;DR: [Here's the script](https://gist.github.com/nicolevanderhoeven/eccc6f910cdc48a5b7934b53a5a0f244).
And here's the end result:
![Gif of the full setup working](/assets/templater-demo.gif)

Requires: Obsidian. The Dataview and Templater plugins. Also requires a separate markdown page for every chapter or bite-sized section of the book or course, with the metadata `time_required` in the YAML frontmatter.


Why Dataview? Dataview can parse that frontmatter, grab the value for `time_required`, and return a list of pages and links. There is a Dataview Query Language, but dataviewjs is more extensible.


Why Templater? I initially wanted to write a script within a dataviewjs block, but:
- Dataview results are only rendered in Preview mode (which I don't spend much time in)
- I hate testing JavaScript within Obsidian.


Instead, I created a folder `scripts` within my vault and selected it as the "user scripts folder" in Templater settings. Then, I created a script, `returnStudyOptions.js`. [Here's the gist for that](https://gist.github.com/nicolevanderhoeven/eccc6f910cdc48a5b7934b53a5a0f244).


In a new note, I typed `<% tp.user.returnStudyOptions(tp, 60) %>`. This line calls the script I created and also passes 60 minutes as the time available. 


I selected "Templater: Replace templates in the active file" from the Command Pane, which runs the script and replaces the line with the script's returned value, which looks something like this:
![Screenshot of the notes returned by the script](/assets/templater-result.png)


I also assigned a hotkey to for replacing the template, for ease of use. That's it! I thought this was a fun way to learn how to use JavaScript in Obsidian. Thanks to [@ealameda](https://twitter.com/ealameda) for the use case!