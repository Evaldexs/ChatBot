import discord
from discord.ext import commands

""" THIS CODE IS NOT OURS CODE IT'S FROM THE INTERNET """
"""Source of the code: https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be """
class FinaruCog:
    def __init__(self, client):
        self.client = client
        
    async def on_message(ctx, message):
        mylist=message.content.split()
        case=0
        no=0
        pers=0
        for words in mylist:
            def valid(words):
                word = ""
                for character in words:
                    if character.isalpha():
                        word+=character
                return word
            word=valid(words)
            # Not in use atm
            #m = ["movie","movies"]
            #ms = ["music", "song", "songs"]
            #d = ["don't","dont","no"]
            if word.lower() == "movie":
                case=1
            elif word.lower() == "music":
                case=2
            elif word.lower() == "dont":
                no=1
            else:
                continue
        for i in range(2):
        	if no == 1 and case != 0:
        		await message.channel.send("What else can I do for you?")
        		break
        	else:
        		if case == 1:
        			await message.channel.send("Searching for movies")
        			break
        		elif case == 2:
        			await message.channel.send("Searching for songs")
        			break

def setup(client):
    client.add_cog(FinaruCog(client))