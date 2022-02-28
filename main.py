import discord
from operations import *
from models import *
#from discord.ext import commands
from config import settings


if __name__ == '__main__':
    try:
        db.connect()
        Messages.create_table()
    except peewee.InternalError as px:
        print(str(px))
#bot = commands.Bot(command_prefix=settings['prefix'])

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return


    #for item in Messages.select().where(
       # Messages.created_at.minute < pw.datetime.datetime.now().minute
   # ):

        #await message.channel.fetch(item.dis_id_str).then(message => message.delete() )


    if message.content.startswith('$hello'):
        add_message(message.id, message.content, message.author)
        if (pw.datetime.datetime.now().minute - find_message(message.id).created_at.minute) >= 3:
            await message.channel.send(str(find_message(message.id).message) + " " + str(find_message(message.id).created_at))


#@bot.command()
#async def hello(ctx):
 #   author = ctx.message.author
#
 #   await ctx.send(f'hello, {author.mention}!')
#
#bot.run(settings['token'])
client.run(settings['token'])