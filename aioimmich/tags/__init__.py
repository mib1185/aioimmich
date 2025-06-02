"""aioimmich tags api."""

from ..api import ImmichSubApi
from .models import ImmichTag


class ImmichTags(ImmichSubApi):
    """Immich tags api."""

    async def async_get_all_tags(self) -> list[ImmichTag]:
        """Get all tags.

        Returns:
            all tags as list of `ImmichTag`
        """
        result = await self.api.async_do_request("tags")
        assert isinstance(result, list)
        return [ImmichTag.from_dict(tag) for tag in result]
