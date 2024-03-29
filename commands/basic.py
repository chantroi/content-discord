from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def content(self, ctx):
        await ctx.respond("Đây là Content Download phiên bản Discord")

    @commands.slash_command()
    async def clear(self, ctx, limit: int = None):
        if limit:
            await ctx.channel.purge(limit=limit)
            await ctx.respond(f"Đã xoá {limit} tin nhắn trong kênh {ctx.channel.mention}")
        else:
            await ctx.channel.purge()
            await ctx.respond(f"Đã xoá mọi tin nhắn trong kênh {ctx.channel.mention}", delete_after=10)

def setup(bot):
    bot.add_cog(Basic(bot))