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
