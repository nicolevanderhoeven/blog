---
title: "How to design a workload model in k6, with the k6 Developer Advocates (k6 Office Hours #42)"
date: 2022-02-18T18:20:21+01:00
draft: false
tags: ['k6.io', 'video', 'english', 'k6 Office Hours', 'performance']
---
On this week's Office Hours, [Paul Balogh](https://twitter.com/javaducky) and [Leandro Melendez](https://twitter.com/srperf) join me to talk about how to design workload models in k6 load testing scripts using scenarios and executors.

{{< youtube 3AJLSH0Ifm4 >}}

## Transcript

- Hello everyone, and welcome to another k6 office hours. I am Nicole van der Hoeven, and for the first time, all three of us developer advocates are in one stream. Could you please introduce yourselves?

- Oh, who's going first?

- I guess you are.

- All right, age before beauty, as they say. Okay, well, hey, I'm Paul Balogh, the newest DevRel here at k6, nice to meet you.

- And on my end Leandro Melendez, also known as a Senor Performo, very happy to contribute here and bringing, usually it's knowledge, but this time I'm gonna be a little bit on the learning side, which is super exciting.

- We learn together.

- Oh yeah.

- Yeah, I mean, I don't think you can really have one without the other. I think it's super valuable to also just ask questions.

- And Nicole, I'm a little disappointed that you don't have a fake mustache to support Leandro and I.

- Yeah. That is not something that I just have lying around, unfortunately.

- We may have to fix that. I was commenting the equivalent here in Mexico is the unibrow.

- I could potentially draw something on my face, maybe, I could try that.

- Is that the Frida Kahlo?

- Oh yeah.

- So, Leandro and Paul are relatively new to k6. I think you both have been here for less than a month.

- Just a month here.

- Oh, just a month now, that's awesome.

- Three.

- But this is the first time, I've been here with you with each of you separately, but this is the first time that all three of us are here. It is pretty cool, welcome.

- Exciting, hopefully it's not overload for everybody watching.

- Yeah. One thing that I wanted to get out of the way is that we have a very awesome community, we have several community champions, but one of them, NaveenKumar, just posted a couple of videos on how to use checks and thresholds in k6. So I'm going to put that in the comments, as well, because I thought that they were pretty awesome videos. NaveenKumar has a YouTube channel where he goes through a bunch of different tools, including k6, but also like JMeter and Gatling, and he always does a good job, so check those out. Oops, I actually didn't post his videos, I think I posted the documentation for what we were talking about, so that's a little premature. Sorry about that, let me put the actual links this time.

- Well, this is a live podcast.

- Yeah, obviously. Sorry, you get what you get. So if that hadn't already tipped you off, what we actually want to about today are scenarios and executors in k6. You may have been confused by the thumbnail because it was like, I realized afterwards, that it was the three of us, our photos, and then the words executors in k6.

- Here come the executors, the three of us.

- I guess that's our new name or something.

- You know, if you invert the k6 logo, it almost looks like a guillotine, so maybe we are the executors.

- Oh, okay.

- I had not noticed that.

- That's a little morbid.

- Oh, you know, hey, I do what I can.

- You're going like play Beatles songs backwards and all that type of stuff, man. I'm sure it was not on purpose.

- It looks like we've lost access to LinkedIn for some reason, but, oh well, this has happened before. Thank you, Mark, for saying we're killer performance engineers, love the pun. So the reason that I wanted to talk about this was that, I don't know if you also have got the same, Leandro, Leandro and I were both in the Automation Guild 2022. We both had a talk there and there are a lot of common questions that come up with regards to load testing. And a lot of it has to do with the results, specifically when, I'm not sure if you can actually hear the wind in my background.

- Is that you, oh wow.

- Are you okay?

- I'm okay, but apparently there's a storm that's in Northern Europe.

- I was gonna say, hopefully you'll still be in Kansas, right?

- I know. It's like 140 kilometer per hour winds.

- Don't end up in Kansas.

- But can I be the straw man, at least, in this Oz thing?

- Sure.

- I always liked him.

- I guess I'm Dorothy. Or the wizard.

- I ask Toto, please.

- I've got Toto around here somewhere, let her in.

- So one question that I was getting a lot, or I saw other people talking about variations of it, was the situation where you might have already run your load test and seen all check marks and everything passed, and the response times were within the expected results, and yet when the application goes live, suddenly there's all these errors, and performance issues, and maybe production incidents that you never saw in any of your tests. And the question is, how can that be when you've done your testing and you didn't find any of that and you only see it in production?

- Yes, of course I experienced that several times, but many things come to mind on, in what environment did you test? What happened in this environment? If you test in production, hopefully 'cause we are modern performance engineers that are not afraid of testing in production. Settings, changes, what was the workload? I mean, I don't know, the list is pretty long.

- Yeah, there's a lot that, that could, that's why that question is hard to answer because there's no one answer. It's like, oh and that happens, always check this. And that's also because it could be that there's something different with the environment. Like maybe it's you didn't test the same version of the code even, or maybe you were testing in not a production-like environment in terms of size, or test data, or something like that. But another reason that I think is easier because we testers normally control it is on the side of the script. It could be that you weren't testing the things that you actually wanted to test. And a big part of that, I think, is workload modeling.

- That's one that I also wanted to comment, 'cause that has been a pain in different occasions. On one hand, watch model, 'cause from what you're saying, there were these projects where in the end we were told, hey, this is a workload, this is a utilization that we are expecting to have in production or that we actually have in production, we want you to test for this. And it was nothing like that. We were told, yeah, it's a thousand clicks per day, but you wanna test an emergency center when there's a tornado. How is that true, how is that relevant, or vice versa? For some reason, our scripts are just simulating a thousand clicks per day where it's 10,000 billions, gazillions, what would've been the right thing. Of course your performance test is gonna be awesome if you underdid it. And the other side of the risk, everyone running and, like, the system is dying, what is happening? Oh, we're pressing it too hard, sorry, our bad.

- Yeah, that's true, could go both ways.

- But definitely you always have to worry about configuration drift anyway. Differences in your environments, unless you're using something like a terraform or something, infrastructure is code where you can make sure that your environments are equal. So if you do your load testing and performance testing in a lower environment or isolated environment that it gets some of that, that it is truly configured the same.

- Yeah, even when the environments are exactly identical, though, let's just say that it's possible to say that, yeah, there are still situations where if your load tests weren't simulating realistic enough load, then you can't really, you may not be able to apply those results to production either.

- And one thing, as I said earlier, on one hand, the problem to getting those realistic numbers, at times, the team doesn't even know, they have no idea what are you asking for. All they know is we want to be able to handle 10 users in the system. I'm kind of simplifying it, usually it's 10 billion users or something like that, right. Okay, 10 billion users, what does that translate into in terms of utilization? And they go like utiliti-what? And that's the first struggle, right. Supposing that you get the right numbers that you know exactly how much to stress each thing, 'cause there there's another differentiator, right. We get this action a thousand times, okay, but to get to that action at times or on some systems that are the same, you have to do others many more times, less times, and they are just telling you about this one. What is the proportion, how much to stress the other one that the other one does need not that many times? So that's one discussion. If you get the numbers right then to landing it into the script and your scenarios, also, it's a very interesting situation, headache-bringing situation at times.

- I think part of the problem is that a lot of times, when we think about load testing, there are only a few parameters that we think about immediately. One them is the number of virtual users. Another one is the test duration. And sometimes you might get like a request per second, like you were saying, Leandro, but those three don't really describe the shape of a load. It's kind of like trying to encapsulate test results into an average figure, like when you get the geometric mean of something, it's not a great way to express the distribution. You know, if you say that the average response time is three seconds, that doesn't mean that you don't have really high response times. Like you could still have a handful of requests that are at 15 seconds, but maybe the rest of them are a hundred milliseconds. It doesn't really

- There is context.

- Accurately describe the whole context, the big picture of the load. And in the same way, things like the number of virtual users, and duration, and requests per second also don't show the entire picture.

- Yeah, wen you're describing it that way, it makes me think when you are asked to describe someone, oh, has beautiful glasses. I mean, I was talking about Paul, sorry, Nicole.

- Oh, sorry.

- No, no, I like your glasses, too. But you need a full picture, right? There are so many elements that a scenario or a workload model includes, so many variations, details that, yeah, as you were saying, I need 10 million users in the system doing what, how often, how long, how many of them are doing which ones? And many of those things, you have to get into the weeds to truly understand and design 'cause this is another one, you will want different workloads for different type of load scenarios. You should not, I was gonna say you cannot, but you can try, but it's not recommended at all to try to kill too many birds with a single stone. You may be able to get two, but more than that gets complicated, gets crazy. So you have to create a work model for that specific risk situation, that scenario that you want to test for. Just one at a time gets challenging, getting all those components, all those items and things that you need to be careful putting together to model and simulate something that resembles realistically that risk scenario, that risk circumstance that you want to test for.

- And here you go again with that killer mentality there, killing multiple birds with one stone. And now Mark's making comments here that actually for killers.

- Okay, okay, let's say you may be looking for a needle into multiple haystacks, no killing.

- There we go.

- I was thinking about what you were saying about the hypothetical scenario of a thousand requests over 24 hours. There's still so many ways to interpret that, right? Because it could be, one interpretation could be, take a thousand requests divided by 24 hours and that's the amount of load that you want to test with a one-hour load test. It could be like that, but if it's emergency services, there are certain times of the day when emergencies are more likely. It could be seasonal, as well, like the incidents of emergencies of ambulances that are sent out increases over the holidays for inexplicable reasons. That kind of thing does give more context than just a thousand over 24 hours. I mean, if you just look at a period of 24 hours, those thousand could have been simulated, could have happened in one hour for all you know.

- Step in a little far from the ambulance example, don't wanna go more on the killer topic. Let's think of a restaurant, if they say, this Golden Arches restaurant, we sell a thousand burgers per day. Okay. Most probably you are selling 80% of that at lunchtime and the rest of the hours we don't care about. So those different behaviors during that period of time is what we should focus on, or care for, or have better information. Well, in the morning you get more, what's the name of the thing, hash Browns, no burgers. Even if you are the same restaurant, which one do you want to simulate? What is the utilization at different periods in time during the day? 'Cause yeah, probably no one, not that many people get a milkshake in the morning, but most of them getting in the night. So some of those variations, you want to make sure that you are doing the right mix, not only how many at a single number per long period of time, what happens each hour of the day, which ones do you care for. As a restaurant, I would say I don't wanna simulate a load test of, I don't know, after lunchtime where everyone is gone and we are super quiet. I don't care load test-wise, right. But lunch time, breakfast time, I don't know, 7:00 AM in a gym, I want to test those type of things of what people are doing and focus on, get a good work load model for what is happening at those times, right.

- So I thought, Mark has a couple comments here. I think also the number of vusers or threads compared to the target arrival rate or expected response time for me is the health of the workload generation. And he follows up with, also synchronizing or rendezvous vuser requests is underused in my opinion. Do you agree, Leandro.

- Well, it's in my personal experience, there have been a few times, at least on the render view or synchronizing part, there are not that many times where I had to leverage those functionalities. I think it kind of depends on the projects that you work on. One that comes to mind, and I really love this example for workload modeling in general, is I worked at a gaming company, Australia's largest gaming company, and the project that I worked on was for the Melbourne Cup. So they sold tickets for the Melbourne Cup. And if you don't know, and probably you don't unless you're Australian, but the Melbourne Cup is a horse race. It is like a two-minute horse race that is for some reason incredibly popular in Australia, in my state, in Victoria, 'cause I lived in Melbourne, we actually got a public holiday for it. So, it's that big. And for some companies, for a lot of these betting companies, the revenue from that one race could be up to 80% of the entire year's revenue. So it is that big.

- Just in that two minutes.

- Yeah, and that's the thing. Betting is open until the race starts. And yet when you look at the workload model for that, it really, the load spikes, the betting spikes just in the few seconds before the race. And that's for a number of reasons, people might not have had the chance to bet earlier in the week because they were working or something. And if you have a public holiday, then you do have the time to just be there watching. And also there are, depending on the types of bet that you placed, there could be a difference in odds. So they're trying to get the last possible information that they can before they have to make a decision about which horse to back. And that's a good case for a rendezvous because there is a clear cutoff and sometimes you see the reverse, like for example, in a university portal or one of these shopping sales, where at midnight all the sales go live. And so you get people maybe refreshing that page all up to that point and then, bam, all of a sudden they start checking out things. And that would be, I think, a good time to use rendezvous.

- No, and in a quick example, you got me thinking, as well, video gaming, when you are on these multiplayer games, most probably everyone watching this are familiar, campaigns, online campaigns, certainly there are so many things happening, there are people playing other things, but a campaign is gonna start at this moment, this schedule. I think there a rendezvous would be a very good use of those type of things. Sadly, in my experience, some of those situations were solved with a spike scenario run out here with an average day in production, so overlapping scenarios. But that's interesting 'cause, as well, it depends on how do you want to tackle that problem. We are going to have a normal day and suddenly something's gonna happen. How do we simulate it? How do we model that workload? What tools do we use? That's a very good point, and again, with performance testing and load testing, there's no one size fit all or the way to do everything. No, it depends, and you can get two very similar loads, simulations, workloads with different approaches, with different things. And that's one that I also wanted to mention, like when modeling, it's something that when you wanna try to get, there are two elements that I like a lot and I struggle a lot of times, when you are modeling your workloads, you have to somewhat randomize the actions. A big thing that we used to leverage in the load runner days was randomized think time in between steps. But eventually you have to say, okay, it's randomized, it's happening, like real people is using the system, but in the end I want just this process, just this virtual user to iterate a thousand times in an hour. Oh, but I have random times in between, okay let's, that modeling, as well, I can tell got so interesting. And even like mathematic, not too complex, but mathematic functions like, okay, over time we have this deviation, if everything goes in the higher random wait time, we may get up here, we may get down there, so on average we'll be simulating this. It's all so challenging.

- Yeah, those delays are definitely part of the workload model. In k6, we call them sleep. In JMeter, they're timers. LoadRunner is think time. There are a lot of different terms for it, but basically a delay is some sort of planned sleep in your script that is meant to simulate a real user maybe taking time to think about what they're going to do next, or read the text on the screen, or type out something in a form. And it actually can have a pretty significant impact on your load tests. First of all, if you don't have any think time at all, then you need to be careful that you're not maxing out your CPU and memory utilization on your load generator because that situation where you're just very quickly firing off requests may not be entirely realistic. And I think that if you have think time that's always the same time, like this is what you were talking about, having dynamic ones, if you always use the same value for your think time, you might see the staggering in your results, but that's due to how your test is set up and not at all to do with how your application is responding. And then if you use dynamic think time, like you said, it can make it harder to plan because it's more difficult to know exactly how many iterations your test is going to complete. So there's always trade-offs, right. There's no one way that's always the best way.

- And it depends, as well, on what are you actually trying to simulate. As you mentioned, there are times where we put think times that want to simulate a real person using the system. There are some others where you just don't want these events to happen at the same time. To give you an example would be like if your script was a soldier marching one, two, one, two, and you're adding soldiers at the same pace, one, two, eventually they all will be doing the same step at the very same time. If you are simulating a military parade or something like that, that's awesome. You have the test. On that time, you may want that to happen or, or work it out with some rendezvous continuously happening. But if not, if you just want to simulate a regular march or people passing in the subway, they are not like one, two, one, it would be very interesting to see, but that's not how real people walk in the every day. There are situations for everything, and it's challenging at times, as you say, not only wait in between steps, but waiting after you complete a cycle and you want to start another one. There, you may also want some randomization or not to be that static so that your generally load simulations do not have to be that robotic, even if they are done by robots or virtual users. So there are several trade-offs.

- I have an extension to your metaphor, I think you'll like, Leandro, what if instead, this is a way that your script might change depending on the business processes and the context of the industry. So what if instead of trying to simulate a military, what you're actually trying to do is simulate Fremen running across the open sand, trying to not have patterns in their steps to avoid attracting Shai-Hulud, the great worm. If you don't know the reference, I'm sorry. But in that case you do not want anything constant. You want something more dynamic, something that isn't easily noticeable, that won't skew the results as much. Oh, we have a question from ChipsAho. I don't know if it's just the Filipino thing, but there's actually a good packet of cookies that's called Chips Ahoy.

- Ahoy, love them.

- If you are faced with budget constraints, how would you prioritize the workload model to use? That's really good. And they follow up with, as performance engineers, I know sometimes our curiosity tends to get the best of us, trying to see how the system behaves in different circumstances.

- Well, answering to, oh yeah, ChipsAho, is from Ahoy, very good cookies, put 'em in the microwave eight seconds and you'll love 'em. So it depends a lot, I would say, and your budget constraints, what are you testing would be my question. What risks does your application will face, or what are the most common reasons? Again, there's no silver bullet or single test that will clear all your performance risks ever again that you may have under loads. What loads were you? What things may harm your system? Those are the ones that you need to focus and prioritize based on that risk. If you already tested one, you know that it'll survive, next test, maybe go to the next one and down the ladder, the risk ladder. But first it depends on your system. What is it going to subject to? What are the processes? And the risks may be different a spring ago from today. You may be releasing a new process that is super critical, super dangerous, will be touching databases or doing important or even dangerous queries. This time, you may want to focus on that one. There's no one test to rule them all, one workload scenario, so it depends.

- I think there are a few things that I would think about first. What is, like Leandro said, what's the biggest risk? Meaning if there's something where if you don't load test this component there might be security implications, test that. Anything that's critical, like payment or something that might affect compliance regulations for whatever industry it is, meaning like how you handle individuals' data, potentially identifiable data, that would be worth load testing. And also anything that's very public, so maybe something like you're about us page is nowhere near as public as your homepage. It can deal your company very significant damage, but hard to quantify damage, in terms of reputation, if your entire homepage is down, rather than if your about us page is down. So that could be a situation where something is not really mission critical or important to the business functionality, but it still would deal a lot of damage. So that's a lot of reputation risk, I guess. A question here not about executors, but we can quickly talk about that. Do we get any performance HTML report in browser k6 load testing? Not yet 'cause this person specified browser. So I don't think that we have that yet for browser, but there are a few extensions. There's the xk6 dashboard one by Ivan Skiba. And there's also xk6, what is it called, xk6 HTML report or something like that. Go have a look at the session that I just had, the show that I just had with Paul last week, actually, where we talked about this very thing. They're both extensions and they're both awesome. They give like a, the Ivan Skiba one, I think, is the one that you did, Paul, right?

- Yeah, and actually I was gonna show that a little bit later here.

- Okay, all right, well let me know when you want to.

- Stay tuned, yeah.

- We might as well jump into that, 'cause I definitely want to show some things about how to actually implement these workload models in k6. So one way that you can do that is by using scenarios. So I have, let's just start with this one. So I have one script here, it is a protocol level script. And I'm just putting it in a separate JavaScript file just so this is a little cleaner to look at, so that we can focus on the scenario. In k6, we have something called scenarios that are ways to set things that run independently of each other. So you can have it be consecutive, or run one before the other, or you can have them run simultaneously. So this one just has, this example that I've got up now is just one scenario and it has an executor. So let's talk a little bit about executors because this is something that's specific to k6. So let's look here. An executor is basically a way to change the way that the load looks. There are a bunch in k6 and I'm actually going to, I already, 'cause I get this question a lot, I'm going to put this in the chat because I have this cheat sheet for how to go about thinking, deciding which one to use. So I'm going to post it in the chat and we, I think that the rule of thumb is if you want to just try one, you can, or you want a simple one, it's probably ramping-vus that you want. And that's because this is the default one and a lot of load testing tools where you set the number of virtual users and duration and then sometimes you might have stages. This is also what k6 defaults to. So let's have a look. This is what that looks like. As you can see, I have ramping-vus set here, and this is a way to change the load depending on the number of virtual users. I also have these stages here. The first one is kind of like, I was trying to simulate a ramp up. So from when the test starts, this will start with zero virtual users. I've got that set here. And then it'll gradually ramp up to 10 over five minutes. This is shorter because I think I was trying to, this was from a demo, so I was trying to make it something that we'd actually get results from, but this could be, you know, 30 minutes, if you wanted, depending on your test. And then this is kind of what we call steady state, where the number of virtual users doesn't fluctuate. It's just holding steady for this period of time, in this case 10 minutes. And this last one where it goes from 10 virtual users to zero is reflective of a ramp down. Paul, did you want to share your screen 'cause I know you said you had some things in cloud to show us.

- I did, yes. And then unfortunately I wasn't able to share for my script, there's something going on with my system here. But let me go ahead and share my browser, which is working. So yeah.

- Awesome.

- So this is a script that I had done and what I did was, as I was trying to go through and then figure out all these different executors, I wanted to see the pattern that each of these executors applies. So now here, let me, maybe it's better if I start down here. So this is the actual script that I executed. So if you look here, you'll see that in these scenarios and hopefully, let me see if I can.

- [Nicole] Yeah, I was just going to ask.

- [Paul] A little bit more legible, there we go. I'm not the only one that may have old eyes and just can't see. So I loaded up the options so that I would have all these different scenarios. 'Cause I wanted to see every one of these executors and I wanted to be able to see what kind of pattern that they applied. And originally you'll see that some of these numbers are a little bit different, but these are all the very specific things that each one requires. So in this case, the shared iteration scenario, and again, I'm not gonna be the expert on what each of these different executors provides, but they're in the docs. So yeah, we can go through there. I'm gonna be working on these docs, as well, in the next couple weeks and try to clean these up a little bit more, maybe make 'em a little bit more, I don't know, state it a little bit differently or to help my understanding anyway. But yeah, so I loaded this up, so I have each one of the different executors set up. So here's the ramping, so similar to what Nicole was talking about with the different durations. So here over a ten-second period, I had it ramp up to, I think, from zero to 10 vus. And then for 10 seconds I would have it keep going at a level 10, so it would be a flat top. And then the last 10 seconds would be ramping down to zero. All these other ones here, too. So, I put every one of these in there so that way then we could go ahead and compare them and, whoa, let me, all right. So each one of these is kind of denoted here and I guess I can't, I wish I could isolate these and then what's really, I guess, the most important here is the purple line and hopefully you're not, no one's really color blind or missing the color differences here. But yeah, so the purple line is the actual number of the request coming through. And then this blue line, or the aqua, is the actual response time for the service. We'll just kind of focus on the purple line that's what these executors are really affecting more so. And then the gray line, this shaded area is actually the virtual users. So you'll see that here it started at zero, and then it ramped up for a period of time, and then it started kind of flattening, and then it would ramp down. Now this is for the accumulation of all the different executors. Unfortunately, and this might be something I might put in as an issue to possibly add or an enhancement is that each one of these lines here is a scenario. So this actually has the shape from that particular executor. So it'd be nice to show the vus in here, as well, but you can kind of infer it based on the activity, the request. So again, that's the purple line again. And so here, you see this executor actually ran pretty quickly to get to the number of requests. I was trying to keep them about the same because I wanted to do, like, a progress bar race. So when I was running this locally, I could see the different areas in which was actually completing the same number of requests faster and all that. But yeah, so this was kind of my playing around and, again, this is on the cloud product. So this is an add feature. But now with talking about the HTML reporting, this is what I actually did here. So let me go ahead and I'm gonna go ahead and run this script again. Now unfortunately, you're not gonna be able to see the actual execution as I run it locally, but let's see.

- [Nicole] Paul, we got a question about the k6 cloud results that you were showing. Could you create a shareable link so that people can also have a look at it?

- [Paul] Well, let's see. How can I do that?

- [Nicole] You can go to the three dots in the upper right. Yep, and then share test results.

- [Paul] All right.

- [Nicole] We can just copy and paste that into the chat.

- [Paul] Cool.

- [Leandro] And then they are out into the world.

- [Paul] Out into the world, yeah. Awesome, cool. See, today I learned again.

- [Nicole] Yeah. Awesome. I'm so glad you did this, though, because I wanted to, but I didn't get around to doing it. So I'm really glad you did.

- [Paul] Yeah, and then I wanted to actually have them separate so I could kind of show each one's pattern again. That's the thing that I was really trying to get to, and I'll probably put together a blog post, so keep an eye out for that, where I'll kind of go through that, and describe, and show patterns that are created by the executors. And then that is as I learn more. Again, so this is, this dashboard that I'm showing here, this is actually an extension. So I did compile this into the k6 binary, custom with this output. And this is available here. This is this xk6 dashboard, and this is also included in our registry on the site, so you'll be able to find this as well. Pretty easy to do this, the xk6, to create the extension and build it. But anyway, we can always give help. Anyway, I'm gonna go ahead in this other window, and I'm gonna go ahead and start this test running. So now as we see here, and I shouldn't have to refresh, but let's see, go ahead and refresh here. All right. So now this test is running in the background. And then we should start seeing the output. There we go. Now, there is a delay. So behind the scenes, this is actually using, it's creating Prometheus-based metrics and then it's serving that up in a little web server locally. So it's really cool. So I haven't been able to play around with it nearly as much as I need to, but anyway, but this is something, it's a nice little tool to be able to use if you don't want just the plain text display in your console. But yeah, so this test is actually already completed. Now, it's actually still running in a way, though, because we have this externally controlled executor where now from another terminal I could sit there and I could say, okay, yeah, now I wanna ramp up the vus to 10 or that type of a thing, just via rest API. But unfortunately, due to technical difficulties, I can't show you that, but I will definitely put that in the blog post when I start putting that together. Anyway, this is one of those cool little tools with this extension that you can kind of, I don't know, really get some cool results. But yeah, that was the big thing. Here's for the external access, this is the rest API where I could sit there and call that custom executor and say pause testing or even to ramp up the number of vus. Still figuring this out a little bit. It's a little, I don't know, it needs some play around with it a little bit to get a good understanding of it. But yeah, I wanted to show that, again, you can do this stuff, have the graphics there. Now, the HTML report that Nicole was talking about, that's something where, yeah, you could save that off, and again, it doesn't have the graphics, I don't think, if I remember correctly, but it does have it where you could then save that off.

- It's not real time either. But it is more like a report.

- Yeah, yeah. That's it, let me go ahead and stop that test. Oh yeah. So again, I will put together something so that way then if anybody wants these details and obviously you can use that link, so it's now shareable, so I will make sure to not delete it .

- Great. I do want to share something, Paul, if you're okay.

- Yeah, absolutely.

- Great. So I also wanted to talk about the fact that we can do it, you can put together a scenario using different executors, but another thing that you could do is have each scenario be a completely different test. One could be a load test. Another could be a chaos engineering test, for instance. Like this is one that I had where this get Pokemon is an HTTP request that just hits the API. And this is intended to be more of a load test, but then you could have a chaos scenario and you can say that at a certain point, you fire off this thing that then terminates one of the pods in Kubernetes, according to certain conditions. This is using the xk6-chaos extension. But in this way, you can see that these are not just load-testing scenarios. These are just testing scenarios and they're different types of testing that you could use. Another type other than chaos is browser testing now that we've got xk6 browser. So now you can do things where you have one scenario that's doing some sort of protocol level test and the other one is doing a browser level test. And because those two are fundamentally different, you may want to be able to control them separately. You probably won't be wanting to generate majority of the load with a browser level test, for instance, you probably wanna do that with your protocol level test, but you might want to piggyback off of the protocol test and run a few, like a handful, of browser users just to be able to get some front-end metrics. So, I think it's kind of cool that you can do that. Another thing that you can do with scenarios and executors, well, it's something with workload modeling anyway for k6, this is a script that I've got for percentages. Now, I think the use case for this, I mean, there are a lot of use cases, but what I actually think this could be used for is an e-commerce scenario where a typical scenario is to have like 100% of the virtual users go into your homepage, and then maybe 50% of them go and browse through the product pages, and then of that 50%, maybe only half of those actually added to the cart. So that is also something that isn't directly related to scenarios and executors, but it does have something to do with the workload model of your test. So in this example, I'm setting a random number between one and 100, and then depending on that, I have this combination, in this case, I'm setting different clients for it. So let's say that there's a really big client that we want to use 50% of the time, you could use that, and then pass that on to some request that you're sending. And in this way, you're already making something that's more realistic than just get a client, just get details for a client. Well, which client is that because maybe that's being cached? Maybe you do want it to be cached, you'd have to see what you want, what you're trying to achieve with that particular test, but it all has an impact on your testing results.

- Yeah, and if I may add for learning some of these functionalities, it makes, and I think I started a comment how the situations, how the ramp-ups work, how when we want to model these targets in the old days, as I said, getting these, okay, my user takes this amount of time of execution, it has this amount of random timers, and it's a pain at times when your process starts to degrade a little bit of performance, and because of that, they don't go as fast as you need them to, as you want to generate, because you did the calculations based on optimal response times, right. So some of these controls will be very useful depending on the scenario that you are wanting to focus and not to do all that type of crazy math that we had to do. I remember with the load runner days, it was like, okay, but if the response time starts to deviate a little bit, this we need to, there's so much that on this situation with some of these options, k6 can mutate may be the wrong word, but adapt to what you're trying to do, right, and keep doing the loads and doing those processes that you are aimed for. There are some others that you are like, if the system starts to go slow, the users will slow down and that's right, that's okay, that's normal, but on others it's like, no, I absolutely want that the users keep coming, keeps hearing the system, even if the system is slowing or many other things that can start to happen. These controls truly make our lives easier. in so many of those situations like crazy.

- We have a question from SJ who says, is there a pacing config in k6 or maybe a throughput controller equivalent? So let's talk about pacing, Pacing and load testing terms is related to think time in that it does impose some sort of timing on the requests, but while a think time is more like a direct sleep on a thread, pacing is more like the space between each iteration and there are different ways to achieve this. k6 doesn't have something that is exactly pacing. But for instance, the way that JMeter would do this is by using the throughput controller, which is what I think SJ is alluding to. And so instead of specifying the time between each iteration, JMeter does it by allowing you to set a target request per second, some sort of throughput. And we do have that. Let me just share my screen again. So this is the executors that we have. And I think this constant arrival rate would be the best for that. Because if we look at the example here, you can set a rate here, a requests per second, that is your target. What k6 does is it sends a request or it does one iteration, sees how many requests were sent, and then adjusts the next one, waits a certain time so that before it does the next iteration to adjust to that. So if it already did, you know, 200 requests per second the first iteration, then maybe it'll just do the same thing for the second iteration. And it will dynamically change throughout the test. So maybe at the beginning of the test, response times are faster because not all the users have ramped up yet. In that case, the pacing might be slower because there's no delay on the server side. And so the script is easily hitting the 200 requests per second, but you'll find that later on throughout the test, you may experience higher response times, and in that case, the pacing will be quicker. So that number will be lower so that it still reaches the 200 requests per second.

- Yeah, it's part of what I was mentioning that easiness of. JMeter, I remember before they didn't have that plugin for the throughput, what was the name, I just forgot about it. At the very first times that we started to use

- Throughput controller.

- Throughput controller, thank you. We didn't have those type of controllers, ways to managing them. And again, bringing the load runner days, I don't remember many useful devices to go through this. And on this case, when you have a scenario that at times when we were designing this workflow, this scenario, we would know, okay, I know that per user, I want that in an hour these many iterations happen. So if you want that, you can use the per vu iterations executor that will help you to quickly configure and manage that, you do have the iterations per user, and maybe you have 10 users, 20 users, you don't care about the number of users. Then you select the shared iterations. I just need this throughput to happen this number of times in this period of time, maybe next time I will have more virtual users, maybe next time I will have less. So you have more control on the end game, to call it in a way, that you're looking for, rather than, and I cannot say this enough, it was a struggle to try to control, and simulate, and reach those goals that you were trying to get in your simulation, and there are so many reasons, as I said, the wait times in between steps were randomized before, as Nicole says, you have the pacing times in between each cycle, and it was so many, like three factors, main factors, I would say, wait time, pacing time, and processing time, each step would add up to that time that there are so many variables that were somewhat random that you could not control. So here you would have some assistance, some help on hitting those goals that you're trying to simulate and having it realistic or on the goal that you're trying to reach, right. It's that difference, I don't know if anyone has gym experience or has ever visited one of those things, but they will tell you, hey, I want to work leg today. Okay, do five repetitions three times. That's if you wanna think of that, how long do you take and do each sit up to go, to give an example, that will be your think time, your wait time in between steps. Okay, you need some rest time before you do the next one. That's the pacing. So for the ones that are not so familiar with those terms, just wanted to throw out that silly example.

- It's one of those things I'd like to, I don't know, I keep thinking of playing around with, you know, if you look at say HTTP audit logs or something like that, they have a timestamp on there as far as when everything came in. Well, if you take that and use that as the basis to basically replay your activity, I don't know, that's one of the things that I keep thinking about, that would be cool to do, or to have, you know, all your activity going into Kafka, and then being able to repeatedly replay the exact same, perfect storm scenario without having the randomness injected in there. I don't know, I'm probably going off on a tangent, but that immediately made me think of that, though. It's like this is one of those things where it's like I always kinda wanna play around with this idea.

- I think that there's a time for that. I think there's a use case for it, but there are also some disadvantages, I think. that people should be aware of. If it's information from a production environment, there are potentially security concerns there for using a user's data to test or a user's account to test. And what happens if that actually gets replayed on their account, which it could be, it, it might not be. Sometimes it doesn't work, sometimes sending the same request, even if it's exactly the same, won't work. I think that that's, I think, more experimental, I guess, when you don't really know what you're looking for and you're trying to narrow it down, but I also think that once you've narrowed it down, it's probably easier and cleaner to script it up so that you can consistently reproduce that scenario. And you can also use test data. Also, you'd be able to kind of break it down, you'd control all the variables, so you know with certainty that when there's only one thing that changed and it was a negative result, then you know that that was the cause of it. But yeah, I think that there's a valid reason to use that, as well.

- Yeah, there's definitely data sanitization that you gotta be concerned about unless we're replaying activity on Leandro's credit card, then it's okay.

- No, please don't. Oops, there are 10,000 charges per hour in your credit card. What?

- Load testing your credit card. Navin Kumar, whose videos I was just plugging at the start of this has a question.

- Very good question.

- Can we intentionally include sleep time in the response time? Now, Mihail, who's one of our developers, if I say something wrong, tell me in the comments, but I believe that there isn't a way, that there's no k6 specific function to do this or option. What I'm thinking of is you could create a custom metric because you can create really a bunch of different metrics, counters, and timers, and gauges, and whatever in k6. So you could definitely do that and have that reported and you could set the timing manually, as well. Another thing that I'm thinking of is if I had to do this, I'd probably just use the xk6 browser extension, because that's already going to include everything, the actual render time. 'Cause now we're getting, if you're including the sleep time or the think time, this is more like getting into the front-end performance side of things and I think it might just be easier to do that.

- That was gonna be kind of a question that I wanted to do, too, Naveen. Like why do you want to include the sleep time programmatically that you are generating in your script? I mean, as you say, Nicole, the front end is important to know those render times, those wasted moments in the response or back-and-forth communication, but what are you trying to use it for? It would be very interesting if you can share it. I'm curious what's the use. Oh, okay, you were just being creative.

- Yeah, I think that, yeah, probably if you want to just see front-end experience, I do think it would be more useful if in this case, if you're including it in the response time, then maybe have a constant sleep, actually, because then it's consistent because you don't want the sleep to be influencing your results.

- I did use something like that a long time ago, but precisely to model this workload to calculate. I generally recommend do a small-ish version of the load test that you want to do, let it run for a while so that you can massage those values of how much random time to sleep here, how much random pacing you have here, and how is the response time affected so that you can balance it out. That could be an interesting use, real-life example, but that's a good question, as well.

- I mean, injecting a network latency and things like that is always a nice thing for backend services. I mean, with microservices, because one single API call on the front end could be going through 10 different microservices ultimately. And to be able to test something where if halfway through those calls if you have a network hiccup where one of the services is not accessible, but it's, anyway, but it's all one of those things where it's like this feels a little bit more on the chaos engineering aspect of things, you know, how is your application going to behave when something goes wrong? If all of a sudden your network grinds to a halt where it's going really slow, is your application handling that scenario appropriately?

- Okay, and on that note, we are actually a little bit over on time already, that went by really quickly. Thank you both for coming and for sharing your thoughts on these topics and also for demoing the k6 cloud stuff that you already had, Paul. Yeah, you are welcome back anytime and I hope we do this again. And for everybody,

- I thought that was the last one.

- Oh, well, sorry to disappoint you. You're stuck now, like you've signed the contract, that was it. You didn't read the fine print. Must come to office hours every Friday.

- This would be the last time that you would want me on here.

- Well, for those of you who are watching, thank you for watching. Thank you for all the awesome questions we got this week and have a good weekend. And if you are in a place where it's very stormy, good luck, hope we all survive it.

- Stay safe.

- Bye everyone, have a good weekend.

- Take care everyone, adios.