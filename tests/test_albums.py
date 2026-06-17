"""Tests for aioimmich."""

from __future__ import annotations

import json

from syrupy.assertion import SnapshotAssertion

from aioimmich.albums.models import ImmichAddAssetsToAlbumResponse, ImmichAlbum

from .const import MOCK_IMMICH_HOST


async def test_get_all_albums_v2(
    mock_immich_with_data, mock_aiointercept, snapshot: SnapshotAssertion
):
    """Test async_get_all_albums with api v2."""
    mock_aiointercept.get(
        f"https://{MOCK_IMMICH_HOST}:2283/api/server/version",
        status=200,
        body=json.dumps({"major": 2, "minor": 7, "patch": 0}),
        repeat=2,
    )
    api = await mock_immich_with_data()
    albums = await api.albums.async_get_all_albums()
    assert len(albums) == 3
    assert albums == snapshot


async def test_get_all_albums(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_all_albums."""
    api = await mock_immich_with_data()
    albums = await api.albums.async_get_all_albums()
    assert len(albums) == 3
    assert albums == snapshot


async def test_get_album_info(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_album_info."""
    api = await mock_immich_with_data()

    # get album info without assets
    album = await api.albums.async_get_album_info(
        "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6"
    )
    assert isinstance(album, ImmichAlbum)
    assert album == snapshot


async def test_add_assets_to_album(mock_immich_with_data, mock_aiointercept):
    """Test async_add_assets_to_album."""
    api = await mock_immich_with_data()

    # test successful adding of assets
    result = await api.albums.async_add_assets_to_album(
        "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6", ["abcdef-0123456789"]
    )
    mock_aiointercept.assert_called_with(
        "https://localhost:2283/api/albums/721e1a4b-aa12-441e-8d3b-5ac7ab283bb6/assets",
        "put",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        data=None,
        json={"ids": ["abcdef-0123456789"]},
    )
    assert isinstance(result, list)
    assert result[0] == ImmichAddAssetsToAlbumResponse.from_dict(
        {
            "id": "abcdef-0123456789",
            "success": True,
        }
    )

    # test unsuccessful adding of assets
    result = await api.albums.async_add_assets_to_album(
        "c4721c25-8669-451f-a6be-3d9d4dc38f5f", ["abcdef-0123456789"]
    )
    mock_aiointercept.assert_called_with(
        "https://localhost:2283/api/albums/c4721c25-8669-451f-a6be-3d9d4dc38f5f/assets",
        "put",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        data=None,
        json={"ids": ["abcdef-0123456789"]},
    )
    assert isinstance(result, list)
    assert result[0] == ImmichAddAssetsToAlbumResponse.from_dict(
        {"id": "abcdef-0123456789", "success": False, "error": "duplicate"}
    )
