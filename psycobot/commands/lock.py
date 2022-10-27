from time import sleep
from config.config import bot
from discord.ext import commands
import discord

@bot.command()
@commands.has_permissions(administrator=True)
async def lock(ctx: commands.Context):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    embed=discord.Embed(
        title='Lock',
        description='**O canal foi travado!**\nMembros comuns não conseguem mandar mensagem, para desbloquear digite `.unlock`'
    )
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(url=ctx.author.display_icon)
    msg = await ctx.send(embed=embed)
    sleep(20)
    await msg.delete()

@lock.error
async def lockError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention} Você não tem permissão de usar esse comando!')