import discord
from discord.ext import commands
import random
import requests

""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """

class TylerCog:
    def __init__(self, client):
            self.client = client

    @commands.command()
    async def chuckNorris(self, ctx):

            # Using api.chucknorris.io/jokes API
            url = 'https://api.chucknorris.io/jokes/random'

            category = 'https://api.chucknorris.io/jokes/categories'

            icon_url = 'https://assets.chucknorris.host/img/avatar/chuck-norris.png'

            res = requests.get(url)

            data = res.json()

            category = data['category']
            value = data ['value']
            await ctx.send (data['value'])
            await ctx.send ("https://assets.chucknorris.host/img/avatar/chuck-norris.png")

def setup(client):
	client.add_cog(TylerCog(client))