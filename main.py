# This example requires the 'message_content' intent.

import discord
import datetime
import subprocess
import json

with open ('secret.txt') as f:
   token = f.readline () 
client = discord.Bot ()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.slash_command(guild_ids=[408157484444811265, 652006495675875359])
async def open(message):
    if message.author == client.user:
        return
    try:
        subprocess.run (["./opendoor.sh"])
        await message.respond ("Door should have opened.")
        print (f"Opened door for {message.author} at {datetime.now()}")
    except:
        await message.respond ("Error :(");

client.run(token)
