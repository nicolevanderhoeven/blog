---
title: "Prepare for Viral Videos With Flood Element"
date: 2018-11-08T23:24:31+01:00
draft: false
tags: ['text', 'english', 'element', 'flood.io']
---
{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/prepare-for-viral-videos-with-flood-element">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/prepare-for-viral-videos-with-flood-element)._

One of the more interesting things to load test is video. You see, traditional load test tools are protocol-based, which means that their approach to load testing video is to capture and simulate the traffic that the browser generates under the covers, sending the same requests to the application. This approach can still be successful-- in fact, one of our favourite clients here at Flood recently [used Gatling to simulate 6 million concurrent users](https://blog.hotstar.com/millons-scale-simulations-1602befe1ce5) streaming video from their application. However, for some use cases, testing at the protocol level can’t simulate everything that happens in a real world use case.

## The Challenge
If you’re a video creator, the ultimate goal is often a simple goal: creating a viral video. Unfortunately, preparing for and simulating this all-important use case is typically impossible with protocol based tools. The same feature that makes them so efficient -- not using a browser to send the requests -- is the same thing that prevents them from being used to simulate the needed browser level events. You see, things like view counts on a video are normally tracked by scripts running on the page. Traditional tools download these scripts along with other page resources, but the scripts themselves are not executed. Enter Flood Element.

## A Solution: Flood Element
Flood Element represents a new way of looking at load testing. It is a browser-based tool, which means that it actually drives an instance of the browser to test an application. Rather than telling it what requests to send to simulate a user like you would do with a protocol-based tool, you tell Element which buttons to click or which elements on a page to interact with just as a real user would. Essentially Element IS a user, using your application the way it was meant to be used. This means that it also executes any scripts that would run on the browser side. It’s so realistic that you could even use Element to make your YouTube video viral* by scripting up users to view your content… hypothetically speaking.

## Simulating Real User Views
Testing video with Flood Element is actually pretty easy, especially if you are familiar with open source testing tools like Selenium. If you haven’t yet begun using Element, go through the installation guide [here](https://element.flood.io/). You can download the full script used for this tutorial [here](https://github.com/flood-io/element/blob/master/examples/youtube.ts). In this example, we’re going to be using a YouTube video of the opening credits the classical cartoon Top Cat (the indisputable leader of the gang) from Warner Bros.

### Step 1. Navigate to the video page
Let’s start with a basic script:

```js
import { step, TestSettings, By, Until } from '@flood/element'
export const settings: TestSettings = {
    loopCount: -1,
    clearCache: true,
    disableCache: true,
    actionDelay: 8,
    stepDelay: 10,
    screenshotOnFailure: true,
    userAgent: 'flood-element-test',
}
export default () => {
	step('01_Home', async browser => {
		await browser.visit('https://www.youtube.com/watch?v=6fvhLlrBrPQI')
		
		await browser.takeScreenshot()
	})
}
```

This is the bones of a basic script in Flood Element. It consists of a single step that involves doing two things: visiting the starting URL, which in this case is the direct link to the YouTube video, and then taking a screenshot once loading the page. Taking screenshots is particularly useful when testing video because screenshots give you a way to check that your script is doing what you want it to do. It’s good to take periodic screenshots as well, to measure progress.

To help you validate that the script runs well locally before scaling to hundreds or thousands of users, you can use our Element CLI. If you save the above code as youtube.ts, open up your terminal in that directory and then type:

`element run youtube.ts`

Assuming you’ve got Element set up correctly, you should see something like this: (Note that screenshots are only available when using iTerm as your shell. They are also saved as files under `.../tmp/element-results/youtube` .)
‍
![Screenshots shown while running Element in iTerm](/assets/20181108-01.png)

Oops! It looks like our script does navigate to the page, but it doesn’t play the video. We’ll need to click on that play button. Let’s add that to our script.

### Step 2. Click the Play button
We’ll need to add some lines to click the play button after visiting the page but before we take the screenshot, so that we can verify later whether or not the play button was clicked.

```js
step('02_ClickPlay', async browser => {
	//Click on Play button
	let playBtn = await browser.findElement(By.xpath('//button[@aria-label="Play"]'))
	await playBtn.click()
	
await browser.takeScreenshot()
	})
```


In this example I used Xpath, but you do have the option to select based on partial text, CSS selector, etc. A tool I like to use to get these is Chrome Developer Tools’ Elements tab, which allows you to get the selectors for a particular element.

### Step 3. Take periodic screenshots
To make sure that the video is really playing, we’ll need to take a screenshot a few seconds after the initial screenshot in order to visually confirm that the video has progressed. Even better, we can get Element to take screenshots at regular intervals. So let’s add a third step:

```js
step('03_Play', async browser => {
        //Take a screenshot every 5 seconds until video finishes
‍
        for (i = 0; i <= 60; i++) {
            await browser.takeScreenshot()
            await browser.wait(5)
        }
    })
```

To use `i`, we'll also need to declare it earlier in the script:

```js
import { step, TestSettings, By, Until } from '@flood/element'
‍
var i = 0
```

In this step, `i` will correspond to every 5 seconds of playtime for the video, so we'll need to make sure that the limit of `i` that we set is sufficient time for the entire video to play. Every 5 seconds, Element will take a screenshot, which will help us verify that the video is progressing after the test.

Click [here](https://github.com/flood-io/element/blob/master/examples/youtube.ts) to download the script before moving on to the next step, unless you’ve been following along at home.

### Step 4. Run it on Flood!
The final step is to upload it to Flood and run the test. Click [here](https://guides.flood.io/scripting-and-tools/flood-element/getting-started-with-element) to see a step-by-step guide for how to do just that. You can choose how many users you’d like to run on Flood and across how many nodes. New users will be given 5 node hours which will allow them to run a test with up to 250 users for 1 hour.  Each node will have a different IP address, so plan for that accordingly if your application takes that into account.

One of the things I love about running it this way is that if you click on the arrow to the right of the sole transaction, you can see screenshots taken along the way to prove that the video is being played:

![Screenshots during test execution in Flood](/assets/20181108-02.jpg)

## Some Considerations for Load Testing Video with Flood Element
### Taking screenshots and using logs are necessary for debugging.

Because the page elements while a video is streaming are static, we’re not going to be able to use those as clues as to where we are in our scenario. To compensate, it’s a good idea to take screenshots and use console.log() to determine progress, especially while debugging. Be careful not to go overboard on these when actually running the load test though, as they will consume system resources.

### Videos may behave differently in headless mode.

While writing this tutorial, I realised that YouTube auto-plays videos when on non-headless mode (aka, when opening a video link manually on a browser or with the `--no-headless` flag in Element). When it’s executed in headless mode via Flood Element, it requires a click on the play button to begin. Again, use screenshots to aid you in spotting these differences.

## Conclusion
Element’s browser-level scripting capabilities allow it to simulate users that interact with pages just like human users would. Element and Flood are a powerhouse combo, providing the flexibility to test with thousands of users across the world within a few minutes.

Element seeks to reduce the gap between a scripted user and a real user -- and it’s so realistic that it’s hard to tell the difference.  We encourage you to take advantage of our free trial offer and run some real world load tests today!

_*We don’t advise or condone the use of Element to artificially inflate views on YouTube in any way which may violate its [Terms of Service](https://www.youtube.com/static?template=terms). The purpose of this article is to showcase Element and how realistically it recreates real users._