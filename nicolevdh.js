import http from 'k6/http';
import { sleep, check, group } from 'k6';

// export const options = {
//     duration: '5m',
//     vus: 5,
//     thresholds: {
//         http_req_duration: ['p(95)<500'],
//         http_req_failed: ['rate<0.05'],
//         checks: ['rate>0.99'],
//     },
// };

const domain = 'https://nicolevanderhoeven.com';
export default function () {
    Home();
    ThinkTime();
    Notes();
    ThinkTime();
}

export function Home () {

    group('Go to home page', function () {
        let res = http.get(domain);
        check(res, {
        'Homepage text verification': (r) => r.body.includes("Developer Advocate at k6.io")
        });

        http.get(domain + '/lib/font-awesome/css/all.min.css');
        http.get(domain + '/lib/jquery/jquery.min.js');
        http.get(domain + '/js/main.js');
        http.get(domain + '/css/style-white.css');
        http.get(domain + '/images/logo.png');
        http.get(domain + '/lib/JetBrainsMono/ttf/JetBrainsMono-Regular.ttf');
        http.get(domain + '/lib/font-awesome/webfonts/fa-brands-400.woff2');
        http.get(domain + '/images/favicon.ico');
    });
}

export function Notes () {
    let res = http.get("https://notes.nicolevanderhoeven.com");
    check(res, {
        'Notes page text verification': (r) => r.body.includes("my working notes")
    });
}

export function ThinkTime() {
    sleep(Math.random() * 5);
}