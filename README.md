


# Servus

[![PyPI version](https://badge.fury.io/py/servus.svg)](https://badge.fury.io/py/servus)
[![PyPI license](https://img.shields.io/pypi/l/servus)](https://pypi.org/project/servus/1.0.0/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

<br>
A wrapper for the aiohttp library for making asynchronous web requests in Python.

Trying to preserve speed and flexibility provided by `aiohttp`, without sacrificing the human-friendliness of `requests`,  `servus` abstracts using client sessions and context managers when making asynchronous HTTP requests in Python.

Example usage:
```py
import servus
import aiohttp
import asyncio

async def main():
	# Create a new session
	my_session = servus.ClientSession()

	# Use Servus to send a request.
	# Servus automatically parses and serializes the response, and returns a ready to use object
	response = await servus.get(my_session, "http://httpbin.org/get")

	print(response.json) # (dict)
	print(response.response) # (aiohttp.ClientResponse)

	# Remeber to close the session!
	my_session.close()

asyncio.run(main())
```

`servus` also has inbuilt support for working with Discord bots.

Example Usage:
```py
import discord
from discord.ext import commands
import asyncio
import servus
from servus.discord_utils import create_requests_client

MY_TOKEN = "<YOUR_TOKEN>"
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))


@bot.command()
async  def hello(ctx):
	"""Hello world, with a HTTP request!"""
	r = await servus.get(bot.session,"https://httpbin.org")
	data = r.json
	await ctx.send(f"World! {data}")

# Add the createRequestClient coroutine to `bot` async loop
bot.loop.create_task(create_requests_client(bot))

# Run the bot
bot.run(MY_TOKEN)
```
