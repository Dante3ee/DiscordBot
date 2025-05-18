import discord
from discord.ext import commands
from discord import app_commands

class specCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.watchlist = {}

    @app_commands.command(name="spec", description="Tu recevras un DM quand la personne termine sa game")
    @app_commands.describe(cible="La personne à surveiller")
    async def spec(self, interaction: discord.Interaction, cible: discord.Member):
        surveillant = interaction.user

        if cible.bot:
            await interaction.response.send_message("Tu ne peux pas surveiller un bot 🤖", ephemeral=True)
            return

        self.watchlist[cible.id] = surveillant.id

        await interaction.response.send_message(
            f"Je te DM quand **{cible.display_name}** termine sa game", ephemeral=True
        )

    @commands.Cog.listener()
    async def on_presence_update(self, before: discord.Member, after: discord.Member):
        if after.id in self.watchlist:
            if before.activity and not after.activity:
                surveillant_id = self.watchlist.pop(after.id)
                surveillant = await self.bot.fetch_user(surveillant_id)
                try:
                    await surveillant.send(f"✅ {after.display_name} a terminé sa game !")
                except discord.Forbidden:
                    print(f"[ERREUR] DMs fermés pour {surveillant}")

async def setup(bot):
    await bot.add_cog(specCog(bot))
