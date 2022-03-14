import asyncio
from pyppeteer import launch

async def main():
    browser = await launch({'headless': True}, executablePath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    page = await browser.newPage()
    await page.goto('https://google.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())