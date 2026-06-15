"""Tests for aioimmich."""

from __future__ import annotations

from unittest.mock import AsyncMock

import pytest
from aiohttp import ClientError

from aioimmich.exceptions import (
    ImmichError,
    ImmichForbiddenError,
    ImmichMissingSetup,
    ImmichNotFoundError,
    ImmichUnauthorizedError,
)


async def test_missing_setup(mock_immich_with_data, mock_immich):
    """Test missing setup errors."""
    mock_immich.async_setup = AsyncMock()
    api = await mock_immich_with_data()
    with pytest.raises(ImmichMissingSetup):
        await api.server.async_get_about_info()


async def test_errors(mock_immich_with_data):
    """Test api errors."""
    api = await mock_immich_with_data()

    with pytest.raises(ImmichError, match="Not found or no album.read access"):
        await api.albums.async_get_album_info("INVALID_ALBUM_ID")

    with pytest.raises(ImmichUnauthorizedError, match="Invalid API key"):
        await api.albums.async_get_album_info("INVALID_API_KEY")

    with pytest.raises(ImmichForbiddenError, match="Forbidden"):
        await api.albums.async_get_album_info("FORBIDDEN")

    with pytest.raises(ImmichNotFoundError, match="Not Found"):
        await api.albums.async_get_album_info("NOTFOUND")

    with pytest.raises(ClientError):
        await api.albums.async_get_album_info("CLIENT_ERROR")
