from dataclasses import dataclass, field
from json import JSONDecodeError
from typing import Any, AnyStr, Dict

import pytest


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#           aiohttp               #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
@dataclass
class MockAioClientResponse:
    """Mock object for aiohttp ClientResponse"""

    response_json: Dict = field(default_factory=lambda: {"data": "hello world"})
    response_data: AnyStr = "hello world"
    response_txt: AnyStr = "hello world"

    has_json: bool = True
    has_data: bool = True
    has_txt: bool = True

    async def json(self):
        if not self.has_json:
            raise JSONDecodeError("No JSON", "Mock Response", 0)

        return self.response_json

    async def data(self):
        if not self.has_data:
            raise Exception("No data")

        return self.response_data

    async def txt(self):
        if not self.has_txt:
            raise Exception("No txt")

        return self.response_txt


@pytest.fixture
def mock_client_response():
    return MockAioClientResponse()


@pytest.fixture
def mock_client_response_no_data():
    return MockAioClientResponse(has_json=False, has_data=False, has_txt=False)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
#           discord.py            #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
class MockDiscordBot:
    pass


@pytest.fixture
def mock_bot():
    return MockDiscordBot()
