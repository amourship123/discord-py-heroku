import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
print(TOKEN)
client = discord.Client()

prefix = ["Yui"]
petname = ["senpai"]

@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


      
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("Yui-chan help") or message.content.startswith(f"{prefix[-1]} help"):
        embed = discord.Embed(title = f"Hey, {petname[-1]}~", url = "https://sites.google.com/view/yui-chan/home", description = f"My documentation", color = 0xFF9CFC)
        await message.channel.send(embed=embed)

    if message.content.startswith("Yui-chan loli") or message.content.startswith(f"{prefix[-1]} loli"):
        await message.channel.send("FBI OPEN UP GO GO GO")

    if message.content.startswith("Yui-chan prefix ") or message.content.startswith(f"{prefix[-1]} prefix "):
        msg = message.content
        prefix.append(msg.split()[2])
        del prefix[0]
        await message.channel.send(f"The new prefix is {prefix[-1]}, but remember you can always use Yui-chan {petname[-1]}~")

    if message.content.startswith("Yui-chan call me ") or message.content.startswith(f"{prefix[-1]} call me"):
        msg = message.content
        petname.append(msg.split()[3])
        del petname[0]
        await message.channel.send(f"I'll call you {petname[-1]}~")

    if message.content.startswith("Yui-chan random hentai") or message.content.startswith(f"{prefix[-1]} random hentai"):
        embed = discord.Embed(title = f"Your hentai, {petname[-1]}~", url = "https://nhentai.net/random", description = f"Feeling adventurous? Why don't you feel adventurous with me later, {petname[-1]}~", color = 0xFF9CFC)
        await message.channel.send(embed=embed)

    if message.content.startswith("Yui-chan link ") or message.content.startswith(f"{prefix[-1]} link "):
        msg = message.content
        code = msg.split()[2]
        if len(code) == 6 and code.isnumeric() == True:
          hen = f"https://nhentai.net/g/{code}/"
          embed = discord.Embed(title = f"Your hentai, {petname[-1]}~", url = hen, description = f"Know what you like? Well, I know you'll like me, {petname[-1]}~", color = 0xFF9CFC)
          await message.channel.send(embed=embed)
        else:
          await message.channel.send(f"Please input a valid code, {petname[-1]}~")

    if message.content.startswith("Yui-chan search ") or message.content.startswith(f"{prefix[-1]} link "):
        msg = message.content
        first = msg.split()
        first.append("filer")
        term = first[2:-1]
        print(term)
        exact = ""
        print(exact)
        for i in term:
          exact = exact + i
          print(exact)
          exact = exact + "+"
          print(exact)
        print(exact)
        search = f"https://nhentai.net/search/?q={exact}"
        embed = discord.Embed(title = f"Your hentai, {petname[-1]}~", url = search, description = f"Looking for something? Please look all over me, {petname[-1]}~", color = 0xFF9CFC)
        await message.channel.send(embed=embed)
        
client.run(TOKEN)
