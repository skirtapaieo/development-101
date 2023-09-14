# Performance - time line of screenshots in Google Dev Tools

You can capture a timeline of screenshots along with performance metrics like First Paint and Largest Contentful Paint in Chrome DevTools. While there isn't a built-in way to export the screenshots directly from DevTools, you have a couple of options to work with:

## Feature in Chrome Dev Tools

No.

## Programmatic Capture (Puppeteer)

Puppeteer, a Node library, provides a high-level API over the Chrome DevTools Protocol, to capture performance metrics and screenshots programmatically.

Here is a simple example code snippet:

```javascript
const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Navigate and wait until network is idle
  await page.goto("https://example.com", { waitUntil: "networkidle2" });

  // Capture Performance Metrics
  const metrics = await page.metrics();
  console.log("Metrics:", metrics);

  // Capture Screenshot
  await page.screenshot({ path: "example.png" });

  await browser.close();
})();
```

You can capture metrics related to First Paint, Largest Contentful Paint etc., and take screenshots at different stages of page load or interactions. You'll need to dig into the Chrome DevTools Protocol for more detailed metric capturing.

### Third-Party Tools

Some third-party tools allow for more advanced performance testing, capturing screenshots, and other metrics. Examples include sites like WebPageTest.
