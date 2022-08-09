"""Discord Bot Helpers"""
import aiohttp
from discord.ext import commands


async def create_requests_client(bot: commands.Bot):
    """Create a new async client session for discord Bot instance"""
    bot.session = aiohttp.ClientSession()


async def close_client(client: aiohttp.ClientSession):
    """
    Close a Client Session. Abstraction of lower level session object close

    Parameters
    ----------
    aioclient : aiohttp.ClientSession
        Client Session to close
    """
    await client.close()
