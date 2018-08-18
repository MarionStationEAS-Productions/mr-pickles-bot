from config import token
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = "p!")

@client.event
async def on_ready():
    print("Bot is ready!")

@client.event
async def on_message(message):
    if message.content == "ping":
        await  client.send_message(message.channel, "<a:twctstorm:460501169375281172>")



client.run(token)

