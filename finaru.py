import discord
from discord.ext import commands
import requests

#this part of the code is from the TMDb docs
from tmdbv3api import TMDb
tmdb = TMDb()
tmdb.api_key = '544c63d3985b02396b68e1db1f86b637'
from tmdbv3api import Movie

class FinaruCog:
    def __init__(self, client):
        self.client = client
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

    @commands.command()
    async def movies(self, ctx):
        await ctx.send("Giving you the most popular films")
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
        if message.content.startswith("/"):
            ok=1
        else:
            mylist=message.content.split()
            case=0
            no=0
            for words in mylist:
                def valid(words):
                    word = ""
                    for character in words:
                        if character.isalpha():
                            word+=character
                    return word
                word=valid(words)
                m = ["movie","movies"]
                ms = ["music", "song"]
                d = ["don't","dont","no"]
                if word.lower() in m:
                    case=1
                elif word.lower() in ms:
                    case=2
                elif word.lower() in d:
                    no=1
                else:
                    continue
            if no == 1 and case != 0:
                await message.channel.send("What else can I do for you?")
            else:
                if case == 1:
                    movie = Movie()
                    popular = movie.popular()
                    i=0
                    for p in popular:
                        if i<10:
                            await message.channel.send(str(i+1) + " : ")
                            await message.channel.send("ID: " + str(p.id) + "\n")
                            await message.channel.send("Title: " + str(p.title) + "\n")
                            await message.channel.send("Overview: " + str(p.overview) + "\n")
                            await message.channel.send("https://image.tmdb.org/t/p/w500" + p.poster_path + "\n")
                            i=i+1
                        else:
                            break
                elif case == 2:
                    await message.channel.send("Searching for songs \n")

def setup(client):
    client.add_cog(FinaruCog(client))