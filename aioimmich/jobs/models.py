"""aioimmich jobs models."""

from __future__ import annotations

from dataclasses import dataclass, field

from mashumaro import field_options
from mashumaro.mixins.json import DataClassJSONMixin


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
class JobStatus(DataClassJSONMixin):
    """Representation of status for a specific job type."""

    job_counts: JobCounts = field(metadata=field_options(alias="jobCounts"))
    queue_status: QueueStatus = field(metadata=field_options(alias="queueStatus"))


@dataclass
class ImmichJobsStatus(DataClassJSONMixin):
    """Representation of all jobs status."""

    background_task: JobStatus = field(metadata=field_options(alias="backgroundTask"))
    backup_database: JobStatus = field(metadata=field_options(alias="backupDatabase"))
    duplicate_detection: JobStatus = field(
        metadata=field_options(alias="duplicateDetection")
    )
    face_detection: JobStatus = field(metadata=field_options(alias="faceDetection"))
    facial_recognition: JobStatus = field(
        metadata=field_options(alias="facialRecognition")
    )
    library: JobStatus
    metadata_extraction: JobStatus = field(
        metadata=field_options(alias="metadataExtraction")
    )
    migration: JobStatus
    notifications: JobStatus
    search: JobStatus
    sidecar: JobStatus
    smart_search: JobStatus = field(metadata=field_options(alias="smartSearch"))
    storage_template_migration: JobStatus = field(
        metadata=field_options(alias="storageTemplateMigration")
    )
    thumbnail_generation: JobStatus = field(
        metadata=field_options(alias="thumbnailGeneration")
    )
    video_conversion: JobStatus = field(metadata=field_options(alias="videoConversion"))


@dataclass
class JobCommand(DataClassJSONMixin):
    """Representation of a job command request."""

    command: str
    force: bool = False
