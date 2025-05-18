import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

class lebot(commands.Bot):
    async def setup_hook(self):
        for extension in ['games','events','spec']:
            await self.load_extension(f'cogs.{extension}')
            

bot = lebot(command_prefix="/",intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot allumé')
    try:
        synced=await bot.tree.sync()
        print(f"command synced : {len(synced)}")
    except Exception as e:
        print(e)

bot.run(os.getenv("TOKEN"))
