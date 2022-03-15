import os, requests, re
from cleantext import clean
from dotenv import load_dotenv

load_dotenv()
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
}
data = requests.get(f'https://api.twitter.com/2/users/1453616508035272705/tweets?max_results=100&expansions=attachments.media_keys&media.fields=preview_image_url,url', headers=headers) # https://tweeterid.com/

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
    'Media links:\n'
    f'{links}'
)

# list of raw text
text_info = eval(data.content)["data"]
text = []
for tweet in range(len(text_info)):
    if "text" in text_info[tweet]:
        text.append(text_info[tweet]["text"].encode('utf-16', 'surrogatepass').decode('utf-16'))

# remove spaces and emojis from raw text
new_text = []
for x in range(len(text)):
    temp = clean(text[x], no_emoji=True, lower=False) # no emojis
    new_text.append(temp.replace(" ", "")) # no spaces
print(
    '\n'
    'Edited raw tweets:\n'
    f'{new_text}\n'
)

# testing
example = "ill-listwinners@EvkozFootball@TauLeBi@Blitz_ethPleaseDMuswithyourDiscordnametoclaim"

def get_loop(n):
    my_list = []
    for i in range(len(example)):
        my_list.append(example[i:i+n])
    del my_list[-n+1:]
    return my_list

for i in range(7, 11):
    my_list = get_loop(i)
    print(my_list)