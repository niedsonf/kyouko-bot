from aiohttp import request
from discord.ext import commands
import requests

class API(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'cat', aliases = ['gato'])
    async def cat(self, ctx):
        api_url = 'https://api.thecatapi.com/v1/images/search'
        response = requests.get(api_url)
        resJson = response.json()
        await ctx.send(f'{resJson[0]["url"]}')

    @commands.command(name = 'dog', aliases = ['cachorro', 'au', 'auau'])
    async def dog(self, ctx):
        api_url = 'https://dog.ceo/api/breeds/image/random'
        response = requests.get(api_url)
        resJson = response.json()
        await ctx.send(f'{resJson["message"]}')

    @commands.command(name = 'waifu', aliases = ['wa'])
    async def waifu(self, ctx):
        api_url = 'https://api.waifu.im/random'
        response = requests.get(api_url)
        resJson = response.json()
        await ctx.send(f'{resJson["images"][0]["url"]}')

def setup(bot):
    bot.add_cog(API(bot))