import discord
from discord.ext import commands
import requests


class League(commands.Cog):
    server = 'na'
    api_key = 'RGAPI-5070294c-f3e1-4193-88ee-1e74b4dd5a9e'

    async def get_summoner_ID(self, summoner_name, lol_api_key='RGAPI-091fd782-b935-41b2-9b15-3ee593fb998c'):
        URL = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summoner_name + '?api_key=' + lol_api_key
        response = requests.get(URL)

        return response.json()

    async def request_ranked_Data(self, ID, region='na', lol_api_key='RGAPI-091fd782-b935-41b2-9b15-3ee593fb998c'):
        URL = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + ID + '/?api_key=' + lol_api_key
        response = requests.get(URL)

        return response.json()

    @commands.Cog.listener()
    async def on_ready(self):
        print('League function is online.')

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def op(self, ctx, *, name):
        return await ctx.channel.send(("`Here you go:` \n" +
                                       f"""https://na.op.gg/summoner/userName={name}"""))

    @commands.command()
    async def lol(self, ctx, *, message):
        embed = discord.Embed(
            colour=discord.Colour.red(),
            title=f"""{message}'s Rank Stats"""
        )

        responseJSON = await self.get_summoner_ID(message)

        ID = responseJSON['id']
        ID = str(ID)
        responseJSON2 = await self.request_ranked_Data(ID)

        self.tier = responseJSON2[0]['tier']
        self.division = responseJSON2[0]['rank']
        self.lp = str(responseJSON2[0]['leaguePoints'])
        self.wins = str(responseJSON2[0]['wins'])
        self.losses = str(responseJSON2[0]['losses'])

        embed.set_thumbnail(url='https://www.riotgames.com/darkroom/1440/656220f9ab667529111a78aae0e6ab9f'
                                ':10e46504aa7f70eb33ef43ee464cb2d4/01-logo.png')

        embed.add_field(name="Tier:", value=f"""{self.tier}""", inline=False)
        embed.add_field(name="Division:", value=f"""{self.division}""", inline=False)
        embed.add_field(name="LP:", value=f"""{self.lp}""", inline=False)
        embed.add_field(name="Wins:", value=f"""{self.wins}""", inline=False)
        embed.add_field(name="Losses:", value=f"""{self.losses}""", inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(League(client))
