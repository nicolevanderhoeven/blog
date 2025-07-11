import http from 'k6/http';
import { sleep, check, group } from 'k6';

// export const options = {
//     duration: '5m',
//     vus: 5,
//     thresholds: {
//         http_req_failed: ['rate<0.05'],
//         checks: ['rate>0.97'],
//     },
//     ext: {
//         loadimpact: {
//           projectID: 3548222,
//           name: "nicolevanderhoeven.com",
//         }
//     }
// };

export default function () {
    main();
}

const domain = 'https://nicolevanderhoeven.com';
export function main () {
    Home();
    ThinkTime();
    Notes();
    ThinkTime();
}

export function Home () {

    group('Home', function () {
        
        let res = http.batch([
            ['GET', domain],
            // ['GET', 'https://nicolevanderhoeven.github.io/css/style-dark.css'],
            // ['GET', domain + '/lib/font-awesome/css/all.min.css'],
            // ['GET', domain + '/lib/jquery/jquery.min.js'],
            // ['GET', domain + '/js/main.js'],
            // ['GET', 'https://nicolevanderhoeven.github.io/images/logo.png'],
            // ['GET', domain + '/lib/JetBrainsMono/ttf/JetBrainsMono-Regular.ttf'],
            // ['GET', domain + '/lib/font-awesome/webfonts/fa-brands-400.woff2'],
            // ['GET', domain + '/lib/font-awesome/webfonts/fa-solid-900.woff2'],
            // ['GET', 'https://nicolevanderhoeven.github.io/images/favicon.ico']
        ]);
        check(res, {
            'Protocol_01 Homepage text verification': (r) => JSON.stringify(r).includes('Portugal')
        });
    });
}

export function Notes () {
    
    group("Notes", function () {
        let res = http.batch([
            ['GET', 'https://notes.nicolevanderhoeven.com/'],
            // ['GET', 'https://publish.obsidian.md/app.js?0baafbfed92e71ff3ff7'],
            // ['GET', 'https://publish.obsidian.md/app.css?0baafbfed92e71ff3ff7'],
            // ['GET', 'https://publish.obsidian.md/lib/purify.min.js'],
            // ['GET', 'https://publish-01.obsidian.md/options/186a0d1b800fa85e50d49cb464898e4c'],
            // ['GET', 'https://publish-01.obsidian.md/cache/186a0d1b800fa85e50d49cb464898e4c'],
            // ['GET', 'https://publish.obsidian.md/favicon.ico?0baafbfed92e71ff3ff7'],
            // ['GET', 'https://publish-01.obsidian.md/access/186a0d1b800fa85e50d49cb464898e4c/obsidian.css'],
            // ['GET', 'https://publish-01.obsidian.md/access/186a0d1b800fa85e50d49cb464898e4c/publish.css'],
            // ['GET', 'https://publish.obsidian.md/lib/pixi.min.js'],
            // ['GET', 'https://publish-01.obsidian.md/access/186a0d1b800fa85e50d49cb464898e4c/Fork%20My%20Brain.md'],
            // ['GET', 'https://publish-01.obsidian.md/access/186a0d1b800fa85e50d49cb464898e4c/assets/profile-token.png'],
            // ['GET', 'https://publish.obsidian.md/lib/prism.min.js'],
            // ['GET', 'https://publish.obsidian.md/public/images/874d8b8e340f75575caa.svg'],
            // ['GET', 'https://publish.obsidian.md/sim.js'],
        ]);
        check(res, {
            'Protocol_02 Notes page text verification': (r) => JSON.stringify(r).includes('Fork My Brain - Fork My Brain')
        });
    });
}

export function ThinkTime() {
    sleep(Math.random() * 5);
}