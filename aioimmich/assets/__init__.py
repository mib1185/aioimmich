"""aioimmich assets api."""

from ..api import ImmichApi


class ImmichAssests:
    """Immich assets api."""

    def __init__(self, api: ImmichApi) -> None:
        """Immich assets api init."""
        self.api = api

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
