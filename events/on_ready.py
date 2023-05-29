"""
This module contains the on_ready event for the kanban bot.
"""
from client import client


@client.event
async def on_ready():
    """
    This event is called when the bot has finished logging in and setting things up.
    """
    print(f'We have logged in as {client.user}')
