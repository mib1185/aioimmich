"""aioimmich jobs models."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


class JobId(StrEnum):
    """Job IDs."""

    BACKGROUND_TASK = "backgroundTask"
    BACKUP_DATABASE = "backupDatabase"
    DUPLICATE_DETECTION = "duplicateDetection"
    FACE_DETECTION = "faceDetection"
    FACIAL_RECOGNITION = "facialRecognition"
    LIBRARY = "library"
    METADATA_EXTRACTION = "metadataExtraction"
    MIGRATION = "migration"
    NOTIFICATIONS = "notifications"
    SEARCH = "search"
    SIDECAR = "sidecar"
    SMART_SEARCH = "smartSearch"
    STORAGE_TEMPLATE_MIGRATION = "storageTemplateMigration"
    THUMBNAIL_GENERATION = "thumbnailGeneration"
    VIDEO_CONVERSION = "videoConversion"


class JobCommand(StrEnum):
    """Job commands."""

    CLEAR_FAILED = "clear-failed"
    EMPTY = "empty"
    PAUSE = "pause"
    RESUME = "resume"
    START = "start"


@dataclass
class JobCounts(DataClassJSONMixin):
    """Representation of job counts for a specific job type."""

    active: int
    completed: int
    delayed: int
    failed: int
    paused: int
    waiting: int


@dataclass
class QueueStatus(DataClassJSONMixin):
    """Representation of queue status for a specific job type."""

    is_active: bool = field(metadata=field_options(alias="isActive"))
    is_paused: bool = field(metadata=field_options(alias="isPaused"))


@dataclass
class ImmichJobStatus(DataClassJSONMixin):
    """Representation of status for a specific job type."""

    job_counts: JobCounts = field(metadata=field_options(alias="jobCounts"))
    queue_status: QueueStatus = field(metadata=field_options(alias="queueStatus"))


@dataclass
class ImmichAllJobStatus(DataClassJSONMixin):
    """Representation of all jobs status."""

    background_task: ImmichJobStatus = field(
        metadata=field_options(alias="backgroundTask")
    )
    backup_database: ImmichJobStatus = field(
        metadata=field_options(alias="backupDatabase")
    )
    duplicate_detection: ImmichJobStatus = field(
        metadata=field_options(alias="duplicateDetection")
    )
    face_detection: ImmichJobStatus = field(
        metadata=field_options(alias="faceDetection")
    )
    facial_recognition: ImmichJobStatus = field(
        metadata=field_options(alias="facialRecognition")
    )
    library: ImmichJobStatus
    metadata_extraction: ImmichJobStatus = field(
        metadata=field_options(alias="metadataExtraction")
    )
    migration: ImmichJobStatus
    notifications: ImmichJobStatus
    search: ImmichJobStatus
    sidecar: ImmichJobStatus
    smart_search: ImmichJobStatus = field(metadata=field_options(alias="smartSearch"))
    storage_template_migration: ImmichJobStatus = field(
        metadata=field_options(alias="storageTemplateMigration")
    )
    thumbnail_generation: ImmichJobStatus = field(
        metadata=field_options(alias="thumbnailGeneration")
    )
    video_conversion: ImmichJobStatus = field(
        metadata=field_options(alias="videoConversion")
    )
