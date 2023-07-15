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
import pytz
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import sympy

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
spell = Speller(lang='en')
client = commands.Bot(
    intents=intents,
    command_prefix=['pmat', 'pt', 'pr', 'pc', 'pp', 'pd', 'ps', 'pb', 'pf'])
cookies = {}
poll_emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
yes_no_emojis = ['👍', '👎']
x = symbols('x')

#CODE
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Type p;help"))

@client.event
async def on_message(message):
    await client.process_commands(message)
    global active
    if message.author == client.user:
        return
    msg = message.content
    author = message.author

    #INTEGRAL CALCULATOR
    if message.content.startswith('p;integral'):
        try:
            words = message.content.split(None, 1)
            x = symbols('x')
            result = integrate(words[1], x)
            await message.channel.send(f"**Result:** ```{result}```")
        except IndexError:
            await message.channel.send(
                "No function to integrate. Please enter a function to integrate and try again! Use ``p;info pmathintegral`` to learn how to use this feature."
            )
    if message.content.startswith("hola"):
        await message.channel.send(
            f"""Hola {author.mention}! I Hope you have a great day!""")
    if message.author.id not in ignore_list and message.content.lower() == "hello":
        await message.channel.send(
            f"""Hello {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith("Hola"):
        await message.channel.send(
            f"""Hola {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('🥺'):
        num_emojis = message.content.count('🥺')
        await message.channel.send('🥺' * num_emojis)
    if message.content.startswith("HOLA"):
        await message.channel.send(
            f"""Hola {author.mention}! I Hope you have a great day!""")
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
    if message.content.startswith('p;calculate'):
        expression = ' '.join(message.content.split()[1:])
        allowed_chars = set('0123456789+-*/() ')
        if set(expression).issubset(allowed_chars):
            try:
                result = sympy.sympify(expression)
                await message.channel.send(f"**Result:** ```{result}```")
            except Exception as e:
                await message.channel.send(f"Error in calculation: {str(e)}")
        else:
            await message.channel.send("Invalid characters in expression. Only numbers and +, -, *, /, (, ) are allowed.")
    await client.process_commands(message)
    if message.content.startswith('Hewwo'):
        await message.channel.send(
            f"""Hewwo {author.mention}! To check out my commands please type ``p;help``. I Hope you have a great day!"""
        )
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('hewwo'):
        await message.channel.send(
            f"""Hewwo {author.mention}! To check out my commands please type ``p;help``. I Hope you have a great day!"""
        )
    if message.content.startswith('HEWWO'):
        await message.channel.send(
            f"""Hewwo {author.mention}! To check out my commands please type ``p;help``. I Hope you have a great day!"""
        )
    if message.content.startswith('p;Hi'):
        await message.channel.send(
            f"""Hi {author.mention}! To check out my commands please type ``p;help``. I Hope you have a great day!"""
        )
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('p;hi'):
        await message.channel.send(
            f"""Hi {author.mention}! To check out my commands please type ``p;help``. I Hope you have a great day!"""
        )
    hey_word = ['hey']
    lc = message.content.lower()
    if any(lc.startswith(keyword) for keyword in hey_word):
        await message.add_reaction('\U0001F44B')
        await message.channel.send(f"""Hey {author.mention}! I Hope you have a great day!""")
    await client.process_commands(message)
    if any(word in msg for word in sad):
        await message.channel.send(random.choice(encouraging_words))
    kitty_words = ['meow', 'kitty', 'cat']
    lowercase_content = message.content.lower()
    if any(lowercase_content.startswith(keyword) for keyword in kitty_words):
        await message.add_reaction('\U0001F431')
        await message.channel.send('meow :cat:')
    await client.process_commands(message)
    if message.content.startswith('p;poll'):
        poll_message = message.content[6:]
        poll_options = poll_message.split('-')
        question = poll_options[0].strip()
        options = [option.strip() for option in poll_options[1:]]
        if len(options) > 10:
            await message.channel.send("Sorry, maximum number of options is 10.")
            return
        poll_embed = discord.Embed(title=question, description='\n'.join([f'{poll_emojis[i]} {option}' for i, option in enumerate(options)]))
        poll = await message.channel.send(embed=poll_embed)
        if options[0].lower() == "yes" and options[1].lower() == "no":
            for emoji in yes_no_emojis:
                await poll.add_reaction(emoji)
        else:
            for emoji in poll_emojis[:len(options)]:
                await poll.add_reaction(emoji)
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
                await message.channel.send(f':cookie: {message.author.mention} has given a cookie to {user.mention}! :cookie:'
                )
    if message.content.startswith('p;hug'):
        embed = discord.Embed(
            title="",
            description=f'''{author.mention} Here is a hug for you :)''',
            color=0xe78be7)
        embed.set_image(url=random.choice(hug_gif))
        embed.set_footer(text="Hope you have a great day :D")
        await message.channel.send(embed=embed)
    choices = ["rock", "paper", "scissors"]
    if message.content.startswith("p;rps"):
        args = message.content.split()
        if len(args) != 2 or args[1].lower() not in choices:
            await message.channel.send("Invalid choice. Choose one: rock, paper, or scissors.")
            return
        user_choice = args[1].lower()
        bot_choice = random.choice(choices)
        await message.channel.send(f"You chose **{user_choice}**. I chose **{bot_choice}**.")
        if user_choice == bot_choice:
            await message.channel.send("It's a **tie**!")
        elif (user_choice == "rock" and bot_choice == "scissors") or \
                (user_choice == "paper" and bot_choice == "rock") or \
                (user_choice == "scissors" and bot_choice == "paper"):
            await message.channel.send("**You** win!")
        else:
            await message.channel.send("**I** win!")
        await client.process_commands(message)
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
    if message.content.startswith('p;translate'):
        try:
            _, to_language, *text = message.content.split()
            text = ' '.join(text)
            translator= Translator(to_lang=to_language)
            translation = translator.translate(text)
            await message.channel.send(translation)
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")
    await client.process_commands(message)
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
    if message.content.startswith('good morning'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good morning! Hope you have a great day :sunny:')
    if message.content.startswith('Good morning'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good morning! Hope you have a great day :sunny:')
    if message.content.startswith('p;structure'):
        try:
            _, *compound_parts = message.content.split()
            compound = ' '.join(compound_parts)
            compound_encoded = requests.utils.quote(compound)
            image_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_encoded}/PNG"
            response = requests.get(image_url)
            if response.status_code == 200:
                img = Image.open(BytesIO(response.content))
                img = img.resize((img.width * 2, img.height * 2))
                img_byte_arr = BytesIO()
                img.save(img_byte_arr, format='PNG')
                img_byte_arr = img_byte_arr.getvalue()
                image_file = discord.File(BytesIO(img_byte_arr), filename="structure.png")
                await message.channel.send(file=image_file)
            else:
                await message.channel.send("Sorry, I couldn't find a structure for that compound.")
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")
    if message.content.startswith('p;binary'):
        decimal = int(message.content.split(' ')[1])
        binary = bin(decimal)[2:]
        await message.channel.send(
            f'The binary equivalent of {decimal} is: **{binary}**.')
    if message.content.startswith('p;avatar'):
        try:
            member = message.mentions[0] if message.mentions else message.author
            embed = discord.Embed(title = f"{member}'s avatar", color = discord.Color.blurple())
            embed.set_image(url = member.avatar_url)
            await message.channel.send(embed=embed)
        except Exception as e:
            await message.channel.send(f"An error occurred: {str(e)}")
    await client.process_commands(message)
    if message.content.startswith('p;wyr'):
        embed = discord.Embed(title='Would you rather...',
                              description=random.choice(wyr_questions),
                              color=0xFF6600)
        await message.channel.send(embed=embed)  
    if message.content.startswith('p;tod'):
        embed = discord.Embed(title=random.choice(random_tod),
                              description='Truth or Dare',
                              color=0xFF6600)
        await message.channel.send(embed=embed)
    if message.content.startswith('p;random_fact'):
        embed = discord.Embed(title="Did you know...",
                              description=random.choice(random_facts),
                              color=0xadd8e6)
        await message.channel.send(embed=embed)
    if message.content.startswith("p;server_count"):
        await message.channel.send(f"I am in currently in ``{len(client.guilds)}`` servers!")
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
    if message.author.id not in ignore_list and client.user in message.mentions:
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
      

    if message.content.startswith("p;"):
        command = message.content.split(";", 1)[1].strip()

        if command.startswith("countdown "):
            _, seconds = command.split()
            seconds = int(seconds)
            message = await message.channel.send(f'{seconds} seconds left!')
            while seconds > 0:
                await asyncio.sleep(1)
                seconds -= 1
                await message.edit(content=f'{seconds} seconds left!')
            await message.channel.send(f'{message.author.mention}, the countdown you set is complete!')

        elif command.startswith("find_time "):
            _, timezone = command.split(" ", 1)
            try:
                tz = pytz.timezone(timezone)
                current_time = datetime.datetime.now(tz)
                await message.channel.send(f'The current time at **{timezone}** is **{current_time.strftime("%H:%M:%S")}**.')
            except pytz.exceptions.UnknownTimeZoneError: 
                await message.channel.send("Could not find the time for the inputted timezone/location.")

        elif command.startswith("gcd "):
            _, num1, num2 = command.split()
            num1, num2 = int(num1), int(num2)
            a = max(num1, num2)
            b = min(num1, num2)
            while b != 0:
                temp = b
                b = a % b
                a = temp
            await message.channel.send(f"**Result:** ```{a}```")

        elif command.startswith("pi "):
            _, digits = command.split()
            digits = int(digits)
            if digits > 1000:
                await message.channel.send("Sorry, I only know up to 1000 digits of pi.")
            else:
                mpmath.mp.dps = digits
                pi_value = str(mpmath.pi)
                await message.channel.send(f"The first **{digits}** digits of pi are: ```{pi_value}```")

        elif command.startswith("exp "):
            _, num1, num2 = command.split()
            num1, num2 = int(num1), int(num2)
            result = num1**num2
            await message.channel.send(f"**Result:** ```{result}```")

        elif command.startswith("sqrt "):
            _, num = command.split()
            num = int(num)
            result = num**0.5
            await message.channel.send(f"**Result:** ```{result}```")
          
        elif command.startswith("factorial "):
            _, num = command.split()
            num = int(num)
            result = math.factorial(num)
            await message.channel.send(f"**Result:** ```{result}```")
        elif command.startswith("log "):
            _, num1, num2 = command.split()
            num1, num2 = int(num1), int(num2)
            result = math.log(num1, num2)
            await message.channel.send(f"**Result:** ```{result}```")
        elif command.startswith("log "):
            _, num1, num2 = command.split()
            num1, num2 = int(num1), int(num2)
            result = math.log(num1, num2)
            await message.channel.send(f"**Result:** ```{result}```")
        elif command.startswith("balance "):
            _, equation = command.split(" ", 1)
            try:
                reactants, products = equation.split('->')
                reactants = reactants.split('+')
                products = products.split('+')
                balanced = balance_stoichiometry(reactants, products)
                balanced_eq = ' + '.join([f'{v} {k}' for k, v in balanced[0].items()]) + ' -> ' + ' + '.join([f'{v} {k}' for k, v in balanced[1].items()])
                await message.channel.send(f'__The balanced chemical equation is:__ {balanced_eq}')
            except Exception as e:
                await message.channel.send(f'Error: {str(e)}')
        elif command.startswith("plot "):
            _, func = command.split(" ", 1)
            x = np.linspace(-10, 10, 400)
            y_func = np.frompyfunc(lambda x: eval(func), 1, 1)
            y = y_func(x).astype(np.float)
            plt.figure()
            plt.plot(x, y)
            plt.axhline(0, color='black',linewidth=1.0)
            plt.axvline(0, color='black',linewidth=1.0)
            plt.grid(True)
            plt.title(func)
            plt.ylim([-20, 20])
            with BytesIO() as image_binary:
                plt.savefig(image_binary, format='png')
                image_binary.seek(0)
                await message.channel.send(file=discord.File(fp=image_binary, filename='plot.png'))
        elif command.startswith("define "):
            _, word = command.split(" ", 1)
            url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()[0]['meanings'][0]['definitions'][0]['definition']
                await message.channel.send(f"**{word}**: {data}")
            else:
                await message.channel.send(f"Sorry, I couldn't find the definition for **{word}**.")
        elif command.startswith("remindme "):
            _, time, unit, reminder = command.split(" ", 3)
            try:
                time = int(time)
                unit = unit.lower()
                if unit in ["second", "seconds"]:
                    await message.channel.send(
                        f"{message.author.mention}, I will make sure to remind you: **{reminder}**"
                    )
                    await asyncio.sleep(time)
                elif unit in ["minute", "minutes"]:
                    await message.channel.send(
                        f"{message.author.mention}, I will make sure to remind you: **{reminder}**"
                    )
                    await asyncio.sleep(time * 60)
                elif unit in ["hour", "hours"]:
                    await message.channel.send(
                        f"{message.author.mention}, I will make sure to remind you: **{reminder}**"
                    )
                    await asyncio.sleep(time * 60 * 60)
                elif unit in ["day", "days"]:
                    await message.channel.send(
                        f"{message.author.mention}, I will make sure to remind you: **{reminder}**"
                    )
                    await asyncio.sleep(time * 60 * 60 * 24)
                else:
                    await message.channel.send(
                        f"{message.author.mention}, please provide a valid time unit (second/seconds/minute/minutes/hour/hours/day/days)."
                    )
                    return
                await message.channel.send(
                    f"{message.author.mention}, you asked me to remind you: **{reminder}**"
                )
            except ValueError:
                await message.channel.send(
                    f"{message.author.mention}, please provide a valid time (integer)."
                )

                await client.process_commands(message)
        elif command.startswith("serverinfo"):
            name = str(message.guild.name)
            description = str(message.guild.description) if message.guild.description else ""
            owner_id = message.guild.owner_id
            owner = await client.fetch_user(int(owner_id))
            id = str(message.guild.id)
            memberCount = str(message.guild.member_count)
            creation_date = message.guild.created_at.strftime("%B %d, %Y")
            icon_url = str(message.guild.icon.url) if message.guild.icon else None
            embed = discord.Embed(
                title=name + " Information",
                description=description,
                color=discord.Color.blue()
            )
            if icon_url:
                embed.set_thumbnail(url=icon_url)
            embed.add_field(name="Owner", value=owner, inline=True)
            embed.add_field(name="Server ID", value=id, inline=True)
            embed.add_field(name="Member Count", value=memberCount, inline=True)
            embed.add_field(name="Created On", value=creation_date, inline=True)
            await message.channel.send(embed=embed)
            await client.process_commands(message)
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

    if message.content.startswith('p;info poll'):
        embed = discord.Embed(title="__**poll**__ :ballot_box:",
                              description='''
Use this command to create a poll with a question and upto 10 options. For example, if the user wishes to ask the question: "What is the best animal?", with the options: "Cats Dogs Lions Tigers", then they must type ``p;poll What is the best animal? - Cats - Dogs - Lions - Tigers`` and the bot will create a poll with reactions for members to be able to react and show their choice. For yes or no style questions, the user must type "yes" or "no" as the options. For example: ``p;poll Should I get a haircut? - Yes - No``. Note that after the poll question, the user must use a "-" before mentioning the first option and then put a "-" to add a new option as shown in the examples above.
                          
__**Syntax**__
p;poll''',
                              color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info define'):
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

    if message.content.startswith("p;info gcd"):
        embed = discord.Embed(
            title="__**math: greatest common divisor**__ :asterisk:",
            description=
            '''This command can be used to calculate the greatest common divisor (gcd) of two numbers. To use this command, the user must type ``p;gcd`` and then the two numbers they desire to calculate the gcd for. For example if a user wishes to find the gcd of ``4`` and ``2`` they must type ``p;gcd 4 2`` and the bot will respond with the result which is ``2``.

__**Syntax**__
p;gcd''',
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

    if message.content.startswith('p;info random_fact'):
        embed = discord.Embed(
            title="__**fact**__ :books:",
            description=
            '''Tells you a random fact, because who doesn't enjoy a random cool fact :)

__**Syntax**__
p;random_fact''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info plot'):
        embed = discord.Embed(
            title="__**math: plot**__ :chart_with_upwards_trend:",
            description=
            '''Returns the image of the graph of a given function. To use the command, the user must first type ``p;plot`` followed by the function they wish to generate the graph for. For example, if the user want's to graph the function ``x^2 + 2x + 4 = 0``, they must type ``p;plot x**2 + 2*x + 4`` and the bot will return an image of the plot of the function. If the user wishes to plot a logarithmic, trigonometric or square root function, they must type the following respectively: ``p;plot k * np.log(x)``, ``p;plot k * np.trigfunction(x)``, ``p;plot k * np.sqrt(x)``, where ``k`` is some numerical constant.

__**Syntax**__
p;plot''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info calculate'):
        embed = discord.Embed(
            title="__**math: calculate**__ :abacus:",
            description=
            '''This command allows the bot to function as a 4-function calculator. Followed by the command name (``p;calculate``), the user must provide with the expression they wish. For example, if the user wishes to calculate ``8 + 11 - 4 + 3 * 4`` then they must type ``p;calculate 8 + 11 - 4 + 3 * 4`` and the bot will return the result, which is ``27``. Note that order of operations matter and that ``8 + 11 - 4 + 3 * 4`` is not the same as ``8 + 11 - (4 + 3) * 4`` as the inputting the latter in the bot will output ``-9``. Use ``+`` for addition, ``-`` for subtraction, ``*`` for multiplication, and ``/`` for division. 

__**Syntax**__
p;calculate''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info pi'):
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

    if message.content.startswith('p;info exp'):
        embed = discord.Embed(
            title='__**math: exponent**__ <:exponent:982926856103796736>',
            description=
            '''Followed by the function (``p;exp``), the user must input two numeric values and pixel will give the output as the result where the first value is the base and the second value is the exponent (ex. ``p;exp 2 4`` <-- this will result in pixel giving an output of 16, which is the result when 2 is raised to 4).
                            
__**Syntax**__
p;exp''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info countdown'):
        embed = discord.Embed(
            title='__**countdown...**__ :hourglass_flowing_sand:',
            description=
            '''Allows the user to set a countdown timer for ``x`` amount of seconds. For example, if a user wants to set a timer for ``30`` seconds, the user can type ``p;countdown 30`` and the bot will display a message that shows the remaining time left in the countdown and will ping the user when the countdown is over.
                            
__**Syntax**__
p;countdown''',
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

    if message.content.startswith('p;info factorial'):
        embed = discord.Embed(
            title='__**math: factorial**__ <:factorial:982929962946424862>',
            description=
            '''Followed by the function (``p;factorial``), the user must input one numeric value and pixel will give the output as the factorial of the inputted value (ex. ``p;factorial 4`` <-- this will result in pixel giving an output of 24, which is the factorial of 4).
                            
__**Syntax**__
p;factorial''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info sqrt'):
        embed = discord.Embed(
            title='__**math: square root**__ <:squareRoot:982932222820614194>',
            description=
            '''Followed by the function (``p;sqrt``), the user must input one numeric value and pixel will give the output as the result of the sqaure root of the inputted value (ex. ``p;sqrt 4`` <-- this will result in pixel giving an output of 2, which is the sqaure root of 4).
                            
__**Syntax**__
p;sqrt''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info remindme'):
        embed = discord.Embed(
            title='__**remind me!**__ :timer:',
            description=
            '''The ``p;remindme`` command allows the user to set a reminder for themselves for any amount of time they desire to. To use this command, the user must first type ``p;remindme`` and then follow it by the amount of time and units and the reminder they want to set. An example of this would be: ``p;remindme 10 minutes go for a walk``, the bot will ping the user after 10 minutes reminding them that they need to go for a walk. Note that only the following units are acceptable and in must be written in the command in the following manner only: ``seconds``, ``seconds``, ``minute``, ``minutes``, ``hour``, ``hours``, ``day``, ``days``. The case of the input does not matter (i.e. the bot will accept: Second, SeCONds, SeconD, so the case of the letters in the input does not matter). 
          
__**Syntax**__
p;remindme''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info log'):
        embed = discord.Embed(
            title='__**math: logrithm**__ :wood:',
            description=
            '''Followed by the function (``pmathlog``), the user must input two numeric values and pixel will give the output as the result of a logrithm where the first inputted value is what we want to find the logrithm of, and the second inputted value is the base of the logrithm. (ex. ``pmathlog 4 2`` <-- this will result in pixel giving an output of 2, which is the logrithmic value given that 4 is the value we want to find the logirthm for and 2 is the base).
                            
__**Syntax**__
p;log''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info integral'):
        embed = discord.Embed(
            title='__**math: integral**__ :man_teacher:',
            description=
            '''Followed by the function ``(p;integral)``, the user must input some mathemtaical function f(x) for which they wish to find the integral of. Here are ways to interpret the result: For example if the user inputs the function ``x``, the output will be ``x**2/2`` which means ``x`` to the second power, divided by two                        

__**Syntax**__
p;integral''',
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

    if message.content.startswith('p;info server_count'):
        embed = discord.Embed(
            title='__**server count**__ :bar_chart:',
            description=
            '''Use this command to check the number of Discord servers Pixel is currently in!
                            
__**Syntax**__
p;server_count''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

  
    if message.content.startswith('p;info balance'):
        embed = discord.Embed(
            title='__**balance **__ :test_tube:',
            description=
            '''Use this command to balance a chemical reaction equation. To use this command, the user must type ``p;balance`` and then the chemical reaction they wish to balance. For example if the user wishes to balance the chemical reaction ``H2 + O2 -> H2O`` they must type ``p;balance H2 + O2 -> H2O`` and the bot will respond with the balance chemical reaction equation!
                            
__**Syntax**__
p;balance''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)
      
    if message.content.startswith('p;info rps'):
        embed = discord.Embed(
            title='__**rock paper scissors**__ :rock: :scroll: :scissors:',
            description=
            '''Use this command to play a game of rock paper scissors with Pixel! To use this command, type ``prps`` followed by your move, for example ``p;rps rock`` if you want to use rock, and Pixel will reply with its move!

__**Syntax**__
p;rps''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info serverinfo'):
        embed = discord.Embed(
            title='__**server information**__ :page_facing_up:',
            description=
            '''Use this command to get information about the Discord server (that the command is being used in). Using this command results in the bot replaying with server information such as the username of the server owner, the date the server was created, the server ID, the server logo and the member count of the server. 

__**Syntax**__
p;serverinfo''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info translate'):
        embed = discord.Embed(
            title='__**translate**__ :speech_left:',
            description=
            '''Use this command to translate any text from english to any other language the user wishes to! To use this command, you must type ``p;translate`` followed by the two letter prefix of the language you wish to translate the text to. For example ``p;translate es today is a good day`` will translate the text "today is a good day" from english to spanish. The bot uses the standard ``ISO 639-1`` language prefix for translation, so when translating to a language, please refer to the table of ``ISO 639-1`` language codes, which can be found here: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes 
Please note that the bot does not support every single one of these languages and the bot will indicate if it does not support a particular language by returning an error instead of the translated text!

__**Syntax**__
p;translate''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)
          
    if message.content.startswith('p;info structure'):
        embed = discord.Embed(
            title='__**structure**__ :scientist:',
            description=
            '''Using this command, a user can request the bot to output the chemical structure of a given chemical compound. For example if the user wishes to output the chemical compound of ``methane``, the user can type ``p;structure methane`` and the bot will then respond with an image of the chemical structure of ``methane``. 

__**Syntax**__
p;structure''',
            color=0x00FFFF)
        embed.set_footer(
            text=random.choice(embed_footers),
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        embed.timestamp = datetime.datetime.utcnow()
        await message.channel.send(embed=embed)

    if message.content.startswith('p;info find_time'):
        embed = discord.Embed(
            title='__**find time**__ :clock:',
            description=
            '''Command information to be added soon!

__**Syntax**__
p;find_time''',
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
• ``p;info <command>``: For more detailed information about a specific command (ex. p;help flip)
• ``p;dm help``: Sends a DM to the user with a list of commands  
• ``p;about``: Give me a chance to introduce myself!
• ``p;ping``: Shows the response time of pixel 
• ``p;server_count``: Shows the number of servers I am in

__**Actions**:__
• ``p;hi``: Say hi to me! 
• ``p;hug``: Hug for the user!
• ``p;cat``: Sends a random cat image or GIF in the chat
• ``p;flip``: Flips a coin
• ``p;roll``: Rolls a 6-sided dice
• ``p;random_fact``: Tells you a random fact
• ``p;remindme <number> <unit> <reminder>``: Allows the user to set a reminder for themselves. Type ``p;info remindme`` for more information. 
• ``p;countdown x``: Allows the user to set a countdown timer for ``x`` amount of seconds.
• ``p;poll question - option(s)``: Allows the user to set up a poll with upto 10 options. Type ``p;info poll`` for detailed information.
• ``p;define <word>``: Allows the user to type in a word from the English language that they wish to find the definition for. 
• ``p;cookie <@user>``: Give a cookie to someone in the Discord server! 
• ``p;countchar text``: Counts the number of characters in a given text. 
• ``p;autocorrect text``: Autocorrects a given text by finding any issues with it. Please type ``p;info autocorrect`` for more details. 
• ``p;binary n``: Converts a decimal ``n`` to binary. 
• ``p;8ball <question>``: Use this command to ask the bot a yes/no style question.
• ``p;translate <prefix> <text>``: Translates a given text in English to a language chosen by the user!
• ``p;balance <chemical reaction>``: Balances a given chemical reaction.
• ``p;structure <chemical compound>``: Returns the structure of a given chemical compound.
• ``p;serverinfo``: Sends information about the Discord server. Type ``p;info pserverinfo`` for detailed information. 
• ``p;find_time``: Information to be added

__**Math**:__                                   
• ``p;calculate <expression to operate>``: Works as a simple 4-function calculator. Type ``p;info calculate`` for a detailed description!
• ``p;exp x y``: Raises the base (x) to an exponent (y)
• ``p;factorial x``: Finds the factorial of the value inputted
• ``p;sqrt x``: Finds the square root of the value inputted     
• ``p;log x y``: Finds the logrithm of the inputted value (x) with respect to the inputted base (y)
• ``p;integral f(x)``: Finds the integral of a given function, please use ``p;info integral`` to learn more!
• ``p;gcd x y``: Finds the greatest common divisor between the two given numbers. 
• ``p;pi n``: Sends the first ``n`` digits of pi.
• ``p;solve f(x)``: Finds the solution to a function ``f(x)``. Type the command ``p;info solve`` for more information!  
• ``p;plot f(x)``: Returns the graph of a given function. For detailed information on useage type ``p;info plot``

__**Games**:__
• ``p;wyr``: Asks a *would you rather* question
• ``p;tod``: Asks a random *Truth*  or *Dare* question
• ``p;trivia``: Asks a trivia question!
• ``p;dare``: Gives a dare
• ``p;truth``: Asks a question for you to answer, truthfully
• ``p;rps``: Plays a game of rock, paper, scissors with the user. You must input your move with the command, for example if you want to use ``rock`` you must type ``p;rps rock``''',
                              color=0xFFFF00)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(
            url=
            ""
        )
        embed.set_footer(
            text="Have a nice day :D",
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        await message.author.send(embed=embed)
  
    if message.content.startswith('p;help'):
        embed = discord.Embed(title="Commands :cat:",
                              description='''
__**About Me**:__
• ``p;help``: Gives a list of commands
• ``p;info <command>``: For more detailed information about a specific command (ex. p;help fact)
• ``p;dm help``: Sends a DM to the user with a list of commands  
• ``p;about``: Give me a chance to introduce myself!
• ``p;ping``: Shows the response time of pixel
• ``p;server_count``: Shows the number of servers I am in

__**Actions**:__
• ``p;hi``: Say hi to me! 
• ``p;hug``: Hug for the user!
• ``p;cat``: Sends a random cat image or GIF in the chat
• ``p;flip``: Flips a coin
• ``p;roll``: Rolls a 6-sided dice
• ``p;random_fact``: Tells you a random fact
• ``p;remindme <number> <unit> <reminder>``: Allows the user to set a reminder for themselves. Type ``p;info remindme`` for more information. 
• ``p;countdown x``: Allows the user to set a countdown timer for ``x`` amount of seconds.
• ``p;poll question - option(s)``: Allows the user to set up a poll with upto 10 options. Type ``p;info poll`` for detailed information.
• ``p;define <word>``: Allows the user to type in a word from the English language that they wish to find the definition for. 
• ``p;cookie <@user>``: Give a cookie to someone in the Discord server! 
• ``p;countchar text``: Counts the number of characters in a given text. 
• ``p;autocorrect text``: Autocorrects a given text by finding any issues with it. Please type ``p;info autocorrect`` for more details. 
• ``p;binary n``: Converts a decimal ``n`` to binary. 
• ``p;8ball <question>``: Use this command to ask the bot a yes/no style question.
• ``p;translate <prefix> <text>``: Translates a given text in English to a language chosen by the user!
• ``pbalance <chemical reaction>``: Balances a given chemical reaction.
• ``p;structure <chemical compound>``: Returns the structure of a given chemical compound.
• ``p;serverinfo``: Sends information about the Discord server. Type ``p;info pserverinfo`` for detailed information. 
• ``p;find_time``: Information to be added

__**Math**:__                                   
• ``p;calculate <expression to operate>``: Works as a simple 4-function calculator. Type ``p;info calculate`` for a detailed description!
• ``p;exp x y``: Raises the base (x) to an exponent (y)
• ``p;factorial x``: Finds the factorial of the value inputted
• ``p;sqrt x``: Finds the square root of the value inputted     
• ``p;log x y``: Finds the logrithm of the inputted value (x) with respect to the inputted base (y)
• ``p;integral f(x)``: Finds the integral of a given function, please use ``p;info pmathintegral`` to learn more!
• ``p;gcd x y``: Finds the greatest common divisor between the two given numbers. 
• ``p;pi n``: Sends the first ``n`` digits of pi.
• ``p;solve f(x)``: Finds the solution to a function ``f(x)``. Type the command ``p;info solve`` for more information!  
• ``p;plot f(x)``: Returns the graph of a given function. For detailed information on useage type ``p;info pmathgraph``

__**Games**:__
• ``p;wyr``: Asks a *would you rather* question
• ``p;tod``: Asks a random *Truth*  or *Dare* question
• ``p;trivia``: Asks a trivia question!
• ``p;dare``: Gives a dare
• ``p;truth``: Asks a question for you to answer, truthfully
• ``p;rps``: Plays a game of rock, paper, scissors with the user. You must input your move with the command, for example if you want to use ``rock`` you must type ``p;rps rock``''',
                              color=0xFFFF00)
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_thumbnail(
            url=
            ""
        )
        embed.set_footer(
            text="Have a nice day :D",
            icon_url=
            "https://cdn.discordapp.com/avatars/978663279926870046/b43a03b91e449bfeb318823d64c8b7fc.png?size=4096"
        )
        await message.channel.send(embed=embed)

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
    ":thinking: In which state is *Mount Rushmore* located? (Answer: || South Dakota ||)",
    ":thinking: What is the capital of Bhutan? (Answer: || Thimphu ||)",
    ":thinking: What is the chemical symbol for the element Silver? (Answer: || Ag ||)",
    ":thinking: What is the capital of Spain? (Answer: || Madrid ||)",
    ":thinking: Which nation won the 2022 FIFA Mens World Cup? And where was it hosted? (Answer: || Argentina won the FIFA Mens World Cup in 2022 which was hosted in Qatar ||)",
    ":thinking: Who discovered the law of universal graviation?  (Answer: || Sir Isaac Newton ||)",
    ":thinking: What is the capital of Japan? (Answer: || Tokyo ||)",
    ":thinking: Who won the 2022-2023 Premier League Golden Boot (Answer: || Erling Haaland ||)",
    ":thinking: Who composed ``Für Elise``? (Answer: || Ludwig van Beethoven ||)", 
    ":thinking: What is the scientific name for the process plants use to convert sunlight into food? (Answer: || Photosynthesis ||)",
    ":thinking: True or False: Dubai is the capital of the United Arab Emirates (Answer: || False. The capital of the U.A.E. is Abu Dhabi ||)",
    ":thinking: In which year did the Russian October Revolution begin? (Answer: || 1917 ||)",
    ":thinking: "
  
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

ignore_list = ['837011037894737951']

keep_alive()
TOKEN = os.environ.get("SECRET")
client.run(TOKEN)
