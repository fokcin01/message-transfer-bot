import discord
from discord.ext import commands
from message_transfer.config.settings import DiscordBotSettings
class DiscordBot (commands.Bot):
    def __init__(self, settings: DiscordBotSettings):

        self.settings = settings


        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(
            command_prefix="!",
            intents=intents
        )

    async def on_ready(self):
        print(f'We have logged in as {self.user}')