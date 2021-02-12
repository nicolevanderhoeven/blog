---
title: "Should I Upgrade to JMeter 4.0? 5 Reasons to Upgrade"
date: 2018-02-23T23:43:25+01:00
draft: false
tags: ['english', 'text', 'jmeter', 'performance']
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/should-i-upgrade-to-jmeter-4-0-5-reasons-to-upgrade">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/should-i-upgrade-to-jmeter-4-0-5-reasons-to-upgrade)._

Apache has just launched [JMeter 4.0](http://jmeter.apache.org/download_jmeter.cgi), a big step up from their previous release, 3.3, which was only released in September last year. Apache seems to be stepping up the frequency of it’s releases, and we’re not complaining. JMeter is an amazing open source load testing tool and the most popular one used at [Tricentis Flood](http://flood.io/) by far.

The big question is: Should you upgrade? Are the new features worth the leap? Will the new black UI make you a better load tester? While this choice should be made on a case-by-case basis and we certainly can’t pretend to give one-size-fits-all advice, here are some good arguments to do it:

### #1: Java 9 support
JDK 9 was released back in September 2017, and if you were one of the people who upgraded to it when prompted, you would have noticed to your frustration that JMeter 3.3 did not play well with it, yielding the error:

```bash
Error: Java version -- 9.0.1 -- is too low to run JMeter. Needs a Java version greater than or equal to 1.8.0 errorlevel=3
```

Good news! This is now fixed. JMeter 4.0 runs smoothly on JDK 9. We'll continue running on JDK 8 at Flood for consistency amongst all our open source load testing tools.

### #2: New Boundary Extractor
Previously, my preferred way to extract dynamic values in JMeter was to use a regular expression extractor, but there’s no doubt that it can sometimes be tricky to get just the right text out of a response. Enter the [Boundary Extractor](http://jmeter.apache.org/usermanual/component_reference.html#Boundary_Extractor).

The boundary extractor allows you to simply set the text immediately before and after the text you want to extract. This saves you wondering whether you should have used a + or a * in your regular expression, and is also easier to validate.

![Boundary Extractor in JMeter](/assets/20180223-01.png)

### #3: New JSON assertion element
While XPath assertion was great, there was previously no counterpart for JSON. The [JSON Assertion](http://jmeter.apache.org/usermanual/component_reference.html#JSON_Assertion) element fills that void nicely, using [JsonPath](https://github.com/json-path/JsonPath) to quickly assert the existence (or non-existence, with the Invert assertion option ticked) of a particular element.

![JSON Assertion element in JMeter](/assets/20180223-02.png)

### #4: New throughput timer
We have a new throughput timer to play with, and it’s called [Precise Throughput Timer](http://home.apache.org/~milamber/jmeter-4.0RC4/docs/usermanual/component_reference.html#Precise_Throughput_Timer).

![Precise Throughput Timer in JMeter](/assets/20180223-03.png)

Whereas the Constant Throughput Timer also had the disadvantage of constant pacing of requests, the Precise Throughput Timer is based on the [Poisson Random Timer](http://home.apache.org/~milamber/jmeter-4.0RC4/docs/usermanual/component_reference.html#Poisson_Random_Timer) and randomly generates the delay between each request. The implementation seems to be well thought out, with the component reference section listing a lot of scenarios they’ve tested for that the previous Constant Throughput Timer might have struggled with. Throughput timers are one of my favourite JMeter features, and still rather unique in the industry.

### #5: Test Plan Autosave
This one’s more of a usability tweak, but it’s a good one. JMeter now automatically saves your script when you run a test, saving you from those all-too-familiar “Wait… did I CTRL+S before I hit CTRL+R?” moments.

Click [here](http://home.apache.org/~milamber/jmeter-4.0RC4/docs/changes.html) to see the full release notes for version.

### BONUS reason: Tricentis Flood support
You can now upload JMeter 4.0 scripts to flood.io and be up and running with your first test hosted on one of our grid nodes around the world. Our customer support team is always happy to help you make the switch to 4.0.