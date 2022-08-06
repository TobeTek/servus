from typing import Dict, AnyStr
from dataclasses import dataclass
from aiohttp import ClientResponse


@dataclass
class AioHttpResponseWrapper:
    """Response Model used for Serializing Response objects"""

    response: ClientResponse
    data: AnyStr
    txt: AnyStr

    json: Dict = {}
