"""Tests for aioimmich."""

from __future__ import annotations

import pytest
from aiohttp import ClientError

from aioimmich.exceptions import ImmichError, ImmichUnauthorizedError
from aioimmich.models import ImmichAlbum, ImmichAsset


async def test_get_all_albums(mock_pegelonline_with_data):
    """Test async_get_all_albums."""
    api = await mock_pegelonline_with_data()
    albums = await api.async_get_all_albums()
    assert len(albums) == 2

    album = albums[0]
    assert isinstance(album, ImmichAlbum)
    assert album.album_id == "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6"
    assert album.asset_count == 4
    assert album.assets == []
    assert album.description == "My first great album"
    assert album.name == "Album 1"
    assert album.thumbnail_asset_id == "0d03a7ad-ddc7-45a6-adee-68d322a6d2f5"

    album = albums[1]
    assert isinstance(album, ImmichAlbum)
    assert album.album_id == "c4721c25-8669-451f-a6be-3d9d4dc38f5f"
    assert album.asset_count == 426
    assert album.assets == []
    assert album.description == "Not so great second album"
    assert album.name == "Album 2"
    assert album.thumbnail_asset_id == "6961329c-d8ee-4f09-9d4e-6997ea5b7bf4"


async def test_get_album_info(mock_pegelonline_with_data):
    """Test async_get_album_info."""
    api = await mock_pegelonline_with_data()

    # get album info without assets
    album = await api.async_get_album_info("721e1a4b-aa12-441e-8d3b-5ac7ab283bb6", True)

    assert isinstance(album, ImmichAlbum)
    assert album.album_id == "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6"
    assert album.asset_count == 4
    assert album.assets == []
    assert album.description == "My first great album"
    assert album.name == "Album 1"
    assert album.thumbnail_asset_id == "0d03a7ad-ddc7-45a6-adee-68d322a6d2f5"

    # get album info with assets
    album = await api.async_get_album_info(
        "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6", False
    )

    assert isinstance(album, ImmichAlbum)
    assert album.album_id == "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6"
    assert album.asset_count == 4
    assert len(album.assets) == 4
    for asset in album.assets:
        assert isinstance(asset, ImmichAsset)
    assert album.description == "My first great album"
    assert album.name == "Album 1"
    assert album.thumbnail_asset_id == "0d03a7ad-ddc7-45a6-adee-68d322a6d2f5"


async def test_view_asset(mock_pegelonline_with_data):
    """Test async_view_asset."""
    api = await mock_pegelonline_with_data()

    # get asset with default size
    asset_bytes = await api.async_view_asset("2e94c203-50aa-4ad2-8e29-56dd74e0eff4")
    assert isinstance(asset_bytes, bytes)
    assert asset_bytes == b"abcdef"

    # get asset with preview size
    asset_bytes = await api.async_view_asset(
        "2e94c203-50aa-4ad2-8e29-56dd74e0eff4", "preview"
    )
    assert isinstance(asset_bytes, bytes)
    assert asset_bytes == b"abcdefabcdef"

    # get asset with fullsize
    asset_bytes = await api.async_view_asset(
        "2e94c203-50aa-4ad2-8e29-56dd74e0eff4", "fullsize"
    )
    assert isinstance(asset_bytes, bytes)
    assert asset_bytes == b"abcdefabcdefabcdefabcdef"


async def test_errors(mock_pegelonline_with_data):
    """Test api errors."""
    api = await mock_pegelonline_with_data()

    with pytest.raises(ImmichError, match="Not found or no album.read access"):
        await api.async_get_album_info("INVALID_ALBUM_ID")

    with pytest.raises(ImmichUnauthorizedError, match="Invalid API key"):
        await api.async_get_album_info("INVALID_API_KEY")

    with pytest.raises(ClientError):
        await api.async_get_album_info("CLIENT_ERROR")
