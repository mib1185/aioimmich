"""aioimmich assets api."""

import os
from collections.abc import AsyncIterator
from datetime import datetime
from hashlib import md5

import aiofiles
from aiohttp import MultipartWriter, StreamReader, hdrs

from ..api import ImmichSubApi
from .models import ImmichAssetUploadResponse


async def _file_sender(file: str) -> AsyncIterator[bytes]:
    async with aiofiles.open(file, "rb") as f:
        chunk = await f.read(64 * 1024)
        while chunk:
            yield chunk
            chunk = await f.read(64 * 1024)


class ImmichAssests(ImmichSubApi):
    """Immich assets api."""

    async def async_view_asset(self, asset_id: str, size: str = "thumbnail") -> bytes:
        """Get an assets thumbnail.

        Arguments:
            asset_id (str)  id of the asset to be fetched
            size (str)      one of [`fullsize`, `preview`, `thumbnail`] size (default: `thumbnail`)

        Returns:
            asset content as `bytes`
        """
        result = await self.api.async_do_request(
            f"assets/{asset_id}/thumbnail", {"size": size}, application="octet-stream"
        )
        assert isinstance(result, bytes)
        return result

    async def async_play_video_stream(self, asset_id: str) -> StreamReader:
        """Get a video stream.

        Arguments:
            asset_id (str)  id of the video to be streamed

        Returns:
            the video stream as `StreamReader`
        """
        result = await self.api.async_do_request(
            f"assets/{asset_id}/video/playback",
            application="octet-stream",
            raw_response_content=True,
        )
        assert isinstance(result, StreamReader)
        return result

    async def async_upload_asset(self, file: str) -> ImmichAssetUploadResponse:
        """Upload a file.

        Arguments:
            file (str)  path to the file to be uploaded

        Returns:
            result of upload as `ImmichAssetUploadResponse`
        """
        stats = os.stat(file)
        filename = os.path.basename(file)

        boundary = md5(str(file).encode("utf-8"), usedforsecurity=False).hexdigest()
        data = {
            "deviceAssetId": f"{self.api.device_id}-{file}-{stats.st_mtime}",
            "deviceId": self.api.device_id,
            "fileCreatedAt": datetime.fromtimestamp(stats.st_mtime).isoformat(),
            "fileModifiedAt": datetime.fromtimestamp(stats.st_mtime).isoformat(),
            "isFavorite": "false",
        }
        with MultipartWriter("form-data", boundary=boundary) as mp:
            for k, v in data.items():
                part = mp.append(v)
                part.headers.pop(hdrs.CONTENT_TYPE)
                part.set_content_disposition("form-data", name=k)

            part = mp.append(_file_sender(file))
            part.headers.pop(hdrs.CONTENT_TYPE)
            part.set_content_disposition(
                "form-data", name="assetData", filename=filename
            )
            part.headers.add(hdrs.CONTENT_TYPE, "application/octet-stream")

            result = await self.api.async_do_request(
                "assets", raw_data=mp, method="POST"
            )
        assert isinstance(result, dict)
        return ImmichAssetUploadResponse.from_dict(result)
