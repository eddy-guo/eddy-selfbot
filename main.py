import os, discord, requests, pdb
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    global guild
    guild = discord.utils.get(bot.guilds, name=GUILD)
    print(f"{bot.user.name} is now connected to {guild.name}.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    ctx = await bot.get_context(message)

    user = int(message.content)
    headers = {
        'Authorization': f'Bearer {BEARER_TOKEN}',
    }
    data = requests.get(f'https://api.twitter.com/2/users/{user}/tweets', headers=headers) # https://tweeterid.com/
    
    response = eval(data.text)['data'][0] # 0 for most recent tweet
    await ctx.send(response)

bot.run(TOKEN)