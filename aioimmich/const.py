"""aioimmich constants."""

import asyncio
import logging

import aiohttp

LOGGER = logging.getLogger(__package__)

CONNECT_ERRORS = (
    aiohttp.ClientError,
    asyncio.TimeoutError,
    OSError,
)
