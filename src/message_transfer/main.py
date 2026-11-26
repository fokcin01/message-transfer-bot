from message_transfer.config.settings import DiscordBotSettings
from message_transfer.adapters.discord.bot import DiscordBot

def main():
    discord_bot_settings = DiscordBotSettings()
    discord_bot = DiscordBot(discord_bot_settings)
    discord_bot.run(discord_bot_settings.discord_bot_token)

if __name__ == '__main__':
    main()