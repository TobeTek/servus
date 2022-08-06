# flake8: noqa
"""
Servus Python Library
~~~~~~~~~~~~~~~~~~~~~

Servus is a wrapper library for `aiohttp`,
useful for making intuitive and concise asynchronous web requests in Python.

:copyright: (c) 2022 by Emmanuel K.
:license: Apache 2.0, see LICENSE for more details.
"""

__author__ = "TobeTek"
__version__ = "1.0.0"

# flake:noqa
from aiohttp import ClientSession

from . import models
from .requests import *
