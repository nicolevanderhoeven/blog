---
title: "Tips and Tricks for Using Flood Element"
date: 2018-11-23T23:07:24+01:00
draft: false
tags: ['english', 'text', 'flood.io', 'element']
---

{{< rawhtml >}}
<link rel="canonical" href="https://www.flood.io/blog/tips-and-tricks-for-using-flood-element">
{{< /rawhtml >}}

_Originally posted [here](https://www.flood.io/blog/tips-and-tricks-for-using-flood-element)._

In case you missed it, there’s a new performance test tool on the block, and it’s called [Flood Element](https://element.flood.io/). It’s a scalable browser-based tool that allows you to write scripts in javascript that interact with web pages like a real user.

Using Browser Level Users is a [newer approach to load testing](https://flood.io/blog/why-you-should-load-test-with-browsers/) that overcomes a lot of the common challenges we hear about traditional methods of testing:

1. Easier scripting that is akin to common functional tools like Selenium and easier to learn
2. More realistic results that are based on true browser performance rather than API responses
3. Ability to test against all components of your web app, including things like Javascript that is rendered via the browser

Given the above benefits, it’s a no brainer to check out Flood Element for your web load testing, especially if you have struggled with the existing tools on the market like JMeter or HP LoadRunner.

Pairing Element with [Flood](https://flood.io/) turns it into a pretty powerful load test tool. We have a [great guide here](https://help.flood.io/getting-started-with-load-testing/step-by-step-guide-flood-element) that you can follow if you’d like to get started with it. As you can imagine, I’ve been using and testing Element for several months now and I thought I’d share some tips I’ve learned along the way.

## Initialising your script
You can always start from scratch, but the quickest way to get started is to type

`element init myfirstelementtest`

from your terminal, filling in the project name you’d prefer.

You’ll then be asked to type in the title of your test as well as the URL you’d like to script against. After a minute, you’ll see that a new directory has been created:

![New directory in Flood Element](/assets/20181123-01.png)

Element will automatically create a file called `test.ts`. This file will contain the skeleton of a script, along with some sample code to help you find a button and then click on it. But before you open it, let’s move on to…

## Choosing the right text editor
Scripting in Element is already pretty simple, but I’ve found two things that really help while scripting are syntax highlighting and code completion. Syntax highlighting will greatly improve your experience when first learning a new test tool like Element, and code completion will make your scripting lightning fast as you become more experienced in the process.  My text editor of choice is [Visual Studio Code](https://code.visualstudio.com/), which has both of those features. It’s slick and clean, and it does the job.

Syntax highlighting is when the text editor intelligently changes the font colour of your code according to its role in the programming language you’re using. Here’s a screenshot of the test.ts file we generated earlier in VS Code to show you what I mean:

![Generated sample Flood Element script](/assets/20181123-02.png)

This makes it easier to make sense of the code at a glance: comments are in green, values and labels are in orange, etc.

Code completion is when you start to type something, and VS Code helpfully opens a context menu with suggestions for methods you can use.

![Auto-completion in VSCode](/assets/20181123-03.gif)

I love this because it means I don’t have to remember the exact name of the method. It also suggests names of variables you’ve already defined and highlights code that doesn’t make sense.  This will help to make your tests more maintainable and readable for others, which is a great benefit as you look to scale your testing out in the future.

![Suggestions in VSCode](/assets/20181123-04.gif)

## Taking screenshots
One of the most powerful features of Element is its ability to take screenshots. I find it immensely useful when debugging because sometimes it’s just easier to see what’s going on visually.  With protocol based tools, debugging can often be a much more involved and technical process.

There are two ways to take screenshots in Element:

1. Add a setting to automatically take a screenshot when an error is encountered. You can do this by setting screenshotOnFailure to true in TestSettings:

```js
export const settings: TestSettings = {
device: Device.iPadLandscape,
userAgent: 'flood-chrome-test',
clearCache: true,
disableCache: true,
screenshotOnFailure: true,
}
```

2. Explicitly take a screenshot at a particular point in the script. You can do this by adding

```js
await browser.takeScreenshot()
```

to your code.

## Viewing Screenshots
Once you’ve taken screenshots within your tests, you will likely want to view them and know that they will be stored for future safekeeping.  Whether you are running your test locally on have uploaded it to Flood to run with increased concurrency, Flood Element has you covered.

### Locally Run Tests
Screenshots will be saved as jpg files in a timestamped folder corresponding to your run. It should look something like: `...myfirstelementtest/tmp/element-results/test/2018-11-20T135700.595Z/flood/screenshots/` and the screenshots will be uniquely named so that new screenshots, even for the same step, don’t overwrite older ones.

However, I rarely have to look up the screenshots in that folder because I prefer to see them in iTerm2 for macOS. iTerm is an alternative to the terminal that works particularly well with Element. When you take a screenshot, iTerm actually shows it in-line:

![Screenshots shown inline with iTerm](/assets/20181123-05.png)
‍
### Tests Run in Flood
Running an Element script on Flood is ideal when you need larger concurrency. Rather than accessing your screenshot locally, Flood will centralize the images into your account so the images remain even after the cloud load injectors are destroyed.  You can get to the screenshot files by downloading Archived Results:

![Archived Results in Flood](/assets/20181123-06.png)

Or you can also choose to click on a step on the dashboard to see a film strip of your test:

![Seeing screenshots during a test with Flood](/assets/20181123-07.png)

## Using Logs
You may need to check out the logs for more technical debugging, especially when the screenshots don’t tell the whole story.  Whether you are running your test locally on have uploaded it to Flood to run with increased concurrency, Flood Element has you covered.

### Locally Run Tests
You can print to the console by typing, for example:

`console.log('orderValues = ' + orderValues)`

This will print the value of the variable orderValues at that point in the script. You would see this in your terminal if you’re running Element locally.

### Tests Run in Flood
If you’re running the script on Flood, you can either download the log (in the same Archived Results zipped file as mentioned earlier) or you can click on the Logs tab:

![Test logs on Flood](/assets/20181123-08.png)
‍
## Fun with Flags
Element comes with a few flags that give you more control over how the script is run locally. Here are a few of my favourites!

### Headless Flag
When in doubt, run Element in non-headless mode to see the script actually opening the web app on Chrome and interacting with the page. This is only possible locally, but there’s nothing like actually seeing for yourself what’s happening in real time instead of relying on screenshots and logs after the fact. To enable this mode, add the flag when running your test:

`element run myfirstelementtest.ts --no-headless`

### Watch Flag
Element will automatically close the browser window when it encounters an error or finishes the iteration. Adding `--watch` will leave the browser window open and then will monitor the script. As soon as the script is saved, it will automatically run it in the same window from the beginning.  Simply add this flag like the above example:

`element run myfirstelement.ts --watch`

### Dev Tools Flag
This opens a browser instance and runs the script with the Chrome Dev Tools open, allowing you to find locators for the next action you want to script.  Simply add this flag like the first example:

`--dev-tools`

### More Flags
For more flags, use:

`element run --help`

## Try Element
You’ve just gotten a crash course on Flood Element. You’re all set! If you haven’t already, download Element [here](https://element.flood.io/) to start writing functional test scripts and reusing them as load test scripts on Flood. If you don’t have a Flood account, you can easily sign up for a free trial here.  

We’re extremely proud to have been able to contribute to the open-source community and can’t wait to have you try this new addition to the Flood line!