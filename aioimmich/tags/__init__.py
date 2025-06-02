"""aioimmich tags api."""

from ..api import ImmichApi
from .models import ImmichTag


class ImmichTags:
    """Immich tags api."""

    def __init__(self, api: ImmichApi) -> None:
        """Immich tags api init."""
        self.api = api

    async def async_get_all_tags(self) -> list[ImmichTag]:
        """Get all tags.

        Returns:
            all tags as list of `ImmichTag`
        """
        result = await self.api.async_do_request("tags")
        assert isinstance(result, list)
        return [ImmichTag.from_dict(tag) for tag in result]
