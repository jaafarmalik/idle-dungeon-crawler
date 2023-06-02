import asyncio
import os
import sys
import json

import discord
from discord.ext.commands import Bot

"""
    .~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.
    |   Initialize Discord Bot - bot.py |
    `~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`
    
    To begin: ensure config.json exists with required fields,
    then run this script to start the bot. 
    
"""

# ===================================S
# Check if config.json exists
# ===================================
if not os.path.isfile(f"{os.path.realpath(os.path.dirname(__file__))}/config.json"):
    sys.exit("Unable to find: 'config.json'")
else:
    with open(f"{os.path.realpath(os.path.dirname(__file__))}/config.json") as file:
        config = json.load(file)
# ===================================


# ===================================
# Declaring intents -
# ===================================
intents = discord.Intents.default()
""" -------------------------------
Set intents to the class default, all except:
    `presences`, 
    `members`,
    `message_content`
"""
# ===================================


client = discord = discord.Client(intents=intents)
client.run(config["token"])
