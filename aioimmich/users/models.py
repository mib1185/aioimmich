"""aioimmich server models."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ..helpers import StrEnum


class AvatarColor(StrEnum):
    """Avatar colors."""

    AMBER = "amber"
    BLUE = "blue"
    GRAY = "gray"
    GREEN = "green"
    ORANGE = "orange"
    PINK = "pink"
    PRIMARY = "primary"
    PURPEL = "purple"
    RED = "red"
    YELLOW = "yellow"


class UserStatus(StrEnum):
    """User status."""

    ACTIVE = "active"
    DELETED = "deleted"
    REMOVING = "removing"


@dataclass
class ImmichUser:
    """Representation of immich user."""

    user_id: str
    email: str
    name: str
    profile_image_path: str
    avatar_color: AvatarColor
    profile_changed_at: datetime
    storage_label: str
    should_change_password: bool
    is_admin: bool
    created_at: datetime
    deleted_at: datetime | None
    updated_at: datetime | None
    oauth_id: str
    quota_size_in_bytes: int | None
    quota_usage_in_bytes: int | None
    status: UserStatus
