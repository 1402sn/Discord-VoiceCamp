# Importing Modules.
from discord.ext import commands
import discord
from colorama import Fore
from keep_alive import keep_alive
from os import environ
import json

bot = commands.Bot("!", self_bot=True) # Defining bot.

@bot.event # Turning the bot online.
async def on_ready():
    print("This program has logged in to the account " + Fore.YELLOW + f"{bot.user}.\n")
    with open("data.json", "r") as f:
        data = json.load(f)
    if data["guild"] == None or data["channel"] == None:
        pass
    else:
        try:
            voice_channel = discord.utils.get(bot.get_guild(int(data["guild"])).channels, id = int(data["channel"]))
            await voice_channel.connect()
            print(f"{Fore.GREEN}[-]{Fore.WHITE} Connected to {Fore.CYAN}{voice_channel} {Fore.WHITE}in {Fore.CYAN}{voice_channel.guild}{Fore.WHITE}.")
        except:
            print(f"{Fore.RED} [ - ] Error Occured. Please reconnect using commands.")

@bot.command() # Join command.
async def join(ctx, voice_channel : discord.VoiceChannel):
    await voice_channel.connect()
    data = {"guild":str(ctx.guild.id),"channel":str(voice_channel.id)}
    with open("data.json", "w") as f:
        json.dump(data, f)
    print(f"{Fore.GREEN}[-]{Fore.WHITE} Connected to {Fore.CYAN}{voice_channel} {Fore.WHITE}in {Fore.CYAN}{voice_channel.guild}{Fore.WHITE}.")
    await ctx.message.delete()

@bot.command() # Leave command.
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()
    with open("data.json", "w") as f:
        json.dump({"guild":None,"channel":None}, f)
    print(f"{Fore.RED}[-]{Fore.WHITE} Disconnected from {Fore.CYAN}{voice_client.channel}{Fore.WHITE} in {Fore.CYAN}{ctx.message.guild}{Fore.WHITE}.")
    await ctx.message.delete()

keep_alive()
bot.run(environ["OTU0NTMzMTAwNTczMDY1MjI2.G6UVoD.pvIztZ33M30lkk03OiQc9emSjCpXl9VmoWGyLo"], bot=False) # Run the bot by adding your token in between the quotes.
