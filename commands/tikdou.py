import discord
import requests
import os

dapi = os.getenv("DAPI")

async def tikdou(ctx):
    url = re.search(r"(?P<url>https?://[^\s]+)", ctx.content).group("url")
    r = requests.get(dapi = "/tikdou", params={"url": url}).json()
    dl_link = r.get("url")
    if isinstance(dl_link, list):
        for link in dl_link:
            await ctx.respond(file=discord.File(link))
    else:
        await ctx.respond(file=discord.File(dl_link))
    await ctx.delete()
    
async def setup (bot):
    await bot.add_listener(tikdou)