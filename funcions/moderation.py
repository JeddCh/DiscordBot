import discord
from discord.ext import commands
from discord.utils import get


class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Moderation function is online.')

    # This function kicks people from the discord
    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)

    # This function bans members from the discord
    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)

    # function unbans member
    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                await ctx.channel.send(f"""Unbanned {user.name}#{user.discriminator}""")
                return

    # filters and deletes profanity
    @commands.Cog.listener()
    async def on_message(self, message):
        bad_words = ["chink", "slav"]

        for word in bad_words:
            if message.content.count(word) > 0:
                await message.delete()
                await message.channel.send(f"""{message.author.mention} Comment was deleted, violation of channel 
guidelines""")


def setup(client):
    client.add_cog(Moderation(client))
