---
title: "How AirTasker uses Ruby JMeter and Flood for their load testing"
date: 2020-02-24T18:23:31+01:00
draft: false
tags: ['performance', 'jmeter', 'ruby', 'flood.io', 'english', 'text']
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/how-airtasker-uses-ruby-jmeter-and-flood-for-their-load-testing">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/how-airtasker-uses-ruby-jmeter-and-flood-for-their-load-testing)._

In the recent RubyConf 2020 held in Melbourne, Australia, Nancy Cai from AirTasker talked about how they built a performance testing framework using Ruby JMeter and Flood. Luckily, we had some pleasantly surprised Flooders in attendance to take notes during this fantastic talk!

AirTasker is a platform allowing the outsourcing of everyday tasks. When discussing the reasons that AirTasker decided they wanted to carry out performance and load testing, Nancy told a fascinating story about an overly successful marketing campaign—a good problem to have, but a problem nonetheless. The Sydney Cats and Dogs Home, an animal shelter, teamed up with AirTasker to pay one lucky person $500 to spend the day playing with the resident animals. The prospect of this dream job created an enormous surge in AirTasker's traffic that caused alarm bells to go off on the underlying application servers, resulting in an end-user experience that was less than desired.

Nancy included this hilarious slide about some common feelings regarding application performance.

![A common feeling when application performance is brought up](/assets/20200224-01.png)

## Steps for running a performance test, the AirTasker way
To avoid repeating that mistake, Nancy and her team set out to run performance testing by using the following simple steps:

1. Determine performance criteria.
2. Configure the test environment to be as production-like as possible.
3. Plan and design based on user behavior, including preparing test data.
4. Implement test design and set up the framework (which in AirTasker's case involved Ruby JMeter as the performance testing tool and Flood as a load testing solution).
5. Run test.
6. Analyze and fine-tune results.

## Setting up a load testing tool and framework
When it came to selecting the right tools for the job, AirTasker wanted tools that met the following criteria:

- Ability to simulate production-like traffic easily
- Widespread use in the industry
- Ease of creation and maintenance of tests for everyone
- Historical results aggregation
- Visualization of performance metrics
- Integration with CI and monitoring tools

Nancy's team compared several load testing tools and found they enjoyed using the Apache JMeter tool, which is a popular open source load testing software. However, they quickly ran into an "out of memory" error after attempting to run about 400-800 concurrent users on a single machine. She and her team decided to use a distributed load testing platform to run the load they required to scale up more effectively.

Enter Flood.

## Why AirTasker chose Flood

![JMeter, Flood, and the Ruby JMeter gem combination is a winner](/assets/20200224-02.png)

> We also chose Flood.io [...] because it comes in with a really good open-source gem called Ruby JMeter. It is a Ruby-based DSL for building JMeter test plans. - Nancy Cai, AirTasker

Nancy and her team enjoyed the benefits of being able to write load tests natively in Ruby and then using Flood's Ruby JMeter gem, which is a Domain-Specific Language (DSL). Flood allowed them to turn their Ruby scripts into .jmx files, which is the native XML format that JMeter uses.

When they were ready to scale up, AirTasker ran the same JMeter script in Flood.

![Sample of a report on Flood from a JMeter test](/assets/20200224-03.png)

The real-time Flood dashboard allowed them to see that there was a problem on one of the API endpoints, called "Get pet reviews." Further investigations revealed a performance issue due to a long-running query against a database server in the code, which AirTasker's developers could fix.

## Best practices

Nancy gives some great advice for anyone running a performance test, including:

- asking the right questions as a load tester
- running baseline tests
- being aware of the difference between your test and production environments
- keeping in mind the caching and autoscaling mechanisms that may drastically change the results
- the differences between stress testing and other types of performance testing

We were so thrilled to hear Nancy's story on how Flood helped AirTasker run their performance tests. Catch the entirety of Nancy's talk below, and check out the resource links at the end of the post to follow Nancy's story.‍

{{< youtube Q09wJm4P8Xw >}}

[Flood's Ruby JMeter gem](https://github.com/flood-io/ruby-jmeter)

[Nancy's GitHub repo](https://github.com/nancy-cai/performance-test-ruby-jmeter) where you can find a copy of her test scripts

Follow Nancy on [Twitter](https://twitter.com/nancycai8)

Follow Nancy on [GitHub](https://github.com/nancy-cai)

