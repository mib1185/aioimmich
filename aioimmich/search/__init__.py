"""aioimmich search api."""

from ..api import ImmichSubApi
from ..assets.models import AssetType, ImmichAsset
from ..people.models import ImmichPerson


class ImmichSearch(ImmichSubApi):
    """Immich search api."""

    async def _async_search_assets(
        self,
        asset_type: AssetType | None = None,
        album_ids: list[str] | None = None,
        person_ids: list[str] | None = None,
        tag_ids: list[str] | None = None,
        page_size: int = 100,
        max_pages: int = 20,
        is_favorite: bool | None = None,
    ) -> list[ImmichAsset]:
        """Search for assets.

        Args:
            asset_type (AssetType | None): filter to `AssetType`
            album_ids (list[str] | None): filter to list of albumIds
            person_ids (list[str] | None): filter to list of personIds
            tag_ids (list[str] | None): filter to list of tagIds
            page_size (int): assets per page
            max_pages (int): maximum number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        data: dict[str, str | int | bool | list[str]] = {"size": page_size}
        if asset_type:
            data["type"] = asset_type.value
        if album_ids:
            data["albumIds"] = album_ids
        if person_ids:
            data["personIds"] = person_ids
        if tag_ids:
            data["tagIds"] = tag_ids
        if is_favorite is not None:
            data["isFavorite"] = is_favorite

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

        Args:
            page_size (int): assets per page
            max_pages (int): maximum number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        return await self._async_search_assets(page_size=page_size, max_pages=max_pages)

    async def async_get_all_favorites(
        self, page_size: int = 100, max_pages: int = 20
    ) -> list[ImmichAsset]:
        """Get all favorite assets.

        Args:
            page_size (int): assets per page
            max_pages (int): maximum number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        return await self._async_search_assets(
            page_size=page_size, max_pages=max_pages, is_favorite=True
        )

    async def async_get_all_by_tag_ids(
        self, tag_ids: list[str], page_size: int = 100, max_pages: int = 20
    ) -> list[ImmichAsset]:
        """Get all assets for given tag ids.

        Args:
            tag_ids (list[str]): filter to list of tagIds
            page_size (int): assets per page
            max_pages (int): maximum number of pages to return

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

        Args:
            person_ids (list[str]): filter to list of personIds
            page_size (int): assets per page
            max_pages (int): maximum number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        return await self._async_search_assets(
            person_ids=person_ids, page_size=page_size, max_pages=max_pages
        )

    async def async_get_all_by_album_ids(
        self, album_ids: list[str], page_size: int = 100, max_pages: int = 20
    ) -> list[ImmichAsset]:
        """Get all assets for given album ids.

        Args:
            album_ids (list[str]): filter to list of albumIds
            page_size (int): assets per page
            max_pages (int): maximum number of pages to return

        Returns:
            a list of `ImmichAsset`
        """
        if self.api.version.major < 3:
            results: list[ImmichAsset] = []
            for album_id in album_ids:
                result = await self.api.async_do_request(f"albums/{album_id}")
                assert isinstance(result, dict)
                results.extend(
                    [ImmichAsset.from_dict(asset) for asset in result["assets"]]
                )
            return results

        return await self._async_search_assets(
            album_ids=album_ids, page_size=page_size, max_pages=max_pages
        )

    async def async_search_persons(self, name: str) -> list[ImmichPerson]:
        """Search for persons by name.

        Args:
            name (str): Person name to search for

        Returns:
            a list of `ImmichPerson`
        """
        result = await self.api.async_do_request("search/person", params={"name": name})
        assert isinstance(result, list)

        return [ImmichPerson.from_dict(person) for person in result]

    async def async_smart_search(
        self,
        query: str,
        page_size: int = 100,
        max_pages: int = 20,
        album_ids: list[str] | None = None,
        person_ids: list[str] | None = None,
        tag_ids: list[str] | None = None,
        is_favorite: bool | None = None,
        is_not_in_album: bool | None = None,
    ) -> list[ImmichAsset]:
        """Perform a smart search for assets by using machine learning vectors to determine relevance.

        Args:
            query (str): Natural language search query
            page_size (int): assets per page
            max_pages (int): maximum number of pages to return
            album_ids (list[str] | None): filter by album IDs
            person_ids (list[str] | None): filter by person IDs
            tag_ids (list[str] | None): filter by tag IDs
            is_favorite (bool | None): filter by favorite status
            is_not_in_album (bool | None): filter assets not in any album

        Returns:
            a list of `ImmichAsset`
        """
        data: dict[str, str | int | bool | list[str]] = {
            "query": query,
            "size": page_size,
        }
        if album_ids is not None:
            data["albumIds"] = album_ids
        if person_ids is not None:
            data["personIds"] = person_ids
        if tag_ids is not None:
            data["tagIds"] = tag_ids
        if is_favorite is not None:
            data["isFavorite"] = is_favorite
        if is_not_in_album is not None:
            data["isNotInAlbum"] = is_not_in_album

        results: list[ImmichAsset] = []
        for page in range(max_pages):
            result = await self.api.async_do_request(
                "search/smart", data={**data, "page": page + 1}, method="POST"
            )
            assert isinstance(result, dict)
            assets = result["assets"]
            results.extend(ImmichAsset.from_dict(asset) for asset in assets["items"])
            if assets.get("nextPage") is None:
                break

        return results
