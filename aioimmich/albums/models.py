"""aioimmich albums models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin

from ..assets.models import ImmichAsset
from ..users.models import ImmichUser


class AssetToAlbumError(StrEnum):
    """Asset upload status."""

    DUPLICATED = "duplicate"
    NO_PERMISSION = "no_permission"
    NOT_FOUND = "not_found"
    UNKNOWN = "unknown"


@dataclass
class ImmichAlbum(DataClassJSONMixin):
    """Representation of an immich album."""

    # non-default parameters
    album_id: str = field(metadata=field_options(alias="id"))
    album_name: str = field(metadata=field_options(alias="albumName"))
    album_thumbnail_asset_id: str | None = field(
        metadata=field_options(alias="albumThumbnailAssetId")
    )
    album_users: list = field(metadata=field_options(alias="albumUsers"))
    asset_count: int = field(metadata=field_options(alias="assetCount"))
    assets: list[ImmichAsset]
    created_at: datetime = field(metadata=field_options(alias="createdAt"))
    has_shared_link: bool = field(metadata=field_options(alias="hasSharedLink"))
    is_activity_enabled: bool = field(metadata=field_options(alias="isActivityEnabled"))
    owner_id: str = field(metadata=field_options(alias="ownerId"))
    owner: ImmichUser
    shared: bool
    updated_at: datetime = field(metadata=field_options(alias="updatedAt"))

    # default parameters
    end_date: datetime | None = field(
        metadata=field_options(alias="endDate"), default=None
    )
    last_modified_asset_timestamp: datetime | None = field(
        metadata=field_options(alias="lastModifiedAssetTimestamp"), default=None
    )
    order: str | None = field(default=None)
    start_date: datetime | None = field(
        metadata=field_options(alias="startDate"), default=None
    )


@dataclass
class ImmichAddAssetsToAlbumResponse(DataClassJSONMixin):
    """Representation of an immich add assets to album response."""

    asset_id: str = field(metadata=field_options(alias="id"))
    success: bool
    error: AssetToAlbumError | None = field(default=None)
