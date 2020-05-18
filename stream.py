import discord, asyncio, sys, time, os, io, shutil
client = discord.Client()
token = ""
from discord.ext import (
    commands,
    tasks
)
client = commands.Bot(
    description='Set Stream Status',
    command_prefix="x",
    self_bot=True
)

def lol(cmd):
    subprocess.call(cmd, shell=True)
    
@client.event
async def on_connect():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("► Set Stream Status ".center(width))
        print("► Made by slash".center(width))
        print("► User: {0}".format(client.user).center(width))
    ui()
@client.command()
async def stream(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/zzz", 
    )
    await client.change_presence(activity=stream) 
    width = shutil.get_terminal_size().columns
    print("")
    print("")
    print("→ You are currently streaming: {0} ".format(message).center(width))

client.run(token, bot=False)