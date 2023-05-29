"""
The main python program to run the kanban bot.
"""
import importlib
import os

from client import client
from utils import BOT_TOKEN

if not BOT_TOKEN:
    raise ValueError('BOT_TOKEN environment variable is not set.')

# Load all commands inside the commands folder
module_names = [f[:-3] for f in os.listdir('commands') if f.endswith('.py')]
for module_name in module_names:
    module = importlib.import_module(f'commands.{module_name}')

# Load all events inside the events folder
module_names = [f[:-3] for f in os.listdir('events') if f.endswith('.py')]
for module_name in module_names:
    module = importlib.import_module(f'events.{module_name}')

client.run(BOT_TOKEN)
