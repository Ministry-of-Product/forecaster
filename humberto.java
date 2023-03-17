(async () => {
  const browser = await puppeteer.launch(chromeOptions);
    try {
      const page = await browser.newPage();
      page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 2});
      await page.goto('https://www.google.com/maps/',
       {waitUntil: 'networkidle2'});
       await page.screenshot({
        path: "screenshot_" + Math.floor(new Date().getTime() / 1000) + ".png",
        clip: { x:200, y: 350, width: 900, height: 575}
       });
    } catch (e) {
      console.log(e);
    } finally {
      await browser.close();
    }
 
})();
