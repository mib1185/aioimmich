"""aioimmich assets api."""

from aiohttp import StreamReader

from ..api import ImmichSubApi


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
