import asyncio, time
from pyppeteer import launch

async def main():
    browser = await launch({'headless': False}, executablePath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    page = await browser.newPage()
    await page.goto('https://google.com')

    content = "pypetteer"
    await page.evaluate(f"""() => {{
        document.getElementsByName('q')[0].value = '{content}';
    }}""")

    # time.sleep(30)
    await page.screenshot({'path': 'screenshot.png'})
    await browser.close()
asyncio.get_event_loop().run_until_complete(main())