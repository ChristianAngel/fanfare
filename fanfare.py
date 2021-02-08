import sys
import random
import time
import asyncio
import discord
from datetime import datetime, timedelta

token = "NzM1OTk5Mjc0ODMxMDUyODgz.XxobGQ.OrB6nd5aQKKgJ-gLNfkVNR2lqP4" # revoked token lul

philid = 634595009701871616

client = discord.Client()

@client.event
async def on_ready():
    print(client.user, "has connected to Discord!")
    await client.change_presence(activity=discord.Game("Mega Man Battle Network 5: Double Team DS"))
    for guild in client.guilds:
        foundUsers = set()
    
        print("Guild name:", guild.name)
        print("Guild ID:", guild.id)

        for voice_channel in guild.voice_channels:
            for member in voice_channel.members:
                if member.id == philid:
                    print("Found Philonous! Connecting...")
                    voice_client = await voice_channel.connect()
                    print("Skipping", len(sys.stdin.buffer.read(2000000)), "bytes...")
                    print("Connected. Playing stdin...")
                    audio_source = discord.FFmpegPCMAudio(sys.stdin, pipe=True, before_options=" -ac 2 -f s16le -ar 48000 ")
                    voice_client.play(audio_source)

    print("Done. Press ^C to disconnect.")
    try:
        await asyncio.sleep(30000)
    except:
        print("Disconnecting...")
        for voice_client in client.voice_clients:
            await voice_client.disconnect()
            
    print("Disconnected.")
    
    
client.run(token)
