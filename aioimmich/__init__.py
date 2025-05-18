"""Aioimmic library."""

from __future__ import annotations

from aiohttp.client import ClientSession

from .albums import ImmichAlbums
from .api import ImmichApi
from .assets import ImmichAssests
from .server import ImmichServer
from .users import ImmichUsers


class Immich:
    """Immich instance."""

    def __init__(
        self,
        aiohttp_session: ClientSession,
        api_key: str,
        host: str,
        port: int = 2283,
        use_ssl: bool = True,
    ) -> None:
        """Immich instace init."""
        self.api = ImmichApi(aiohttp_session, api_key, host, port, use_ssl)

        self.albums = ImmichAlbums(self.api)
        self.assets = ImmichAssests(self.api)
        self.server = ImmichServer(self.api)
        self.users = ImmichUsers(self.api)
