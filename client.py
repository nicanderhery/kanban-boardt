"""
This module contains the client for the kanban bot.
"""
import discord

from utils.load_env import GUILD_ID


class NClient(discord.Client):
    """
    The client for the kanban bot that inherits from discord.Client.
    """

    def __init__(self, *, intents: discord.Intents, guild_id: int = 0):
        super().__init__(intents=intents)
        # A CommandTree is a special type that holds all the application command
        # state required to make it work. This is a separate class because it
        # allows all the extra state to be opt-in.
        # Whenever you want to work with application commands, your tree is used
        # to store and work with them.
        # Note: When using commands.Bot instead of discord.Client, the bot will
        # maintain its own tree instead.
        self.tree = discord.app_commands.CommandTree(self)
        self.guild = discord.Object(id=guild_id)

    # In this basic example, we just synchronize the app commands to one guild.
    # Instead of specifying a guild to every command, we copy over our global commands instead.
    # By doing so, we don't have to wait up to an hour until they are shown to the end-user.
    async def setup_hook(self):
        # This copies the global commands over to your guild.
        self.tree.copy_global_to(guild=self.guild)
        await self.tree.sync(guild=self.guild)


selected_intents = discord.Intents.default()
selected_intents.message_content = True
client = NClient(intents=selected_intents,
                 guild_id=int(GUILD_ID) if GUILD_ID else 0)
