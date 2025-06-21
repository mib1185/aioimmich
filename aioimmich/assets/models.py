"""aioimmich models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from enum import StrEnum

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


class AssetType(StrEnum):
    """Asset type."""

    AUDIO = "AUDIO"
    IMAGE = "IMAGE"
    OTHER = "OTHER"
    VIDEO = "VIDEO"


class UploadStatus(StrEnum):
    """Asset upload status."""

    CREATED = "created"
    DUPLICATED = "duplicate"
    REPLACED = "replaced"


@dataclass
class ExifInfo(DataClassJSONMixin):
    """Exif info."""

    city: str | None = field(default=None)
    country: str | None = field(default=None)
    date_time_original: datetime | None = field(
        metadata=field_options(alias="dateTimeOriginal"), default=None
    )
    description: str | None = field(default=None)
    exif_image_height: int | None = field(
        metadata=field_options(alias="exifImageHeight"), default=None
    )
    exif_image_width: int | None = field(
        metadata=field_options(alias="exifImageWidth"), default=None
    )
    exposure_time: str | None = field(
        metadata=field_options(alias="exposureTime"), default=None
    )
    file_size_in_byte: int | None = field(
        metadata=field_options(alias="fileSizeInByte"), default=None
    )
    f_number: float | None = field(
        metadata=field_options(alias="fNumber"), default=None
    )
    focal_length: float | None = field(
        metadata=field_options(alias="focalLength"), default=None
    )
    iso: int | None = field(default=None)
    latitude: float | None = field(default=None)
    lens_model: str | None = field(
        metadata=field_options(alias="lensModel"), default=None
    )
    longitude: float | None = field(default=None)
    make: str | None = field(default=None)
    model: str | None = field(default=None)
    modify_date: str | None = field(
        metadata=field_options(alias="modifyDate"), default=None
    )
    orientation: str | None = field(default=None)
    projection_type: str | None = field(
        metadata=field_options(alias="projectionType"), default=None
    )
    rating: str | None = field(default=None)
    state: str | None = field(default=None)
    time_zone: str | None = field(
        metadata=field_options(alias="timeZone"), default=None
    )


@dataclass
class ImmichAsset(DataClassJSONMixin):
    """Representation of an immich asset."""

    # non-default parameters
    asset_id: str = field(metadata=field_options(alias="id"))
    asset_type: AssetType = field(metadata=field_options(alias="type"))
    checksum: str
    device_asset_id: str = field(metadata=field_options(alias="deviceAssetId"))
    device_id: str = field(metadata=field_options(alias="deviceId"))
    duration: str
    file_created_at: datetime = field(metadata=field_options(alias="fileCreatedAt"))
    file_modified_at: datetime = field(metadata=field_options(alias="fileModifiedAt"))
    has_metadata: bool = field(metadata=field_options(alias="hasMetadata"))
    is_archived: bool = field(metadata=field_options(alias="isArchived"))
    is_favorite: bool = field(metadata=field_options(alias="isFavorite"))
    is_offline: bool = field(metadata=field_options(alias="isOffline"))
    is_trashed: bool = field(metadata=field_options(alias="isTrashed"))
    local_datetime: datetime = field(metadata=field_options(alias="localDateTime"))
    original_file_name: str = field(metadata=field_options(alias="originalFileName"))
    original_path: str = field(metadata=field_options(alias="originalPath"))
    owner_id: str = field(metadata=field_options(alias="ownerId"))
    people: list  # TODO: proper dataclass necessary
    resized: bool
    thumbhash: str
    updated_at: datetime = field(metadata=field_options(alias="updatedAt"))

    # default parameters
    duplicate_id: str | None = field(
        metadata=field_options(alias="duplicateId"), default=None
    )
    exif_info: ExifInfo | None = field(
        metadata=field_options(alias="exifInfo"), default=None
    )
    library_id: str | None = field(
        metadata=field_options(alias="libraryId"), default=None
    )  # This property was deprecated in v1.106.0
    live_photo_video_id: str | None = field(
        metadata=field_options(alias="livePhotoVideoId"), default=None
    )
    original_mime_type: str | None = field(
        metadata=field_options(alias="originalMimeType"), default=None
    )
    visibility: str | None = field(default=None)


@dataclass
class ImmichAssetUploadResponse(DataClassJSONMixin):
    """Representation of an immich asset upload response."""

    asset_id: str = field(metadata=field_options(alias="id"))
    status: UploadStatus
