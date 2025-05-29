"""aioimmich server models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


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
class ImmichUser(DataClassJSONMixin):
    """Representation of an immich user."""

    avatar_color: AvatarColor = field(metadata=field_options(alias="avatarColor"))
    email: str
    name: str
    profile_changed_at: datetime = field(
        metadata=field_options(alias="profileChangedAt")
    )
    profile_image_path: str = field(metadata=field_options(alias="profileImagePath"))
    user_id: str = field(metadata=field_options(alias="id"))


@dataclass
class ImmichUserObject(ImmichUser):
    """Representation of an immich user configuration object."""

    # non-default parameters
    created_at: datetime = field(metadata=field_options(alias="createdAt"))
    is_admin: bool = field(metadata=field_options(alias="isAdmin"))
    oauth_id: str = field(metadata=field_options(alias="oauthId"))
    should_change_password: bool = field(
        metadata=field_options(alias="shouldChangePassword")
    )
    status: UserStatus
    storage_label: str = field(metadata=field_options(alias="storageLabel"))

    # default parameters
    deleted_at: datetime | None = field(metadata=field_options(alias="deletedAt"))
    quota_size_in_bytes: int | None = field(
        metadata=field_options(alias="quotaSizeInBytes")
    )
    quota_usage_in_bytes: int | None = field(
        metadata=field_options(alias="quotaUsageInBytes")
    )
    updated_at: datetime | None = field(metadata=field_options(alias="updatedAt"))
