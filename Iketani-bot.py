import json, re, discord, discord.utils
from discord.ext import commands


#declaring client
client = discord.Client()
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="You"))
    #await client.change_presence(activity=discord.Watching('Python3'))
#Read auth Token file
with open('foken.txt', 'r') as file:
    token = file.read()


def load_counters():
    with open('counters.json', 'r') as f:
       counters = json.load(f)
    return counters

def save_counters(counters):
    with open('counters.json', 'w') as f:
       json.dump(counters, f)


@client.event
async def on_message(message, case_insensitive=True):
    if message.content.lower() =='oof':
        counters = load_counters()
        counters["oof"] += 1
        channel = message.channel
        await channel.send(f'Another oof - Total: {str(counters["oof"])}')
        save_counters(counters)
    elif message.content.lower() == 'f':
        counters = load_counters()
        counters["f"] += 1
        channel = message.channel
        await channel.send(f'フ count - Total: {str(counters["f"])}')
        save_counters(counters)



client.run(token)
