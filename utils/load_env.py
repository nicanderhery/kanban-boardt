"""
This module contains all variables that need to be loaded from the .env file.
"""
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Discord environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')
GUILD_ID = os.getenv('GUILD_ID')

# Postgres environment variables
POSTGRES_URL = os.getenv('POSTGRES_URL')
POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
