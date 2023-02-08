import discord
from discord.ext import commands
import asyncio

# set the password
password = "secret"
client = discord.Client()
responded = False
# create the bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='hello')
async def hello(ctx):
    global responded
    if not responded:
        await ctx.send("Hello!")
        responded = True
        await asyncio.sleep(2) # Wait for 30 seconds
        responded = False # Reset the response

@bot.command(name='register')
async def register(ctx):
    # prompt the user for a password
    await ctx.send("Please enter the password:")

    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    # wait for the user's response
    msg = await bot.wait_for('message', check=check)

    # check if the password is correct
    if msg.content == password:
        # give the user the role
        role = discord.utils.get(ctx.guild.roles, name="registered")
        await ctx.author.add_roles(role)
        await ctx.send("Registration successful! You now have the 'registered' role.")
    else:
        await ctx.send("Incorrect password.")


bot.run('your_token')
