"""aioimmich users api."""

from ..api import ImmichApi
from .models import ImmichUserObject


class ImmichUsers:
    """Immich users api."""

    def __init__(self, api: ImmichApi) -> None:
        """Immich users api init."""
        self.api = api

    async def async_get_my_user(self) -> ImmichUserObject:
        """Get my own user info.

        Returns:
            my own user info as `ImmichUserObject`
        """
        result = await self.api.async_do_request("users/me")
        assert isinstance(result, dict)
        return ImmichUserObject.from_dict(result)
