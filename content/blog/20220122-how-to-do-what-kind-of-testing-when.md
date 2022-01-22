---
title: "How to Do What Kind of Testing When: Testing Types by Scope"
date: 2022-01-22T16:42:49+01:00
draft: false
tags: ['text', 'english', 'performance', 'testing', 'ship30for30']
---

Correctly identifying _when_ you test could be just as important as _what_. Below are types of testing according to scope.

### Static testing

Static testing occurs when requirements are written. Question requirements and spell out what each one means.

_Concerns:_ Setting up a system to track and link requirements to test cases, negotiating business needs with technical feasibility, clarifying scope.

### Unit testing

Unit testing occurs when coding begins. Practice Test-Driven Development by translating requirements into tests before writing the code.

_Concerns:_ Treating test code like application code, getting developer buy-in, communicating technical implementation, performance, pair programming.

### System testing 

System testing occurs when a build is released. Employ black-box testing: step back from the code and assess the feature as a whole for consistency.

_Concerns:_ Adherence to common design standards, equivalence partitioning, boundary value analysis, fighting scope creep, usability, creating test data.

### System integration testing (SIT)

SIT occurs when integrating multiple components. Use white-box or grey-box testing to target the interactions and traffic between components.

_Concerns:_ API testing, stubbing and mocking, identifying request paths throughout the system, performance benchmarking, observability and analysis.

### Business acceptance testing (BAT)

BAT occurs when the code is assessed against overall business goals. Seek out SMEs who can help you verify expected outcomes.

_Concerns:_ Adherence to business requirements and regulations, process testing, simplifying request flows, identifying potential customer pain points.

### User acceptance testing (UAT)

User acceptance testing occurs before code is released to production. Map test cases to requirements and test real-world scenarios.

_Concerns:_ Testing for superuser workflows, data cleansing, verifying real user behavior from historical logs, exploratory testing, end-to-end performance.

### Regression Testing

Regression testing occurs between builds. Supplement a robust automation test suite with nuanced manual test cases that address known problem areas.

_Concerns:_ Setting up a CI/CD pipeline, deciding what to automate, consolidating test and development tools, tracking failures over time.

### Question everything

Remember: **testing is an attitude.**