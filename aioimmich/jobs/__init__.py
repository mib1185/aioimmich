"""aioimmich jobs api."""

from ..api import ImmichSubApi
from .models import (
    ImmichJobsStatus,
    JobCommand,
    JobStatus,
)


class ImmichJobs(ImmichSubApi):
    """Immich jobs api."""

    async def async_get_all_jobs_status(self) -> ImmichJobsStatus:
        """Get all jobs status.

        Returns:
            all jobs status as `ImmichJobsStatus`
        """
        result = await self.api.async_do_request("jobs/status")
        assert isinstance(result, dict)
        return ImmichJobsStatus.from_dict(result)

    async def async_send_job_command(
        self, job_id: str, command: str, force: bool = False
    ) -> JobStatus:
        """Send job command.

        Args:
            job_id: The job type ID (e.g., "thumbnailGeneration", "metadataExtraction")
            command: The command to send ("start", "pause", "resume", "empty", "clear-failed")
            force: Whether to force the command

        Returns:
            job status as `JobStatus`
        """
        job_command = JobCommand(command=command, force=force)
        result = await self.api.async_do_request(
            f"jobs/{job_id}", data=job_command.to_dict(), method="PUT"
        )
        assert isinstance(result, dict)
        return JobStatus.from_dict(result)
