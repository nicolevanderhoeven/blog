---
title: "Introducing Flood Agent: standalone infrastructure for load testing"
date: 2020-04-07T19:03:42+01:00
draft: false
tags: ['performance', 'english', 'text', 'flood.io', 'video']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/introducing-flood-agent-standalone-infrastructure-for-load-testing">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/introducing-flood-agent-standalone-infrastructure-for-load-testing)._

Working from home during this pandemic and wondering how to start load tests from the office? Today, we're officially introducing Flood Agent, a way to turn your own physical or virtual machines into load generators that you can control from anywhere with an internet connection.

## TL;DR:

- Installing Flood Agent on a machine lets you start load tests on it remotely from Flood—even if it's within a corporate VPN.
- Flood Agent is a simple binary that you can install on Linux, macOS, and Windows machines.
- Once you've installed Flood Agent, your machines show up on the Flood web app to use as load generators or grids.

## Boldly going where no one has gone before

Load testing within your company's VPN and trying to coordinate it from home is like being on a maintenance pod trying to contact your starship, but a Mazarite ship is broadcasting a jamming signal, so comms are down. That Mazarite ship is your company's firewall, and it can make testing difficult.

‍![](/assets/20200407-01.jpg)

The easiest way around this is to provision load generators in the cloud. However, because your application servers are still behind a firewall, you'd need to convince IT security to [whitelist the IP addresses](https://guides.flood.io/test-execution/infrastructure/static-ip-addresses#hosted-grids) of the load generators. Depending on how tight security policies are, this may not be an option even in this new world of remote working.

Flood Agent is a way to start load tests on Flood from the load generators you already have. It's a cross-platform agent that you can install on your regular load generators, allowing you to control them on Flood.

‍‍![](/assets/20200407-02.png)

Flood Agent is kind of like the [Borg Collective](https://en.wikipedia.org/wiki/Borg#Borg_Collective). Each machine that you install Flood Agent on is assimilated into the Borg. A hive mind (you, on the Flood site) controls all Borgs, coordinating test execution with robotic efficiency.

![](https://media.giphy.com/media/J6P7vFEQ6PcgE/giphy.gif)

Check out this video to follow along as I walk you through the process of setting up Flood Agent, or you can keep reading for the text version.

‍{{< youtube 6VFn96aKSU8>}}
‍
## Installing and configuring Flood Agent

Flood Agent is a free binary, and it runs on Linux, Mac, or Windows machines. You can [download the appropriate version](https://github.com/flood-io/flood-agent/releases/latest) for your operating system and then follow the installation instructions here for more information:

[Getting started on Linux](https://guides.flood.io/infrastructure/standalone-infrastructure/getting-started-on-linux)

[Getting started on macOS](https://guides.flood.io/infrastructure/standalone-infrastructure/getting-started-on-macos)

[Getting started on Windows](https://guides.flood.io/infrastructure/standalone-infrastructure/getting-started-on-windows)

After installing Flood Agent, you can configure it according to how you want to use it. Start Flood Agent in your terminal and use the configure functionality. Here's what that command looks like on macOS, but you can follow the links above for other operating systems:

```shell
./flood-agent configure
```
### Linking your Flood account

The command above yields a prompt for a token like this:

![](/assets/20200407-03.jpg)

This token allows Flood to run load tests on the load generator that you've installed Flood Agent in. To get the token, go to the [API Access page](https://app.flood.io/account/api) on your Flood account ([you already have one, don't you?](https://app.flood.io/sign-up)) and click REVEAL token.

![](/assets/20200407-04.jpg)

You should see a string of characters like this:

![](/assets/20200407-05.jpg)‍

Copy your token (anything after the = sign) and paste it into the Flood Agent terminal window.

### Choosing load testing tools

Next, you can choose which tools you'd like to set up and which version of those tools Flood Agent uses to run your tests.

‍![](/assets/20200407-06.jpg)

Starting with JMeter, Flood Agent asks you which of the tools you'd like to configure. You can choose to set up your tools at the beginning so that you don't have to set them up again, or you can go back to this configuration wizard at any point to add another tool. Either way, you need to provide the tools that you select in one of two ways: via a Docker image supplied by Flood, or via a [local installation](https://guides.flood.io/infrastructure/standalone-infrastructure/getting-started-local-jmeter-and-gatling) that you already have.

For this example, I chose to configure JMeter and to use a local installation. Local installations give you the most flexibility because you can use the version of the tool that you prefer, along with any special plugins. However, if you already have Docker installed or don't want to manually install JMeter separately, you can also use our Docker image for JMeter.

Selecting a local installation prompts you to provide the location of that directory:

‍![](/assets/20200407-07.jpg)

For JMeter, this looks something like `/Users/nvanderhoeven/jmeter/apache-jmeter-5.1.1.`

After you enter this file path, Flood Agent checks to make sure the directory is valid. You can also set the configuration for other tools in this dialog.

![](/assets/20200407-08.jpg)

After you finish the configuration, the wizard writes to a config.yaml file in your Flood Agent directory. You can also edit this configuration file directly in the future if you prefer.

## Verifying Flood Agent configuration

To run a final check on whether Flood Agent has been installed correctly, type `./flood-agent check`. You should see a summary of the configuration options you selected as well as some connectivity and validity checks, like this:

‍
![](/assets/20200407-09.jpg)

These green check marks mean you're good to go! If you're running Flood Agent from within a corporate network, though, you may see some errors here.

## Troubleshooting network connectivity within a corporate network

If your company already has a web proxy, check out [our guide on running floods through this proxy](https://guides.flood.io/infrastructure/standalone-infrastructure/deployment/integrating-with-a-web-proxy).

Please ensure that the load generator that you've installed Flood Agent on has access to the following endpoints:

```shell
<https://drain.flood.io>
<https://beacon.flood.io>
<https://vault.flood.io>
<https://flood-archives.s3-accelerate.amazonaws.com>
<https://logs.us-east-1.amazonaws.com>
<https://sns>.*.amazonaws.com
<https://sqs>.*.amazonaws.com
```

You may need to request these from your IT department.

If you get stuck, please contact us at [support@flood.io](mailto:support@flood.io). We'd love to go over your specific situation and get you up and running.

Once Flood Agent returns a successful check, you can start up your own grid!

## Turning your machine into a Flood grid

A grid, in Flood terminology, is a group of machines to be used for load generation. To make your machine a grid, run this command:

```shell
./flood-agent --grid askaflooder
```

where `askaflooder` is the name of your grid.

‍![](/assets/20200407-10.jpg)

Once you see those [agent] ready and awaiting next job messages, you're ready to run your test!

## Running a load test on your own infrastructure

Log into your account on Flood, if you aren't already, and [create a new stream](https://guides.flood.io/overview-of-flood/scripting-your-load-test#creating-a-stream) like you normally would, uploading your load testing script and data files. When [launching your test](https://guides.flood.io/overview-of-flood/launching-your-test), though, select the option for Hosted infrastructure and then choose the grid with Flood Agent running on it.

‍![](/assets/20200407-11.jpg)

Go ahead and launch your test. Congratulations, you're now set up to run a load test on your on-premise load generators!

## Giving it a go
Flood Agent is a free download, so you'll only need to pay when you run load tests on Flood. However, we also have a free tier— perfect for a proof-of-concept while you're working from home.

If you have any questions about Flood Agent, check out [our documentation](https://guides.flood.io/infrastructure/standalone-infrastructure/flood-agent) or [email us](mailto:support@flood.io). We'd be happy to get you started!

[Download Flood Agent for free here](https://github.com/flood-io/flood-agent/releases).

‍![](/assets/20200407-12.gif)