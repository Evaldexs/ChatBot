import discord
from discord.ext import commands
import random

class TylerCog:
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def jokies(self, ctx):
    	jokes = ["What did the pig say to the cow? \n I don't want any beef lol", "What do you call a dog that does magic \n A Labracadabrador"]
    	joke = random.choice(jokes)
    	await ctx.send(joke)

def setup(client):
    client.add_cog(TylerCog(client))