from discord.ext import commands
from utils.firebase import DataBase
import random

class Gambling(commands.Cog):

    def __init__(self, bot):
        self.bot = bot 

    @commands.command(name = 'dice', aliases = ['dado'])
    async def dice(self, ctx, bet: int):
        multiplier = {
            1: -1,
            2: -0.75,
            3: -0.5,
            4: 0.5,
            5: 0.75,
            6: 1
        }
        calc = lambda x, m: x*multiplier[m]
        userData = DataBase.getData(str(ctx.author.id))
        if abs(bet) > userData['coin']:
            await ctx.send(f'{ctx.author.mention}, você possui apenas {userData["coin"]} moedas!')
        else:
            res = random.randint(1,6)
            value = round(calc(abs(bet), res))
            DataBase.saveData(
                str(ctx.author.id),
                coin = userData['coin'] + value
            )
            if res < 4:
                await ctx.send(f'O dado caiu {res} e {ctx.author.mention} perdeu {value} moedas')
            else: 
                await ctx.send(f'O dado caiu {res} e {ctx.author.mention} ganhou {value} moedas')

def setup(bot):
    bot.add_cog(Gambling(bot))