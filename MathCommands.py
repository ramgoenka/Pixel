#command prefix is 'pmat'

#INTEGRAL CALCULATOR
    if message.content.startswith('pmathintegral'):
        try:
            words = message.content.split(None, 1)
            x = symbols('x')
            result = integrate(words[1], x)
            await message.channel.send(f"Result: ```{result}```")
        except IndexError:
            await message.channel.send("No function to integrate. Please enter a function to integrate and try again! Use ``p;info integral`` to learn how to use this feature.")

@client.command()
async def hadd(ctx, num1: int, num2: int):
  a = num1+num2
  await ctx.send(f"**Result:** {a}")

@client.command()
async def hsubstract(ctx, num1: int, num2: int):
  a = num1-num2
  await ctx.send(f"**Result:** {a}")

@client.command()
async def hmultiply(ctx, num1: int, num2: int):
  a = num1*num2
  await ctx.send(f"**Result:** {a}")  

@client.command()
async def hdivide(ctx, num1: int, num2: int):
  a = num1/num2
  await ctx.send(f"**Result:** {a}")

@client.command()
async def hexp(ctx, num1: int, num2: int):
  a = num1**num2
  await ctx.send(f"**Result:** {a}")

@client.command()
async def hsqrt(ctx, num1: int):
  a = num1**0.5
  await ctx.send(f"**Result:** {a}")  

@client.command()
async def hfactorial(ctx, num1: int):
  a = math.factorial(num1)
  await ctx.send(f"**Result:** {a}") 

@client.command()
async def hlog(ctx, num1: int, num2: int):
  a = math.log(num1, num2)
  await ctx.send(f"**Result:** {a}")
