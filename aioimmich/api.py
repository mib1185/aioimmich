"""aioimmich api."""

from __future__ import annotations

from dataclasses import dataclass

from aiohttp import StreamReader
from aiohttp.client import ClientSession

from .const import CONNECT_ERRORS, LOGGER
from .exceptions import ImmichError, ImmichForbiddenError, ImmichUnauthorizedError


@dataclass
class CacheEntry:
    """Representation of response cache entry."""

    etag: str | None
    result: dict | list | None


class ImmichApi:
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
        self.cache: dict[str, CacheEntry] = {}

    async def async_do_request(
        self,
        end_point: str,
        params: dict | None = None,
        method: str = "get",
        application: str = "json",
        raw_response_content: bool = False,
    ) -> list | dict | bytes | StreamReader | None:
        """Perform the request and handle errors."""
        headers = {"Accept": f"application/{application}", "x-api-key": self.api_key}
        url = f"{self.base_url}/{end_point}"

        cache_key = f"{method}_{end_point}_{params}"
        if cache_key not in self.cache:
            self.cache[cache_key] = CacheEntry(None, None)

        cache_entry = self.cache[cache_key]
        if (etag := cache_entry.etag) is not None:
            headers.update({"If-None-Match": etag})

        LOGGER.debug(
            "REQUEST url: %s params: %s headers: %s",
            url,
            params,
            {**headers, "x-api-key": "**********"},
        )

        try:
            resp = await self.session.request(
                method, url, params=params, headers=headers
            )
            LOGGER.debug("RESPONSE headers: %s", dict(resp.headers))
            if resp.status == 304:  # 304 = not modified
                LOGGER.debug("RESPONSE from cache")
                return cache_entry.result

            if resp.status == 200:
                if raw_response_content:
                    LOGGER.debug("RESPONSE as stream")
                    return resp.content
                if application == "json":
                    result = await resp.json()
                    if cache_entry.etag is None:
                        cache_entry.etag = resp.headers.get("Etag")
                    cache_entry.result = result
                    LOGGER.debug("RESPONSE: %s", result)
                    return result
                LOGGER.debug("RESPONSE as bytes")
                return await resp.read()

            err_result = await resp.json()
            LOGGER.debug("RESPONSE %s", err_result)
            if resp.status == 400:
                raise ImmichError(err_result)
            if resp.status == 401:
                raise ImmichUnauthorizedError(err_result)
            if resp.status == 403:
                raise ImmichForbiddenError(err_result)
            return resp.raise_for_status()

        except CONNECT_ERRORS as err:
            LOGGER.debug("connection error", exc_info=True)
            LOGGER.error(
                "Error while getting data: %s: %s",
                err.__class__.__name__,
                err.__class__.__cause__,
            )
            raise err
