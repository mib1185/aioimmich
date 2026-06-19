"""aioimmich albums api."""

from ..api import ImmichSubApi
from .models import ImmichAddAssetsToAlbumResponse, ImmichAlbum


class ImmichAlbums(ImmichSubApi):
    """Immich albums api."""

    async def async_get_all_albums(self) -> list[ImmichAlbum]:
        """Get all albums.

        Returns:
            list of all albums as `list[ImmichAlbum]`
        """
        if self.api.version.major < 3:
            result = await self.api.async_do_request("albums", {"shared": "false"})
            assert isinstance(result, list)
            result_shared = await self.api.async_do_request(
                "albums", {"shared": "true"}
            )
            assert isinstance(result_shared, list)
            return [ImmichAlbum.from_dict(album) for album in result + result_shared]

        result = await self.api.async_do_request("albums")
        assert isinstance(result, list)
        return [ImmichAlbum.from_dict(album) for album in result]

    async def async_get_album_info(self, album_id: str) -> ImmichAlbum:
        """Get album information.

        Args:
            album_id (str): id of the album to be fetched

        Returns:
            album as `ImmichAlbum`
        """
        result = await self.api.async_do_request(f"albums/{album_id}")
        assert isinstance(result, dict)
        return ImmichAlbum.from_dict(result)

    async def async_add_assets_to_album(
        self, album_id: str, asset_ids: list[str]
    ) -> list[ImmichAddAssetsToAlbumResponse]:
        """Add given assets to the given album.

        Args:
            album_id (str): id of the album to add the assets
            asset_ids (list): list of asset ids to add to the album

        Returns:
            result of adding as list of `ImmichAddAssetsToAlbumResponse`
        """
        result = await self.api.async_do_request(
            f"albums/{album_id}/assets", data={"ids": asset_ids}, method="PUT"
        )
        assert isinstance(result, list)
        return [ImmichAddAssetsToAlbumResponse.from_dict(item) for item in result]
