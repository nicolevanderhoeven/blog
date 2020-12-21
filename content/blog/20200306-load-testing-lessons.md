---
title: "Load Testing Lessons from the Iowa Caucus"
date: 2020-03-06T21:59:02+01:00
draft: false
tags: ['performance', 'english', 'text', 'jmeter']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/load-testing-lessons-from-the-iowa-caucus">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/load-testing-lessons-from-the-iowa-caucus) and [here](https://thenewstack.io/how-id-load-test-the-iowa-caucus-app/)._

**TL;DR? Here are the highlights in this article:**

Shadow, Inc. created a mobile app for the Iowa Caucus in February 2020, and the app failed, causing reported results to be delayed.
The app reported different vote totals due to a system integration bug where the output was in a different format than what it needed to be.
Here are the steps to load testing a mobile app:
1. Test planning: Does the app require load testing? If yes, what is the underlying technology? How do we create a workload model?
2. Scripting: Which mobile load testing tool should we use? How do we record traffic from a mobile device?
3. Execution: What load test scenarios should we have? How can we scale up the load generated?
Conclusion: While the Iowa Reported App failure was not due entirely to load testing, load testing could have helped make it more robust.

---

A company called Shadow, Inc. made headlines earlier this week when they developed an app to count and report votes during the Iowa Democratic Caucus in the US. This app, called IowaReporterApp, ended up failing on several fronts, resulting in a [days-long delay](https://www.nytimes.com/2020/02/06/upshot/iowa-caucuses-errors-results.html) in publishing the total votes, during which manual methods had to be employed.

![](/blog/assets/20200306-01.jpg)

_Source: [@ShadowIncHQ on Twitter](https://twitter.com/ShadowIncHQ/status/1224773796307050497)_

This delay led to significant criticism from the software testing industry as well as from the general public. Some developers raised questions about the [code quality of the app](https://www.vice.com/en_us/article/3a8ajj/an-off-the-shelf-skeleton-project-experts-analyze-the-app-that-broke-iowa). The app [inaccurately reported voting totals](https://twitter.com/iowademocrats/status/1225170253778444291) that differed from the Democratic Party's own manual reports, suggesting an issue with functional testing, particularly system integration testing. Shadow's [refusal to accept the Department of Homeland Security's help with security testing](https://thehill.com/policy/cybersecurity/481409-dhs-chief-says-offer-to-vet-iowa-caucus-app-was-declined) also raised eyebrows. What was perhaps the most damning, though, was the question of [whether such an app was necessary in the first place](https://twitter.com/zeynep/status/1224545350364672001), when cheaper and more effective solutions existed.

What I'm most interested in, however, are the load issues that the app faced. Let's rewind a little to before the caucus. How would I have load tested an app like the IowaReporterApp?

## Planning a mobile load testing

One of the first things to figure out when planning a load test is whether a load test is even necessary.

### Do you even need to load test your mobile app?

To answer that, I had to find out more about the app.

In the caucus, residents of Iowa who registered themselves as Democratic voters gathered to vote on whom they thought should be the party's candidate for the presidential elections later this year.

There are a few things that I think make this app the perfect candidate for load testing:

- **It was highly publicized.** The caucuses would always have been an event of international interest, but the hype surrounding electronic voting increased media attention on the caucus even further.

- **It was mission-critical**. The precinct chairs would use the app as the primary device for capturing votes.

- **It needed to handle significant simultaneous load**. There were [over a thousand precinct caucuses](https://en.wikipedia.org/wiki/2020_Iowa_Democratic_caucuses) organized, each with a precinct chair that would be using the app.

For these reasons, the answer is a resounding "Yes."

### What type of app is it?

The best way to learn about an app is to ask its developers. In this case, I opted to do a little research on my own by [downloading the .apk file that Motherboard (Vice) made available](https://www.vice.com/en_us/article/z3b3g9/here-is-a-link-to-the-shadow-inc-app-that-blew-up-the-iowa-caucus) and looking through the code myself.

The app is a mobile-only app for Android and iOS devices, written mostly using Facebook's React Native package. The primary function of the app was to sent the vote totals to Shadow Inc.'s [Google Cloud Functions](https://cloud.google.com/functions/?utm_source=google&utm_medium=cpc&utm_campaign=emea-nl-all-en-dr-bkws-all-all-trial-e-gcp-1008073&utm_content=text-ad-none-any-DEV_c-CRE_253510459861-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+EXA_M:1_NL_EN_General_Cloud+Functions_ETL+Warehouse-KWID_43700019207359819-kwd-135583196912-userloc_9065312&utm_term=KW_google%20functions-ST_google+functions&ds_rl=1242853&ds_rl=1245734&ds_rl=1245734&gclid=EAIaIQobChMI6bKKzNi_5wIVk-R3Ch04HA1XEAAYASAAEgKTcPD_BwE) server.

The technology involved is worth noting because it can help determine which load testing tool to use. Since the Iowa Reporter App, like most mobile apps, sends requests to a RESTful API, JMeter or Gatling, both well-tested, robust, and open-source protocol-level tools with large user bases, were perfect for the job. I decided to go with JMeter, my personal tool of choice.

### How do we create a workload model?

Now let's talk about the workload model, which is a plan for how the load we generate needs to look. The objective here is to simulate the load that matches the expected real-life load as closely as possible.

At this point, I would typically look at historical data to try to see the amount of load and the load profile. If I had metrics on the server traffic after previous releases of the app using something like Google Analytics or an APM tool, I would have used that data as a starting point for the workload model of this release. However, in this case, the app hadn't been publicly released before, so I needed to make some educated guesses.

[According to Wikipedia](https://en.wikipedia.org/wiki/2020_Iowa_Democratic_caucuses), there were a total of 1,777 Iowa precinct caucuses, of which 99 were global satellite caucuses set up for Iowa residents temporarily not able to attend the local caucuses.

In a Democratic caucus, the actual voting process generally takes [about two hours](https://www.theguardian.com/us-news/2020/feb/03/iowa-caucuses-2020-elections-candidates). In the Iowa caucus, the precinct chairs would have used the app twice - once for each round of voting. Around the end of the two hours, each chair's app would have sent the main payload, containing total votes for each candidate, to the backend server. All this is done simultaneously across all 1,777 precincts.

At a minimum, there are two main events here:

1. The login - Precinct chairs needed to log in to the app, which would presumably have happened around the same time across all precincts towards the beginning of the voting process, because the app also contained instructions on how to run a caucus.

2. The submission - This is the transmission of the total vote counts for each candidate, sent to Google Cloud Functions, and would also have happened around the same time.

It's possible that the app also sent other requests between these two events, but since most of the app is inaccessible without a valid login, I'll focus on the initial login request.

In a situation like this where I don't have previous data to show how spread out those requests was, it's prudent to err on the side of caution. Assuming the precinct chairs triggered those requests within 10 minutes of each other and rounding up the number of requests for some wiggle room, I estimated that there would have been 1,800 login requests within 10 minutes.

I decided to test this as a gradual ramp-up of users within 10 minutes.

## Scripting for mobile

Okay, time to write the script. Since I didn't have the luxury of being able to ask the developers for the format of the login request, I did the next best thing and tried to find out myself by recording the app traffic in action.

![](/blog/assets/20200306-02.png)

### Recording mobile traffic on a laptop with JMeter

Here's how I was able to see the request from the mobile app:

- I downloaded the app to a spare Android mobile by using the APK link above.

- I set up an HTTP(S) Test Script Recorder on JMeter on my laptop with the port 8888.  I also made sure my laptop was connected to my wifi network.

- I set up my mobile to use a proxy using my laptop's local IP address on the network and port 8888.

- Then, I went back to JMeter on my laptop and started the HTTP(S) Test Script Recorder.

- Finally, I navigated to the app, typed in flood.io in the Precinct ID field (obviously not a real ID), and clicked the "Click here to log in" button.

Here's the traffic as seen on JMeter's View Results Tree listener afterward:

![](/blog/assets/20200306-03.png)

And here's the recorded request within the recording controller:

![](/blog/assets/20200306-04.png)

### Analyzing the request

It looks like at least the initial login request is a GET to an Auth0 service, with several parameters being passed in the body. It also has some authorization headers.

The parameter values also look like they might be dynamic, meaning they change from session to session. At this point, I would typically change some of these from being hardcoded values into dynamic ones so that the application receives a request in the right format, and I could look through [Auth0's API documentation](https://auth0.com/docs/api/authentication) to find out how the authentication message should be formulated.

Since I don't have a valid login for testing purposes, I skipped this step and just used the raw request for demonstration purposes.

### Preparing to run

Think time is a delay between requests meant to simulate the time it takes for a user to think before taking another action. Without think time, JMeter would fire off requests one after another, which often isn't realistic and drains resources. I don't want that, so I added a JMeter timer. There are plenty of timers available, but I settled on a Uniform Random Timer.

[The CEO of Shadow told Motherboard](https://www.vice.com/en_us/article/3a8ajj/an-off-the-shelf-skeleton-project-experts-analyze-the-app-that-broke-iowa) that many precinct chairs were confused by the login process as they had to put in three strings of numbers in the right sequence. So, I decided to work that into the script with the timer. I set it up with a constant delay of 2 minutes and a random delay of 1 minute so that the delay would vary from 2 minutes to 3 minutes to simulate a precinct chair attempting to log in a few times.

## Execution: Running your mobile load test

[According to Motherboard](https://www.vice.com/en_us/article/z3b3g9/here-is-a-link-to-the-shadow-inc-app-that-blew-up-the-iowa-caucus), Shadow has already taken the app servers offline. However, it's not a good idea to run a full load test against an endpoint that you don't own, so I decided not to run a test.

Usually, though, I’d want to start with a shakeout test of 10 users or so, and then gradually increase the user load until the peak of 1,800 users. I also would have played around with changing the load profile, such as by increasing or decreasing the ramp-up or steady-state durations, experimenting with stress tests and soak tests, and adding traffic from another availability zone to simulate the 99 satellite precincts around the world. Running multiple load generators can quickly get out of hand if you want to use physical machines, so I would run load tests on the cloud with something like [Flood](https://flood.io/). All of these little changes would have given valuable data that would help me gauge the app’s performance in production-like situations.

## Conclusion

Building quality software is not a trivial task. There are many moving parts to account for, and critical errors can be introduced in every stage of an app's development. While load issues were not the main culprit in the failure of the IowaReporterApp, a simple load test like the one I describe here, might have improved app stability and reliability. Even in cases where load testing doesn't seem necessary, it can still uncover gross issues in configuration, usability, or security for an app developed on a deadline.