"""Tests for aioimmich."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion

from aioimmich.server.models import (
    ImmichServerAbout,
    ImmichServerStatistics,
    ImmichServerStorage,
)


async def test_get_about_info(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_about_info."""
    api = await mock_immich_with_data()
    about_info = await api.server.async_get_about_info()

    assert isinstance(about_info, ImmichServerAbout)
    assert about_info == snapshot


async def test_get_storage_info(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_storage_info."""
    api = await mock_immich_with_data()
    storage_info = await api.server.async_get_storage_info()

    assert isinstance(storage_info, ImmichServerStorage)
    assert storage_info == snapshot


async def test_get_server_statistics(
    mock_immich_with_data, snapshot: SnapshotAssertion
):
    """Test async_get_server_statistics."""
    api = await mock_immich_with_data()
    usage_statistics = await api.server.async_get_server_statistics()

    assert isinstance(usage_statistics, ImmichServerStatistics)
    assert usage_statistics == snapshot
