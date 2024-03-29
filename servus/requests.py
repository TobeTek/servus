"""
HTTP Requests API

A module that exposes HTTP verbs/requests to end users

TODO: Implement HEAD and OPTIONS methods
"""

from aiohttp import ClientSession

from . import __utils as _utils


async def get(session: ClientSession, url: str, **params):
    """
    Send an asynchronous GET request

    Parameters
    ----------
    session : ClientSession
        aiohttp ClientSession used to make requests
    url : str
        The URL endpoint

    Returns
    -------
    AioHttpResponseWrapper
        Final Response returned by the function.
    """
    async with session.get(url, **params) as resp:
        fresp = await _utils.parse_response(resp)
    return fresp


async def post(session: ClientSession, url, **params):
    """
    Send an asynchronous POST request

    Parameters
    ----------
    session : ClientSession
        aiohttp ClientSession used to make requests
    url : str
        The URL endpoint

    Returns
    -------
    AioHttpResponseWrapper
        Final Response returned by the function.
    """
    async with session.post(url, **params) as resp:
        fresp = await _utils.parse_response(resp)
    return fresp


async def put(session: ClientSession, url, **params):
    """
    Send an asynchronous PUT request

    Parameters
    ----------
    session : ClientSession
        aiohttp ClientSession used to make requests
    url : str
        The URL endpoint

    Returns
    -------
    AioHttpResponseWrapper
        Final Response returned by the function.
    """
    async with session.put(url, **params) as resp:
        fresp = await _utils.parse_response(resp)
    return fresp


async def patch(session: ClientSession, url, **params):
    """
    Send an asynchronous PATCH request

    Parameters
    ----------
    session : ClientSession
        aiohttp ClientSession used to make requests
    url : str
        The URL endpoint

    Returns
    -------
    AioHttpResponseWrapper
        Final Response returned by the function.
    """
    async with session.patch(url, **params) as resp:
        fresp = await _utils.parse_response(resp)
    return fresp


async def delete(session: ClientSession, url, **params):
    """
    Send an asynchronous DELETE request

    Parameters
    ----------
    session : ClientSession
        aiohttp ClientSession used to make requests
    url : str
        The URL endpoint

    Returns
    -------
    AioHttpResponseWrapper
        Final Response returned by the function.
    """
    async with session.delete(url, **params) as resp:
        fresp = await _utils.parse_response(resp)
    return fresp
