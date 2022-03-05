"""Executable bot script

Uses the imported logic of the bot for the following run

If you wrote new logic and want to use it - add import with your module

"""

# Configuration of bot
from configs.config import BOT_INSTANCE, BOT_TOKEN

# Remove old message logic
import apps.remove_bot

# Hello bot logic
import apps.hello_bot


if __name__ == '__main__':
    BOT_INSTANCE.run(BOT_TOKEN['token'])
