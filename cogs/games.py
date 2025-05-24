import random 
import discord
from discord.ext import commands
from discord import app_commands

class GamesCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.hybrid_command()
    async def coinflip(self,ctx):
        auteur = ctx.author
        result = random.choice(['Pile','Face'])
        await ctx.send(f'Resultat obtenu : {result}')
        print(f"{auteur} a joué et a fait {result} !")
    
async def setup(bot):
    await bot.add_cog(GamesCog(bot))