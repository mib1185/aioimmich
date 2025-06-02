"""aioimmich tags models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class ImmichTag(DataClassJSONMixin):
    """Representation of an immich tag."""

    # non-default parameters
    created_at: datetime = field(metadata=field_options(alias="createdAt"))
    name: str
    tag_id: str = field(metadata=field_options(alias="id"))
    updated_at: datetime = field(metadata=field_options(alias="updatedAt"))
    value: str

    # default parameters
    color: str | None = field(metadata=field_options(alias="avatarColor"), default=None)
    parent_id: str | None = field(
        metadata=field_options(alias="parentId"), default=None
    )
