"""aioimmich server api."""

from ..api import ImmichApi
from .models import ImmichServerAbout, ImmichServerStatistics, ImmichServerStorage


class ImmichServer:
    """Immich server api."""

    def __init__(self, api: ImmichApi) -> None:
        """Immich server api init."""
        self.api = api

    async def async_get_about_info(self) -> ImmichServerAbout:
        """Get server about info.

        Returns:
            server about info as `ImmichServerAbout`
        """
        result = await self.api.async_do_request("server/about")
        assert isinstance(result, dict)
        return ImmichServerAbout(
            result["version"],
            result["versionUrl"],
            result["licensed"],
            result.get("build"),
            result.get("buildUrl"),
            result.get("buildImage"),
            result.get("buildImageUrl"),
            result.get("repository"),
            result.get("repositoryUrl"),
            result.get("sourceRef"),
            result.get("sourceCommit"),
            result.get("sourceUrl"),
            result.get("nodejs"),
            result.get("exiftool"),
            result.get("ffmpeg"),
            result.get("libvips"),
            result.get("imagemagick"),
        )

    async def async_get_storage_info(self) -> ImmichServerStorage:
        """Get server storage info.

        Returns:
            server storage info as `ImmichServerStorage`
        """
        result = await self.api.async_do_request("server/storage")
        assert isinstance(result, dict)
        return ImmichServerStorage(
            result["diskSize"],
            result["diskUse"],
            result["diskAvailable"],
            result["diskSizeRaw"],
            result["diskUseRaw"],
            result["diskAvailableRaw"],
            result["diskUsagePercentage"],
        )

    async def async_get_server_statistics(self) -> ImmichServerStatistics:
        """Get server usage statistics.

        Returns:
            server usage statistics as `ImmichServerStatistics`
        """
        result = await self.api.async_do_request("server/statistics")
        assert isinstance(result, dict)
        return ImmichServerStatistics(
            result["photos"],
            result["videos"],
            result["usage"],
            result["usagePhotos"],
            result["usageVideos"],
        )
