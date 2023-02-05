import os

import discord

from dotenv import load_dotenv

import json

load_dotenv()

food_file = open(os.getenv('JSON_FILE_LOCATION'))

food_data = json.load(food_file)

LOCATION = os.getenv('CURRENT_LOCATION')
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents =  discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    message_str = str(message.content)
    if food_data["Location"] == LOCATION and message.content in food_data["Keywords"]:
        await message.channel.send(food_data.get("Restaurants"))
    else:
        await message.channel.send("No responses were found for your request")


client.run(TOKEN)

