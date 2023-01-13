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
    if message.content.startswith('hello'):
        await message.channel.send(
            f"""Hello {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('Hello'):
        await message.channel.send(
            f"""Hello {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('p;Hi'):
        await message.channel.send(
            f"""Hi {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('p;hi'):
        await message.channel.send(
            f"""Hi {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('Hey'):
        await message.channel.send(
            f"""Hey {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if message.content.startswith('hey'):
        await message.channel.send(
            f"""Hey {author.mention}! I Hope you have a great day!""")
        await message.add_reaction('\U0001F44B')
    if any(word in msg for word in sad):
        await message.channel.send(random.choice(encouraging_words))
    if message.content.startswith('p;kitty'):
        await message.channel.send('meow :cat:')
        await message.add_reaction('\U0001F431')
    if message.content.startswith('p;Kitty'):
        await message.add_reaction('\U0001F431')
        await message.channel.send('meow :cat:')
    if message.content.startswith('p;cat'):
        await message.add_reaction('\U0001F431')
        await message.channel.send('meow :cat:')
    if message.content.startswith('p;Cat'):
        await message.add_reaction('\U0001F431')
        await message.channel.send('meow :cat:')
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
    if message.content.startswith('p;flip'):
        await message.channel.send(random.choice(coin_outcomes))
        await message.add_reaction('\U0001FA99')
    if message.content.startswith('p;Flip'):
        await message.channel.send(random.choice(coin_outcomes))
        await message.add_reaction('\U0001FA99')
    if message.content.startswith('p;roll'):
        await message.channel.send(random.choice(dice_roll))
    if message.content.startswith('p;Roll'):
        await message.channel.send(random.choice(dice_roll))
    if message.content.startswith('gn'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good Night & sweet dreams! :sleeping:')
    if message.content.startswith('GN'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good Night & sweet dreams! :sleeping:')
    if message.content.startswith('Gn'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good Night & sweet dreams! :sleeping:')
    if message.content.startswith('Goodnight'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good Night & sweet dreams! :sleeping:')
    if message.content.startswith('goodnight'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good Night & sweet dreams! :sleeping:')
    if message.content.startswith('p;ping'):
        await message.channel.send(
            f'**Bot latency**: {client.latency * 10000} ms')
    if message.content.startswith('good night'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good Night & sweet dreams! :sleeping:')
    if message.content.startswith('Good night'):
        await message.add_reaction('\U0001F634')
        await message.channel.send('Good Night & sweet dreams! :sleeping:')
    if message.content.startswith('gm'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good Morning! Hope you have a great day :sunny:')
    if message.content.startswith('Gm'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good Morning! Hope you have a great day :sunny:')
    if message.content.startswith('Goodmorning'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good Morning! Hope you have a great day :sunny:')
    if message.content.startswith('Good morning'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good Morning! Hope you have a great day :sunny:')
    if message.content.startswith('goodmorning'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good Morning! Hope you have a great day :sunny:')
    if message.content.startswith('good morning'):
        await message.add_reaction('\U0001F304')
        await message.channel.send(
            'Good Morning! Hope you have a great day :sunny:')
    if message.content.startswith('p;wyr'):
        await message.channel.send(random.choice(wyr_questions))
    if message.content.startswith('p;fact'):
        await message.channel.send(random.choice(random_facts))
    if message.content.startswith('p;trivia'):
        await message.channel.send(random.choice(trivia_questions))
    if message.content.startswith('I appreciate pixel'):
        await message.channel.send('Aww! I appreciate you too :blush:')
    if message.content.startswith('i appreciate pixel'):
        await message.channel.send('Aww! I appreciate you too :blush:')
    if message.content.startswith('p;random cat'):
        embed = discord.Embed(title="Meow :cat:", description="", color=0x00FFFF)
        embed.set_image(url=random.choice(cat_images))
        await message.channel.send(embed=embed)  
    if message.content.startswith('p;hug'):
        embed = discord.Embed(title="", description=f"""{author.mention} Here is a hug for you :)""", color=0xFF00FF)
        embed.set_image(url=random.choice(hug_gif))
        await message.channel.send(embed=embed) 
#NEED TO FULLY UPDATE
