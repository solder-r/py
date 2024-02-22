import os
import discord
import traceback
import asyncio
import sys
from discord.ext import commands
from keep_alive import keep_alive

def restart_script():
    print("Restarting bot...")
    python = sys.executable
    os.execl(python, python, *sys.argv)

class Bot(commands.Bot):
    def __init__(self, intents: discord.Intents, **kwargs):
        super().__init__(intents=intents, **kwargs)

    async def on_ready(self):
        try:
            print(f"Logged in as {self.user} ({self.user.id})")

            # Replace these channel IDs with the desired channels
            channel_ids = ["1199077734501077222"]

            while True:
                for channel_id in channel_ids:
                    channel = self.get_channel(channel_id)

                    if channel:
                        await channel.send("Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk Ksmk <@1197317124444672140><@1179439014261035143><@1197210349154336838> <@1188498708124418148><@1089244632900177981> <@1185236523591942297> <@783440952454152222> <@582020387726950414>")
                    else:
                        print(f"Channel with ID {channel_id} not found.")

                # Adjust the sleep duration (in seconds) based on your desired interval
                await asyncio.sleep(10)  # Sleep for 10 seconds between iterations

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            traceback.print_exc()

    async def on_disconnect(self):
        print("Disconnected. Reconnecting...")
        restart_script()

    async def on_error(self, event, *args, **kwargs):
        error_message = traceback.format_exc()
        print(f"Error in event {event}: {error_message}")

if __name__ == "__main__":
    try:
        # Get your bot token from environment variables
        token = os.environ.get("token")

        if not token:
            print("Bot token not found. Add it as an environment variable.")
        else:
            # Import the keep_alive module
            keep_alive()

            custom_intents = discord.Intents.default()
            custom_intents.message_content = True

            bot = Bot(custom_intents, command_prefix='!')
            bot.run(token)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        traceback.print_exc()
