from config.config import bot
from discord.ext import commands
import discord

@bot.command()
@commands.has_permissions(administrator=True)
async def unban(ctx: commands.Context, usuario: discord.User, *, reason='Sem motivo'):
    embed = discord.Embed(title=f"<:right:1033860677321891870> | Desbanido")
    embed.add_field(name="<:membro:1033852173865451624> membro", value=f"{usuario} `{usuario.id}`")
    embed.add_field(name="<:moderador:1033852036531363880> moderador", value=f"{ctx.author.mention} `{ctx.author.id}`")
    embed.add_field(name='<:arquivo:1033852096140808264> motivo', value=reason)
    embed.set_thumbnail(url=usuario.display_avatar)
    channel = bot.get_channel(1034148126916890655)
    await channel.send(embed=embed)
    await ctx.guild.unban(user=usuario)
    await ctx.reply(embed=embed)

@unban.error
async def unbanMissingRequiredArgumentError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        ctx.reply('Está faltando parâmetros no comando. Tente novamente ou contate o desenvolvedor.')

@unban.error
async def unbanMissingPermissionsError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        ctx.reply('Você não tem permissões suficientes!')