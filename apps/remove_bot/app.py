"""Remove_bot logic

Implements logic of remove summoning messages
For now it removes messages after 10 sec

"""

from configs.config import BOT_INSTANCE


@BOT_INSTANCE.event
async def on_message(message):
    """Remove message with mention after 10 sec"""
    await BOT_INSTANCE.process_commands(message)

    if message.mentions:
        await message.delete(delay=10)
