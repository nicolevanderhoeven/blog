---
title: "Postman for load testing using k6, with Tim Haselaars (k6 Office Hours #43)"
date: 2022-02-25T18:00:11+01:00
draft: false
tags: ['k6.io', 'video', 'english', 'k6 Office Hours', 'performance', 'postman']
---
[Postman](https://www.postman.com/) is a near-ubiquitous tool for anyone doing API testing, and many teams use collections to create and organize complicated test suites. However, there's one thing that Postman isn't good at: load testing. That's where k6 comes in.

In this video, [Tim Haselaars](https://twitter.com/timhaselaars) joined k6 Office Hours to talk to [Paul Balogh](https://twitter.com/javaducky) and me about how to use Postman collections to run load tests using k6.

{{< youtube Be66Db4wHLA >}}

## Transcript

- Hello everyone and welcome to another k6 Office Hours. I am Nicole van der Hoeven and today I have two guests. One of them may already be familiar to you, Paul Balogh.

- Hey everyone.

- And our special guest is Tim Haselaars. Tim, would you like to introduce yourself?

- Okay, hi, nice to meet you Nicole and Paul. I am Tim Haselaars. I'm living in Belgium. I'm a product manager, and I work at the marketing automation company called Selligent. I have a passion for APIs. I love music, I'm a DJ as well in my spare time.

- Oh, nice.

- And if I still have some spare time left, I like to contribute to a number of open source projects, which the Postman-to-k6 is one of the projects I've been working on together with the k6 team in the past. So that's a bit of why I'm here today. So nice to meet you both.

- Yeah, that's a pretty big if though, if you have time, you're a DJ.

- It's a hobby thing, but I'm really proud of it actually, because I've been playing a lot, and there's one festival in Europe, Tomorrowland, I've been playing it each year for the past 10 years.

- Oh, wow.

- So it's a small stage, but I'm really proud of it.

- Nice.

- Yeah.

- Well, that is awesome. You should be proud of that. I think that kind of makes sense, because product management is such a multidisciplinary role as well. Like, it's not all technical, and it's not all people skills. It's a mixture of both, and a lot of other things.

- Yeah, that's also what keeps it interesting, at least for me, what keeps it interesting, actually, so yeah.

- So what do you typically do in your current job, and what does it have to do with k6?

- Okay, in my current job, I'm a product manager, so we have a digital platform, marketing automation platform and I'm spearheading the API renewal program. So we had a number of APIs in our company which customers use to connect and exchange data with marketing data, and we're renewing that, and performance is critical, because we have a number of really big customers in Europe, or , the Dutch luxury brand, and we talk about huge volume, so our APIs has to be scalable, and performant, and we use k6 to guarantee that we keep them up to standard, actually. So that's what we do. And my role there is to make sure the teams, I help with the API design, and I check with the teams, and I document stuff together with the teams, we try to do that. So what I'm going to talk about is also my experience with k6 and the way we use it at the company a bit more.

- Awesome.

- Cool, so how did you first start, what made you start to use k6? Did you try other things before that?

- Yes. In a previous job, a couple of years ago, I was working at a hosting company, and they were doing a, there was an anniversary of the national lottery, it's like the lottery company, so it had,, they expected a lot of visitors to the website, and we wanted to make sure the hosting was up to par, and it was able to handle the volumes. And I tried to test it, performance test it, load test it, and I used Jmeter, and the experience was, I struggled a lot with it. And I started browsing for another solution, and then I hit, I found k6. text was really nice. You could really quickly start nice documentation, and that's how I rolled into k6. And then I shifted jobs, and at the current job, I said we have to use k6, because it's so much easier than using JMeter. You can script it, you can automate it, and that's it, yeah. I used it once, and never looked back.

- So nice, with the automation, did you put hook that in your CI/CD pipeline as well?

- Yes we do. I can, I have a diagram. Like, I'm really proud of it. Maybe I'm a bit, how do you say, biased by it, but I'm really proud of what we've achieved with the automation aspect actually. And we came from a far away, a far place, but now, we have a nice automated flow, actually.

- That's awesome.

- Which I hope I can showcase a bit later on in the talk.

- Yeah.

- Yeah, I'd love to see it. And do you use k6 Cloud or k6 OSS?

- We had used Cloud in the past, I think right now, my team are mostly using the OSS version of it. I don't know why. I have to check with them, actually, but I think we had a number of dashboards set up, and they were a bit detailed to what we need, or what I needed at least, and that's why I think we stick with, for now we stick with the OSS version of k6.

- Okay, awesome. So I guess people might be wondering, seeing the title of this video, what Postman has to do with either Selligent or k6.

- Yeah, actually that's a story I want to tell, how did we ended up with k6, and the whole story. So what typically happens if you start developing an API is you build your API, and then you want to test it, you want to play around with it. You want to experiment with it. And the first thing that you do as a non-technical user like, I take Postman. Postman is an application where you can model your request in a nice tool, and then you can just fire them. You don't have to a curl script, or you don't have to use any CI tools for making API calls. So that was the logical step. So we build an API, I want to experiment, play around with it, so we ended up using Postman for it. But maintaining Postman is not so easy when you go for automation flows. And then when you want to take a step further, if you want to do performance tests, that's another a thing. And yeah, that's why I think we went from what we did to Postman just the next, as a first phase. But sooner, the more end points we have, the more we wanted to test and the more we wanted to play around with it, the bigger everything became. So that's why, yeah, we wanted to make it an automation level and make it a bit more streamlined so that the manual work would go down a lot.

- Sounds like you have a fan out in the viewers.

- Yeah.

- Yeah. I like to make things visual, because it helps me visualize my thoughts and everything. So yeah.

- I've used Postman before. I think it's almost ubiquitous now for anyone who's doing any sort of API testing. I think at some point people would've used Postman just because it is very easy to get started, but I do, I have also run across some of the issues that you describe when you're scaling up, when you have a very complex test suite or you want to have one, it is, I think I personally still like the scripting approach of being able to have the full, you know, being able to have condition loops and that sort of thing. There's still a lot more flexibility when, when you're just dealing with pure code. But I know that I think it was, I mean, relatively recently when I started using Postman, it was just firing off requests, and it was like a single user kind of thing, but what are the features available for performance testing for Postman, you alluded to it, them, and you said that maybe they're not, they weren't exactly what you were looking for.

- No, no. Maybe I should quickly show a bit how I--

- Yeah, sure.

- Work with it if that's okay for you. Okay, I'm gonna showcase my, so well, just as a reference, I created fake endpoint and I was set up a Postman collection. So what you do typically in Postman is you have an API that you define. In our case, I created a k6 office hour CRM API, just plain and simple where you can see, yeah, you could see some context you potentially want to interview in the future, and you model them. So you have your endpoint, you just put them in. You say, it's a get post, put, whatever you need, and then you can just fire it and it's response. And so this is an actual API request happening behind the scenes. That's really nice because as a non-technical user, you don't have to have any technical expertise. You just enter the endpoint percent and you're up and running. But it also has some nice features if you want to make complex things, like you said, Nicole, if you want to use variables, because you might want to experiment with your API endpoints in different environments, so you can use variables. That's what they use with the curly brackets here. So it's a base URL. So I can shift around so if I want to switch, I have potentially two environments. I have a production one and a dev one. I can easily switch between them and then the variables will also switch along. That's a really nice thing to do with Postman. The next thing, what I really like about Postman is that you can use it to create cruds and you can create flows with it. So it's really straightforward. So if you say, I want to create one item and then I want to use the item in my detailed call in my, so I have all leads, create a lead and I want to get the leads, so this is the end point, you could just define it as a variable. You could say, I want to, that this lead ID can be used to fetch the right lead ID. So if you create one, that's the body, I do a post request. And what happens is you get a new ID back, which is unique because I just created a new contact in our CRM application. And you can use scripting in Postman to say, ah, there is a data response, and I'm gonna store that response in my lead ID variable. So it allows some scripting within a GUI which is really nice, and it also allows you to define tests. Like I want to check what's the response. It should be 200. You can define a Postman test. They use a bit of assertion, kind of syntax for that. So what started out as something really straightforward, I wanted to just test and play around with it, experiment of the endpoints. It became much more. And we started building like a full suite out of Postman, in Postman itself, a test suite. And that's really cool because as a non-technical user, you could just share this collection with anybody on the team and they could just run the same request and play around with it. You can even pass it on to partners or colleagues or customers, when they say, when they want to use your API, you can just say, ah, you can use a Postman collection to play around with it. And another nice thing about Postman is that you can run scenarios, like I said, and you can run them at scale. So right now I'm doing get leads, creating a lead. Then I'm gonna fetch the lead that I just created. So I created Elon Musk as a user. I can update that one as well. So I can put a body and touch and I can even delete it. So if I would run this in a cycle, I would test actually the whole flow of a typical crud operation. You can fetch one, create one, edit one, delete one, and then it's back to normal again. And so lemme talk about, yeah, sorry.

- [Nicole] Sorry, I just wanted to, sorry to interrupt, but would it be possible to try and zoom here in this one to see if you can make it just a little bit bigger?

- [Tim] Okay, something like that?

- [Nicole] Yes. Thank you. Sorry.

- [Tim] No, no, no worries. So what you can do Postman, if we talk about test automation, you can just say, I want to run all these, these API requests in the sequence, like they're organized here, and you can just run them. So if you run them, you see you put in some test, this one is a success, success, creation successful. And so actually testing if your API's responding as you expected, but you cannot test it at scale or at high volume. The only thing you could do in Postman is if I press run, I could define a number of iterations. So if I would say, I want to do 10 iterations, I'm just gonna run them now, so you can see, you can see it just creates blocks. but while I'm talking, it took to run all these 10, five times 10 requests, it took me, let's say one minute to run. So we cannot really test at scale if, that's not the use case of Postman. The use case of Postman is to experiment with request, do some testing on some validation of the response and the inputs are okay and that's about it. So I needed something more if you want to do that scale. So while I discovered k6, k6 has this nice scripting language, you could define--

- [Nicole] Tim before you, sorry. Before you move on, we do have a question. Chaitra asks, can you share this collection please, just to get along with Postman.

- [Tim] Okay.

- [Nicole] Is there a way that you could share, make that public or something?

- You can, I haven't tried it, but I guess if I click share and I could, can I create a JSON link? Maybe could JSON link, update the link, maybe like that? I haven't tried this actually before either so.

- [Nicole] Awesome, we're learning in public.

- [Paul] Exactly. No pressure, no pressure.

- [Nicole] Yeah.

- [Tim] Oh, should I put it in the comments, or how would I do that?

- [Nicole] Yeah, sure. That would be great.

- [Paul] Yeah, otherwise I was gonna say we could probably put something together too for after, you know, the presentation if someone wants to access that, if there's no issue with that.

- [Nicole] Okay, I'll put that in the comments.

- [Tim] So I was asked as well from the k6 team to update our blog post about Postman and k6. So what I'm gonna do after this session is going to review the blog post that they have already on the website and then update it with maybe some content that I'm talking about in this show here.

- [Nicole] Great.

- [Nicole] And we also got a comment from Jim Munro who says Postman is definitely not designed for load testing.

- [Tim] No, no.

- [Nicole] And that's what it seemed like. So it seemed like you could only do iterations. Is that right? You can't set, you can't have more threads or users.

- [Tim] No, that's it. So the only thing you can do is you can run a sequence and you can run it in a number of iterations, but you can, you can't define how many users, you can't define how long iteration, you can define sleep, but that's difficult. So Postman is great for what it is. It's great for testing some of your contracts of your API, is great for experimenting with your API, and really kickstart using your API, but if you want to do volume, to test the volume at scale, I wouldn't recommend Postman at all. But that's also a bit the problem, because you already spent a lot of time making a nice collection, preparing it, grooming it, updating all the time. If you then want to go to k6, you would have to rewrite everything. So if you, this is how k6 syntax looks so you can define your iterations. You know this better than me actually. And you can just use a get request. And you can script your request. You can also check it. So that's the same as you would do in the Postman where you test your response. You could check if it's a 200. But if you have a complex scripts, you can, they become really large to maintain and to keep them up to date. And that's what I struggled with because it felt like I'm reinventing the wheel. So I made a diagram out of it just to explain it. So if you have an API and you have to update it, you would have to really update your collection and say, every time something changes an endpoint was added or a property was changed, you needed to update, go into the Postman collection, manually correct everything, extend it, and yeah, keep it up to date. But if you would go to k6, you have twice the work, actually. You have your API that's changing. So you need to update your collection. You need to update your k6 scripts. So if you have five endpoints, that's doable. But if you have 20 endpoints for one API, that's a lot of work to keep them in sync, because this is a moving target, but it forces you to keep in sync to other moving targets because you want to be able to experiment and test them, contract, and you also want to test them at scale with the load. And I was looking really for a way, like how can I leverage this nicely prepared Postman collection and use for k6 scripts? And that's what I, when I ended up with this scenario where you have your API, I update my post collection, I want to generate a k6 script. And I was looking around like, how can I do that? And I found on the k6 website, I found some blog items on, on how that they provided a Postman to k6 converter. And that really triggered me and I started playing around with it. And I really, really liked it. So it gives me all the flexibility of modeling everything in Postman, preparing the whole flow. So if I want to run it in sequence, I could do that. But then it also converted it into a k6 script where I had no maintenance on it, and that was really nice. And when I found the Postman k6 package, like a year ago or something, the purpose of that was to kickstart your k6 experience. And I said, but you can do much more with it. You could even fully automate it with some parameters because the first time I converted my collection, it had like 20 endpoints. I still needed to do add some minor things, I needed to add some k6 specific stuff to it, like how many iterations do I want to do, is there certain parameters I want to add that are not by default converted over. So I said, okay, what can I do to make it even better? And I don't have to touch the k6 script anymore. So the first time that you converted it, I had to modify it still. So each time that I would do this kind of a behavior, the API changes, I need to update my Postman collection and I needed to update my k6 script. I want to, my ideal world would be, I don't have to touch the k6 script at all. I just convert it and I was able to run it in one go. And I can show you how it works, because it's really straightforward in the end.

- Yeah.

- If it's okay, you can export your collection--

- [Nicole] Yeah, sure.

- [Tim] So if you do export, you can just say export and you download a JSON file and you can do the same thing with your own environment. So if you want to have your test environment and you want to also convert them you can because you can also export these from Postman. And what you end up with, I'm gonna close this one, you end up with two JSON files. So as you can see, it's the k6 office hours. It has some syntax in it, like the test scripts are there, the endpoints are there, the way you connect to them. So all the request information is in this configuration, in the environment file. You can find all your variables that you have defined. So let me just now showcase it. Sorry, I'm gonna, this one. So if you run the Postman-to-k6 converter, it expects actually two things. You define an input, my Postman collection, and you define an output. So if I would run this, just closely watch what happens there, it does some things behind the scenes, and once it's finished, you would get, actually, if things go well, let's see if it's there, you would get this. Yeah, that that's the goal of CLI. It should be fast. You get the k6 script. I'm gonna go over that later on, and you get this library folder. The library folder, what it is is because the converter, Postman uses number of functions, some methods that are not mapping exactly towards k6. So once this package, it adds some additional functionality that Postman uses. Like it uses low dash and some encryption, stuff like that, and it just adds the libraries there. So if you would do this manually, you would also have to include the libraries, but it does it for you. It includes all the libraries. And it's actually a wrap around the, let's go for the SHIM quickly. If it's not clear what I'm trying to explain, stop me, Nicole.

- [Nicole] Yeah, but we can also answer this question from Carlos Ramirez. You can also integrate, well, not a question, a comment. You can also integrate your process using the Postman API key to request information about your collection and environment. And he also adds, oh, no, sorry, this is from Chaitra Nanjesh, this is interesting, because we use k6 in Tesco, says load test, and I think we can try this to see if it works for us. So people are already liking what you're sharing Tim.

- [Tim] Yeah, that's the goal, That's also why I liked it actually--

- [Nicole] Do you also do what Carlos was suggesting?

- [Tim] Yes, and I even go a step further, but that's, I'm gonna come back to that later. I'm gonna showcase how we do the Full Monty in the end, actually. I'm building up.

- [Nicole] Awesome. Sorry, people are excited.

- [Tim] Yeah, I'm also excited, so I hope that I'm coming across properly.

- [Nicole] You're doing great, don't worry.

- [Tim] Okay. Just for reference, you have to think of this Postman-to-k6 thing as it's wrapping Postman functions and k6 functions and combining them in one place. So it's abstracting away the k6 part and it matches with the Postman stuff. So that's what it does behind the scenes. So if you see, if you do an execute request, which is an, it's a function actually, behind the scenes, it just does the HTTP dot request, which is a k6 function. So it wraps a lot of things together, and I think if I would go to execute test, you would also see it uses the k6 check function. Just for reference, this is the wrapping part. This is all not so relevant. You don't have to care about it. What's relevant is what's being generated for you. So it says on top, it's an autogenerated file here. It does some imports. It imports also k6 related items and it sets default options. By default, it says maximum redirects. And then it does some strange things which are not k6 related, but that's typically what the package does. That's the wrap that you see. It defines a collection with a base URL, and then you will see that my group is there, I have my request get all leads. It showcases the URL. It showcases that it does a test here. So everything that you had defined in your Postman collection, sorry... Get all tests and you could see the test here. It's translated into a k6 kind of syntax and it's ready to be used. And you see all the requests on here, all ready to be used. It even matches a response codes that you can match to a variable in Postman. You could do anything. The body is there that I inserted that you can create. So if I were now just say k6, sorry, k6 run k6 scripts. Oh, dunno know why this is happening? Give it a second to start up. There you go.

- [Nicole] Cool.

- [Tim] So I haven't touched anything, I just took my Postman collection, converted it with the converter that we built a while ago together with k6 and then you can see the tests there. So I created a number of tests. Postman expects to, the response is expected to be 200. I get all the data. My average is my group duration because you also have a group there. So if you have 20 endpoints, you will test 20 endpoints, but I don't need to write any k6. So I only do my maintenance for, my maintenance only happens in here. I only have to maintain my Postman collection and my k6 gets generated out of them. So that's really nice thing here. Yeah, that's the library that we're using. No, that's not, that's not my library actually. I think it's moved to--

- [Paul] Uh-oh.

- [Nicole] Hope this is the right one.

- [Paul] Yeah, we gotta update our show notes.

- [Nicole] Yeah, we do. Oh, with the API deck one. Sorry about that.

- [Tim] No worries. I think I made a pool request a while ago, so.

- [Nicole] Ah, I see. Okay, I will update the description.

- [Tim] But I, just to continue.

- [Nicole] Can you also post, Tim, the link?

- [Tim] Yeah, I'll post it. Of course.

- [Nicole] Thanks.

- [Tim] But it's really cool. Maybe cool's not the right word because the package supports a number of things so that you can even tweak the output even further. So by default, I just say, give me the Postman collection and generate a k6 and it would work. But if you want to automate this on a higher level, need to do work for automation, you wanted to tweak some things. Maybe I want to play around with some k6 parameters, or I wanted to do something else, or I want to exclude stuff, or I want to include my environment because, if you see here, there is no, there's only my base url, but I have a lot of variables I want to use in my Postman collection that I already defined. I have login information. I have some Postman base URL. So you can take it even further because now you just get a script, but it's just, the script is already addressed. So you can take it step further. So for example, if you would say, I want to increase the number of iterations, you could just say like this. You have this parameter, says iteration 10. I'm not going to convert it. There we go. And if you see my script now has options already set at 10. That's nice. That's handy because you want to automate this, of course. And you can even go, take a step further. I want to include my Postman environment variables. So I'm gonna, there's also a parameter for that. So you can pass some environment variables. So you can even pass some global variables. This is typically Postman, but you can just take the ones that Postman provides, export them and use them. So if I now do this kind of thing, so this is my file with my Postman variables, like I showed. Let's do this again. And here, you'll see all my variables that were exposed in my environment are now available for my k6 script to be used in automation workflows. So that's really nice, but I can even take it a step further. What if I have special k6 related parameters? I'm just gonna copy paste them here for the sake of the demo, but I might want to define my iterations or my maximum redirects because k6 offers a lot of parameter options. Like I want to use cookies. I want to use headers. The number of redirects. I want to set some text. I want to define a timeout. All these k6 related parameters, I want to make sure that my automation flow was able to process them because I want to run the script without touching it. So I want to be able to just say, take these parameters for this pipeline, these parameters are applicable for production. So you could switch environments. For example, what we do is we have different test scenarios defined. So if we go for a small test, we run it like this, we define stages and thresholds. Well, if we want to really do performance testing, we have different ones. So these options, we use them to pass them along to the pipeline. So I could do something again with the generation part.

- [Nicole] Question from Sri. Is it one environment at a time only?

- [Tim] Yes, because what you generate is what you inject the script. So it, you would then have to generate a second script, but that's really easy to do because you would just say, I want to have, for example, just showcasing it here, I'm gonna take this script is for the second test stage. You just run it and then you get a second script next to it. So you don't have to worry about it. You don't think about one script. You just fork it as much as you need with different configuration options defined that you would use.

- [Nicole] Yeah, and Sri, I wanted to also add here that with k6, you can have, you can test more than one environment at a time. What Tim is showing here is that for, because of the way that the that Postman treats these collections separately, every environment is separate. And so the converter also converts them to separate k6 scripts. However, once they're in k6 script format, once it's all JavaScript, you could use k6 executors and scenarios to run them simultaneously, if that's what you'd prefer or anything else.

- [Tim] So in this example, what I'm doing, I'm going to pass on my K6 parameters as a JSON file so that I can put them in a Git somewhere. And if I then just say, press go, you will see that it also just updates this option spot on the top. There we go. So you will see, I have defined it to be in this case five virtual users, 10 iterations, maximum redirects, and just adds it on top. So I can switch around in my pipeline without touching anything. I just prepare everything, and then it's just a matter of defining which command I should to run and it just does it for me. So that's really handy and it really makes automation a lot easier in that regard. And there's one thing I really like. It's a small thing, actually. Now it generates one big file. So everything is in this one big file, all the request, it's doable if you have like me, for example, four requests or five requests. But if you have like 20 endpoint or 20 requests, it's a huge file. And to handle that, you can just pass along one parameter. I'm not sure if it's commonly used a lot, but I'm a big fan of it. It's called a separate parameter. So what happens now? The options are there. The request configuration is there. But you just get this in your k6 script. I'm not sure which one, I'm gonna remove one because otherwise I might get confused. There we go. You get this, and this is actually, it splits all your requests in a separate folder like you would see them in Postman and each request would be separated from the rest. And that makes it really easy. If you want to test something specifically, if you would have one script, it would run everything. But now I can just comment out, I don't want to do the create, I don't want to do the update and delete. I only want to test to get all leads. You just say k6, k6 run k6 script. Give it a second to warm up. There you go. It will only test that request that I defined. So if your 20 endpoints, your k6 script has been generated for you will have 20 lines and all your requests will be nicely separated from each other. So you can even say, I want to tweak it a bit, or you have all flexibility then, while if you don't use a separate parameter, it just generates one file with everything in it. Do I make sense still?

- [Nicole] Yes you do. But there's a comment here from one of our engineers who wrote that initial blog post that you may be updating, Mostafa said last time you wrote an article about it, it needed a few changes to make things work, so well done.

- [Tim] Yeah. Yes, that was one of my first VRs that I did. I wanted to make separate flow over pretty much everything. And there's one final thing I want to showcase for, with the k6 part, is now you have to really, like all these parameters, they become very long and difficult. You could also just define them as a JSON file and just pass them along. And now you can just define the one file, put the main Git, and then you could just say, I want, this is the output, my environment. You can even define that it uses a handle summary, or you can add request tagging on top of it. And if you do it like that, you get, you just have to do one parameter, one command, actually. So if I do it like this, you see, it just says, this is my input file. I've defined an options file, which I referred to. And if I then just do it, it would take all these parameters that I've defined and you would get, again, everything nicely generated for you. All the requests are there and it even added the handle summary thing on top of that, which is something--

- [Nicole] Oh nice.

- [Tim] So everything is there. And so this is the automation flow that's really powerful because otherwise you would have to add, if you want to have a summary, you have to add a modified file. But now I just define one configuration file, I define my parameters, I define whatever I need. Just run it, and my script, I don't need to touch it. I can just say, okay, k6 run k6 script. And you would see that it generates, yeah, it generates a test. It does, I think five or 10 iterations. There we go. And it doesn't open anymore. It generates the JSON file. If I close my, quickly here, you would see a summary report is here. So it just, yeah, there is no manual work anymore to run k6, just keep your equipment collection up to date.

- [Paul] And you're helping folks out with your example here.

- [Tim] Yeah, okay, great. Okay, that's in summary, the things that I want to showcase about the converter. There are some nice things added since the last releases from the k6 team. So I added some, requested and changed some things, and I'm really happy with it. It works flawless at the moment in our organization actually. So I'm really happy with it.

- [Nicole] Yeah, it seems really, I think I tried this initially, like when Mostafa was saying, there are a few things that you, you had to get done, but this seems way slicker, and it seems like you've really focused on making it automatic so that don't, there is no manual intervention, which totally makes sense in a CI/CD pipeline.

- [Tim] Yes, correct. And I wanted to put my effort on the Postman and the management of the Postman collection, because that was a tool where we were all working on and maintaining it. And I wanted to keep the workload on k6 as low as possible. And I think we succeeded it quite well on that regard. There are some things that are not available out of the box. Like you cannot do the send request. You cannot set next request. But what I did add was, what I'm also really proud of, the dynamic functions from Postman. You could just add any, pretty much any generated stuff. Let's see if it shows, if it works like that.

- [Nicole] There's also some nice comments for you. There's Gertjan De Wilde, who says, Go Tim. There's Pepe Cano as well from k6 chiming in with his support. James is saying nice to see this getting the love it deserves, much better experience. And Charly is saying, Very useful tool, congratulations.

- [Tim] Thank you.

- [Nicole] Lots of love in the comments for you.

- [Paul] Definitely.

- [Tim] Okay. But honesty, we took it a even a level further, but maybe I should, maybe there are, if there are other questions we should talk about or not, I'm not sure.

- [Nicole] I'm interested in this. So what were you saying, the dynamic part that you added parameters?

- [Tim] Let's see.

- [Nicole] I mean, you also don't have to demonstrate everything. Can we just like acknowledge the fact that Tim who doesn't even work for k6 or Postman volunteered to do like a live demo about this. So that's awesome. Don't feel like you have to show us everything. You can just talk about it.

- Yeah, Postman really provides this nice, what they call dynamic variables. And so it's, this is a screenshot of it. So if you use curly brackets, it's random, and then you can say, I want the full name, I want the bank account or anything that uses Faker behind the scenes, and you can make dummy data out of it. So that's really handy if you want to really make, yeah, realistic data without having to use for loops or anything, just put in the variable. And that was not fully supported in Postman to k6. So we brought in that support as well to make sure that you could have the full functionality of the dynamic variables attached to that. So yeah, there are a number of things we did since the last release of it, and I think dynamic variables was in much demand at that moment. There you go. Yeah, and I'm really happy for Mostafa, I'm not sure how to pronounce it correctly, because I think he was one of the first ones who pointed out in his blog post about functionality. So thank you for pointing it out to me.

- Yeah, now that I think about it, I should have asked Mostafa to be here too. Oh, I missed that opportunity. Sorry about that Mostafa. That's so good about the dynamic variables, because that's one of the things that you have to think about when you shift from just a purely automization mode, like automated testing mode to load testing is that you can't, you then have to start thinking about the data that you're sending too, because if you're trying to get realistic response times it could trigger caching on the service side if you're just requesting the same thing. So yeah, totally makes sense. k6 can already, you can already import faker with k6, so great, great job for putting that together.

- Yeah, no, that's very cool though, but yeah, it's like, you can use Postman for your user, your UI, your, you know, your development environment and do all this stuff and then even goes through there and generates some random data. So, yeah, that's cool. Very cool.

- Oh, go on.

- But maybe I'm gonna talk first before I want to show the final piece of what we did.

- Well, just, just quickly, I just wanted to ask about the limitations of this approach that you see.

- Not all functions of Postman are supported. So that's the downside of it actually. But for the use is that that we are using it, we have everything covered. Like you have the, the dynamic variables, you have the environment variables, you can define k6 parameters. Yeah, there was nothing stopping us. I think if you want to do complex scenarios and you want to do if-else situations, there it's not suited for. That's the same problem you would have in Postman. It would be difficult to make these if-else conditions in Postman as well. So that's, if you do simple tests, functional tests in Postman, you can really easily port them to k6 and then you have performance tests end points.

- And in the spirit of the whole free and open software. I mean, do you have issues where like you're looking for help? Is there any gaps that you're still looking to fill?

- There are some bugs I cannot reproduce at the moment, something with XML conversions, but right now it's feels quite feature complete. I haven't added that much, actually. The base was already there by the k6 team members who built the initial library. So I just added some sugar coating on top to make the automation flows much smoother and less manual work, or linked actually. But if people have great ideas, I think they should just make a PR and add it to the package.

- Yeah, did you want to show us something else?

- Yes, I want to show how we ran a step further even, because yeah, if you update your API and then you have to update your Postman collection, it then generates a nice k6. But we also use openAPI as a documentation tool where we document and design our API. So every change that you do on your API, you need to add them to your API, and then you, so you still have to maintain not one output, the Postman, but you also have to update your documentation. And I want to flip that around. I want to make the API documentation leading, generate the Postman collection out of it and generate out of the Postman collection, a k6 suite. So that as a product manager, I don't have to maintain all these documents anymore. I just maintain one thing, and that's my openAPI and my team or our team then only just need to develop the application itself. And it's called spec driven approach. It's nothing new, but I'm a really big fan of it and I'm a really, yeah, we introduced it a year ago and it solved so much and it brought so much quality on the company level, in our documentation, in our test suites. So that's something I want to share as well, because it's so valuable once you get how it works and if the right tools and properties, you can really do it. And this is actually where we are right now. I can also demo how it works. So we have, I'm managing an openAPI documentation. We use the formatting and we validate it if it's valid. And then we use a generated one. And from the generated one, we generate documentation. So public documentation, stop lights, just like whatever you call it, we generate a Postman collection that we can share with the customers and we run contract tests, we run soak tests and we run smoke tests all based on this openAPI documentation. So, and again, there's no no contact or no changes involved. We just, we managed the spec on its own and it's really, really something powerful and useful. And I can quickly show how it would work actually if you're interested.

- [Nicole] Yes, but before you do, a wild Mostafa appears.

- Hello.

- How awesome is that? Let's just say hello to Mostafa, who just joined last minute since he was already in the comments anyway.

- Nice to meet you. And I'm grateful that you wrote the blog post so many, so many months or years ago, so thank you for that.

- Yeah, yeah, I really felt the need that we needed this article, so that's why I wrote it in the first place. And then, yeah, I found a lot of issues that you solved, and thank you, it was a great job you did, and well done.

- Thank you. And thank you for putting out the 90% of it. I said I only had to put in the sugar on the top of it and the cherry on the top.

- No, no, no, no, that's not true, that's not true.

- Mostafa--

- In the first place just to clarify.

- Yeah, Mostafa while you're here can you quickly introduce who you are and why we've randomly invited you onto the stream?

- Of course. Okay, so I am a backend developer at k6. I'm almost three years with k6, like it was called Load Impact before being renamed completely to k6, and now Grafana. I've been a developer advocate when the first like idea came into place that we want to have a developer advocacy program. And yeah, I've been a developer advocate for a year and then came back to back it. So I worked with lots of these tools and tried to help others because like, there were no other resources available. Like there was this read-me on the project and that was it. No mention of it anywhere. Only the hidden knowledge of everyone inside the company of how to use this tool, but nobody knew without outside the company. So tried to learn it from others, specifically, Pepe, thanks for that, from here. And I tried to write that blog post and try to share the knowledge. So that's basically it.

- Great, so we also got a comment: Great with the diagram. Can you share this?

- Of course I can. Yeah, I'll do that.

- All right, I guess that's our cue to head back. Please continue, Tim.

- Oh, I'm not gonna, I'm just gonna showcase it, and then I hope everybody will really appreciate and see the power that it brings actually. So, okay, so maybe start with the beginning. I'm gonna close my screens a bit to clean it up. So I have this openAPI spec that I, it's just a copy of what we just described. So this is how it looks, this is documentation using Docly. You can see it's the k6 office hours CRM application. You can see the list in there. You can see the create, the get. So it's just the definition of what the API would look like. This is the documentation part of it. So I'm using now two tools. I'm gonna use Portman as another package that I built together with API Deck and make an API Deck where we can convert the openAPI to Postman, and from the Postman, you can generate a k6 one. And that's really nice because you only need two commands, one source file, and you have two outputs out of the box. So that's really powerful. I find it powerful at least. So I'm gonna take my commands correctly.

- So If it's okay, can you, I'm not, I'm not up to speed with Portman. So it creates a Postman collection already given openAPI, is something in openAPI specification?

- Yes.

- That's awesome.

- There was, Postman built a patch like Mostafa, k6 build a patch where you can convert from Postman to k6, and Postman build a Postman where you can convert from openAPI to Postman. And when I found out, I said, that's amazing. You don't have to maintain a Postman collection anymore, but it wasn't, it was missing some functionality, and the major thing that I was missing, it was just creating the request than Postman, but not the tests. It was not handling the tests of it. It was not assigning variables. It was just taking the Postman request and converting them into openAPI requests, into Postman. So you still needed to maintain and modify them. And I said, it has to be, because an openAPI documentation or specification, it describes everything, the request type, the body, the properties, if you do it properly, you have all, everything in one go. And I said, why not use that to create a test suite, update your variables, do all the dynamic stuff you would expect it to come out of the box. And that's why we created Portman. It started as a PR on that openAPI to Postman package, but then I met Nick from openAPI, from API Deck, sorry. And then we came together and we said, let's collaborate, and let's make a startup package out of it that you can plug in and use it to automate these kind of workflows. And it's really, yeah, I'm biased again, but I really like it.

- No, it sounds awesome.

- A question here. May I ask a question here? So have you seen the openAPI generator package that I've written?

- Yes, I saw that and that I had the same comments as I had initially. It generates a nice k6 script, but it it's usually you still have to manually adapt a lot of things and correct it.

- Yeah, but sorry that I interrupted you. There's this latest PR point? I think Michael, if I'm currently remembering his name, so Michael added a feature to, to be able to add certain extension to the, to your Swagger or openAPI collection so that it generates everything for you. And if you add examples to your API output, to your responses, then it can extract those examples and put it in your script so you don't need to modify anything. So you can create basically the same thing you did for Postman, you can do it for the openAPI. So the new revision, the new PR and the new version that is released by Ophelia, the maintainer of the openAPI project helps you create a complete test from start to finish with no modification.

- Yeah, I think that's great, but we do two types, three types of tests. We will do contract tests, and then we use Newman for it. And we want to use k6 because Newman, it can do schema validation, it can do a lot, I think a lot more than k6 can right now. I think it's also the goal for k6 to do all these contract validation. It can, I guess, but I treat them differently. I think the Newman Postman has more contract testing capabilities, while I think k6 is perfect for performance and load testing at scale, where you only focus on what's the response, is it 200 or is it not a 200, at least that's how I use it actually.

- That's fair enough.

- Yeah, what Portman does it converts openAPI to Postman. So I'm gonna showcase that quickly. So it just took the, this openAPI that's here now, and then gives a while to spin it up. There we go. It's converting it. And if things go well... Let me check something happening here. Here it is. So here's my Postman collection. It's just generated it. It does everything for you. So it creates, recreate, so there wasn't a collection there. It just recreated for you. And I hope things, it's not showcasing it here. That's bad, too bad. So it just generates and if I would import in Postman, let's quickly do that... Give me a second to find everything. There we go. So this is the k6 and it's generated by Portman. There we go. If you see you have the same endpoints--

- [Nicole] Oh, nice.

- [Tim] So the first thing it's great because you don't have to recreate your Postman collection. You just, you just run it from your openAPI specification and you get, as a result, you get your requests pre-tailed already, also your post exercise is ready. So you can see here, it inserts a body, everything, I don't have to do anything. It just takes your openAPI and converts it to Postman. Plus it adds a lot of tests already. You see, it does contract testing by design. So it includes automatically 200 contact applications. So it just injects your contract test in there. And that's really nice because I only need to maintain one document, my openAPI specification, as a result, I get all my requests in Postman, and I get all my tests in Postman without writing any code. I just need to maintain it in the openAPI documentation.

- Wow this is really awesome, Tim.

- So keep in mind that this was the flow before you had to create your Postman collection and add the tests, and then you could generate k6. Now we turn it around. Now we generate the Postman and request, and then we can use that to generate, okay, six scripts. And so we only need to maintain this part in, yeah, or you know, that's the only thing I need to maintain as a product manager and the team, of course, they built the API and the service and everything, but I get this and I can focus only on this. And this is easy to manage because it's a YAML, you can play around, you can add endpoints, you can remove endpoints and just run it. A minute later, I have a Postman collection to play with it and I can run it at scale with k6, doing the volume tests. What else can I showcase quickly here? Let me see if I can. I just--

- [Nicole] Some more nice comments here. Such an awesome flow, says Gertjan, and James says his mind is blown and, and I join him on that sentiment right now.

- [Mostafa] Exactly. That's a full test suite, like from start to finish.

- Yeah, and like example, schema validation. It comes out of the box. You don't have to add it. It just does it for you. And the richer you make a documentation, the richer the test suite will become. And it also, Portman, be extended, you can also do variations. So now it just validates if it's a 200, but you can also have it generate 404s, and then it will remove items from it. If it's a required property, it'll create a variation out of it. And then you can test I'd the 404s are not present. And so you get two test suites in one go, actually.

- Wow. That is, that's so awesome. Maybe we can like, try and summarize this as we try to collectively recapture our blown minds. So I think that there are two different tools here, Postman and k6, which are really for different things. The Postman is really better for API testing, and as you mentioned, Tim ,contract testing, and k6 is better for load testing. And their features are pretty divergent after a certain point, but they do have a commonality, and it seems like that's what you've really capitalized on. Mostafa and Tim both have worked on this. and you you're trying to make, you've gotten us closer to this ideal of having just one set of test suites, and it doesn't really matter whether it's automation test suites or load test suites or, it can just be the one thing and you no longer have to maintain two separate ones. And that's having like the amount of time that you need to set it up, but also running it. Because having to explain this to somebody else is also a huge deal when you're not the only tester on your team.

- Nope, exactly.

- And the nice thing is as a product manager, I'm not technically, so but I can contribute to it. I can, I just need to maintain the openAPI specification and the whole team benefits from anything that I do. If we need to add a new endpoint, I can design it. Not even five minutes later, one minute later, I can just run it in a pipeline, see if it works, and that's a bit, the cycle of spec driven development. You put your spec at the center, the spec at the center, and then you design it, simulate it, fill it, Then you build it, you test it. But the spec is a test driver here and then you can even run it on production and yeah, do the management aspect as well, because then you can monitor it as well based on your API specification. So that's, as a product manager, I'm really proud that we pulled this off because that was one of the ambitions when we wanted a newer, or API program, like how can we use a manual workload, what can we automate, and yeah, I'm really happy because it's all open source based. There is no other software involved. We just use k6. It has excellent dashboards to individualize reports. We use Postman to generate contract testing and manage it, play around with it. And we benefit from such large ecosystem , Swagger as documentation interface, where you can display or openAPI as well. So it's almost full cycle or I don't know what's the term for it, but yeah, I really, I'm really happy with where we are right now. It's a good place to be in an API landscape actually, especially from, yeah--

- You've taken it a step further, right? This is no longer just about test suites. It's also because you are building on the openAPI specifications, it's all connected even from not just the development part, but the design part. And Pepe actually has a question about this. He says, can you show us more about the process that updates the APIs? What does it do?

- How do you mean? This flow, this one?

- Sorry, which one? Yes, I believe so.

- The powerful thing about this can also be because if you have an openAPI specification, you can even generate clients or service side code from it so that in the end, your API service can also just be generated from an API specification. There is a really nice openAPI, there's a really nice openAPI open source project, it's called I think openAPI Generator, and then you can just run a C# library or an API for that. You just take your openAPI documentation and you run, you run it and you get as a result, you get C# code that you can run in production. And that's also what we use in our company. You have some teams that just manage to build the openAPI specification and they use that to generate C# code and have APIs up and running in no time. I hope that this is the answering this question.

- Yeah, Mostafa, Paul, anything you want to say to Tim.

- Yeah, no questions but, yeah, that would come later, but I need to definitely pass this along, this video along to some people that I used to work with, because this will blow their minds as well. This is something that they definitely need.

- Yeah.

- Do everyone.

- Great job, great job.

- Yeah, great job, exactly. I'm literally speechless because I've worked with all these tools and I know all the--

- Clearly not literally.

- Well, not the ones that Tim wrote, the ones that we had before. But anyhow, this is a great addition to this mix of open source software that was out there and that we used, and this is basically end-to-end testing. So based on a YAML file, which is an openAPI specification, you can generate tests for your API. You can generate load tests. You can generate, I don't know, like literally everything.

- It's also documentation. You get documentation, nice looking documentation out the box, a playground with Postman and you get the numbers to back it up with even graphs from k6. I really like your dashboarding. So if you have a customer and they they're asking about SLA, we just pull up some graphs from k6 and everybody's happy with that. So we, the full ecosystem has really matured a lot over the last couple of years.

- Bravo.

- Yeah, this is so freaking awesome. Thank you so much, Tim, for coming on. By the way, he's not even working for k6. He's just, and I think you said at one point, oh, I'm a product manager. I'm not technical. I beg to differ. This is pretty amazing things that you've put together. There's a bunch of comments here too. James says he's literally waiting for the livestream to end, so he can link to the video with a timestamp. Well, let's just try and drag it on for him, shall we? Thanh says plus a thousand votes, and people are also saying thank you, and outstanding, almost the holy grail. So lots of fans in comments. Thank you so much, Tim, for joining us. I know we're a bit over time. I'm kind of taken aback by how much value you just showed us. This is amazing, I think we need to have you back.

- Yeah, I'm gonna write a blog post for k6 and one for API Deck where I'm going to get more into the details because yeah, it's a show now, it's a difficult to but I'm gonna try to write it up and then extend a bit on what, sorry.

- Mostafa.

- Mostafa, apologies, I'm really bad.

- It's fine, it's fine, no worries.

- Yeah, I think can be really powerful to share with the rest of the world that they can, yeah, maybe use some parts of it or not, but I benefit a lot from it. The whole team benefits a lot from it, actually. I can showcase, this is a pipeline we use, for example. So this is we do tests, then we run Postman and we do tests and if it's 100%, it gets deployed. So it's not just a gimmick, me showcasing it. This is really happening in our company. So we use it to build it. We use it to have nice dashboard with k6 attached to that. So yeah, I'm grateful that you put it out there for us to benefit from it.

- Thank you.

- That's so great, thank you.

- Yeah, I--

- Go on, Mostafa..

- Review the article that you want to write.

- Okay, I'll keep Pepe in the loop and then you'll reach out.

- Of course, of course.

- Great, thank you. Thank you as well, Paul and Mostafa, for coming on, Mostafa, even though, sorry, I should have invited you even earlier. Thank you everybody for watching. Thanks everyone in the chat. Have a great weekend, everybody.

- Absolutely.

- Thank you for having me.

- Yeah, thank you.

- Yeah, all right, see you all.

- Bye.