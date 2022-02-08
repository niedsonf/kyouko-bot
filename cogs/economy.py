from utils.firebase import DataBase
from discord.ext import commands
import discord

class Economy(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'give', aliases = ['g', 'doar'])
    async def give (self, ctx, user: discord.User, value: int):
        if user.id == ctx.author.id:
            await ctx.send(f'{ctx.author.mention}, você não pode transferir dinheiro para si mesmo.')
        else:
            userData = DataBase.getData(str(ctx.author.id))
            if abs(value) > userData['coin']:
                await ctx.send(f'{ctx.author.mention}, você possui apenas {userData["coin"]} moedas.')
            else:
                targetData = DataBase.getData(str(user.id))
                DataBase.saveData(
                    str(ctx.author.id),
                    coin = userData['coin'] - abs(value)
                )
                DataBase.saveData(
                    str(user.id),
                    coin = targetData['coin'] + abs(value)
                )
                await ctx.send(f'{ctx.author.mention} deu {abs(value)} moedas para {user.mention}')

def setup(bot):
    bot.add_cog(Economy(bot))