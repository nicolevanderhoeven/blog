import http from 'k6/http';
import { sleep, check, group } from 'k6';

export const options = {
    duration: '5m',
    vus: 5,
    thresholds: {
        'group_duration{groupName:Home}': ['p(95)<500'],
        'groupDuration{groupName:Notes}': ['p(95)<1000'],
        http_req_failed: ['rate<0.05'],
        checks: ['rate>0.99'],
    },
};

const domain = 'https://nicolevanderhoeven.com';
export default function () {
    Home();
    ThinkTime();
    Notes();
    ThinkTime();
}

export function Home () {

    group('Home', function () {
        let res = http.get(domain);
        check(res, {
        'Homepage text verification': (r) => r.body.includes("Maastricht")
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
    
    group("Notes", function () {
        let response = http.get("https://notes.nicolevanderhoeven.com/");
        response = http.get("https://publish.obsidian.md/app.js?0baafbfed92e71ff3ff7");
        response = http.get("https://publish.obsidian.md/app.css?0baafbfed92e71ff3ff7");
        response = http.get("https://publish.obsidian.md/lib/purify.min.js");
        response = http.get("https://publish.obsidian.md/public/fonts/450beda71fb8564202a0.woff2");
        response = http.get("https://publish-01.obsidian.md/options/186a0d1b800fa85e50d49cb464898e4c");
        response = http.get("https://publish-01.obsidian.md/cache/186a0d1b800fa85e50d49cb464898e4c");
        response = http.get("https://publish.obsidian.md/favicon.ico?0baafbfed92e71ff3ff7");
        response = http.get("https://publish-01.obsidian.md/access/186a0d1b800fa85e50d49cb464898e4c/obsidian.css");
        response = http.get("https://publish-01.obsidian.md/access/186a0d1b800fa85e50d49cb464898e4c/publish.css");
        response = http.get("https://publish.obsidian.md/lib/pixi.min.js");
        response = http.get("https://publish-01.obsidian.md/access/186a0d1b800fa85e50d49cb464898e4c/Fork%20My%20Brain.md");
        check(response, {
            'Notes page text verification': (r) => r.body.includes("my working notes")
        });
        response = http.get("https://publish.obsidian.md/public/fonts/b0b9c035692f884e8635.woff2");
        response = http.get("https://publish-01.obsidian.md/access/186a0d1b800fa85e50d49cb464898e4c/assets/profile-token.png");
        response = http.get("https://publish.obsidian.md/lib/prism.min.js");
        response = http.get("https://publish.obsidian.md/public/images/874d8b8e340f75575caa.svg");
        response = http.get("https://publish.obsidian.md/public/fonts/856e8f46fd911d2040c3.woff2");
        response = http.get("https://publish.obsidian.md/sim.js");
    });
}

export function ThinkTime() {
    sleep(Math.random() * 5);
}