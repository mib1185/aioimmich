"""aioimmich jobs api."""

from ..api import ImmichSubApi
from .models import ImmichAllJobsStatus, ImmichJobStatus, JobCommand, JobId


class ImmichJobs(ImmichSubApi):
    """Immich jobs api."""

    async def async_get_all_jobs_status(self) -> ImmichAllJobsStatus:
        """Get all jobs status.

        Returns:
            all jobs status as `ImmichJobsStatus`
        """
        result = await self.api.async_do_request("jobs")
        assert isinstance(result, dict)
        return ImmichAllJobsStatus.from_dict(result)

    async def async_send_job_command(
        self, job_id: JobId, command: JobCommand, force: bool = False
    ) -> ImmichJobStatus:
        """Send job command.

        Args:
            job_id: The job type ID
            command: The command to send
            force: Whether to force the command

        Returns:
            job status as `JobStatus`
        """
        result = await self.api.async_do_request(
            f"jobs/{job_id}", data={"command": command, "force": force}, method="PUT"
        )
        assert isinstance(result, dict)
        return ImmichJobStatus.from_dict(result)
