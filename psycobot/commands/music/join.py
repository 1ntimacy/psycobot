from config.config import bot
import discord
from discord.ext import commands

@bot.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def join(ctx: commands.Context):
    author = ctx.message.author
    voice_channel = author.voice.channel
    await voice_channel.connect()
    await ctx.reply(f'Entrei com sucesso em {voice_channel}')

@bot.command()
@commands.has_permissions(administrator=True)
async def quit(ctx: commands.Context):
    for x in bot.voice_clients:
        if(x.channel == ctx.author.voice.channel):
            return await x.disconnect()

@join.error
async def joinMissingPermissionsERROR(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        ctx.reply('Você não tem permissões suficientes!')

@quit.error
async def quitMissingPermissionsERROR(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        ctx.reply('Você não tem permissões suficientes!')