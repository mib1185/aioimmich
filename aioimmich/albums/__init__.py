"""aioimmich albums api."""

from ..api import ImmichApi
from ..assets.models import ImmichAsset
from .models import ImmichAlbum


class ImmichAlbums:
    """Immich albums api."""

    def __init__(self, api: ImmichApi) -> None:
        """Immich albums api init."""
        self.api = api

    async def async_get_all_albums(self) -> list[ImmichAlbum]:
        """Get all albums.

        Returns:
            list of all albums as `list[ImmichAlbum]`
        """
        result = await self.api.async_do_request("albums")
        assert isinstance(result, list)
        return [ImmichAlbum.from_dict(album) for album in result]

    async def async_get_album_info(
        self, album_id: str, without_assests: bool = False
    ) -> ImmichAlbum:
        """Get album information and its assets.

        Arguments:
            album_id (str)          id of the album to be fetched
            without_assests (bool)  whether to fetch the asstes for the album

        Returns:
            album with assests (when `without_assests=False`) as `ImmichAlbum`
        """
        result = await self.api.async_do_request(
            f"albums/{album_id}",
            {"withoutAssets": "true" if without_assests else "false"},
        )
        assert isinstance(result, dict)
        print(result)
        return ImmichAlbum.from_dict(result)
