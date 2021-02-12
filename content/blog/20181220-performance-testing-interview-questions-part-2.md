---
title: "Performance Testing Interview Questions, Part 2: JMeter"
date: 2018-12-20T14:47:18+01:00
draft: false
tags: ['english', 'text', 'performance', 'jmeter']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/performance-testing-interview-questions-part-2-jmeter-interview-questions">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/performance-testing-interview-questions-part-2-jmeter-interview-questions)._

In this part, we’ll go over some questions that are commonly asked in technical interviews about the use of the most popular open-source load testing tool, [Apache JMeter](http://jmeter.apache.org/).

### Using JMeter, you record a key business process. Upon playing it back, however, you notice an error on the first page. What could have gone wrong and how would you fix this?
While recorders have gone a long way towards making scripting easier, modern security measures like the implementation of viewstates have also made scripting more complicated to record. Some more complicated applications will pass dynamic values in responses that it expects to see in the succeeding request, otherwise the request is blocked. This is great for security, but it also means that you will need to manually extract these values in your script.

In JMeter, you would do this by adding a response extractor to your sample that will extract the dynamic string according to rules you set, and then save the string to a parameter. This parameter must then be used in the next request that you send.

While running your test plan, you get the error: `java.lang.OutOfMemoryError: Java heap space`. How do you fix it?
The easy fix is to edit `jmeter.bat` and increase the heap memory (search for `HEAP`) and increase heap space allocated like this:
`HEAP="-Xms512m -Xmx2048m"`

The part in bold increases the heap space to 2 GB.

However, it’s also worthwhile looking at your test plan and removing any obvious memory hogs. One of the things we see a lot is enabled listeners that aren’t even being used. Listeners are great while debugging, but should be disabled when running a load test. Writing too many lines to the log is another culprit here that should also be commented out when running important tests. And of course, you should always run JMeter in non-GUI mode during load tests!

### After running a load test, the results show that 300 transactions were executed with a PASSED status and returning responses of HTTP 200. However, the DBA tells you that there were no records written to the database as a result of the transactions. How would you troubleshoot this?
I see this happening with clients all the time, so I think this makes a great technical interview question. This is also why I said earlier that you shouldn’t count on a test tool to tell you a test has passed. It’s possible for a transaction to have the status PASSED and return an HTTP 200 but still be hiding an error.

This is mainly due to poor scripting that does not include validations that check whether the script has gotten to the right page. For example, you could use a Response Assertion as a child of your home page sample with the words “Welcome, Nicole” to determine whether the user Nicole has logged in successfully.

This is a critical step, because without it, it’s possible for a server to return a nice error page, or an incorrect one, such as the home page, with an HTTP 200.

### How do you use a data file to read user account details from a CSV in JMeter?
JMeter has a [CSV Data Set Config Element](https://jmeter.apache.org/usermanual/component_reference.html#CSV_Data_Set_Config) built specifically for this purpose. You can simply add one to your test plan, browse to the CSV file that you’d like to use, and select the options for how to share that data among the threads in your JMeter script.

### How would you go about testing a website that uses HTTP/2 on JMeter?
There is a JMeter plugin called HTTP/2 Sampler that accomplishes just this. My colleague Jason just wrote [a blog post](https://flood.io/blog/jmeter-tutorial-http2-test/) on this very topic, but basically the plugin adds new HTTP/2 versions to the standard HTTP request and request defaults samplers as well as the Simple Data Writer and View Results Tree listener. These elements will need to be used in order to test an application using HTTP/2.

### What can you do to synchronise the execution of multiple JMeter instances on different load generators?
Apache JMeter has released [this handy PDF file](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.pdf) to describe the steps necessary to run JMeter in distributed mode. This involves installing Java and JMeter on all machines and setting them up in a master and slave configuration so that one machine controls the rest. On the master, you’ll need to add remote hosts to the jmeter.properties file. When everything is set up, you should be able to open up JMeter on the master and do a a remote start of your current test plan on any or all slaves that you choose.

The problem with this setup is the clunkiness of working with different machines and essentially having to set them up the same way. After the test, there’s the daunting task of logging back onto each machine, gathering the data, and transferring them back into a central repository. Then you’re faced with consolidating the data from each injector in order to see a picture of the whole test. You can see that this set up quickly goes from time-consuming to a nightmare, especially when potentially thousands of different machines are involved.

If only there were [an easier way](https://flood.io/)...