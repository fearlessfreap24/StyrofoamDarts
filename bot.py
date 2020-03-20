# bot.py
import os
import discord
from dotenv import load_dotenv

# load enviroment variables from .env file
load_dotenv()

# retrieve environment variables
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# create discord client to run event handling from discord guild
client = discord.Client()

# function to load cuss word dictionary from file
def loadCussWords():
    # open file read-only
    fs = open('cursewords.txt', 'r')

    # there's only one line in the file
    line = fs.readline()

    # separate the line by separator and create list
    line = line.split(', ')

    # return list
    return line

# global variable for list of cuss words
cusswords = loadCussWords()

# function to print information once connected to guild
@client.event
async def on_ready():
    # check if guild attached to is correct
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    # print bot name and guild name and number
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    # list guild members
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')


# function to read messages and parse for cuss words and react to cuss words.
@client.event
async def on_message(message):

    # make sure bot doesn't respond to bot posts
    if message.author == client.user:
        return

    # get the message, change to lower case and make it a list
    msg = message.content.lower().split()

    # iterate message list looking for cuss words.
    for word in msg:
        if word in cusswords:

            # log offender to terminal
            print(f'{word} {message.author}')

            # create response to offense and tag offender in response
            response = f'@{message.author} was shot in the foot'

            # post response
            await message.channel.send(response)
            break

        # exception handling
        elif message.content == 'raise-exception':
            raise discord.DiscordException

# run the client
client.run(TOKEN)
