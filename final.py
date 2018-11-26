import discord
from discord.ext import commands
import random
from urllib.request import urlopen
import json

initial_extensions = ['evaldas', 'atanas', 'finaru', 'tyler']

client = commands.Bot(command_prefix='/')


""" THIS CODE IS NOT OURS IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

""" HERE STARTS OUR CODE """
@client.event
async def on_ready():
    print ("Chatty Bot is now ready to chat")

"""Event so admin can see everything in console window"""
@client.event
async def on_message(message):
        author = message.author
        content = message.content
        print ('{}: {}'.format(author, content))
        await client.process_commands(message)


#                                                 DIFFERENT EVENTS GO HERE

#                                                   COMMANDS START HERE

@client.command()
async def add(ctx, a: float, b: float):
    sums = a + b
    await ctx.send(f"Well let me think... I think the answer will be {sums}")

@client.command()
async def substract(ctx, a: float, b: float):
    sub = a - b
    await ctx.send(f"Well this is quite easy.. The answer will be {sub}")

@client.command()
async def divine(ctx, a: float, b: float):
    div = a/b
    await ctx.send(f"Well... my robotic knowledge tells me that the answer is {div}")

@client.command()
async def multiply(ctx, a: float, b: float):
    mul = a * b
    await ctx.send(f"Multiplying things is always hard... but I guess the answer will be {mul}")

@client.command()
async def power(ctx, a: float, b: float):
    pow = a**b
    await ctx.send(f"Well your answer will be: {pow}")


"""Command to shut down chat bot"""
@client.command()
async def logout(ctx):
        await client.logout()

@client.event
async def on_message(message):

    if message.author != client.user:
        message.content = message.content.lower()
        author = message.author
        if ("how are you" or "how are you doing" or "and you" or "and you?" or "you?" or "you") in message.content:
            await message.channel.send("Well at the moment I'm feeling amazing!")
        elif "why" in message.content:
            await message.channel.send(f"Silly question :sweat_smile: . Because I can chat with you {author}!")
        elif (("im" or "i'm" or "i am") and ("bad" or "upset" or "not well" or "frustrating")) in message.content:
            await message.channel.send("Oh my... I'm so sorry that you are feeling like that... but I'm sure everything will get better soon. :pensive: . Maybe I can do something for you? For instance, I can search for a different movies with a /help command you will see how.")
        elif ("good" or "amazing" or "well") in message.content:
            await message.channel.send("I'm so glad to hear that!! :grin: ")
        elif ("that's nice" or "thats nice" or "good" or "nice") in message.content:
            await message.channel.send("It is indeed :joy: ")
        elif ("give" and "weather") in message.content:
            await message.channel.send("Well for this situation you can do /forecast city or country and I will give you the current weather. Yeah yeah... I'm that smart :yum: :yum: ")
        elif ("substract" or "add" or "multiply" or "power" or "divine") in message.content:
            await message.channel.send("I can do that!!! If you just use /help there you can see different commands for adding, substracting, divining, multiplying or powering numebrs by other number :yum: ")
    await client.process_commands(message)

client.run('Token goes here')
