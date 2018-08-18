from config import token
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = "p!")

@client.event
async def on_ready():
    print("*I have been summoned...*")

@client.event
async def on_message(message):
    if message.content == "ping":
        await  client.send_message(message.channel, "<a:twctstorm:460501169375281172> Coming Shortly")
		
@client.event
async def on_message(message):
    if message.content == "info":
        await  client.send_message(message.channel, "Mr. Pickles | Ver. 0.0.1 | Developed by MZFX18#0069 & JoshTheGamer632#0017")



client.run(token)

