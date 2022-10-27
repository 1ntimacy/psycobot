from config.config import prefix, bot
import discord

@bot.event
async def on_ready():
    print(f'{bot.user} está online !')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"prefixo: {prefix}"))