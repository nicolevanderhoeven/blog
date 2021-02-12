---
title: "Pros and Cons of API load testing"
date: 2020-08-18T21:22:49+01:00
draft: false
tags: ['performance', 'flood.io', 'english', 'text', 'flood element', 'selenium']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/pros-and-cons-of-api-load-testing">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/pros-and-cons-of-api-load-testing)._

‍API load testing is one of the most popular ways to run a load test because of the number of open source and commercial load testing tools available on the market that support it. Creating a script to hit your application's API endpoints is the traditional approach to load testing, but it's not the only one.

Here are some things to consider when deciding whether or not API load testing is right for your application.

## Disadvantages of API load testing

### API load testing does not simulate real users interacting with elements of your webpage.

‌In contrast to a customer opening up a browser and filling out forms on your site, an API load testing script will consist only of the underlying requests to the server that are made by clicking on those on-screen elements. Exactly how the customer triggers those requests, and what buttons they’ve pressed, is irrelevant. It’s all about the raw requests.‌

The format of these requests will be dictated by the type of API your application uses, and it may take some technical knowledge or expertise to be able to formulate requests correctly. However, a RESTful API is one of the most common types, and it is considered to be relatively simple to use.

![](/assets/20200818-01.png)
_HTTPS requests for amazon.com. This is what an API load testing script would need to replicate._

### It doesn’t give you an idea of how user-friendly your application is.

‌API load testing tools don’t give you feedback on how long your pictures took to render on your users’ browsers or whether that “SUBMIT” button is in an obvious spot.

### ‌It doesn’t measure front-end performance or how quickly pages render in different browsers.

‌While all the resources that the server returns can be downloaded by your tool of choice, there is no browser on which to run them.

### ‌API load testing doesn’t run client-side scripts.

‌It isn’t what you’re looking for if your application is a single-page web app that relies heavily on JavaScript or AJAX to dynamically populate and update the page. Your load testing tool will download the scripts, but not execute them.‌

‌This includes scripts like those required to trigger Google Analytics, which prompts many an engineer to question the results of an API load test due to the inability to see the traffic come in on Google Analytics. API load testing won’t help you with that. Running browser-level load tests using tools like [Flood Element](https://element.flood.io) or [Selenium](https://selenium.dev) may be more useful.

If you've decided that API load testing is not the best way to load test your application, you can look at browser-based load testing as an alternative.

![](/assets/20200818-02.jpg)

_Executing a browser-based load testing script using Flood Element._
‌
## ‌Advantages of API load testing

Now that we’ve talked about what API load testing isn’t good at, let’s talk about what it IS good at.

‌### It allows you to load test specific servers rather than the whole stack.

‌API load testing allows you to tailor your load testing by applying load only on particular servers. This is particularly useful in more complicated applications that involve several components and would require substantial effort to reproduce in a test environment. Using APIs, you can test only the functions you want to test.

### It is well-supported. ‌

API load testing has been around for decades. There are lots of robust tools you can choose from, both commercial and open-source, and many of these tools have large communities and extensive documentation around how to script the most common cases. It’s a far cry from the browser-level testing space, which is relatively new and sparsely populated by comparison.

‍![](/assets/20200818-03.png)
_The [JMeter site](https://jmeter.apache.org/usermanual/index.html) contains a wealth of information, including a User's Manual_
‍
### It’s not as resource-intensive as browser-level testing.

You can simulate more users with API load testing than with browser-level load testing. Since most interactions on the browser-level get translated to requests anyway, generating load this way is incredibly efficient, allowing you to hit your server with requests while bypassing the UI layer and the resource overhead that that entails.

For example, at [Flood](https://flood.io) we’ve baselined some of the tools that we support to see how many users we can run on an AWS m5.xlarge instance:

Selenium: 5 users
Flood Element: 20-40 users
JMeter: 1000 users
Gatling: 1000 users

‌You’ll see that the browser-level test tools, Selenium and Flood Element, can run significantly fewer users on the same sized node as can the protocol-level tools, JMeter and Gatling. This isn’t due to an inefficiency in the tools but rather to the fact that browser-level tools inherently need more CPU and memory to start separate instances of browsers per user and render pages graphically. You can run more users per node (or machine) by carrying out API load testing with protocol-level tools.

### It’s cheaper.

‌The efficiency in resource utilization translates directly into cost savings because every node that you don’t need to execute your tests on is one fewer node that you’ll have to pay to provision (whether on premises or in the cloud).

‌For this reason, API load testing is one of the most cost-efficient ways you can get started with load testing, allowing you to scale up your load relatively cheaply while getting immediate results.

## How to get started with API load testing

API load testing isn't for every application, but depending on your test scenario, it may be the easiest way to test application performance.

If you're new to non-functional testing or API load testing in particular and would like some step-by-step tutorials on how to get started, check out my free ebook, [API Load Testing: A Beginner's Guide](https://guides.flood.io/ebooks/api-load-testing). It takes you through the basics of API load testing, including planning your first load test, selecting an open source tool, scripting, executing a test on the cloud, analyzing results, and even integrating it into your CI/CD pipelines.