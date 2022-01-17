---
title: "Testing tool cheat sheet for load testers who don't just care about numbers"
date: 2022-01-17T16:30:07+01:00
draft: false
tags: ['english', 'text', 'performance', 'gatling', 'jmeter', 'k6.io', 'flood.io', 'locust', 'playwright', 'puppeteer', 'ship30for30']
---
It's not enough to decide _how much_ load you want to generate. You also have to know _how_ you're generating it.

Your approach affects what part of your application is tested, the results returned, and the budget you'll need to run your test.

Here are three main categories of load testing tools:

## Protocol-based load testing tools:

These tools simulate the underlying messages sent back and forth between an application and a client.

_Choose a protocol-based tool if_: you want to generate massive load, you want to load test before components are integrated, you want to test APIs, or you are budget-conscious.

_Best in class tools_: Gatling, JMeter, k6, Locust, Neoload

## Browser-based load testing tools:

These tools automate real user interactions with an interface.

_Choose a browser-based tool if:_ you want to measure end-to-end performance, you want to reuse your browser automation scripts, you want front-end performance metrics, or you have a higher budget.

_Best in class tools:_ Cypress, Flood Element, k6, Playwright, Puppeteer

## Hybrid load testing tools:

This approach is a mixture of the previous two. You can do this in a few ways:
-   Use a protocol tool to generate the majority of the load, and a browser tool for a handful of virtual users _(best functionality, highest effort/cost)_
-   Use a browser-based tool for all load _(expensive, simplest)_
-   Find a tool that can do both _(ideal solution, few options)_
    
## Whatever you choose, compare like with like.

Happy testing!