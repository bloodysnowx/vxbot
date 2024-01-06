import discord
import re
from dotenv import load_dotenv
import os

class VxBot(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if contains_twitter_url(message.content) == False:
            return
        username, tweet_id = extract_username_and_hash(message.content)
        vxtwitter_url = create_vxtwitter_url(username, tweet_id)
        await message.reply(vxtwitter_url)
        
def contains_twitter_url(url):
    pattern = r'https?://(twitter|x)\.com/'
    return bool(re.match(pattern, url))

def extract_username_and_hash(url):
    pattern = r'https?://(twitter|x)\.com\/([a-zA-Z0-9_]{1,16})/status/([0-9]+)'
    matches = re.findall(pattern, url)
    return matches[0][1], matches[0][2]

def create_vxtwitter_url(username, tweet_id):
    return f'https://vxtwitter.com/{username}/status/{tweet_id}'

load_dotenv()
discord_token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = VxBot(intents=intents)
client.run(discord_token)