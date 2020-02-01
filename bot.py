import discord
from discord.ext import commands, tasks
import os

client = commands.Bot(command_prefix = '.')


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

players = {}


@client.command()
async def load(ctx, extension):
    client.load_extension(f'functions.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'functions.{extension}')


for filename in os.listdir('./functions'):
    if filename.endswith('.py'):
        client.load_extension(f'functions.{filename[:-3]}')


# States when the bot is ready
@client.event
async def on_ready():
    print("Bot is powered up.")


client.run(token)
