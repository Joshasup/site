import discord
import random
import ligmaUsers

client = discord.Client()


@client.event
async def on_ready():
    
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="!dicegod"))

##Josh Messages


@client.event
async def on_message(message):
    
    if message.author == client.user:
        return

    server = client.get_guild(280925621322776576)
    #help
    if message.content.startswith('!dicegod'):
      await message.channel.send("```\n!leeg / !league : Roll a 1d2 \n!addcustom (win/loss) @Name#1234 [message] : Adds a custom meessage to either win/loss responses\n```")
    #league of legends
    if message.content.startswith('!leeg') or message.content.startswith('!league') :
        ranNum = random.randint(0, 1)
        userDisplayName = message.author.display_name
        if ( ranNum == 0):
            await message.channel.send("```"+ userDisplayName +"'s Result: " + str(ranNum) + ", PLAYING```" + ligmaUsers.respondWin(message.author.id))
        else:
            await message.channel.send("```"+ userDisplayName +"'s Result: " + str(ranNum)  + ", NOT PLAYING```" + ligmaUsers.respondLoss(message.author.id))
    #addcustom
    if message.content.startswith('!addcustom'):
      contents = message.content.split(" ", 3)
      if (contents[1] == "win"):
        if (message.mentions):
          print(contents[2] + " " + "<@!"+str(message.mentions[0].id)+">")
          if (contents[2] == "<@!"+str(message.mentions[0].id)+">"):
            print("1")
            if (len(contents) == 4):
              print("2")
              print(contents[3])
              if (contents[3] != None and contents[3].isspace() == False):
                print("3")
                f = open("responseWins.txt", "a")
                f.write("\n" + str(message.mentions[0].id) + " "+ contents[3])
                f.close()
                ligmaUsers.addResponseWin(str(message.mentions[0].id), contents[3])
                print(ligmaUsers.responseWin)
                await message.channel.send("Added '*"+ contents[3] + "*' to **"+ message.mentions[0].display_name + "**'s win texts")
              else:
                await message.channel.send("Error in fourth argument, cant find custom message, format is '!addcustom (win/loss) @Name#ID 'custom message' ' ")
            else:
              await message.channel.send("Error in third argument, cant find user, format is '!addcustom (win/loss) @Name#ID 'custom message' ' ")
        else:
          
          await message.channel.send("Error in third argument, cant find user, format is '!addcustom (win/loss) @Name#ID 'custom message' ' ")

      elif (contents[1] == "loss"):
        if (message.mentions):
          print(contents[2] + " " + "<@!"+str(message.mentions[0].id)+">")
          if (contents[2] == "<@!"+str(message.mentions[0].id)+">"):
            print("1")
            if (len(contents) == 4):
              print("2")
              print(contents[3])
              if (contents[3] != None and contents[3].isspace() == False):
                print("3")
                f = open("responseLoss.txt", "a")
                f.write("\n" + str(message.mentions[0].id) + " "+ contents[3])
                f.close()
                ligmaUsers.addResponseLoss(str(message.mentions[0].id), contents[3])
                print(ligmaUsers.responseLoss)
                await message.channel.send("Added '*"+ contents[3] + "*' to **"+ message.mentions[0].display_name + "**'s loss texts")
              else:
                await message.channel.send("Error in fourth argument, cant find custom message, format is '!addcustom (win/loss) @Name#ID 'custom message' ' ")
            else:
              await message.channel.send("Error in third argument, cant find user, format is '!addcustom (win/loss) @Name#ID 'custom message' ' ")
        else:
          
          await message.channel.send("Error in third argument, cant find user, format is '!addcustom (win/loss) @Name#ID 'custom message' ' ")
      else:
         await message.channel.send("Error in second argument, format is '!addcustom (win/loss) @Name#ID 'custom message' ' ")

    if message.content.startswith('!propic'):
      await message.channel.send("https://cdn.discordapp.com/attachments/801002756428005387/813796825890816000/unknown.png")



client.run("ODEzNzIyMjQwNTIzOTYwMzQx.YDTb5A.MJ6elPxATCX4zCGirgH5TxJiP18")
