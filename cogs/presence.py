from discord.ext import commands
import discord

class Presence(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'presence')
    async def presence(self, ctx, **kwargs):
        await self.bot.change_presence(status = discord.Status.idle, activity = discord.Streaming(name=".h", url="https://www.twitch.tv/jackverso"))

def setup(bot):
    bot.add_cog(Presence(bot))