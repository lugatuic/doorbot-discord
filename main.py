# This example requires the 'message_content' intent.

import discord
import datetime
import subprocess
import json
import open_door as door

with open ('secret.txt') as f:
   token = f.readline () 
client = discord.Bot ()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.slash_command(guild_ids=[408157484444811265, 652006495675875359, 833734451866763285])
async def open(message):
    if message.author == client.user:
        return
    await message.respond (f"Received door open request from {message.author}")

    allowed = False
    for r in message.author.roles:
        if (r.name == "Doorkeeper"):
            allowed = True

    if not allowed:
        await message.respond(f"Missing door role!")
        return
    door.openSolenoid()

    w = await message.respond(f"Hurry! The door is open!", ephemeral=True)
    for i in range(10):
        await w.edit(content=f"Hurry! The door is open for {10 - i} more seconds!")
        door.wait(1)

    await w.edit(content="Door is now closed!")
    door.closeSolenoid()
    await message.respond("Processed!")

    # try:
    #     subprocess.run (["./opendoor.sh"], check=True)
    #     await message.respond ("Door should have opened.")
    # except:
    #     await message.respond ("Error :(");
    #     return

    print (f"Opened door for {message.author} at {datetime.datetime.now()}")

client.run(token)
