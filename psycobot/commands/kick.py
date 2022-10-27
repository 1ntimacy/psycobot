from config.config import bot
from discord.ext import commands
import discord

@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx: commands.Context, usuario:discord.Member, *, reason="Sem motivo"):
    embed = discord.Embed(title=f"<:banido:1033852121071763538> | Kickado")
    embed.add_field(name="<:membro:1033852173865451624> membro", value=f"{usuario} `{usuario.id}`")
    embed.add_field(name="<:moderador:1033852036531363880> moderador", value=f"{ctx.author.mention} `{ctx.author.id}`")
    embed.add_field(name='<:arquivo:1033852096140808264> motivo', value=reason)
    embed.set_thumbnail(url=usuario.display_avatar)
    await usuario.send(embed=embed)
    await usuario.kick(reason=reason)
    channel = bot.get_channel(1034148083384205413)
    await channel.send(embed=embed)
    await ctx.reply(embed=embed)


@kick.error
async def kickMemberNotFoundError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply('Membro não encontrado!')

@kick.error
async def kickMissingPermissionsError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('Você não tem permissões suficentes!')