---
title: "Week of Testing: Day 2 - Comparing tests against a baseline"
date: 2020-11-25T19:21:53+01:00
draft: false
tags: ['performance', 'english', 'k6.io', 'video', 'aws', 'continuous testing']
---

{{< youtube dcahi7-9pRs >}}

Day 2 of my Week of Testing!

Yesterday I ran my first load test on k6, and actually set up the thresholds wrong. I still maintain that there are some UI improvements that could still be made in that area, and that feedback was well-received. Apparently I'm not the only one who has made the same mistake.

Today I learned that on k6, you can actually set one test to be a baseline. There's so much I want to say on this topic - that's probably a whole blog post there - but for now, suffice it to say that having a baseline test to compare succeeding tests to is a key to a successful round of load testing. I was happy to see that k6 thinks so too, because that functionality is built into the UI by default.

I also think that being able to schedule a test regularly is fantastic for practicing Continuous Testing. Of course, teams already using CI/CD pipelines would probably get the most benefit out of running load tests using the command line rather than through the UI, but it's nice to know that scheduling is an option in the UI as well.