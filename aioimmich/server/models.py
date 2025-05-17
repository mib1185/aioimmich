"""aioimmich server models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ImmichServerAbout:
    """Representation of the immich server about information."""

    version: str
    version_url: str
    licensed: bool
    build: str | None
    build_url: str | None
    build_image: str | None
    build_image_url: str | None
    repository: str | None
    repository_url: str | None
    source_ref: str | None
    source_commit: str | None
    source_url: str | None
    nodejs: str | None
    exiftool: str | None
    ffmpeg: str | None
    libvips: str | None
    imagemagick: str | None


@dataclass
class ImmichServerStorage:
    """Representation of the immich server storage information."""

    disk_size: str
    disk_use: str
    disk_available: str
    disk_size_raw: int
    disk_use_raw: int
    disk_available_raw: int
    disk_usage_percentage: float


@dataclass
class ImmichServerStatistics:
    """Representation of the immich server usage statistics."""

    photos: int
    videos: int
    usage: int
    usage_photos: int
    usage_videos: int
