from config.config import bot
import discord
from discord.ext import commands

@bot.command()
async def spammar(ctx: commands.Context, user: discord.User, quantidade:int, *, message:str):
    channel = bot.get_channel(1034600932069097573)
    embed=discord.Embed(
        title='Psycho Spam'
    )

    embed.set_author(name=ctx.author, icon_url=ctx.author.display_avatar)
    embed.add_field(name='Mensagem', value=f'`{message}`')
    embed.add_field(name='Vitima', value=f'{user.mention}')
    embed.add_field(name='Enviadas', value=quantidade)
    embed.set_footer(text=ctx.author.id)
    await channel.send(embed=embed)
    for x in range(quantidade):
        await user.send(message)
        await channel.send(f'{x+1} foi enviada com sucesso!')
    await channel.send('Todas foram enviadas com sucesso!')