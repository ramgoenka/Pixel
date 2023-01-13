    if message.content.startswith('p;dm help'):
        await message.channel.send(f"""{author.mention} Commands list sent in DM! """)
        embed = discord.Embed(title="Commands :cat:", description='''
__**About Me**:__
``p;help``: Gives a list of commands
``p;dm help``: Sends a direct message (DM) to the user with a list of commands  
``p;about``: Give me a chance to introduce myself! <-- Under Construction :hammer:
``p;ping``: Shows the real time latency (response time) of the bot
                                 
__**Actions**:__
``p;hi``: Say hi to me! 
``p;hug``: Free hug for the user! Everyone deserves a hug :)
``p;random cat``: Sends a random cat image or GIF in the chat
``p;cat``: A cat that responds with meow! 
``p;kitty``: A kitty that responds with meow!
``p;flip``: Flips a coin
``p;roll``: Rolls a 6-sided dice
``p;fact``: Tells you a random fact
__**Math**:__                                   
``pmathadd value1 value2``: Adds two inputted values together
``pmathsubstract value1 value2``: Substracts two inputted values
``pmathmultiply value1 value2``: Multiplies two values inputted by the user
``pmathdivide value1 value2``: Divides two values inputted by the user
``pmathexp value1 value2``: Raises the base (value1) to an exponent (value2)
``pmathfactorial value1``: Finds the factorial of the value inputted
``pmathsqrt value1``: Finds the square root of the value inputted        
``pmathlog value1 value2``: Finds the logrithm of the inputted value (value1) with respect to the inputted base (value2)
                           
__**Games**:__
``p;wyr``: Asks a *would you rather* question
``p;tod``: Asks a random *Truth (T)*  or *Dare (D)* question <-- Under Construction :hammer:
``p;trivia``: Asks a trivia question with the answer hidden in spoilers. Click the spoiler to reveal the answer and check if you are right!
``p;dare``: Gives a dare <-- Under Construction :hammer:
``p;truth``: Asks a question for you to answer, truthfully <-- Under Construction :hammer:''', color=0x00ff00)
        embed.set_footer(text="Thank you for using pixel :)")
        await message.author.send(embed=embed)
    if message.content.startswith('p;help'):
      embed = discord.Embed(title="Commands :cat:", description='''
__**About Me**:__
``p;help``: Gives a list of commands
``p;dm help``: Sends a direct message (DM) to the user with a list of commands  
``p;about``: Give me a chance to introduce myself! <-- Under Construction :hammer:
``p;ping``: Shows the real time latency (response time) of the bot
                                 
__**Actions**:__
``p;hi``: Say hi to me! 
``p;hug``: Free hug for the user! Everyone deserves a hug :)
``p;random cat``: Sends a random cat image or GIF in the chat
``p;cat``: A cat that responds with meow! 
``p;kitty``: A kitty that responds with meow!
``p;flip``: Flips a coin
``p;roll``: Rolls a 6-sided dice
``p;fact``: Tells you a random fact
__**Math**:__                                   
``pmathadd value1 value2``: Adds two inputted values together
``pmathsubstract value1 value2``: Substracts two inputted values
``pmathmultiply value1 value2``: Multiplies two values inputted by the user
``pmathdivide value1 value2``: Divides two values inputted by the user
``pmathexp value1 value2``: Raises the base (value1) to an exponent (value2)
``pmathfactorial value1``: Finds the factorial of the value inputted
``pmathsqrt value1``: Finds the square root of the value inputted        
``pmathlog value1 value2``: Finds the logrithm of the inputted value (value1) with respect to the inputted base (value2)
                           
__**Games**:__
``p;wyr``: Asks a *would you rather* question
``p;tod``: Asks a random *Truth (T)*  or *Dare (D)* question <-- Under Construction :hammer:
``p;trivia``: Asks a trivia question with the answer hidden in spoilers. Click the spoiler to reveal the answer and check if you are right!
``p;dare``: Gives a dare <-- Under Construction :hammer:
``p;truth``: Asks a question for you to answer, truthfully <-- Under Construction :hammer:''', color=0x00ff00)
      embed.set_footer(text="Thank you for using pixel :)")
      await message.channel.send(embed=embed)
