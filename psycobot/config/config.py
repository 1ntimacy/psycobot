import discord
from discord.ext import commands
import json

# Request GET config.json
with open("config/config.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    owner = data["owner"]
    guild = data["guild"]

bot = commands.Bot(prefix, intents = discord.Intents.all())
