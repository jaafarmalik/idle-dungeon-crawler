import discord
import config

##### ##### ##### ##### ##### #####
###
### Initialize - bot.py
###
##### ##### ##### ##### ##### #####

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    if config.DEBUG == True:
        return message.channel.send(f"We have logged in as {client.user}")


@client.event
async def on_ready():
    print(f"  [IDC]: SUCCESSFULLY EXECUETED ON USER: {client.user}")


client.run(config.TOKEN)
