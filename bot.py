import discord
from discord.ext import commands
import aiohttp
import re
from datetime import timedelta
import traceback
import os
from random import choice, randint

owner = ["222526329109741568"]

bot = commands.Bot(command_prefix='p!', description=" <:mrpickles:480552232165572608> I'm that demonic border collie from that television show.")

@bot.event
async def on_ready():
    print('Mr. Pickles Discord Bot')
    print('Logged in as')
    print(bot.user.name)
    print('With ID:')
    print(bot.user.id)
    print('Number of Guilds:')
    print((len(bot.servers)))
    print('------')
    print('Invite me to your server:')
    print(discord.utils.oauth_url(bot.user.id))
    await bot.change_presence(game=discord.Game(name='with my vaccum cleaner~ | p!help'))

@bot.command(pass_context=True, hidden=True)
async def setgame(ctx, *, game):
    if ctx.message.author.id not in owner:
        return
    game = game.strip()
    if game != "":
        try:
            await bot.change_presence(game=discord.Game(name=game))
        except:
            await bot.say("<:mrpickles:480552232165572608> Failed to change game")
        else:
            await bot.say("<:mrpickles:480552232165572608> Successfuly changed game to {}".format(game))
    else:
        await bot.send_cmd_help(ctx)

@bot.command(pass_context=True, hidden=True)
async def setname(ctx, *, name):
    if ctx.message.author.id not in owner:
        return
    name = name.strip()
    if name != "":
        try:
            await bot.edit_profile(username=name)
        except:
            await bot.say("<:mrpickles:480552232165572608> Failed to change name")
        else:
            await bot.say("<:mrpickles:480552232165572608> Successfuly changed name to {}".format(name))
    else:
        await bot.send_cmd_help(ctx)

@bot.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):
        await send_cmd_help(ctx)
    elif isinstance(error, commands.BadArgument):
        await send_cmd_help(ctx)
    elif isinstance(error, commands.CommandInvokeError):
        print("<:mrpickles:480552232165572608> Exception in command '{}', {}".format(ctx.command.qualified_name, error.original))
        traceback.print_tb(error.original.__traceback__)

@bot.command(pass_context=True, no_pm=True)
async def avatar(ctx, member: discord.Member):
    """User Avatar"""
    await bot.reply("{}".format(member.avatar_url))

@bot.command(pass_context=True, no_pm=True)
async def guildicon(ctx):
    """Guild Icon"""
    await bot.reply("{}".format(ctx.message.server.icon_url))

@bot.command(pass_context=True)
async def guildid(ctx):
	  """Guild ID"""
	  await bot.say("`{}`".format(ctx.message.server.id))

@bot.command(pass_context=True, hidden=True)
async def setavatar(ctx, url):
	if ctx.message.author.id not in owner:
		return
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as r:
			data = await r.read()
	await bot.edit_profile(avatar=data)
	await bot.say("<:mrpickles:480552232165572608> I changed my icon")

@bot.command()
async def invite():
  	"""Bot Invite"""
  	await bot.say("\U0001f44d")
  	await bot.whisper("<:mrpickles:480552232165572608> Add me with this link {}".format(discord.utils.oauth_url(bot.user.id)))

@bot.command()
async def guildcount():
  	"""Bot Guild Count"""
  	await bot.say("<:mrpickles:480552232165572608> **I'm in {} Guilds!**".format(len(bot.servers)))

@bot.event
async def send_cmd_help(ctx):
    if ctx.invoked_subcommand:
        pages = bot.formatter.format_help_for(ctx, ctx.invoked_subcommand)
        for page in pages:
            em = discord.Embed(description=page.strip("```").replace('<', '[').replace('>', ']'),
                               color=discord.Color.blue())
            await bot.send_message(ctx.message.channel, embed=em)
    else:
        pages = bot.formatter.format_help_for(ctx, ctx.command)
        for page in pages:
            em = discord.Embed(description=page.strip("```").replace('<', '[').replace('>', ']'),
                               color=discord.Color.blue())
            await bot.send_message(ctx.message.channel, embed=em)
            
@bot.command(pass_context=True)
async def ping():
    """Pong!"""
    await bot.reply(" <:mrpickles:480552232165572608> Pong!")

@bot.command(pass_context=True)
async def info():
    """Pong!"""
    await bot.reply(" <:mrpickles:480552232165572608> Mr. Pickles | Ver. 0.0.1 | Developed by MZFX18#0069 & JoshTheGamer632#0017")


bot.run('')  # Where 'TOKEN' is your bot token