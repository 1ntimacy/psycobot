from config.config import bot
from discord.ext import commands
import discord

@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx: commands.Context, usuario:discord.User, *, reason="Sem motivo"):
    embed = discord.Embed(title=f"<:banido:1033852121071763538> | Banido")
    embed.add_field(name="<:membro:1033852173865451624> membro", value=f"{usuario} `{usuario.id}`")
    embed.add_field(name="<:moderador:1033852036531363880> moderador", value=f"{ctx.author.mention} `{ctx.author.id}`")
    embed.add_field(name='<:arquivo:1033852096140808264> motivo', value=reason)
    embed.set_footer(text='discord.gg/psycobabies')
    embed.set_thumbnail(url=usuario.display_avatar)
    await usuario.send(embed=embed)
    await ctx.guild.ban(user=usuario, reason=reason)
    channel = bot.get_channel(1034148104661901342)
    await channel.send(embed=embed)
    await ctx.reply(embed=embed)


@ban.error
async def banidoMemberNotFoundError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MemberNotFound):
        await ctx.reply('Membro não encontrado!')

@ban.error
async def banidoMissingPermissionsError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        await ctx.reply('Você não tem permissões suficentes!')