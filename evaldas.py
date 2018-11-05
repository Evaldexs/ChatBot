import discord
from discord.ext import commands
import requests


""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """
class EvaldasCog:
	def __init__(self, client):
		self.client = client

	@commands.command()
	@commands.guild_only()
	async def status(self, ctx ,member: discord.Member):
		if str(member.status) == "online":
			await ctx.send("{} is currently online, you can freely contact him now :grin: .".format(member))
		elif str(member.status) == "offline":
			await ctx.send("{} is currently offline, try to contact him later on :grimacing: .".format(member))
		elif str(member.status) == "idle" or str(member.status) == "dnd":
			await ctx.send("{} is currently idle or in do not disturb mode, better don't contact them now :sweat_smile: .".format(member))
		else:
			await ctxt.send("There is no such user")

	@commands.command()		
	async def weather(self, ctx, city: str):
		#Using apixu.com online weather API 
		url = 'http://api.apixu.com/v1/current.json?key=c1884e326807480a815194158182810&q={}'.format(city)

		res = requests.get(url)

		data = res.json()

		name = data['location']['name']
		temp_c = data['current']['temp_c']
		temp_f = data['current']['temp_f']
		wind_speedEU = data['current']['wind_kph']
		wind_speedUK = data['current']['wind_mph']
		latitude = data['location']['lat']
		longitude = data['location']['lon']
		description = data['current']['condition']['text']

		await ctx.send (f'Well... the current weather in {name} is:')
		await ctx.send (f'Temperature: {temp_c} °C')
		await ctx.send (f'Temperature: {temp_f} F\nWind speed: {wind_speedEU} km/h\nWind speed: {wind_speedUK} m/s\nDescription of the clouds: {description}')

def setup(client):
	client.add_cog(EvaldasCog(client))