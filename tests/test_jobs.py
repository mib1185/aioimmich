"""Tests for aioimmich jobs."""

from __future__ import annotations

from syrupy.assertion import SnapshotAssertion

from aioimmich.jobs.models import ImmichAllJobStatus, ImmichJobStatus


async def test_get_all_jobs_status(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_get_all_jobs_status."""
    api = await mock_immich_with_data()
    jobs_status = await api.jobs.async_get_all_jobs_status()

    assert isinstance(jobs_status, ImmichAllJobStatus)
    assert jobs_status == snapshot


async def test_send_job_command(mock_immich_with_data, snapshot: SnapshotAssertion):
    """Test async_send_job_command."""
    api = await mock_immich_with_data()
    job_status = await api.jobs.async_send_job_command(
        "thumbnailGeneration", "pause", force=True
    )

    assert isinstance(job_status, ImmichJobStatus)
    assert job_status == snapshot
