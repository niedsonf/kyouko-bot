from discord.ext import commands
import threading
import discord

class Admin(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'clear')
    @commands.has_permissions(administrator = True)
    @commands.cooldown(1, 30, commands.BucketType.channel)
    async def clear(self, ctx, qtd: int):
        if qtd > 100:
            await ctx.send(f'{ctx.author.mention}, só é possível apagar 100 mensagens por vez.') 
        else:
            await ctx.channel.purge(limit = qtd)

    @commands.command(name = 'mute')
    @commands.has_permissions(administrator = True)
    async def mute(self, ctx, target: discord.Member, tempo: int):
        m = lambda t, s: t.edit(mute = s)
        await m(target, True)
        threading.Timer(abs(tempo), await m(target, False))

def setup(bot):
    bot.add_cog(Admin(bot))