import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix = '.', case_insensitive = True)
bot.remove_command('help')

def load():
    for f in os.listdir('./cogs'):
        if f.endswith('.py'):
            bot.load_extension(f'cogs.{f[:-3]}')
    print('Loaded Cogs!')        
load()

@bot.command(name = 'restart')
async def restart(ctx):
    for f in os.listdir('./cogs'):
        if f.endswith('.py'):
            bot.unload_extension(f'cogs.{f[:-3]}')
    load()
    await ctx.send('Comandos recarregados!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

bot.run(TOKEN)