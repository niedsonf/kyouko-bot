from datetime import datetime
from discord.ext import commands
import discord
import datetime
from utils.firebase import DataBase

class Claim(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'daily', aliases = ['d', 'diaria'])
    async def daily(self, ctx):
        userData = DataBase.getData(str(ctx.author.id))
        if userData == 0:
            await ctx.send(f'{ctx.author.mention}, junte-se ao clube para ter acesso a todos os comandos. Digite .join ou .help para mais informações!')
        else:
            dailyStatus = DataBase.checkCD(userData['dailyCD'])
            if dailyStatus == 'Disponível':
                DataBase.saveData(
                    str(ctx.author.id), 
                    dailyCD = DataBase.getTimestamp() + datetime.timedelta(hours=24), 
                    coin = userData['coin'] + 3000)
                await ctx.send(f'{ctx.author.mention}, diária coletada!')
            else:
                await ctx.send(f'Diária em cooldown, tente novamente em {dailyStatus}')

    @commands.command(name = 'weekly', aliases = ['w', 'semanal'])
    async def weekly(self, ctx):
        userData = DataBase.getData(str(ctx.author.id))
        if userData == 0:
            await ctx.send(f'{ctx.author.mention}, junte-se ao clube para ter acesso a todos os comandos. Digite .join ou .help para mais informações!')
        else:
            weeklyStatus = DataBase.checkCD(userData['weeklyCD'])
            if weeklyStatus == 'Disponível':
                DataBase.saveData(
                    str(ctx.author.id), 
                    weeklyCD = DataBase.getTimestamp() + datetime.timedelta(days=7), 
                    coin = userData['coin'] + 21000)
                await ctx.send(f'{ctx.author.mention}, semanal coletada!')
            else:
                await ctx.send(f'Semanal em cooldown, tente novamente em {weeklyStatus}')

def setup(bot):
    bot.add_cog(Claim(bot))