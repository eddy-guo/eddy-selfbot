import asyncio
from pyppeteer import launch
from main import text_list
from ocr import ocr_list

continue_selector = '#app-mount > div.app-3xd6d0 > div > div > div > section > div > button > div'
login_selector = '#app-mount > div.app-3xd6d0 > div > div > div > div > form > div > div > div.mainLoginContainer-wHmAjP > div.block-3uVSn4.marginTop20-2T8ZJx > button.marginBottom8-emkd0_.button-1cRKG6.button-f2h6uQ.lookFilled-yCfaCM.colorBrand-I6CyqQ.sizeLarge-3mScP9.fullWidth-fJIsjq.grow-2sR_-F > div'

async def main():
    browser = await launch({'headless': False,
                            'executablePath': 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
                            'args': [
                                       r'--user-data-dir=C:\Users\Eddy\AppData\Local\Google\Chrome\User Data', 
                                       '--profile-directory=Profile 6',
                                       ]
                            })
    page = await browser.newPage()
    await page.goto('https://discord.gg/F4FjDku3')
    
    await page.waitForSelector(continue_selector)
    await page.click(continue_selector)
    await page.waitForSelector(login_selector)
    await page.click(login_selector)

    await browser.close()

asyncio.get_event_loop().run_until_complete(main())

# will no longer run; alt account disabled for botting HAHA