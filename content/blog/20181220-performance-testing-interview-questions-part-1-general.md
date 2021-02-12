---
title: "Performance Testing Interview Questions, Part 1: General"
date: 2018-12-20T12:41:40+01:00
draft: false
tags: ['english', 'text', 'performance']
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/performance-testing-interview-questions-part-1-general">
{{< /rawhtml >}}

_Originally published [here](https://www.flood.io/blog/performance-testing-interview-questions-part-1-general)._

## Preparation is Key for the Perfect Interview
Performance testing interviews can be a nerve wracking experience.  We all understand it’s necessary, but we dread it anyway. Each company has its own style of interview, so you may need to prepare differently for each opportunity. This interview series will cover some general sample questions and scenarios as well as my answers to them to help you nail that performance testing interview!

I’ve broken down the potential questions into the most popular categories, so you can prepare easily for your all-important interview:

### What is Performance Testing?  What is Load testing?  What is Stress Testing?
Performance testing is the process of systematically determining, quantifying and improving the speed, reliability, and efficiency of an application with the aim of improving user experience. This includes both front-end and back-end performance testing.

Load testing is a specific type of back-end performance testing where automated scripts are written to send requests in an attempt to simulate the peak user load expected on the application servers.

Stress testing takes that one step further and applies load in excess of what is expected in order to determine the maximum capacity of the system under test.

### What is the difference between front-end and back-end performance testing? Which one is more important?
Both front-end and back-end performance testing measure how fast an application responds, but they measure different components of that overall user response time.

Front-end performance is concerned with how quickly text, images, and other page elements are displayed on a user’s browser page. Back-end performance is concerned with how quickly these elements are processed by the site’s servers and sent to the user’s machine upon request. Front-end performance is the part of the iceberg above the water line, and back-end performance is everything underneath that you can’t see.

Both are important because they can both determine whether a user continues to use your application. Front-end performance tends to be easier to test and can provide some quick wins due to the large amount of optimisation tweaks that can be done without writing code. Back-end performance tends to be more difficult to test because it often uncovers problems with the underlying infrastructure and hardware that are of a more technical nature.

### Why does performance testing matter?
Performance testing matters because application performance has a significant impact on user experience. A site that is unreachable or slow to load due to an inability to cope with unexpected load will cause users to browse to competitor’s sites and tarnish the brand’s reputation.

### How do you know when a load test has passed?
Ideally, you would have discussed your nonfunctional requirements with key stakeholders before load testing begins. This means that you set your own pass criteria before you even run the tests. You would ideally have a list of specific transactions (selected based on criticality or complexity according to the business) whose response time needs to fall under a threshold you’ve predetermined. “Fast” is not specific enough-- a number is better. Depending on what kind of tests you’re running (soak, stress, volume, etc) you may have other nonfunctional requirements about duration, resource utilisation on the server side, or specific outcomes to scenarios you’d like to test.

As a general rule, don’t rely on a load test tool to determine whether your load test has passed. Rely on it to report your results, but always compare the results to the requirements to determine successes or failures.

### What would you advise to clients who say they can’t afford to performance test because they don’t have the resources to maintain several load generators on site?
This is the main reason that performance testing has for so long been considered a luxury that only big companies can afford. Luckily technology moves on, and in 2018 we’re at a point where everyone can load test. The big innovation here has been the cloud and the ability to spin up thousands of virtual machines with a few mouse clicks. Services like Amazon AWS, Microsoft Azure and Google Cloud make it so that every budding entrepreneur can “borrow” the computing hardware necessary to do cloud load testing with thousands of users and then give them back after the test, without the hassle and cost of maintaining them. I would advise the clients to look for a a cloud load testing solution that utilizes virtual machines on the cloud to run their tests affordably.

### You run a load test against a server with 4GB RAM and the results show an average response time of 30 seconds for a particular request. The production server has been allocated 8GB RAM. What would you expect the average response time of the same request to be in production given the same load?
Trick question! While you may be tempted to answer that the response time would be halved to 15 seconds, reality is rarely that convenient. Response times are a factor of so much more than memory. Things like CPU utilisation, network throughput, latency, load balancing configuration, and just application logic are always going to influence load tests. You can’t assume a linear progression in response time just because you’ve upgraded one part of the hardware. This is why it’s important to load test against an environment that is as production-like as possible.

### What is a percentile and why would you look at percentile response times when you already have average response times?
A percentile is a statistical measure that describes a value that a certain percentage of the sample either meets or falls under. For example, a 90th percentile response time of 5 seconds means that 90% of the responses took 5 seconds or less to be returned. It can be an important measure because they soften the impact that outliers have on more inclusive measures such as averages. A transaction with an average response time of 2.5 seconds may seem perfectly acceptable to the business, but when the 90th percentile response time is 20 seconds, this is a good reason to investigate further.

### What are some trends in performance testing that you think will continue in 2019 and beyond?
Cloud is an easy answer, as the cloud brings some compelling benefits in terms of reduced cost and just ease of use. However, I already touched on that in a previous question, so I’ll talk about another trend: open source.

There’s a reason that open source is still around: it works. The main advantage of open source tools is not that they are free, although that is a big part of the appeal. The real advantage is that open source tools are community-based and community-led, which means features get built for it faster than sometimes commercial tools can keep up with, and they’re built by users of the tool themselves. Open source tools like [JMeter](http://jmeter.apache.org/), [Gatling](http://gatling.io/) and [Selenium](http://seleniumhq.org/) have revolutionized the industry due to their impressive feature sets, built by a growing community that has developed plugins for everything you can think of. More and more, even big companies with big budgets choose to go open source simply because of the wealth of knowledge of these tools that are already available for free.

We’re huge proponents of open source tools at Flood, which is why we recently open-sourced our very own tool, [Element](https://element.flood.io/). We will continue to support all things open source, because we firmly believe that the future is open source.