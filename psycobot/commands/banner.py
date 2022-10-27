import discord
from config.config import bot
import requests

@bot.command()
async def banner(ctx, id:discord.Member):
    socket = requests.get(f'https://api.147.wtf/banner?id={id.id}')
    socket_user = requests.get(f'https://api.147.wtf/user?id={id.id}')

    socket_user_json = socket_user.json()
    socket_json = socket.json()
    
    nick = socket_user_json["user"]['username']
    nick_hashtag = socket_user_json['user']['discriminator']
    banner = socket_json['banner']

    embed = discord.Embed(
        title=f':frame_photo: **{nick}#{nick_hashtag}**'
    )

    embed.set_image(url='{}{}'.format(banner, '?size=2048'))
    await ctx.send(embed=embed)