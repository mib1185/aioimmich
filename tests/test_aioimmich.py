"""Tests for aioimmich."""

from __future__ import annotations

import pytest
from aiohttp import ClientError

from aioimmich.exceptions import (
    ImmichError,
    ImmichForbiddenError,
    ImmichNotFoundError,
    ImmichUnauthorizedError,
)


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
