import discord
from discord.ext import commands
import random

""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """
class AtanasCog:
	def __init__(self, client):
		self.client = client
		
	async def on_message(ctx,message):
		# Possible questions that user can input with what
		x = ["Hi","Hey","Sup","Greetings","Hello", "hi", "hey", "sup", "greetings", "hello"]

		a = ["What are you doing", "what are you doing" , "what are you doing?", "What are you doing?"]
		b = ["What kind of songs do you like","What kind of songs do you like?", "what kind of songs do you like", "what kind of songs do you like?"]
		c = ["What food do you like?", "What food do you like?", "what food do you like", "what food do you like?"] 
		d = ["What movies do you like", "What movies do you like?", "what movies do you like?", "what movies do you like"]
		e = ["What do you like to do in your free time", "What do you like to do in your free time?", "what do you like to do in your free time?","what do you like to do in your free time"]
		f = ["What is you'r favourite memory from your childhood","What is you'r favourite memory from your childhood?", ]
		g = ["What are you like?", "What are you like?", "what are you like", "what are you like?"]
		h = ["What was you favourite class in high-school", "What was you favourite class in high-school?", "what was your favourite class in high-school", "what was your favourite class in high-school"]
		i = ["What is the best party you have been to", "What is the best party you have been to?","what is the best party you have been to", "what is the best party you have been to?"]
		j = ["What is your favourite colour", "What is your favourite colour?" , "What's your favourite colour" , "What's your favourite colour?" , "what is your favourite colour?" , "what is your favourite colour?" , "what's your favourite colour" , "what's your favourite colour?"]
		k = ["What is your favourite sport" , "What is your favourite sport?" , "what is your favourite sport" , "what is your favourite sport?" , "what's your favourite sport" , "what's your favourite sport?" , "What's your favourite sport" "What's your favourite sport?"]
		l = ["What is your favourite fruit" , "What is your favourite fruit?" , "what is your favourite fruit" , "what is your favourite fruit?" , "What's your favourite fruit" , "What's your favourite fruit?" , "what's your favourite fruit" , "what's your favourite fruit?"]
		m = ["What is your favourite vegetable" , "What is your favourite vegetable?" , "what is your favourite vegetable" , "what is your favourite vegetable?" , "What's your favourite vegetable" , "What's your favourite vegetable?" , "what's your favourite vegetable" , "what's your favourite vegetable?"]
		n = ["What is your favourite season" , "What is your favourite season?" , "what is your favourite season" , "what is your favourite season?" , "What's your favourite season" , "What's your favourite season?" , "what's your favourite season" , "what's your favourite season?"]
		o = ["What is your favourite day of the week" , "What is your favourite day of the week?" , "what is your favourite day of the week" , "what is your favourite day of the week?" , "What's your favourite day of the week" , "What's your favourite day of the week?" , "what's your favourite day of the week" , "what's your favourite day of the week?"]
		p = ["What is your favourite song" , "What is your favourite song?" , "what is your favourite song" , "what is your favourite song?" , "What's your favourite song" , "What's your favourite song?" , "what's your favourite song" , "what's your favourite song?"]
		q = ["What hobby do you have" , "What hobby do you have?" , "what hobby do you have" , "what hobby do you have?"] 
		r = ["What is your favourite animal" , "What is your favourite animal?" , "what is your favourite animal" , "what is your favourite animal?" , "What's your favourite animal" , "What's your favourite animal?" , "what's your favourite animal" , "what's your favourite animal?"]
		s = ["What are you studying" , "What are you studying?" , "what are you studying" , "what are you studying?" , "What're you studying" , "What're you studying?" , "what're you studying" , "what're you studying?"]

		#Possible questions that user can input with where
		xx = ["Hey there!", "Hi hi!", "Greetings human!", "Sup"]

		aa = ["Where are you going?", "Where are you going" , "where are you going?" , "where are you going"]
		bb = ["Where is the toilet" , "Where is the toilet?" , "where is the toilet" , "where is the toilet?" , "Where's the toilet" , "Where's the toilet?" , "where's the toilet" , "where's the toilet?"]
		cc = ["Where do you workout" , "Where do you workout?" , "where do you workout" , "where do you workout?" ]
		dd = ["Where is the food" , "Where is the food?" , "where is the food" , "where is the food?" , "Where's the food" , "Where's the food?" , "where's the food" , "where's the food?"]
		ee = ["Where do you study" , "Where do you study?" , "where do you study" , "where do you study?"]
		ff = ["Where do you like going?" , "Where do you like going" , "where do you like going?" , " where do you like going"] 
		gg = ["Where do you live?" , "Where do you live" , "where do you live?" , "where do you live"]
		hh = ["Where are you from?" , "Where are you from" , "where are you from?" , "where are you from" , "Where're you from?" , "Where're you from" , "where're you form?"]
		ii = ["Where do you work?" , "Where do you work" , "where do you work?" , "where do you work"]
		jj = ["Where did you grow up?" , "Where did you grow up" , "where did you grow up?" , "where did you grow up"]

		if message.content in a:
			await message.channel.send ("I am listening to a song, and you?")
		elif message.content in x:
			random_xx = random.choice(xx)
			await message.channel.send(str(random_xx) + " , " + str(message.author) + ". How are you today?")
		elif message.content in b:
			await message.channel.send ("I like R&B! What about you?") 
		elif message.content in c:
			await message.channel.send ("I like fast food.")
		elif message.content in d: 
			await message.channel.send ("I like horror/action movies.")
		elif message.content in e:
			await message.channel.send ("I like going out and watching movies.") 
		elif message.content in f:
			await message.channel.send ("It was when I learned how to ride a bike.") 
		elif message.content in g: 
			await message.channel.send ("I am very outgoing and talkative.")
		elif message.content in h: 
			await message.channel.send ("My favourite class was programming.") 
		elif message.content in i:
			await message.channel.send ("The best party I have been was in my hometown.")
		elif message.content in j:
			await message.channel.send ("My favourite colour is blue.") 
		elif message.content in k:
			await message.channel.send ("I love basketball.")
		elif message.content in l:
			await message.channel.send ("My favourite fruit is banana.")
		elif message.content in m:
			await message.channel.send ("My favourite vegetable is tomato.")
		elif message.content in n:
			await message.channel.send ("I really enjoy the weather through the summer.") 
		elif message.content in o:
			await message.channel.send ("My favourite day of the week is Friday.")
		elif message.content in p:
			await message.channel.send ("My favourite song is by: Eminem - Not alike.") 
		elif message.content in r:
			await message.channel.send ("My favourite animal is Rhin.") 
		elif message.content in q:
			await message.channel.send ("I like being lazy all day long.")
		elif message.content in s:
			await message.channel.send ("I'm not studying, already finished everything :stuck_out_tongue_winking_eye: ")
		elif message.content in aa:
			await message.channel.send ("I can't go anywhere while Im chatting with you")
		elif message.content in bb:
			await message.channel.send ("Down the hall on the right side") 
		elif message.content in cc: 
			await message.channel.send ("I go to the closest gym")
		elif message.content in dd: 
			await message.channel.send ("It's in the fridge")
		elif message.content in ee:
			await message.channel.send ("I am studying in Coventry university")
		elif message.content in ff: 
			await message.channel.send ("I like being out") 
		elif message.content in gg: 
			await message.channel.send ("I live in Discord")
		elif message.content in hh: 
			await message.channel.send ("I am from the Internet")
		elif message.content in ii:
			await message.channel.send ("I am not working I study")
		elif message.content in jj:
			await message.channel.send ("I grew up in Stara Zagora")
		else:
			pass

def setup(client):
	client.add_cog(AtanasCog(client))