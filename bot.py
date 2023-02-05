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
    mentioned_keywords = [] 
    
    if food_data["Location"] == LOCATION:
        for word in message.content.split(" "):
            if word in food_data["Keywords"]:
                mentioned_keywords.append(word)
        if len(mentioned_keywords) > 0:
            await message.channel.send("Here are some options for {} near {}:".format(mentioned_keywords, LOCATION))
            await message.channel.send(food_data.get("Restaurants"))
        else:
            await message.channel.send("No responses were found for your request.")




client.run(TOKEN)

