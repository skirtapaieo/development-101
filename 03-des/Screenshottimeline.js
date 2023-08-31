const puppeteer = require("puppeteer");

(async () => {
  const browser = await puppeteer.launch();
  const page = await browser.newPage();

  // Navigate and wait until network is idle
  await page.goto("https://spela.svenskaspel.se/casino/", {
    waitUntil: "networkidle2",
  });

  // Capture Performance Metrics
  const metrics = await page.metrics();
  console.log("Metrics:", metrics);

  // Capture Screenshot
  await page.screenshot({ path: "example.png" });

  await browser.close();
})();
