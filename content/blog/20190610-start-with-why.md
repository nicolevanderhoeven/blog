---
title: "Start with Why: How to Write Requirements for API Load Testing"
date: 2019-06-19T21:49:17+01:00
draft: false
tags: ['text', 'english', 'performance', 'requirements']
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/start-with-why-how-to-write-requirements-for-api-load-testing">
{{< /rawhtml >}}

_Originally published [here](https://www.flood.io/blog/start-with-why-how-to-write-requirements-for-api-load-testing)._

Every good test begins with requirements.

You may think, “But I’m a tester! I’m not a business analyst!”, and I hear you. But as testers, especially on smaller teams or shorter projects, it’s still part of our job to make sure we know what our clients want. Otherwise, how do we know whether we’ve succeeded or failed?

At Flood, I often speak to project teams who ask for help interpreting reports. Most of those times, the problem is not that they don’t understand the metrics or what they measure. The problem is that they didn’t set pass or fail criteria in the first place, and so they don't have anything to judge the results against. This is always a big warning sign.

## Which performance testing metrics are important? Why are we testing, anyway?
Requirements inform every step of the load testing process. Why are we doing load testing? What exactly do we want to test? How will we know when a test has passed or failed? How will we know if application performance is good enough to go into production? What does “good enough” mean?

[Tim Koopmans](https://flood.io/blog/author/tim-koopmans/), co-founder of Flood, coined the acronym SPEAR to describe the different aspects of a performance that should be considered in load testing. This is a great starting point when thinking about what we want our nonfunctional requirements to cover.

### Scalability
Scalability is the application’s ability to cope with increasing demands by increasing the amount of server resources. This could mean scaling _up_ (increasing the resources of the dedicated server) or scaling _out_ (adding more nodes to shoulder the load). What happens when more users than expected sign up in response to a promotion on your site?

### Performance
The most common performance metric is page response time, but there are other considerations to be made here, such as throughput (requests per minute) and the number of concurrent sessions that need to be supported. Things like the total size of the resources on the page, whether or not a CDN is being used, and what to cache are also worth discussing.

### Elasticity
Elasticity is a relatively newer aspect to performance testing brought about by advances in the cloud that allow application infrastructure to adapt to changes in load. Unlike scalability, elasticity emphasises scaling down as much as it does scaling up. Testing that virtual machines scale up when load increases is important, but testing that virtual machines also scale down when load decreases can also help save on unnecessary costs.

### Availability
To test for high availability, ask yourself what would happen when (not if) your application’s server fails. Is there another server that the load balancer will seamlessly send traffic towards? Does the throughput fluctuate wildly? If users are connected to one server that fails, is your application smart enough to make new connections to another server? Or will it simply serve up an error page that users won’t know what to do with? Disaster recovery is best tested when there’s no disaster imminent.

### Reliability
Reliability encompasses a lot of scenarios, but they all have to do with whether or not your application returns expected responses. Does your error rate increase when you increase the duration of your load test? Are you adding verification steps to your load testing scripts to check whether or not the HTTP 200 response that the application returned is not actually an error page?

## What should my application’s response time be?
Our clients frequently ask us what the industry standard is for response times, wanting to make sure their applications measure up. The answer, however, is more complicated than a single number.

Industry standards for response time are only useful when applications are very similar. Constantly changing technologies used in web development as well as innate differences in business processes, however, make it very difficult to extrapolate a single number that will apply to all, or even most, applications in a certain industry.

The home page of one e-commerce app, for instance, might be several seconds slower than that of their main competitor. However, that doesn’t take into account the fact that their app loads a video showcasing new products. Does that mean that the development team should remove the video in order to fall in line with their competition?

Well, maybe. But not necessarily. It’s a business decision that needs to be made after perhaps using focus groups to determine the impact of the video, forecasting changes in conversion rate due to it, and comparing its projected value to the effects of being slower than the competition. A/B experiments could be used to test these assumptions and gather quantifiable data to support the team decision.

These factors are often not considered in the search for one number to rule them all, which is why a fixation on that number can be detrimental. Instead, I encourage project teams to brainstorm and come up with their own numbers for all metrics that would be more appropriate for their application. Gathering comparative metrics from a competitor may be part of this process.

## What is a good API load testing requirement?
A good requirement, just like any good goal, is SMART:

### Specific
Vagueness in a requirement leads to vagueness in results interpretation.

_Instead of_: “The performance of the web application…”

_Try_: “The average response time of the Login transaction...”

### Measurable
Make sure there is a quantifiable way to know whether requirements have been achieved.

_Instead of_: “Decrease user frustration.”

_Try_: “The error rate must be below 3% at peak load.”

### Agreed Upon
Have the appropriate stakeholders been involved?

_Instead of_: “The system must be able to generate emails as soon as users register.”

_Try_: “The system must be able to generate a maximum of 100 emails an hour, after which emails are queued.”

A good example for this is a project I was involved in that aimed to increase the speed with which emails were generated. Unfortunately, the particular email being sent included a big change that many customers were expected to contact the support team about. The problem was that nobody had thought to include Support in the conversation. Once they heard about the expected end result, the support team quickly raised their concern that they would not be able to handle the expected volume of emails unless the emails were staggered. This could have been avoided if they had been brought into discussions from the very beginning, in the requirements gathering phase.

### Realistic
Can we meet this requirement given the resources available?

_Instead of_: “All requests must be returned within 5 ms.”

_Try_: “90% of the Catalog page requests should be returned within 3 seconds.”

### Timely
Especially for nonfunctional testing, consider adding a timeframe to requirements.

_Instead of_: “The digital code is sent by SMS upon successful client log in at peak load.”

_Try_: “The digital code will be sent by SMS no later than 5 minutes after successful client log in at peak load.”

## Go forth and write great load testing requirements
Requirements represent a great opportunity to think things through and make sure everyone on the project team is on the same page about the goals for your load testing. Too often projects skip this phase, only to realise much later that the tests that were executed didn’t address a key stakeholder’s concerns.

In load testing, as in many things: when in doubt about what to do, start with why.