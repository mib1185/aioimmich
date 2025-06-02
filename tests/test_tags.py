"""Tests for aioimmich."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion


async def test_get_all_tags(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_all_tags."""
    api = await mock_immich_with_data()
    tags = await api.tags.async_get_all_tags()

    assert len(tags) == 3
    assert tags == snapshot
