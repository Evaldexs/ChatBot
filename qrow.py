import discord
from discord.ext import commands
import random

""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """
class QrowCog:
	def __init__(self, client):
		self.client = client
		
	async def on_message(ctx,message):
		# Possible questions that user can input with How
		x = ["Hi","Hey","Sup","Greetings","Hello", "hi", "hey", "sup", "greetings", "hello"]

		a = ["How are you", "how are you", "How are you?","how are you?"]
		b = ["How do you work", "how do you work", "How do you work?", "how do you work?"]
		c = ["How to finish my homework", "how to finish my homework", "How to finish my homework?", "how to finish my homework?"] 
		d = ["How to pass the exam", "how to pass the exam", "How to pass the exam?","how to pass the exam?"]
		e = ["How to find a free moive", "how to find a free moive", "How to find a free moive?", "how to find a free moive?"]
		f = ["How do you think about me", "how do you think about me", "How do you think about me?", "how do you think about me?"]
		g = ["How do you think about youself","how do you think about youself","How do you think about youself?","how do you think about youself?"]

		if message.content in a:
			await message.channel.send ("Great,What about you?")
		elif message.content in b:
			await message.channel.send ("That's a secret.") 
		elif message.content in c:
			await message.channel.send ("Hardworking,please!")
		elif message.content in d: 
			await message.channel.send ("Only you can help yourself.")
		elif message.content in e:
			await message.channel.send ("Please support genuine!") 
		elif message.content in f:
			await message.channel.send ("Not bad.") 
		elif message.content in g: 
			await message.channel.send ("I am just a virtual chatbot.")
		else:
			pass

def setup(client):
	client.add_cog(QrowCog(client))
