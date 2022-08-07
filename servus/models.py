"""Data objects for Responses and Response Wrappers"""
from dataclasses import dataclass, field
from typing import AnyStr, Dict

from aiohttp import ClientResponse


@dataclass
class AioHttpResponseWrapper:
    """Response Model used for Serializing Response objects"""

    response: ClientResponse
    data: AnyStr = ""
    txt: AnyStr = ""

    # Default of an empty dictionary
    json: Dict = field(default_factory=dict)
