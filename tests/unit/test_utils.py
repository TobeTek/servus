from json import JSONDecodeError

import aiohttp
import pytest

import servus
from servus import __utils


@pytest.mark.asyncio
async def test_parse_response(mock_client_response, mock_client_response_no_data):
    r = await __utils.parse_response(mock_client_response)

    # Existing data is parsed successfully
    assert type(r) == servus.models.AioHttpResponseWrapper
    assert r.json == {"data": "hello world"}
    assert r.data == "hello world"
    assert r.txt == "hello world"

    # Missing data is ignored and defaults are used
    r = await __utils.parse_response(mock_client_response_no_data)

    assert type(r) == servus.models.AioHttpResponseWrapper
    assert r.json == {}
    assert r.data == ""
    assert r.txt == ""
