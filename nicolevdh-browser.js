import { chromium } from 'k6/experimental/browser';
import { check, sleep } from 'k6';
import { randomIntBetween } from "https://jslib.k6.io/k6-utils/1.4.0/index.js";

export const options = {
    thresholds: {
        webvital_cumulative_layout_shift: ['p(75)<0.1'],
        webvital_largest_content_paint: ['p(75)<2500'],
        checks: ['rate>0.97'],
    },
}

export default function () {
    browser();
}

export async function browser () {
    const browser = chromium.launch({ headless: true });
    const page = browser.newPage();

    await page.goto('https://nicolevanderhoeven.com');
    sleep(randomIntBetween(1, 3));

    check(page, {
        'Browser_01 Homepage accessed': p => p.locator("//a[text()='Last Video']").isVisible() === true,
    })

    // const speakingLink = page.locator("(//a[@href='/speaking'])[1]");
    // await speakingLink.click();
    await page.goto('https://nicolevanderhoeven.com/speaking');

    sleep(randomIntBetween(3, 5));

    check(page, {
        'Browser_02 Speaking page accessed': p => p.locator("//img[@src='/assets/expoqa-3.jpeg']").isVisible() === true,
    });

    page.close();
    browser.close();

}