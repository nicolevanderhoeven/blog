---
title: "Basics of load testing with k6 and Grafana in 20 minutes"
date: 2021-10-12T01:04:02+02:00
draft: false
tags: ['english', 'video', 'performance', 'k6.io', 'grafana', 'observability', 'prometheus', 'presentation']
---
This was a video I pre-recorded in preparation for [the first Grafana EMEA virtual meetup](https://nicolevanderhoeven.com/blog/20211005-testing-with-k6-and-grafana-better-together/).

{{< youtube gvounvDSDGg >}}

In mid-June (just three months ago), k6 joined the Grafana Labs family. Many people didn't quite understand what the connection was between k6 and Grafana, but I thought it made a lot of sense.

Google's Site Reliability Engineering book talks about 4 golden signals that we should measure in a system: latency, traffic, errors, and saturation. Load testing provides 3 of those (latency, traffic, and errors), but it doesn't show saturation, and it doesn't give us visibility into the system.

Grafana brings observability. k6 brings data. They work really well together, which is why we've been using each other's products for a few years now, before there was ever any talk of an acquisition.

In this video, I talk about why k6 and Grafana are better together and also demonstrate:

- how to run a simple script in k6 OSS
- how to make sense of the results of a load test
- test execution options: running locally, sending results to k6 Cloud, and running a test from k6 Cloud-- all triggered using the CLI
- two different integration options to bring k6 and Grafana together: the k6 Cloud Grafana data source plugin and Prometheus Remote Write
