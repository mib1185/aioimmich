"""Aioimmic library."""

from __future__ import annotations

from aiohttp.client import ClientSession

from .const import CONNECT_ERRORS, LOGGER
from .exceptions import ImmichError, ImmichUnauthorizedError
from .models import ImmichAlbum, ImmichAsset


class Immich:
    """immich api."""

    def __init__(
        self,
        aiohttp_session: ClientSession,
        api_key: str,
        host: str,
        port: int = 2283,
        use_ssl: bool = True,
    ) -> None:
        """Immich api init."""
        self.session: ClientSession = aiohttp_session
        self.api_key = api_key
        self.base_url = f"{'https' if use_ssl else 'http'}://{host}:{port}/api"

    async def _async_do_request(
        self,
        end_point: str,
        params: dict | None = None,
        method: str = "get",
        application: str = "json",
    ) -> dict | bytes | None:
        """Perform the request and handle errors."""
        headers = {"Accept": f"application/{application}", "x-api-key": self.api_key}
        url = f"{self.base_url}/{end_point}"

        LOGGER.debug("REQUEST url: %s params: %s headers: %s", url, params, headers)

        try:
            async with self.session.request(
                method, url, params=params, headers=headers
            ) as resp:
                if resp.status == 200:
                    if application == "json":
                        result = await resp.json()
                        LOGGER.debug("RESPONSE %s", result)
                        return result
                    LOGGER.debug("RESPONSE bytes")
                    return await resp.read()

                err_result = await resp.json()
                LOGGER.debug("RESPONSE %s", err_result)
                if resp.status == 400:
                    raise ImmichError(err_result)
                if resp.status == 401:
                    raise ImmichUnauthorizedError(err_result)
                return resp.raise_for_status()

        except CONNECT_ERRORS as err:
            LOGGER.debug("connection error", exc_info=True)
            LOGGER.error(
                "Error while getting data: %s: %s",
                err.__class__.__name__,
                err.__class__.__cause__,
            )
            raise err

    async def get_all_albums(self) -> list[ImmichAlbum]:
        """Get all albums.

        Returns:
            list of all albums as `list[ImmichAlbum]`
        """
        result = await self._async_do_request("albums")
        assert isinstance(result, dict)
        return [
            ImmichAlbum(
                album["id"],
                album["albumName"],
                album["description"],
                album["albumThumbnailAssetId"],
                album["assetCount"],
                [],
            )
            for album in result
        ]

    async def get_album_info(
        self, album_id: str, without_assests: bool = False
    ) -> ImmichAlbum:
        """Get album information and its assets.

        Arguments:
            album_id (str)          id of the album to be fetched
            without_assests (bool)  whether to fetch the asstes for the album

        Returns:
            album with assests (when `without_assests=False`) as `ImmichAlbum`
        """
        result = await self._async_do_request(
            f"albums/{album_id}",
            {"withoutAssets": "true" if without_assests else "false"},
        )
        print(result)
        assert isinstance(result, dict)
        return ImmichAlbum(
            result["id"],
            result["albumName"],
            result["description"],
            result["albumThumbnailAssetId"],
            result["assetCount"],
            [
                ImmichAsset(
                    asset["id"], asset["originalFileName"], asset["originalMimeType"]
                )
                for asset in result["assets"]
            ],
        )

    async def view_asset(self, asset_id: str, size: str = "thumbnail") -> bytes:
        """Get an assets thumbnail.

        Arguments:
            asset_id (str)  id of the asset to be fetched
            size (str)      one of [`fullsize`, `preview`, `thumbnail`] size (default: `thumbnail`)

        Returns:
            asset content as `bytes`
        """
        result = await self._async_do_request(
            f"assets/{asset_id}/thumbnail", {"size": size}, application="octet-stream"
        )
        assert isinstance(result, bytes)
        return result
