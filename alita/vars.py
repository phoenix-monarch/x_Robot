from os import getcwd

from prettyconf import Configuration
from prettyconf.loaders import EnvFile, Environment

env_file = f"{getcwd()}/.env"
config = Configuration(loaders=[Environment(), EnvFile(filename=env_file)])


class Config:
    """Config class for variables."""

    LOGGER = True
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    APP_ID = int(config("APP_ID", default=None))
    API_HASH = config("API_HASH", default=None)
    OWNER_ID = int(config("OWNER_ID", default=1198820588))
    MESSAGE_DUMP = int(config("MESSAGE_DUMP", default=None))
    DEV_USERS = [int(i) for i in config("DEV_USERS", default="").split()]
    SUDO_USERS = [int(i) for i in config("SUDO_USERS", default="").split()]
    WHITELIST_USERS = [int(i) for i in config("WHITELIST_USERS", default="").split()]
    DB_URI = config("DB_URI", default="")
    DB_NAME = config("DB_NAME", default="alita")
    NO_LOAD = config("NO_LOAD", default="").split()
    PREFIX_HANDLER = config("PREFIX_HANDLER", default="/").split()
    SUPPORT_GROUP = config("SUPPORT_GROUP", default="DivideSupport")
    SUPPORT_CHANNEL = config("SUPPORT_CHANNEL", default="DivideProjects")
    ENABLED_LOCALES = [str(i) for i in config("ENABLED_LOCALES", default="en").split()]
    WORKERS = int(config("WORKERS", default=16))
    BOT_USERNAME = ""
    BOT_ID = ""
    BOT_NAME = ""

