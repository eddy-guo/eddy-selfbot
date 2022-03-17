import os, requests
from cleantext import clean
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
}
data = requests.get(f'https://api.twitter.com/2/users/1453616508035272705/tweets?max_results=5&expansions=attachments.media_keys&media.fields=preview_image_url,url', headers=headers) # https://tweeterid.com/

# list of tweet media links

def media():
    if "includes" not in eval(data.content):
        print("No media links from the tweets scraped.")
        return
    else:
        media_info = eval(data.content)["includes"]["media"]
        links = []
        for tweet in range(len(media_info)):
            if "url" in media_info[tweet]:
                links.append(media_info[tweet]["url"])
            elif "preview_image_url" in media_info[tweet]: # add more elif's if media link 
                links.append(media_info[tweet]["preview_image_url"])
        print(
            '\n'
            'Media links:\n'
            f'{links}\n'
        )
media()

# list of raw text
text_info = eval(data.content)["data"]
text = ""
for tweet in range(len(text_info)):
    if "text" in text_info[tweet]:
        text += clean(text_info[tweet]["text"].encode('utf-16', 'surrogatepass').decode('utf-16'), no_emoji=True, lower=False).replace(" ", "").replace('\n', '')

# iterate through text and add every n-letter code into a list
def get_loop(n):
    code_list = []
    for i in range(len(text)):
        code_list.append(text[i:i+n])
    del code_list[-n+1:]
    return code_list

# attach all 7, 8, 9, and 10-letter code lists into one list
final_list = []
for i in range(7, 11):
    code_list = get_loop(i)
    final_list += code_list
print(final_list)
print(len(final_list))