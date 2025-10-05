"""Tests for aioimmich."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion


async def test_get_all_people(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_all_tags."""
    api = await mock_immich_with_data()
    people = await api.people.async_get_all_people(page_size=3, max_pages=1)

    assert len(people) == 3
    assert people == snapshot


async def test_get_people_count(mock_immich_with_data):
    """Test async_get_people_count."""
    api = await mock_immich_with_data()
    count = await api.people.async_get_people_count()

    assert count == 3
