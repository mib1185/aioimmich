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

    async def async_get_tag_by_id(self, tag_id: str) -> ImmichTag:
        """Get a specific tag by its uuid.

        Args:
            tag_id (str):  Tag ID

        Returns:
            `ImmichTag`
        """
        result = await self.api.async_do_request(f"tags/{tag_id}")
        assert isinstance(result, dict)
        return ImmichTag.from_dict(result)

    async def async_filter_tags_by_name(self, name: str) -> list[ImmichTag]:
        """Filter tags by name.

        Args:
            name (str): Tag name to filter by (case-insensitive)

        Returns:
            a list of `ImmichTag`
        """
        return [
            tag
            for tag in await self.async_get_all_tags()
            if name.lower() in tag.name.lower()
        ]
