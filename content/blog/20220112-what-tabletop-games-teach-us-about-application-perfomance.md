---
title: "What Tabletop Games Teach Us About Application Perfomance"
date: 2022-01-12T16:30:29+01:00
draft: false
tags: ['testing', 'text', 'English', 'ship30for30', 'tabletop games', 'performance']
---

# What tabletop games teach us about application performance

Tabletop games and application performance have more in common than you might think.

See, it's all about optimization. Both involve juggling several variables: some that you can control, and some that you can't.

Here's what I've learned about application performance from playing tabletop games.

## #1: Get more workers

In worker placement games, you should always spend your first worker to train more workers.

Similarly, one of the most basic ways to increase concurrency is multithreading: using more than one thread at a time. (See: Golang) This applies to testing tools as much as to systems. The 1 Thread: 1 Virtual User paradigm is flawed.

## #2: Spend time on getting your engine going

Get your big combos in place before you tap to attack.

Things like setting up automation frameworks or CI/CD pipelines DO set you back in the beginning, but they are worth their mana cost in the long run.

## #3: Draft with others in mind

The trick to drafting is knowing what you're leaving for others as much as what you're taking for yourself.

The short game is getting your team to do the testing. The long game is getting everyone in the company involved in testing.

## #4: Hope for a nat 20, plan for a nat 1

Sometimes proficiency, expertise, and a luckstone just aren't enough.

Instead of wondering _whether_ an app will fail, take for granted that it will, and start planning for it. Keep that Action Surge in your back pocket.

## #5: Sometimes, you just have to trade for sheep

The 2:1 port is valuable, but not always the best option.

Learn what you can, but accept that you can't learn it all. Reach out to others with compatible skillsets and ask the "stupid" questions that nobody else wants to ask.

## Testing is a team sport, and everyone gets a chance to play.

Happy gaming!