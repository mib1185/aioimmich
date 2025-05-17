"""aioimmich models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ImmichAsset:
    """Representation of an immich asset."""

    asset_id: str
    file_name: str
    mime_type: str


@dataclass
class ImmichAlbum:
    """Representation of an immich album."""

    album_id: str
    name: str
    description: str
    thumbnail_asset_id: str
    asset_count: int
    assets: list[ImmichAsset]
