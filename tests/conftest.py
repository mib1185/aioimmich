"""Test config for aioimmich."""

from __future__ import annotations

import json
from typing import Any, AsyncGenerator, Generator

import aiohttp
import pytest
from aioresponses import aioresponses

from aioimmich import Immich

from .const import (
    MOCK_DATA,
    MOCK_DATA_ALBUM_1_ASSETS,
    MOCK_IMMICH_API_KEY,
    MOCK_IMMICH_HOST,
)


class MockImmich(Immich):
    """Immich test double that allows per-instance overrides."""


@pytest.fixture(name="mock_aioresponse")
def m_aioresponse() -> Generator[aioresponses, Any, None]:
    """Mock a web request and provide a response."""
    with aioresponses() as m:
        yield m


@pytest.fixture(name="mock_immich")
async def m_immich() -> AsyncGenerator[MockImmich, Any]:
    """Return Immich session."""
    session = aiohttp.ClientSession()
    immich = MockImmich(session, MOCK_IMMICH_API_KEY, MOCK_IMMICH_HOST)
    yield immich
    await session.close()


@pytest.fixture
def mock_immich_with_data(mock_aioresponse, mock_immich):
    """Comfort fixture to initialize immich session."""

    async def data_to_immich() -> Immich:
        """Initialize immich session."""
        for path, data in MOCK_DATA.items():
            mock_aioresponse.get(
                f"https://{MOCK_IMMICH_HOST}:2283/api/{path}",
                status=data["status"],
                body=data["body"],
                exception=data.get("exception"),
                repeat=data.get("repeat", 1),
            )
        mock_aioresponse.post(
            f"https://{MOCK_IMMICH_HOST}:2283/api/search/metadata",
            body=json.dumps(
                {"assets": {"items": MOCK_DATA_ALBUM_1_ASSETS, "nextPage": None}}
            ),
        )
        mock_aioresponse.post(
            f"https://{MOCK_IMMICH_HOST}:2283/api/assets",
            status=201,
            body=json.dumps({"id": "abcdef-0123456789", "status": "created"}),
        )

        mock_aioresponse.put(
            f"https://{MOCK_IMMICH_HOST}:2283/api/albums/721e1a4b-aa12-441e-8d3b-5ac7ab283bb6/assets",
            body=json.dumps([{"id": "abcdef-0123456789", "success": True}]),
        )
        mock_aioresponse.put(
            f"https://{MOCK_IMMICH_HOST}:2283/api/albums/c4721c25-8669-451f-a6be-3d9d4dc38f5f/assets",
            body=json.dumps(
                [{"id": "abcdef-0123456789", "success": False, "error": "duplicate"}]
            ),
        )

        await mock_immich.async_setup()
        return mock_immich

    return data_to_immich
