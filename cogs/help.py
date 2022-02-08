from discord.ext import commands
import discord

class Help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    def getEmbed(self, ctx, **kwargs):
        em = discord.Embed(title = kwargs['title'], description = kwargs['desc'], color = ctx.author.color)
        return em

    @commands.command(name = 'convidar', aliases = ['invite'])
    async def convidar(self, ctx):
        await ctx.send(f'https://discord.com/api/oauth2/authorize?client_id=769182098350800936&permissions=8&scope=bot')

    @commands.group(name = 'help', aliases = ['h', 'ajuda'])
    async def help(self, ctx):
        if ctx.invoked_subcommand is None:
            comandos = '.join ou .j\n.daily ou .d\n.weekly ou .w\n.perfil ou .p\n.dice\n.clear\n.cat'
            descricao = 'Entrar para o clube\nRecompensa diária\nRecompensa semanal\nAbrir perfil\nAposta jogando um dado\nApaga mensagens do chat\nGatos'
            em = discord.Embed(title = 'Lista de Comandos', description = 'Digite .help <nome do comando> para ter mais informações sobre o mesmo', color = ctx.author.color)
            em.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url)
            em.add_field(name = chr(173), value = comandos)
            em.add_field(name = chr(173), value = chr(173))
            em.add_field(name = chr(173), value = descricao)
            await ctx.send(embed = em)

    @help.command()
    async def join(self, ctx):
        em = self.getEmbed(ctx, title = f'Junte-se ao clube', desc = 'Utilize o comando <.join> para se cadastrar e ter acesso a todos os comandos!')
        await ctx.send(embed = em)

    @help.command()
    async def daily(self, ctx):
        em = self.getEmbed(ctx, title = f'Recompensa diária', desc = 'Utilize o comando <.daily> para coletar a recompensa de 3.000 moedas diárias. É necessário estar cadastrado!')
        await ctx.send(embed = em)

    @help.command()
    async def weekly(self, ctx):
        em = self.getEmbed(ctx, title = f'Recompensa semanal', desc = 'Utilize o comando <.weekly> para coletar a recompensa de 21.000 moedas semanais. É necessário estar cadastrado!')
        await ctx.send(embed = em)

    @help.command()
    async def perfil(self, ctx):
        em = self.getEmbed(ctx, title = f'Abrir perfil', desc = 'Utilize o comando <.p> para abrir o seu perfil ou o de outro player (ex: .p @alvo). É necessário estar cadastrado!')
        await ctx.send(embed = em)

    @help.command()
    async def dice(self, ctx):
        em = self.getEmbed(ctx, title = f'Apostar no dado', desc = f'Utilize o comando <.dice "valor"> para apostar a quantia no lançamento de um dado.')
        em.add_field(name = 'Lados 1,2 e 3', value = 'O usuário perde, respectivamente, 100%, 75% ou 50% do valor apostado')
        em.add_field(name = 'Lados 4,5 e 6', value = 'O usuário ganha, respectivamente, 50%, 75% ou 100% do valor apostado')
        await ctx.send(embed = em)

    @help.command()
    async def cat(self, ctx):
        em = self.getEmbed(ctx, title = f'Meeeeooww', desc = f'Utilize o comando <.cat> para invocar uma foto ou gif de gato aleatoriamente')
        await ctx.send(embed = em)

    @help.command()
    async def clear(self, ctx):
        em = self.getEmbed(ctx, title = f'Apaga mensagens do chat', desc = f'Utilize o comando <.clear "nº <= 100"> para apagar mensagens no chat. É necessário ser um administrador do servidor!')

def setup(bot):
    bot.add_cog(Help(bot))