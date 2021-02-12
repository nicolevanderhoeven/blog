---
title: "Performance Testing Interview Questions, Part 3: LoadRunner"
date: 2018-12-20T22:54:24+01:00
draft: false
tags: ['text', 'english', 'loadrunner', 'performance']
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/performance-testing-interview-questions-part-3-loadrunner-interview-questions">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/performance-testing-interview-questions-part-3-loadrunner-interview-questions)._

Like it or not, [LoadRunner](https://www.microfocus.com/en-us/products/loadrunner-load-testing/overview) is one of the most popular commercial load test tools, and with good reason. Its protocol support is extensive, and many a load tester has cut his/her teeth on LoadRunner. In this last part of our interview series, we’ll go over some questions you may have to answer when interviewing for a role using Mercury HP MicroFocus LoadRunner.

### What sort of transactions would you put into vuser_init and vuser_end?
Both are used for transactions that would only need to run once, at the beginning and at the end of a script. They’re akin to [JMeter](http://jmeter.apache.org/)’s `setUp` and `tearDown` thread groups. Some things you might put in vuser_init are user logins or navigation to get to the start of the business process you really want to test, and logouts and any data cleanup to reset the application for the next test are common things to put in vuser_end. Note that if you want each virtual user to iterate through a list of user accounts during the test, you _won’t_ want to put logins and logouts in vuser_init and vuser_end.

### When would you run a script in VuGen and when would you run it in Controller?
VuGen is short for Virtual User Generator, and it’s where the actual scripting is done. Running in VuGen is good for writing or debugging a script, where you can quickly see where a script fails, what the response is, and what you need to change. You can also step through the code line by line (F10) to more accurately see, for example, variable values changing throughout your script. It’s really only for shaking out scripts with a single user. Running in VuGen also only runs from your local machine. Once you’re ready to run a load test, you’d switch to Controller.

The Controller is like the command center in LoadRunner: from the Controller, you can actually ramp up the number of users and choose from different scenario configuration settings in order to tailor your workload model to the scenario you’re trying to test. Controller also runs the scripts headlessly; it won’t open up a separate instance of VuGen for every user, so it’s a lot more resource intensive. Controller will also allow you to configure remote load generators and run scripts on them.

### How would you set up LoadRunner to run certain transactions a certain percentage of the time? For example, for every 100 users that browses to a site, you want 25 of them visiting each of the About, Catalog, Contact, and Reviews pages.
You can write the code to visit each page in separate Actions. Then, in Runtime Settings, you can modify the run logic, create an Action Block that has all four actions, and assign a percentage to them (25%).

Of course, you can also hard code this in C within the actions, if you’d prefer, but moving these values to Runtime Settings makes it easier to maintain and reuse by other testers.

### How is LoadRunner pacing different from how it’s implemented in other tools?
Most test tools allow you to set a fixed or variable pacing that adds onto however long one iteration takes to complete.

LoadRunner has a pacing feature that allows you to set a specific time and then adds a variable amount of time to your test _depending on response times for the included transactions_. So if you set pacing to 5 minutes and one iteration takes 3 minutes to finish, LoadRunner will automatically wait 2 minutes before starting the next one. If it takes 6 minutes, it will not add any more wait time and proceed instead to the next iteration. This comes in handy because you can more accurately predict how many transactions the script will do in a certain amount of time.

### Why would the traffic from a load test on LoadRunner not be seen in Google Analytics?
[Google Analytics](https://marketingplatform.google.com/about/analytics/) runs when the browser of a user downloads and executes a javascript file that then sends information to Google to increment the site statistics for the current visit. However, most traditional load test tools work on the protocol level; that is, they send requests directly to the application server and download resources from a page to simulate users. This means that while they download the Google Analytics script, they don’t execute it, which means the scripted visits aren’t counted.

In order to use Google Analytics to view statistics from a load test, you’ll need to use a browser-level load test tool. LoadRunner actually has this covered with their [TruClient](https://marketplace.microfocus.com/appdelivery/content/truclient) protocol, which interacts with elements on the page like a user would. It will also work for testing single-page applications that use [AJAX](https://en.wikipedia.org/wiki/Ajax_(programming)) to change the data displayed on a page instead of reloading new pages.

Of course, for open source alternatives to TruClient, we at Flood prefer [Element](http://element.flood.io/) or [Selenium](https://flood.io/blog/load-testing-guide-selenium/) load testing, both of that will actually open the site in a browser and executed scripts like a real user.