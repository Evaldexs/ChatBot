import discord
from discord.ext import commands
import requests

""" Twitter API docs : https://python-twitter.readthedocs.io/en/latest/index.html
    TMDb docs : https://www.themoviedb.org/documentation/api """


#this part of the code is from the twitter api docs
import twitter
api = twitter.Api('tncvlizYNuoPCFrc2BbKNn3bS','TP3ZAqe2NRigShnHeH2vKctgwlay01D27DOqcB4ugeyTDtsSoi','1061914001523818496-EgqAXwVpo8gJMkLoWVYz3alSRkYnNS','W7D0UbAj4OlPdsAgjHnkDVTDnpNsuS2hVDsKewF6rPbDz')
#here ends the part of the code from the twitter api docs

#this part of the code is from the TMDb docs
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '544c63d3985b02396b68e1db1f86b637'
from tmdbv3api import Movie
#here ends the part of the code from TMDb docs

""" The next three lines ar from the internet. 
Source : https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """

class FinaruCog:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def toptweets(self, ctx, name: str):
        #using Twitter API
        await ctx.send("Giving you the latest 5 tweets on the following : #" + name)
        results = api.GetSearch(raw_query="l=en&q=%23" + name + "%20&result_type=recent&since=2014-07-19&count=6")
        for result in results:
            await ctx.send("The tweet was created at " + result.created_at)
            await ctx.send("https://twitter.com/" + str(result.user.id) + "/status/" + str(result.id_str))
            #await ctx.send(result.id)
            #await ctx.send(result.id_str)
            #await ctx.send(result.text)
            #await ctx.send(result.user)
            #await ctx.send(result.entities)
        
    
    @commands.command()
    async def movie(self, ctx, name: str):
        #using TMDb API
        await ctx.send("Searching for 5 similar matches for " + name)
        movie = Movie()
        search = movie.search(name)
        i=0
        for result in search:
            if i<5:
                mid = result.id
                similar = movie.similar(mid)
                for results in similar:
                    if i<5:
                        await ctx.send(results.title + "\n")
                        await ctx.send(results.overview + "\n")
                        await ctx.send("https://image.tmdb.org/t/p/w500" + results.poster_path + "\n")
                        i= i+1

    
    async def movies(self, ctx):
        #using TMDb API
        await ctx.send("Giving you the most popular movies")
        movie = Movie()
        popular = movie.popular()
        i=0
        for p in popular:
            if i<10:
                await ctx.send(str(i+1) + " : ")
                await ctx.send("ID: " + str(p.id) + "\n")
                await ctx.send("Title: " + str(p.title) + "\n")
                await ctx.send("Overview: " + str(p.overview) + "\n")
                await ctx.send("https://image.tmdb.org/t/p/w500" + p.poster_path + "\n")
                i=i+1
            else:
                break
    
    async def on_message(ctx, message):
        if (message.author.bot == False):
            if message.content.startswith("/") == False:
                mylist=message.content.split()
                case=0
                no=0
                sim=0
                for words in mylist:
                    def valid(words):
                        word = ""
                        for character in words:
                            if character.isalpha():
                                word+=character
                        return word
                    word=valid(words)
                    m = ["movie","movies","film"]
                    d = ["don't","dont","no"]
                    if word.lower() in m:
                        case=1
                    elif word.lower() in d:
                        no=1
                    elif word.lower() == "similar":
                        sim=1
                    else:
                        continue
                if no == 1 and case != 0:
                    await message.channel.send("What else can I do for you?")
                else:
                    if case == 1:
                        if sim == 0:
                            await ctx.movies(message.channel)
                        else:
                            await message.channel.send("If you want a similar match for a certain movie, use the '/movie name' command and I'll give you 5 similar matches for your movie")

def setup(client):
    client.add_cog(FinaruCog(client))
