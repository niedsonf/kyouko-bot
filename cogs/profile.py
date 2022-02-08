from discord.ext import commands
import discord
from utils.firebase import DataBase

class Profile(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'join', aliases = ['j', 'entrar'])
    async def join(self, ctx):
        userData = DataBase.createUser(str(ctx.author.id))
        if(userData == 0):
            await ctx.send(f'{ctx.author.mention} já faz parte do clube!')
        else:
            await ctx.send(f'{ctx.author.mention} entrou para o clube. Digite .h para ver todos os comandos!')
    
    @commands.command(name = 'perfil', aliases = ['p'])
    async def perfil(self, ctx, user: discord.User = None):
        if not user:
            userData = DataBase.getData(str(ctx.author.id))
            user_roles = ctx.author.roles
            nickname = ctx.author.display_name
            avatar = ctx.author.avatar_url
            
        else:
            userData = DataBase.getData(str(user.id))
            user_roles = user.roles
            nickname = user.display_name
            avatar = user.avatar_url

        if userData == 0:
            await ctx.send(f'{ctx.author.mention}, junte-se ao clube para ter acesso a todos os comandos. Digite .join ou .help para mais informações!')

        else:
            user_roles.pop(0)
            rolesString = ''
            for role in user_roles:
                rolesString += role.mention + ' '

            dailyStatus = DataBase.checkCD(userData['dailyCD'])
            weeklyStatus = DataBase.checkCD(userData['weeklyCD'])
            em = discord.Embed(title = nickname, description = rolesString, color = user_roles[-1].color)
            em.add_field(name = 'Coins', value = userData['coin'])
            em.add_field(name = 'Daily', value = dailyStatus)
            em.add_field(name = 'Weekly', value = weeklyStatus)
            em.set_footer(text = f'{nickname} participa do clube desde {userData["entrada"].strftime("%d/%m/%Y")}')
            em.set_thumbnail(url = avatar)
            await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Profile(bot))