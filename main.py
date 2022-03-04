import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix=settings['prefix'])


def is_me(ctx):
    return ctx.message.author == bot.user


@bot.command()
async def hello(ctx):
    author = ctx.message.author

    await ctx.send(f'hello, {author.mention}!')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if is_me:
        return

    if message.mentions != []:
        await message.delete(delay=10)

bot.run(settings['token'])




