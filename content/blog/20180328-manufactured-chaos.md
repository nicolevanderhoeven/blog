---
title: "Manufactured Chaos: How Netflix Does Performance Testing"
date: 2018-03-28T23:35:52+01:00
draft: false
tags: ['text', 'english', 'chaos engineering']
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/manufactured-chaos-how-netflix-does-performance-testing">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/manufactured-chaos-how-netflix-does-performance-testing)._

It’s always ideal to run performance tests against an environment that’s production-like. That way, you can ensure that your tests aren't being influenced by factors that are not present in production - such as sub-optimal specifications, or the configurations of a test server. So, what does a good performance tester do? They compare their machine specifications and request production-sized boxes to run their tests against. But is that really enough?

Here's the reality: despite our planning, we still sometimes see things in production that we don’t see, and can’t reproduce, in the test environment. It's hard to predict every possible failure. Even if you do recognize the danger, it’s still difficult to recreate the perfect storm of circumstances that could potentially lead to its occurrence. The more complex your network architecture is, the more likely it is that these failures will occur. As a result, there’s something of a “don’t breathe or it might break” feeling that comes with deploying to production. So how do you test your application to get the maximum degree of confidence in its performance?

If you’re Netflix, your answer would be to **lean into the chaos**.

Chaos theory, in a nutshell, tells us that what looks random actually contains patterns that, while unpredictable, are recognizable and thus manageable. Far from representing disorder, chaos is our word for events that may be infinitely complex and interconnected in ways that aren’t immediately apparent. Chaos engineering takes this principle and applies it to software. Developers can code to reduce the occurrence of chaos as much as possible, but they can also code to make sure applications can withstand chaos if it does occur. As testers, one way we can test the latter is to manufacture chaos.

Netflix’s testing strategy puts a lot of emphasis on manufacturing chaos because their business model involves streaming gigabits of data to customers on demand, from anywhere in the world, at a consistently fast enough speed that people aren’t annoyed by buffering in the middle of a rousing speech by the Mother of Dragons. In 2015, Netflix accounted for 36% of traffic in [North America](http://fortune.com/2015/10/08/netflix-bandwith/). Netflix customers stream 125 million hours of video [every day](https://www.wired.com/2016/03/netflixs-grand-maybe-crazy-plan-conquer-world/). Netflix used to serve the content from their own private data centers but moved to the cloud in 2008 after a database corruption disrupted their business for three days. Today, Netflix is 100% in the cloud, which provides tangible benefits such as architecture that can scale on demand thanks to their use of Amazon Web Services (AWS) - incidentally, the same CDN that we use here at Flood IO. However, even the cloud isn’t invulnerable to chaos. Enter the Simian Army.

![The Simian Army at Netflix](/assets/20180328-01.png)

Conjuring up the humorous image of a squadron of monkeys wreaking havoc in a data center, the Simian Army is a series of tools developed by Netflix that code chaos into their tests - on purpose. At Netflix, every build has to pass not just the standard suite of functional and nonfunctional tests, but also the chaotic-but-programmable tests of the Simian Army, all of which Netflix have made available as open-source tools on Github. Each monkey is a real-world manufactured-chaos test that the application under test must pass in order to be deployed into production with a high degree of confidence in its stability and continued performance.

**Chaos Monkey** selects a node or container within a node at random and terminates it unexpectedly, forcing Netflix engineers to adapt their code to deal with this behavior by quickly rerouting requests to backup nodes and containers.

**Janitor Monkey** detects unused resources (instances, volumes) in the cloud and terminates them. Ideally, all resources no longer used should be shut down, but in practice this doesn’t always happen. People forget to delete things they’re not using anymore. Applications are changed to use new volumes, and old ones are forgotten. While it’s a good idea to make sure everyone is aware of the need to clean up after themselves, Janitor Monkey assumes that things will fall through the cracks and automatically comes to the rescue. Janitor Monkey also sends a notification to the owner of the resource with enough time to mark the resource as an exception before deletion.

**Conformity Monkey** scans instances and determines whether they conform to a set of rules specified by the organization. If an instance is not configured the right way, Conformity Monkey sends the owner a notification. It can detect things like an instance being created without the appropriate security groups or tags.

**Security Monkey** monitors your entire public or private cloud to look for policy changes or incorrectly configured instances that could lead to serious security breaches. It even provides a UI so that you can see a history of changes to important policies and whom they were made by.

**The Simian Army** is a marked departure from traditional software testing techniques, which are very much procedural and based on predetermined flows. The assumption is that people behave logically, are all experts in their field, forget nothing, and always follow best practices. But is this actually realistic?

Netflix’s approach to testing is innovative in that they don’t assume that everyone involved knows exactly what they’re doing, from the developers to the infrastructure engineers to the testers. Neither do they assume that it is always possible to know the exact cause of failures in production. Sometimes bad stuff just hits the fan and nobody sees it coming. The very nature of our work in technology requires constant change, and it can be difficult to keep up with all the ways in which applications are becoming increasingly more integrated with each other. This will only become more apparent as the Internet of Things becomes more popular.

At [Flood](https://flood.io/), we often see our customers targeting production environments, and there are some strong arguments for doing this. Testing later in the lifecycle means we can start to tackle production-sized problems around availability, scalability and reliability that would have otherwise been difficult to reproduce. Let’s face it. We all sometimes see monkeys in our data centers. Maybe it’s time we started planning for it.

## References:
[Completing the Netflix cloud migration](https://media.netflix.com/en/company-blog/completing-the-netflix-cloud-migration.)
[What is chaos theory?](http://fractalfoundation.org/resources/what-is-chaos-theory/)
[Principles of chaos engineering](http://principlesofchaos.org/)
[The Netflix Simian Army](https://medium.com/netflix-techblog/the-netflix-simian-army-16e57fbab116)
[Chaos engineering - surviving the failures in distributed systems](https://medium.com/becloudy/chaos-engineering-surviving-the-failures-in-distributed-systems-5688c6905dbb)
[Chaos engineering series - Part 1: chaos engineering deep dive](https://www.linkedin.com/pulse/chaos-engineering-series-part-i-deep-dive-sathiya-shunmugasundaram/)
[What is Simian Army?](https://github.com/Netflix/SimianArmy/wiki)