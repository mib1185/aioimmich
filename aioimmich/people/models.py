"""aioimmich people models."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


@dataclass
class ImmichPerson(DataClassJSONMixin):
    """Representation of an immich person."""

    # non-default parameters
    person_id: str = field(metadata=field_options(alias="id"))
    is_hidden: bool | None = field(metadata=field_options(alias="isHidden"))
    name: str
    thumbnail_path: str = field(metadata=field_options(alias="thumbnailPath"))

    # default parameters
    birth_date: datetime | None = field(
        metadata=field_options(alias="birthDate"), default=None
    )
    color: str | None = field(default=None)
    is_favorite: bool | None = field(
        metadata=field_options(alias="isFavorite"), default=None
    )
    updated_at: datetime | None = field(
        metadata=field_options(alias="updatedAt"), default=None
    )
