---
title: "Canonical Observability with Simon Aronsson and Michele Mancioppi (k6 Office Hours #38)"
date: 2022-01-21T18:23:47+01:00
draft: false
tags: ['k6.io', 'grafana', 'performance', 'english', 'video', 'ship30for30']
---
Today, my former colleague [Simon Aronsson](https://simme.dev) brought his _new_ colleague, [Michele Mancioppi](https://twitter.com/mmanciop), to k6 Office Hours to talk about observability, and how they do it at [Canonical](https://canonical.com). It turned into a great conversation about trends in observability from the last decade, and how it relates to performance and reliability testing.

{{< youtube SD5Y4QejEu4 >}}

## Transcript

- Hello everyone, and welcome back to the first k6 Office Hours of the year. Happy 2022, I'm Nicole Vander Hoeven.

- And I'm Simme, we're back from the dead.

- And I'm Michele.

- Simme is back. Yes, so Simme unfortunately is only temporarily back, and he's brought his new colleague. I mean, I'm kind of sad, but I'm happy to meet you Michele Manciopi.

- Hello everyone.

- Welcome. Simme why don't you first tell everybody, how you betrayed us at k6.

- Sure, I'm so sorry for that, was a couple of months ago now. I think I quit at k6 in October, beginning of October something like that, to join Canonical and Michele, where we are trying to build a really awesome observability stack to know little part built on top of Grafana products.

- Yeah, it has been a very interesting three months. It's actually a pretty refreshing to be able to use high quality software and compose it in ways that are, you know, they just work through, cool.

- So we already have a few people in the peanut gallery, there's Simme and Michele and our newest colleague, I think senior performer, all saying hi to you Simme. so you're very much missed.

- Congratulations to k6 for bringing Leandra.

- Definitely, and by the way, Leandra will be on k6 Office Hours next week, he just accepted the invite. So when I'm letting him like relax, and do his bootcamp onboarding things, and his week of load testing this week. . Ooh Danielle is here as well. Michele, why don't you talk about yourself, and what you do at Canonical?

- Well, I am a product manager at Canonical, for observer BD team. I was brought in with the goal of making the entirety of the product line of Canonical observable. Canonical is chiefly known for Ubuntu, but we have like a meter other products and they all need to be observable because they all sit at different levels of critical pieces of the infrastructure. Before Canonical, I was the technical product manager at Instana, which has been what baby ham it's a product that does very automated observability. It's mostly proprietary, but it was a lot of fun trying to make observability the way it's supposed to be. That is seamless. Very easy to roll out. Before that I was at SAP where I was the technical lead of the performance team for SAP cloud platform, where my job was mostly to figure out where things were slow and fix it. And then I realized that rather than helping one single developer at the time, would they be more productive in actually providing pretty decent tools to do that at scale so people could do it themselves, which then brought me down the path of figuring out it's actually fun here to make an observability product than it is to using one. And then the CircleCI.

- So Simme what was it about Canonical that won you over?

- I actually think it was to no little part Michele won me over with his argumentation for--

- Okay. I'm taking him off the stream sorry. No, no, No.

- 'Cause I got you everyone, bye.

- No. We're still all friends.

- I do really miss the k6 family for sure. But yeah, it was just such a cool and exciting opportunity to be able to make this huge leap in observability with Canonical, for such a vastly used project or suite of tools and products. So that's mainly one of them.

- I'm sorry. Can we stop to remark? That was the coolest cup I've seen in a long.

- It is as if this is sponsored, this is a hydrate spark, it's a smart water bottle. And it's marketed like for people like me because it's a water bottle, but it has Bluetooth and LED light. So, you know, obviously I had to buy.

- Yeah, just out of curiosity, what are the key values of the Bluetooth support?

- Oh, it tells me when I need to drink water. It's very important stuff.

- How do you monitor that A, the Bluetooth is working and how do you receive those notifications?

- Well, it's funny that you ask, there is an app for it. This is totally not sponsored. Okay. But there is an app for it. I was gonna say Simme that it seems like there was a slight change in your focus as well, because at k6, we're more focused on the performance and reliability testing part of it. But definitely we've also dabbled in the observability space, especially with the acquisition of Grafana. So it seems like your new role is also more focused towards observability. Was that one of the considerations?

- Sure it is. And then that was definitely one of the considerations during my, what is it now? 12 or something years in tech, I've been doing way more observability and monitoring work than I've been doing performance testing. And so that definitely felt like coming home in a sense to me.

- And I wanna ask you both this because you've both been in observability for awhile. How do you think observability and performance testing go together? Do you see them as separate disciplines entirely, there's clearly some sort of overlap, right? Should companies be doing both, one or the other?

- I definitely think there is a lot of overlap. One thing that I know that you and I have been pushing forward when we've been discussing this previously on the stream is that performance testing is great, but it usually only allows you to do a black box perspective testing, right? You're able to measure the performance of your system, given certain interfaces or end points that you are able to observe the performance off and pairing that with observability tools, like for instance, loci or tempo, or Prometheus's allows you to really drill back into the stack and figure out what is causing those problems. So I definitely think that it makes sense to combine the both to be able to observe the whole system and not just the edges of it.

- Do you agree with that Michele?

- Yeah, very much, over go and say that actually, it's very hard to draw a demarkation between the performance and of observability, especially since in the last few decades and the increasingly disproportionately larger role that internet and internet systems taking our lives. We have come to see, you know, slow as the new down, which means that not only the software needs to work but it needs to be fast. And if you observability is fundamentally the art of understanding, are there problems? I mean, so how bad was impacted and how badly, and that is both in terms of software, it is broken as software is luck. Many of the techniques that you would use in, for example, a QA system to check the scalability of your software is something that you can use at scale in production to make sure that you're at least carrying that much load, as well as techniques for example, for performance testing, you often do a lot of black box monitoring. The techniques that you use to check if today in SIL on a mobile connection, your web store is reachable is very similar in terms of technologies and capabilities and as technical requirements. So the technology is there to use, to throw a lot of requests security to your software. So it's fundamentally the performance tools are versatile like that.

- Yeah, I totally agree with that. I have always taken the stance that it's definitely better when you have both of them because observability is great. But then in pre-production environments, it can be a little tricky 'cause you don't have real traffic and that's where performance testing can come in handy and performance testing is great, but you don't always want to run it in production. And also you, it's not always a good idea to be reliant on the results of the performance testing tool. You know, sometimes it makes a lot more sense to be already using the same observability stack that you use in production. And I also want to call out that performance testing is often thought of as load testing, but that's really just one kind of performance that is being measured there. And so what about a related topic to observability as monitoring? I know Michele, you have a lot to say on that topic.

- Oh my, can I rant?

- Yes. Go ahead. I'm familiar with your blog posts.

- Ooh influence. I have a --

- I do research, you know.

- I thought you came across it because, you know, super rabid spike. No, the, so I have been around the observability industry for awhile and I have a certain annoyance towards what the industry has done by rebranding perfectly good monitoring and application performance tools in terms of the hot new term up observability that you need to sell to sort of the software. The way I see it's a much more formal, shall we say way. Observability is a property that you want your systems to have, monitoring is the way that we have to make most systems observable. However, something that I hope we will see in our lifetime, our software systems and such a level of quality and standardization in our profession of creating software systems. So that monitoring and observability becomes build team in the softwares we create. If you think about it all the for example, automatic distributed tracing and all the amazing innovations that have occurred over the past 15 years are effectively reckoning the lack of observability as a functional requirement of a piece of software. Monitoring is the art to collecting data.

- Yeah, and I think that there's also a connotation of monitoring being a bit more passive. Would you agree with that?

- Not necessarily, no. At the end of it so there is, I really take the view that monitoring is a means to the end of observability. It is true that in the past few years, with new generations of tools, we have made leaps and bounds in both the capability of collecting useful telemetry with very little work in terms of toil to roll it out, without the proper tools are there and I used to work for one where you deploy an agent and it automatically discovers all around it. There is a lot of dark magic going on, but it works. And then it becomes very cheap to actually get to the holy grail of monitoring that is to have as little silos as possible. Telemetry wants to have friends. You want to see end to end systems how they relate to one another. Now, the moment that something that has changed recently in the industry is we have gotten better, not only at collecting telemetry, but analyzing it. When you compare monitoring tools that we started with right there the Nagios of the world. You'll need it to know in advance what you were looking for. Now with broader collection of telemetry, for example, distributed tracing, a very powerful type of telemetry, very little underutilized in terms of the insights can provide you, you end up having a lot of data that is likely going to be useful, and you have much more freedom in how you analyze it, both in terms of discovering issues as they occur, as well as afterwards in terms of post-mortem.

- I do have, however one, I agree with you completely Michele. I do however, think Nicole has a point in that if you look at the traditional monitoring tools that people used to use, like Nagios for instance, it was always this very weird situation where you put up SNMP traps or collected, you know, logs that were thrown at you in a very passive manner. But I would say that it turned monitoring itself has come to evolve into a state where it very much is an active practice in the same way as people would describe observability.

- Oh. So you are making a very interesting distinction of rather than receiving as a data sync telemetry that was emitted, but something else that you go and get it through RTI, things like deploying an agent that does stuff. That's pretty interesting.

- Yeah. Or for instance, actually triggering a synthetic test that just prompts a common user flow and make sure that that still works. I mean, as compared to just admitting this passive telemetry data that just keeps rolling on, but maybe lacks the context as you put it on more advanced workflows where you'd correlate multiple sources of data or the multiple actions to derive your data that you want to.

- It is true that in the past 15, 20 years, there has been an increase of active monitoring. I remember doing it back in the day with smoke tests that were of a crunch up every 15 minutes. I was so young. And now it's that it's kind of a baseline of observability. I mean, you need to want to catch everything, but if there is catastrophic failure, you will know hopefully before someone starts opening tickets or you're upping your drops. Yeah.

- Yeah. I think Simme it was right when he was saying, what I was talking about was like the more traditional approach that it's just something that's there in the background whereas these days, the way that it should be done is a lot more proactive.

- And also they focus on actually gathering telemetry to be able to detect failure modes rather than probing for a certain thing. It used to be much more focused on a single point that you would probe for data. And--

- It used to have simpler software too.

- We sure did.

- Yeah, that's for sure. But I also wanted to say that there's also been, there's still some push based monitoring, but we're also now seeing more poll based monitoring systems, more event driven ones. And I think this is all the evolution of monitoring and observability, right? Because these things did not exist not too long ago.

- To be fair, the one should, it is pretty true. We have much more pool and pool length. This is something that a permit use has pretty much popularized with the concept of scraping, but there are entire domains where we deploy a software that is still very much push based. For example, IOT, for very basic reasons of network visibility, it's very hard to go and reach out into someone else's rooftop and go get the data. So there is still the mechanics of push buffer and pulled it for example, gave us in the primitive ecosystem, push gateway mechanism.

- Grafana agent that actually sits in between you and a cloud service or something else, and allows you to not punch holes in your firewall, but rather reach out and deliver data to something.

- Yeah, it's kind of like you mentioned that our applications in general are just getting more and more complex, it reminds me the push the trend from monolith to microservices and then now some people are also going back. It's never really gone, right. And it's really difficult to say, no, this is the new way, nobody else is doing or should do the other way. It's not really like that. A lot of things in tech are cyclical.

- When I actually spoke about our systems are getting more complex. I was thinking exactly of micro services because we made a trade as an industry for very, very simple, very small components. And then pushing all the complexity that you cannot make disappear under the carpet of service meshes, many containers, things that need to be versioned independently remain compatible, which is actually one of the main drivers why in the observability industry, we moved from the very traditional, I don't like the word pillars, but the very traditional telemetry types of logs and metrics with the occasional sprinkling of profiling to rather extensive use of distributed tracing because all of a sudden the problem was less often in the single simpler components and much more often in between.

- But this is kind of a funny conversation to me 'cause I don't know if you remember, but 10 years ago we used to talk about microservices as well, but then we called it service-oriented architecture and it wasn't the new cool thing. And then we decided that that was kind of cumbersome and powerful to work with. And we started to merge together our software, again, introduced monoliths.

- But in a service record architecture, we tended to have a very expensive, very large piece of machinery called the enterprise service bus that actually was providing to some extent that kind of visibility that today we need to have through tracing.

- And let's also not discount the effect of the proliferation of cloud providers, because when you have your own data center and your audiences, maybe your internal company or something, maybe it is a good thing to go from one huge complex monolith to three simpler services. But when it's not three, it's like hundreds, maybe then you start needing like another layer to orchestrate and manage and all of the traffic between each of those components. It's definitely not that clear cut to say which one is better.

- I definitely think you're bang on in that case, Nicole, 'cause we've moved from maybe having a couple of software devs for a company that did some kind of HTML that website with some access database backend in the worst cases, right? We now have these huge teams of hundreds of developers that are all working on a compost system together. And having that as a monolith would in practice require us to either do these huge orchestrations of release trains that no one is able to do in a proficient fashion. Or we would have to have downtime all the time 'cause we would need to redeploy everything every time we made a change. So in that sense, it really makes sense to split it up as we grow our teams and we grow our development efforts as well.

- I have a rather, so coming from a very enterprise background I have a rather newest feel to be on the subject. And my take is that usually technological problems are not technological problems, there are people problems. One of the main motivators that was towards going to the extreme distribution of microservices. 'Cause I tried to fight back against the Conway's law. The fact that roughly the architecture of your system mirrored the architecture of your organization. So we said, look, we have all these teams, these pizza teams, it's very hard to make them cooperate to create a well-behaved monolith. So let's give each of them their independent infrastructure and talk over standardize protocols like most of the HTTP and some sort of RPC built on top of it. And that would provide for them a way to be productive independent of each other.

- Exactly.

- As an industry, we dramatically underestimated the cost and complexity that comes from the need of coordination and compatibility and understanding among these teams, because now you no longer have one code base that you can run tests against. You have to have multiple ones that may interact surprisingly at Atlanta. These for example, has led to introduction of contract based testing, where teams contribute to each other interface tests. And there's also the saying, which is something that is a harsh reality that every observable behavior of an application with a large enough user base, will become a dependency for somebody somewhere.

- I think this is the whole premise of Conway's law, right? The idea that our architect, the software architecture or the infrastructure that we put into place in a lot of ways starts to evolve depending on how our team is structured. And I think it's both a technological and a human problem as well. When you talk about coordination between teams or between services, it's really the same thing.

- Yeah. We have made actually strides in how easy it is to make software inter operate with each other. If you go back, we started, we were talking about SOA. SOA came with a curse called SOAP. It was incredibly complicated, mindbogglingly hard to make run at scale. Today, we have a bunch of, so we are using HTP for other things. Sometimes I would think too many, we have good stuff like GRPC, like arrow, a lot of different protocols that can be very efficiently used to either make a synchronous message passing happen or synchronous invocations. We have a lot of tools that in the past year and half, I think we've got the big two trigger happy in deploying a lot of new tools in production. And I'm saying this with a background of someone that fundamentally had to support every single piece of technology that made input or output, for example, on Java. It would surprise you how many different HTTP clients for Java are I think in production, I lost count. There were 50, it's insane. And I'm, for example, you raised your mark right with a very, very beautiful LED and Bluetooth. And it's super cool. I feel--

- I was trying to share something that Simme was sharing there, but I can't actually see it for some reason. Oh, there it is.

- It's okay.

- What's this Simme?

- I love to say, I like to bring out this picture whenever we talk about why observability is needed. 'Cause while it's a lot larger than most of us operate with, and it's still very striking that they think this is supposed to be Netflix's is a microservice architecture at some point, whether it is or not, I don't really know, but it's supposed to be and trying to--

- Can I be trashy? Can I be able to trashy?

- Thank you.

- Architecture has an element of deliberation that they do not believe there's an actual out of the system has, this is an emergent system is a lot of architectures that then meshed into something.

- Definitely.

- It's remarkable that it works so well.

- Yeah. And one of the cool things there, I think is the fact that without observability where this big ball of yarn, it would be completely unfeasible to reason about anything this system is doing at scale. You wouldn't be able to reason about the particular part, maybe that you are working on one of these small dots that we can't even see because of all the lines. But to reason about what it does is as a whole would be completely unreasonable. But with tools like, for instance, distributed tracing, we're suddenly able to follow end to end an action of a user or an agent within this system. That was all I wanted to think of that.

- I love distributed systems, distributed tracing in distributed systems, because it actually gives you the means of answering the most important question or you're faced with an issue, who is affected and how badly? When you go on an enterprise setting and our people are often databases service, your application completely blowing up, could be a drop in the bucket of their system. They will not probably have the central entry you have to have a very different take on priorities unless you have agreed upon a slice on the silos and the failure that you are fundamentally up streaming through your users may not be their concern, but the moment you have the shooting tracing, that goes from the deepest database to the device in the face of your user, yet you have a very clear perception of how bad is something that is the one most important piece of information that you need in front of your face when the pager goes off again at 3:00 AM, you need to decide whether it's time to go on to Batman, or if it can wait until the third coffee tomorrow morning.

- I think that's the real success of the "Squid Game" right? Because that image that you had up Simme, and just imagine that times 114 million users that are potentially using many of those systems, it's amazing that it works at all at that scale, especially.

- Something that always gives me those thoughtful moments of, oh my God, what are we doing as an industry? Is that a potentially simple issues have disproportionate impact on popular services to the life of many, many people. It goes from lack of entertainment. You're there you want to see the latest, "Witcher" episode, cool stuff. You're disappointed if the thing is on top, multiply that by a medium people that cannot get there, there are fix, Hey, you have a significant amount of life around that has gotten worse, but it goes also to something that is maybe much more limited, but much more tragic. For example, when I was working at SAP, one of our customers was, I cannot say the country, but it was the first aid response service of one of the countries. We were scared plus that something so important that either the platform, because downtime would have consistent consequences to real people, something that we have seen recently with the move to the cloud and the disproportionate role that for example, U.S system one has on everybody's life today. We have seen how the risk is getting more and more concentrated into fewer and fewer, very large, very complex, very reliable, but critical pieces of infrastructure, in ways that I do not believe as a society we have had yet. And that is where it really humbles me as an engineer to think, well, this has to work, right?

- Yeah. We went through that in, I think in the last k6 Office Hours, I had somebody from oil funk, who is an emergency services provider in Austria, and it was cool, but also a little scary to find out that they are using k6 for, in part to also handle the traffic from the 112 emergency hotline. So it's cool to see something that you're working on, be used in such a critical industry, right. But at the same time, it's also a little scary because it could actually be lives that are lost if you know, we don't do our jobs well enough, it's a little humbling to think of that.

- I guess the closest resemblance we've had to these critical infrastructures that everyone relies on would it be like the transatlantic Telegraph cable? I mean, that has like in, I think it's currently 19 cables or something like that, that make up the transatlantic telephone cable. But I really any catastrophic failure there would really isolate us in terms of cross continental communication.

- But that is less likely to result in loss of life. Then, for example, your neighbor want service, not being able to follow you.

- For sure.

- I'm sorry for having completely spoiled the mood. I think that as an industry, we need to go in deserve the role of engineers. If we built bridges the way we push software to production, in some cases, I don't think anybody would cross a river without crossing themselves first.

- What's interesting is in that spaghetti soup of microservices that you showed Simme, now we're seeing that our observability stack is part of those. They are also contributing back to the system that we have to monitor. I don't know if either of you saw the post-mortem by roadblocks.

- It was classic. I had ops to them. It's a, we have all been there.

- Yes yes. Do you have to talk about it Michele?

- I do, but I don't think I would be able to be nearly as good as a Simme for this.

- I just came to be honest. So I don't have any detail commentary on that either.

- It was the classic fallacy of oh jolly, oh golly. The same infrastructure that is powering my observability system was probably the system that went down.

- All right. All right. Yeah, that really is something that you'll see a lot. I mean, for instance, say that you have a deployment of the classic Grafana suite somewhere, and you have that running in the same data cluster maybe, or at least the same cloud provider as you have your critical workloads and to make it even worse, you could go down to having it in the same geographic region, or even on the same cluster nodes or the same hardware that you're using for the rest of your critical infrastructure. When something goes south there, in terms of your critical infrastructure, it is likely that that was all will also, as I think, where to kick would roadblock, spill over to your monitoring system. And if that happens, how are you gonna be able to tell that you've been hit?

- This is the classic blast radius question. Everything has failure modes, actually, several of them, and the more abstractions we deploy, the more failure modes we introduce, for example, Simme and I are building an observability system based on Kubernetes natives. Our guidance is if you deployed, deployed to a different cluster on different hardware, because you should never put the monitoring system on the same infrastructure, close to the infrastructure stuff we monitor.

- It's not only that. We also usually recommend that if you deploy our monitoring system, deploy another monitoring system that makes sure that your monitoring system is up and set them up in a, what did they call it? That dead mans trigger?

- The dead man switch is the idea that, for example, do you know in the movies when the hero goes in front of him and says, if you kill me, you will be exposed in two days time. That's the classic deadness which is something that happens unless someone periodically goes there and tells him not to. In this case, in the case of monitoring is unless your system, your monitoring system is telling you that it's fine, assume tragedy. It never goes to the level of a specific use cases, but first of all, you need, let me take a step back. The best monitoring system is the one that tells you whether it's something to look at, right? You actually do not want to have dashboards, however, colorful and beautiful in front of your face all the time, unless it is for Ferguson purposes, you actually want to be able to focus on something else and jump into the action when stuff is hitting the fan. In order to do that, you must have the guarantee that is the easy model of notification. You will receive it because silence, you want to know that it means that it's good. You don't want to have to doubt if there is something going on that my sister should tell me but doesn't, which is why you set up fundamentally a health check thing that says I'm thinking here and all it's fine. That is the diagnose switch.

- I found it so interesting to read through the post-mortem and props to them too, by the way, for releasing something so detailed, they were not afraid to, you know, say what they'd done wrong and what they were doing to address it. I thought it was really well-written, but I want to read one part of it, because I thought it was so good. They said, "There was a circular dependency between our telemetry systems and console, which meant that when console was unhealthy, we lacked the telemetry data that would have made it easier for us to figure out what was wrong. We've removed the circular independency, our telemetry systems no longer depend on the systems they're configured to monitor." I thought that was a great takeaway from that whole incident. And because they've shared it in the post-mortem, they're not the only ones who can learn from it.

- Very generous of them to expose themselves that way and actually left the rest of the industry learn from their mistakes. And so hard work as you said, Michele, our love to the team at the roadblocks who probably need needed a bit of time out after that.

- But there is also another component of a human component here. They did the right thing. They reestablished trust. They are telling us, we learned from our mistakes so that you can as well. In the scope of monitoring systems, trust is the ultimate currency because a monitoring system is literally a measurement system for the health of other systems. If you cannot trust your measurement system, what is the point of it?

- And you usually only get one go with that as well. If you burn that trust, it's gonna be very, very hard to build up again.

- So this is something that touches me very personal because I used to work on a solution that was exquisitely powerful, but therefore also very complicated and complex. And the moment you have automation, someone somewhere sometimes is going to be broken by it. And reestablishing that trust was never easy and sometimes impossible depending on the scale of failure that you're well-intended means of automatically monitoring something I should have brought to the customer. Something that we seldom say as an industry, when we try to sell a product to somebody else, is that everything has a cost. If you want to take away complexity from you to roll out very simple systems and set up that thing, reports stuff over there, and you want it to automatically, there's a higher risk that the automation will cause an issue. Of course, that in many cases is a justified risk. You can roll out the monitoring gradually and the easier it is to roll out a monitoring system at scale, the more you reach the holy grail of monitoring, that is the network effect. The moment that you can start observing how issues in systems propagate, correlate, or are not correlated there is something very important.

- So let's talk a bit more about the characteristics of a good observability stack. We've already mentioned a few we've mentioned that, it should be independent as much as possible from the systems that they're trying to monitor. We've also said that maybe we should also take into account the human side of things rather than just the technological. Maybe you should tailor the complexity of your observability stack to the size and experience and structure of your teams. What are some other things that you both could name in your ideal observability stack?

- One thing that I really like to highlight here is the ease of use or the economics of the system that you are using. I used to do a analogy to how EpiPens work for people with allergies. If you're eating a peanut and you're allergic to peanuts, you don't want to have to assemble the cure for that, right. Or something that alleviates or takes you out of immediate danger. You need it to be simple, just as take it out, push it in your leg, and it's done. You don't have to think about it. The same goes for monitoring or observability systems as well I would say. If you have to, when you're awakened by a notification in the middle of the night, and maybe you're even hung over or worse, and you are supposed to fix something that is critical, and you have to start thinking about what to do, then your observability system has in my eyes, at least failed you, you need to be able to get a notification that says this is wrong, here's the data that proves that, click here to get a closer look and just be presented with all the information you need to be able to make a decent decision on how to proceed.

- One thing recently on that note that I've come across is how potentially easy it is for a new Blake me to set up a whole observability stack or at least monitoring, but he could definitely expand upon it is EBPF, because we've been talking about distribution of systems and also of observability related services, but there's also a trend of going lower and lower level, right? And EBPF monitoring is monitoring at the kernel level, recently with some people from the k6 team, Artem Charlie, Kevin, Danielle, Lopez, shout out to those guys. We did this hackathon project actually for EBPF monitoring. And the whole reason that I got into it was because the promise was you install this binary, you drop it into your cluster on your local machine. And then it just kind of exposes magically all of these things that I normally would have had to set up like node exporters for, you know, it was we're living in a golden age of monitoring and observability I think. The things that are possible, like I can't even keep up anymore, be talking about ergonomics. I mean, what is more ergonomic than not having to do much of anything.

- You are talking about the day one, the fact that it is so easy to set up apart from monitoring system is exactly what you need to be able to monitor at scale. It removes the thought. EBPF is a fantastic technology. We are fundamentally given a virtual machine to run inside the kernel to execute logic, that allows us to do in a centralized place. Things that in the past were almost impossible. For example, the first thing I ever did with a team of vinyl in Stanhope with EBPF was actually to detect how a process that, that was impossible in user land. But with EBPF, it was actually pretty simple. We literally spent more time making sure that the techniques would work across all the operating systems that we need to support and to figure out how to find out that. EBPF the, I see two big potentials for that, for things that are not possible already today with sufficient tips. The first one is to give us a distributed tracing tool that largely independent from their own time. Now there are technology limitations there. It's hard to find out how to trace context. I'm sure that someone somewhere out there is figuring it out as we speak, probably, that we reduce to some extent the toil that is necessary to support the federal fire hose of new technologies, libraries, and stuff like that is put in production every day. But the second one that excites me even more because the shoot the tracing is largely already possible is actually to have cheap enough in terms of overhead and consistent enough across run times production profiling. People look at distributed tracing as a way of figuring out what is slow. And it works remarkably well as long as the bottleneck is in between processes, the moment you want to drill down, why this requests into the insight, this process was taking too long. You see what you're tracing is not so suited anymore. You end up looking at the leaf instead of the forest, because there is so many more requests going on through the system, that unless you have a lot of spans that are very, very detailed and fundamentally to trace threat level profiling, you are not going to which costs a huge amount of overhead. You are not going to have the information needed to find out, okay, good stock in the Dow library again. However, the moment that you have things, basically you have to find out where the CPU, memory or location, memory usage and wait time hotspots are in your application. You actually have the first places to work at to improve the overall system. It's not gonna tell you why that request was going badly, but the moment you saw the hotspot, you are virtually guaranteed that many requests are going to get better. And then you can measure them again in terms of input output, observability tracing. Now people out there are going to say, Michele, what the hell are we talking about? Today we have a lot of amazing technologies to the production profile and they are true because for example, they are right because for example, if you look at the Java virtual machine with, for example, the Java flight recorder, you have excellent facilities with super low overhead to figure out what is your Java or cuddling or cradle program doing true. But they're very specific to the particular run time and to a particular programming language. And when you start comparing what wait time, for example, looks like in Golang as respected over to machine with code routines, instead of, I dunno, loom threads, project loom, and all the rest of the stuff, you end up actually having telemetry that seems to say the same things, but in reality has a different semantic. And that is a challenge in our systems that have more and more grown polyglot. When we had the, our happy little monolith fault, it was one language. Now this year the systems are implementation of many different languages that behaves differently, and yet they are operated in some cases by roughly the same people, for example, necessarily teams, right? Having fluency in terms of performance across several languages is a significant challenge. Now, if we actually get through EBPF production profiling, for example, the folks behind parka and also the folks we have big pixie, there's an amazing job there. If we manage to have something that will give us close enough, precise enough production, profiling information across whatever we may wanna throw into a container that is going to be a generational change in terms of making complex systems run better at scale.

- That's something that we're interested in at k6 as well. I mean, I'm a performance Sesser so the first thing I think of as the network side of it, there are a lot of network metrics that could be gathered at that level. And the reality now is that without EBPF, you're in this position where each new service has needs some other exporter that you need to install. And like there's so many plugins to plugins and many different combinations of things, when really they might all be using HTTP. Like, why don't we have something that just detects, maybe not, it won't be everything right. It's never EBPF has never going to completely be able to, or, well, I shouldn't say never because you know, that could change very quickly, but I don't see it as being the end all be all solution. But if it can provide some of the more common metrics, that's already a step in the right direction. Talk about usability and ergonomics right?

- And also provide a safe assessable baseline across a lot of different technologies working together.

- Yeah. For sure. What other things do you think would you have in your ideal observability stack?

- You asked me?

- Either of you?

- Go ahead Michele, I don't have a lot of ideas on that.

- Well, actually, if you go on the, okay, can I make us most shield for a link? If you go on google, WWW.ubuntu.com/whatisobservability/whatisobservability. There you see a kind of overview of the things that I find most meaningful, monitoring different types of systems. Second, I'm gonna give here that your own.

- They can share my screen record.

- I assume you want this one?

- Awesome.

- Yes. So this page is fundamentally a work of love of Simme and I, about the way we see observe a PVT. And the diagram that you see on screen is a, of course, simplified and very generic can your manage me if I lie, but it is a thirst overview of the kind of telemetry that you use at different levels in your infrastructure in order to monitor things. This is important for filamentary two reasons. One, is to provide guidance for people that may be new to observability in terms of which things to focus first, when you look at the telemetry types that are used on the right hand side, you will see that metrics and logs are of course universal. That's what we started with. They are very good. Every software that deserves to run somewhere is capable of emitting clogs. Most of them can emit metrics and more and more, thanks to primitives that is really proud. There are the metrics sometimes serious thing to the forefront of enterprise systems. It didn't used to be that. Then you start seeing that profiling gets, for example, the moment you move above the virtualization hardware, and you start talking about processes and applications, profiling them makes perfect sense.

- Sorry Michele for cutting you off. But I think you might need to need to explain the icons.

- That is correct.

- That's really. We don't have that context.

- Ah, they don't explain themselves. Maybe then you use amino the icons.

- Yes.

- So the chart that you see on the left hand side is metrics, mentors, time series fundamental. That's what we use to monitor things. There's a lot. Then the table with the reds and greens and yellows followed by text that locks, the old, that bar chart is actually supposed to be flamed charts and that's profiling showing hotspots. The strange thing with all those horizontal bars that is distributed tracing, that is the best way I can come up with to visualize spans. Spans is the basic data structure in distributed tracing. It describes an action taken by system to process a request. For example, you would have a span for the receiver of an HTTP request. The span is opened is created when your HTTP server is receiving the request, it's going to be closed, but it simply is doing amazing things to get to the image in a screen--

- Most of this you've probably seen in your browser, was what I was about to say, like something similar when you browse on webpage, you'd get this span alike view of how the different correlate.

- It's similar, but there is a key difference. One of the key concepts of distributed tracing as coming from dapper, which is fundamentally the progenitor of all modern distributed systems is the parent-child relation between spans, which is the closest you can get to cow's reality. We are, for example, when your application is receiving an HTTP request and is issuing your query to Mongo to retrieve some data, you will have a parent's span for the receiver of the HP request. And the child's span that says, I spoke to Mongo, took me this longer. And this query, I got so many data back that is the parent-child relation. And it fundamentally, you would not have spoken to Mongo if not for the incoming request. Now things get Merck here when we talk about a synchronous messaging, because the beauty and simplicity of the trees of spans that you have in synchronous systems, kind of get lost with a messaging the moment that you have batch consumers. You'll have many requests that result in a whole bunch of messaging being queued up in your messaging queue. And one application consuming messages originated in different traces all at once, fundamentally creating a merge, but I digress. I'm sorry. So we were talking about... I just get so excited about this future tree.

- No, it's great. I know that you said that you have a hard stop and I'd like to get you off a little bit early for your meeting Michele, but why don't you talk about what Canonical has to do with observability at all?

- Well, can I call does a lot of things, including a very beloved operating system together with an amazing community of volunteers, Ubuntu, we are responsible for a huge amount of software. We have offerings for Kubernetes, for OpenStack, for SAF, for a lot of systems that people use to run their applications and data centers. And it is the mission of Simme and I to make sure that those systems come with excellent monitoring capabilities, that you can monitor them with open source software, whether or not you want to use the monitoring system that Canonical provides you. At the end of the day, what we're doing is in variable source fashion. We want to make sure that all the appliances that you can get from Canonical, the SAF, the OpenStack, the Kubernetes is, there are the cube flows and all the machine learning. They are, you can monitor them with best-in-class open source monitoring tools like videos, like getting logs out of SIS log, the security traces with open telemetry, where it makes sense. And that is the part of the work of Simme and I, that is about stepping up the game in terms of making software provided by Canonical observable in a way that you can use, for example, with your existing monitoring system, we really believe every single word we say, when we say the metric, once France, it's all about having radio systems be monitored together. Now, if you do not happen to have a radio monitoring system, wherever monitoring the rest, we can give you one, but if you have a monitoring system and you're comfortable with it, you by all rights should be able to monitor whatever piece of software you get from Canonical with it. And this is what to do.

- That's awesome. I wish we had more time to talk about this, but maybe we can have you both in some future episode, I feel like there's so many things that I wanted to dig deeper into, but thank you both for coming.

- Thank you so much.

- I am so happy. Simme I'm so happy to have you back on again. I've always enjoyed doing these with you, so it's a little bit weird that you're now on as a guest, but I'm happy that you're also bringing things that you've learned at Canonical back to us. And Michele welcome. I'd love to have you--

- Thank you.

- Back again for sure with or without Simme.

- Anytime. But Simme is finer yeah.

- All right. Thank you.

- Sure. Sure. Thank you everybody for watching and I guess we'll see you next week. Bye everyone.

- Bye, have a wonderful day.