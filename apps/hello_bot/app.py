"""The main module with application "hello" logic"""

# Import an instance of "bot" from config
from configs.config import BOT_INSTANCE


@BOT_INSTANCE.command()
async def hello(ctx):
    """Responds to the greeting

    This func responds to the greeting like:
    request -> [ctx]hello
    response -> Hello, @[user_name]!

    """

    author = ctx.message.author

    await ctx.send(f'hello, {author.mention}!')
