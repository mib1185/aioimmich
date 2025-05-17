"""Test config for aioimmich."""

from __future__ import annotations

import json

import aiohttp
import pytest
from aioresponses import aioresponses

from aioimmich import Immich

from .const import MOCK_DATA, MOCK_IMMICH_API_KEY, MOCK_IMMICH_HOST


@pytest.fixture
def mock_aioresponse():
    """Mock a web request and provide a response."""
    with aioresponses() as m:
        yield m


@pytest.fixture
async def mock_immich():
    """Return Immich session."""
    session = aiohttp.ClientSession()
    api = Immich(session, MOCK_IMMICH_API_KEY, MOCK_IMMICH_HOST)
    yield api
    await session.close()


@pytest.fixture
def mock_pegelonline_with_data(mock_aioresponse, mock_immich):
    """Comfort fixture to initialize immich session."""

    async def data_to_immich() -> Immich:
        """Initialize PegelOnline session."""
        for path, data in MOCK_DATA.items():
            mock_aioresponse.get(
                f"https://{MOCK_IMMICH_HOST}:2283/api/{path}",
                status=data["status"],
                body=json.dumps(data["body"]),
                exception=data.get("exception"),
            )
        return mock_immich

    return data_to_immich
