#command prefix is 'pmath'

@client.command()
async def add(ctx, num1: int, num2: int):
  a = num1+num2
  await ctx.send(f"**Result:** {a}")

@client.command()
async def substract(ctx, num1: int, num2: int):
  a = num1-num2
  await ctx.send(f"**Result:** {a}")

@client.command()
async def multiply(ctx, num1: int, num2: int):
  a = num1*num2
  await ctx.send(f"**Result:** {a}")  

@client.command()
async def divide(ctx, num1: int, num2: int):
  a = num1/num2
  await ctx.send(f"**Result:** {a}")

@client.command()
async def exp(ctx, num1: int, num2: int):
  a = num1**num2
  await ctx.send(f"**Result:** {a}")

@client.command()
async def sqrt(ctx, num1: int):
  a = num1**0.5
  await ctx.send(f"**Result:** {a}")  

@client.command()
async def factorial(ctx, num1: int):
  a = math.factorial(num1)
  await ctx.send(f"**Result:** {a}") 

@client.command()
async def log(ctx, num1: int, num2: int):
  a = math.log(num1, num2)
  await ctx.send(f"**Result:** {a}")
