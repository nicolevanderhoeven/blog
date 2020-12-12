---
title: "How to Write a Load Test Plan"
date: 2020-09-21T16:33:23+01:00
draft: false
tags: ['performance', 'english', 'text', 'flood.io']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/how-to-write-a-test-plan-for-load-testing">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/how-to-write-a-test-plan-for-load-testing)._

People often start load testing by creating a script in their favorite load testing tool, but good load testing starts before that. Planning a load test may seem like a tedious exercise, but it is essential to ensuring the success of your testing.

A test plan should answer why, what, who, when, and how the testing will be carried out.

A good test plan, particularly for load testing, includes the following components:

* Requirements
* Scope
* Entry criteria
* Workload modeling
* Server monitoring
* Test doubltes
* Test Scenarios

We'll dive into each of these, but first, a note on the format of a test plan.

## Test Plan Format

Test plans have been traditionally presented as a document, but there's no hard-and-fast rule. Instead, the length of a test plan, and the level of detail it goes into, should be tailored for the complexity of the project and the backgrounds of the stakeholders.

Teams using Agile methodologies may not have a formal test plan at all, but I would argue that all teams should still have some sort of plan, whether it's a Word document or a list of bullet points. Written plans clarify and communicate intent, and testing can be an expensive and fruitless exercise without a consensus on its intent.

Technical documentation can be difficult to digest and understand, and that's dangerous when it comes to software development and testing, where it's imperative that all stakeholders are on the same page about the state of an application.

Paul McLean, a performance engineer, has a creative solution for this. He creates a companion video for every technical report, giving stakeholders the option to read the written report for details but watch the video for a more high-level and nuanced explanation.

Here's an example of a companion video he created for a test plan:

{{<youtube FJj_7nyV3Ak>}}

## Requirements

Everything starts with requirements. Until requirements are identified, load testing can only ever be aimless and explanatory, and any performance bottlenecks spotted will be incidental. 

Requirements inform every step of the load testing process. Why are we doing load testing? What exactly do we want to test? How will we know when a test has passed or failed? How will we know if application performance is good enough to go into production? What does “good enough” mean?

This is such an important part of the planning process that I felt it deserved its own blog post. See it here: [Start with Why: How to Write Requirements for API Load Testing](https://www.flood.io/blog/start-with-why-how-to-write-requirements-for-api-load-testing). Even though I specifically mention API load testing, the principles apply to load testing in general.

## Scope

At Flood, we use a product development methodology called [Shape Up](https://basecamp.com/shapeup) to keep us on track as we build new features. Projects in Shape Up are called "shaped work", and one of the basic properties of shaped work is that it is bounded.

> ...shaped work [also] indicates what not to do. It tells the team where to stop. There’s a specific appetite—the amount of time the team is allowed to spend on the project. Completing the project within that fixed amount of time requires limiting the scope and leaving specific things out.- Ryan Singer, [Shape Up: Stop Running in Circles and Ship Work that Matters](https://basecamp.com/shapeup)

Defining scope is setting boundaries. Business priorities need to be weighed against the resource limitations (number of people available to do the work and time available) in order for testing to deliver maximum value.

Some considerations for scope include:
* Specific features or key transactions to be tested
* Types of tests included (component test vs end-to-end test)
* Test scenarios (peak load test vs disaster recovery)
* Applications included in testing

As with most things in the planning phase, scope is something that can change during the test when unexpected circumstances arise or when priorities change. But it's still a good practice to define the scope at the beginning, and update it as it changes.

![](/blog/assets/how-to-write-a-load-test-plan01.jpg)

It's important, however, to _prune with intention_. By keeping our objectives in mind, we can keep our work in line with our intentions.

## Entry criteria

Occasionally, you may be asked to load test an application that isn't ready to be load tested. This happens more often than you think. While it's true that Performance Testing is something that should be baked into all software development from the beginning, this doesn't hold true for Load Testing. Load testing is only one activity that falls underneath the broader umbrella of performance testing.

Entry criteria are conditions that you need to be fulfilled before the testing actually begins. It’s a good idea to have these conditions communicated beforehand so that everyone is clear on what needs to be set up before you can do your job.

### Functional testing: Does the application work?

Load testing cannot realistically be carried out until at least the core functionality has been tested and high-severity defects have been fixed. Depending on the kind of load test you want to execute, you may also want to specify that UAT has been executed, as there’s no point doing an end-to-end load test with 1000 users if it doesn’t work for one user.

### Load Testing Environment: Is it production-like?

Nonfunctional testing has stricter requirements for an environment than does functional testing, and you may have to champion this cause. For load testing, it is not enough to have an application staging environment that is a virtual machine that is a quarter of the size of the production environment. It’s important to get as close to a production-like environment as possible in terms of capacity (memory, CPU), codebase (the actual build that will be deployed), and integrations with other environments or servers (if within test scope).

Load testing is not linear: a response time of 5 seconds on a server with half the capacity of the production server does not necessarily equate to a response time of 2.5 seconds in production.

This is also the time to think about your load injectors. Will they be on-premises, or in the cloud? A good entry criterion is the availability of the machines in the right network and with the right tools installed. If you’re using commercial tools, license provisioning should be a criterion. What sort of capacity will your load testing scripts require?

### Support: Are there people available with expertise in key components?

Load testing is a team activity. When a load test involves multiple application teams, it’s important to request availability of key persons on those teams during the test. Often as load testers, we are seen as working independently, but the truth couldn’t be farther from that. Load testing is a team sport. We need support from:

business analysts who will be able to tell us how things are expected to work and what the current priorities are

* developers whom we can consult when poorly performing code needs to be optimised
* functional testers who can show us how the application works
* DevOps engineers who can help us provision and monitor servers

and many more!

‍![](/blog/assets/how-to-write-a-load-test-plan02.jpg)

### Test Data: Do you have dummy data for your virtual users to interact with?

Once you have as close a copy of the production environment as possible, keep in mind that it’s still a clean copy, which may not be realistic. If there are databases in production, how much data do they contain? The application server may respond differently when your test database is empty compared to when it must contend with gigabytes of data in the production database.

Using production data for testing purposes can be dangerous, not to mention illegal, in certain circumstances. To avoid this, you can scrub sensitive data or generate your own, either by injecting records into a database or by writing an automation script to create data on the front-end. If you write a script, you may be able to reuse parts of it later for your load test. 

## Workload Modeling

A workload model is a schema describing the load profile for a given test scenario, and it involves determining what (the key transactions), how much (the load distribution among the transactions) and when (timing of the load) to test.

Workload modeling can be the most difficult part of the testing process because it involves finding out how load test scripting can best mimic what is actually happening in production. It can also be the most critical.

Here's my account of working on a project in horse racing, where workload modeling was of particular importance: [Workload Modeling - Preparing for Large Events like the Melbourne Cup](https://www.flood.io/blog/workload-modeling-preparing-for-large-events-like-the-melbourne-cup).

‍![](/blog/assets/how-to-write-a-load-test-plan03.jpg)
_When you're selling bets for the Melbourne Cup, every second matters._

## Server monitoring

Executing a load test without monitoring server health is like flying blind. You’ll know when you land safely and you’ll know when you crash, but even if you do crash, you won’t know why—or how you can avoid it next time. Monitoring server health is the black box that will tell you what went wrong.

For load testing, you'll want to monitor the application servers that you're testing as well as the load generators that you're using to run the load tests themselves. That's right; if you're not watching carefully, the machines you run the load tests on can be the bottlenecks in themselves, causing unnecessary failures in your load tests.

[Joe Colantonio](https://testguild.com/performance-test-resource-utilization/) goes over the basics of resource utilization in terms of four main areas of concern:

* CPU
* Memory
* Disk
* Network

[Here's another guide](https://www.flood.io/blog/load-testing-tutorial-server-monitoring) I put together on the basic metrics as well as some tools you can use to set up your monitoring.

Regardless of which metrics you identify as key or which tools you use, you'll want to make sure that they're all set up to measure server health before you run your load tests.

## Test doubles

Part of the strategic planning around load testing is deciding which components need to be tested in conjunction with your stated requirements. Applications can sometimes be complex enough that load testing end-to-end is not feasible due to the number of teams involved or the cost of duplicating application infrastructure.

Keeping it as simple as possible will lead to fewer dependencies, so it's worth considering creating test doubles to isolate relevant components. Test doubles include stubs, mocks, and full virtual services.

‍![](/blog/assets/how-to-write-a-load-test-plan04.jpg)

A test double is that part that replaces a complicated component that is not within scope. It’s a “dumber” version that responds to requests enough to allow you to go on with your load testing without actually requiring that component.

Test doubles allow us to abstract out other components we don't want to test so that we can concentrate on the one that we do. The point of a test double is to remove the variables and noise introduced by other parts of the application so that we can focus on testing how one component responds.

If you are willing to put the time into creating a test double, you can drastically reduce the amount of resources you need to set up an environment and isolate components. Reducing variables in your test allows you to more quickly determine where performance bottlenecks lie.

## Test Scenarios

A test scenario is the description of a contained situation or condition under which the application will be tested. A test scenario is usually based on several test cases and includes a plan for how these test cases will be executed.

Choosing your test scenarios means deciding which situation is most likely to yield the data that you require. Employing several different types of scenarios will give you a greater understanding of your application’s capabilities. You should feel free to create your own scenarios that are uniquely tailored to your requirements, but here are some common scenarios to start out with. Take the number of users and durations mentioned as guidelines and not rules.

Here's what our Flooder amigo, Señor Performo, has to say about test scenarios: 

{{<youtube EGzoAadzWwM>}}
_Text version [here](https://www.flood.io/blog/ask-a-flooder-21-senor-performo-on-load-testing-scenarios)_

## Conclusion

Creating a test plan can seem daunting, but the process of writing it serves as a prompt for discussions among your team. 

Here's a [pro tip from Scott Moore](https://techbeacon.com/app-dev-testing/how-go-performance-tester-performance-engineer): Once you come up with a template you're happy with, save it and reuse it for future projects. Modify it over time based on feedback to see progressive improvement.

> Building a set of reusable documents and other deliverables ("templates") to use in the initial planning phase and final reporting will speed your initial startup time. I recommend working with or learning from others with experience to build out some of these templates.

‍When in doubt, remember that the format of a test plan is not as important as making sure it is meaningful and comprehensible for your team.

‍For more information about the load testing process, check out [my book on API load testing](https://guides.flood.io/ebooks/api-load-testing).