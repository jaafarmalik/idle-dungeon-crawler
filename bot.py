###
### An example of 'message_content' intent.
###

# Import our configuration file, redacted for security.
import config

# Import the library
import discord

intents = discord.Intents.default()
intents.message_content = True

# Create an instance of client, our connection to discord.
client = discord.Client(intents=intents)


# Initiate the @client.event decorator to register an event.

# The discord.py lib has many events, so we handle them in a
# "callback" manner.


# Essentially, a function that is called when something happens.
# In this case, the on_ready() event is called when the bot has
# finished logging in, and the on_message() event is called when
# the bot has received a message.
@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


# Since the on_message() event is called every time a message is sent,
# we have to make sure to ignore messages sent by the bot itself.
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # After, we check if message.content starts with '!hello', and if
    # it does, we send a message back to the channel it was sent in.
    # This is a very basic way of handling commands, which will need
    # to be later automated with the discord.ext.commands framework.
    if message.content.startswith("!hello"):
        await message.channel.send("Hello!")


# Lastly, we run the bot login token.
client.run(config.TOKEN)
