---
title: "Innovation in Isolation"
date: 2020-05-05T22:59:57+01:00
draft: false
tags: ['culture', 'english', 'flood.io', 'text']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/innovation-in-isolation">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/innovation-in-isolation)._

We've always been a fully distributed team at Flood, but the current world crisis has still changed the way we work. Here are some of the things we're doing to keep self-isolation from being _too_ isolating— and maybe it'll help your team too!

Within the Flood team, flooders-in-training (aka children) have made more surprise appearances in team meetings. Work has been punctuated with grocery runs to buy essentials before they run out. Some of us who were out of our home countries when all this happened have had to arrange emergency travel before international borders shut. It would be foolish to deny the impact on team morale as the entire world goes through this collective trauma, eyes glued to numbers that increase by the minute.

Not exactly the most productive work environment.

Yet there's still work to be done (something we're grateful for), and there are still many features we'd love to bring to Flood. So how do we keep everyone motivated to release and maintain software?

## Encouraging banter

Work shouldn't be all about work. Understanding everyone's personal circumstances is vital to a team's ability to work together professionally. We use Slack as our primary communication tool throughout the day, and we already had quite a few non-work channels on there (#anything, #hobbies, #gaming, #drones, and #travel to name a few). Now we have one for COVID-related chatter as well.

![](/blog/assets/20200505-01.jpg)

In this channel, we share news from our parts of the world, post photos of things that are sold out in our local supermarkets, talk about new hobbies we've taken up to stay sane, and discuss the struggles of co-working with spouses and children who are now also working or studying from home.

Having a dedicated channel gives people license to open up about what's going on in their personal lives, and it helps the team understand where everyone's headspace is at. We also use #eng-covid-19 for memes. A lot of memes. It's easier to work through a tough situation if you can laugh about it together.

## Over-communicating

Our co-founder and Product Manager, Ivan Vanderbyl, recently [wrote a great article](https://enterprisersproject.com/article/2020/4/9-collaboration-tool-tips-remote-teams) with some tips for keeping communication lines open. This is particularly important during this crisis, where schedules and priorities can change quickly.

* Emojis - We use emojis as a non-verbal cue to convey tone, approval, agreement, and disagreement. We add emojis to messages we send and also use them as reactions on Slack to messages from other people. Even when you don't have an answer or when a response is not required, emojis signal acknowledgment so that nobody feels like they're shouting into the void. Over time, we've developed emojis that are specific to Flood culture, such as the avocado:

![](/blog/assets/20200505-02.jpeg)
_Source: Our [Twitter account](https://twitter.com/flood_io/status/1230166412066512896)_

‍We even have a fruit-based vocabulary of emojis that we can use in our Slack status messages to convey our general mood. Being in Carrot Mode, for instance, means that you're trying to focus and would appreciate not being direct messaged or @ mentioned.

![](/blog/assets/20200505-03.png)

‍When working remotely, and especially when in self-isolation, everyone has their own cadence for working. It's on each person to communicate that schedule so that others can respect it.

* Text chat - We're used to working asynchronously due to time zones, so text-based discussions are necessary. We try to over-communicate and "think out loud" before making decisions just in case we have to suddenly stop working due to illness or other pandemic-related reasons. Even something as simple as leaving a link to a document that we're working on means that someone else will be able to find it if we're unavailable.

* Voice chat - We tend to use voice chat for quick discussions or updates about work-related things. It's also great for those of us in Europe who are suffering from slower internet connection speeds at certain times of the day due to everyone being home and streaming Netflix.

* Video calls - Video calls are for team retros, 1:1 calls with managers, and personal or sensitive conversations where body language is crucial. It's also great for recreating that "hanging out at a pub" vibe. Speaking of which... welcome to the Flood pub!

![](/blog/assets/20200505-04.jpeg)

The Flood Pub is open on Friday afternoons. It's where we all hang out together with a beverage of our choice and talk about things that are entirely not work-related. We hop on a Zoom call together, Tim (our General Manager) fires up the "jukebox" (Spotify playlist), and we end the week by getting some facetime with each other—just as we would do (and have done) if we were together in person.

![](/blog/assets/20200505-05.jpeg)

‍Meeting in this low-pressure context lets us talk about things we wouldn't mention otherwise. It's also a fun way to check in with each other after another week at work (and in quarantine).

## Doing stuff

While communicating openly is productive, getting stuff done as a team boosts spirits.  Here's what we've done recently to kick our output into high gear.

### BOINC

Like most of you, we've been cooped up in our houses, watching events unfold and feeling helpless as things happen that are beyond our control. BOINC gives us a chance to do something to contribute that IS in our control.

BOINC is a platform by the University of California Berkeley that lets you volunteer your spare computer (or mobile device!) processing power to science. From the official site, Boinc "downloads scientific jobs to your computers and runs them invisibly in the background."

In our case, we wanted to help sequence proteins like the novel coronavirus using Rosetta@Home. BOINC is a perfect fit for Flood because we are in the unique position of starting up and managing thousands of virtual machines 24/7. Our Ops team has been hard at work automating the donation of our computing power to the Rosetta@Home project when these machines aren't being used.

![](/blog/assets/20200505-06.jpeg)

We're proud to say our contribution is INcreasing over time as our engineers find new ways to streamline the process. We're already in the [top 5% of BOINC users in the world](https://www.boincstats.com/stats/-1/user/detail/87605321733/overview) by contribution.

### GIG: Great Ideas Gathering

Every year, the mothership (Tricentis) runs a three-day hackathon called GIG. Two weeks ago was the first-ever GIG where most participants, not just the Flood team, were working remotely.

The theory behind hackathons is that the daily grind can be exhausting after a while, and it can sometimes be beneficial to introduce a short burst of work to revitalize the team. Hackathons provide a framework for small groups to pitch, execute, and report on a single idea without committing too much time to it. Everyone gets a chance to step away from regular duties and work furiously together on something they might not have otherwise gotten to work on.

A hackathon where the team members are separated by distance and timezone is certainly another beast, but here are some lessons we learned about remote hackathons:

* **Come up with a good idea**: This is easier said than done, but a good hackathon idea is a creative solution that delivers a lot of value. Here are the ideas we came up with:

    - Floody - Use AI to improve onboarding by walking new users through the steps for running a flood (live on Flood now!)

    - Flood Bot - Add smarter checks to detect patterns in load tests and help flooders understand their results (prototype)

    - Flood Gate - Use AWS Fargate to reduce costs in provisioning, scaling, and managing virtual servers by about 30% (proof of concept)

When thinking up ideas for GIG, we didn't commit to releasing them publicly. Even a project idea that doesn't end up making it into the finished product is an occasional worthwhile detour for team productivity and morale.

* **Limit scope**: GIG is a sprint, not a marathon. While my team (comprised of Jason Rizio and me) was planning out what we wanted to do, we quickly realized that there was a lot more that we wanted to do, but it just wasn't feasible within the strict timeframe. In the end, we decided to go for an incremental piece of work that we could push to production before the deadline instead of completing just one step towards something abstract and unreleasable.The other Flood teams also needed to whittle down the scope to a smaller, completable chunk: a working prototype.

* **Clarify assignments**: With members on different timezones, it was essential to have an initial meeting to plan out everything that needed to be done and by when. In this situation particularly, we found it useful to split apart the project into independent chunks, to minimize the need to collaborate in real-time.

* **Touch base regularly**: When working independently, team members can quickly diverge off the main path. To avoid that, we met up at least daily by hopping on an audio call on Zoom to spend a few minutes updating each other on the work we'd done. Doing this gives others a chance to help out when one member encounters roadblocks.For anything that didn't need to be real-time, we worked asynchronously on chat. Here's a screenshot of the number of messages and files exchanged to our dedicated GIG Slack channel during the event:

![](/blog/assets/20200505-07.jpeg)

‍Yup, 1,535 messages and 60 files in 3 days. That's collaboration!

We generally prefer public rather than private channels, and we certainly stuck to that throughout GIG. When you're working with more than one person, it's counterproductive to have private conversations that can't be referenced by other people.

We also learned that it's useful to keep tabs on what the other teams are doing. After the event started, my team realized that another team was changing a page on the Flood app that we intended to use. Luckily, both teams were able to work around it.

It's also only fair to let other teams chime in on important decisions within the project that might affect future work— like the name for your mascot.

![](/blog/assets/20200505-08.jpeg)

* **Leave time for the video**: It's not just about doing the work; it's about communicating what you've done in a way that others can appreciate. Here's a video that my team (composed of Jason Rizio and me) put together for Floody and our improvements to the onboarding process:

{{< youtube OeIPWovOua4 >}}

* **Celebrate**: After the work is done, don't forget to pat each other on the back for the hard work! For us, this meant [a round of tacos](https://twitter.com/c_a_dunlop/status/1246111919762591746) for everyone and a trip to the Flood pub. (Why do we have so many food-based rewards?)

## It's not easy

Keeping a team unified and working efficiently towards a common goal is always tricky, and working remotely, especially during a world crisis, doesn't change that. Distributed team members need to put in more effort to consciously over-communicate, make room for each other's unique circumstances, and do little projects that foster creativity when we're all feeling a little lackluster. Incorporating these tips can create a culture of healthy productivity within a remote team.

‍