"""Tests for aioimmich."""

from __future__ import annotations

from aioimmich.server.models import (
    ImmichServerAbout,
    ImmichServerStatistics,
    ImmichServerStorage,
)


async def test_get_about_info(mock_immich_with_data):
    """Test async_get_about_info."""
    api = await mock_immich_with_data()
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


async def test_get_storage_info(mock_immich_with_data):
    """Test async_get_storage_info."""
    api = await mock_immich_with_data()
    storage_info = await api.server.async_get_storage_info()

    assert isinstance(storage_info, ImmichServerStorage)
    assert storage_info.disk_available == "136.3 GiB"
    assert storage_info.disk_available_raw == 146403004416
    assert storage_info.disk_size == "294.2 GiB"
    assert storage_info.disk_size_raw == 315926315008
    assert storage_info.disk_usage_percentage == 48.56
    assert storage_info.disk_use == "142.9 GiB"
    assert storage_info.disk_use_raw == 153400406016


async def test_get_server_statistics(mock_immich_with_data):
    """Test async_get_server_statistics."""
    api = await mock_immich_with_data()
    usage_statistics = await api.server.async_get_server_statistics()

    assert isinstance(usage_statistics, ImmichServerStatistics)
    assert usage_statistics.usage == 119525451912
    assert usage_statistics.photos == 27038
    assert usage_statistics.usage_photos == 54291170551
    assert usage_statistics.usage_videos == 65234281361
    assert usage_statistics.videos == 1836
