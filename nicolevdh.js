import { main } from './nicolevdh-protocol.js';
import { frontend } from './nicolevdh-browser.js';

export const options = {
    thresholds: {
        http_req_failed: ['rate<0.05'],
        checks: ['rate>0.97'],
        // webvital_cumulative_layout_shift: ['p(75)<0.1'],
        // webvital_largest_content_paint: ['p(75)<2500'],
    },
    scenarios: {
        protocol: {
            executor: 'ramping-vus',
            exec: 'protocol',
            startVUs: 0,
            stages: [
                { duration: '1m', target: 10 },
                { duration: '10m', target: 10 },
                { duration: '1m', target: 0},
            ]
        },
        // frontend: {
        //     executor: 'ramping-vus',
        //     exec: 'frontend',
        //     startVUs: 0,
        //     stages: [
        //         { duration: '1m', target: 1 },
        //         { duration: '10m', target: 3 },
        //         { duration: '1m', target: 0}
        //     ]
        // }
    },
    ext: {
        loadimpact: {
          projectID: 3548222,
          name: "nicolevanderhoeven.com",
        }
    }
};

export function protocol () {
    main();
}

// export function frontend () {
//     frontend();
// }