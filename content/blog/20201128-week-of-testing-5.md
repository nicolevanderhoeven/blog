---
title: "Week of Testing: Day 5 - The thing about learning in public"
date: 2020-11-28T20:03:04+01:00
draft: false
tags: ['performance', 'english', 'k6.io', 'video']
---

{{< youtube quoOYnweKw >}}

Yesterday I mentioned that I'd used the `constant-vus` executor to recreate the stepped load profile. Well, the thing about learning publicly is that it also means making mistakes publicly!

I was kindly informed by a few of my new colleagues that `constant-vus` was not the most optimal way to recreate the stepped load profile. [Simme](https://simme.dev) wrote up a little function so I wouldn't have to repeat myself so much, and [Pepe Cano](https://twitter.com/ppcano_) and Pawel Suwala (the CTO of k6 himself) both told me nicely that using [stages](https://k6.io/docs/getting-started/running-k6#stages-ramping-up-down-vus) would have been the better solution.

So, let's chalk that up to a TIL (Today I Learned) and record that snippet here for prosperity (found in the k6 documentation linked above):

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '30s', target: 20 },
    { duration: '1m30s', target: 10 },
    { duration: '20s', target: 0 },
  ],
};

export default function () {
  let res = http.get('https://httpbin.org/');
  check(res, { 'status was 200': (r) => r.status == 200 });
  sleep(1);
}
```
