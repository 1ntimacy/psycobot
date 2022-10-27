from config.config import bot
from discord.ext import commands
from time import sleep
import discord
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(ctx: commands.Context, limit:int):
    z = await ctx.channel.purge(limit=limit)
    embed=discord.Embed(
        title='Clear',
        description=f'foram apagadas o total de {len(z)} mensagens com nenhuma falha.'
    )
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(url=ctx.author.display_icon)
    msg = await ctx.send(embed=embed)
    sleep(15)
    await msg.delete()

@clear.error
async def clearMissingPermissionsError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('Você não tem permissões suficientes!')

@clear.error
async def clearMissingRequiredArgument(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.reply('Está faltando parâmetros! coloque a quantidade de mensagens que deseja apagar depois do `.clear` exemplo: `.clear 20`')