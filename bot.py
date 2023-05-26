import asyncio
import os
import sys
import json

import discord
from discord.ext.commands import Bot

import config

"""
    Initialize Discord Bot - bot.py
"""

if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("Unable to find: 'config.json'")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)

intents = discord.Intents.default()
# intents.message_content = True

bot = Bot(
    command_prefix="!",
    intents=intents,
)

client = discord = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("We have logged in")
    return


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "ping":
        await message.channel.send("pong")


client.run(config["token"])
