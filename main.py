from init import bot_token
import discord

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(
    description="Content Download",
    intents=intents,)

@bot.event
async def on_ready():
    print("OK")

bot.load_extension("commands")
bot.run(bot_token)