---
title: "The Tester's Toolbox Is Flawed"
date: 2022-01-11T16:30:49+01:00
draft: false
tags: ['personal knowledge management', 'testing', 'text', 'English', 'ship30for30']
---

Every tester has a toolbox.

In the toolbox rests a variety of tools for every conceivable purpose. Part of our job, as testers, is to choose the right one for the job. Sounds reasonable, right?

That kind of thinking could be dangerous.

## "The right tool for every job" fails for multiple jobs.

You end up with multiple tools. One for accessibility testing. Another for API testing. Another for browser testing. Another for load testing. _This is the modern tester's dilemma_: we spend more time working with our tools than with the application under test.

In the real world, including a new tool in your testing stack means a new framework, usually a new programming language, and sometimes even new colleagues with experience in those tools. And what about continuous testing? All those tools have to talk to each other at some point.

More tools = more time, effort, and money.

### **When choosing tools, prioritize multitools.**

A multitool can be used for different purposes and prioritizes flexibility.

Here are a few ways to spot a multitool:

**#1: It is a polymath.** A multitool is good at many things and is limited in use case only by the imagination of those that use it.

**#2: It uses what you know.** A multitool is built on languages and frameworks you and your team already know, reducing ramp-up time.

**#3 It plays well with others.** A multitool doesn't force you to use it to the exclusion of everything else. It integrates well with best-in-class tools.

When you optimize for individual jobs, you're missing the big picture. You're ultimately left holding the ends of multiple tools and creating a kraken of a test suite with all these tools cobbled together.

Instead, prioritize multitools.

