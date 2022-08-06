from json import JSONDecodeError

import aiohttp

from .models import AioHttpResponseWrapper


async def parse_response(resp: aiohttp.ClientResponse):
    """
    Parse ClientResponse

    Extract response object properties so they can be accessed synchronously
    e.g JSON, text and Binary data fields

    Parameters
    ----------
    resp : aiohttp.ClientResponse
        Async Response object

    Returns
    -------
    AioHttpResponseWrapper
        Wrapped response that provides synchronous access response properties
    """
    # Create data with default values
    data = dict.fromkeys(["json", "response", "txt", "data"])

    data["response"] = resp
    try:
        data["json"] = await resp.json()

    except JSONDecodeError:
        # No JSON was returned
        pass

    try:
        data["txt"] = await resp.txt()

    except Exception:
        pass

    try:
        data["data"] = await resp.data()
    except Exception:
        pass

    # Create a new ResponseWrapper and pass in extracted values
    return AioHttpResponseWrapper(**data)
