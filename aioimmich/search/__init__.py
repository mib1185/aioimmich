"""aioimmich search api."""

from ..api import ImmichSubApi
from ..assets.models import AssetType, ImmichAsset


class ImmichSearch(ImmichSubApi):
    """Immich search api."""

    async def _async_search_assets(
        self,
        asset_type: AssetType | None = None,
        person_ids: list[str] | None = None,
        tag_ids: list[str] | None = None,
        page_size: int = 100,
        max_pages: int = 20,
    ) -> list[ImmichAsset]:
        """Search for assets.

        Arguments:
            asset_type (`AssetType | None`)  filter to `AssetType`
            person_ids (`list[str] | None`)  filter to list of personIds
            tag_ids (`list[str] | None`)     filter to list of tagIds
            page_size (`int`)                assets per page
            max_pages (`int`)                maximun number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        data: dict[str, str | int | bool | list[str]] = {"size": page_size}
        if asset_type:
            data["type"] = asset_type.value
        if person_ids:
            data["personIds"] = person_ids
        if tag_ids:
            data["tagIds"] = tag_ids

        results: list[ImmichAsset] = []
        for page in range(max_pages):
            result = await self.api.async_do_request(
                "search/metadata", data={**data, "page": page + 1}, method="POST"
            )
            assert isinstance(result, dict)
            assets = result["assets"]
            results.extend(ImmichAsset.from_dict(asset) for asset in assets["items"])
            if assets.get("nextPage") is None:
                break

        return results

    async def async_get_all(
        self, page_size: int = 100, max_pages: int = 20
    ) -> list[ImmichAsset]:
        """Get all assets.

        Arguments:
            page_size (`int`)  assets per page
            max_pages (`int`)  maximun number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        return await self._async_search_assets(page_size=page_size, max_pages=max_pages)

    async def async_get_all_by_tag_ids(
        self, tag_ids: list[str], page_size: int = 100, max_pages: int = 20
    ) -> list[ImmichAsset]:
        """Get all assets for given tag ids.

        Arguments:
            tag_ids (`list[str]`)  filter to list of tagIds
            page_size (`int`)      assets per page
            max_pages (`int`)      maximun number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        return await self._async_search_assets(
            tag_ids=tag_ids, page_size=page_size, max_pages=max_pages
        )

    async def async_get_all_by_person_ids(
        self, person_ids: list[str], page_size: int = 100, max_pages: int = 20
    ) -> list[ImmichAsset]:
        """Get all assets for given person ids.

        Arguments:
            person_ids (`list[str]`)  filter to list of tagIds
            page_size (`int`)         assets per page
            max_pages (`int`)         maximun number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        return await self._async_search_assets(
            person_ids=person_ids, page_size=page_size, max_pages=max_pages
        )
