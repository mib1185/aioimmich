"""aioimmich api."""

from __future__ import annotations

from aiohttp.client import ClientSession

from .const import CONNECT_ERRORS, LOGGER
from .exceptions import ImmichError, ImmichForbiddenError, ImmichUnauthorizedError


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

    async def async_do_request(
        self,
        end_point: str,
        params: dict | None = None,
        method: str = "get",
        application: str = "json",
    ) -> list | dict | bytes | None:
        """Perform the request and handle errors."""
        headers = {"Accept": f"application/{application}", "x-api-key": self.api_key}
        url = f"{self.base_url}/{end_point}"

        LOGGER.debug(
            "REQUEST url: %s params: %s headers: %s",
            url,
            params,
            {**headers, "x-api-key": "**********"},
        )

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
