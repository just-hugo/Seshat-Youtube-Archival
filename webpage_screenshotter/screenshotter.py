import asyncio
from pyppeteer import launch


async def main():
    # launch a new headless browser instance with a new page open
    browser = await launch(headless=True)

    # open a new page in a browser instance
    page = await browser.newPage()

    # load a webpage by URL in the new page
    await page.goto('https://stackoverflow.com/questions/51000899/better-way-to-take-screenshot-of-a-url-in-python')

    # take a screenshot of the page
    await page.screenshot({'path': 'screen.png', 'fullPage': True})

    # close the browser
    await browser.close()

# run an asynchronous loop to take a screenshot
asyncio.get_event_loop().run_until_complete(main())
