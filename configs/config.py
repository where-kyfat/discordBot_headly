"""Bot configuration file

Add any common settings to this file

"""

import json
import os
from discord.ext import commands


# Bot information and tokens
with open("configs/bot_token.json", "r") as read_file:
    BOT_TOKEN = json.load(read_file)

# Initializing a bit instance
BOT_INSTANCE = commands.Bot(command_prefix=BOT_TOKEN['prefix'])

# Database parameters from environment params
DB = {
    'USER': os.environ.get('DB_USER'),
    'POSTGRES': os.environ.get('DB_POSTGRES'),
    'PASSWORD': os.environ.get('DB_PASSWORD'),
    'HOST': os.environ.get('DB_HOST'),
    'PORT': os.environ.get('DB_PORT')
}
