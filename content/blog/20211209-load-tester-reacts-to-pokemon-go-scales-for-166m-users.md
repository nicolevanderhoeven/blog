---
title: "Load Tester Reacts to Pokemon Go Scales for 166m Users"
date: 2021-12-09T16:13:59+01:00
draft: false
tags: ['performance', 'english', 'video', 'pokemon']
---

{{< youtube MtsEFebioWI >}}

## Transcript


NICOLE: Last year, Pokemon GO, a mobile app developed by Niantic Labs, made $1.23 billion in revenue with 166 million players from all over the world. This level of success is unprecedented, especially for an app that was encouraging people to go outside at a time when many governments were encouraging them to stay inside. In tech, though, success comes at a cost. Here's what Niantic has to do under the hood to keep this massively popular game running.

Hey everyone, I'm Nicole van der Hoeven. I've been helping companies
through their load testing for over 10 years, and I like to talk about tech travel and taking notes. I'm also a Pokemon GO player. I've been playing it since
the day it was released in July 2016.

In this video, I'm going to be reacting to a conversation between Priyanka Vergadia from Google and James Prompanya from Niantic Labs. Thank you to Joe Colantonio's TestGuild News Show last month, for bringing it to my attention.

Let's get started.


PRIYANKA: Yep.
NICOLE: Okay. Everybody knows that you should be doing a curve ball to catch Pokemon the fastest way.

PRIYANKA: I am catching some Pokemons. Did you know that it was
built on Google Cloud? Well, let's talk--

NICOLE: GCP, okay.

PRIYANKA: At Niantic Labs to take a behind the scenes look at Pokemon Go's architecture, and how it scales for large number of players. Hi James, welcome to the show.

JAMES: Pokemon Go is not your typical mobile game.

NICOLE: I love that he's got Pokemon paraphernalia everywhere.

JAMES: Catching these little creatures around you called Pokemon that are
appearing in a real world. Encourage you to go outside, explore and discover things using augmented reality. A big part of that, which wasn't in--

NICOLE: See this is one of the things that make me really impressed with their implementation. They have majority of their users using mobile networks. That's a really hard thing to account for, especially when you're talking about a global audience that is playing in different parts of the world. So it's really important that everything is front-loaded, and that they're minimizing the amount of traffic, the amount of resources that each player has to download on their mobile network.

JAMES: Wasn't included in the game when it first came out, was this big community aspect of it. We really liked this part of the game. So we made it a major part by hosting regular live events, such as Community Days, Raid Hours,Team GO Rocket Takeovers, all culminates in this big summer event that we call GO Fest.

PRIYANKA: So it's--

NICOLE: So this is a really brave move as well because they have events that are timed. So they happen at the same time for people in that time zone. And earlier on in Pokemon Go's history, I did experience some slowness and some congestion in the mobile networks. But I mean, that's a really difficult thing for them to plan for. I'm interested to see how they solve that.

PRIYANKA: How does Pokemon Go back and actually scale to handle these peaks in traffic?

JAMES: So we use Google Cloud. (chuckles) We have lots of services that need scaling such as the Google Kubernetes Engine and Spanner. Our front-end service is hosted on GKE, and it's pretty easy to scale the nodes there. Google Cloud provides us with all the tools we need to manage the Kubernetes cluster.

NICOLE: So it's really cool to hear him talking about their stacks. So they're using GCP, Google Cloud Platform. They're on Kubernetes, so they're using GKE, the Google Kubernetes Engine. And they use Google Cloud Spanner, which is a very highly available relational database.

JAMES: To give an idea of scale, we have about 5,000 spanner nodes handling the traffic and thousands of Kubernetes nodes running just for the Pokemon--

NICOLE: That is so interesting. 5,000 Spanner nodes. That's just for the data. That makes sense because Niantic's main reason for creating this game, or the way that they're making money, I guess, is by getting the data from users about walking paths and ...Basically, geo location or spatial data. So it's super important for them to be able to store the data that they're getting from their application usage.

JAMES: We also have the various microservices that host other parts of the--

NICOLE: So another thing that they're doing to keep it scalable is
by using microservices. See the traditional way is to use a monolith, so one large application with many sub-components. The problem with that though, is you can't independently scale those components, you'd have to scale the entire application. And when that application is already really big and complex, that's really inefficient because you're scaling everything, even services that you
may not need to scale. So it's really smart that they've chosen for a microservices based architecture, so that each of those components can be scaled separately of each other.

JAMES: And if you compare ourselves to maybe World of Warcraft, you'll see that other massively multiplayer online games, they split players into multiple realms, but for us, all of our players, they reside on a single realm. It was important for us that players can always interact with each other and share the same game, the experience, no matter where or when they're playing.

PRIYANKA: Yeah--

NICOLE: Okay. So I happen to have also played WoW, World of Warcraft. My main 'toon was a disciplined priest. So when you sign up to WoW, you have to choose a realm, that's basically a server or group of servers so that they don't have to shoulder the entire load from all users. So that was WoW's way to reduce the load. And he's making the point that Pokemon Go can't really do that to a certain extent. It's not entirely correct to say that they don't have
that sort of splintering, because they do still splinter based on the time zone. You're only seeing people in that location in your time zone. 

Even events, they sometimes say 10:00 AM in your local time. So you're not necessarily playing at the same time that people in Australia are playing. So there is some splintering, but it is less than what there would be for a game like WoW.

JAMES: When we're looking at different providers, we saw that Spanner
has consistent indexing that allows us to do more complex database schemas with these primary and secondary keys. Data Store was also non-relational with atomic and durable transactions. So we needed a relational database with full consistency, and made the choice to go to Spanner, which gave us these global ACID transactions.

NICOLE: So he's talking about consistency, global consistency, being a big deal and a big factor for why they chose to go and use Google Cloud Spanner instead of Google Data Store. And the reason is that normally, when you have a bunch of different instances of database, it doesn't matter so much that those requests are processed in exactly the order that they came in. Because usually those
requests are being made by different people, and they're trying to change different accounts. But with Pokemon Go, there's the added complexity of wanting to keep the integrity of the chronological order. So if I go and attack a gym before you do, my, the process, the request that I created by attacking the gym, should be processed before yours is because it matters who gets to the gym first. So that's an interesting twist.

PRIYANKA: Now let's say I'm a player and I'm playing the game right now. I open my app to catch a Pokemon. What is happening behind the scenes? How does the request flow work?

JAMES: When the user catches a Pokemon, we receive that request through the Google Cloud Load Balancer. All of the static media is also stored on Google Cloud storage buckets. And it's downloaded to the phone when you first start the app. We also have caching enabled at the load balancers. So it's--

NICOLE: Already, they've mentioned they have a load balancer, so that that's like a traffic controller that's sitting above the servers and saying, "Okay, this request goes to this server." And then maybe when that server is processing too many requests, that load balancer should be able to say, "All right, now let's
divert some of the traffic to another server that maybe isn't as heavily utilized." 

He also mentioned that they employ caching. This is what I was saying earlier that because you want to minimize the amount of traffic and the bytes that are flowing on the network, you want to employ caching for maybe things that
aren't going to change so more static assets. Maybe you might want to change the Pokemon that's in a gym, but the location of that gym is something that should and can be cached. He's right now talking about caching on the server side, on
the application side, and not on the mobile phone. But I wonder if they're going to talk about that later as well.

JAMES: It's all cached and served through Google Cloud CDN. So when the Poke--

NICOLE: So he also mentions using a CDN, so a Content Delivery Network, which is really good because that means that if I'm in the Netherlands and I make a request to their servers, my request isn't then going to be sent to a server in the US, because it's going to be sent to one of the servers in my country or nearby. That means that the latency between my request being sent, and that request getting to the server, and retrieving that resource and back, is going to be a lot lower. So it's ... This is a way to improve performance.

JAMES: The player catches the Pokemon, the GCLB sends the request to our GKE cluster. And we have a front-end service that sits behind Nginx reverse proxy. The request goes from the user's phone through the reverse proxy, to one of these player, front-end services. We also have this thing called a Spatial Query Backend. It's a cache by location.

So that is where we store the information that determines where a Pokemon is shown on the map, what gyms and Poke stops are around you, what time zone you're in, or any other feature that is location-based.

PRIYANKA: Now, what happens when I hunt a Pokemon down and catch it?

JAMES: When you catch a Pokemon, it sends the request to the front end, to the Spanner database, where your player entity is stored and it store it there. For catching Pokemon, that actually doesn't go to the Spatial Query Backend. If you were, instead, if you were battling in a gym or adding lures to the Poke stop, that information is stored on the Spatial Query Backend, and--

NICOLE: Okay. So it sounds like the Spatial Query Backend is only storing data about the world, the Pokemon Go world that everybody can see. So people don't need to know whether another person has caught a particular Pokemon. They just need to know whether there's a lure on a Poke stop, or whether the gym is Team Mystic and things like that that everybody else can see. So there's this segmentation of some data that is specific to the user, and other data that all users need to see.

JAMES: We also use Pub/Sub to send the message to a Pub/Sub topic, which is then used for analytics pipeline.

NICOLE: He talks about a Pub/Sub model, which means that their architecture is event driven. So the traditional way that this is handled is by polling. So normally when an service is waiting for something to happen, it goes, and it sends a message and it checks. Basically like, "Hey, are we there yet? Are we there yet? Are we there yet?"

And then when it finally gets a response that "Yes, we are," then it can do something with that data. Instead what they're doing as a Pub/Sub. So instead it waits for events. There is no constant polling, again, reducing the amount of traffic that's going back and forth. And it just specifies criteria for what it is actually waiting for. And when that happens, after the services that require that event are subscribed, then that event is published to all of them. And then they can then do whatever they want with that event.

PRIYANKA: So, how do you ensure that when two people who are in the same geographic regions, see the same Pokemon data, and keep that relatively in sync, especially during the events?

JAMES: So it's actually pretty interesting. Everything in our servers are deterministic. So even if players are on different machines, they're sensitive to
different front-end services, if they're in the same physical location, all the inputs would be the same and the same Pokemon would get returned to both users. There's a lot of caching involved and as well as precise timing, especially when the settings are changed and they need to be in sync across all the servers.

So it's very tricky, but it was very important for us that all the players feel like they're part of this one shared world.

NICOLE: I'm not entirely sure what he means when he says that it's deterministic.I'm going to guess, and I have no relationship with Google or with Niantic, but I'm thinking that what he means is that when you're catching a Pokemon, there is no request that's being sent to the servers to say, "Hey, did I catch this?" Instead, there's probably some sort of algorithm. This Psyduck is caught 80% of the time and appears 2% of the time. So 2% of the Pokemons that you're gonna see appear in this area, are going to be Psyducks. And that's also reducing the load going back and forth, right? Because it's just the equation or the algorithm that determines whether you catch a Pokemon or not.

JAMES: This game data is of interest to our data science team. They use this for marketing purposes, for verifications. For example, we might want to say that this player, or players caught x millions amount of Pokemon during our Saturday Community Day events. So, it's important that we have that information in an easily accessible manner.

NICOLE: So there's a lot of data here that they track. So I've got my distance walked, Pokemon caught, I'm at 18,878. Poke stops visited, total XP, start date. And then there are these medals as well. So, they look at things like, how far have you walked in total? So all of these things are data points that they store for every single user. No wonder they have such a focus on databases, right?

PRIYANKA: As the events grow, like you mentioned, in some of these events, the traffic grows to millions of users per second. You also said--

NICOLE: Per second!

PRIYANKA: ...of data is generated. How does the system scale when it comes to data pipeline?

JAMES: Yeah. So when there's increase of transactions, there is increase of load
throughout the system with a lot of our data pipelines for things like BigQuery, one of that--

NICOLE: I'm not actually sure she was saying millions of users per second, but that's a little bit ambiguous. Maybe she meant millions of requests per second. And the way that they're trying to do that is they're reducing the size of those requests. If she means there are millions of concurrent users at any given time, that doesn't necessarily mean that those users are all doing something at the exact same time. So I would have wanted to see exactly how many requests, to hear
how many requests per second they're needing to deal with, or how many bytes per second are being sent over the wire. That would've been cool.

JAMES: ...Just works. Google Cloud will handle the increase in traffic without any intervention.

PRIYANKA: With that much traffic, obviously health of the system is critical as well. How do you monitor the health of the system during these massive events?

JAMES: So we use multiple monitoring systems, including Prometheus, Grafana, and Google Cloud monitoring. On a personal level, I actually prefer it to Google Cloud monitoring because it's very simple to use--

NICOLE: Whoo whoo! And they're using Prometheus and Grafana ... Oh, this is entirely unexpected, but I'm actually wearing a Grafana shirt. So it's really cool that they're using Prometheus and it really, it makes sense, because they're on a Kubernetes cluster and Prometheus and Kubernetes just go really well together. By the way, I work for Grafana, for context.

PRIYANKA: What are some of the expansions and improvements you're looking to do in the future?

JAMES: On the Google Cloud side of things, we are looking into things such as Agones and Google Game servers, and using that to see how we can make our game even better.

PRIYANKA: We wish you and the Niantic team best of luck for these enhancements. And this has obviously been super insightful for us, James. Thanks for joining me today and sharing your architecture with us.

JAMES: Yeah, thanks for having me. This was fun.

NICOLE: That was really good. So there were a few things that were mentioned there for how they're scaling Pokemon Go, that I wrote down here.

One, they use an event driven architecture and also a microservices based architecture, both of which are way more performant than the traditional methods.And the microservices based architecture will also let them scale up independently as demand increases as well. And they're also using Cloud Spanner instead of Google Data Store, prioritizing global consistency, as well as high availability. 

They front-load a lot of the static assets that are used by the application. And they're being downloaded when the app is initially downloaded or installed onto users' mobile phones. That way they don't have to keep serving the same data if it's going to be used consistently. And when something changes, like a different lot of Pokemon, they release these patches that let you download a lot of those images so that when you catch those Pokemons, then you already have all that information on your phone. And on a related note, they're employing a lot of caching. They talked about caching on the mobile app side, and on their server side.

Events are also staggered. So splintered realms sort of, because they're happening
on different time zones, depending on where you live. And not completely simultaneously, regardless of the time in the part of the world where you're from.

They're also using things like Prometheus, Grafana and Google Cloud Monitoring. They didn't mention how they're actually using multi-tenant versions of Prometheus like, maybe, I don't know if they're using Cortex or something like that, but that's something that they should look into.

And they also mentioned potentially increasing the number of Google Game Servers.

I really appreciated that behind the scenes look. I wish more companies would do this, especially for apps that I personally love and use. One thing that I'm really curious about though, is the testing side of it. Because testing an application of this scale and complexity, is another thing entirely from observability. And I would have wanted to know how they're doing their performance and load testing. And whether they're doing things like chaos engineering maybe, or reliability testing to improve the availability and reliability of their application.

If you're still watching this, then chances are high that you like Pokemon and load testing as much as I do, which is a bit of an odd combination. And in that case, check out this video, on how I run chaos experiments using k6, Prometheus and Grafana. Thank you for joining me as I watched this awesome video.

And as they say in the Netherlands, (Dutch) Until next time! Bye!