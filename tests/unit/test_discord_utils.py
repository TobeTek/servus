from json import JSONDecodeError
from re import L

import aiohttp
import pytest

import servus
from servus import discord_utils


@pytest.mark.asyncio
async def test_client_create_and_close(mock_bot):
    await discord_utils.create_requests_client(mock_bot)
    assert type(mock_bot.session) == aiohttp.ClientSession

    await discord_utils.close_client(mock_bot.session)
    assert mock_bot.session.closed == True
