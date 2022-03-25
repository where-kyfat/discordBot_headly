"""Remove_bot logic

Implements logic of removing messages with mention,
For now it removes messages after 10 sec,
Also it removes messages with mentions elder 24 hours.
To remove these messages send "$delete_old_mes" to discord chat.

"""

from datetime import datetime, timedelta

from configs.config import BOT_INSTANCE


@BOT_INSTANCE.event
async def on_message(message):
    """Remove message with mention after 10 sec."""
    await BOT_INSTANCE.process_commands(message)

    if message.mentions:
        await message.delete(delay=10)


@BOT_INSTANCE.command()
async def delete_old_mes(ctx):
    """Remove messages with mention elder 24 hours
       and send their number in a chat.

    """
    await ctx.send('Delete starting')
    count_deleting = 0
    async for message in ctx.channel.history(limit=None):
        if (message.mentions and
                (message.created_at < datetime.now() - timedelta(hours=24))):
            await message.delete()
            count_deleting += 0
    await ctx.send(f'Delete ended! Deleted {count_deleting} messages')
