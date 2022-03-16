import asyncio, time
from pyppeteer import launch

input_selector = '#app-mount > div.app-3xd6d0 > div > div > div > div > form > div > div.block-3uVSn4.marginTop40-Q4o1tS > div.marginBottom8-emkd0_ > div > input'
submit_selector = '#app-mount > div.app-3xd6d0 > div > div > div > div > form > div > div.block-3uVSn4.marginTop40-Q4o1tS > div:nth-child(3) > button > div'

async def main():
    browser = await launch({'headless': False}, executablePath="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    page = await browser.newPage()
    await page.goto('https://discord.gg/F4FjDku3')
    
    await page.waitForSelector(input_selector)
    await page.type(
        f'{input_selector}',
        'Eddy Guo'
        )
    await page.screenshot({'path': 'before.png'})

    await page.click(submit_selector)
    await page.waitForXPath('//*[@id="app-mount"]/div[2]/div/div/div/section/div')
    await page.screenshot({'path': 'after.png'})
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())