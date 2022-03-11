import requests, os
from dotenv import load_dotenv

load_dotenv()

BEARER_TOKEN = os.getenv('BEARER_TOKEN')

headers = {
    'Authorization': f'Bearer {BEARER_TOKEN}',
}
data = requests.get(f'https://api.twitter.com/2/users/1453616508035272705/tweets', headers=headers) # https://tweeterid.com/
print(data.text)

