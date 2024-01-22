from init import bot_token
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(
    description="Content Download",
    intents=intents,)

@bot.event
async def on_ready():
    print("OK")

bot.load_extension("commands")
bot.run(bot_token)