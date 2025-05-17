"""aioimmich albums models."""

from __future__ import annotations

from dataclasses import dataclass

from ..assets.models import ImmichAsset


@dataclass
class ImmichAlbum:
    """Representation of an immich album."""

    album_id: str
    name: str
    description: str
    thumbnail_asset_id: str
    asset_count: int
    assets: list[ImmichAsset]
