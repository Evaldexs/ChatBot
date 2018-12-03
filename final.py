import discord
from discord.ext import commands
import random
from urllib.request import urlopen
import json

initial_extensions = ['evaldas', 'atanas', 'finaru', 'tyler','qrow']

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
async def add(ctx, a: int, b: int):
    sum = a + b
    await ctx.send(f"Well let me think... I think the answer will be {sum}")

@client.command()
async def substract(ctx, a: int, b: int):
    sub = a - b
    await ctx.send(f"Well this is quite easy.. The answer will be {sub}")

@client.command()
async def divine(ctx, a: int, b: int):
    div = a/b
    await ctx.send(f"Well... my robotic knowledge tells me that the answer is {div}")

@client.command()
async def multiply(ctx, a: int, b: int):
    mul = a * b
    await ctx.send(f"Multiplying things is always hard... but I guess the answer will be {mul}")

@client.command()
async def power(ctx, a: int, b: int):
    pow = a**b
    await ctx.send(f"Well your answer will be: {pow}")


"""Command to shut down chat bot"""
@client.command()
async def logout(ctx):
        await client.logout()


client.run('Token goes here')
