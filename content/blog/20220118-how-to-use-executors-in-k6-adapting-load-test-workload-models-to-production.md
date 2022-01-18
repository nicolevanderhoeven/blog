---
title: "How to Use Executors in k6: Adapting Load Test Workload Models to Production"
date: 2022-01-18T22:45:52+01:00
draft: false
tags: ['english', 'text', 'performance', 'k6.io', 'workload model', 'ship30for30']
---
Executors in k6 are like traffic cops.

They define the shape and volume of traffic that your k6 load testing script follows during test execution. Executors can also drastically affect your results if you don't get them right.

Here are all the executor options in k6 and when you should use each one:

## k6 executors

-   **_shared-iterations_**: Fix the number of total iterations for the entire test. Use when you want to create precisely X rows of test data during a prep run.
    
-   **_per-vu-iterations_**: Fix the number of iterations each virtual user (VU) does. Use when you want each VU to use exactly X rows of test data.
    
-   **_constant-vus_**: Fix the number of VUs and duration, but allow the number of iterations to vary. Use for straightforward tests or shakeout tests.
    
-   **_ramping-vus_**: Set stages, each with a number of VUs and a duration, and let the number of iterations vary. Use for easiest comparison with other load testing tools and for custom load profiles.
    
-   **_constant-arrival-rate_**: Fix the number of requests per second (rps) and duration, and allow the number of VUs and iterations to vary. Use when you have a simple load profile with a request throughput requirement (rps).
    
-   **_ramping-arrival rate_**: Like **_constant-arrival-rate_**, but with stages. For each stage, fix the number of rps and duration. Use for spike tests, multiphase load profiles with distinct requirements, and Game Day simulations.
    
-   **_externally-controlled_**: Fix max VUs and time, and allow everything else to be changed at runtime. Use for disaster recovery, breakpoint, or stress tests where you want ultimate flexibility in adapting your test to real-time results.
    

## Still unsure?

Use **_ramping-vus_**. It's probably what you're used to from other tools.

Ready to move up? Use **_ramping-arrival-rate_**. Rps is a better (but still not perfect) measure of throughput for comparison than just the number of VUs.

## When in doubt, look at production.

Making sure your test looks and acts like real traffic yields the best results!

For more details, check out [the k6 documentation](https://k6.io/docs/using-k6/scenarios/#executors)