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

	@commands.command()		
	async def weather(self, ctx,city: str):


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

		sunny = ['Sunny']
		cloudy = ['Partly cloudy', 'Overcast']
		cloudy2 = ['Cloudy']
		rainy = ['Patchy rain possible', 'Patchy light rain', 'Light rain', 'Light rain shower','Light drizzle']
		heavyRain = ['Heavy rain at times', 'Heavy rain', 'Moderate or heavy freezing rain',  'Moderate or heavy rain shower', 'Moderate rain at times', 'Moderate rain', 'Torrential rain shower']
		rainFreezing = ['Light freezing rain']
		rainThunder = ['Patchy light rain with thunder', 'Moderate or heavy rain with thunder']
		snow = ['Patchy snow possible', 'Blowing snow', 'Patchy light snow', 'Light snow', 'Patchy moderate snow', 'Moderate snow', 'Patchy heavy snow', 'Heavy snow', 'Light snow showers', 'Moderate or heavy snow showers']
		snowThunder = ['Patchy light snow with thunder', 'Moderate or heavy snow with thunde']
		mistFog = ['Mist', 'Fog']
		thunders = ['Thundery outbreaks possible']

		'''
		await ctx.send (f'Well... the current weather in {name} is:')
		await ctx.send (f'Temperature: {temp_c} °C')
		await ctx.send (f'Temperature: {temp_f} F\nWind speed: {wind_speedEU} km/h\nWind speed: {wind_speedUK} m/s\nDescription of the clouds: {descriptions}')
		
		'''
		embed_weather = discord.Embed(

            title = (f'The current weather in {name} is just like this')

            )
		if description in cloudy:
			embed_weather.set_image(url =  'https://www.gov.gg/govgg1/images/weather/f.png')
			embed_weather.set_footer(text= "Ughh... why can't it be always sunny, right?")

		elif description in sunny:
			embed_weather.set_image(url =  'http://www.jmkxyy.com/weather-sun-icon/weather-sun-icon-18.jpg')
			embed_weather.set_footer(text= "YAY! It's sunny outside! Go and do stuff outside you lazy man!")

		elif description in cloudy2:
			embed_weather.set_image(url = 'https://www.clipartmax.com/png/middle/129-1293850_download-icon-mostly-cloudy-weather-icon.png')
			embed_weather.set_footer(text = "Unfortunately, it's going to be cloudy today... No sun for today")

		elif description in thunders:
			embed_weather.set_image(url = 'https://clip2art.com/images/thunder-clipart-cloudy-7.png')
			embed_weather.set_footer(text = "A thunderstorm is on patrol! Don't forget to turn off every electronic device!!")

		elif description in mistFog:
			embed_weather.set_image(url = 'https://cdn0.iconfinder.com/data/icons/weather-289/65/49-512.png')
			embed_weather.set_footer(text = "A mysterious fog or mist might shroud your precious city")

		elif description in rainy:
			embed_weather.set_image(url = 'https://cdn3.iconfinder.com/data/icons/chubby-weather/403/rain_less-512.png')
			embed_weather.set_footer(text = "Well... it's going to be rainy today, but not a heavy rain. However, I would rather choose an umbrella than nothing")

		elif description in heavyRain:
			embed_weather.set_image(url = 'https://cdn3.iconfinder.com/data/icons/chubby-weather/439/rain_heavy-512.png')
			embed_weather.set_footer(text = "HEAVY RAIN INCOMING!!! Don't forget your umbrella if you don't want to get wet")

		elif description in snow:
			embed_weather.set_image(url = 'https://vignette.wikia.nocookie.net/animal-jam-clans-1/images/6/6f/Snow-icon-46069.png/revision/latest?cb=20180305165847')
			embed_weather.set_footer(text = "Brrrrr... It's going to be cold today... Don't forget to put on warm clothes")

		elif description in rainThunder:
			embed_weather.set_image(url = 'https://cdn3.iconfinder.com/data/icons/weather-icons-1/64/Lightning_Rain-512.png')
			embed_weather.set_footer(text = "Oh my... I would rather stay at home and turn off every electronic device since it might be a thunderstorm nearby! However, if you are brave enough then don't forget to take an umbrella with you, it's rainy outside!")

		elif description in rainFreezing:
			embed_weather.set_image(url = 'https://www.clipartmax.com/png/small/92-927311_and-rain-and-snow-symbol.png')
			embed_weather.set_footer(text = "I would rather stay at home... But if you don't want to, better wear something warm because it's going to be a cold day! Oh.. and of course don't forget to bring an umbrella as well.")

		embed_weather.add_field(name = 'Temperature °C', value = '{}'.format(temp_c), inline = True )
		embed_weather.add_field(name = 'Temperature F', value = '{}'.format(temp_f), inline = True )
		embed_weather.add_field(name = 'Wind speed (km/h)', value = '{}'.format(wind_speedEU), inline = True )
		embed_weather.add_field(name = 'Wind speed (m/s)', value = '{}'.format(wind_speedUK), inline = True )
		await ctx.send(embed=embed_weather)

""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """
def setup(client):
	client.add_cog(EvaldasCog(client))
