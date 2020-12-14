---
title: "Week of Testing: Day 3 - Running a load test locally using k6"
date: 2020-11-26T19:31:33+01:00
draft: false
tags: ['performance', 'english', 'k6.io', 'video', 'jmeter']
---

{{< youtube y5tteMKZUqk >}}

I've had my fun playing around with k6 Cloud, the SaaS component. For Day 3, I thought it was time to jump into the heart of k6: k6 the [open source load testing tool](https://github.com/loadimpact/k6).

First impressions: logging was a little sparser than I expect, coming from having used load testing tools that just do this for me automatically. I think one of the first things I'll do with k6 is to create my own little "load testing starting script" that I'll always use, with all of the appropriate logging already set up.

Otherwise, I was really impressed with how quickly it installed. If you scrub over to the timestamp [1:46](https://www.youtube.com/watch?v=y5tteMKZUqk&ab_channel=k6&ts=106) in the video, you'll hear that I was actually expecting to have to speed up the installation process while editing to save time, but the installation actually finished before I could say that I was going to do so. By my count that was 7 seconds between hitting enter in my terminal and the download finishing.

**7 seconds**.

I can't help but compare that to [JMeter](https://jmeter.apache.org/). JMeter is honestly probably my go-to load testing right now-- it's not good for absolutely everything, but it's the tool that I reach for when I "just want to test this one thing". I've used it for years, and it's the tool that I know the most. But one of the issues with JMeter is that there's so much to do before it's actually usable.

Before you even open JMeter, you need to install Java, and when I first started in load testing, I spent a long time wrestling with getting setting the Java environment variable in Windows before my computer would even recognize that Java was installed. Then you need to install JMeter-- but any JMeter tester will tell you that there are some plugins that you just can't do without, and that really you should always install. That's why there are so many "best plugins in JMeter" lists ([here's my top 3](/blog/20200414-aaf11))... because most of them are necessary, but you wouldn't know that if you're new to JMeter.

The fact that k6 starts up in 7 seconds is... shockingly good.