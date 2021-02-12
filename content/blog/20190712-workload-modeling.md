---
title: "Workload Modeling - Preparing for Large Events like the Melbourne Cup"
date: 2019-07-12T17:49:36+01:00
draft: false
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/workload-modeling-preparing-for-large-events-like-the-melbourne-cup">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/workload-modeling-preparing-for-large-events-like-the-melbourne-cup)_.

![](/assets/20190712-01.jpeg)

You've probably heard the story several times before: a company does load testing, their application goes live, and then that application fails under production load, and company loses profits to a competitor. This happens a lot more than we'd like it to at [Flood](http://flood.io).  The silver lining for most companies is that the world won't know if their app is down for a few minutes or a few hours.

But what happens if the application you're testing happens to be tied to an event that millions of people watch— one that is so important it's even a public holiday?  At Flood, many of us have worked together preparing sites for major events like the Melbourne Cup.  Perhaps you are working for a betting site too. Are you ready to be bombarded with the onslaught of users right before races begin?

Failures to find and fix performance bottlenecks can be very public. Just last year, we found that [many sites were not properly prepared](https://www.theage.com.au/business/companies/online-betting-sites-crashed-in-lead-up-to-melbourne-cup-20181106-p50ebb.html) for the influx of new users that [[Melbourne Cup]] can bring. If you're a site selling bets online for the Melbourne Cup, like the unfortunate ones in that article, chances are high that your inability to keep up with the load would not have gone unnoticed.

## What is the Melbourne Cup?  And why should I care?
The Melbourne Cup is a thoroughbred horse race that is the crown jewel of Melbourne's annual Spring Racing Carnival, a three-month season where the highest-rated horses are pitted against each other. The Melbourne Cup race itself only takes a few minutes, but the 2018 race was watched by over 30 million viewers within Australia (Cheik-Hussein, 2018).

Talk about failing publicly.

As if that weren't bad enough, having your site down during the crucial time before the race would have significant financial consequences. 

The Victoria Racing Club (2019) reports that Melbourne Cup 2018 added a cool AU $447.6 million to Victoria state's coffers, including money gained from not only bets but also from race tickets, accommodation, fashion retail and food.

Given how many people now purchase those things online, we can only guess how much of a company's annual revenue could be lost from a slow-performing or nonexistent site during this frenzy.

So how could several of Australian's betting sites have allowed this to happen? Viewership of the Cup only __slightly__ increased from the previous year (Cheik-Hussein, 2018). They almost certainly did load testing for this peak period. Why didn't their testing identify performance bottlenecks?

There are a lot of reasons why this might have happened, but one possible answer is inadequate workload modelling. In this article, I'll go over how you can avoid this if you're testing for the Melbourne Cup or another major gambling event.

## What is a workload model?
A workload model is a schema describing the load profile for a given test scenario, and it involves determining __what__ (the key transactions), __how much__ (the load distribution among the transactions) and __when__ (timing of the load) to test."

## What to test: key transactions
This, together with the scope and business need, will determine what you script and what you actually test. Not everything needs to be load tested. Here’s how to determine what does:

### Business-critical or high risk transactions

Include anything that is vital to the success of the release.

Major site-wide changes require testing across a wide variety of functions. Even the betting giant Tabcorp, Australia largest gaming company, admitted to performance issues when they introduced changes to their site in advance of the 2008 Spring Racing Carnival ("[Tabcorp acknowledges betting web site poor performance", 2008](http://thoroughbrednews.com.au/news/story/tabcorp-acknowledges-betting-web-site-poor-performance-36333?section=Australia)).

Payment is a high-risk area, so anything touching it should be thoroughly load tested, including the payment calculation and processing engine. The payment processing load may differ depending on the horse that wins the race— if the winner is an outsider (a horse with long odds that seemed unlikely to win), your server will need to process much fewer payments than if a favourite does. Make sure you test for the higher load.

### Known pain points
A good place to start is any pages that your Customer Support team have reported as a pain point for customers. Let customers tell you what they want.

### Transactions that are technically complex
These transactions sometimes go through several application servers and are processed several times before a response is returned to the user. This means that they’re also the most likely to present issues when one or all of those servers are under load.

Not all bets are equal. The type of bet placed can also change the load on the application servers. Fixed odds bets take into account odds that expert bookmakers have set. Since these odds, and thus the price of a bet, are manually set, placing a fixed odds bet doesn't require much computational power.

By contrast, a parimutuel bet is one where the odds have been determined by the bets that have already been placed. Parimutuel bet prices continually vary over time as each new bet changes the odds slightly, so parimutuel bets require more processing and exert more load on different components than fixed odds bets.

For this reason, _both_ types of bets should be part of your test scenario.

### High-traffic transactions
For instance, customers may tend to refresh their account page repeatedly after a race as they wait impatiently for their payout so that they can bet on the next race.

## How much to test: load distribution
Now that you've selected __what__ you want to test, you'll want to make sure that you're also testing those transactions in the right proportion. [Racing.com](http://racing.com) lists 12 types of betting sub-types each for fixed odds and parimutuel wagering. Some sub-types may affect different components, so it's important to test each one with the right number of users.

A simple way to do this in JMeter is to use the [Throughput Controller](https://jmeter.apache.org/usermanual/component_reference.html#Throughput_Controller). If you select "Percent Executions" in the dropdown menu, you can select how often the samples within that controller is executed.

![](/assets/20190712-02.png)

This way, you can set one bet type to be used 70% of the time, and another 5% of the time, etc., according to the numbers you've gathered from your historical metrics.

## When to test: load timing
The load profile will tell you how the load is distributed over time. Since applications are used in different ways, it’s not enough to get an average hits per second over the last year and test at that level. You’ll need to understand which transactions those hits are going to.

Look specifically for trends over time. These could be yearly, seasonal, monthly or even daily patterns. One of the most marked examples of this is in the racing industry, which normally shows load profiles that are incredibly "spiky". This is because betting traffic tends to be highest in the few minutes __before__ a race begins as people rush to get their bets in, levelling off __during__ a race as they watch what happens, and then start up again after the race as they hurry to collect their winnings and bet on future races.

One of our favourite clients at Flood, [[Hotstar]], simulated video streaming traffic to their site in preparation for the [Indian Premier League in 2018](https://blog.hotstar.com/millons-scale-simulations-1602befe1ce5) (Agrawal, 2018).

After analysing the data they had from previous years, they decided on a load test that had this load profile:

![Hotstar's load profile](/assets/20190712-03.png)

[[Hotstar]]'s load profile for their Indian Premier League 2018 tests through Flood. Source: https://blog.hotstar.com/millons-scale-simulations-1602befe1ce5

The spikes in load correspond to the start of cricket games. This spiky profile means that they had to test at higher levels of load for a short period of time, instead of testing with a lower user count for a longer time. In this case, using the average number of users throughout the day would have drastically oversimplified things. Given that their load tests required 4 million concurrent users, that small change in the workload model could have negatively impacted their results and performance during the games in production.

You can only determine what the “Peak” in traffic is for your application after you’ve seen historical data. If you’re like [[Hotstar]] and you want to test the performance on game day, don’t pick traffic from some other month where there are no games— take a look at your highest season traffic-wise and test for that. You may even want to increase those figures by 10% or so in order to leave some room for growth.

During this year's IPL tournament, [Hotstar broke a global viewership record with their 18.6 million users](https://techcrunch.com/2019/05/12/hotstar-disneys-indian-streaming-service-sets-new-global-record-for-live-viewership/) (Singh, 2019).

Luckily they'd done their load testing with Flood beforehand!

## Where to test from: channels, networks and geography
So, now that you know what you’re testing and when you’re testing, the next question is where you’re testing _from_.

### How are your users placing their bets?
While more and more people are moving to online betting, if you have a substantial amount of users that still bet by other means, you'll want to account for that too. 65% of Australian betting was digital in 2016 (Amsel, 2017), but what about the other 35%? If you expect users to be betting through machines at retail outlets, in person at the track, or on the telephone, perhaps you need to load test the systems that those bets flow into as well.

### What networks are your users betting from?
With more and more people browsing the internet on their mobile devices, it’s worth considering how big an effect users’ networks have on their experience of your application.

With more and more people browsing the internet on their mobile devices, it’s worth considering how big an effect users’ networks have on their experience of your application.

While you can’t control users’ network speeds, what you can do is simulate them by throttling the bandwidth available so that you can see how quickly your application would respond for them. Most load test tools can do this, and you may be able to determine how many of your users access your app on slower connections by looking at your analytics. If you decide that this is in scope, you can then build it into your scripts so that your tests will also show you response times on different types of networks.

### Network Bandwidth throttling in JMeter
In JMeter, you can control this by adding the following line to your user.properties or jmeter.properties file:

`httpclient.socket.https.cps=19200000`

This sets the “characters per second” and, when set to anything greater than zero, will allow you to simulate different speeds.

Here’s a way to calculate the value to set:

`cps = (target bandwidth in kbps * 1024) / 8`

If you’re running your JMeter test through [[Flood]] there’s no need to modify your properties file. You can simply add this line to the [Advanced Parameters section](https://help.flood.io/en/articles/593297-parameter-substitution) when you’re editing your stream:

`-Jhttpclient.socket.https.cps=19200000`

For more information about this, check out [Apache’s documentation](https://wiki.apache.org/jmeter/Controlling%20Bandwidth%20in%20JMeter%20to%20simulate%20different%20networks).

### Network bandwidth throttling in Gatling
With Gatling, this is also indirectly possible to simulate by throttling the number of requests per second. It’ll be a little more difficult to correlate requests per second to network bandwidth, but seeing historical data of real mobile users of your application should help here. Then you can multiply that by the number of users in your simulation and set up the throttling using something like this:

```scala
setUp(scn.inject(constantUsersPerSec(100) during (30 minutes))).throttle(
reachRps(100) in (10 seconds),
holdFor(1 hour)
)
```

[Here’s Gatling’s documentation](https://gatling.io/docs/2.3/general/simulation_setup#simulation-setup-throttling) for more information on this.

### Where in the world are your users?
The geographical location of your load test generators affects the response time you’ll get. If you use on-premises machines to generate the load and see 1-second response times, the machines are on the same corporate network as your application servers and have less latency. This means that the response times will be a lot faster than those of a client using your application from across the world.

Depending on where your customers live, latency can change the reported response time. In general, you would want to have a look at your analytics and see where most of your customer base is. Ideally, you’d want to generate load in those regions— remember, we’re trying to make your load testing as realistic as possible.

This is one big reason to switch from on-premises load generators to load generators in the cloud. Service providers like [Amazon](http://aws.com), [Azure](http://azure.com) and [Google](http://cloud.google.com) allow you to provision machines with a few clicks and even select their location. Load testing on the cloud can be significantly cheaper (because you don’t have to provision or maintain physical machines and you only pay for when you use them) and more realistic, because they allow you to approximate the effect of distance on your application response times. It also allows you to test the effect of [[Content Distribution Networks]](CDNs), if you’re using any.

## Prepare for your next major event with Flood
If you are under the gun to load test before your next major event, especially if that is the Melbourne Cup, we are here to help!

Make sure to sign up for your [free trial of Flood](http://), which can be done in under 5 minutes and will give you 5 free node hours to run your first load test.  We are [here to chat](https://flood.io/contact-flood/) and would love to discuss your strategy to prepare for your next major event.

Happy testing!

## References
- 2018 Melbourne Cup Carnival delivers record economic benefit. (2019). _Victoria Racing Club._ Retrieved from https://www.flemington.com.au/news/2019-04-18/2018-melbourne-cup-carnival-delivers-record-economic-benefit
- Amsel, P. (2017). Two-thirds of Australian betting turnover is done digitally. [_CalvinAyre.com_](http://CalvinAyre.com). Retrieved from https://calvinayre.com/2017/05/18/business/digital-two-thirds-australian-betting-turnover/
- Agrawal, A. (2018). Millions scale simulations. __Hotstar.__ Retrieved from https://blog.hotstar.com/millons-scale-simulations-1602befe1ce5
- Cheik-Hussein, M. (2018). Melbourne Cup TV ratings up slightly, as streaming skyrockets. _AdNews_. Retrieved from http://www.adnews.com.au/news/melbourne-cup-tv-ratings-up-slightly-as-streaming-skyrockets
- Singh, M. (2019). Hotstar, Disney's Indian streaming service, sets new global record for live viewership. _TechCrunch_. Retrieved from https://techcrunch.com/2019/05/12/hotstar-disneys-indian-streaming-service-sets-new-global-record-for-live-viewership/
- Tabcorp acknowledges betting web site poor performance. (2008). _Throughbred News_. Retrieved from http://thoroughbrednews.com.au/news/story/tabcorp-acknowledges-betting-web-site-poor-performance-36333?section=Australia
- Toscano, N. and Cunningham, M. (2018). Online betting sites crashed in lead-up to Melbourne Cup. _The Age_. Retrieved from https://www.visitmelbourne.com/regions/melbourne/events/sports/horse-racing/spring-racing-carnival
- Types of betting. (Accessed in July 2019). [_Racing.com_](http://Racing.com). Retrieved from https://www.racing.com/new-to-racing/types-of-betting
- ‍
date: 2019-07-12T17:49:36+01:00
draft: false
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/workload-modeling-preparing-for-large-events-like-the-melbourne-cup">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/workload-modeling-preparing-for-large-events-like-the-melbourne-cup)_.

![](/assets/20190712-01.jpeg)

You've probably heard the story several times before: a company does load testing, their application goes live, and then that application fails under production load, and company loses profits to a competitor. This happens a lot more than we'd like it to at [Flood](http://flood.io).  The silver lining for most companies is that the world won't know if their app is down for a few minutes or a few hours.

But what happens if the application you're testing happens to be tied to an event that millions of people watch— one that is so important it's even a public holiday?  At Flood, many of us have worked together preparing sites for major events like the Melbourne Cup.  Perhaps you are working for a betting site too. Are you ready to be bombarded with the onslaught of users right before races begin?

Failures to find and fix performance bottlenecks can be very public. Just last year, we found that [many sites were not properly prepared](https://www.theage.com.au/business/companies/online-betting-sites-crashed-in-lead-up-to-melbourne-cup-20181106-p50ebb.html) for the influx of new users that [[Melbourne Cup]] can bring. If you're a site selling bets online for the Melbourne Cup, like the unfortunate ones in that article, chances are high that your inability to keep up with the load would not have gone unnoticed.

## What is the Melbourne Cup?  And why should I care?
The Melbourne Cup is a thoroughbred horse race that is the crown jewel of Melbourne's annual Spring Racing Carnival, a three-month season where the highest-rated horses are pitted against each other. The Melbourne Cup race itself only takes a few minutes, but the 2018 race was watched by over 30 million viewers within Australia (Cheik-Hussein, 2018).

Talk about failing publicly.

As if that weren't bad enough, having your site down during the crucial time before the race would have significant financial consequences. 

The Victoria Racing Club (2019) reports that Melbourne Cup 2018 added a cool AU $447.6 million to Victoria state's coffers, including money gained from not only bets but also from race tickets, accommodation, fashion retail and food.

Given how many people now purchase those things online, we can only guess how much of a company's annual revenue could be lost from a slow-performing or nonexistent site during this frenzy.

So how could several of Australian's betting sites have allowed this to happen? Viewership of the Cup only __slightly__ increased from the previous year (Cheik-Hussein, 2018). They almost certainly did load testing for this peak period. Why didn't their testing identify performance bottlenecks?

There are a lot of reasons why this might have happened, but one possible answer is inadequate workload modelling. In this article, I'll go over how you can avoid this if you're testing for the Melbourne Cup or another major gambling event.

## What is a workload model?
A workload model is a schema describing the load profile for a given test scenario, and it involves determining __what__ (the key transactions), __how much__ (the load distribution among the transactions) and __when__ (timing of the load) to test."

## What to test: key transactions
This, together with the scope and business need, will determine what you script and what you actually test. Not everything needs to be load tested. Here’s how to determine what does:

### Business-critical or high risk transactions

Include anything that is vital to the success of the release.

Major site-wide changes require testing across a wide variety of functions. Even the betting giant Tabcorp, Australia largest gaming company, admitted to performance issues when they introduced changes to their site in advance of the 2008 Spring Racing Carnival ("[Tabcorp acknowledges betting web site poor performance", 2008](http://thoroughbrednews.com.au/news/story/tabcorp-acknowledges-betting-web-site-poor-performance-36333?section=Australia)).

Payment is a high-risk area, so anything touching it should be thoroughly load tested, including the payment calculation and processing engine. The payment processing load may differ depending on the horse that wins the race— if the winner is an outsider (a horse with long odds that seemed unlikely to win), your server will need to process much fewer payments than if a favourite does. Make sure you test for the higher load.

### Known pain points
A good place to start is any pages that your Customer Support team have reported as a pain point for customers. Let customers tell you what they want.

### Transactions that are technically complex
These transactions sometimes go through several application servers and are processed several times before a response is returned to the user. This means that they’re also the most likely to present issues when one or all of those servers are under load.

Not all bets are equal. The type of bet placed can also change the load on the application servers. Fixed odds bets take into account odds that expert bookmakers have set. Since these odds, and thus the price of a bet, are manually set, placing a fixed odds bet doesn't require much computational power.

By contrast, a parimutuel bet is one where the odds have been determined by the bets that have already been placed. Parimutuel bet prices continually vary over time as each new bet changes the odds slightly, so parimutuel bets require more processing and exert more load on different components than fixed odds bets.

For this reason, _both_ types of bets should be part of your test scenario.

### High-traffic transactions
For instance, customers may tend to refresh their account page repeatedly after a race as they wait impatiently for their payout so that they can bet on the next race.

## How much to test: load distribution
Now that you've selected __what__ you want to test, you'll want to make sure that you're also testing those transactions in the right proportion. [Racing.com](http://racing.com) lists 12 types of betting sub-types each for fixed odds and parimutuel wagering. Some sub-types may affect different components, so it's important to test each one with the right number of users.

A simple way to do this in JMeter is to use the [Throughput Controller](https://jmeter.apache.org/usermanual/component_reference.html#Throughput_Controller). If you select "Percent Executions" in the dropdown menu, you can select how often the samples within that controller is executed.

![](/assets/20190712-02.png)

This way, you can set one bet type to be used 70% of the time, and another 5% of the time, etc., according to the numbers you've gathered from your historical metrics.

## When to test: load timing
The load profile will tell you how the load is distributed over time. Since applications are used in different ways, it’s not enough to get an average hits per second over the last year and test at that level. You’ll need to understand which transactions those hits are going to.

Look specifically for trends over time. These could be yearly, seasonal, monthly or even daily patterns. One of the most marked examples of this is in the racing industry, which normally shows load profiles that are incredibly "spiky". This is because betting traffic tends to be highest in the few minutes __before__ a race begins as people rush to get their bets in, levelling off __during__ a race as they watch what happens, and then start up again after the race as they hurry to collect their winnings and bet on future races.

One of our favourite clients at Flood, [[Hotstar]], simulated video streaming traffic to their site in preparation for the [Indian Premier League in 2018](https://blog.hotstar.com/millons-scale-simulations-1602befe1ce5) (Agrawal, 2018).

After analysing the data they had from previous years, they decided on a load test that had this load profile:

![Hotstar's load profile](/assets/20190712-03.png)

[[Hotstar]]'s load profile for their Indian Premier League 2018 tests through Flood. Source: https://blog.hotstar.com/millons-scale-simulations-1602befe1ce5

The spikes in load correspond to the start of cricket games. This spiky profile means that they had to test at higher levels of load for a short period of time, instead of testing with a lower user count for a longer time. In this case, using the average number of users throughout the day would have drastically oversimplified things. Given that their load tests required 4 million concurrent users, that small change in the workload model could have negatively impacted their results and performance during the games in production.

You can only determine what the “Peak” in traffic is for your application after you’ve seen historical data. If you’re like [[Hotstar]] and you want to test the performance on game day, don’t pick traffic from some other month where there are no games— take a look at your highest season traffic-wise and test for that. You may even want to increase those figures by 10% or so in order to leave some room for growth.

During this year's IPL tournament, [Hotstar broke a global viewership record with their 18.6 million users](https://techcrunch.com/2019/05/12/hotstar-disneys-indian-streaming-service-sets-new-global-record-for-live-viewership/) (Singh, 2019).

Luckily they'd done their load testing with Flood beforehand!

## Where to test from: channels, networks and geography
So, now that you know what you’re testing and when you’re testing, the next question is where you’re testing _from_.

### How are your users placing their bets?
While more and more people are moving to online betting, if you have a substantial amount of users that still bet by other means, you'll want to account for that too. 65% of Australian betting was digital in 2016 (Amsel, 2017), but what about the other 35%? If you expect users to be betting through machines at retail outlets, in person at the track, or on the telephone, perhaps you need to load test the systems that those bets flow into as well.

### What networks are your users betting from?
With more and more people browsing the internet on their mobile devices, it’s worth considering how big an effect users’ networks have on their experience of your application.

With more and more people browsing the internet on their mobile devices, it’s worth considering how big an effect users’ networks have on their experience of your application.

While you can’t control users’ network speeds, what you can do is simulate them by throttling the bandwidth available so that you can see how quickly your application would respond for them. Most load test tools can do this, and you may be able to determine how many of your users access your app on slower connections by looking at your analytics. If you decide that this is in scope, you can then build it into your scripts so that your tests will also show you response times on different types of networks.

### Network Bandwidth throttling in JMeter
In JMeter, you can control this by adding the following line to your user.properties or jmeter.properties file:

`httpclient.socket.https.cps=19200000`

This sets the “characters per second” and, when set to anything greater than zero, will allow you to simulate different speeds.

Here’s a way to calculate the value to set:

`cps = (target bandwidth in kbps * 1024) / 8`

If you’re running your JMeter test through [[Flood]] there’s no need to modify your properties file. You can simply add this line to the [Advanced Parameters section](https://help.flood.io/en/articles/593297-parameter-substitution) when you’re editing your stream:

`-Jhttpclient.socket.https.cps=19200000`

For more information about this, check out [Apache’s documentation](https://wiki.apache.org/jmeter/Controlling%20Bandwidth%20in%20JMeter%20to%20simulate%20different%20networks).

### Network bandwidth throttling in Gatling
With Gatling, this is also indirectly possible to simulate by throttling the number of requests per second. It’ll be a little more difficult to correlate requests per second to network bandwidth, but seeing historical data of real mobile users of your application should help here. Then you can multiply that by the number of users in your simulation and set up the throttling using something like this:

```scala
setUp(scn.inject(constantUsersPerSec(100) during (30 minutes))).throttle(
reachRps(100) in (10 seconds),
holdFor(1 hour)
)
```

[Here’s Gatling’s documentation](https://gatling.io/docs/2.3/general/simulation_setup#simulation-setup-throttling) for more information on this.

### Where in the world are your users?
The geographical location of your load test generators affects the response time you’ll get. If you use on-premises machines to generate the load and see 1-second response times, the machines are on the same corporate network as your application servers and have less latency. This means that the response times will be a lot faster than those of a client using your application from across the world.

Depending on where your customers live, latency can change the reported response time. In general, you would want to have a look at your analytics and see where most of your customer base is. Ideally, you’d want to generate load in those regions— remember, we’re trying to make your load testing as realistic as possible.

This is one big reason to switch from on-premises load generators to load generators in the cloud. Service providers like [Amazon](http://aws.com), [Azure](http://azure.com) and [Google](http://cloud.google.com) allow you to provision machines with a few clicks and even select their location. Load testing on the cloud can be significantly cheaper (because you don’t have to provision or maintain physical machines and you only pay for when you use them) and more realistic, because they allow you to approximate the effect of distance on your application response times. It also allows you to test the effect of [[Content Distribution Networks]](CDNs), if you’re using any.

## Prepare for your next major event with Flood
If you are under the gun to load test before your next major event, especially if that is the Melbourne Cup, we are here to help!

Make sure to sign up for your [free trial of Flood](http://), which can be done in under 5 minutes and will give you 5 free node hours to run your first load test.  We are [here to chat](https://flood.io/contact-flood/) and would love to discuss your strategy to prepare for your next major event.

Happy testing!

## References
- 2018 Melbourne Cup Carnival delivers record economic benefit. (2019). _Victoria Racing Club._ Retrieved from https://www.flemington.com.au/news/2019-04-18/2018-melbourne-cup-carnival-delivers-record-economic-benefit
- Amsel, P. (2017). Two-thirds of Australian betting turnover is done digitally. [_CalvinAyre.com_](http://CalvinAyre.com). Retrieved from https://calvinayre.com/2017/05/18/business/digital-two-thirds-australian-betting-turnover/
- Agrawal, A. (2018). Millions scale simulations. __Hotstar.__ Retrieved from https://blog.hotstar.com/millons-scale-simulations-1602befe1ce5
- Cheik-Hussein, M. (2018). Melbourne Cup TV ratings up slightly, as streaming skyrockets. _AdNews_. Retrieved from http://www.adnews.com.au/news/melbourne-cup-tv-ratings-up-slightly-as-streaming-skyrockets
- Singh, M. (2019). Hotstar, Disney's Indian streaming service, sets new global record for live viewership. _TechCrunch_. Retrieved from https://techcrunch.com/2019/05/12/hotstar-disneys-indian-streaming-service-sets-new-global-record-for-live-viewership/
- Tabcorp acknowledges betting web site poor performance. (2008). _Throughbred News_. Retrieved from http://thoroughbrednews.com.au/news/story/tabcorp-acknowledges-betting-web-site-poor-performance-36333?section=Australia
- Toscano, N. and Cunningham, M. (2018). Online betting sites crashed in lead-up to Melbourne Cup. _The Age_. Retrieved from https://www.visitmelbourne.com/regions/melbourne/events/sports/horse-racing/spring-racing-carnival
- Types of betting. (Accessed in July 2019). [_Racing.com_](http://Racing.com). Retrieved from https://www.racing.com/new-to-racing/types-of-betting
- ‍
