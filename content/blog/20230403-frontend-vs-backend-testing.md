---
title: "Frontend vs. backend: How to plan your performance testing strategy"
date: 2023-04-03T13:20:53+01:00
draft: false
tags: ['k6.io', 'text', 'english', 'performance', 'grafana labs', 'load testing']
---
*Originally posted [here](https://grafana.com/blog/2023/04/03/frontend-vs.-backend-how-to-plan-your-performance-testing-strategy/)*.

There are many aspects of application performance, but they broadly fall into two categories: frontend performance and backend performance. As a tester, it’s important to know the differences between the two and how that impacts the way you approach your tests.

In this blog, I’ll provide a high-level overview of frontend performance testing and backend performance testing, including pros and cons of each one. I’ll also explain why you need both if you really want a holistic view of how your application is performing. 

{{< youtube xVACRP5qIJI >}}

## Why (and where) to use frontend performance testing

Frontend performance testing verifies user experience [at the interface level](https://grafana.com/blog/2023/02/10/watch-how-to-pair-grafana-faro-and-grafana-k6-for-frontend-observability/). Basically, this entails everything a user sees when they access your web app, whether it’s on a laptop or other devices. This might involve automating user interactions with the site through the browser — for example, clicking on a button, filling out a form, or having scripts that load on the browser and run. 

![mockup of a site called "Crocs R Cool"](/assets/crocs-r-cool.png)
_In frontend testing, you're looking at how components of the UI respond._

The metrics we analyze for frontend performance tests are typically quite different from what we use for backend testing. Let’s say we want to know the time it takes for a page to render after a user clicks on a button that directs them there. This isn’t the same thing as measuring server response time; that total round trip takes a lot more into account — things like latency or the time it takes for a client-side script to run and display the requested information.

### Advantages of frontend performance testing

The great thing about frontend performance testing is that it provides a more realistic measurement of your end users’ experiences. They don’t care what’s going on under the hood; they care about the overall experience — and that’s exactly what frontend performance testing measures. Unlike backend performance testing, frontend performance testing looks at everything from a user’s point of view: from the time they visit a webpage to the time they can interact with something on that page.

On top of that, most (about 80%) of the performance issues end users report are frontend issues. It doesn’t make much sense to skip this type of testing; it can be a critical step in finding ways to improve the overall user experience.

### Disadvantages of frontend performance testing

The most obvious disadvantage of frontend testing is that it doesn’t look under the hood. If you only do frontend testing, you’re almost certain to miss something. Maybe a component isn’t working, which is creating issues for your users. But you wouldn’t know that because you’re only testing what’s visible from the browser. In other words, you might be in the situation where you know something in the application is wrong and responding too slowly, but you don’t know what.

Frontend performance testing can also be quite expensive compared to, say, protocol-based testing. That’s because you need enough resources (memory and CPU) to actually spin up a browser instance and interact with your application the way that a real user would. The same load generator that could run tens of thousands of backend virtual users may only be able to run 50 frontend virtual users before running out of resources.

Finally, only testing frontend performance can sometimes lead to pretty misleading results, especially as you scale. As load increases, the response time for the frontend remains fairly constant, but that’s not the case with the backend. 

![graph plotting response time over the number of concurrent users for front-end and back-end](/assets/Frontend-Backend-LoadTesting.png)

_While the frontend component of response time remains more or less constant, the backend component of response time increases exponentially with the number of concurrent users._

This phenomenon occurs because most of the issues that frontend performance tests might identify, such as a slow-running client-side script, don’t tend to compound. It’ll be just as slow on each user’s computer regardless of how many users are running it. However, problems uncovered by backend performance testing are on the side of the application, not the users. If a database can’t keep up with 100 users sending queries to it, then 1,000 users sending it queries is likely to yield an even worse response time.

## Why (and where) to use backend performance testing

As you might have guessed at this point, backend performance testing targets the infrastructure under the hood. This could be a database that contains customer information, a payment gateway, or an authentication service for customers that have already signed up. These are things that an end user doesn’t see and maybe isn’t ever even aware of, but they still have an effect on response times. 

![graphic of application components](/assets/backend.png)

_Backend testing addresses infrastructure users might not even be aware of, like different databases, gateways, and services that underpin an application._

Scripting against the backend is quite different from scripting against the frontend. Instead of scripting user interactions like clicking, you’re scripting certain requests that are being sent on the protocol level. So, for example, you could have an HTTP GET request for the page and also for its embedded resources. 

```javascript
import http from 'k6/http';
import { sleep } from 'k6';

export default function () {
  http.get('https://test.k6.io');
  sleep(1);
}
```

The sample Grafana k6 script above is an example of a simplified backend performance test. It makes a single HTTP request to retrieve the contents of [https://test.k6.io](https://test.k6.io), and then waits one second.

Backend performance includes things beyond just load times and latency. It includes scalability, availability, reliability, and similar attributes, so the metrics that we measure are different as well. We might look at server uptime or response times per component. We could also trace the path of a particular request through the application stack.

An illustration shows that performance testing can address scalability, elasticity, availability, latency, resiliency, and reliability.
Application performance is more than just speed. Backend testing helps us verify many different aspects of performance.

![diagram of different types of performance](/assets/performance-ilities.png)

_Application performance is more than just speed. Backend testing helps us verify many different aspects of performance._

### Advantages of backend performance testing

As we already discussed, frontend testing doesn’t cover everything, but it’s also more complicated than that. The 20% or so of performance bottlenecks that are backend-related can be the hardest to troubleshoot, identify, and fix. Even worse, a lot of backend performance issues can spiral out of control at higher levels of load and can be quite expensive to fix later on in a development cycle. The worst time to realize that you need to rethink your entire infrastructure is after it’s already failed in production. If you take care of backend performance testing earlier (commonly known as shifting left), it makes such pivots less costly.

Another advantage of backend testing is the ability to target different components of an application. You can choose which API endpoint to hit and how hard, and you can target specific user flows, so it doesn’t always have to be end-to-end testing. 

And finally, backend performance tests tend to be less resource-intensive; they’re just protocol-level requests that can be easily ramped up.You don’t need to spin up a browser instance, or even parse through the Document Object Module (DOM) of a webpage or look for specific elements. It’s just a matter of sending these requests, and that’s something that you can increase the scale of pretty cheaply. 

### Disadvantages of backend performance testing

Backend performance testing won’t tell you anything about what’s happening on the frontend, and a lot of sites these days actually use scripts that have to run on the frontend. So with backend performance testing tools, you just download those scripts. But the response time they measure is the download time, which is not really realistic because those scripts are executed. A backend performance test would fetch the text of the script. A frontend performance test would run it — and that script might do something like perform a calculation. You need frontend performance testing to measure that properly.  

Backend performance testing is also much more expansive than front end performance testing, especially with microservices-based applications. There are so many components to track that it can be difficult to determine where to look. You can quickly find yourself going down a rabbit hole of constant, never-ending performance tuning. 

## Frontend + backend testing for the win

So, as we’ve seen, frontend testing and backend testing both seem to have advantages and disadvantages. So which one should you use? Both, if at all possible! They look at different parts of application performance, so doing both is essential if you want a holistic view of user experience. 

![diagram of k6 being used for both frontend and backend testing](/assets/frontend-vs-backend-meta.png)

_Software teams can use Grafana k6 to address frontend and backend performance testing._

If you’re operating at a smaller scale, use your own discretion about how to find the right mix for needs. But if you’re testing at a larger scale with thousands of users and you want to test both the frontend and backend aspects of application performance, I suggest you change your test strategy so the majority of the load is generated with backend performance testing scripts. That’s because of the resource intensiveness of frontend performance testing scripts, which we discussed earlier. 

So, if you generate most of the load with the backend and then you have a handful of frontend performance testing scripts running in the background, you should still get a good idea of how both are performing. Remember, frontend application performance remains fairly constant throughout different levels of load, so you’ll still get a lot of useful insights on both types of performance without worrying too much about the scaling costs.

Frontend and backend performance both affect what your end users think of your application. If the underlying application servers respond immediately to all requests, but then a huge picture of a crocodile makes your homepage excruciatingly slow to load, then users aren’t going to like that. 

On the other hand, if your homepage is really sleek and quick to load, but the application server hasn’t responded with the data that the browser needs to render, then users aren’t going to like that either.

A common problem when testing both frontend and backend performance is script duplication: because of the differences in the two approaches, you often have to use two separate tools — which means two test suites and potentially two scripting languages. While this is a valid approach, it’s more sustainable to look for a tool that can target both types of performance, such as k6. 

Whichever tool(s) you end up using, testing both frontend and backend performance is going to give you the clearest view of how your application really performs.

_The easiest way to get started with k6 is through Grafana Cloud k6. The free tier includes 500 virtual user hours/month for k6 testing and more. [Sign up for free now!](https://grafana.com/auth/sign-up/create-user?pg=blog&plcmt=body-txt)_