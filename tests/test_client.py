import asyncio

import aiohttp
import pytest

import servus


@pytest.mark.asyncio
async def test_client_get():
    session = aiohttp.ClientSession()
    r = await servus.get(session, "https://reqres.in/api/users?page=2")
    assert type(r.json) == dict, f"{r.json} is not a dict"
