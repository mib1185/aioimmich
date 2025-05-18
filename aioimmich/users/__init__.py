"""aioimmich users api."""

import dateutil.parser

from ..api import ImmichApi
from .models import AvatarColor, ImmichUser, UserStatus


class ImmichUsers:
    """Immich users api."""

    def __init__(self, api: ImmichApi) -> None:
        """Immich users api init."""
        self.api = api

    async def async_get_my_user(self) -> ImmichUser:
        """Get my own user info.

        Returns:
            my own user info as `ImmichUser`
        """
        result = await self.api.async_do_request("users/me")
        assert isinstance(result, dict)
        return ImmichUser(
            result["id"],
            result["email"],
            result["name"],
            result["profileImagePath"],
            AvatarColor(result["avatarColor"]),
            dateutil.parser.isoparse(result["profileChangedAt"]),
            result["storageLabel"],
            result["shouldChangePassword"],
            result["isAdmin"],
            dateutil.parser.isoparse(result["createdAt"]),
            (
                dateutil.parser.isoparse(result["deletedAt"])
                if result["deletedAt"]
                else None
            ),
            (
                dateutil.parser.isoparse(result["updatedAt"])
                if result["updatedAt"]
                else None
            ),
            result["oauthId"],
            result["quotaSizeInBytes"],
            result["quotaUsageInBytes"],
            UserStatus(result["status"]),
        )
