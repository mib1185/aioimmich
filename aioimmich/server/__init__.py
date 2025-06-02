"""aioimmich server api."""

from ..api import ImmichSubApi
from .models import (
    ImmichServerAbout,
    ImmichServerStatistics,
    ImmichServerStorage,
    ImmichServerVersionCheck,
)


class ImmichServer(ImmichSubApi):
    """Immich server api."""

    async def async_get_about_info(self) -> ImmichServerAbout:
        """Get server about info.

        Returns:
            server about info as `ImmichServerAbout`
        """
        result = await self.api.async_do_request("server/about")
        assert isinstance(result, dict)
        return ImmichServerAbout.from_dict(result)

    async def async_get_storage_info(self) -> ImmichServerStorage:
        """Get server storage info.

        Returns:
            server storage info as `ImmichServerStorage`
        """
        result = await self.api.async_do_request("server/storage")
        assert isinstance(result, dict)
        return ImmichServerStorage.from_dict(result)

    async def async_get_server_statistics(self) -> ImmichServerStatistics:
        """Get server usage statistics.

        Returns:
            server usage statistics as `ImmichServerStatistics`
        """
        result = await self.api.async_do_request("server/statistics")
        assert isinstance(result, dict)
        return ImmichServerStatistics.from_dict(result)

    async def async_get_version_check(self) -> ImmichServerVersionCheck:
        """Get server version check result.

        Requires immich server v1.134.0

        Returns:
            server version check result as `ImmichServerVersionCheck`
        """
        result = await self.api.async_do_request("server/version-check")
        assert isinstance(result, dict)
        return ImmichServerVersionCheck.from_dict(result)
