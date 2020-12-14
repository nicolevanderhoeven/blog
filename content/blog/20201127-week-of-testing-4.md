---
title: "Week of Testing: Day 4 - Load profiles on k6"
date: 2020-11-27T19:54:06+01:00
draft: false
tags: ['performance', 'k6.io', 'video']
---

{{< youtube jDmMmc75RRM >}}

k6 has a cool feature where even if you start a load test locally via the CLI, you can still stream the results to k6 Cloud. It's an interesting compromise between debugging a test locally (and therefore not paying for cloud infrastructure) and sharing results for load tests run on the cloud. It worked seamlessly, too.

I also wanted to see how to recreate a specific load profile that I commonly use - the stepped load profile. In JMeter, I typically do this with a plugin - the jp@gc Ultimate Thread Group is my thread group of choice. So, I created it in JMeter (I love that it shows a little image of it as well, while you're building it) and then attempted to recreate it in k6.

I definitely had to look at the k6 documentation for this. I used the `constant-vus` executor for this, but k6 has [several other executors](https://k6.io/docs/using-k6/scenarios#executors) to choose from, and it worked as well as I had hoped.

So far, my experience with k6 has been positive. Things are well-documented, and they just work out of the box. No plugins necessary.