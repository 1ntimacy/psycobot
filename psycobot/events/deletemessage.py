from config.config import bot
import discord

@bot.event
async def on_message_delete(message:discord.Message):
    channel = bot.get_channel(1034139157062234152)
    embed = discord.Embed(
        title='Mensagem apagada!'
    )

    embed.set_author(name=message.author, icon_url=message.author.display_avatar)
    embed.add_field(name='Mensagem', value=f'`{message.content}`')
    embed.add_field(name='Canal', value=message.channel.mention)
    embed.set_footer(text=message.author.id)
    await channel.send(embed=embed)