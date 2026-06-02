"""aioimmich memories models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin

from ..assets.models import ImmichAsset


@dataclass
class ImmichMemory(DataClassJSONMixin):
    """Representation of an immich memory."""

    created_at: datetime = field(metadata=field_options(alias="createdAt"))
    memory_id: str = field(metadata=field_options(alias="id"))
    updated_at: datetime = field(metadata=field_options(alias="updatedAt"))
    memory_at: datetime = field(metadata=field_options(alias="memoryAt"))
    show_at: datetime = field(metadata=field_options(alias="showAt"))
    hide_at: datetime = field(metadata=field_options(alias="hideAt"))
    owner_id: str = field(metadata=field_options(alias="ownerId"))
    is_saved: bool = field(metadata=field_options(alias="isSaved"))
    type: str
    data: dict
    assets: list[ImmichAsset]
