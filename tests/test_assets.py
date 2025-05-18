"""Tests for aioimmich."""

from __future__ import annotations


async def test_view_asset(mock_immich_with_data):
    """Test async_view_asset."""
    api = await mock_immich_with_data()

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
