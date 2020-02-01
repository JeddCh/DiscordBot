import discord
from discord.ext import commands


class Command(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Command function is online.')

    # returns ping of the bot
    @commands.command()
    async def ping(self, ctx):
        await ctx.channel.send(f"""Ping: {round(self.client.latency * 1000)}ms""")

    # function clears number of lines entered defaulting at 2
    @commands.command()
    @commands.has_role('Mods')
    async def clear(self, ctx, amount=2):
        await ctx.channel.purge(limit=amount)


def setup(client):
    client.add_cog(Command(client))