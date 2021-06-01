---
title: "What Is Load Testing? - A real-world explanation"
date: 2021-06-01T20:23:17+02:00
draft: false
tags: ['english', 'performance', 'video', ]
---

I've made about 60 videos on load testing and application performance to date, but I realized that I've never made one defining load testing, which seemed like a glaring mistake. So, here's my attempt!

{{< youtube cCFwqlcHkX8 >}}

*Rough transcript below - though I went off script a few times:*

Load testing is a key part of making sure that an application performs well and reliably. But what IS load testing, anyway? In this video, I break it down for you in simple terms. And if you're a family member or friend of mine trying to understand what it is I do for a living, thank you! This is for you too.

### Software testing

It takes a whole team to build software, but some roles are more visible than others. For example, pretend you want to build a bridge. Who do you need to build it?
- An architect to design the specifications of the bridge
- A liaison or representative to the gemeente or local council to clarify what the specifications ARE
- Builders who will physically build the bridge, who might need to hire subcontractors for various materials and services
- Someone to double-check that what you're building is up to code (testers)
- Someone to manage it all, and maybe a few more levels of team leads
- Traffic enforcers to detour traffic away from the bridge while it's being built

So who is responsible for "building" the bridge? The answer is, everybody. Everybody has a part to play. Every part is important.

It's the same thing with software. When we think about building software, we often think about developers, but that's not the full picture. Just like building a bridge, it's a team effort. But I want to zoom in on one role in particular, because it's the role I've had most often: load tester.

But first, let's go on a field trip. 

### Load testing on the field

Does this bridge look familar? This is the Sint Servaasbrug, and they SAY that it's the bridge on the €10 note. It might be true, too, because it's here in my current hometown of Maastricht, the Netherlands, where the European Union was founded in the Treaty of Maastricht. The name Maastricht means the crossing of the Maas, which is the name of this river here.

So let's pretend the bridge hasn't been built yet, and that we're helping build it. Let's put on our load tester hats. As a load tester, it's our job to make sure that the bridge can support the weight it is intended to support.

How do we know how much weight it's intended to support? Well, the council or the rest of the team helping us build the bridge might have some ideas on that, or some building standards that we can use. That's a good place to start, and we should definitely discuss that with them, but as a load tester, it's also our job to question those requirements. Let's do some research.

This is the street leading up to the bridge. Remember, the bridge isn't built yet, but maybe we can get an idea of the kind of traffic that the area gets. 

Some things to watch out for or questions to answer:
- How many people are walking?
- How many are on bikes?
- How many are on bakfiets bikes?
- Are vehicles allowed on this street, and if so, how many of them drive through?
- Do people tend to pass by in groups, or on their own?

Another thing we can do is check other bridges. This is the Hoogbrug, another bridge across the Maas river. It's not going to be an exact match for the kind of traffic we might expect on OUR bridge, but it might give us some ideas. So we can scout this out the way we did the street near our bridge.

One difference we can see right away is that this bridge has stairs on both ends. Our bridge isn't going to have that. The stairs do have the lip to make pushing a bike up it easier, but it's not as easy as riding through, and any heavier vehicles are out. And people are probably less likely to go up stairs than they are to walk up an incline. So we already know that this bridge will probably experience less traffic than our bridge, but it's still good to take notes on.

Okay, let's head back home, write down our findings, and think about what we've learned.

### Tying it back to software testing

What we learned was useful, but there are still a few things we don't know:

- It is 10 AM right now. But is that really the highest point of traffic during the day? To be really sure, we should really try to go back at different times. Maybe there's an increased amount of traffic during lunch as people go to restaurants or back to their homes to eat. Maybe a horde of kids would go across our bridge after school to go home.
- And we should think beyond that, too. Are weekends busier because more people are out? Or are weekdays busier because people are going to and from work?
- Then there are some things that are seasonal. Maastricht happens to be in the part of the Netherlands that celebrates Carnaval, so sometimes that area looks like *this*. Carnaval involves a slow parade of people, bikes, and trucks through the bridge to the central town square, called the Vrijthof. That's absolutely something we'll have to plan for when testing our bridge.

We've been talking about the bridge this whole time, but as load testers, we go through the same process for software, too. What we've just done on our field trip is called a workload model. A workload model is describes the load profile for a given test scenario, and it involves determining _what_ (the key transactions), _how much_ (the load distribution among the transactions) and _when_ (timing of the load) to test.

For a web application, for example, like a web site, we might try to look through analytics and monitoring tools to try to determine things like:
- How many users access our site?
- Which pages do they visit? Some pages are like pedestrians - they don't have much comparative weight and aren't complex to process. But other pages are like big old trucks, that involve many components of our application and are comparatively very intensive.
- When do they visit the site? Is our site the sort of site people go to to work, or to avoid work? at weekends, or during the week?
- Are there any seasonal events, like sales or holidays, that might drive MORE people to our site?
- Where are the users from? Are they in the same country that our application servers are located in, or are they quite far away? What sort of internet speeds do they have? What percentage of them use computers to access our site, and what percentage of them use tablets or mobiles?

That was just a taste of the kinds of questions a load tester has to answer during the course of testing. There's still a lot more to cover - for starters, we haven't even talked about how to actually RUN the tests yet! I plan to make more videos going through typical activites in load testing in more detail, but for now, I hope that gave you a good idea of what load testing is. And Mom, I hope you know what I do for a living now. :D

Thanks for watching!