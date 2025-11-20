---
title: "Lightweight Opensource APM with OTel Demo (Grafana ❤️‍🔥 OpenTelemetry Community Call #2)"
date: 2025-11-19T14:48:59+01:00
draft: false
tags: ["opentelemetry", "english", "video", "grafana labs", "grafana otel community call"]
---
This community call with my coworker Liudmila Molkova featured an interview with Cyrille Le Clerc from Grafana Labs, focusing on the OpenTelemetry demo as a practical example of a lightweight, open-source Application Performance Monitoring (APM) solution. Cyril explained the purpose and architecture of the OTel demo, highlighting its role as a realistic, complex microservices application that has become a de facto standard for observability vendors. The discussion explored the modern definition of APM, followed by a detailed walkthrough of a Grafana dashboard built on OTel data, covering RED metrics, alerting, trace correlation, and infrastructure monitoring. A significant portion of the conversation was dedicated to the role and challenges of integrating logs within an OpenTelemetry framework. The interview concluded with a look at the future of the OTel demo, including plans for AI observability and eBPF instrumentation.

{{< youtube cX74hkdI1zM >}}

## Transcript

### Introduction

**Liudmila:**  
Okay. Hi everyone. Welcome to the second Grafana and OpenTelemetry community call. This time we're going to talk about the lightweight open-source APM and we will use the OpenTelemetry demo as our playground. We have an expert, Cyrille, who works at Grafana. Cyrille, do you want to introduce yourCyrillef?

**Cyrille:**  
Thank you very much, Liudmila. My name is Cyrille, and I am a product manager at Grafana Labs. I've been working on open-source products for 15 years, first on Jenkins for CI/CDs, then at Elastic on observability, and now at Grafana Labs, also on observability. In addition to my day job, I have been an open-source contributor for about 20 years, starting with Apache Java projects and then moving on to Jenkins integration with Maven and OpenTelemetry. Now, I focus more on the OpenTelemetry project, like the OpenTelemetry demo, and I contribute to OpenTelemetry Helm charts as well. At Grafana Labs, I am the product management lead in charge of OpenTelemetry and I cover other areas as well. [laughter]

**Nicole:**  
That's great. It's great to have you here with us. Also, great for my internet to act up just a few minutes before this. Anyway, hi! I’m Nicole van der Hoeven, a developer advocate at Grafana. I work with Cyrille over there, and I'm really excited to be talking about OpenTelemetry. I'm the newbie of all of us here. [laughter] I have used OpenTelemetry in some demo apps I've built. Most recently, I used it for instrumenting an AI app. I'm excited to ask Cyrille all my questions because when he says he likes OpenTelemetry, what he really means is he's the guy at Grafana who's always banging on that OpenTelemetry drum. He's like, "Tell all the things!" [laughter]

**Liudmila:**  
It's probably my turn. I'm Liudmila. I work on the OpenTelemetry project and I'm a technical committee member. To echo what Nicole said, nobody knows all of OpenTelemetry, and this call is where we will uncover areas that are new to each of us. Going forward, we'll probably have more of these calls. So, with that, let’s talk about the OpenTelemetry demo. Cyrille, what is it? Why do we care?

### What is the OpenTelemetry Demo?

**Cyrille:**  
So, the OpenTelemetry demo was born to showcase OpenTelemetry. OpenTelemetry was created in the context of cloud-native architecture. This demo is a cloud-native application—a distributed microservices application that is instrumented with OpenTelemetry. It's maintained by the OpenTelemetry community and showcases all dimensions of modern monitoring or observability, including all telemetry types: traces, metrics, logs, and more at every layer. We started with monitoring the application layer and are now extending to show the infrastructure layer.

We demo various technologies: Java, .NET, Node.js, and nearly all programming languages, including Rust. We also show how to instrument middleware and databases, such as Kafka, PostgreSQL, and Redis, all deployed on Docker Compose to make it easy to play with on your local desktop or deployed on Kubernetes to be more production-like. 

This is a complex demo that shows everything, and what's interesting is that it is realistic and currently used by 40 observability vendors to demonstrate their solutions with the OpenTelemetry demo. So, when you get familiar with the OpenTelemetry demo, it’s really easy to evaluate different vendors quickly. It comes "batteries included," with open-source monitoring and observability technologies like Prometheus, Jaeger, OpenSearch, and Grafana to showcase how to implement an observability solution with OpenTelemetry.

### Exploring the Application

**Liudmila:**  
Thanks for the intro! So maybe we should take a quick look at what the application itCyrillef looks like to make it more concrete. 

I'm connected to a Kubernetes cluster, and I'm just port forwarding. This is the telescope shop we have in the OpenTelemetry demo. We can go and buy things, and now we have something in the cart that we can place an order for. Oh, actually, this application might not work as expected. Well, that's why we need observability, right? If things don't work, we need to figure out what's broken and how to fix it.

Before we move on, I just want to show that even though you only see the front-end web shop, it's a relatively large application. It has quite a few services, databases, caches, a front-end proxy, and a log generator that consistently sends requests. 

We're super lucky to have all the telemetry Cyrille talked about. We have metrics in Prometheus, traces in Jaeger, and logs in OpenSearch, all visible in Grafana as a single pane of glass that you can refer to. With this, we can start looking at the telemetry itCyrillef. But I wanted to check with Cyrille or Nicole if you have any additional thoughts or anything we should cover here.

**Nicole:**  
No, I think you presented it well. It's a very complex topology because we want to demo everything.

**Cyrille:**  
Yeah, it's almost complex by design. You could probably have made this simpler, but it's supposed to approximate real applications that aren't simple. That's the problem with some of these other demo apps; they are so simple to deploy that they work because they're monolithic or something like that. This one is much more of a polyglot architecture, involving microservices that represent the real challenges that people face in the field.

### Application Performance Monitoring (APM)

**Liudmila:**  
One great thing about this demo is that sometimes it's hard to understand how someone onboarded an application to OpenTelemetry. The demo has a lot of information on what services are used, and it demonstrates what's been done to instrument this application with OpenTelemetry, which can help anyone with their journey in the OpenTelemetry space. Okay, wonderful! Let’s change gears and start looking at the APM dashboard. 

Before we go there, let's talk about what APM is for a second. Why do we care? What is it?

**Cyrille:**  
APM is a very old concept—over 15 years old. We’ve had several generations of monitoring tools. APM stands for Application Performance Monitoring. I see APM as a monitoring and observability technology that helps you monitor your application and understand its health. 

When I think about it, the first thing that comes to mind is understanding if my service is healthy or unhealthy. In a distributed architecture, I need to see my service in the context of the connections between services, typically represented with a service map. If I find something unhealthy, I need to drill down to see the health of a service. This means switching back and forth between the service metrics, which are more aggregated, and the traces, which give indications of how business transactions are executed. 

I also need to access logs to verify how things really happen and if there are messages that help me understand the problem. This is how I understand my service. Additionally, my service is deployed on a runtime and middleware, so I need to be able to zoom lower to see how it's behaving on the Kubernetes pod or Linux box. 

APM allows me to switch back and forth between all layers, zooming in and out all the time across all telemetry types. This is essential for understanding health and troubleshooting. Another dimension is detecting anomalies, so I can wake people up at night when something goes wrong. This is where I create alerts and notifications. 

In the past, with monoliths, we created many alerts, but now we adopt best practices with SLOs, observing workflows, and root cause analysis. This is my vision of APM and why I think it’s more important than ever.

**Nicole:**  
When you talk about application performance management or monitoring, do you differentiate that from the wider field of observability? Some people say APM sounds outdated because it focuses on the application or just on performance, which is ambiguous.

**Cyrille:**  
The monitoring landscape has evolved a lot. With cloud-native architecture, many things have changed, and we had to change our best practices. The best practices from 20 years ago in monoliths are not the same as today’s best practices for distributed cloud-native architectures.

There were disruptions in the past by innovators who focused primarily on traces, and we learned a lot from that. But now I think the landscape is getting more stable. We recognize the value in metrics, traces, and logs, and we’ve evolved our best practices to leverage the best of all three. 

Some people prefer to call it observability. I know there are nuances, but this is my current perspective.

**Liudmila:**  
It's good to synchronize on terms. It sounds like we are on the same page. 

**Cyrille:**  
Now, with microservices architecture, we focus more on alerting symptoms rather than causes, centering more on the health of the application and the service provided to users than on the infrastructure layer. So, application monitoring or observability is becoming the entry point for people in charge of keeping the systems running.

**Nicole:**  
Why don’t we take a look at the dashboard and go through it?

### APM Dashboard Exploration

**Cyrille:**  
We will cover different parts of the dashboard throughout the hour. Let’s start with the top row—the red metrics. You can call them duration, error, and request rate. 

**Nicole:**  
I believe the red metrics were created by Tom Wilkerson, who still works at Grafana. I think it was looCyrilley based on the Google SRE book, even though they didn't explicitly say “red” there.

**Cyrille:**  
When you think about any particular service, you would think about some well-known terminology, which might be service level indicators, or just your application. Service level indicators talk more about what's important for the application, while red metrics focus more on the telemetry itCyrillef, like the raw data behind your SLI.

One thing that stands out is the alerts. It looks pretty awesome to see that something violates the threshold we've set—probably high latency. Let’s explore it. We see it's been firing for 17 hours. That’s quite a duration.

**Nicole:**  
That’s not so good. Let’s see the alert on the latency. The P95 is firing for a specific operation. 

**Cyrille:**  
We can look at this chart, which shows the latency around P99, which is like 18 milliseconds. Is it really a problem?

**Nicole:**  
No, it was for the demo. It's very situational; it depends on your services. The focus was to show practitioners best practices for creating alerts on HTTP endpoints. Typically, you have two families of alerts: latency alerts and error rate alerts. 

**Cyrille:**  
We decided to take P95 as a commonly adopted indicator. Some take P99, but P95 is often more relevant. Something that's perhaps not noted here is that we take a time interval of 5 minutes. We wanted to provide this out of the box because it relates to the data collection interval, which is typically every minute for hotel setups and quite common in Prometheus. 

Having a 5-minute window is quite good. These are best practices we worked on, identifying good labels to help practitioners succeed by easily routing alerts to the right people and having the right notification schemes.

**Nicole:**  
Imagine if there was actually high latency. Now we can enable this view and look at the examples of operations with the worst performance—like the outliers you would see here. We use Jaeger as a store for telemetry, and if it were any other store that supports tracing, you would see something similar.

**Cyrille:**  
This brings us to the Jaeger UI. I don't want to spend a lot of time here, but it’s just another confirmation that nothing is visibly wrong with this operation. Things are just going a bit slower in the cloud, as usual.

#### Alert Analysis

**Liudmila:**  
We talked about alerts. There are other interesting things in this picture. For example, the request rate is pretty normal. If there were a spike in usage, we would see it here. The error rate looks good—there are no errors. By looking at these three metrics, you can get a basic understanding of the health of your system and this specific service.

**Cyrille:**  
This dashboard illustrates years of best practices that the industry has accumulated. We have layers of information. At the top, you have your service identifier, the last metrics received time, and the overview of the aggregated service red metrics. 

This aggregated view across all operations of my service will help you decide if this service is healthy or not. If you have doubts or think something is going wrong, P95 is good at surfacing outliers.

Typically, you will scroll down to the HTTP or gRPC operations, where you have the details broken down by operation. It’s likely that not all business operations have problems; it could be just a subset of them. 

Here you can see the outbound services. If you have a problem, this data will help you understand if it’s happening within your service or is it a downstream service. In microservices architecture, that’s always a question. 

**Nicole:**  
Are those dashboards powered exclusively by metrics?

**Cyrille:**  
Everything is powered by metrics, specifically the OpenTelemetry semantic conventions. Initially, the OpenTelemetry demo derived metrics from spans, which was a great idea four years ago, but it had some limits. Now, OpenTelemetry has standardized some semantic conventions for HTTP server calls, client calls, database client calls, RPC calls, and messaging. 

**Nicole:**  
I noticed during my time with the demo that the coverage of metrics is uneven across programming languages. Java, for instance, has great instrumentation, while in other languages, it depends on the instrumentation.

**Cyrille:**  
Yes, that’s true. It’s uncommon for OpenTelemetry instrumentations to emit logs these days, but let’s move on to that.

### Logs and Observability

**Nicole:**  
So, what’s the deal with logs? Why are they not as important?

**Cyrille:**  
Logs are traditionally outputted in stdout, and we’ve lost Nicole. [laughter] The challenge is that traces and metrics are captured by SDKs within your app, while logs come from external log collectors, making correlation tough. When we discuss with practitioners and tell them that the OpenTelemetry SDK can directly export logs, they often respond that their log processes are mature and they can’t disrupt them just to trust the new kid on the block.

It takes time to change your log toolchain. And while OpenTelemetry SDKs have capabilities to directly export logs, it’s not easy to get people to change practices they’ve had for 30 years.

**Nicole:**  
To demonstrate Cyrille’s point about correlation, the most basic way to correlate is by trace ID and span ID. When we capture distributed traces, we can also attribute logs to the specific operation. 

**Cyrille:**  
Yes, and when we look at a trace inside Grafana, we can see logs associated with it. 

**Nicole:**  
If we open the trace view, we can see the details for this operation. There are a bunch of attributes you can correlate to understand what happened.

**Cyrille:**  
Logs provide the details. I think the negative sentiment around logs came from the idea that they don’t work as well in distributed applications as they did in monolithic applications. We had to evolve our practices to log the right way for distributed applications.

**Nicole:**  
It’s user error because logs are the signals you can abuse the most. You can put anything in a log line, which causes issues. With metrics, you don’t have as much leeway, which makes it simpler to deal with.

**Cyrille:**  
Yes, and we need to convince users that going into log analytics tools is much more efficient than tailing logs directly.

**Nicole:**  
It is more complicated to analyze logs than traces because they aren’t always structured. 

**Cyrille:**  
Exactly. We have to help organizations better structure their logs for better value. 

### Questions and Community Engagement

**Liudmila:**  
We have a question here. “We are planning to adopt the LGTM stack as an observability platform. Is there any blueprint documentation aligned with observability 2.0?”

**Cyrille:**  
LGTM stands for Loki, Grafana, Tempo, and Mimir. It’s an integrated solution. Observability 2.0 is about unified telemetry—having everything correlated and not just reacting to errors. It’s about understanding business impacts when you decrease response times. 

**Nicole:**  
So, it’s more about understanding the overall system rather than just monitoring.

**Cyrille:**  
Yes, exactly. 

**Liudmila:**  
How do I know which metrics and traces to prioritize first when instrumenting a distributed system with OpenTelemetry?

**Cyrille:**  
We recommend starting with auto-instrumentation first. It provides metrics and traces at a technical level, and with HTTP, the endpoints are meaningful from a business standpoint. You start with auto-instrumentation and then add custom instrumentation on critical workflows.

**Nicole:**  
What’s the current state of the OpenTelemetry demo? Can it monitor infrastructure as well?

**Cyrille:**  
Yes, OpenTelemetry was born in the application layer, but infrastructure monitoring came a bit later. We’re working with the hotel demo folks to showcase better infrastructure monitoring done by OpenTelemetry.

**Liudmila:**  
If people want to contribute or try out the hotel demo for themCyrilleves, where should they go?

**Nicole:**  
I posted the link in the chat to the OpenTelemetry site. 

**Cyrille:**  
If you want to participate in the demo, we have community meetings, and I can share another link in the channel for more information.

**Liudmila:**  
Great! Thank you both for being here and for everyone watching. I think that's a great way to end this call.

**Cyrille:**  
Thank you very much! It was a pleasure to be invited and an honor. 

**Nicole:**  
Thank you!