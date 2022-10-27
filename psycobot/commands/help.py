from config.config import bot
import discord
from discord.ext import commands

@bot.command()
async def ajuda(ctx: commands.Context):
    embed=discord.Embed(
        title='Ajuda'
    )
    embed.add_field(name='avatar', value='Pegue o avatar de qualquer usuário do discord.')
    embed.add_field(name='banner', value='Pegue o banner de qualquer usuário do discord.')
    embed.add_field(name='ban', value="Bane um usuário.")
    embed.add_field(name="unban", value="Desbane um usuário.")
    embed.add_field(name='kick', value="Expulsa um usuário.")
    embed.add_field(name='lock', value='Feche um canal no discord.')
    embed.add_field(name='unlock', value='Abre um canal no discord.')
    embed.add_field(name='clear', value='Limpe um canal no discord.')
    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.set_thumbnail(url=ctx.author.display_icon)
    await ctx.reply(embed=embed)