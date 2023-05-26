import logging
import logging.handlers

# DEBUG REWORK IN PROGRESS

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
