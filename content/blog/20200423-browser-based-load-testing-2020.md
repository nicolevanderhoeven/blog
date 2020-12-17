---
title: "Browser-based load testing in 2020"
date: 2020-04-23T16:48:09+01:00
draft: false
tags: ['performance', 'browsers', 'jmeter', 'gatling', 'selenium', 'element', 'puppeteer', 'english', 'flood.io', 'text']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/browser-based-load-testing-in-2020">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/browser-based-load-testing-in-2020)._

We [first announced](https://flood.io/blog/level-up-your-load-testing-with-browser-level-users) our open-source browser-based load testing tool based on Puppeteer, [Flood Element](https://element.flood.io/), in February 2018. Despite our decision to make it an entirely separate tool from Flood, we've enjoyed using it so much as a team that several of us have written about it:

Tim Koopmans: [Load testing for DevOps... with Browser Level Users (BLU)](https://flood.io/blog/load-testing-for-devops-with-browser-level-users-blu)

Kevin Dunne: [A new approach to load testing with browser level users](https://flood.io/blog/a-new-approach-to-load-testing-with-browser-level-users)

me: [Prepare for viral videos with Flood Element](https://flood.io/blog/prepare-for-viral-videos-with-flood-element)

Lachie Cox: [Why should you load test with real browsers?](https://flood.io/blog/why-you-should-load-test-with-browsers)

our friend Eduardo Riol, as translated by Antonio Jimenez: [Puppeteer vs. Selenium for test automation: is a new leader emerging?](https://flood.io/blog/selenium-vs-puppeteer-for-test-automation-is-a-new-leader-emerging)

Clearly, we're huge fans of load testing a web application with real browsers. But does the wider software testing industry share that sentiment?

## Browser-based load testing in 2020

Browser-level load testing is still pretty new, and there aren't too many providers offering it right now. Luckily, we just so happen to have access to a database of load tests run on Flood since 2013. Here's a bar chart visualizing data we've collected about the load testing tools flooders have used (we support Selenium, JMeter, Gatling, and Element).

### Load tests executed on Flood over time, grouped by load testing tool

![](/blog/assets/20200423-01.png)

### Browser-level load testing is increasing in popularity

#### In 2020, almost 35% of the load tests run on Flood are browser-based load tests.

While the total number of load tests run across all tools increased across the board, the percentage of tests that utilized Selenium and Element, as compared to JMeter and Gatling, has also increased from 2018. Both Selenium and Element are browser-based load testing tools.

By contrast, JMeter, a protocol-level load testing tool which previously enjoyed a 70% share of the traffic on Flood, now accounts for only a bit over 50% of usage. JMeter's share of the protocol-level pie is higher than Gatling's, but the percentage of usage for both tools appears to be contracting when compared to that of browser-based tools.

### Element use is increasing faster than Selenium use

Despite the fact that Selenium has been around longer, **25% of all floods today are run using Element**. This is a significant increase in just two years, and one that bodes well for the future. While we're still fans of Selenium and still support it, one reason we see for the dominance of Element in today's market is resource efficiency.

In our baseline tests, we've seen that Element can run from 20-50 users per Flood node (an [AWS m5.xlarge instance](https://aws.amazon.com/blogs/aws/m5-the-next-generation-of-general-purpose-ec2-instances/)), whereas Selenium can only run up to 5. This leads to some significant cost savings, as running the same number of users with Element requires fewer load generators than with Selenium.

Another reason might be the fact that Element uses Puppeteer in the background. Puppeteer, developed by Google, understandably shines when driving Google Chrome (and recently, Firefox). Puppeteer load testing is growing in popularity due to the wealth of metrics it has access to.

## How browser-based load testing works

Traditional load testing is done on the protocol level by sending messages directly to the web server. These messages are sent without simulating the application interface, and the responses that are received from the server are not visualized, either. "Users" in protocol-level load testing scripts are actually threads, with each one sending a list of messages at predefined intervals, and we refer to these users as Protocol-Level Users (PLU). JMeter and Gatling use PLU to generate load.

The screenshot below shows what one request for a single action might look like in a JMeter test plan.

![](/blog/assets/20200423-02.jpg)
_Example of an HTTP request with parameters on JMeter_

In browser-based load testing, real browser instances are opened on load generators, and the load testing tool plays the part of a real user in navigating the web application using the GUI. We refer to the virtual users in browser-based load testing as Browser-Level Users (BLU).

Here's an example of the same action in the JMeter example above, but this time in an Element test script:

```javascript
step('Step 1', async browser => {
    //Click Start button
    let startButton = await browser.findElement('.btn-default')
    await startButton.click()
})
```

This version simply describes the button to be found and clicked, whereas the protocol-level version needs to be more precise in what exactly is passed to the server.

Both types of load testing tools can apply the same load on an application (as long as it supports both methods— see the next section). The main difference is in how the load is generated.

A protocol-level script will contain instructions on which messages to send, which protocols to use, which headers to include, and other information that a typical end-user would not see.

A browser-level script will contain instructions on how to _interact_ with the application: which buttons to click, what to type in text fields, which links to follow, and other on-screen elements that an end-user would be familiar with. This leads us to one of the big advantages of browser-based load testing.

## Pros and cons of browser-based load testing

### Pros

#### Simple scripting— or no scripting at all

Protocol-level tools require in-depth knowledge about how an application works, what format it expects requests to be in, and how it responds. On the browser-level, you don't need to know any of that. When scripting a login process, for instance, you just need to tell the script to type a username and password in the right fields and then click Log In. The script doesn't need to know that the form submits an encrypted request using the Auth0 API (something you'd need to know for a protocol-level script).

In some cases, you might be able to get away with using something like our [qTest Explorer plugin](https://flood.io/blog/record-load-tests-in-flood-element-using-qtest-explorer) to record a business process, generating a script without any scripting at all. Even when you have to write or modify the script, though, it's a lot less intimidating than most protocol-level scripts.

They're also easier to troubleshoot. In addition to opening a real browser instance on your computer when you run a script locally, Element can also display this information on the console (shown here on iTerm):

‍![](/blog/assets/20200423-03.jpg)
_Screenshots upon execution on Element using iTerm_

‍This allows you to understand what's going on in the script and in the application, letting you detect bottlenecks faster.

#### Reduced test complexity

The streamlined requirements for scripting lead to a straightforward test. There's no chance of getting request parameters or values wrong.

#### Ability to test entire stack from the user perspective

Unlike testing APIs, you don't need to decide which server you want to hit or make sure you have the appropriate requests to hit all the servers. A browser-level test script interacts with page elements like a real user would, so all underlying application servers are tested. Pair this with [cloud-based infrastructure on Flood](https://guides.flood.io/infrastructure/demand-infrastructure/advantages-of-testing-in-the-cloud), and you've got a compact package for testing your application.

#### Capable of testing any user behavior

Protocol-level load test tools struggle with some types of applications, such as single-page apps (SPAs), where a lot of the processing is done on the client side. Browser-level load testing tools shine here, because scripted interactions for these apps are no different for SPAs than other web apps.

#### Record network and user interaction times for front-end optimization

Browser-level tools show you response times from the user's perspective: how long after a user clicks the log in button does the user see his or her account balance? This metric is a practical one that may differ wildly from the traditional response times that a protocol-level tool reports. Measuring real user experience is a great value add for your test.

#### Easier to maintain

Lower script complexity means that a browser-based test script is more resilient to changes in the codebase. A change in the underlying requests sent will not require a change in the test script, making it perfect for regression testing.

It's also easier to pass on to other members of the team due to high readability. Here's an example of how to select a value from a dropdown menu in Element:

```javascript
await browser.selectByValue('#challenger_age','34')
```

It's easy to see that the script is looking for an element with the ID "challenger_age" and selecting the value "34". This step could correspond to dozens of requests that need to be scripted if testing on the protocol level, which makes those scripts harder to understand without a proper handover.

### Cons

Browser-based load testing tools have a higher CPU and memory footprint than protocol-based tools. Test scripts in JMeter and Gatling send messages to and record responses from a server without really needing to parse responses. By contrast, browser-based tools parse the server response in order to access the Domain Object Model (DOM) elements on the page.

Using real browsers might be closer to the real user experience, but it also takes its toll on node resources. It is possible to run in headless mode, where browsers are started "invisibly" without actually graphically rendering them. However, even then, a browser-level tool can run fewer concurrent users on a node than a protocol-level tool.

## Best tools and applications for browser-based load testing

While other commercial tools exist for this, we're partial to open source tools at Flood.

### Selenium

![](/blog/assets/20200423-04.jpg)

Selenium load testing is appealing because Selenium is already well-known for test automation and functional testing, and a lot of companies already have full test suites in Selenium. The possibility of reusing those resources and just running them at scale as load tests is, by far, the most compelling reason to use Selenium.

### Puppeteer

![](/blog/assets/20200423-05.jpg)

Google's just getting started with Puppeteer, and the amount of metrics it exposes is exciting: it seems like anything in Chrome Developer Tools can be accessed by Puppeteer. Imagine running a load test on ONE tool that gives you statistics about back-end performance (response times, the effect of bandwidth restrictions, resources returning errors) AND front-end performance (client-side script console logs, render times, time to first paint, etc). It's hard to imagine a future where this ISN'T a valuable tool in the performance arsenal.

Under Puppeteer, of course, is [Element](https://element.flood.io/)— our load-flavored version of Puppeteer.

![](/blog/assets/20200423-06.png)

## Is protocol-based load testing dead?

No. Testing on the protocol-level may have its drawbacks, but it's popular for a reason. If you're testing mobile apps or API endpoints, protocol-level testing tools allow you to focus on hitting what you want to test and only what you want to test. Sometimes you don't want to test the whole stack. It really depends on your test scenarios.

Plus, protocol-level tools tend to be really resource efficient. We've been able to easily run about 1000 users per Flood node with JMeter and Gatling, easily outstripping browser-level tools. It makes sense, since JMeter and Gatling don't need to start browser instances to generate load.

It's significantly cheaper to generate very high loads with protocol-level tools. This efficiency makes protocol-level tools a good choice for high concurrency load testing and especially stress testing.

## What are we doing to support BLU?

Clearly, our usage metrics show that browser-based load testing is on the rise, and we're planning to ramp up our offerings in this area while also maintaining support for protocol-level tools. Here's what you can look forward to from us:

* New releases
    * We just released [version 1.2.3 of Element](https://element.flood.io/docs/1.0/install) a few weeks ago, which addresses some bugs and improve stability for certain actions.
* Dedicated Element team
    * We've put together a team of developers who will be focusing on improving Element exclusively. Despite Element being an open source tool, we're putting our own resources behind it to improve it faster.
* Partnering with consulting services
    * It can be difficult to get started on a new tool, and Element is no exception. While we provide a load testing platform to run Element scripts, some companies want help to create the scripts in the first place. To this end, we've partnered with expert consultants who have already been using Element with great success: [Foulk Consulting](https://foulkconsulting.com/) and [Planit Testing](https://www.planittesting.com/).

## Conclusion

When choosing a performance testing tool, it's important to consider the advantages and disadvantages of protocol-level and browser-level testing tools. We think both types of tools deserve to be in a solid performance and load testing strategy. They can also be used in tandem in a hybrid load testing approach, improving overall application performance and scalability.

In 2018, we predicted that testing web-based applications with real browsers would increase in popularity, so we're thrilled to see our theory validated in 2020. Browser-based load testing is increasing in usage, and our open source tool, Element, is leading the charge. It's exciting to be at the forefront of this revolution, and we intend to increase support for load testing with real browsers even more this year.