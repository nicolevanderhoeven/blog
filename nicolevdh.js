import http from 'k6/http';
import { sleep, check } from 'k6';

export const options = {
    duration: '5m',
    vus: 5,
    thresholds: {
        http_req_duration: ['p(95)<500'],
    },
};

export default function () {
    let res = http.get('https://nicolevanderhoeven.com', {tags: { name: '01_Home' }});
    check(res, {
      'is status 200': (r) => r.status === 200,
      'text verification': (r) => r.body.includes("Developer Advocate at k6.io")
    });
    sleep(Math.random() * 5);
}
