####
### discord.py - loggin module
##
#

#
# READ THE DOCS! ~ JAAFAR <-- I'm not joking.
#
# CREDIT/DOCREF:
#
# https://discordpy.readthedocs.io/en/stable/logging.html
# https://docs.python.org/3/library/logging.handlers.html#module-logging.handlers

# Prints to sys.stderr with coloured output.
import logging
import logging.handlers

# Provides a default configurations for the
# logging module on discord when using Client.run():
import config
import discord
import bot

from discord import Client

# Can be also configured to output to a file or
# by using the loggin.handlers specifically -
# logging.handlers.FileHandler

# Outputs a debug log to the working directory -
# handler = logging.FileHandler(filename="debug.log", encoding="utf-8", mode="w")

# To run the bot with the debug handler, pass
# the handler as a keyword argument to Client.run():
# Client.run(config.TOKEN, log_handler=handler)


# You could also configure the log level to: logging.DEBUG

# client.run(config.TOKEN, log_handler=handler, log_level=logging.DEBUG)

# Verbose level of DEBUG a lot of events logged, and it would clog
# the stderr of the program

# To setup with lib config without using Client.run(), use discord.utils.setup_logging():

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
logging.getLogger("discord.http").setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename="debug.log",
    encoding="utf-8",
    maxBytes=32 * 1024 * 1024,  # 32 Mb
    backupCount=5,
)

dt_fmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

# Suppress the default configuration since we have our own
client.run(config.TOKEN, log_handler=None)

# Default configuration, outputs debug for everything the library outputs except https requests.

# TO-DO:
# Review and implement more advance layout https://docs.python.org/3/library/logging.html#module-logging
