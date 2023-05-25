#IMPORTING NEEDED LIBRARIES AND SETTING UP THE CLIENT
import discord
import os
import random
from discord.ext import commands
import math
import datetime
from keepalive import keep_alive
from sympy import *
import asyncio
import requests
import mpmath
from bs4 import BeautifulSoup
from autocorrect import Speller
import numpy as np
from translate import Translator
from chempy import balance_stoichiometry

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
spell = Speller(lang='en')
client = commands.Bot(
    intents=intents,
    command_prefix=['pmat', 'pt', 'pr', 'pc', 'pp', 'pd', 'ps', 'pb'])
cookies = {}

#CODE
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Type p;help"))


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        return
    msg = message.content
    author = message.author

    #INTEGRAL CALCULATOR
    if message.content.startswith('pmathintegral'):
        try:
            words = message.content.split(None, 1)
            x = symbols('x')
            result = integrate(words[1], x)
            await message.channel.send(f"**Result:** ```{result}```")
        except IndexError:
            await message.channel.send(
                "No function to integrate. Please enter a function to integrate and try again! Use ``p;info integral`` to learn how to use this feature."
            )
          
    if message.content.startswith('!poll'):
        poll_data = message.content[5:].split('/')
        poll_question = poll_data[0]
        poll_options = [option.strip() for option in poll_data[1:]]
        poll_message = '**{}**\n\n'.format(poll_question)
        for i, option in enumerate(poll_options):
            poll_message += '{}️⃣ {}\n'.format(i + 1, option)
        poll = await message.channel.send(poll_message)
        for i in range(len(poll_options)):
            reaction = '️️️️️️{}️⃣'.format(i + 1)
            await poll.add_reaction(reaction)
    words = message.content.split()

    if message.content.startswith("Hello"):
        await message.channel.send(
            f"""Hello {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith("hello"):
        await message.channel.send(
            f"""Hello {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith("HELLO"):
        await message.channel.send(
            f"""Hello {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith("hola"):
        await message.channel.send(
            f"""Hola {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith("Hola"):
        await message.channel.send(
            f"""Hola {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith("HOLA"):
        await message.channel.send(
            f"""Hika {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('howdy'):
        await message.channel.send(
            f"""Howdy {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('🤠')
    if message.content.startswith('Howdy'):
        await message.channel.send(
            f"""Howdy {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('🤠')
    if message.content.startswith('HOWDY'):
        await message.channel.send(
            f"""Howdy {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('🤠')
    if message.content.startswith('heya'):
        await message.channel.send(
            f"""Heya {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('Heya'):
        await message.channel.send(
            f"""Heya {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('HEYA'):
        await message.channel.send(
            f"""Heya {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('heyo'):
        await message.channel.send(
            f"""Heyo {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('Heyo'):
        await message.channel.send(
            f"""Heyo {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('HEYO'):
        await message.channel.send(
            f"""Heyo {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('hewwo'):
        await message.channel.send(
            f"""Hewwo {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('Hewwo'):
        await message.channel.send(
            f"""Hewwo {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('HEWWO'):
        await message.channel.send(
            f"""Hewwo {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('p;Hi'):
        await message.channel.send(
            f"""Hi {author.mention}! To check out my commands please type ``p;help``. I Hope you have a great day!"""
        )
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('p;hi'):
        await message.channel.send(
            f"""Hi {author.mention}! To check out my commands please type ``p;help``. I Hope you have a great day!"""
        )
    if message.content.startswith('hey'):
        await message.channel.send(
            f"""Hey {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('Hey'):
        await message.channel.send(
            f"""Hey {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('HEY'):
        await message.channel.send(
            f"""Hey {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if any(word in msg for word in sad):
        await message.channel.send(random.choice(encouraging_words))
    if words[0].lower() == 'kitty':
        await message.channel.send('meow :cat:')
        await message.add_reaction('\U0001F431')
    if words[0].lower() == 'cat':
        await message.add_reaction('\U0001F431')
        await message.channel.send('meow :cat:')
    if words[0].lower() == 'meow':
        await message.add_reaction('\U0001F431')
        await message.channel.send('meow :cat:')
    if message.content.startswith('p;cookie'):
        if len(message.mentions) == 0:
            await message.channel.send(
                'You need to mention a user to give a cookie to!')
        else:
            user = message.mentions[0]
            if client.user in message.mentions:
                await message.channel.send(
                    f'Aww, thank you for the cookie, {message.author.mention}! :cookie:'
                )
            else:
                await message.channel.send(
                    f':cookie: {message.author.mention} has given a cookie to {user.mention}! :cookie:'
                )
    if message.content.startswith('p;hug'):
        embed = discord.Embed(
            title="",
            description=f'''{author.mention} Here is a hug for you :)''',
            color=0xe78be7)
        embed.set_image(url=random.choice(hug_gif))
        embed.set_footer(text="Hope you have a great day :D")
        await message.channel.send(embed=embed)

    if message.content.startswith('p;cat'):
        embed = discord.Embed(title="",
                              description=f'''Meow :cat:''',
                              color=0xe78be7)
        embed.set_image(url=random.choice(cat_images))
        embed.set_footer(text="Hope you have a great day =^-^=")
        await message.channel.send(embed=embed)
      
    if message.content.startswith('bye'):
        await message.channel.send(
            f'''Bye {author.mention}! Hope you have a great rest of your day!'''
        )
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('Bye'):
        await message.channel.send(
            f'''Bye {author.mention}! Hope you have a great rest of your day!'''
        )
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('BYE'):
        await message.channel.send(
            f'''Bye {author.mention}! Hope you have a great rest of your day!'''
        )
        await message.add_reaction('\U0001F44B')

    if message.content.startswith('p;flip'):
        embed = discord.Embed(title="",
                              description=random.choice(coin_outcomes))
        await message.channel.send(embed=embed)
        await message.add_reaction('\U0001FA99')
    if message.content.startswith('P;flip'):
        embed = discord.Embed(title="",
                              description=(random.choice(coin_outcomes)))
        await message.channel.send(embed=embed)
        await message.add_reaction('\U0001FA99')
    if message.content.startswith('p;roll'):
        embed = discord.Embed(title="", description=random.choice(dice_roll))
        await message.channel.send(embed=embed)
    if message.content.startswith('p;Roll'):
        await message.channel.send(random.choice(dice_roll))

    if message.content.startswith('gn'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('goodnight'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('Goodnight'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('good night'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('Good night'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('Good Night'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('Gn'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('GN'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('GOODNIGHT'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good night & sweet dreams! :sleeping:')
    if message.content.startswith('p;about'):
        await message.channel.send('''Hello! 
            
My name is Pixel and I am a Discord bot full of random interesting commands and features. I am written using multiple libraries in Python, and can perform various functions such as calculations, setting reminders, sending cat images, playing games, and much more! Type ``p;help`` to get a list of all my commands! Additionally you can type ``p;info <command name>`` to get more information on a specific command from my list of commands!

Thanks for checking me out and I hope you have a nice day :)

~ Meow :cat:''')
    if message.content.startswith('p;ping'):
        await message.channel.send(
            f'**:ping_pong: Bot latency**: {client.latency * 10000} ms')

    if words[0].lower() == 'gm':
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good morning! Hope you have a great day :sunny:')
    if words[0].lower() == 'goodmorning':
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good morning! Hope you have a great day :sunny:')
    if message.content.startswith('good morning'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good morning! Hope you have a great day :sunny:')
    if message.content.startswith('Good morning'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good morning! Hope you have a great day :sunny:')
    if message.content.startswith('p;binary'):
        decimal = int(message.content.split(' ')[1])
        binary = bin(decimal)[2:]
        await message.channel.send(
            f'The binary equivalent of {decimal} is: **{binary}**.')
    if message.content.startswith('p;wyr'):
        embed = discord.Embed(title='Would you rather...',
                              description=random.choice(wyr_questions),
                              color=0xFF6600)
    if message.content.startswith('p;tod'):
        embed = discord.Embed(title=random.choice(random_tod),
                              description='Truth or Dare',
                              color=0xFF6600)
        await message.channel.send(embed=embed)
    if message.content.startswith('p;fact'):
        embed = discord.Embed(title="Did you know...",
                              description=random.choice(random_facts),
                              color=0xadd8e6)
        await message.channel.send(embed=embed)
    if message.content.startswith('p;trivia'):
        await message.channel.send(random.choice(trivia_questions))
    if message.content.startswith('I appreciate pixel'):
        await message.channel.send('Aww! I appreciate you too :blush:')
    if message.content.startswith('i appreciate pixel'):
        await message.channel.send('Aww! I appreciate you too :blush:')
    if message.content.startswith('p;truth'):
        embed = discord.Embed(title=random.choice(truth_questions_only),
                              description='Type: Truth',
                              color=0x008000)
        await message.channel.send(embed=embed)
    if message.content.startswith('p;dare'):
        embed = discord.Embed(title=random.choice(dare_questions_only),
                              description='Type: Dare',
                              color=0xFF0000)
        await message.channel.send(embed=embed)
    if message.content.startswith('I appreciate Pixel'):
        await message.channel.send('Aww! I appreciate you too :blush:')
    if message.content.startswith('i appreciate Pixel'):
        await message.channel.send('Aww! I appreciate you too :blush:')
    if message.content.startswith('p;countchar'):
        text = message.content.split(' ', 1)[1]
        count = len(text)
        await message.channel.send(
            f'The text "{text}" has **{count}** characters.')
    if message.content.startswith('p;autocorrect'):
        text = message.content.split(' ', 1)[1]
        corrected = spell(text)
        if corrected != text:
            await message.channel.send(
                f'Here is the corrected text: **{corrected}**')
        else:
            await message.channel.send('No errors found in the given text.')
    if client.user in message.mentions:
        await message.channel.send(
            f"Hi {author.mention}! To check out my commands please type ``p;help``. I Hope you have a great day!"
            "")
    if message.content.startswith('p;solve '):
        try:
            function = message.content.split('p;solve ')[1]
            x = symbols('x')
            solution = solve(function, x)
            solution_string = '\n'.join([f'{x} = {sol}' for sol in solution])
            await message.channel.send(
                f'Solutions to the function ``{function}`` are:```{solution_string}```'
            )
        except:
            await message.channel.send(
                'Invalid input or syntax. Please try again.')
    if message.content.startswith("p;8ball"):
        await message.channel.send(random.choice(list_eight_ball))

#INFORMATION COMMANDS FOR EACH OF THE BOT COMMANDS

    if message.content.startswith('p;info help'):
        embed = discord.Embed(title="__**help**__ :pencil:",
                              description='''
Use this command to get a list of commands with a brief description of their function.
                            
__**Syntax**__
p;help''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info 8ball'):
        embed = discord.Embed(title="__**8ball**__ :8ball:",
                              description='''
Ask the bot a (yes/no style) question and it will provide you with a reply using it's 8ball!
                            
__**Syntax**__
p;8ball''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info solve'):
        embed = discord.Embed(title="__**solve**__ :abacus:",
                              description='''
Use this command to find the solution to any equation of the form ``f(x) = 0``. For example, if the user wishes to find solutions to the equation ``x^2 + 2x + 1 = 0``, they must type ``p;solve x**2 + 2*x + 1`` and the bot will respond with the solutions to the equation. If the user wishes to solve the equation ``3^x = 9``, they must type ``p;solve 3**x - 9`` and the bot will repsond with the solutions to the function. Note: The bot as of now can only solve single variable functions. 
                            
__**Syntax**__
p;solve''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info binary'):
        embed = discord.Embed(title="__**binary**__ :zero: :one:",
                              description='''
This commands takes in a base 10 (decimal) integer as the input and outputs the binary forms of the integer. 
                            
__**Syntax**__
p;binary''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info autocorrect'):
        embed = discord.Embed(title="__**autocorrect**__ :white_check_mark:",
                              description='''
Use this command to fix any potential issues with a given text. The command takes a given text as an input and returns a(n) (auto)corrected version of the text free of any spelling errors. Note, the command will not successfully work 100% of the times and can cause issues thus looking at the correct version and making a decision about if or not it is the desired output might be necessary if needed. 
                            
__**Syntax**__
p;autocorrect''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info countchar'):
        embed = discord.Embed(title="__**count characters**__ :1234:",
                              description='''
Use this command to get a count of characters in a given text. To use this command, the user must type ``p;countchar`` followed by the text the want to find the count of characters for. For example if a user wishes to find the number of characters in the text "Hello Pixel," they must type ``p;countchat Hello Pixel`` and the bot will then respond with the number of characters in the given text.                                               
__**Syntax**__
p;countchar''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info psearch'):
        embed = discord.Embed(title="__**search**__ :mag_right:",
                              description='''
This command returns the first few results (upto 5) realted to a query inputted by the user. To use this command the user must type ``psearch`` followed by the topic the hope to find search results for. For example if a user wants search results for cats, they must time ``psearch cat`` and the bot will return the first few web search results it is able to fetch relating to cats. 
                            
__**Syntax**__
psearch''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info ppoll'):
        embed = discord.Embed(title="__**poll**__ :ballot_box:",
                              description='''
Use this command to create a poll with a question and upto 10 options. For example, if the user wishes to ask the question: "What is the best animal?", with the options: "Cats Dogs Lions Tigers", then they must type ``ppoll What is the best animal? Cats Dogs Lions Tigers`` and the bot will create a poll with reactions for members to be able to react and show their choice. For yes or no style questions, the user must type "yes" or "no" as the options. For example: ``ppoll Should I get a haircut? Yes No``. 
                          
__**Syntax**__
ppoll''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pdefine'):
        embed = discord.Embed(title="__**define**__ :book:",
                              description='''
Use this command to find the definiton of any word in the english langauge. For example, if the user wishes to find the definition of the word "dessert", then the user must type ``pdefine dessert`` and the bot will reply with the definition of the word "dessert". 
                            
__**Syntax**__
pdefine''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith("p;info pmathgcd"):
        embed = discord.Embed(
            title="__**math: greatest common divisor**__ :asterisk:",
            description=
            '''This command can be used to calculate the greatest common divisor (gcd) of two numbers. To use this command, the user must type ``pmathgcd`` and then the two numbers they desire to calculate the gcd for. For example if a user wishes to find the gcd of ``4`` and ``2`` they must type ``pmathgcd 4 2`` and the bot will respond with the result which is ``2``.

__**Syntax**__
pmathgcd''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info dm help'):
        embed = discord.Embed(title="__**dm help**__ :calling:",
                              description='''
Use this command to get a list of commands with a brief description of their function, sent to you in a direct message (DM)
                            
__**Syntax**__
p;dm help''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info about'):
        embed = discord.Embed(title="__**about**__ :cat:",
                              description='''
Give me a chance to tell you a little about me!

__**Syntax**__
p;about''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info ping'):
        embed = discord.Embed(title="__**ping**__ :ping_pong:",
                              description='''
Use this command to see the real-time latency (response time) of pixel.
                            
__**Syntax**__
p;ping''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info hi'):
        embed = discord.Embed(
            title="__**hi**__ :wave:",
            description='''Say hi to me for a greeting in return :)
                            
__**Syntax**__
p;hi''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info hug'):
        embed = discord.Embed(
            title="__**hug**__ :people_hugging:",
            description=
            '''A hug from pixel for the user! Everyone deserves a hug, hope this makes your day better! :D
                            
__**Syntax**__
p;hug''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info cat'):
        embed = discord.Embed(
            title="__**random cat**__ :cat2:",
            description=
            '''Using this command sends a random cat image or GIF in the chat. Cats are awesome :3

__**Syntax**__
p;cat
''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info flip'):
        embed = discord.Embed(
            title="__**flip**__ :coin:",
            description=
            '''Flips a fair 2-sided coin, and gives the output as heads or tails. So what is your call, heads or tails?

__**Syntax**__
p;flip''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info roll'):
        embed = discord.Embed(
            title="__**roll**__ :game_die:",
            description=
            '''Rolls a fair 6-sided game dice and gives the output in the form of the numerical result of the dice roll. So what number do you think it is going to be?

__**Syntax**__
p;roll''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathadd'):
        embed = discord.Embed(
            title="__**math: addition**__ <:addition:982883419774140436>",
            description=
            '''Followed by the function (``pmathadd``), the user must input all the numeric values and pixel will give an output as the sum of the numeric values. For example: ``pmathadd 10 5`` <-- this will result in Pixel giving an output of 15.0, which is the sum of 10 and 5 when added. Another example: ``pmathadd 23412 14234 12223``` <-- will result in Pixel giving an output of 49869.0, which is the sum of the three numbers.  

__**Syntax**__
pmathadd''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info fact'):
        embed = discord.Embed(
            title="__**fact**__ :books:",
            description=
            '''Tells you a random fact, because who doesn't enjoy a random cool fact :)

__**Syntax**__
p;fact''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathsubtract'):
        embed = discord.Embed(
            title="__**math: subtraction**__ <:subtraction:982885939686813717>",
            description=
            '''Followed by the function (``pmathsubtract``), the user must input as many numeric values as they wish to substract, and Pixel will give an output as the difference of the numeric values (ex. ``pmathsubtract 10 5`` <-- this will result in pixel giving an output of 5, which is the difference between 10 and 5).

__**Syntax**__
pmathsubtract''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathdivide'):
        embed = discord.Embed(
            title="__**math: division**__ <:division:982888820666167306>",
            description=
            '''Followed by the function (``pmathdivide``), the user must input two numeric values and pixel will give an output as the quotient of the two values (ex. ``pmathdivide 10 5`` <-- this will result in pixel giving an output of 2, which is the quotient when 10 is divided by 5).

__**Syntax**__
pmathdivide''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathpi'):
        embed = discord.Embed(
            title="__**math: pi**__ :pie:",
            description=
            '''This command allows the user to ask the bot to send the first ``n`` digits of pi. To use this command, the user must first type ``pmathpi`` and then followed by the digits of pi the desire to be sent by the bot. For example if a user wants the first 100 digits of pi, then they must type ``pmathpi 100`` and the bot will then respond with the first 100 digits of pi. No more than 1000 digits can be requested.

__**Syntax**__
pmathpi''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathmultiply'):
        embed = discord.Embed(
            title=
            "__**math: multiplication**__ <:multiplication:982890472886382632>",
            description=
            '''Followed by the function (``pmathmultiply``), the user must input as many numeric values as they wish to multiply and pixel will give an output as the product of the numeric values (ex. ``pmathmultiply 10 5`` <-- this will result in pixel giving an output of 50, which is the product when 10 is multiplied by 5).

__**Syntax**__
pmathmultiply''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathexp'):
        embed = discord.Embed(
            title='__**math: exponent**__ <:exponent:982926856103796736>',
            description=
            '''Followed by the function (``pmathexp``), the user must input two numeric values and pixel will give the output as the result where the first value is the base and the second value is the exponent (ex. ``pmathexp 2 4`` <-- this will result in pixel giving an output of 16, which is the result when 2 is raised to 4).
                            
__**Syntax**__
pmathexp''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pcountdown'):
        embed = discord.Embed(
            title='__**countdown...**__ :hourglass_flowing_sand:',
            description=
            '''Allows the user to set a countdown timer for ``x`` amount of seconds. For example, if a user wants to set a timer for ``30`` seconds, the user can type ``pcountdown 30`` and the bot will display a message that shows the remaining time left in the countdown and will ping the user when the countdown is over.
                            
__**Syntax**__
pcountdown''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info cookie'):
        embed = discord.Embed(
            title='__**cookie**__ :cookie:',
            description=
            '''Allows the user to send a cookie to another user/bot in the server. The user can also give themselves a cookie. Sharing is caring and sharing the sweetness of cookies with everyone in the server is great! So share cookies with your server members and enjoy :)
                            
__**Syntax**__
p;cookie''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathfactorial'):
        embed = discord.Embed(
            title='__**math: factorial**__ <:factorial:982929962946424862>',
            description=
            '''Followed by the function (``pmathfactorial``), the user must input one numeric value and pixel will give the output as the factorial of the inputted value (ex. ``pmathfactorial 4`` <-- this will result in pixel giving an output of 24, which is the factorial of 4).
                            
__**Syntax**__
pmathfactorial''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathsqrt'):
        embed = discord.Embed(
            title='__**math: square root**__ <:squareRoot:982932222820614194>',
            description=
            '''Followed by the function (``pmathsqrt``), the user must input one numeric value and pixel will give the output as the result of the sqaure root of the inputted value (ex. ``pmathsqrt 4`` <-- this will result in pixel giving an output of 2, which is the sqaure root of 4).
                            
__**Syntax**__
pmathsqrt''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info premindme'):
        embed = discord.Embed(
            title='__**remind me!**__ :timer:',
            description=
            '''The ``premindme`` command allows the user to set a reminder for themselves for any amount of time they desire to. To use this command, the user must first type ``premindme`` and then follow it by the amount of time and units and the reminder they want to set. An example of this would be: ``premindme 10 minutes go for a walk``, the bot will ping the user after 10 minutes reminding them that they need to go for a walk. Note that only the following units are acceptable and in must be written in the command in the following manner only: ``seconds``, ``seconds``, ``minute``, ``minutes``, ``hour``, ``hours``, ``day``, ``days``. The case of the input does not matter (i.e. the bot will accept: Second, SeCONds, SeconD, so the case of the letters in the input does not matter). 
          
__**Syntax**__
premindme''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathlog'):
        embed = discord.Embed(
            title='__**math: logrithm**__ :wood:',
            description=
            '''Followed by the function (``pmathlog``), the user must input two numeric values and pixel will give the output as the result of a logrithm where the first inputted value is what we want to find the logrithm of, and the second inputted value is the base of the logrithm. (ex. ``pmathlog 4 2`` <-- this will result in pixel giving an output of 2, which is the logrithmic value given that 4 is the value we want to find the logirthm for and 2 is the base).
                            
__**Syntax**__
pmathlog''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathintegral'):
        embed = discord.Embed(
            title='__**math: integral**__ :man_teacher:',
            description=
            '''Followed by the function (pmathintegral), the user must input some mathemtaical function f(x) for which they wish to find the integral of. Here are ways to interpret the result: For example if the user inputs the function `x`, the output will be `x**2/2` which means `x` to the second power, divided by two                        

__**Syntax**__
pmathintegral''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info tod'):
        embed = discord.Embed(
            title='__**truth or dare...**__ :face_with_monocle:',
            description=
            '''Use this command to have Pixel ask you a random *truth* or *dare* question. Use this function alone or with a group of people, there are fun questions and dares for everyone!                         

__**Syntax**__
p;tod''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info trivia'):
        embed = discord.Embed(
            title='__**trivia**__ :thinking:',
            description=
            '''Use this function to have Pixel ask you a random trivia question. The answer is hidden in spoilers, so put your guess in the chat and check if you were correct! There are questions from a variety of different topics, there is something for everyone, use these to test your knowledge or learn something new :)

__**Syntax**__
p;trivia''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info dare'):
        embed = discord.Embed(
            title="__**I dare you to...**__ :smiling_imp:",
            description=
            '''Use this command to have Pixel give you a random dare to do. There are a bunch of fun dares for all.
                        
__**Syntax**__
p;dare''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info truth'):
        embed = discord.Embed(
            title='__**answer truthfully...**__ :detective:',
            description=
            '''Use this command to have Pixel ask you a question for you to truthfully answer. No lying or cheating ;)
                            
__**Syntax**__
p;truth''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)
    if message.content.startswith('p;info prps'):
        embed = discord.Embed(
            title='__**rock paper scissors**__ :rock: :scroll: :scissors:',
            description=
            '''Use this command to play a game of rock paper scissors with Pixel! To use this command, type ``prps`` followed by your move, for example ``prps rock`` if you want to use rock, and Pixel will reply with its move!

__**Syntax**__
prps''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info ptranslate'):
        embed = discord.Embed(
            title='__**translate**__ :speech_left:',
            description=
            '''Use this command to translate any text from english to any other language the user wishes to! To use this command, you must type ``ptranslate`` followed by the two letter prefix of the language you wish to translate the text to. For example ``ptranslate es today is a good day`` will translate the text "today is a good day" from english to spanish. The bot uses the standard ``ISO 639-1`` language prefix for translation, so when translating to a language, please refer to the table of ``ISO 639-1`` language codes, which can be found here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
Please note that the bot does not support every single one of these languages and the bot will indicate if it does not support a particular language by returning an error instead of the translated text!

__**Syntax**__
ptranslate''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)
      
    if message.content.startswith('p;info ptictactoe'):
        embed = discord.Embed(
            title='__**TicTacToe**__ :regional_indicator_x: :o2:',
            description=
            '''Use this command to play a game of tictactoe or have two people play a game of tictacoe. To start the game type ``ptictactoe`` followed by the the userID of the first place (i.e pinging the first player) and the userID of the second of the second player (i.e. pinging the second player), it should look something like this: ``ptictactoe @player1 @player2``. Once the game has started, the player who makes the first move is pinged by pixel. To mark a tyle type ``ptplace`` followed by an integer between 1 - 9 (included) corresponding to the value of the tile you want to mark, make sure that the tile hasn't already been marked before, (ex. ``ptplace 4`` <-- this marks the 4th tile). The tiles are numbered in the following manner:
            
1 2 3
4 5 6 
7 8 9

Good luck!
                            
__**Syntax**__
ptictactoe''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pmathmatrixmult'):
        embed = discord.Embed(
            title='__**matrix multiplication**__ :1234:',
            description=
            '''Using this command, the user can multiply any two matrices they wish to find the product for. To use the command, the user must type: ``pmathmatrixmult "1 2; 3 4" "5 6;7 8" where the two matrices are surrounded by quotation marks and the rows are separated by a semi-colon.

__**Syntax**__
pmathmatrixmult''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

#HELP COMMANDS
    if message.content.startswith('p;dm help'):
        await message.channel.send(
            f"""{author.mention} Commands list sent in DM! """)
        embed = discord.Embed(title="Commands :cat:",
                              description='''
__**About Me**:__
• ``p;help``: Gives a list of commands
• ``p;info <command>``: For more detailed information about the specific command (ex. p;help fact)
• ``p;dm help``: Sends a DM to the user with a list of commands  
• ``p;about``: Give me a chance to introduce myself!
• ``p;ping``: Shows the real time response time of pixel  

__**Actions**:__
• ``p;hi``: Say hi to me! 
• ``p;hug``: Free hug for the user! Everyone deserves a hug :)
• ``p;random cat``: Sends a random cat image or GIF in the chat
• ``p;flip``: Flips a coin
• ``p;roll``: Rolls a 6-sided dice
• ``p;fact``: Tells you a random fact
• ``premindme <number> <unit> <reminder>``: Allows the user to set a reminder for themselves. To use this command, you must type ``premindme`` followed by the amount of time and the unit of the time and the reminder, in that order. For example ``premindme 30 minutes wash the car``, this will set a reminder for the user and will notify them after 30 minutes to wash their car! 
• ``pcountdown x``: Allows the user to set a countdown timer for ``x`` amount of seconds. 
• ``ppoll question option(s)``: Allows the user to set up a poll with upto 10 options. Type ``p;info ppoll`` for detailed information on functionality and useage!
• ``pdefine <word>``: Allows the user to type in a word from the english language that they wish to find the definition for. 
• ``p;cookie <@user>``: Give a cookie to someone in the Discord server! 
• ``psearch query``: Returns the first few results (upto 5 maximum) related to a query inputted by the user. 
• ``p;countchar text``: Counts the number of characters in a given text. 
• ``p;autocorrect text``: Autocorrects a given text by finding any issues with it. Please type ``p;info autocorrect`` for more details. 
• ``p;binary n``: Converts a decimal ``n`` to binary. 
• ``p;8ball <question>``: Use this command to ask the bot a yes/no style question.
• ``ptranslate <prefix> <text>``: Translates a given text in English to a language chosen by the user! 

__**Math**:__                                   
• ``pmathadd <number 1> <number 2> <number 3> ... <number n>``: Adds the inputted values. 
• ``pmathsubtract <number 1> <number 2> <number 3> ... <number n>``: Substracts the inputted values.
• ``pmathmultiply <number 1> <number 2> <number 3> ... <number n>``: Multiplies the inputted values.
• ``pmathdivide x y``: Divides the inputted values
• ``pmathexp x y``: Raises the base (x) to an exponent (y)
• ``pmathfactorial x``: Finds the factorial of the value inputted
• ``pmathsqrt x``: Finds the square root of the value inputted     
• ``pmathlog x y``: Finds the logrithm of the inputted value (x) with respect to the inputted base (y)
• ``pmathintegral f(x)``: Finds the integral of a given function, please use ``p;info pmathintegral`` to learn more!
• ``pmathgcd x y``: Finds the greatest common divisor between the two given numbers. 
• ``pmathpi n``: Sends the first ``n`` digits of pi.
• ``p;solve f(x)``: Finds the solution to a function ``f(x)``. Type the command ``p;info solve`` for more information!
• ``pmathmatrixmult <matrix 1> <matrix 2>``: Returns the result as the product of two matrices. Type ``p;info pmathmatrixmult`` for more information!   

__**Games**:__
• ``p;wyr``: Asks a *would you rather* question
• ``p;tod``: Asks a random *Truth*  or *Dare* question
• ``p;trivia``: Asks a trivia question!
• ``p;dare``: Gives a dare
• ``p;truth``: Asks a question for you to answer, truthfully
• ``prps``: Plays a game of rock, paper, scissors with the user. You must input your move with the command, for example if you want to use ``rock`` you must type ``prps rock``
• ``ptictactoe @player1 @player2``: This allows the two pinged users to play a game of TicTacToe! Type ``ptplace`` followed by an integer from 1 - 9 to mark your tile. Type ``p;info ptictactoe`` for more detailed information.''',
                              color=0xFFFF00)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(
            url=
            ""
        )
        embed.set_footer(
            text="If you find any issues or would like for me to add something, please make a GitHub Issue at github.com/RamGoenka/Pixel/issues",
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        await message.author.send(embed=embed)
    if message.content.startswith('p;help'):
        embed = discord.Embed(title="Commands :cat:",
                              description='''
__**About Me**:__
• ``p;help``: Gives a list of commands
• ``p;info <command>``: For more detailed information about the specific command (ex. p;help fact)
• ``p;dm help``: Sends a DM to the user with a list of commands  
• ``p;about``: Give me a chance to introduce myself!
• ``p;ping``: Shows the real time response time of pixel  

__**Actions**:__
• ``p;hi``: Say hi to me! 
• ``p;hug``: Free hug for the user! Everyone deserves a hug :)
• ``p;random cat``: Sends a random cat image or GIF in the chat
• ``p;flip``: Flips a coin
• ``p;roll``: Rolls a 6-sided dice
• ``p;fact``: Tells you a random fact
• ``premindme <number> <unit> <reminder>``: Allows the user to set a reminder for themselves. To use this command, you must type ``premindme`` followed by the amount of time and the unit of the time and the reminder, in that order. For example ``premindme 30 minutes wash the car``, this will set a reminder for the user and will notify them after 30 minutes to wash their car! 
• ``pcountdown x``: Allows the user to set a countdown timer for ``x`` amount of seconds.
• ``ppoll question option(s)``: Allows the user to set up a poll with upto 10 options. Type ``p;info ppoll`` for detailed information on functionality and useage!
• ``pdefine <word>``: Allows the user to type in a word from the english language that they wish to find the definition for. 
• ``p;cookie <@user>``: Give a cookie to someone in the Discord server! 
• ``psearch query``: Returns the first few results (upto 5 maximum) related to a query inputted by the user. 
• ``p;countchar text``: Counts the number of characters in a given text. 
• ``p;autocorrect text``: Autocorrects a given text by finding any issues with it. Please type ``p;info autocorrect`` for more details. 
• ``p;binary n``: Converts a decimal ``n`` to binary. 
• ``p;8ball <question>``: Use this command to ask the bot a yes/no style question.
• ``ptranslate <prefix> <text>``: Translates a given text in English to a language chosen by the user!

__**Math**:__                                   
• ``pmathadd <number 1> <number 2> <number 3> ... <number n>``: Adds the inputted values. 
• ``pmathsubtract <number 1> <number 2> <number 3> ... <number n>``: Substracts the inputted values.
• ``pmathmultiply <number 1> <number 2> <number 3> ... <number n>``: Multiplies the inputted values.
• ``pmathdivide x y``: Divides the inputted values
• ``pmathexp x y``: Raises the base (x) to an exponent (y)
• ``pmathfactorial x``: Finds the factorial of the value inputted
• ``pmathsqrt x``: Finds the square root of the value inputted     
• ``pmathlog x y``: Finds the logrithm of the inputted value (x) with respect to the inputted base (y)
• ``pmathintegral f(x)``: Finds the integral of a given function, please use ``p;info pmathintegral`` to learn more!
• ``pmathgcd x y``: Finds the greatest common divisor between the two given numbers. 
• ``pmathpi n``: Sends the first ``n`` digits of pi.
• ``p;solve f(x)``: Finds the solution to a function ``f(x)``. Type the command ``p;info solve`` for more information!
• ``pmathmatrixmult <matrix 1> <matrix 2>``: Returns the result as the product of two matrices. Type ``p;info pmathmatrixmult`` for more information!  

__**Games**:__
• ``p;wyr``: Asks a *would you rather* question
• ``p;tod``: Asks a random *Truth*  or *Dare* question
• ``p;trivia``: Asks a trivia question!
• ``p;dare``: Gives a dare
• ``p;truth``: Asks a question for you to answer, truthfully
• ``prps``: Plays a game of rock, paper, scissors with the user. You must input your move with the command, for example if you want to use ``rock`` you must type ``prps rock``
• ``ptictactoe @player1 @player2``: This allows the two pinged users to play a game of TicTacToe! Type ``ptplace`` followed by an integer from 1 - 9 to mark your tile. Type ``p;info ptictactoe`` for more detailed information.''',
                              color=0xFFFF00)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(
            url=
            ""
        )
        embed.set_footer(
            text="If you find any issues or would like for me to add something, please make a GitHub Issue at github.com/RamGoenka/Pixel/issues",
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        await message.channel.send(embed=embed)

#ROCK PAPER SCISSORS
    if message.content.startswith("prps"):
        choices = choices = [
            "rock", "paper", "scissors", "rock", "paper", "scissors", "rock",
            "paper", "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors", "rock", "paper", "scissors", "rock", "paper",
            "scissors"
        ]
        bot_choice = random.choice(choices)
        user_choice = message.content[5:]
        if user_choice.lower() in choices:
            if user_choice.lower() == bot_choice:
                await message.channel.send("I choose **" + bot_choice +
                                           "** too! It's a tie.")
            elif (user_choice.lower() == "rock" and bot_choice == "scissors"
                  ) or (user_choice.lower() == "scissors" and bot_choice
                        == "paper") or (user_choice.lower() == "paper"
                                        and bot_choice == "rock"):
                await message.channel.send("I choose **" + bot_choice +
                                           "**. You win!")
            else:
                await message.channel.send("I choose **" + bot_choice +
                                           "**. I win!")
        else:
            await message.channel.send(
                "**Invalid choice**. Please choose rock, paper or scissors.")


#COUPLE OF USEFUL COMMANDS INCLUDING MATHEMATICS AND ACTIONS
@client.command()
async def hadd(ctx, *args):
    try:
        numbers = [float(num) for num in args]
        a = sum(numbers)
        await ctx.send(f"**Result:** ```{a}```")
    except ValueError:
        await ctx.send('Please provide valid numbers as input.')

@client.command()
async def hsubtract(ctx, *args):
    try:
        if len(args) < 2:
            await ctx.send('Please provide at least two numbers.')
            return
        numbers = [float(num) for num in args]
        result = numbers[0]
        for num in numbers[1:]:
            result -= num
        await ctx.send(f"**Result:** ```{result}```")
    except ValueError:
        await ctx.send('Please provide valid numbers as input.')

@client.command()
async def hmultiply(ctx, *args):
    try:
        numbers = [float(num) for num in args]
        result = 1
        for num in numbers:
            result *= num
        await ctx.send(f"**Result:** ```{result}```")
    except ValueError:
        await ctx.send('Please provide valid numbers as input.')

@client.command()
async def ountdown(ctx, seconds: int):
    message = await ctx.send(f'{seconds} seconds left!')
    while seconds > 0:
        await asyncio.sleep(1)
        seconds -= 1
        await message.edit(content=f'{seconds} seconds left!')
    await ctx.send(f'{ctx.author.mention}, the countdown you set is complete!')

@client.command()
async def earch(ctx, *, query: str):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}&num=5"
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    results = soup.select(".g")
    for i, result in enumerate(results):
        title = result.select_one(".DKV0Md").text
        link = result.select_one("a")["href"]
        snippet = result.select_one(".VwiC3b").text
        await ctx.send(
            f"**__Result {i+1}:__**\n**{title}**\n{link}\n{snippet}\n")

@client.command()
async def hdivide(ctx, num1: int, num2: int):
    a = num1 / num2
    await ctx.send(f"**Result:** ```{a}```")

@client.command()
async def hgcd(ctx, num1: int, num2: int):
    a = max(num1, num2)
    b = min(num1, num2)
    while b != 0:
        temp = b
        b = a % b
        a = temp
    await ctx.send(f"**Result:** ```{a}```")

@client.command()
async def hpi(ctx, digits: int):
    if digits > 1000:
        await ctx.send("Sorry, I only know up to 1000 digits of pi.")
    else:
        mpmath.mp.dps = digits
        pi_value = str(mpmath.pi)
        await ctx.send(
            f"The first **{digits}** digits of pi are: ```{pi_value}```")

@client.command()
async def hexp(ctx, num1: int, num2: int):
    a = num1**num2
    await ctx.send(f"**Result:** ```{a}```")

@client.command()
async def hsqrt(ctx, num1: int):
    a = num1**0.5
    await ctx.send(f"**Result:** ```{a}```")

@client.command()
async def hfactorial(ctx, num1: int):
    a = math.factorial(num1)
    await ctx.send(f"**Result:** ```{a}```")

@client.command()
async def hlog(ctx, num1: int, num2: int):
    a = math.log(num1, num2)
    await ctx.send(f"**Result:** ```{a}```")

@client.command()
async def ranslate(ctx, lang_to, *, args):
    translator= Translator(to_lang=lang_to)
    translation = translator.translate(args)
    await ctx.send(translation)

@client.command()
async def efine(ctx, word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json(
        )[0]['meanings'][0]['definitions'][0]['definition']
        await ctx.send(f"**{word}**: {data}")
    else:
        await ctx.send(f"Sorry, I couldn't find the definition for **{word}**."
                       )
      
def parse_matrix(matrix_str):
    try:
        matrix = []
        rows = matrix_str.split(';')
        for row in rows:
            matrix.append([float(num) for num in row.split()])
        return np.array(matrix)
    except ValueError:
        return None

@client.command()
async def hmatrixmult(ctx, matrix1: str, matrix2: str):
    try:
        mat1 = parse_matrix(matrix1)
        mat2 = parse_matrix(matrix2)
        if mat1 is None or mat2 is None:
            raise ValueError
        product = np.matmul(mat1, mat2)
        await ctx.send(f"**Result:** ```{product}```")
    except ValueError:
        await ctx.send(
            'Please provide valid matrices as input. Use semicolon to separate rows and space for columns.'
        )
@client.command()
async def alance(ctx, *, equation):
    try:
        reactants, products = equation.split('->')
        reactants = reactants.split('+')
        products = products.split('+')
        balanced = balance_stoichiometry(reactants, products)
        balanced_eq = ' + '.join([f'{v} {k}' for k, v in balanced[0].items()]) + ' -> ' + ' + '.join([f'{v} {k}' for k, v in balanced[1].items()])
        await ctx.send(f'__The balanced chemical equation is:__ {balanced_eq}')
    except Exception as e:
        await ctx.send(f'Error: {str(e)}')

@client.command()
async def oll(ctx, question, *options: str):
    if len(options) <= 1:
        await ctx.send("You need more than one option to create a poll!")
        return
    if len(options) > 10:
        await ctx.send("You cannot create a poll with more than 10 options!")
        return
    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['👍', '👎']
    else:
        reactions = [
            '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟'
        ]
    description = []
    for i, option in enumerate(options):
        description += '\n {} {}'.format(reactions[i], option)
    embed = discord.Embed(title=question, description=''.join(description))
    react_message = await ctx.send(embed=embed)
    for reaction in reactions[:len(options)]:
        await react_message.add_reaction(reaction)


@client.command()
async def emindme(ctx, time: int, unit: str, *, reminder: str):
    await ctx.send(f"{ctx.author.mention}, I will make sure to remind you :)")
    unit = unit.lower()
    if unit == 'seconds':
        await asyncio.sleep(time)
    elif unit == 'second':
        await asyncio.sleep(time)
    elif unit == 'minutes':
        await asyncio.sleep(time * 60)
    elif unit == 'minute':
        await asyncio.sleep(time * 60)
    elif unit == 'hours':
        await asyncio.sleep(time * 60 * 60)
    elif unit == 'hour':
        await asyncio.sleep(time * 60 * 60)
    elif unit == 'days':
        await asyncio.sleep(time * 60 * 60 * 24)
    elif unit == 'day':
        await asyncio.sleep(time * 60 * 60 * 24)
    else:
        await ctx.send(
            f"{ctx.author.mention}, please provide a valid time unit (second/seconds/minute/minutes/hour/hours/day/days)."
        )
        return
    await ctx.send(
        f"{ctx.author.mention}, you asked me to remind you: **{reminder}**")


#TICTACTOE
player1 = ""
player2 = ""
turn = ""
gameOver = True
board = []
winningConditions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
                     [2, 5, 8], [0, 4, 8], [2, 4, 6]]


@client.command()
async def ictactoe(ctx, p1: discord.Member, p2: discord.Member):
    global count
    global player1
    global player2
    global turn
    global gameOver

    if gameOver:
        global board
        board = [
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:", ":white_large_square:",
            ":white_large_square:"
        ]
        turn = ""
        gameOver = False
        count = 0
        player1 = p1
        player2 = p2
        line = ""
        for x in range(len(board)):
            if x == 2 or x == 5 or x == 8:
                line += " " + board[x]
                await ctx.send(line)
                line = ""
            else:
                line += " " + board[x]
        num = random.randint(1, 2)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
    else:
        await ctx.send(
            "A game is already in progress! Please finish it before starting a new one."
        )


@client.command()
async def place(ctx, pos: int):
    global turn
    global player1
    global player2
    global board
    global count
    global gameOver

    if not gameOver:
        mark = ""
        if turn == ctx.author:
            if turn == player1:
                mark = ":regional_indicator_x:"
            elif turn == player2:
                mark = ":o2:"
            if 0 < pos < 10 and board[pos - 1] == ":white_large_square:":
                board[pos - 1] = mark
                count += 1
                line = ""
                for x in range(len(board)):
                    if x == 2 or x == 5 or x == 8:
                        line += " " + board[x]
                        await ctx.send(line)
                        line = ""
                    else:
                        line += " " + board[x]

                checkWinner(winningConditions, mark)
                print(count)
                if gameOver == True:
                    await ctx.send(
                        f"""**Result**: {mark} is the winner! :tada:""")
                elif count >= 9:
                    gameOver = True
                    await ctx.send("**Result**: It's a tie!")
                if turn == player1:
                    turn = player2
                elif turn == player2:
                    turn = player1
            else:
                await ctx.send(
                    "Please type ``ptictactoe @player1 @player2`` to start a game of TicTacToe. Type ``ptplace`` followed by an integer from 1 - 9 (inclusive) corresponding to the tile you want to mark. Make sure the tile hasn't already been marked and is empty. Good luck!"
                )
        else:
            await ctx.send("It is not your turn yet.")
    else:
        await ctx.send(
            "To start a new game of TicTacToe, type ``ptictactoe @player1 @player2``."
        )


def checkWinner(winningConditions, mark):
    global gameOver
    for condition in winningConditions:
        if board[condition[0]] == mark and board[
                condition[1]] == mark and board[condition[2]] == mark:
            gameOver = True


@ictactoe.error
async def tictactoe_error(ctx, error):
    print(error)
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please mention 2 players for this command.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please mention 2 players for this command.")


@place.error
async def place_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please enter a position you would like to mark.")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Please make sure to enter an integer.")


embed_footers = [
    'Thanks for using pixel :)',
    'You must be tired from being so purr-fect :D', 'You are very pawsome :)',
    'Are you from Tennessee? Because you are the only ten I see :D',
    'If you were a burger at McDonalds, you would be the McAmazing :)',
    'You seem to have a nice cat-titude :D',
    'Thanks for checking out my commands :)', 'Hope you have a great day :D',
    'Your back must hurt from carrying all that amazingness :)'
]

sad = [
    "I am a failure", "i am failure", "i am a failure", "im a failure",
    "i'm failure", "i'm a failure", "I'm a failure", "I am a disgrace",
    "I am useless", "I am stupid", "I am an idiot", "I am dumb",
    "I am disappointing", "I am useless", "I am not smart", "I'm dumb",
    "I'm stupid", "i am disgrace", "i am a disgrace", "im a disgrace",
    "i'm disgrace", "i'm a disgrace", "i am idiot", "i am an idiot",
    "im an idiot", "i'm idiot", "i'm an idiot", "i am unsmart", "im unsmart",
    "i'm unsmart", "i am stupid", "i am a stupid", "im a stupid", "i'm stupid",
    "i'm a stupid", "i am dumb", "i am a dumb", "im a dumb", "i'm dumb",
    "i'm a dumb", "i am disappointing", "i am a dissappointing",
    "im a dissappointing", "i'm dissappointing", "i'm a dissappointing",
    "i am useless", "i am a useless", "im a useless", "i'm useless",
    "i'm a useless", "i am unintelligent", "i am a unintelligent",
    "im a unintelligent", "i'm unintelligent", "i'm a unintelligent",
    "i am not smart", "i am a not smart", "im a not smart", "i'm not smart",
    "i'm a not smart", "i am Failure", "i am a Failure", "im a Failure",
    "i'm Failure", "i'm a Failure", "i am Idiot", "i am a Idiot", "im a Idiot",
    "i'm Idiot", "i'm a Idiot", "i am Stupid", "i am a Stupid", "im a Stupid",
    "i'm Stupid", "i'm a Stupid", "i am Dumb", "i am a Dumb", "im a Dumb",
    "i'm Dumb", "i'm a Dumb", "i am Disappointing", "i am a Disappointing",
    "im a Disappointing", "i'm Disappointing", "i'm a Disappointing",
    "i am Useless", "i am a Useless", "im a Useless", "i'm Useless",
    "i'm a Useless", "i am Disgrace", "i am a Disgrace", "im a Disgrace",
    "i'm Disgrace", "i'm a Disgrace", "i am Unsmart", "i am a Unsmart",
    "im a Unsmart", "i'm Unsmart", "i'm a Unsmart", "I'm stupid",
    "i am Unintelligent", "i am a Unintelligent", "im a Unintelligent",
    "i'm Unintelligent", "i'm a Unintelligent", "i am Not smart",
    "I am Not smart", "i am a Not smart", "im a Not smart", "i'm Not smart",
    "i'm a Not smart", "I am trash", "i'm trash", "I'm trash", "i am trash",
    "I’m garbage", "i'm garbage", "I am garbage", "i am garbage",
    "i am dumbest", "I am dumbest"
]

encouraging_words = [
    "Aww! That is not true :(", "No, you are an amazing person :)",
    "Hopefully it gets better <(^-^<)",
    "You are a capable individual with great potential!",
    "Believe in yourself, you got this!",
    "Keep your head high! Eventually you will get there :)",
    "Don't give up! You got this!",
    "There is light at the end of the tunnel :)",
    "Sending good vibes and happy thoughts your way  <(^-^<)",
    "Believe in yourself! Because I for sure do :)",
    "Believe in yourself, you are amazing!",
    "Stay strong! You are powerful and you are a fighter! You got this!",
    "I am rooting for you!", "You are a wonderful person!",
    "You are amazing :)"
]

hug_gif = [
    "https://c.tenor.com/nUrfyD_VmM8AAAAC/hug-cute.gif",
    "https://c.tenor.com/4XQiR1rkwIAAAAAC/ghost-hug-ghost-hugs.gif",
    "https://c.tenor.com/UKsNkAqj7YcAAAAC/hug.gif",
    "https://c.tenor.com/NGFif4dxa-EAAAAC/hug-hugs.gif",
    "https://c.tenor.com/GdJRGf60YN4AAAAC/hugs-sending-virtual-hugs.gif",
    "https://c.tenor.com/XQh-aF1wTUIAAAAC/ghosthug.gif",
    "https://c.tenor.com/Vx-Fmk3G7McAAAAM/cute.gif",
    "https://media2.giphy.com/media/9Y1LEFKsbbP4hrLgV3/giphy.gif?cid=790b76119eb6ba36ddfbe56bf3ca28b4c38ddc7f8c1cacef&rid=giphy.gif&ct=g",
    "https://c.tenor.com/8Jk1ueYnyYUAAAAC/hug.gif",
    "https://c.tenor.com/1T1B8HcWalQAAAAC/anime-hug.gif",
    "https://c.tenor.com/Ct4bdr2ZGeAAAAAC/teria-wang-kishuku-gakkou-no-juliet.gif",
    "https://c.tenor.com/ia_mkwn2dwYAAAAC/love.gif",
    "https://c.tenor.com/endJ8_rbXUYAAAAC/be-happy-love.gif",
    "https://c.tenor.com/XyMvYx1xcJAAAAAC/super-excited.gif",
    "https://c.tenor.com/3mr1aHrTXSsAAAAC/hug-anime.gif",
    "https://c.tenor.com/EqzscTWbbXEAAAAC/kanna-dragon-maid.gif",
    "https://c.tenor.com/cFhjNVecNGcAAAAC/anime-hug.gif",
    "https://c.tenor.com/tEUwg3wJ_aYAAAAM/hug-viking.gif",
    "https://c.tenor.com/qF7mO4nnL0sAAAAC/abra%C3%A7o-hug.gif",
    "https://c.tenor.com/SXk-WqF6PpQAAAAC/anime-hug.gif"
]

coin_outcomes = [
    "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**",
    "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**",
    "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**",
    "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**",
    "**Heads**", "**Tails**", "**Heads**", "**Tails**", "**Heads**",
    "**Tails**", "**Heads**", "**Tails**", "**Heads**", "**Tails**",
    "**Heads**", "**Tails**"
]

dice_roll = [
    "You rolled a **1** :game_die:", "You rolled a **2** :game_die:",
    "You rolled a **3** :game_die:", "You rolled a **4** :game_die:",
    "You rolled a **5** :game_die:", "You rolled a **6** :game_die:"
]

cat_images = [
    "https://upload.wikimedia.org/wikipedia/commons/3/38/Adorable-animal-cat-20787.jpg",
    "https://images.rawpixel.com/image_1000/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L2ZyYW5pbWFsX2NhdF9raXR0ZW5fYnJpdGlzaC1pbWFnZS1reWJlYXlrNC5qcGc.jpg",
    "https://cc0.photo/wp-content/uploads/2016/10/Striped-cat-on-a-meadow-2048x1365.jpg",
    "https://c.pxhere.com/images/8d/1e/604c6eb3dca5d46f3854ae974ccf-1603569.jpg!d",
    "https://pixnio.com/free-images/2021/09/14/2021-09-14-08-25-52-1049x1350.jpg",
    "https://c.tenor.com/bK1qpWGyQKkAAAAd/kitty.gif",
    "https://c.tenor.com/1iAVPVejxSkAAAAd/cat-cats.gif",
    "https://cdn.pixabay.com/photo/2020/06/02/06/18/kitten-5249587_1280.jpg",
    "https://pixnio.com/free-images/2017/09/26/2017-09-26-09-57-33-1100x733.jpg",
    "https://i0.wp.com/pixahive.com/wp-content/uploads/2020/10/A-cute-cat-124534-pixahive.jpg?fit=1560%2C1040&ssl=1",
    "https://pixnio.com/free-images/2017/09/26/2017-09-26-09-59-07-1100x733.jpg",
    "https://pixnio.com/free-images/2017/09/26/2017-09-26-07-39-47-1100x733.jpg",
    "https://live.staticflickr.com/5698/23119711630_c3ffe739a0_b.jpg",
    "https://cdn.stocksnap.io/img-thumbs/960w/cat-kitten_BY1YIGNS0Y.jpg",
    "https://images.rawpixel.com/image_1300/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIyLTA1L3B4NzU1MDcwLWltYWdlLWt3dnhnbzBsLmpwZw.jpg",
    "https://pixnio.com/free-images/2017/09/26/2017-09-26-07-23-15-1100x818.jpg",
    "https://c.pxhere.com/photos/5e/7b/cat_feline_staring_kitty_pet_cute_cat-640016.jpg!d",
    "https://c.tenor.com/ZhfMGWrmCTcAAAAC/cute-kitty-best-kitty.gif",
    "https://media.discordapp.net/attachments/1011341536597917705/1044029794783858808/Tumblr_l_52756928702686.gif"
]

wyr_questions = [
    "Give up junk food for a month **__OR__** Give up all forms of social media for a week?",
    "Be reborn as a cat **__OR__** A dog?",
    "Be invisible **__OR__** Be able to fly?",
    "Be rich but lonely **__OR__** Be poor but have loyal friends?",
    "Know how you die **__OR__** Know when you die?",
    "Have a lot of distant friends **__OR__** One really good and close friend?",
    "Cry each time something funny happens **__OR__** Laugh each time something tragic /  sad happens?",
    "Be caught cheating in a relationship **__OR__** Be caught cheating on a test?",
    "Have as much wealth as you wish but always remain sad **__OR__** Live paycheck to paycheck but be happy?",
    "Never be able to speak again **__OR__** Never be able to hear again?",
    "Be able to sleep 8 hours but only during day-time **__OR__** Only be able to sleep for 1 hour during the night?",
    "Be able to go back in the past and fix a mistake **__OR__** Be able to go back in the past and revive one dead person?",
    "Find the love of your life **__OR__** Win a million dollars?",
    "Give up showering for a month **__OR__** Give up all forms of social media for a month?",
    "Be a famous serial-killer **__OR__** Be poor?",
    "Get a private island **__OR__** A private jet?",
    "Be the fastest runner in the world **__OR__** Have the highest vertical jump in the world?",
    "Be a famous athlete **__OR__** A famous singer?",
    "Never be able to lie **__OR__** Always be lied to?",
    "Give up being able to eat meat **__OR__** Give up being able to eat vegetables?",
    "Live in the middle of the ocean for an year **__OR__** Live in the middle of a dense forest for an year?",
    "Live in 45°C for one year **__OR__** Live in -45°C for one year?",
    "Be chased by a clown **__OR__** Be chased by a lion?",
    "Be fluent in every language **__OR__** Be a master of every single musical instrument?",
    "Be stuck in an elevator with the power supply gone **__OR__** Be stuck in a train in the middle of nowhere?",
    "Be 4 feet tall **__OR__** Be 8 feet tall?",
    "Be a famous singer **__OR__** A famous Author?",
    "Be an Olympic gold medalist **__OR__** Win a Nobel Prize?",
    "Never be able to make a phone call ever again **__OR__** Never be able to send a text ever again?",
    "Give up social media for the rest of your life **__OR__** Eat the same dinner for the rest of your life?",
    "Give up YouTube **__OR__** Give up Netflix?",
    "Have the ability to freeze time for 10 minutes but it be only a one time thing **__OR__** Be able to time travel 10 minutes into the future but have it be only a one time thing (i.e. you only have 1 chance to use the ability)?",
    "Give up ramen **__OR__** Give up sushi?",
    "Give up tea **__OR__** Give up coffee?",
    "End world hunger **__OR__** Be able to eat your favourite food's for free, whenever and wherever?",
    "Get $1 million handed to your right now **__OR__** be paid $10,000 every month for the next 12 months?",
    "Have front row tickets to a musician you’ve never heard of **OR** Listen to your favorite band perform from the parking lot?",
    "Only eat burger for the rest of your life **__OR__** Only eat pizza for the rest of your life?",
    "Eat the same breakfast for the rest of your life **__OR__** Eat the same dinner for the rest of your life?",
    "Always be underdressed **__OR__** Always be overdressed?",
    "Sleep in suit for the rest of your life **__OR__** Attend formal gatherings/events in pyjamas?",
    "Be colorblind **__OR__** Give up the sense of taste?",
    "Date someone rich who doesn't care about you **__OR__** Date someone working minimum wage and treat you very nicely?",
    "Rewind life by 5 years **__OR__** Fastforward by 5 years?",
    "Restart your life **__OR__** Continue with it as it is?",
    "Be a T.V. show villain **__OR__** A video game villain?",
    "Witness the beginning of the world **__OR__** The end of it?",
    "Murder your best friend and get away with it **__OR__** Be put in jail for 20 years for a crime you did not commit?",
    "Be the best player on the worst team **__OR__** The worst player on the best team?",
    "Sneeze uncontrollably for 4 hours everyday **__OR__** Have uncontrollable hiccups everyday for 4 hours?",
    "Cheat your way to success **__OR__** Have all your hardwork go in vain?",
    "Be allergic to water **__OR__** Be allergic to sunlight?",
    "Be stung by a bee **__OR__** Be bitten by a street dog?",
    "Be a lion **__OR__** Be a tiger?",
    "Be 20 years old for the rest of your life **__OR__** Be 40 years old for the rest of your life?",
    "Have everyone forget who you are **__OR__** Have you forget every single person you have ever known or talked to?",
    "Have a spider in your bed for one night **__OR__** Have a snake in your bed for night?",
    "Bring back dinosaurs **__OR__** Have the world be locked in a global pandemic forever?",
    "Have 3 feet deducted from your current height **__OR__** Have 3 feet added to your current height?",
    "Be sent to prision for 5 years but be paid $5 million the moment your term in jail ends **__OR__** Never go to jail and work minimum wage for the rest of your life?",
    "Have a spider crawl up your arm **__OR__** A snake crawl up your arm?",
    "Never be able to lie ever again **__OR__** Have every lie you are every told become true?",
    "Be able to speak to animals and understand them **__OR__** Be able to read the mind of anyone you want?",
    "Have a terrible boss but a six-figure job **__OR__** A great boss but a minimum wage job?",
    "Have to eat one jar of strawberry jam everyday for the rest of your life **__OR__** One jar of peanut butter everyday for the rest of your life?",
    "Be with someone you love but they don't love you back **__OR__** Be with someone who loves you but you don't love them back?",
    "Lose all your hard earned money **__OR__** Lose all your friends?",
    "Be with the love of your life **__OR__** Win a $1 million?",
    "Flip a coin and if it lands on heads you win $1 million **__OR__** Be given $10,000 right now?",
    "Have your mother look through your search history **__OR__** Have your best friend look through your search history?",
    "Only be able to shower once a month **__OR__** Only be able to check your phone once a day for 1 hour?",
    "Give up cursing and using any sort of swear words and foul language forever **__OR__** Have to run 5 miles every single morning for the rest of your life?",
    "Do an amazing trickshot but have no one witness it **__OR__** Do something embarrassing and have a lot of people witness it?",
    "Give up ice-cream **__OR__** Give up cola and soda?",
    "Be expelled from school for 30 days **__OR__** Be in prision for 30 days?"
]

random_facts = [
    "Sudan has more pyramids than any country in the world. :flag_sd:",
    "The bumblebee bat is the world’s smallest mammal. :bat:",
    "There are parts of Africa in all four hemispheres. :earth_africa:",
    "The Philippines consists of 7,641 islands. :flag_ph:",
    "Japan has one vending machine for every 40 people. :flag_jp:",
    "There’s only one letter that doesn’t appear in any U.S. state name, it is Q. :regional_indicator_q:",
    "A cow-bison hybrid is called a beefalo. :cow: :bison:",
    "Armadillo shells are bulletproof. :muscle:",
    "Some octopus species lay around 56,000 eggs at a time. :octopus:",
    "Blue whales eat up to half a million calories in one mouthful. :whale:",
    "The current American flag was designed by a high school student. :flag_us:",
    "No number before 1,000 contains the letter A. :1234:",
    "Giraffe tongues can be 20 inches long. :giraffe:",
    "Cats are believed to be the only mammals who don’t taste sweetness. :cat:",
    "Humans aren’t the only animals that dream, rats dream too. :rat:",
    "If the sun exploded right now, you wouldn't know about it for another eight minutes. :boom:",
    "Over 80 million bacteria can be exchanged in one kiss. :microbe:",
    "Australia is wider than the moon, while the moon as a diameter of 3400 km, Australia has a diameter of 4000 km. :flag_au:",
    "*face with tears of joy* is the most used emoji worldwide. :joy:",
    "A shrimp's heart is located in its head. :shrimp:",
    "Odontophobia is the fear of teeth (or the fear of anything related to dentistry in general). :tooth:",
    "Elephants are the only animal to have four forward-facing knees. :elephant:",
    "The 1939 novel *Gadsby* is a 50,000 word novel and doesn't contain the *E* :book:",
    "Lady Liberty (Statue of Liberty) wears a size 879 shoe. :statue_of_liberty:",
    "Koala fingerprints are so close to human fingerprints that they could taint crime scenes. :koala:",
    "There are so many types and variants of apples that if you ate one everyday, it would take you approximately 20 years to have had tried them all. :apple:",
    "The Unicorn is the national animal of Scotland. :scotland:",
    "*Cynophobia* is known as the fear of dogs. :dog:",
    "Sloths can hold their breaths for up to 40 minutes. :sloth:",
    "Snails can tend to have very long naps, some lasting up to three years! :snail:",
    "Kangaroos can not walk backwards. :kangaroo:",
    "There are 31,556,926 seconds in a year. :timer:",
    "Lemons float but limes sink. :lemon:",
    "Hot water turns into ice faster than cold water. This observation is called the *Mpemba effect* :thermometer:",
    "The longest word in the English language, according to the Guinness Book of World Records, is ``pneumonoultramicroscopicsilicovolcanoconiosis``. :speaking_head:",
    "The Mona Lisa is the most valuable painting in the world, with an estimated worth of over $800 million. :art:",
    "The human nose can detect over 1 trillion different scents. :nose:",
    "The oldest known living tree on Earth is a bristlecone pine that is over 5,000 years old. :deciduous_tree:"
]

trivia_questions = [
    ":thinking: Who was the 28th U.S. president? (Answer: || Woodrow Wilson ||)",
    ":thinking: How many countries does the continent Africa comprise of? (Answer: || 54 ||)",
    ":thinking: Which is the largest country in the world by land area? (Answer: || Russia ||)",
    ":thinking: How many states does the United States of America comprise of? (Answer: || 50 ||) ",
    ":thinking: Which were the last two states to join the Union? (Answer: || Alaska and Hawaii ||)",
    ":thinking: Which country won the Men's Fifa World Cup 2018, and against whom? (Answer: || France won against Croatia ||) ",
    ":thinking: Which team (either one is fine) has won the most Men's NBA Championships? (Answer: || Boston Celtics and Los Angeles Lakers have both won 17 NBA Championships ||)",
    ":thinking: Who was the first person to step foot on the Moon? (Answer: || Neil Armstrong ||)",
    ":thinking: What is the area on the Moon known as where the first person stepped foot on? (Answer: || Sea of Tranquility ||)",
    ":thinking: In the state of Georgia, it’s illegal to eat what with a fork? (Answer: || Fried Chicken ||)",
    ":thinking: The name of which African animal means *river horse*? (Answer: || Hippopotamus ||)",
    ":thinking: Which country has won the most Men's ICC Cricket World Cup titles? (Answer: || Australia ||)",
    ":thinking: In which year did World War II start? Which year did it end in? (Answer: || Start: 1939, End: 1945 ||)",
    ":thinking: What is the capital of Norway? (Answer: || Oslo ||)",
    ":thinking: Which continent, based on land area, is the largest in the world? (Answer: || Asia ||)",
    ":thinking: Which state in the United States of America has the most electoral college votes? (Answer: || California, it has 55 electroal votes ||)",
    ":thinking: Which country is also known as the *land of the rising sun*? (Answer: || Japan ||)",
    ":thinking: How many points is a touchdown? (Answer: || 6 points ||)",
    ":thinking: How many terms did Benjamin Franklin serve as president? (Answer: || He was never a president ||)",
    ":thinking: Which team won the first ever NBA championship? (Answer: || Philadelphia Warriors in 1946 ||)",
    ":thinking: Which is the largest state in the United States of America based on land area? (Answer: || Alaska ||)",
    ":thinking: Which is the largest state in the United States of America based on land area? (Answer: || Rhode Island ||)",
    ":thinking: Who is on the 100 U.S. Dollar bill? (Answer: || Benjamin Franklin ||)",
    ":thinking: Who was the 1st President of the United States of America? (Answer: || George Washington ||)",
    ":thinking: Who was the 16th U.S. president and is on the $5 bill? (Answer: || Abraham Lincoln ||)",
    ":thinking: What is the more popular name for the portrait officially titled “La Gioconda,” painted in 1503? (Answer: || Mona Lisa ||)",
    ":thinking: What is the capital of India? (Answer: || New Dehli ||)",
    ":thinking: What is the capital of the United States of America? (Answer: || Washington, D.C. ||)",
    ":thinking: Which two countries have the longest shared international border? (Answer: || Canada and the U.S.A. ||)",
    ":thinking: What is the human body’s largest organ? (Answer: || Skin ||)",
    ":thinking: How many bones do sharks have? (Answer: || 0 bones ||)",
    ":thinking: What was the first country to give women the right to vote? (Answer: || New Zealand ||)",
    ":thinking: What river runs through Paris? (Answer: || The Seine ||)",
    ":thinking: Which is the longest river in the world? (Answer: || The Nile ||)",
    ":thinking: Mount Everest is the tallest mountain in the world, what is the second tallest mountain in the world? (Answer: || Mount K2 ||)",
    ":thinking: How many stars and stripes are in the U.S.A. flag? (Answer: || 50 stars & 13 stripes  ||)"
    ":thinking: ",
    ":thinking: What is the rarest blood type? (Answer: || AB Negative ||)",
    ":thinking: How many countries are in the European Union? (Answer: || 27 ||)",
    ":thinking: What does DNA stand for? (Answer: || Deoxyribonucleic Acid ||)",
    ":thinking: How many phases does the moon have? (Answer: || Eight ||)",
    ":thinking: How many hearts does an octopus have? (Answer: || Three ||)",
    ":thinking: Which two planets in our Solar System have no moons? (Answer: || Mercury and Venus ||)",
    ":thinking: What U.S. city has the nickname “Motown,” derived from ‘motor town’? (Answer: || Detroit ||)",
    ":thinking: Uranus and which other planet are nicknamed the “ice giants”? (Answer: || Neptune ||) ",
    ":thinking: How many centimeters are in 1 inch (Answer: || 2.54, however any value between 2.5 and 2.54 is acceptable ||)",
    ":thinking: *Area 51* is located in which U.S. State? (Answer: || Nevada ||)",
    ":thinking: What country has the most natural lakes? (Answer: || Canada ||)",
    ":thinking: Muscat is the capital of which country? (Answer: || Oman ||)",
    ":thinking: In what country would you find Lake Bled? (Answer: || Slovenia ||)",
    ":thinking: What is the hottest planet in the solar system? (Answer: || Venus ||)",
    ":thinking: The Taj Mahal was constructed as a tomb of the wife of which Mughal Emperor? (Answer: || Shah Jahan ||)",
    ":thinking: What is the day after Christmas called? (Answer: || Boxing Day ||)",
    ":thinking: How many years in a decade? (Answer: || 10 years ||)",
    ":thinking: How many years in a century? (Answer: || 100 years ||)",
    ":thinking: In which state is *Mount Rushmore* located? (Answer: || South Dakota ||)"
]

random_tod = [
    'Have you ever skipped class? If so then which class was it?',
    'Have you ever blamed something you did on someone and have gotten them in trouble?',
    'What is the best meal you have ever had?',
    'What is something you wish you could tell to your younger self?',
    'What is something you regret doing in the past and would like to change?',
    'Have you ever spilled someones secret?',
    'If you could be anyone or anything for 1 hour, who or what would it be?',
    'Have you ever peed the pool?', 'What is your favourite movie?',
    'What is one thing you wish you could change about your parents?',
    'What is one thing you wish you could change about your friends?',
    'Do you know how to tie shoe laces?', 'Do you hold grudges?',
    'Have you ever pulled a prank on someone and it went wrong?',
    'If there were absolutely no consequences whatsoever, what is the one thing you would do?',
    'Have you ever lied to your parents?',
    'What is the longest you have ever gone without showering?',
    'What is the longest you have ever gone without sleeping?',
    'Have you ever broken the law? (i.e. done something illegal)',
    'Do you have a secret that you want no one to know? Would you tell it if you were offered $1 million to do so?',
    'Have you ever cheated on a test?',
    'What is/was your favourite subject in school?',
    'Have you ever shoplifted? From where and what did you take?',
    'Would you consider yourself an introvert, extrovert or an ambivert?',
    'Are you vegetarian? If not then would you be willing to become vegetarian?',
    'Do you like cheese?',
    'What is the one thing you wish you could change about your past?',
    'Do you have any regrets? If so (and if you feel comfortable sharing), what are they?',
    'Have you ever been in a relationship? Are you in one as of now?',
    'Who is your favourite singer?',
    'If you could master one language, which one would it be?',
    'Were you a quiet kid or a loud kid?',
    'What is your biggest (or one of your biggest) fears?',
    'What is your biggest (or one of your biggest) pet peeve?',
    'What is the most embarrassing thing you have ever done?',
    'When was the last time you said a lie?'
    'If you could have dinner with one person, dead or alive, who would it be?',
    'Who would be your *plus 1* to a concert by your favorite artist / band?',
    'Would you consider your sleep schedule to be good/normal?',
    'How many hours did you sleep last night?',
    'Write your name with your non-dominant hand',
    'Give up all forms of social media for the next 10 minutes',
    'Touch some grass (and if you are allergic to grass then go outside for a brief stroll',
    'Give up junk food for the next 16 hours',
    'DM someone the word *meow* and respond to everything they say with *meow* for the next 5 minutes',
    'Let the group pick a profile picture for you to set for the next 24 hours',
    'Do 10 push ups',
    'Close your eyes and type a message and send it in the chat',
    'Only type with your left and for the next 10 minutes',
    'Act like a 5 year old for the next 5 minutes',
    'Talk in an accent for the next 5 minutes',
    'Imitate the behaviour of your favourite fictional character',
    'Try not to blink for as long as possible',
    'DM *uwu* to the 3rd person in your Direct Messeges list',
    'Sing your favorite song',
    'Type your name only using your toes and send it in the chat',
    'Show everyone an embarrassing picture of yourself from your childhood',
    'When was the last time you had pizza?',
    'Do any missing homework or assignments or any pending work for at least the next one hour',
    'Drink a glass of water',
    'Rickroll the 5th person in your DMs (Direct Message)',
    'Count up to 100 in one sitting'
]

truth_questions_only = [
    'Have you ever skipped class? If so then which class was it?',
    'Have you ever blamed something you did on someone and have gotten them in trouble?',
    'What is the best meal you have ever had?',
    'What is something you wish you could tell to your younger self?',
    'What is something you regret doing in the past and would like to change?',
    'Have you ever spilled someones secret?',
    'If you could be anyone or anything for 1 hour, who or what would it be?',
    'Have you ever peed the pool?', 'What is your favourite movie?',
    'What is one thing you wish you could change about your parents?',
    'What is one thing you wish you could change about your friends?',
    'Do you know how to tie shoe laces?', 'Do you hold grudges?',
    'Have you ever pulled a prank on someone and it went wrong?',
    'If there were absolutely no consequences whatsoever, what is the one thing you would do?',
    'Have you ever lied to your parents?',
    'What is the longest you have ever gone without showering?',
    'What is the longest you have ever gone without sleeping?',
    'Have you ever broken the law? (i.e. done something illegal)',
    'Do you have a secret that you want no one to know? Would you tell it if you were offered $1 million to do so?',
    'Have you ever cheated on a test?',
    'What is/was your favourite subject in school?',
    'Have you ever shoplifted? From where and what did you take?',
    'Would you consider yourself an introvert, extrovert or an ambivert?',
    'Are you vegetarian? If not then would you be willing to become vegetarian?',
    'Do you like cheese?',
    'What is the one thing you wish you could change about your past?',
    'Do you have any regrets? If so (and if you feel comfortable sharing), what are they?',
    'Have you ever been in a relationship? Are you in one as of now?',
    'Who is your favourite singer?',
    'If you could master one language, which one would it be?',
    'Were you a quiet kid or a loud kid?',
    'What is your biggest (or one of your biggest) fears?',
    'What is your biggest (or one of your biggest) pet peeve?',
    'What is the most embarrassing thing you have ever done?',
    'When was the last time you said a lie?'
    'If you could have dinner with one person, dead or alive, who would it be?',
    'Who would be your *plus 1* to a concert by your favorite artist / band?',
    'Would you consider your sleep schedule to be good/normal?',
    'How many hours did you sleep last night?',
    'When was the last time you ate pizza'
]

dare_questions_only = [
    'Write your name with your non-dominant hand',
    'Give up all forms of social media for the next 10 minutes',
    'Touch some grass (and if you are allergic to grass then go outside for a brief stroll',
    'Give up junk food for the next 16 hours',
    'DM someone the word *meow* and respond to everything they say with *meow* for the next 5 minutes',
    'Let the group pick a profile picture for you to set for the next 24 hours',
    'Do 10 push ups',
    'Close your eyes and type a message and send it in the chat',
    'Only type with your left and for the next 10 minutes',
    'Act like a 5 year old for the next 5 minutes',
    'Talk in an accent for the next 5 minutes',
    'Imitate the behaviour of your favourite fictional character',
    'Try not to blink for as long as possible',
    'DM *uwu* to the 3rd person in your Direct Messeges list',
    'Sing your favorite song',
    'Type your name only using your toes and send it in the chat',
    'Show everyone an embarrassing picture of yourself from your childhood',
    'Do any missing homework or assignments or any pending work for at least the next one hour',
    'Drink a glass of water',
    'Rickroll the 5th person in your DMs (Direct Message)',
    'Count up to 100 in one sitting'
]

list_eight_ball = ["Yes.", "No.", "Maybe.", "I am not sure."]

keep_alive()
TOKEN = os.environ.get("SECRET")
client.run(TOKEN)

