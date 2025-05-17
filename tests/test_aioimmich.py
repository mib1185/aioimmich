"""Tests for aioimmich."""

from __future__ import annotations

import pytest
from aiohttp import ClientError

from aioimmich.albums.models import ImmichAlbum
from aioimmich.assets.models import ImmichAsset
from aioimmich.exceptions import ImmichError, ImmichUnauthorizedError
from aioimmich.server.models import (
    ImmichServerAbout,
    ImmichServerStatistics,
    ImmichServerStorage,
)


async def test_get_all_albums(mock_pegelonline_with_data):
    """Test async_get_all_albums."""
    api = await mock_pegelonline_with_data()
    albums = await api.albums.async_get_all_albums()
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
    album = await api.albums.async_get_album_info(
        "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6", True
    )

    assert isinstance(album, ImmichAlbum)
    assert album.album_id == "721e1a4b-aa12-441e-8d3b-5ac7ab283bb6"
    assert album.asset_count == 4
    assert album.assets == []
    assert album.description == "My first great album"
    assert album.name == "Album 1"
    assert album.thumbnail_asset_id == "0d03a7ad-ddc7-45a6-adee-68d322a6d2f5"

    # get album info with assets
    album = await api.albums.async_get_album_info(
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
    asset_bytes = await api.assets.async_view_asset(
        "2e94c203-50aa-4ad2-8e29-56dd74e0eff4"
    )
    assert isinstance(asset_bytes, bytes)
    assert asset_bytes == b"abcdef"

    # get asset with preview size
    asset_bytes = await api.assets.async_view_asset(
        "2e94c203-50aa-4ad2-8e29-56dd74e0eff4", "preview"
    )
    assert isinstance(asset_bytes, bytes)
    assert asset_bytes == b"abcdefabcdef"

    # get asset with fullsize
    asset_bytes = await api.assets.async_view_asset(
        "2e94c203-50aa-4ad2-8e29-56dd74e0eff4", "fullsize"
    )
    assert isinstance(asset_bytes, bytes)
    assert asset_bytes == b"abcdefabcdefabcdefabcdef"


async def test_get_about_info(mock_pegelonline_with_data):
    """Test async_get_about_info."""
    api = await mock_pegelonline_with_data()
    about_info = await api.server.async_get_about_info()

    assert isinstance(about_info, ImmichServerAbout)
    assert about_info.build == "14709928600"
    assert about_info.build_image == "v1.132.3"
    assert (
        about_info.build_image_url
        == "https://github.com/immich-app/immich/pkgs/container/immich-server"
    )
    assert (
        about_info.build_url
        == "https://github.com/immich-app/immich/actions/runs/14709928600"
    )
    assert about_info.exiftool == "13.00"
    assert about_info.ffmpeg == "7.0.2-7"
    assert about_info.imagemagick == "7.1.1-47"
    assert about_info.libvips == "8.16.1"
    assert about_info.licensed is False
    assert about_info.nodejs == "v22.14.0"
    assert about_info.repository == "immich-app/immich"
    assert about_info.repository_url == "https://github.com/immich-app/immich"
    assert about_info.source_commit == "02994883fe3f3972323bb6759d0170a4062f5236"
    assert about_info.source_ref == "v1.132.3"
    assert (
        about_info.source_url
        == "https://github.com/immich-app/immich/commit/02994883fe3f3972323bb6759d0170a4062f5236"
    )
    assert about_info.version == "v1.132.3"
    assert (
        about_info.version_url
        == "https://github.com/immich-app/immich/releases/tag/v1.132.3"
    )


async def test_get_storage_info(mock_pegelonline_with_data):
    """Test async_get_storage_info."""
    api = await mock_pegelonline_with_data()
    storage_info = await api.server.async_get_storage_info()

    assert isinstance(storage_info, ImmichServerStorage)
    assert storage_info.disk_available == "136.3 GiB"
    assert storage_info.disk_available_raw == 146403004416
    assert storage_info.disk_size == "294.2 GiB"
    assert storage_info.disk_size_raw == 315926315008
    assert storage_info.disk_usage_percentage == 48.56
    assert storage_info.disk_use == "142.9 GiB"
    assert storage_info.disk_use_raw == 153400406016


async def test_get_server_statistics(mock_pegelonline_with_data):
    """Test async_get_server_statistics."""
    api = await mock_pegelonline_with_data()
    usage_statistics = await api.server.async_get_server_statistics()

    assert isinstance(usage_statistics, ImmichServerStatistics)
    assert usage_statistics.usage == 119525451912
    assert usage_statistics.photos == 27038
    assert usage_statistics.usage_photos == 54291170551
    assert usage_statistics.usage_videos == 65234281361
    assert usage_statistics.videos == 1836


async def test_errors(mock_pegelonline_with_data):
    """Test api errors."""
    api = await mock_pegelonline_with_data()

    with pytest.raises(ImmichError, match="Not found or no album.read access"):
        await api.albums.async_get_album_info("INVALID_ALBUM_ID")

    with pytest.raises(ImmichUnauthorizedError, match="Invalid API key"):
        await api.albums.async_get_album_info("INVALID_API_KEY")

    with pytest.raises(ClientError):
        await api.albums.async_get_album_info("CLIENT_ERROR")
