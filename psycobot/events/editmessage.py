from config.config import bot
import discord

@bot.event
async def on_message_edit(before:discord.Message, after:discord.Message):
    channel = bot.get_channel(1034139187047321601)
    embed = discord.Embed(
        title='Mensagem editada!'
    )

    embed.set_author(name=before.author, icon_url=before.author.display_avatar)
    embed.add_field(name='Antiga', value=f'`{before.content}`')
    embed.add_field(name='Atual', value=f'`{after.content}`')
    embed.add_field(name='Canal', value=before.channel.mention)
    embed.set_footer(text=before.author.id)
    await channel.send(embed=embed)