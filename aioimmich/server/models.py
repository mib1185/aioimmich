"""aioimmich server models."""

from __future__ import annotations

from dataclasses import dataclass, field

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class ImmichServerAbout(DataClassJSONMixin):
    """Representation of the immich server about information."""

    build_image_url: str | None = field(metadata=field_options(alias="buildImageUrl"))
    build_image: str | None = field(metadata=field_options(alias="buildImage"))
    build_url: str | None = field(metadata=field_options(alias="buildUrl"))
    build: str | None
    exiftool: str | None
    ffmpeg: str | None
    imagemagick: str | None
    libvips: str | None
    licensed: bool
    nodejs: str | None
    repository_url: str | None = field(metadata=field_options(alias="repositoryUrl"))
    repository: str | None
    source_commit: str | None = field(metadata=field_options(alias="sourceCommit"))
    source_ref: str | None = field(metadata=field_options(alias="sourceRef"))
    source_url: str | None = field(metadata=field_options(alias="sourceUrl"))
    version_url: str = field(metadata=field_options(alias="versionUrl"))
    version: str


@dataclass
class ImmichServerStorage(DataClassJSONMixin):
    """Representation of the immich server storage information."""

    disk_available_raw: int = field(metadata=field_options(alias="diskAvailableRaw"))
    disk_available: str = field(metadata=field_options(alias="diskAvailable"))
    disk_size_raw: int = field(metadata=field_options(alias="diskSizeRaw"))
    disk_size: str = field(metadata=field_options(alias="diskSize"))
    disk_usage_percentage: float = field(
        metadata=field_options(alias="diskUsagePercentage")
    )
    disk_use_raw: int = field(metadata=field_options(alias="diskUseRaw"))
    disk_use: str = field(metadata=field_options(alias="diskUse"))


@dataclass
class ByUserUsage(DataClassJSONMixin):
    """Usage by user."""

    photos: int
    quota_size_in_bytes: int | None = field(
        metadata=field_options(alias="quotaSizeInBytes")
    )
    usage: int
    usage_photos: int = field(metadata=field_options(alias="usagePhotos"))
    usage_videos: int = field(metadata=field_options(alias="usageVideos"))
    user_id: str = field(metadata=field_options(alias="userId"))
    user_name: str = field(metadata=field_options(alias="userName"))
    videos: int


@dataclass
class ImmichServerStatistics(DataClassJSONMixin):
    """Representation of the immich server usage statistics."""

    photos: int
    usage_by_user: list[ByUserUsage] = field(
        metadata=field_options(alias="usageByUser")
    )
    usage_photos: int = field(metadata=field_options(alias="usagePhotos"))
    usage_videos: int = field(metadata=field_options(alias="usageVideos"))
    usage: int
    videos: int
