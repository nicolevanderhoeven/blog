---
title: "Presentation Slides as Code"
date: 2021-03-02T19:07:31+01:00
draft: false
tags: ['english', 'text', 'obsidian', 'Markdown', 'DevRel', 'hugo']
---

I was working on a presentation for later this month when [Marie Drake](https://mariedrake.com) told me about [slides.com](https://slides.com). It's basically a Powerpoint replacement (which, let's be honest, needs replacing) in that it lets you create slides _and_ it lets you present from it. It even goes beyond Powerpoint in that it also saves your slides publicly for people to view later.

Before she'd mentioned slides.com, I had been planning on creating a presentation on [Obsidian](https://obsidian.md), my note-taking tool of choice. The advantage of this approach is that presentations in Obsidian are just Markdown files with `---` between lines of text to delineate slides. 

The problem with using Obsidian on its own is that it's severely lacking in features, and it's also not shareable. You can, of course, publish the Markdown file, but people won't be able to view them in slide format. After playing with slides.com, however, I also discovered it had its own weaknesses. It is completely UI-driven, so there's no way to create slides just from a Markdown file. It's also hosted by them, so there are limitations imposed, depending on which pricing tier you pay for.

So I got to Googling. And I think I found a pretty good setup for my needs.

## The end result

- I write the presentation in Obsidian, in Markdown. [Here's](https://gist.github.com/nicolevanderhoeven/752017196efc1ee861c6d3baa5dfca31) what that looks like in a sample presentation where I'm trying out a bunch of features.
- I use [Hugo](https://gohugo.io) to generate a static website and convert the Markdown files into javascript and html, using [reveal.js](https://github.com/hakimel/reveal.js) and the [reveal-hugo](https://github.com/dzello/reveal-hugo) theme.
- I push the static website to a remote repository on [GitHub](https://github.com). [GitHub Pages](https://pages.github.com/) serves that site (for free!) on my custom subdomain.

Check out the final product here: 
[https://slides.nicolevanderhoeven.com/sample](https://slides.nicolevanderhoeven.com/sample)

![A screenshot of the title presentation slide](/assets/20210302-reveal-hugo-sample.png)

## The setup

### Prerequisites

- An Obsidian vault (or you can actually just use any text editor)
- Git installed and set up with credentials
- A GitHub account
- Hugo installation (`brew install hugo`)

### Create a new Hugo site

Open up a terminal window and `cd` to a folder in your Obsidian vault. Then, create a new Hugo-generated site:

```bash
hugo new site slides
```

Replace `slides` with the name of your new site.

You should have a new directory, `slides`, in your Obsidian vault.

### Add the reveal-hugo theme

`cd` into `slides` and clone the reveal-hugo repo. The documentation suggests using a submodule:

```bash
git submodule add git@github.com:dzello/reveal-hugo.git themes/reveal-hugo
```

Personally, I just cloned it because I know I'm probably going to be messing around with it substantially:

```bash
git clone git@github.com:dzello/reveal-hugo.git themes/reveal-hugo
```

You should have a `/themes/reveal-hugo` folder that contains the theme.

### Configure reveal-hugo theme

Set up your new Hugo site to use the reveal-hugo theme by adding the following to `/config.toml`:

```yaml
theme = "reveal-hugo"

[markup.goldmark.renderer]
unsafe = true

[outputFormats.Reveal]
baseName = "index"
mediaType = "text/html"
isHTML = true
```

The `Reveal` part is what lets you output text in slide format.

### Create your slides

Go to `/content` and create a file there, called `_index.md`. The filename is important, as is its location (I learned that the hard way). This file is going to be the first page people see, so it should probably be a list of your presentation slides. For now, put in something like this:

```markdown
+++
title = "My presentations"
outputs = ["Reveal"]
+++

Here are my presentation slides!

[sample presentation](/sample)

```

Then, create a new folder for your presentation, such as `sample`. In `/content/sample`, create a file called `_index.md`. Again , the filename is also important here (guess how I learned that).

This index file is going to be where you actually create your slides. Here's the context of my `/content/sample/_index.md`:

<script src="https://gist.github.com/nicolevanderhoeven/752017196efc1ee861c6d3baa5dfca31.js"></script>

Each slide is separated by `---`, just like in Obsidian, which apparently uses the same converter that reveal-hugo does, [reveal.js](https://github.com/hakimel/reveal.js). Note that if you want to try out having an image as a background to one of the slides, you'll need to add that to your `/sample` folder and change the filename in the slide in this part: 

```bash
slide background-image="lucrezia-carnelos-AsM4T46tqcU-unsplash.jpg"
```

### Generate your site

Now it's time to generate your site! Wait - didn't we already do that? Sort of that. That was creating the framework for the site, but now you need to get Hugo to convert those Markdown files you've just created into something publishable. So cd to the root directory `slides` and run this:

```bash
hugo
```

That command should generate a `slides/public` folder, where all the publishable code will go.

At this point, you can also check your work by starting a local server with `hugo server` and navigating to `http://localhost:1313`.

### Push your site to a remote GitHub repo

`cd` into your public folder. This is important, as I initially started the repo in `slides` and it took me ages to realize that GitHub Pages requires an `index.html` in the root directory to function.

Initialize a Git repo:

```bash
git init
```

Stage and commit your changes:

```bash
git add .
```

```bash
git commit -m 'Initial commit'
```

Create a repository on your GitHub account called `username.github.io` where `username` is your GitHub username. (If you already have a repo called that, you can alternatively push the contents of `public` to a branch called `gh-pages`). The repo name matters.

Push your changes to your repo.

```bash
git push -u origin master
```

You should now have a repository on GitHub called `username.github.io`, containing everything in `public`.

### Set up GitHub Pages

On GitHub, go to the repository settings and scroll down to the GitHub Pages section. Select the right branch (`master` in most cases) and click Save.

### (Optional) Using a custom domain

If you want to use a custom domain, enter it in the repository settings from the previous step.

Then, go to your domain registrar and add a CNAME record pointing `www` to `username.github.io`. [Here's more information on that](https://docs.github.com/en/github/working-with-github-pages/about-custom-domains-and-github-pages) from GitHub.

It can take a few hours for DNS records to propagate, so after you set this up, take a break before you convince yourself you've set something up wrong. ;)

### Check out your new site!

When you navigate to your new site, you should first see the contents of `slides/content/_index.md`, which has a link to your sample presentation. Clicking on that should _reveal_ (ha) the slides one by one. You can navigate through them with the arrow keys, and you can also see speaker notes (if you put any in, which I did on the third slide if you copied my sample slides).

### Other issues I faced

I ran into a few issues during this setup because:

- I was already tracking changes in my Obsidian vault with Git
- I already had a repo called `nicolevanderhoeven.github.io`, and I needed to create a branch called `gh-pages` to still use GitHub Pages.
- My Obsidian repo on GitHub is a private one, but I wanted the slides to be public.

If you have a similar setup, maybe the following instructions will help.

#### Use worktrees, not subtrees or submodules

After attempts to make this setup work with submodules and subtrees, both of which were way too complicated for what I needed, I settled on using worktrees.

Add `public` to `.gitignore`. From `slides`:

```bash
echo "public/" >> .gitignore
```

Create a worktree for `public`, to be tracked on the branch `gh-pages`:

```bash
git worktree add public gh-pages
```

After you generate the static code via `hugo`:

```bash
cd public
git add .
git commit -m 'Commit message'
git push origin gh-pages

```

Your `gh-pages` branch should contain only the files in `public`.

#### GitHub Pages with a private repo

GitHub Pages is free, but if you want to be able to use it with a private repo, [you can't](https://docs.github.com/en/github/working-with-github-pages/troubleshooting-custom-domains-and-github-pages). Sorry!

You can look into using GitHub Actions to copy `public` from your private repo to a public one, or you could just [spend the $4/month](https://github.com/pricing) to remove the restriction. I opted to pay, because I love GitHub anyway.

## Presentation as code

That's it! I ran into a few snags while I was attempting to implement this, so I thought I'd document it here in case it helps anyone else. Despite the setbacks, I think it's worth it-- I can now whip up presentations in Markdown within Obsidian and have that published to a site I control for people to look through at their own leisure. This should speed up my presentation creation process considerably.

Theoretically.

If only I could stop procrastinating on creating this presentation by setting up a framework for creating presentations...
