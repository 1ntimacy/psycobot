import discord
import requests
from config.config import bot
from discord.ext import commands

@bot.command()
async def avatar(ctx, usuário:discord.User):
    try:
        get_avatar = requests.get(f"https://api.147.wtf/user?id={usuário.id}")
        avatar_json = get_avatar.json()
        avatar = avatar_json['user']['avatarURL']
        avatar = str(avatar)
        teste_avatar = avatar.find('webp')
        user = avatar_json['user']['username']
        embed=discord.Embed(
            title=f':frame_photo: {user}'
        )
        embed.set_image(url='{}{}'.format(avatar, '?size=2048'))
        if teste_avatar == 89:
            teste = avatar.replace('webp','gif')
            embed.set_image(url='{}{}'.format(teste, '?size=2048'))
        await ctx.send(embed=embed)
    except:
        await ctx.send('Deu algum erro contate algum desenvolvedor do bot.')

@avatar.error
async def avatarError(ctx: commands.Context, error: commands.CommandError):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Erro! está faltando parâmetros coloque o id ou mencione o usuário depois de escrever o comando, exemplo: `.avatar 23423423424442` ou `.avatar @kyan`')
