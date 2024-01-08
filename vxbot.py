import discord
import re
from dotenv import load_dotenv
import os
from typing import Tuple, Final

class VxBot(discord.Client):
    async def on_ready(self) -> None:
        print('Logged on as', self.user)

    async def on_message(self, message) -> None:
        if message.author == self.user:
            return
        if contains_twitter_url(message.content) == False:
            return
        username, tweet_id = extract_username_and_hash(message.content)
        vxtwitter_url = create_vxtwitter_url(username, tweet_id)
        await message.reply(vxtwitter_url)
        
def contains_twitter_url(message: str) -> bool:
    pattern = r'https?://(twitter|x)\.com/'
    return bool(re.search(pattern, message))

def extract_username_and_hash(message: str) -> Tuple[str, str]:
    pattern = r'https?://(twitter|x)\.com\/([a-zA-Z0-9_]{1,16})/status/([0-9]+)'
    matches = re.findall(pattern, message)
    return matches[0][1], matches[0][2]

def create_vxtwitter_url(username, tweet_id) -> str:
    return f'https://vxtwitter.com/{username}/status/{tweet_id}'

if __name__ == '__main__':
    load_dotenv()
    discord_token: Final[str] = os.getenv('DISCORD_TOKEN')

    intents: discord.Intents = discord.Intents.default()
    intents.message_content = True
    client: VxBot = VxBot(intents=intents)
    client.run(discord_token)