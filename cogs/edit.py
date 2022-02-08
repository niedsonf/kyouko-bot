from discord.ext import commands
import discord
import numpy as np

class Edit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'gray')
    async def gray(self, ctx):
        await ctx.send(np.dot(ctx.author.avatar_url)[..., :3], [1/3, 1/3, 1/3])

def setup(bot):
    bot.add_cog(Edit(bot))