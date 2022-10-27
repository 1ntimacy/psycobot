from config.config import bot
import discord
import requests

@bot.event
async def on_member_join(member:discord.Member):
    channel = bot.get_channel(1033469533631025241)
    mainchannel = bot.get_channel(1033469533631025234)
    rules = bot.get_channel(1033508471313801257)
    alert = bot.get_channel(1033469533631025236)

    embed = discord.Embed(
        description=f"<a:black_setapreta1992:1033510158741024778> sobre nós {mainchannel.mention}\n<a:black_setapreta1992:1033510158741024778> veja as regras em {rules.mention}\n<a:black_setapreta1992:1033510158741024778> veja os alertas em {alert.mention}",
        colour=discord.Color.light_gray()
    )
    get_avatar = requests.get(f"https://api.147.wtf/user?id={member.id}")
    avatar_json = get_avatar.json()
    avatar = avatar_json['user']['avatarURL']
    avatar = str(avatar)
    teste_avatar = avatar.find('webp')
    if teste_avatar == 89:
            teste = avatar.replace('webp','gif')
            embed.set_author(name=f"{member} bem vindo!", icon_url=teste)
    embed.set_author(name=f"{member} bem vindo!", icon_url=avatar)
    embed.set_footer(text=member.id)
    await channel.send(embed=embed)
    channel2 = bot.get_channel(1034150508182654986)
    await channel2.send(embed=embed)