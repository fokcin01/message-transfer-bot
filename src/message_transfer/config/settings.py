import os
from dotenv import load_dotenv


class DiscordBotSettings:
    def __init__(self):
        load_dotenv()

        self.discord_bot_token = os.getenv("DISCORD_BOT_TOKEN")
        self.database_path = os.getenv("DATABASE_PATH")
        self.log_level = os.getenv("LOG_LEVEL")

        self.validate()

    def validate(self):
        if not self.discord_bot_token:
            raise ValueError("DISCORD_BOT_TOKEN is missing")

        if not self.database_path:
            raise ValueError("DATABASE_PATH is missing")

        if not self.log_level:
            raise ValueError("LOG_LEVEL is missing")
