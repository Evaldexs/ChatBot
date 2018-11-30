import discord
from discord.ext import commands
import random
import requests
import urllib.request, json


""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """

class MapsCog:
    def __init__(self, client):
            self.client = client

    @commands.command()
    async def maps(self, ctx):


            # Using the GeoCode API from google
            url = 'https://maps.googleapis.com/maps/api/geocode/json?address=lhr&key=AIzaSyD9JtHb6csp8Evb27YCoH2EDTH5snKZtKQ'

            res = requests.get(url)

            data = res.json()

            status = data ['status']

            results = data ['results'][0][('formatted_address')]

            await ctx.send (data['status'])
            await ctx.send (data['results'][0][('formatted_address')])

def setup(client):
    client.add_cog(MapsCog(client))
