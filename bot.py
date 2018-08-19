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
    if message.content == "p!ping":
        await  client.send_message(message.channel, "What the fuck do you want? I'm here to stop the crime.")
		
@client.event
async def on_message(message):
    if message.content == "p!info":
        await  client.send_message(message.channel, "<:mrpickles:480552232165572608> Mr. Pickles | Ver. 0.0.1 | Developed by MZFX18#0069 & JoshTheGamer632#0017")



client.run(token)

