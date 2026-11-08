"""Tests for aioimmich."""

from __future__ import annotations

import json

import pytest
from aiohttp import ClientResponse, StreamReader

from aioimmich.assets.models import ImmichAssetUploadResponse, UploadStatus
from aioimmich.exceptions import ImmichNotFoundError

from .const import MOCK_IMMICH_HOST

VIDEO_ID = "2e65a5f2-db83-44c4-81ab-f5ff20c9bd7b"
VIDEO_URL = f"https://{MOCK_IMMICH_HOST}:2283/api/assets/{VIDEO_ID}/video/playback"


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

    # get the edited asset
    asset_bytes = await api.assets.async_view_asset(
        "2e94c203-50aa-4ad2-8e29-56dd74e0eff4", edited=True
    )
    assert isinstance(asset_bytes, bytes)
    assert asset_bytes == b"abcdefabcdefabcdefabcdefabcdef"


async def test_upload_asset(mock_immich_with_data, mock_aiointercept, tmp_path):
    """Test async_upload_asset."""
    test_file = tmp_path / "image.png"
    test_file.write_bytes(b"abcdef")

    api = await mock_immich_with_data()
    result = await api.assets.async_upload_asset(test_file.as_posix())
    assert isinstance(result, ImmichAssetUploadResponse)
    assert result.asset_id == "abcdef-0123456789"
    assert result.status is UploadStatus.CREATED


async def test_play_video_stream(mock_immich_with_data, mock_aiointercept):
    """Test async_play_video_stream."""
    mock_aiointercept.get(VIDEO_URL, body=b"abcdef")

    api = await mock_immich_with_data()
    stream = await api.assets.async_play_video_stream(VIDEO_ID)
    assert isinstance(stream, StreamReader)
    assert await stream.read() == b"abcdef"


async def test_open_video_stream(mock_immich_with_data, mock_aiointercept):
    """Test async_open_video_stream."""
    mock_aiointercept.get(VIDEO_URL, body=b"abcdef")

    api = await mock_immich_with_data()
    resp = await api.assets.async_open_video_stream(VIDEO_ID)
    assert isinstance(resp, ClientResponse)
    async with resp:
        assert resp.status == 200
        assert await resp.content.read() == b"abcdef"
    assert resp.closed
    mock_aiointercept.assert_called_with(
        VIDEO_URL,
        headers={"Accept": "application/octet-stream", "x-api-key": "abcdef1234567890"},
    )


async def test_open_video_stream_range(mock_immich_with_data, mock_aiointercept):
    """Test async_open_video_stream with a range header."""
    mock_aiointercept.get(
        VIDEO_URL,
        status=206,
        body=b"cd",
        headers={"Content-Range": "bytes 2-3/6", "Accept-Ranges": "bytes"},
    )

    api = await mock_immich_with_data()
    async with await api.assets.async_open_video_stream(
        VIDEO_ID, range_header="bytes=2-3"
    ) as resp:
        assert resp.status == 206
        assert resp.headers["Content-Range"] == "bytes 2-3/6"
        assert await resp.content.read() == b"cd"
    mock_aiointercept.assert_called_with(
        VIDEO_URL,
        headers={
            "Accept": "application/octet-stream",
            "x-api-key": "abcdef1234567890",
            "Range": "bytes=2-3",
        },
    )


async def test_open_video_stream_release_unread(
    mock_immich_with_data, mock_aiointercept
):
    """Test that an unread video stream can be released."""
    mock_aiointercept.get(VIDEO_URL, body=b"abcdef" * 100000)

    api = await mock_immich_with_data()
    resp = await api.assets.async_open_video_stream(VIDEO_ID)
    async with resp:
        assert await resp.content.read(6) == b"abcdef"
    assert resp.closed
    assert resp.connection is None


async def test_open_video_stream_not_found(mock_immich_with_data, mock_aiointercept):
    """Test async_open_video_stream with an unknown asset."""
    mock_aiointercept.get(
        VIDEO_URL,
        status=404,
        body=json.dumps(
            {
                "message": "Not found or no asset.read access",
                "error": "Bad Request",
                "statusCode": 404,
            }
        ),
    )

    api = await mock_immich_with_data()
    with pytest.raises(ImmichNotFoundError):
        await api.assets.async_open_video_stream(VIDEO_ID)
