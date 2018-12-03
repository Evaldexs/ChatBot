import discord
from discord.ext import commands
import random
import requests
import urllib.request, json

""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """

class TylerCog:
    def __init__(self, client):
            self.client = client


    @commands.command()
    async def chucknorris(self, ctx):

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

    @commands.command()
    async def maps(self, ctx):


            # Using the GeoCode API from google
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=bhx&key=AIzaSyD9JtHb6csp8Evb27YCoH2EDTH5snKZtKQ'

            res = requests.get(url)

            data = res.json()

            status = data ['status']

            results = data ['results'][0][('formatted_address')]

            await ctx.send (data['status'])
            await ctx.send (data['results'][0][('formatted_address')])


def setup(client):
	client.add_cog(TylerCog(client))
