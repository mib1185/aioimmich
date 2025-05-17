"""aioimmich models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ImmichAsset:
    """Representation of an immich asset."""

    asset_id: str
    file_name: str
    mime_type: str
