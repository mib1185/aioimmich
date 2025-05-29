"""Tests for aioimmich."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion

from aioimmich.albums.models import ImmichAlbum


async def test_get_all_albums(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_all_albums."""
    api = await mock_immich_with_data()
    albums = await api.albums.async_get_all_albums()
    assert len(albums) == 2
    assert albums == snapshot


async def test_get_album_info(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_album_info."""
    api = await mock_immich_with_data()

    # get album info without assets
    album = await api.albums.async_get_album_info(
        "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6", True
    )
    assert isinstance(album, ImmichAlbum)
    assert album == snapshot

    # get album info with assets
    album = await api.albums.async_get_album_info(
        "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6", False
    )
    assert isinstance(album, ImmichAlbum)
    assert album == snapshot
