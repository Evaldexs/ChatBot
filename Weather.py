import requests

def weather(city):

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

	print('The current weather in {} is'.format(name))
	print('Temperature: {} °C'.format(temp_c))
	print('Temperature: {} '.format(temp_f))
	print('Wind speed: {} k/h'.format(wind_speedEU))
	print('Wind speed: {} m/s'.format(wind_speedUK))
	print('Latitude: {} '.format(latitude))
	print('Longitude: {} '.format(longitude))
	print('Description of the clouds: {} '.format(description))
city = input('Your location name: ')
weather(city)
