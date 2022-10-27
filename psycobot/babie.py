from config.config import bot, token
from events import onready, onmemberjoin, deletemessage, editmessage
from commands.banner import banner
from commands.music import join
from commands import lock, unlock, avatar, kick, ban, unban, clear, help, pvspammer
##########################################
#                 EVENTS
##########################################

#     O QUE FAZER QUANDO O BOT LIGAR

onready

#     O QUE FAZER QUANDO UM MEMBRO ENTRAR

onmemberjoin
deletemessage
editmessage

##########################################
#               COMMANDS
##########################################

#     COMANDO PARA PEGAR AVATAR DE UM USUÁRIO

avatar
banner
lock
unlock
kick
ban
unban
clear
help
join
pvspammer

#RUN BOT
bot.run(token)