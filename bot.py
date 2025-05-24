"""Bot module"""

import json
import discord
import actions

with open("settings.json", encoding="utf-8") as settings:
    settings = json.load(settings)

INVITE_URL = settings["invite_url"]
TOKEN = settings["token"]


def run_discord_bot():
    """Runs Botchy"""
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is now running!")
        print(f"The invite url is {INVITE_URL}")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        print(f'{message.author} said: "{message.content}" on #{message.channel}')

        await actions.execute(message)

    client.run(TOKEN)
