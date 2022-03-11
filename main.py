import os, requests
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
}
data = requests.get(f'https://api.twitter.com/2/users/1453616508035272705/tweets?max_results=5&expansions=attachments.media_keys&media.fields=preview_image_url,url', headers=headers) # https://tweeterid.com/

# list of tweet media links
media_info = eval(data.content)["includes"]["media"]
links = []
for tweet in range(len(media_info)):
    if "url" in media_info[tweet]:
        links.append(media_info[tweet]["url"])
    elif "preview_image_url" in media_info[tweet]: # add more elif's if media link 
        links.append(media_info[tweet]["preview_image_url"])
print()
print(links)

# list of tweet text
text_info = eval(data.content)["data"]
text = []
for tweet in range(len(text_info)):
    if "text" in text_info[tweet]:
        text.append(text_info[tweet]["text"])
print()
print(text)