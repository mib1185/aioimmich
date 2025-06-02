"""Tests for aioimmich."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion


async def test_get_all_assets(
    mock_immich_with_data, mock_aioresponse, snapshot: SnapshotAssertion
):
    """Test async_get_all."""
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all()
    mock_aioresponse.assert_called_with(
        "https://localhost:2283/api/search/metadata",
        "post",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        json={"size": 100, "page": 1},
    )
    assert len(assets) == 4
    assert assets == snapshot


async def test_get_all_by_tag_ids(
    mock_immich_with_data, mock_aioresponse, snapshot: SnapshotAssertion
):
    """Test async_get_all_by_tag_ids."""
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all_by_tag_ids(
        ["14ce3af3-67be-41c6-b77c-b25abddaf546"]
    )
    mock_aioresponse.assert_called_with(
        "https://localhost:2283/api/search/metadata",
        "post",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        json={
            "size": 100,
            "tagIds": ["14ce3af3-67be-41c6-b77c-b25abddaf546"],
            "page": 1,
        },
    )
    assert len(assets) == 4
    assert assets == snapshot


async def test_get_all_by_person_ids(
    mock_immich_with_data, mock_aioresponse, snapshot: SnapshotAssertion
):
    """Test async_get_all_by_person_ids."""
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all_by_person_ids(
        ["14ce3af3-67be-41c6-b77c-b25abddaf546"]
    )
    mock_aioresponse.assert_called_with(
        "https://localhost:2283/api/search/metadata",
        "post",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        json={
            "size": 100,
            "personIds": ["14ce3af3-67be-41c6-b77c-b25abddaf546"],
            "page": 1,
        },
    )
    assert len(assets) == 4
    assert assets == snapshot
