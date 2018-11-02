

def recommandations(message):
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
            if word.lower() in {"movie","movies"}:
                case=1
            elif word.lower() in {"music","song","songs"}:
                case=2
            elif word.lower() in {"don't","dont","no"}:
                no=1
            else:
                continue
        if no == 1 and case != 0:
            await message.channel.send("What else can I do for you?")
        else:
            if case == 1:
                await message.channel.send("Searching for movies")
            elif case == 2:
                await message.channel.send("Searching for songs")
