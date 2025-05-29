"""Tests for aioimmich."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion

from aioimmich.users.models import ImmichUserObject


async def test_get_my_user(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_my_user."""
    api = await mock_immich_with_data()
    user = await api.users.async_get_my_user()

    assert isinstance(user, ImmichUserObject)
    assert user == snapshot
