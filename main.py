import os, requests, re
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
print(
    '\n'
    'Media links: \n'
    f'{links}'
)

# list of raw text
text_info = eval(data.content)["data"]
text = []
for tweet in range(len(text_info)):
    if "text" in text_info[tweet]:
        text.append(text_info[tweet]["text"].encode('utf-16', 'surrogatepass').decode('utf-16'))
print('-' * 200)
print(
    "Raw tweets: "
    f'{text}'
)

# remove spaces, newlines, and emojis from raw text
new_text = []
emoji_patterns = re.compile("["
                    u"\U0001F600-\U0001F64F"
                    u"\U0001F300-\U0001F5FF"
                    u"\U0001F680-\U0001F6FF"
                    u"\U0001F1E0-\U0001F1FF"
                    u"\U00002500-\U00002BEF"  
                    u"\U00002702-\U000027B0"
                    u"\U00002702-\U000027B0"
                    u"\U000024C2-\U0001F251"
                    u"\U0001f926-\U0001f937"
                    u"\U00010000-\U0010ffff"
                    u"\u2640-\u2642"
                    u"\u2600-\u2B55"
                    u"\u200d"
                    u"\u23cf"
                    u"\u23e9"
                    u"\u231a"
                    u"\ufe0f"
                    u"\u3030"
                    "]+", flags=re.UNICODE)

for x in range(len(text)):
    temp = emoji_patterns.sub(r'', text[x])
    new_text.append(temp.replace(" ", ""))
    
print('-' * 200)
print(
    "Edited raw tweets: "
    f'{new_text}'
)

# tweets with proper encoding (display purposes)
print("-" * 200)
print("Encoded tweets:")
for x in range(len(text)):
    print(text[x].encode('utf-16', 'surrogatepass').decode('utf-16'))
    print("-" * 200)