# flake8: noqa
"""
An example of a discord bot that makes use of `servus` to make asynchronous web requests
`bot.session` holds the Client session that the bot makes use of throughout its lifecycle

"""

import discord
from discord.ext import commands

import servus

MY_TOKEN = "<YOUR_TOKEN>"

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))


@bot.event
async def on_ready():
    """On ready event!"""
    print("Logged in as " + str(bot.user))
    print("User ID: " + str(bot.user.id))
    r = await servus.get(bot.session, "https://reqres.in/api/users?page=2")
    print(r)

    print("Ready!")


@bot.command()
async def ping(ctx):
    """Ping pong!"""
    latency = ctx.bot.latency
    latency = latency * 1000
    latency = round(latency)
    await ctx.send("Pong! My ping is **{}ms**!".format(latency))


@bot.command()
async def hello(ctx):
    """Hello world!"""
    r = await servus.get(bot.session, "https://reqres.in/api/users?page=2")
    print(r)
    data = r.json
    await ctx.send(f"World! {data}")


@bot.command()
async def world(ctx):
    """World, hello!"""
    await ctx.send("Hello!")


@bot.command()
async def slap(ctx, user: discord.Member = None):
    if user is None:
        message = "I don't wanna slap you!"
    else:
        message = "{} was slapped by {}! *ouch*".format(
            ctx.author.mention, user.mention
        )
    await ctx.send(message)


# Add the createRequestClient coroutine to `bot` async loop
bot.loop.create_task(servus.discord_utils.createRequestsClient(bot))

# Run the bot
bot.run(MY_TOKEN)
