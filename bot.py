###
### Bot entry
###

import config
import debug

import discord

# from discord import Client

client = discord.Client()


@client.event
async def on_ready():
    print(f"  [IDC]: SUCCESSFULLY EXECUETED ON USER: {client.user}")


client.run(config.TOKEN)
