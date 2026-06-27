"""Tests for aioimmich."""

from __future__ import annotations

import json

from syrupy.assertion import SnapshotAssertion

from .const import MOCK_IMMICH_HOST


async def test_get_all_assets(
    mock_immich_with_data, mock_aiointercept, snapshot: SnapshotAssertion
):
    """Test async_get_all."""
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all()
    mock_aiointercept.assert_called_with(
        "https://localhost:2283/api/search/metadata",
        "post",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        json={"size": 100, "page": 1},
    )
    assert len(assets) == 4
    assert assets == snapshot


async def test_get_all_favorite_assets(
    mock_immich_with_data, mock_aiointercept, snapshot: SnapshotAssertion
):
    """Test async_get_all_favorites."""
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all_favorites()
    mock_aiointercept.assert_called_with(
        "https://localhost:2283/api/search/metadata",
        "post",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        json={"size": 100, "isFavorite": True, "page": 1},
    )
    assert len(assets) == 4
    assert assets == snapshot


async def test_get_all_by_tag_ids(
    mock_immich_with_data, mock_aiointercept, snapshot: SnapshotAssertion
):
    """Test async_get_all_by_tag_ids."""
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all_by_tag_ids(
        ["14ce3af3-67be-41c6-b77c-b25abddaf546"]
    )
    mock_aiointercept.assert_called_with(
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
    mock_immich_with_data, mock_aiointercept, snapshot: SnapshotAssertion
):
    """Test async_get_all_by_person_ids."""
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all_by_person_ids(
        ["14ce3af3-67be-41c6-b77c-b25abddaf546"]
    )
    mock_aiointercept.assert_called_with(
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


async def test_get_all_by_album_ids(
    mock_immich_with_data, mock_aiointercept, snapshot: SnapshotAssertion
):
    """Test async_get_all_by_album_ids."""
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all_by_album_ids(
        ["14ce3af3-67be-41c6-b77c-b25abddaf546"]
    )
    mock_aiointercept.assert_called_with(
        "https://localhost:2283/api/search/metadata",
        "post",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        json={
            "size": 100,
            "albumIds": ["14ce3af3-67be-41c6-b77c-b25abddaf546"],
            "page": 1,
        },
    )
    assert len(assets) == 4
    assert assets == snapshot


async def test_get_all_by_album_ids_v2(
    mock_immich_with_data, mock_aiointercept, snapshot: SnapshotAssertion
):
    """Test async_get_all_by_album_ids with api v2."""
    mock_aiointercept.get(
        f"https://{MOCK_IMMICH_HOST}:2283/api/server/version",
        status=200,
        body=json.dumps({"major": 2, "minor": 7, "patch": 0}),
        repeat=2,
    )
    api = await mock_immich_with_data()
    assets = await api.search.async_get_all_by_album_ids(
        ["14ce3af3-67be-41c6-b77c-b25abddaf546"]
    )
    mock_aiointercept.assert_called_with(
        "https://localhost:2283/api/albums/14ce3af3-67be-41c6-b77c-b25abddaf546",
        "get",
        headers={"Accept": "application/json", "x-api-key": "abcdef1234567890"},
        params=None,
        json=None,
    )
    assert len(assets) == 4
    assert assets == snapshot
