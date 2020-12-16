---
title: "On-premise load testing advantages and disadvantages"
date: 2020-04-30T23:06:59+01:00
draft: false
tags: ['performance', 'english', 'flood.io', 'text']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/on-premise-load-testing-advantages-and-disadvantages">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/on-premise-load-testing-advantages-and-disadvantages)._

Where you run your load test can affect the results that you get as well as your project's bottom line. In general, there are two infrastructure options to consider for load testing your apps: on-premise and cloud. Which type of environment is best for load testing both web or mobile apps?

## Differences between on-premise and cloud load testing

### What is on-premise load testing?

On-premise load testing is running your performance or load testing scripts on load generators you physically control. Typically, these load generators are machines that are either in your office or data center. In on-premise load testing, you are responsible for all aspects of the maintenance of the load generators, including hardware upgrades and software installations such as testing tools, but that also comes with increased control and security.

### What is cloud load testing?

In cloud load testing, you run your load tests on a service provider's machines, effectively outsourcing the provisioning and maintenance of your load generators. Running "on the cloud" means you're paying someone else to be responsible for these machines. In cloud load testing, you don't "own" the machines your test is running on; it's more like renting some time on someone's data center whenever you need it. Cloud-based infrastructure isn't necessarily less secure than on-premise infrastructure, but there are certainly more security considerations to keep in mind.

### Pros and cons of on-premise load testing

On-premise load testing is no better or worse than cloud load testing; it just depends on what you need. There's a meme that the cloud is just a fancy term for someone else's computer— but [that's an oversimplification](https://www.zdnet.com/article/stop-saying-the-cloud-is-just-someone-elses-computer-because-its-not/) that glosses over nuances that might make a difference to your bottom line.

Here are some questions to ask yourself when deciding between load testing on the cloud or on-premise.

‍![](/blog/assets/20200430-01.jpg)

_Test infrastructure can make or break your load tests._

### Cloud vs. on-premise load testing: how do you decide?

#### Why are you running a load test?

If your intention for running load tests is to test your web application's load balancing, the source of the web traffic, and the location of your environment, may not be as important. If you intend to do stress testing, you may want the scalability of a cloud setup.

#### Who is the intended audience of your application?‍

Load testing is most accurate when it is as realistic to the production workload and user base as possible. Running a load test on-premises means that the traffic comes from one location, which could be ideal if your application is an internal one.

##### Do you have the resources in your team/company to maintain load generators?

All machines need to be provisioned, set up, and maintained to function correctly. Depending on how many machines you need, you may even need a team of trained professionals to monitor your environment.

#### What is your budget?

Both cloud and on-premise load testing have costs. Cloud load testing requires a smaller outlay of cash initially but may cost more to maintain as you continue to pay for the computing time. On-premise load testing requires more money upfront but may cost less to maintain in the long run.

#### How many virtual users do you want to run?

The number of virtual users you intend to test your application against correlates to the number of load generators you require. In general, the more machines you need, the more expensive it becomes (for both cloud and on-premise load testing), but if you only need a handful of users, perhaps you can find a machine or two on-premise that could do the trick.

### Advantages of on-premise load testing
‍
![](/blog/assets/20200430-02.jpg)

#### Increased control

Since you own the machines you're testing on, you can set your environment up with your exact specifications in mind. You'll be able to make hardware upgrades or update versions of operating systems and load testing tools whenever you want, without needing to liaise with a third-party provider. This option can come in handy if you routinely use non-standard configurations or legacy software. If you're also doing other types of non-functional testing, like security testing, it may be easier to change the configuration on on-premise machines.

#### Greater data security

The question of cloud vs. on-premises may be a business decision. Some industries or businesses with stringent compliance and regulatory requirements may have no choice but to run tests on-premise because owning the load generators also means controlling who has access to the data that's on them. An on-premise environment lets you lock down access if necessary. With cloud load testing, you'd need to have security arrangements with the cloud provider that you choose so that any test data or identifying client information seen or accessed by your test scripts remains confidential.

#### Lower cost and lower barrier to entry in some situations

If you don't intend to run too many users of your test script and you already have a spare machine or two at the office, on-premise load testing may be the easiest and most cost-effective way to get started. This way, you avoid having to request the budget for a new tool and needing to train your team on a new interface.

#### Fewer variations due to latency

Controlling your own load generators means controlling the network they run on. If your corporate network is generally stable, and your test scenarios don't involve testing from different geographical locations, reported response times (and user experience) more closely reflect server processing time rather than latency and travel time.

### Disadvantages of on-premise load testing
‍
![](/blog/assets/20200430-03.jpg)

#### Higher cost in some situations

Maintaining your own load generators comes with a higher up-front cost, which may be a showstopper for smaller projects or companies. The more concurrent users you require for your load test, the more machines you need, the more licenses you need for your testing tool (unless it's open source), and the longer it takes to recover your investment.

#### Geographical limitations

Since all your machines are in one place, you can't accurately simulate the user experience for customers who might access your web app from another location. You also can't fully test the effect of CDNs and other tools that your application might employ to keep response times low. Web apps that can be accessed by anyone on the internet might require performance tests that take into account customers from different regions.

#### More setup

You need to do all the setup yourself for both hardware and software components. You also need a way to coordinate your test, so that load generators start and end when you want them to. You may want to divert some resources towards environment management.

#### Less flexibility

With on-premise load generators, you can't add, remove, or scale up nodes on the fly according to your test— something cloud load testing excels at.

## On-premise load testing best practices

The environment you're testing in is especially important when you're using your own infrastructure. Here are some best practices for a performance testing strategy that involves on-premise load generation.

### Run baseline tests

Treat load testing like a scientific experiment. Before you begin changing variables to improve performance, spend some time figuring out your test configuration so that it's repeatable. Pay attention to things like workloads, business processes, the number of users you're running per load generator, test environment configuration values, script pacing and think time set in your testing tool, and test script transactions. Make sure that the resource utilization on your machines remains healthy during a test; otherwise, you're load testing the load generators themselves rather than your application servers.

Then, run a few tests against your application servers without making any changes. This way, you create a "control group" or control test against which to compare future tests.

This process is called _baselining_ your application performance.

‍![](/blog/assets/20200430-04.jpg)
_Flood's Project View lets you track an application's performance over time and compare recent tests to a baseline_
‍
### Consider using containers or virtual machine images

Along the lines of reducing variables, it's especially important to use load generators that are as identical as you can make them. You can manually check that you're installing the same software and tools on each one, or you can do as cloud providers do and automate this process.

It's easy to miss software that are necessary for monitoring or the load testing tool you're using. For example, JMeter and Gatling require certain versions of Java. Test automation or browser-level load testing tools might require web browsers.

You can use [containers such as Docker](https://www.docker.com/resources/what-container) to create a standalone package of everything you need for your  test. Alternatively, if you're using virtual machines, you can also create a full system image that you can use for every virtual machine.

The difference between the two is that a container lets you be more granular about what is included in the package that you then deploy to all your load generators. Virtual machines include hardware components that you can set, whereas containers are software-only, decreasing package sizes.

Using containers or images allows you to keep your load generators as identical as possible (in terms of hardware and software) so that you can assume similar results from each one.

‍‍![](/blog/assets/20200430-05.jpg)
‍
### Don't neglect monitoring

It's easy to forget that your application servers aren't the only ones that need monitoring. Your load generators need monitoring as well, so that they don't end up being the bottleneck in your tests. Here's  [a starter list of server metrics](https://flood.io/blog/load-testing-tutorial-server-monitoring) that you should consider monitoring.

You might also consider how you can integrate [performance management](https://stackify.com/mistakes-evaluating-application-performance-management/) tools you already use into your monitoring strategy.

### Spend time on a framework for gathering data

One of the biggest challenges in on-premise load testing is figuring out how to get data from your tests. Each machine runs your test script independently of the others, so at the end of your test, you're likely to end up with several results files. After you download these off every machine, how do you combine them into a single summary?

Manually collating results is an option, but it's a tedious one. You can copy all the files into one directory and then concatenate them so that you end up with one giant one. Depending on the size of those results files and how long you ran the test, however, this may not be feasible. For larger files, you might consider aggregating the data and increasing the granularity, so that instead of seeing raw response time for every transaction, you only see the average response time for every 15 seconds. You can use a tool like [Logstash](https://www.elastic.co/logstash) for this.

It takes some time and technical expertise to set up a framework for results gathering that works for your purposes, especially if you want to go a step further and have real-time results.

Of course, you can also skip this part by just using the framework we've already set up on Flood. Tim Koopmans, our co-founder, created the first prototype of what would become Flood specifically because he got tired of having to set up this framework for every engagement.

## How to run an on-premise load test with Flood Agent
‍
The easiest way to get started with an on-premise load test is by using [Flood Agent](https://flood.io/blog/introducing-flood-agent-standalone-infrastructure-for-load-testing). Flood Agent is an executable that you can install onto a machine that effectively turns it into a full-fledged load generator.     Then, you can start a test from the Flood web interface and have your test script start running on your machines.

Agent takes care of a few typical problems we've discussed so far:

* It uses containers to ensure that load generators are identically provisioned.
* It automatically gathers CPU, memory, and network metrics on load generators.
* It coordinates the execution of the load test so that you only need to start it from one central place.
* It enables real-time monitoring of results while the test is running.
* It aggregates and collates all the results for you into a dashboard.

We think Agent addresses pain points that we've seen over and over again in our own on-premise performance testing projects as well as in our customers'. Agent is a [free download](https://github.com/flood-io/flood-agent/releases/latest) and works with [all performance testing tools that Flood supports](https://guides.flood.io/scripting-and-tools/choosing-a-tool).

## Conclusion

On-premise load testing is still a valid option despite the growth in popularity of cloud-based infrastructure, and it has its advantages and disadvantages. This type of load testing trades a little bit of flexibility for increased data security and control, which is a tradeoff that some companies may be willing to make.

On-premise load testing has traditionally included a lot of tedious setup and maintenance. Still, you can reduce maintenance effort by creating an internal load testing framework upfront that automates coordination, monitoring, and results collection. Using Flood Agent can mitigate time spent on this initial setup.