import asyncio

import aiohttp
import pytest

import servus


@pytest.mark.asyncio
async def test_client_get(httpbin):
    session = aiohttp.ClientSession()
    r = await servus.get(session, httpbin.url + "/get/")
    assert type(r.json) == dict, f"{r.json} is not a dict"
    print(r.json)


@pytest.mark.asyncio
async def test_client_post(httpbin):
    session = aiohttp.ClientSession()
    r = await servus.post(session, httpbin.url + "/post/")
    assert type(r.json) == dict, f"{r.json} is not a dict"


@pytest.mark.asyncio
async def test_client_put(httpbin):
    session = aiohttp.ClientSession()
    r = await servus.put(session, httpbin.url + "/put/")
    assert type(r.json) == dict, f"{r.json} is not a dict"


@pytest.mark.asyncio
async def test_client_patch(httpbin):
    session = aiohttp.ClientSession()
    r = await servus.patch(session, httpbin.url + "/patch/")
    assert type(r.json) == dict, f"{r.json} is not a dict"


@pytest.mark.asyncio
async def test_client_delete(httpbin):
    session = aiohttp.ClientSession()
    r = await servus.delete(session, httpbin.url + "/delete/")
    assert type(r.json) == dict, f"{r.json} is not a dict"
