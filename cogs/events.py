import random 
import discord
from discord.ext import commands

class eventsCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

        @bot.event
        async def on_ready():
            print('Bot allumé')
            try:
                synced=await bot.tree.sync()
                print(f"command synced : {len({synced})}")
            except Exception as e:
                print(e)

        @bot.event
        async def on_message(message: discord.Message):
            if message.author.bot:
                return
            if message.content.lower() == 'footjob':
                channel = message.channel
                author = message.author
                await author.send("https://media.discordapp.net/attachments/535451640812142602/1130553951578759168/ezgif.com-apng-to-gif.gif?ex=682777ea&is=6826266a&hm=0be3628a65697fb3819f220cee7cae7f5827037b42e7d3227b292eae6211bd08&")
            
            if message.content.lower() =='tg morgant':
                channel = message.channel
                author = message.author
                await author.send("https://tenor.com/view/my-honest-reaction-kumala-la-kumala-la-savesta-kumala-my-honest-gif-26073681")

        @bot.tree.command(name='youtube',description="affiche un lien youtube")
        async def youtube(interaction: discord.Interaction):
            await interaction.response.send_message("alder : https://www.youtube.com/@AlderiateYouTube")

        @bot.tree.command(name='twitch',description="affiche un lien twitch")
        async def youtube(interaction: discord.Interaction):
            await interaction.response.send_message("https://www.twitch.tv/waspouille")

            
async def setup(bot):
    await bot.add_cog(eventsCog(bot))
    
