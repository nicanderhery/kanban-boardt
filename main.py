"""
The main python program to run the kanban bot.
"""
import os

import discord
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Check if environment variables are set
if BOT_TOKEN is None:
    raise ValueError('BOT_TOKEN environment variable not set.')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    """
    This event is called when the bot has finished logging in and setting things up.
    """
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message: discord.Message):
    """
    This event is called when a message is sent in a channel the bot can see.

    Args:
        message (_type_): _description_
    """
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send(f'Hello! {message.author.mention}')

client.run(BOT_TOKEN)
