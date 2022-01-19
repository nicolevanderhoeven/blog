---
title: "An Overview of Software Testing"
date: 2022-01-19T17:10:11+01:00
draft: false
tags: ['english', 'video', 'performance', 'testing', 'ship30for30']
---

{{< youtube huiptd8Y2I0 >}}

## Transcript

NICOLE: What is the difference between good software and bad software? Is it features or user interface or marketing? In my totally biased opinion, what actually makes a difference is how well the software was tested. But software testing encompasses a lot of different areas and it doesn't even always have to be someone with a word tester in their job title that does the testing. So whether you're looking to get started in the industry, or just trying to cross skill, here's an overview of the main types of software testing. 

Is it just me, or does your desk get that clutter too after a week of work? 

Anyway, software testing is the process of validating whether an application works as intended, but there's a lot of vagueness in that statement. One of the broadest ways to categorize testing types though, is whether it's functional or operational. 

Functional testing is more about application features. Is there a form to capture user email addresses? Is there a button next to it that submits those addresses? Once the button is clicked, where do the user details go? Do they go to the database? Are they stored correctly? Those are the sort of ways in which functional testers think. Operational testing traditionally called non-functional testing, is a way of verifying software quality and aspects that extend beyond the features of the application. 

Operational testing sometimes involves concerns that are more subjective or qualitative. So it can be a little bit more difficult to test, because those things only arise in certain conditions. Am saying, operational testing here, instead of non-functional testing, because I was talking to Paul Bruce who made an excellent video just on this topic. He talks about why the term nonfunctional requirement is really a bit of a misnomer.

PAUL: It relegates all these other things, security, performance, installation, deployment, accessibility. It relegates them to a nice to have, so it should be functional versus operational.

NICOLE: So I'm using his term operational testing instead. 

Here are the different forms of operational or non-functional testing. 

First there's accessibility testing. It is involved with verifying that end users can consume or navigate content. Usually through assistive devices like screen readers. While most forms of testing begin with a statistically normal user in mind, accessibility testing seeks out outliers in terms of location, linguistic background and disability. 

Usability testing is designing with user experience in mind, specifically concerning the placement of on-screen elements and the intuitiveness of the process flow of an application. 

Localization testing is a way of making sure that applications are usable in the local context, in the sense of being colloquially appropriate for users in different countries and from different cultures. 

Security testing verifies that a system has no flaws that could be exploited, to gain access to confidential information or features that would not otherwise be accessed by expected means. 

So that was me talking from my home in the Netherlands, but this week I am in Portugal. The remote working life, am I right? 

But anyway, performance testing is my favorite topic and my favorite type of testing because that's the one that I've had the most experience with. Performance testing is more qualitative. So it's more about how well the application works. And there are two main types of performance testing and that's front-end performance, and back-end performance testing. 

Front-end performance testing seeks to verify the user experience at the interface level. So that's everything that the end user sees on their local machine. 

There are different approaches to front-end performance testing, and the first of them is performance profiling. Performance profiling involves running your application through a series of automated checks. And there are a lot of sites for this, where you just put in your URL, if it's a web app, and you get a score in the end. That tells you how performance your application is, the most popular example for this and also the easiest to get started with, is DevTools because that's already in Chrome and Firefox based browsers. But you can also go to sites like Webpagetest, or GTMetrix, YSlow, which is a plugin, or you can use Google Lighthouse, which is now included with Chrome Dev Tools. 

The next approach to front-end performance testing is called RUM or Real User Monitoring. So the difference is that with performance profiling, that's often done manually, and as a one-off thing, like maybe at the beginning of a test or during, but Real User Monitoring is not usually done within testing environments. As the name suggests, these tools measure the experience of real users. So they have to be run in production. Examples of tools in this space are; New Relic's RUM, Elastic has a RUM as well, there's Catchpoint, SpeedCurve Uptrends and many more. 

And the third approach to measuring front-end performance is by using some sort of browser-based automation tool. So typically this has been something like Selenium, but that's falling out of favor in terms of more modern solutions like Playwright, Puppeteer, Cypress and so on. 

So front-end performance is about everything that the user sees on their end, but back-end performance testing is about everything that they don't see. It's about the network. It's about latency, the application servers, the way the infrastructure is set up and all of those things that are a little bit more difficult to look into, but can also have severe bottlenecks. Back-end performance testing seeks to verify aspects of an application such as scalability, elasticity, availability, reliability and responsiveness. 

Scalability is the application's ability to respond to changes in demand. This could mean scaling up, which means increasing the resources available to a server, but it could also mean scaling out, meaning increasing the number of servers that are available to handle the application load. 

Elasticity is a related topic to scalability, except where scalability is all about scaling up or out. Elasticity also emphasize a scaling down or in, and that's because having these services or servers available on the Cloud that are dynamically adjusting can also be quite expensive. So elasticity makes sure that the infrastructure that's available or the resources available are always appropriate for the size of the demand. So when demand increases, elasticity also checks whether the application decreases it servers or resources in response to that. 

Availability is how long the application stays up, despite changing circumstances in production. So this is typically measured by uptime. Availability can also be tested using disaster recovery procedures, and you're not just testing the application itself, but also the processes around it. So are there enough people that are on call so that they would be able to come in and troubleshoot when there's a production incident? All of those things are included in application availability. 

Reliability checks to see how your application behaves in response to unexpected errors. Reliability basically takes it as a given that your application is going to fail somehow, sometime, maybe you don't know exactly when that will be or how it will fail, but it's going to happen. So a big part of reliability and site reliability engineering is trying to expose your application to those failures beforehand so that you can build confidence about how it will behave when those things actually happen in production. 

And the last aspect to back-end performance testing is responsiveness. And this is usually equated with load testing. Load testing is more of a technique for testing though. And really load tests can be used to test not just responsiveness, but also reliability or availability or scalability, basically any of the "ilities" in this part of back-end performance testing. 

Protocol-based load testing verifies the backend performance of an application, not by simulating real users accessing the application, but by simulating the underlying requests that go back and forth between the client or the user and the application servers. One of the benefits of protocol-based load testing is that it takes up fewer resources on the side of the load generator, and therefore is less expensive to run. Some popular protocol-based load testing tools are k6, JMeter, Gatling LoadRunner, NeoLoad, and Silk Performer. 

Browser-based load testing verifies the application by simulating real users accessing it. So it also has the benefit of including these front-end performance metrics. Browser-based testing can also be called browser-driven or UI-based testing. Some popular tools for browser-based load testing are Playwright, Puppeteer, Flood Element and as of a few weeks ago, k6. 

Then there's hybrid load testing, which takes the best of protocol and browser-based load testing tools by combining them in one test. Now this can present some challenges, especially if you're using different tools for the browser-based script, than you're using for the protocol-based script. The ideal is to use your protocol based load testing tool, to simulate majority of the load to cut down on costs for the execution and scaling out of your load test. And then you run a handful of users using your browser based load testing tool. So you still get some metrics for front-end performance while that load is being applied by the protocol based tool. 

Testing software can be really daunting because there are many aspects of an application that you can test. But that's because there's also many aspects of an application that can fail. And that's why all roads lead to testing and why the success of an app hinges on how well it's been tested. 

If you'd like to zero in, on load testing in particular, check out this video that I made on what load testing is. Thanks for watching. And like they say, here in Portugal, Obrigada!