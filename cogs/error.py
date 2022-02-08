from turtle import title
from discord.ext import commands
import discord

class ErrorHandle(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):

        if isinstance(error, commands.MissingPermissions):
            title = f'Permissão ausente'
            desc = f'Use ".help <nome do comando>" para mais informações.'

        elif isinstance(error, commands.MissingRequiredArgument):
            title = f'Argumento ausente'
            desc = f'Use ".help <nome do comando>" para mais informações.'

        elif isinstance(error, commands.BadArgument):
            title = f'Argumento inválido'
            desc = f'Use ".help <nome do comando>" para mais informações.'

        elif isinstance(error, commands.CommandOnCooldown):
            title = f'Comando em cooldown'
            desc = f'Tente novamente em {round(error.retry_after)}s.'

        em = discord.Embed(title = title, description = desc, color = ctx.author.color)
        em.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(ErrorHandle(bot))