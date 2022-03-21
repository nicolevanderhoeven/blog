---
title: "Real Browser Testing With xk6-browser"
date: 2022-03-16T16:55:56+01:00
draft: false
tags: ['english', 'video', 'k6.io', 'browser', 'testing']
---

{{< youtube y04wavsZxSs >}}

_Transcript:_

Without a doubt, my favorite k6 extension is xk6-browser. xk6-browser finally brings browser test automation to k6. So you don't need to learn a new tool or figure out how to integrate it if you already have load tests. You can create JavaScript-based, browser-driven tests with k6. Here's how. 

Since xk6-browser is an extension, we're gonna need to build a custom version of k6 that includes that extension. And the thing that builds that is called xk6. What I'm doing here is I'm instructing xk6 to create a build using version 0.35 of k6, that includes xk6-browser. And this is a link to the repository where xk6-browser is stored. 

## Writing a browser testing script

So now that we have a version of k6 that includes xk6-browser, the next step is to create the browser script. Now you can do that in the one script, but just for ease of debugging I'm gonna put it in another script for now. We're not going to be using the HTTP requests anymore so I'm going to import launcher from k6/x/browser. And I'll save that as browser. 

I'm definitely going to be using sleep, so let me go ahead and import that now as well. We'll also need a default function for this. We're setting up an instance of the launcher that's going to launch Chromium in particular, and we do want to see it so I'm going to say `headless: false`. If you set this to true, that means that you won't actually see the web browser being driven by the script, which is handy to see during demos. So we'll do that, and then we have to set up the context. 

So browser, oops, new context. And then we set up a page. The first one is go to the homepage. The second one is to view a product. Third, add the product to the cart. Fourth is go to the cart and then last, I want to check out. So to do that, I've already defined the browser context in page. Now I need to do `page.goto http://ecommerce.k6.io` and I will also want to wait for `waitUntil: networkidle`. 

Great. I wanted to add some sort of check to make sure that I've actually gotten to a place so, let's open up DevTools here and I wanna make sure that some results are displayed. I don't necessarily need, you know 1-12 of 17 but, I want this one. Okay, so I'll also say `page.waitForSelector` and that'll be this. 

And then let's do a screenshot, because we just for, just in case we wanna debug later we wanna make sure that we will be able to have a look at at this screenshot to see what exactly went wrong. And I'll put that in screenshots and I'll say `01_homepage`. Then let's do a sleep. And I always like to do the random one. Random, and let's say it from zero to four. This time I'm doing the custom k6 version `browser.js`. 

For browser-based tests, I find it much more useful to actually see what's going on rather than to look at the output. Because as you can see there are all sorts of errors here and I believe that they're actually application errors so they can be a little bit misleading. It looks like that happened but let's just look at the screenshots. Screenshot, yeah. That, that loaded fine. So we can continue.

Next step is to view a product. Okay, let's go back here. This time I want to click this thing. It doesn't really matter which, which item it is. I'll just choose the first one. Looks like this is the actual product link. So let element = page. And this is where we actually paste the selector which is what I got from DevTools. 

And then we haven't done anything yet with it. We want to actually click it. So `element.click`. After that though, I'm going to want to make sure that we get to the right page. So, let's see what happens when we click it. What can we look for? I guess we can look for this add to cart button, cuz if the item didn't show up then we wouldn't be able to add it to the cart. So let's grab that. Button, button name is add to cart. Copy that. 

So then I'll say `page.waitForSelector`, the selector with a button name there. Take another screenshot because why not? I'll say `02_view-product` and then another sleep. From here it was pretty much more of the same. Here's me scripting adding the product to the cart, viewing the cart and then finally going to the checkout page. And here's what happened when I played it all back. Here it is going to the homepage, and then clicking on the first product, and then adding that product to the cart, and then clicking view cart, and then proceeding to checkout. 

The best part about this is that you don't have to choose between the browser test and the protocol test. They're both in k6 and written in JavaScript so you could include them in the same script. You can use stages to schedule when one starts and when one ends. You can change the load profile, add checks and thresholds. And you can also use all of the output options that are available for protocol tests for the browser tests as well. 

The catch is that xk6-browser is really new. We've just announced it. It's still in beta so you are likely to come across more than a few bugs. However, I'd still recommend that you give it a go. I've been playing around with it and I've found it more than serviceable for a lot of my use cases. Plus it's just really cool to be able to test front-end performance along with back-end performance in the same testing script. 

Thanks for watching. I will put a link to the xk6-browser repository below and happy testing.