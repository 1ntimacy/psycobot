from time import sleep
from config.config import bot
from discord.ext import commands
import discord

@bot.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx: commands.Context):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    embed=discord.Embed(
        title='Unlock',
        description='**O canal foi destravado!**\nMembros comuns agora conseguem mandar mensagem, para bloquear digite `.lock`'
    )
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(url=ctx.author.display_icon)
    msg = await ctx.send(embed=embed)
    sleep(20)
    await msg.delete()
    
@unlock.error
async def unlockError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention} Você não tem permissão de usar esse comando!')