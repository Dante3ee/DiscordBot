import random 
from discord.ext import commands

class GamesCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.hybrid_command()
    async def pileouface(self,ctx):
        result = random.choice(['Pile','Face'])
        await ctx.send(f'Resultat obtenu : {result}')
    
async def setup(bot):
    await bot.add_cog(GamesCog(bot))