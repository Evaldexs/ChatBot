import discord
from discord.ext import commands
import random
import requests

""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """

class JokesCog:
    def __init__(self, client):
            self.client = client

    @commands.command()
    async def jokes(self, ctx):

            # Using api.chucknorris.io/jokes API
            url = 'https://safe-falls-22549.herokuapp.com/random_joke'

            res = requests.get(url)

            data = res.json()

            setup = data['setup']
            
            punchline = data ['punchline']

            await ctx.send (data['setup'])
            await ctx.send (data['punchline'])
def setup(client):
	client.add_cog(JokesCog(client))