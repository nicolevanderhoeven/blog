import http from 'k6/http';
import { sleep, check, group } from 'k6';

export const options = {
    duration: '5m',
    vus: 5,
    thresholds: {
        http_req_duration: ['p(95)<500'],
    },
};

const domain = 'https://nicolevanderhoeven.com';
export default function () {
    Home();
}

export function Home () {

    group('Go to home page', function () {
        let res = http.get(domain);
        check(res, {
        'is status 200': (r) => r.status === 200,
        'text verification': (r) => r.body.includes("Developer Advocate at k6.io")
        });

        res = http.get(domain + '/lib/font-awesome/css/all.min.css');
        check(res, {
        'is status 200': (r) => r.status === 200
        });

        res = http.get(domain + '/lib/jquery/jquery.min.js');
        check(res, {
        'is status 200': (r) => r.status === 200
        });

        res = http.get(domain + '/js/main.js');
        check(res, {
        'is status 200': (r) => r.status === 200
        });

        res = http.get(domain + '/css/style-white.css');
        check(res, {
        'is status 200': (r) => r.status === 200
        });

        res = http.get(domain + '/images/logo.png');
        check(res, {
        'is status 200': (r) => r.status === 200
        });
        
        res = http.get(domain + '/lib/JetBrainsMono/ttf/JetBrainsMono-Regular.ttf');
        check(res, {
        'is status 200': (r) => r.status === 200
        });

        res = http.get(domain + '/lib/font-awesome/webfonts/fa-brands-400.woff2');
        check(res, {
        'is status 200': (r) => r.status === 200
        });

        res = http.get(domain + '/images/favicon.ico');
        check(res, {
        'is status 200': (r) => r.status === 200
        });
    })
    

    sleep(Math.random() * 5);
}