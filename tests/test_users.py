"""Tests for aioimmich."""

from __future__ import annotations

from dateutil import parser

from aioimmich.users.models import AvatarColor, ImmichUser, UserStatus


async def test_get_my_user(mock_pegelonline_with_data):
    """Test async_get_my_user."""
    api = await mock_pegelonline_with_data()
    user = await api.users.async_get_my_user()

    assert isinstance(user, ImmichUser)
    assert user.avatar_color == AvatarColor.PRIMARY
    assert user.created_at == parser.isoparse("2025-05-11T10:07:46.866Z")
    assert user.deleted_at is None
    assert user.email == "admin@immich.local"
    assert user.is_admin is True
    assert user.name == "admin"
    assert user.oauth_id == ""
    assert user.profile_changed_at == parser.isoparse("2025-05-11T10:07:46.866Z")
    assert user.profile_image_path == ""
    assert user.quota_size_in_bytes is None
    assert user.quota_usage_in_bytes == 119526467534
    assert user.should_change_password is True
    assert user.status is UserStatus.ACTIVE
    assert user.storage_label == "admin"
    assert user.updated_at == parser.isoparse("2025-05-18T00:59:55.547Z")
    assert user.user_id == "e7ef5713-9dab-4bd4-b899-715b0ca4379e"
